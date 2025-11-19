# Import libraries
from __future__ import annotations

import time
import re
from typing import List, Optional, Tuple, Set
from functools import lru_cache

import requests
import pandas as pd
from bs4 import BeautifulSoup


WIKI_BASE = "https://en.wikipedia.org"


# ------------------------------------------------------------------
# Networking helper
# ------------------------------------------------------------------


def _fetch_soup(url: str) -> Optional[BeautifulSoup]:
    """
    Request a URL and return a BeautifulSoup parser, or None on failure.
    Add User-Agent so Wikipedia doesn't reject.
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        # "From": "youremail@example.com",
        "Accept-Language": "en-US,en;q=0.9",
    }

    try:
        resp = requests.get(url, headers=headers, timeout=10)
    except requests.RequestException as e:
        print("request error:", e, "for", url)
        return None

    if resp.status_code != 200:
        # Keep the noisy line to help diagnose bad lookups quickly
        print("bad status:", resp.status_code, "for", url)
        return None

    return BeautifulSoup(resp.text, "html.parser")


# ------------------------------------------------------------------
# UFC event list + fighter extraction
# ------------------------------------------------------------------


def get_ufc_event_links(limit_events: int | None = None) -> List[str]:
    """
    Grab links to individual UFC event pages from the 'Past events' table
    on https://en.wikipedia.org/wiki/List_of_UFC_events
    """
    url = f"{WIKI_BASE}/wiki/List_of_UFC_events"
    soup = _fetch_soup(url)
    if soup is None:
        return []

    # Page has multiple wikitables.
    # table[0] ~ Upcoming events
    # table[1] ~ Past events
    wikitable_list = soup.find_all("table", class_="wikitable")
    if len(wikitable_list) < 2:
        print("didn't find expected Past events table structure for UFC")
        return []

    past_events_table = wikitable_list[1]
    rows = past_events_table.select("tbody tr")

    event_urls: List[str] = []
    for r in rows[1:]:
        cells = r.find_all("td")
        if len(cells) < 2:
            continue
        link = cells[1].find("a")
        if not link:
            continue
        href = link.get("href", "")
        if href.startswith("/wiki/"):
            event_urls.append(WIKI_BASE + href)

    if limit_events is not None:
        event_urls = event_urls[:limit_events]

    return event_urls


def _extract_fighters_from_event_page(event_url: str) -> Set[str]:
    """
    Given a single UFC/WEC event page URL, pull fighter names from bout tables.

    Heuristic:
    - many event pages have tables where the bout rows look like:
        [Result, Fighter A, 'def.', Fighter B, ...]
      So we take td[1] and td[3] from rows that look like fights.

    We skip things like "def." or "vs." to reduce errors.
    """
    soup = _fetch_soup(event_url)
    if soup is None:
        print("couldn't load event page:", event_url)
        return set()

    fighters: Set[str] = set()

    tables = soup.find_all("table", class_=["wikitable", "toccolours"])
    for table in tables:
        for row in table.find_all("tr"):
            cells = row.find_all("td")

            # skip header-ish rows
            if len(cells) < 5 or any(c.has_attr("colspan") for c in cells):
                continue

            # td[1] ~ fighter A, td[3] ~ fighter B in most UFC/WEC bout tables
            f1 = cells[1].get_text(strip=True)
            f2 = cells[3].get_text(strip=True)

            # basic filters
            if (
                f1
                and f2
                and "def" not in f1.lower()
                and "def" not in f2.lower()
                and "vs." not in f1.lower()
                and "vs." not in f2.lower()
            ):
                fighters.add(f1)
                fighters.add(f2)

    return fighters


def _drop_garbage_names(df: pd.DataFrame, org: str) -> pd.DataFrame:
    """
    Remove rows that are clearly not fighter names
    (venues, event subtitles, etc.).
    """
    bad_entries = [
        "Anthony PettisdefeatsBenson HendersonUFC 164",
        "vs.",
        "Defeated",
        "Defeats",
        "Anderson Silva(UFC Champion)",
        "Antônio Braga NetodefeatsAnthony SmithUFC on Fuel TV: Nogueira vs. Werdum",
        "Antônio Rogério NogueiradefeatsDave HermanUFC 153",
        "Apr 13, 2013",
        "B.J. PenndefeatsJens PulverThe Ultimate Fighter 5 Finale",
        "BMO Harris Bradley Center",
        "BankAtlantic Center",
        "Bankers Life Fieldhouse",
        "Bell Centre",
        "Boardwalk Hall",
        "Brendan SchaubdefeatsMatt MitrioneUFC 165",
        "Bridgestone Arena",
        "Brisbane Entertainment Centre",
        "Bryce Mitchell (FW)",
        "Capital FM Arena",
        "Charles OliveiradefeatsEric WiselyUFC on Fox: Evans vs. Davis",
        "Chris LytledefeatsJason GilliamUFC 73",
        "CotaiArena",
        "Cox Pavilion",
        "Dan Henderson(Pride Champion)",
        "Dec 15, 2012",
        "Dec 8, 2007",
        "Demian MaiadefeatsRick StoryUFC 153",
        "Din ThomasdefeatsJeremy StephensUFC 71",
        "Fabrício WerdumdefeatsAntônio Rogério NogueiraUFC on Fuel TV: Nogueira vs. Werdum",
        "Forrest GriffindefeatsMaurício Rua1UFC 76",
        "Georges St-PierredefeatsMatt Serra2UFC 79",
        "Goiânia Arena",
        "Gold Coast Convention and Exhibition Centre",
        "HP Pavilion",
        "HSBC Arena",
        "Hard Rock Hotel and Casino",
        "Ivan MenjivardefeatsJohn AlbertUFC on Fuel TV: Sanchez vs. Ellenberger",
        "Joe StevensondefeatsMelvin GuillardUFC Fight Night: Stevenson vs. Guillard",
        "John Gunther (LW)",
        "Julija Stoliarenko (WFW)",
        "Jun 1, 2012",
        "Jun 23, 2007",
        "Jun 23, 2012",
        "Jun 8, 2013",
        "Kenny Florian(Tie)Marcus Davis(Tie)",
        "Kenny RobertsondefeatsBrock JardineUFC 157",
        "Leah Letson (WFW)",
        "Luis Peña (LW)",
        "MGM Grand Garden Arena",
        "MTS Centre",
        "Macy Chiasson (WFW)",
        "Manchester Evening News Arena",
        "Mandalay Bay Events Center",
        "Marcus DavisdefeatsPaul TaylorUFC 75",
        "Martin KampmanndefeatsDrew McFedriesUFC 68",
        "Martin KampmanndefeatsThiago AlvesUFC on FX: Alves vs. Kampmann",
        "Matt ArroyodefeatsJohn KolosciThe Ultimate Fighter 6 Finale",
        "Matt WimandefeatsPaul SassUFC on Fuel TV: Struve vs. Miocic",
        "Nate DiazdefeatsJim MillerUFC on Fox: Diaz vs. Miller",
        "Pannie Kianzad (WFW)",
        "Piotr HallmanndefeatsFrancisco TrinaldoUFC Fight Night: Teixeira vs. Bader",
        "Prudential Center",
        "Quinton Jackson(UFC Champion)",
        "Roger HuertadefeatsClay GuidaThe Ultimate Fighter 6 Finale",
        "Ronaldo SouzadefeatsChris CamozziUFC on FX: Belfort vs. Rockhold",
        "Ronda RouseydefeatsLiz CarmoucheUFC 157",
        "Rousimar PalharesdefeatsMike MassenzioUFC 142",
        "Saitama Super Arena",
        "Scotiabank Saddledome",
        "Seminole Hard Rock Hotel and Casino",
        "Sleep Train Arena",
        "Sérgio MoraesdefeatsNeil MagnyUFC 163",
        "TD Garden",
        "TJ WaldburgerdefeatsNick CatoneThe Ultimate Fighter 16 Finale",
        "The Faber Trifecta -Urijah FaberdefeatsIvan MenjivaratUFC 157Scott JorgensenatThe Ultimate Fighter: Team Jones vs. Team Sonnen FinaleMichael McDonaldatUFC on Fox: Johnson vs. Benavidez 2",
        "The Korean ZombiedefeatsDustin PoirierUFC on Fuel TV: The Korean Zombie vs. Poirier",
        "The O2arena",
        "The Odyssey",
        "The Ultimate Fighter: Live Finale",
        "The Ultimate Fighter: Team Carwin vs. Team Nelson Finale",
        "The Ultimate Fighter: Team Couture vs. Team Liddell Finale",
        "The Ultimate Fighter: Team Hughes vs. Team Franklin Finale",
        "The Ultimate Fighter: Team Hughes vs. Team Serra Finale",
        "The Ultimate Fighter: Team Jones vs. Team Sonnen Finale",
        "The Ultimate Fighter: Team Pulver vs. Team Penn Finale",
        "The Ultimate Fighter: Team Rousey vs. Team Tate Finale",
        "U.S. Bank Arena",
        "United Center",
        "WEC 18: Unfinished Business",
        "WEC 26: Condit vs. Alessio",
        "WEC 27: Marshall vs. McElfresh",
        "San Manuel Indian Bingo and Casino",
        "WEC 3: All or Nothing",
        "WEC 21: Tapout",
        "Hard Rock Hotel and Casino",
        "WEC 23: Hot August Fights",
        "WEC 11: Evolution",
        "WEC 25: McCullough vs. Cope",
        "WEC 28: Faber vs. Farrar",
        "WEC 19: Undisputed",
        "WEC 31: Faber vs. Curran",
        "WEC 7: This Time It's Personal",
        "WEC 5: Halloween Havoc",
        "WEC 12: Halloween Fury 3",
        "WEC 29: Condit vs. Larson",
        "WEC 24: Full Force",
        "Tachi Palace Hotel & Casino",
        "WEC 10: Bragging Rights",
        "WEC 6: Return of a Legend",
        "WEC 30: McCullough vs. Crunkilton",
        "WEC 22: The Hitmen",
        "WEC 4: Rumble Under the Sun",
        "WEC 9: Cold Blooded",
        "WEC 20: Cinco de Mayhem",
        "WEC 8: Halloween Fury 2",
        ">170 Ib >77.1 kg",
        ">145 Ib >65.8 kg",
        ">125 Ib >56.7 kg",
        ">135 Ib >61.2 kg",
        ">115 Ib >52.2 kg",
        ">155 Ib >70.3 kg",
        "Any number within parenthesis in a fighter's record symbolizes a no contest",
        ">185 Ib >83.9 kg",
        ">205 Ib >93 kg",
    ]

    out = df.copy()

    # strip numeric-only rows
    out = out[~out["Fighter"].str.strip().str.isnumeric()]

    # strip wiki citation-style rows like "[12]"
    out = out[~out["Fighter"].str.strip().str.match(r"^\[\d+\]$")]

    # strip champ suffixes "(c)" / "(ic)"
    out = out[~out["Fighter"].str.strip().str.endswith("(c)")]
    out = out[~out["Fighter"].str.strip().str.endswith("(ic)")]

    # get rid of bad strings
    out = out[~out["Fighter"].isin(bad_entries)]

    # kill event-title noise: "UFC 189: Mendes vs McGregor"
    out = out[
        ~out["Fighter"].str.contains(
            r"(?i)\bUFC\b|\bFight Night\b|\bThe Ultimate Fighter\b"
        )
    ]

    return out.reset_index(drop=True)


def get_ufc_fighters(limit_events: int | None = None) -> pd.DataFrame:
    """
    Scrape UFC past event pages, pull fighter names, clean obvious junk.
    """
    event_urls = get_ufc_event_links(limit_events=limit_events)
    print("got", len(event_urls), "UFC event URLs")

    all_fighters: Set[str] = set()

    for i, url in enumerate(event_urls):
        print(f"[UFC {i+1}/{len(event_urls)}] {url}")
        names = _extract_fighters_from_event_page(url)
        if names:
            all_fighters.update(names)
        time.sleep(0.5)  # slight delay for each page

    df = pd.DataFrame(sorted(all_fighters), columns=["Fighter"])
    df = _drop_garbage_names(df, org="ufc")
    return df.reset_index(drop=True)


# ------------------------------------------------------------------
# WEC events use the same approach
# ------------------------------------------------------------------


def get_wec_event_links(limit_events: int | None = None) -> List[str]:
    """
    Pull WEC event links from https://en.wikipedia.org/wiki/List_of_WEC_events
    """
    url = f"{WIKI_BASE}/wiki/List_of_WEC_events"
    soup = _fetch_soup(url)
    if soup is None:
        return []

    wikitable_list = soup.find_all("table", class_="wikitable")
    # layout is similar: table[1] is Past events on that page
    past_idx = 1 if len(wikitable_list) > 1 else 0
    past_events_table = wikitable_list[past_idx]

    rows = past_events_table.select("tbody tr")
    event_urls: List[str] = []
    for r in rows[1:]:
        cells = r.find_all("td")
        if len(cells) < 2:
            continue
        link = cells[1].find("a")
        if not link:
            continue
        href = link.get("href", "")
        if href.startswith("/wiki/"):
            event_urls.append(WIKI_BASE + href)

    if limit_events is not None:
        event_urls = event_urls[:limit_events]

    return event_urls


def get_wec_fighters(limit_events: int | None = None) -> pd.DataFrame:
    """
    Scrape WEC past event pages, pull fighter names, remove champion suffixes
    """
    event_urls = get_wec_event_links(limit_events=limit_events)
    print("got", len(event_urls), "WEC event URLs")

    all_fighters: Set[str] = set()

    for i, url in enumerate(event_urls):
        print(f"[WEC {i+1}/{len(event_urls)}] {url}")
        names = _extract_fighters_from_event_page(url)
        if names:
            all_fighters.update(names)
        time.sleep(0.5)

    df = pd.DataFrame(sorted(all_fighters), columns=["Fighter"])

    # WEC pages sometimes add "(c)" / "(ic)" after champ names in the bout table
    df = df[~df["Fighter"].str.strip().str.endswith("(c)")]
    df = df[~df["Fighter"].str.strip().str.endswith("(ic)")]

    df = _drop_garbage_names(df, org="wec")
    return df.reset_index(drop=True)


# ------------------------------------------------------------------
# Simpler org lists (Pride, Strikeforce, Bellator, Invicta, PFL, Rizin)
# These are mostly "alumni" or "current roster" tables where column 2 is a name.
# ------------------------------------------------------------------


def get_pride_fighters() -> pd.DataFrame:
    url = f"{WIKI_BASE}/wiki/List_of_Pride_Fighting_Championships_alumni"
    soup = _fetch_soup(url)
    if soup is None:
        return pd.DataFrame(columns=["Fighter"])

    fighters = set()
    for table in soup.find_all("table", class_="wikitable"):
        for row in table.find_all("tr")[1:]:  # skip header
            cells = row.find_all("td")
            if len(cells) >= 2:
                name = cells[1].get_text(strip=True)
                if name and not name.startswith("["):
                    fighters.add(name)

    df = pd.DataFrame(sorted(fighters), columns=["Fighter"])
    df = df[~df["Fighter"].str.strip().str.match(r"^—$")]
    return df.reset_index(drop=True)


def get_strikeforce_fighters() -> pd.DataFrame:
    url = f"{WIKI_BASE}/wiki/List_of_Strikeforce_alumni"
    soup = _fetch_soup(url)
    if soup is None:
        return pd.DataFrame(columns=["Fighter"])

    fighters = set()
    for table in soup.find_all("table", class_="wikitable"):
        for row in table.find_all("tr")[1:]:
            cells = row.find_all("td")
            if len(cells) >= 2:
                name = cells[1].get_text(strip=True)
                if name and not name.startswith("["):
                    fighters.add(name)

    df = pd.DataFrame(sorted(fighters), columns=["Fighter"])
    df = df[~df["Fighter"].str.strip().str.match(r"^!a$")]
    return df.reset_index(drop=True)


def get_bellator_fighters() -> pd.DataFrame:
    url = f"{WIKI_BASE}/wiki/List_of_Bellator_MMA_alumni"
    soup = _fetch_soup(url)
    if soup is None:
        return pd.DataFrame(columns=["Fighter"])

    fighters = set()
    for table in soup.find_all("table", class_="wikitable"):
        for row in table.find_all("tr")[1:]:
            cells = row.find_all("td")
            if len(cells) >= 2:
                name = cells[1].get_text(" ", strip=True)
                if name and not name.startswith("["):
                    fighters.add(name)

    df = pd.DataFrame(sorted(fighters), columns=["Fighter"])
    df = df[~df["Fighter"].str.strip().str.match(r"^!a$")]
    return df.reset_index(drop=True)


def _scrape_simple_roster(
    url: str,
    suffix_filter: Optional[List[str]] = None,
    bad_values: Optional[List[str]] = None,
) -> pd.DataFrame:
    """
    Helper for Invicta / PFL / Rizin: read roster tables and take fighter name
    from the 2nd <td>. Edit names with "(C)" or "*" suffixes
    """
    soup = _fetch_soup(url)
    if soup is None:
        return pd.DataFrame(columns=["Fighter"])

    fighters = set()
    for table in soup.find_all("table", class_="wikitable"):
        for row in table.find_all("tr")[1:]:
            cells = row.find_all("td")
            if len(cells) >= 2:
                name = cells[1].get_text(" ", strip=True)
                if name and not name.startswith("["):
                    fighters.add(name)

    df = pd.DataFrame(sorted(fighters), columns=["Fighter"])

    if suffix_filter:
        for suffix in suffix_filter:
            df = df[~df["Fighter"].str.strip().str.endswith(suffix)]

    if bad_values:
        df = df[~df["Fighter"].isin(bad_values)]

    return df.reset_index(drop=True)


def get_invicta_fighters() -> pd.DataFrame:
    return _scrape_simple_roster(
        f"{WIKI_BASE}/wiki/List_of_current_Invicta_FC_fighters",
        suffix_filter=["(C)"],
    )


def get_pfl_fighters() -> pd.DataFrame:
    return _scrape_simple_roster(
        f"{WIKI_BASE}/wiki/List_of_current_PFL_fighters",
        suffix_filter=["(C)", "*"],
    )


def get_rizin_fighters() -> pd.DataFrame:
    return _scrape_simple_roster(
        f"{WIKI_BASE}/wiki/List_of_current_Rizin_Fighting_Federation_fighters",
        suffix_filter=["(C)"],
    )


# ------------------------------------------------------------------
# Master fighter list
# ------------------------------------------------------------------


def build_master_fighter_list() -> pd.DataFrame:
    """
    Pull fighters from all orgs, merge, dedupe, normalize a few known aliases.
    Adds `has_wiki_page` by checking common page variants for each name.
    """
    dfs = [
        get_ufc_fighters(),  # UFC events
        get_wec_fighters(),  # WEC events
        get_pride_fighters(),  # Pride alumni
        get_strikeforce_fighters(),  # Strikeforce alumni
        get_bellator_fighters(),  # Bellator alumni
        get_invicta_fighters(),  # Invicta roster
        get_pfl_fighters(),  # PFL roster
        get_rizin_fighters(),  # Rizin roster
    ]

    combined = pd.concat(dfs, ignore_index=True)
    combined = combined.drop_duplicates(subset=["Fighter"]).reset_index(drop=True)

    # normalize some name variants
    replacements = {
        "Bret Cooper": "Brett Cooper",
        "Wágner da Conceição Martins": "Zuluzinho",
        "Abu Azaitar": "Ottman Azaitar",
        "Abusupiyan Magomedov": "Abus Magomedov",
        "Amanda Cooper": "Amanda Brundage",
        "Antonio McKee": "A. J. McKee",
        "King Green": "Bobby Green",
    }
    combined["Fighter"] = combined["Fighter"].replace(replacements)

    # --- Add has_wiki_page (True/False) ---
    combined["has_wiki_page"] = combined["Fighter"].apply(check_has_wiki_page)

    return combined.reset_index(drop=True)


# ------------------------------------------------------------------
# Fighter record scraping (per fighter)
# ------------------------------------------------------------------


def _infer_gender_from_intro(soup: BeautifulSoup) -> Optional[str]:
    """
    Very rough gender guess based on 'he' / 'she' pronoun in the first paragraph.
    """
    first_para = soup.find("p")
    if not first_para:
        return None
    text = first_para.get_text(" ", strip=True).lower()
    if " she " in text:
        return "female"
    if " he " in text:
        return "male"
    return None


def _extract_infobox_info(soup: BeautifulSoup) -> Tuple[Optional[str], Optional[str]]:
    """
    Pull division(s) and weight info from the fighter infobox.
    Returns (divisions, weight_info).
    """
    infobox = soup.find("table", class_="infobox")
    divisions = None
    weight_info = None

    if not infobox:
        return divisions, weight_info

    for row in infobox.find_all("tr"):
        header = row.find("th")
        if not header:
            continue
        label = header.text.strip().lower()
        value_cell = row.find("td")
        if not value_cell:
            continue

        if "division" in label:
            divisions = value_cell.get_text(" / ", strip=True)
        elif "weight" in label and weight_info is None:
            weight_info = value_cell.get_text(" ", strip=True)

    return divisions, weight_info


def _find_mma_record_table(soup: BeautifulSoup) -> Optional[pd.DataFrame]:
    """
    Locate the 'Mixed martial arts record' table on a fighter's page and
    return it as a DataFrame (raw). Returns None if not found.
    """
    all_elements = soup.find_all(["h2", "table"])
    record_table = None

    # Find <h2> "Mixed martial arts record", then first following wikitable
    for i, el in enumerate(all_elements):
        if el.name == "h2" and "Mixed martial arts record" in el.get_text():
            for j in range(i + 1, len(all_elements)):
                nxt = all_elements[j]
                if nxt.name == "table" and "wikitable" in nxt.get("class", []):
                    table_text = nxt.get_text(" ", strip=True)
                    if "Opponent" in table_text and "Method" in table_text:
                        record_table = nxt
                        break
            break

    if record_table is None:
        return None

    rows = record_table.find_all("tr")
    if not rows:
        return None

    headers = [th.get_text(strip=True) for th in rows[0].find_all("th")]
    fight_rows = []
    for row in rows[1:]:
        cells = row.find_all(["td", "th"])
        if len(cells) < 5:
            continue
        fight_rows.append([c.get_text(" ", strip=True) for c in cells])

    if not fight_rows:
        return None

    expected_cols = len(headers)
    norm_rows = []
    for r in fight_rows:
        if len(r) == expected_cols:
            norm_rows.append(r)
        elif len(r) > expected_cols:
            norm_rows.append(r[:expected_cols])
        else:
            norm_rows.append(r + [""] * (expected_cols - len(r)))

    return pd.DataFrame(norm_rows, columns=headers)


def _page_exists(soup: BeautifulSoup | None) -> bool:
    """
    True if the fetched page looks like a real article (not a 'noarticletext' page).
    """
    if soup is None:
        return False
    # Wikipedia shows this box when the page doesn't exist
    if soup.find(id="noarticletext"):
        return False
    # Disambiguation pages usually have this class; treat them as "exists"
    # because they are valid titles and often include links to the correct fighter page.
    # You can change to False if you want to exclude disambiguations.
    return True


@lru_cache(maxsize=20000)
def check_has_wiki_page(name: str) -> bool:
    """
    Check common variants for fighter pages and return True if any exists,
    even if no record table is present. Cached for speed.
    """
    # Try a few frequent disambiguation suffixes in order
    variants = ["", " (fighter)", " (mixed martial artist)", " (kickboxer)"]
    base = name.strip()
    for suffix in variants:
        page_name = f"{base}{suffix}".replace(" ", "_")
        url = f"{WIKI_BASE}/wiki/{page_name}"
        soup = _fetch_soup(url)
        if _page_exists(soup):
            return True
        # small politeness delay to avoid hammering on repeated misses
        time.sleep(0.05)
    return False


def _scrape_single_fighter_page(
    name: str,
    variant_suffix: str = "",
) -> Optional[pd.DataFrame]:
    """
    Try to scrape a single fighter wiki page.
    Try plain name, then ' (fighter)', then ' (kickboxer)' which can happen due to people with the same name
    """
    page_name = f"{name}{variant_suffix}".replace(" ", "_")
    url = f"{WIKI_BASE}/wiki/{page_name}"

    soup = _fetch_soup(url)
    if soup is None:
        return None

    gender = _infer_gender_from_intro(soup)
    divisions, weight_info = _extract_infobox_info(soup)
    record_df = _find_mma_record_table(soup)
    if record_df is None:
        return None

    record_df.insert(0, "Fighter", name)
    record_df["has_wiki_page"] = True
    record_df["Division"] = divisions
    record_df["Weight Info"] = weight_info
    record_df["Gender"] = gender

    return record_df


def scrape_fighter_record(name: str) -> Optional[pd.DataFrame]:
    df = _scrape_single_fighter_page(name)
    if df is not None:
        return df

    df = _scrape_single_fighter_page(name, " (fighter)")
    if df is not None:
        return df

    df = _scrape_single_fighter_page(name, " (kickboxer)")
    return df


def scrape_all_fighters(
    fighter_df: pd.DataFrame, sleep_seconds: float = 1.0
) -> pd.DataFrame:
    """
    Given a DataFrame with a 'Fighter' column,
    scrape each fighter's "Mixed martial arts record" table and stack them.
    """
    records = []
    failed = []

    for idx, name in enumerate(fighter_df["Fighter"]):
        print(f"[{idx+1}/{len(fighter_df)}] {name} ...")
        result = scrape_fighter_record(name)
        if result is not None:
            records.append(result)
        else:
            failed.append(name)

        if sleep_seconds:
            time.sleep(sleep_seconds)

    if failed:
        print(
            f"WARNING: failed to scrape {len(failed)} fighters (sample: {failed[:5]})"
        )

    if not records:
        return pd.DataFrame()

    return pd.concat(records, ignore_index=True)
