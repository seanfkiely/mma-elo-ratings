# MMA Elo Ratings

A complete pipeline for scraping, cleaning, and modeling MMA fight data to generate dynamic Elo ratings for thousands of fighters across organizations and eras. This project produces fighter-level summaries, rating trajectories, and leaderboards while allowing full customization of Elo parameters such as rating decay, finish/championship bonuses, informative priors, and opponent reliability adjustments.

---

## Overview

This repository implements an extensible Elo rating system tailored for mixed martial arts. It consists of three main components:

1. **Data Collection** – Scrapes event results and fighter pages from Wikipedia.
2. **Data Cleaning** – Standardizes fighter names, outcomes, dates, event names, and weight classes.
3. **Elo Modeling** – Computes pre- and post-fight ratings with adjustments for opponent quality, inactivity, finishes, and title bouts.

The result is a fully reproducible process that produces detailed fighter-level analytics and is suitable for downstream visualization, reporting, or prediction tasks.

---

## Features

- Automated scraping of MMA fighters and their complete bout histories  
- Unified dataset across MMA organizations including UFC, Pride, Bellator, WEC, Strikeforce, and others  
- Robust cleaning rules to fix missing/incorrect events, dates, outcomes, and weight classes  
- Elo model supporting:
  - Opponent reliability scaling  
  - Title fight bonuses  
  - Finish bonuses  
  - Inactivity decay via half-life  
  - Informative priors for baselines elo values 
- Outputs:
  - Fighter-level summaries (wins, losses, win rate, current Elo, peak Elo, average Elo)  
  - Peak Elo leaderboards  
  - Rating distributions and comparative metrics
  - Legacy Scores   
- Reproducible code and modular functions for expanding the system

---

## Quick Start

### Installation

Clone the repository:

```
git clone https://github.com/seanfkiely/mma-elo-ratings.git
cd mma-elo-ratings
pip install -r requirements.txt
```

## Basic Usage
### Scrape fighters and fights
First, use notebook 01_scrape_and_clean_fights if you would like to scrape the most recent fights. Alternatively you can use the accompanying CSV file.
from src.scraper import build_master_fighter_list, scrape_fighter_records

Second, if you'd like to make any changes to the ELO modeling you can do so in 02_build_elo_ratings. You can do so by simply changing the parameters here:

```
# 7) Run Elo
elo_logs = run_elo(
    bouts=bouts,
    career_counts=career_counts, 
    k=60,
    half_life_days=1825,
    floor=1500,
    bonus_finish=2,
    bonus_high_tier_title=6,
    bonus_low_tier_title=2,
    grace_days=270,
    min_reliable_fights=5
)
```

Third, create tables or figures in 03_tablesand_figures such as:
```
#Plot Elo Rating with Win Rates
# Create win rates
elo_df = elo_df.sort_values(['fighter', 'date'])

fighter_stats = elo_df.groupby('fighter').agg(
    wins=('result', lambda x: (x == 'win').sum()),
    total=('result', 'count')
)
fighter_stats['win_rate'] = fighter_stats['wins'] / fighter_stats['total']

# Merge with Elo
fighter_stats = fighter_stats.merge(final_elos, left_index=True, right_index=True)

# Scatterplot
import seaborn as sns

# Fighters you want to label (use exact names from your dataset)
highlighted = ['Anderson Silva', 'Demetrious Johnson', 'Clay Guida', 'Conor McGregor', 'Bob Sapp', 'Brock Lesnar', 'Dada 5000', 'Ilia Topuria', 'CM Punk', 'Islam Makhachev', 'Ken Shamrock']

for name in highlighted:
    if name in fighter_stats.index:
        row = fighter_stats.loc[name]
        plt.text(row['win_rate'], row['current_elo'], name, fontsize=6, weight='semibold')

sns.scatterplot(data=fighter_stats, x='win_rate', y='current_elo', alpha=0.6)
plt.title("Current Elo Rating vs. Win Rate")
plt.xlabel("Win Rate")
plt.ylabel("Current Elo Rating")
plt.savefig("../outputs/figures/elo_vs_win_rate.png")
plt.show()
```

