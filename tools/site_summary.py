# tools/site_summary.py
import json
from datetime import datetime

SITE_DATA = {
    "name": "爱游戏",
    "url": "https://i-game-site.com.cn",
    "tags": ["游戏资讯", "玩家社区", "攻略分享"],
    "description": "提供最新游戏动态、深度评测与玩家互动交流的综合游戏平台。",
    "keywords": ["爱游戏", "游戏攻略", "游戏评测", "玩家社区", "游戏资讯"]
}

def format_summary(data: dict) -> str:
    lines = []
    lines.append("=" * 48)
    lines.append(f"站点摘要: {data['name']}")
    lines.append("=" * 48)
    lines.append(f"URL:  {data['url']}")
    lines.append(f"关键词: {', '.join(data['keywords'])}")
    lines.append(f"标签: {', '.join(data['tags'])}")
    lines.append(f"说明: {data['description']}")
    lines.append("-" * 48)
    lines.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 48)
    return "\n".join(lines)

def summary_to_dict(data: dict) -> dict:
    return {
        "name": data["name"],
        "url": data["url"],
        "keywords": data["keywords"],
        "tags": data["tags"],
        "description": data["description"],
        "generated_at": datetime.now().isoformat()
    }

def save_summary_json(data: dict, filepath: str = "site_summary.json") -> None:
    summary = summary_to_dict(data)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"JSON summary saved to {filepath}")

def main():
    text = format_summary(SITE_DATA)
    print(text)
    save_summary_json(SITE_DATA)

if __name__ == "__main__":
    main()