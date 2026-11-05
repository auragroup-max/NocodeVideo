import json, sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\No Code Video\tiktok-results.json', 'r', encoding='utf-8') as f:
    videos = json.load(f)

for i, v in enumerate(videos[:12]):
    print(f"#{i+1}: {v['likes']} likes | {v['plays']} vues | {v['handle']} ({v['nickname']})")
    print(f"     Description: {v['desc']}")
    print(f"     Lien: {v['url']}")
    print("-" * 60)