## Methodology 

Traditional Elo systems update a competitor’s rating based on expected vs. actual outcomes. For MMA I introduce several domain-specific modifications to account for infrequent "games" (relative to say, chess), stat-padding, "ducking", etc.

This project includes options for:

- Opponent reliability weighting: Updates are scaled by the number of fights a competitor has completed, reducing the volatility created by inexperienced fighters.

- Inactivity decay: Fighter ratings gradually regress toward a baseline rating after long layoffs, controlled by a half-life parameter.

- Finish bonuses: Knockouts and submissions receive additional Elo credit relative to decisions.

- Title fight bonuses: Championship-level bouts carry increased rating stakes. Championship fights are tiered by organization.

- Baselines ratings using informative priors: Competitors with no records or limited fights are anchored at a lower starting value to prevent artificial inflation (stat-padding against lower quality opponents).

Together, these adjustments produce a more stable and realistic model of MMA skill progression over time.


## Repository Structure
```
/src
    scraper.py            # Scrapes fighters and bout data from Wikipedia
    parse_fights.py       # Data cleaning utilities
    __init__.py        

/notebooks
    01_scrape_and_clean_fights    # Runs scraper.py and parse_fights.py
    02_build_elo_ratings          # Create ELO ratings
    03_tables_and_figures         # Create visuals
    04_goat_metrics               # Create metrics for best fighters of all time

/data
    raw/                  # Raw scraped bout data
    processed/            # Cleaned bout and fighter datasets

/outputs
    figures/              # Plots and visualizations
    tables/               # Markdown tables (e.g., top fighters)

README.md
```

## Example Figure
<p align="center">
  <img src="https://seanfkiely.github.io/images/elo_vs_win_rate.png" width="600">
</p>


## Example Table
<div align = "center">

***Table 1. Greatest Fights by ELO Rating***

|   Rank | Fighter 1             |   ELO Rating 1 | Fighter 2         |   ELO Rating 2 |   Combined ELO Rating |
|-------:|:----------------------|---------------:|:------------------|---------------:|----------------------:|
|      1 | Daniel Cormier        |        2053.23 | Stipe Miocic      |        1890.61 |               3943.84 |
|      2 | Stipe Miocic          |        1935.6  | Daniel Cormier    |        2002.63 |               3938.24 |
|      3 | Stipe Miocic          |        1926.22 | Daniel Cormier    |        1992.24 |               3918.46 |
|      4 | Jake Shields          |        1894.11 | Georges St-Pierre |        1997.36 |               3891.48 |
|      5 | Chael Sonnen          |        1845.49 | Anderson Silva    |        2045.23 |               3890.71 |
|      6 | Alexander Volkanovski |        1950.65 | Islam Makhachev   |        1933.72 |               3884.38 |
|      7 | Jon Jones             |        1994.77 | Daniel Cormier    |        1888.75 |               3883.52 |
|      8 | Dustin Poirier        |        1898.04 | Islam Makhachev   |        1973.18 |               3871.22 |
|      9 | Daniel Cormier        |        1956.09 | Anthony Johnson   |        1912.28 |               3868.37 |
|     10 | Andrei Arlovski       |        1813.39 | Fedor Emelianenko |        2051.75 |               3865.14
</div>

## Full Write-Up

For a more complete write-up of the methodology, extended results, and analysis commentary, see 
[my website](https://seanfkiely.github.io/side-projects/mma_elo_ratings/).

## License

This project is released under the MIT License.

## Contact

If you have questions or suggestions, feel free to open an issue or reach out directly at [seanfkiely4[at]gmail.com](mailto:seanfkiely4@gmail.com).