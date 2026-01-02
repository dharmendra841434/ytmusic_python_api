from ytmusicapi import YTMusic
import json

def inspect_charts():
    yt = YTMusic()
    charts = yt.get_charts(country='IN')
    # Use only first few items to avoid giant output
    subset = {k: v for k, v in charts.items() if k != 'countries'}
    print(json.dumps(subset, indent=2)[:2000])

if __name__ == "__main__":
    inspect_charts()
