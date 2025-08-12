#!/usr/bin/env python3
"""
测试Google Scholar数据格式的脚本
用于检查数据结构和paper ID
"""

import json
import os
import sys

def test_data_format():
    """测试数据格式"""
    results_dir = "results"
    data_file = os.path.join(results_dir, "gs_data.json")
    
    if not os.path.exists(data_file):
        print(f"错误: 数据文件不存在: {data_file}")
        print("请先运行 main.py 生成数据")
        return 1
    
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print("=== Google Scholar 数据格式检查 ===")
        print(f"总引用数: {data.get('citedby', 'N/A')}")
        print(f"h-index: {data.get('hindex', 'N/A')}")
        print(f"i10-index: {data.get('i10index', 'N/A')}")
        print(f"更新时间: {data.get('updated', 'N/A')}")
        
        print("\n=== 论文列表 ===")
        publications = data.get('publications', {})
        if not publications:
            print("没有找到论文数据")
            return 0
        
        for i, (pub_id, pub_data) in enumerate(publications.items(), 1):
            title = pub_data.get('bib', {}).get('title', 'Unknown Title')
            citations = pub_data.get('num_citations', 0)
            year = pub_data.get('bib', {}).get('pub_year', 'Unknown Year')
            
            print(f"{i}. ID: {pub_id}")
            print(f"   标题: {title}")
            print(f"   年份: {year}")
            print(f"   引用: {citations}")
            print()
        
        print("=== 建议的HTML元素 ===")
        print("在about.md中使用以下格式:")
        for i, (pub_id, pub_data) in enumerate(publications.items(), 1):
            title = pub_data.get('bib', {}).get('title', 'Unknown Title')
            print(f'<span class="show_paper_citations" data="{pub_id}">Loading...</span>')
        
        return 0
        
    except Exception as e:
        print(f"错误: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(test_data_format())
