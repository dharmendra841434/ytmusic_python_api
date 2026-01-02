from ytmusicapi import YTMusic
yt = YTMusic()
charts = yt.get_charts('IN')
print("Keys:", list(charts.keys()))
for key in charts:
    if isinstance(charts[key], dict):
        print(f"Sub-keys for {key}:", list(charts[key].keys()))
