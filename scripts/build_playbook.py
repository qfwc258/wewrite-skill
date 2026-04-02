#!/usr/bin/env python3
import argparse
import json

def build_playbook(client):
    """从历史文章生成playbook"""
    return {'rules': []}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--client', required=True)
    args = parser.parse_args()
    
    playbook = build_playbook(args.client)
    print(json.dumps(playbook, ensure_ascii=False, indent=2))