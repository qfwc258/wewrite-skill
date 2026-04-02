#!/usr/bin/env python3
import argparse
import json

def fetch_stats(client, days=7):
    """获取文章统计数据"""
    return []

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--client', required=True)
    parser.add_argument('--days', type=int, default=7)
    args = parser.parse_args()
    
    stats = fetch_stats(args.client, args.days)
    print(json.dumps(stats, ensure_ascii=False, indent=2))