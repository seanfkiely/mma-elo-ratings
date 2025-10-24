# MMA ELO Rating System
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import requests
from bs4 import BeautifulSoup

def get_ufc_event_links():
    url = "https://en.wikipedia.org/wiki/List_of_UFC_events"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to load event list.")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("table.wikitable tbody tr td:nth-child(2) a")  # 2nd column = event link

    event_urls = []
    for link in links:
        href = link.get("href", "")
        if href.startswith("/wiki/UFC"):
            event_urls.append("https://en.wikipedia.org" + href)

    return event_urls

# Example usage:
event_urls = get_ufc_event_links()
print(f"Found {len(event_urls)} events.")
print(event_urls[:5])  # Show first 5


# def scrape_mma_fight_history(name: str):
#     # Build Wikipedia URL
#     fighter_name = name.replace(" ", "_")
#     url = f"https://en.wikipedia.org/wiki/{fighter_name}"

#     # Fetch the page
#     response = requests.get(url)
#     if response.status_code != 200:
#         print(f"Failed to load page for {name}")
#         return None

#     soup = BeautifulSoup(response.text, "html.parser")

#     # Find all headers and tables in page
#     all_elements = soup.find_all(["h2", "table"])

#     fight_table = None

#     # Look for the 'Mixed martial arts record' heading
#     for i, element in enumerate(all_elements):
#         if element.name == "h2" and "Mixed martial arts record" in element.text:
#             # After finding the MMA section, search for the correct table
#             for j in range(i + 1, len(all_elements)):
#                 if all_elements[j].name == "table" and "wikitable" in all_elements[j].get("class", []):
#                     candidate = all_elements[j]
#                     if "Opponent" in candidate.text and "Method" in candidate.text:
#                         fight_table = candidate
#                         break
#             break  # stop once found

#     if fight_table is None:
#         print(f"No MMA fight table found for {name}")
#         return None

#     # Parse the fight table
#     rows = fight_table.find_all("tr")
#     headers = [th.text.strip() for th in rows[0].find_all("th")]
#     fight_data = []

#     for row in rows[1:]:
#         cells = row.find_all(["td", "th"])
#         if len(cells) < 5:
#             continue  # Skip incomplete rows
#         fight_data.append([cell.text.strip() for cell in cells])

#     # Check if we actually collected any fights
#     if not fight_data:
#         print("Table found but no valid fight rows were parsed.")
#         return None

#     # Create the DataFrame
#     df = pd.DataFrame(fight_data, columns=headers[:len(fight_data[0])])
#     return df

# # ----------------------------

# # Example usage: Benson Henderson
# benson_df = scrape_mma_fight_history("Benson Henderson")

# if benson_df is not None:
#     print(benson_df.head())
#     benson_df.to_csv("benson_henderson_mma.csv", index=False)
#     print("Saved to benson_henderson_mma.csv")
# else:
#     print("Failed to scrape Benson Henderson's MMA record.")

#df = pd.read_csv("gsp_fight_history.csv")
#print(df.head())