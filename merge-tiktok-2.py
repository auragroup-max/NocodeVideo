import json

with open(r'd:\No Code Video\raw-tiktok-2.json', 'r', encoding='utf-16', errors='replace') as f:
    text = f.read()

start_idx = text.find('{')
end_idx = text.rfind('}')

if start_idx != -1 and end_idx != -1:
    raw_json = text[start_idx:end_idx+1]
    data = json.loads(raw_json)
    
    items = []
    if "output" in data and isinstance(data["output"], dict):
        out = data["output"]
        if "videos" in out:
            items = out["videos"]
        elif "data" in out:
            items = out["data"]
    elif "videos" in data:
        items = data["videos"]
        
    print(f"Items in search 2: {len(items)}")
    
    # Load previous results
    with open(r'd:\No Code Video\tiktok-results.json', 'r', encoding='utf-8') as f_prev:
        all_videos = json.load(f_prev)
    
    seen_ids = set(v["id"] for v in all_videos if v.get("id"))
    
    added = 0
    for it in items:
        aweme = it.get("aweme_info") or it
        aweme_id = aweme.get("aweme_id") or aweme.get("id") or ""
        if aweme_id in seen_ids:
            continue
        seen_ids.add(aweme_id)
        
        desc = aweme.get("desc") or aweme.get("title") or ""
        author_info = aweme.get("author") or {}
        nickname = author_info.get("nickname") or ""
        unique_id = author_info.get("unique_id") or ""
        stats = aweme.get("statistics") or {}
        plays = stats.get("play_count", 0)
        likes = stats.get("digg_count", 0)
        shares = stats.get("share_count", 0)
        comments = stats.get("comment_count", 0)
        video_obj = aweme.get("video") or {}
        duration = video_obj.get("duration", 0)
        
        all_videos.append({
            "nickname": nickname,
            "handle": f"@{unique_id}",
            "desc": desc,
            "plays": plays,
            "likes": likes,
            "shares": shares,
            "comments": comments,
            "duration_s": duration / 1000 if duration > 1000 else duration,
            "id": aweme_id,
            "url": f"https://www.tiktok.com/@{unique_id}/video/{aweme_id}" if aweme_id and unique_id else ""
        })
        added += 1
        
    all_videos.sort(key=lambda x: x["likes"], reverse=True)
    with open(r'd:\No Code Video\tiktok-results.json', 'w', encoding='utf-8') as f_out:
        json.dump(all_videos, f_out, ensure_ascii=False, indent=2)
        
    print(f"Added {added} new videos. Total now: {len(all_videos)}")
