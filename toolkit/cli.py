#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='Markdown file')
    parser.add_argument('--cover', help='Cover image')
    parser.add_argument('--theme', default='xiaochchen')
    parser.add_argument('--title', help='Article title')
    
    args = parser.parse_args()
    print(f'Publishing: {args.file}')

if __name__ == '__main__':
    main()