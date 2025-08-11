# src/soccer_scrape.py
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path

URL = "https://www.vegasinsider.com/soccer/odds/las-vegas/"  # try this first

def fetch_html(url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, timeout=20)
    r.raise_for_status()
    return r.text

def parse_with_read_html(html: str) -> pd.DataFrame | None:
    try:
        tables = pd.read_html(html)
        if not tables:
            return None
        # pick the largest table (often the odds grid)
        return max(tables, key=lambda t: t.shape[0] * t.shape[1])
    except ValueError:
        return None

def parse_with_bs4(html: str) -> pd.DataFrame | None:
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")
    if not table:
        return None
    rows = []
    for tr in table.find_all("tr"):
        cells = [c.get_text(strip=True) for c in tr.find_all(["th","td"])]
        if cells:
            rows.append(cells)
    if len(rows) < 2:
        return None
    header, body = rows[0], rows[1:]
    # ensure unique column names if site repeats headers
    seen, cols = set(), []
    for h in header:
        h2 = h or "col"
        while h2 in seen:
            h2 += "_dup"
        seen.add(h2)
        cols.append(h2)
    df = pd.DataFrame(body, columns=cols)
    return df

def main():
    html = fetch_html(URL)
    df = parse_with_read_html(html) or parse_with_bs4(html)
    if df is None or df.empty:
        print("❌ Could not parse any table. The page may be JS-rendered or layout changed.")
        return

    # add a timestamp and source to help you later when merging multiple sources
    df["scraped_at"] = datetime.utcnow().isoformat(timespec="seconds") + "Z"
    df["source_url"] = URL

    # make sure data/ exists
    Path("data").mkdir(parents=True, exist_ok=True)

    stamp = datetime.utcnow().strftime("%Y%m%d")
    outpath = Path("data") / f"soccer_odds_raw_{stamp}.csv"
    df.to_csv(outpath, index=False)
    print(f"✅ Saved {outpath} with shape {df.shape}")

if __name__ == "__main__":
    main()