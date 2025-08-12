# Google Scholar 爬虫

这个爬虫用于自动获取Google Scholar的引用数据，并更新到GitHub仓库中。

## 功能特性

- 自动获取Google Scholar作者信息
- 支持超时控制，避免长时间挂起
- 可选的SerpAPI支持，提高稳定性
- 自动提交结果到GitHub分支
- 在网页中显示引用数据

## 环境变量

- `GOOGLE_SCHOLAR_ID`: 你的Google Scholar ID（必需）
- `SERPAPI_API_KEY`: SerpAPI密钥（可选，但推荐使用）
- `SCHOLAR_TIMEOUT_SECONDS`: 脚本超时时间，默认600秒（10分钟）

## 在网页中显示引用数据

### 1. 总引用数显示
在HTML中添加：
```html
<span id="total_cit">Loading...</span>
```

### 2. 论文引用数显示
在HTML中添加：
```html
<span class="show_paper_citations" data="paper_id">Loading...</span>
```

### 3. 获取正确的paper_id
运行测试脚本查看数据格式：
```bash
cd google_scholar_crawler
python test_data_format.py
```

### 4. 示例用法
在 `_pages/about.md` 中：
```markdown
**Total Citations: <span id="total_cit">Loading...</span>**

- PTransIPs: <span class="show_paper_citations" data="实际的paper_id">Loading...</span>
```

## 解决超时问题

如果你遇到6小时超时问题，可以尝试以下解决方案：

### 1. 使用SerpAPI（推荐）
在GitHub Secrets中添加`SERPAPI_API_KEY`：
1. 注册 [SerpAPI](https://serpapi.com/)
2. 获取API密钥
3. 在GitHub仓库设置中添加Secret：`SERPAPI_API_KEY`

### 2. 调整超时设置
- 工作流超时：30分钟（已在配置中设置）
- 脚本超时：10分钟（可通过环境变量调整）

### 3. 手动运行测试
```bash
cd google_scholar_crawler
pip install -r requirements.txt
export GOOGLE_SCHOLAR_ID="你的ID"
export SCHOLAR_TIMEOUT_SECONDS=300
python main.py
```

## 故障排除

如果仍然遇到问题：
1. 检查网络连接
2. 确认Google Scholar ID正确
3. 考虑使用代理或VPN
4. 检查GitHub Actions日志获取详细错误信息
5. 运行 `python test_data_format.py` 检查数据格式

## 定时运行

当前设置为每天上午8点运行。可以在`.github/workflows/google_scholar_crawler.yaml`中修改cron表达式。
