#!/usr/bin/env python3
import argparse

def learn_edits(client, draft, final):
    """学习编辑差异"""
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--client', required=True)
    parser.add_argument('--draft', required=True)
    parser.add_argument('--final', required=True)
    args = parser.parse_args()
    
    learn_edits(args.client, args.draft, args.final)