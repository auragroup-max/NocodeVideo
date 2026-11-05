import json

log_path = r'C:\Users\2em Entreprise\.gemini\antigravity\brain\dbe29b29-d902-44e4-bdde-bd19c9553aaf\.system_generated\tasks\task-315.log'

with open(log_path, 'r', encoding='utf-8', errors='replace') as f:
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
    elif "data" in data:
        items = data["data"]
        
    print(f"Total items found: {len(items)}")
    
    parsed = []
    for it in items:
        aweme = it.get("aweme_info") or it
        desc = aweme.get("desc") or aweme.get("title") or ""
        author_info = aweme.get("author") or {}
        nickname = author_info.get("nickname") or ""
        unique_id = author_info.get("unique_id") or ""
        stats = aweme.get("statistics") or {}
        plays = stats.get("play_count", 0)
        likes = stats.get("digg_count", 0)
        shares = stats.get("share_count", 0)
        comments = stats.get("comment_count", 0)
        aweme_id = aweme.get("aweme_id") or aweme.get("id") or ""
        video_obj = aweme.get("video") or {}
        duration = video_obj.get("duration", 0)
        
        parsed.append({
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
    
    # Sort by likes descending
    parsed.sort(key=lambda x: x["likes"], reverse=True)
    
    with open(r'd:\No Code Video\tiktok-results.json', 'w', encoding='utf-8') as out_f:
        json.dump(parsed, out_f, ensure_ascii=False, indent=2)
    print("Saved", len(parsed), "videos sorted by likes.")
