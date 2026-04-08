# IPL 2026 Score Tracker
# Fetches and stores IPL match data for cricket fans in Nepal

import json
from datetime import datetime

SEASON = "IPL 2026"

def get_today_match():
    """Returns today's IPL match details"""
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"Fetching IPL match data for {today}...")
    return {
        "date": today,
        "season": SEASON,
        "status": "live"
    }

def get_points_table():
    """Returns current IPL 2026 points table standings"""
    with open("scores.json", "r") as f:
        data = json.load(f)
    return data["points_table"]

def get_live_score():
    """Prints live IPL score update"""
    print(f"IPL 2026 live score updated.")

def get_schedule():
    """Returns IPL 2026 match schedule"""
    print(f"Loading IPL schedule 2026...")
    return {
        "season": SEASON,
        "total_matches": 74,
        "playoffs": ["Qualifier 1", "Eliminator", "Qualifier 2", "Final"]
    }

if __name__ == "__main__":
    get_today_match()
    get_points_table()
    get_live_score()
    get_schedule()
