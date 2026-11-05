import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

all_videos = []
seen_ids = set()

def load_file(filepath, enc='utf-8'):
    for e in [enc, 'utf-16', 'utf-8']:
        try:
            with open(filepath, 'r', encoding=e) as f:
                return json.load(f)
        except Exception:
            continue
    return {}

for fpath in ['raw-dropship.json', 'raw-dropship-2.json']:
    d = load_file(fpath)
    videos = d.get('output', {}).get('videos', [])
    for item in videos:
        v = item.get('aweme_info', item)
        item_id = str(v.get('aweme_id') or v.get('id') or '')
        if not item_id or item_id in seen_ids:
            continue
        seen_ids.add(item_id)
        
        desc = v.get('desc') or ''
        author = v.get('author', {})
        nickname = author.get('nickname', '')
        unique_id = author.get('unique_id', '')
        stats = v.get('statistics', {})
        digg = stats.get('digg_count', 0)
        play = stats.get('play_count', 0)
        share = stats.get('share_count', 0)
        comment = stats.get('comment_count', 0)
        
        url = f"https://www.tiktok.com/@{unique_id}/video/{item_id}" if unique_id and item_id else ""
        
        all_videos.append({
            'id': item_id,
            'author': nickname,
            'handle': unique_id,
            'url': url,
            'desc': desc.replace('\n', ' ').strip(),
            'likes': digg,
            'views': play,
            'shares': share,
            'comments': comment
        })

all_videos.sort(key=lambda x: x['likes'], reverse=True)

with open('dropship-tiktok-results.json', 'w', encoding='utf-8') as f:
    json.dump(all_videos, f, ensure_ascii=False, indent=2)

print(f"Total unique videos extracted: {len(all_videos)}\n")
for i, v in enumerate(all_videos[:12]):
    print(f"#{i+1} | {v['likes']:,} likes | {v['views']:,} vues | @{v['handle']} ({v['author']})")
    print(f"   Desc: {v['desc']}")
    print(f"   Link: {v['url']}\n")
