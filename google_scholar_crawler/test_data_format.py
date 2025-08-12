#!/usr/bin/env python3
"""
测试Google Scholar数据格式的脚本
用于检查数据结构和paper ID
"""

import json
import os
import sys
from datetime import datetime

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
        
        print("\n=== 论文列表（按引用数排序）===")
        publications = data.get('publications', {})
        if not publications:
            print("没有找到论文数据")
            return 0
        
        # 按引用数排序
        sorted_pubs = sorted(
            publications.items(),
            key=lambda x: x[1].get('num_citations', 0),
            reverse=True
        )
        
        for i, (pub_id, pub_data) in enumerate(sorted_pubs, 1):
            title = pub_data.get('bib', {}).get('title', 'Unknown Title')
            citations = pub_data.get('num_citations', 0)
            year = pub_data.get('bib', {}).get('pub_year', 'Unknown Year')
            url = pub_data.get('pub_url') or pub_data.get('eprint_url', 'No URL')
            
            print(f"{i}. ID: {pub_id}")
            print(f"   标题: {title}")
            print(f"   年份: {year}")
            print(f"   引用: {citations}")
            print(f"   链接: {url}")
            print()
        
        print("=== 数据结构分析 ===")
        print(f"论文总数: {len(publications)}")
        
        # 检查数据结构
        if publications:
            sample_pub = next(iter(publications.values()))
            print(f"示例论文数据结构:")
            print(json.dumps(sample_pub, indent=2, ensure_ascii=False))
        
        print("\n=== 建议的HTML元素 ===")
        print("在about.md中使用以下格式:")
        for i, (pub_id, pub_data) in enumerate(sorted_pubs[:5], 1):  # 只显示前5篇
            title = pub_data.get('bib', {}).get('title', 'Unknown Title')
            print(f'<span class="show_paper_citations" data="{pub_id}">Loading...</span>')
        
        print("\n=== 动态显示建议 ===")
        print("推荐使用动态显示系统，它会自动:")
        print("1. 按引用数排序论文")
        print("2. 显示论文标题、年份和引用数")
        print("3. 提供论文链接")
        print("4. 自动处理错误情况")
        
        return 0
        
    except Exception as e:
        print(f"错误: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(test_data_format())
