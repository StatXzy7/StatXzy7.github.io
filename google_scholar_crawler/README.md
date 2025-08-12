# Google Scholar 爬虫

这个爬虫用于自动获取Google Scholar的引用数据，并更新到GitHub仓库中。

## 功能特性

- 自动获取Google Scholar作者信息
- 支持超时控制，避免长时间挂起
- 可选的SerpAPI支持，提高稳定性
- 自动提交结果到GitHub分支
- 动态显示引用数据在网页中

## 运行频率

### 自动运行
- **每周一上午8点** - 自动更新引用数据
- **每月1号上午8点** - 备用更新（手动触发工作流）

### 手动触发
如果需要立即更新数据，可以手动触发：
1. 进入GitHub仓库的Actions页面
2. 选择"Get Citation Data (Manual)"工作流
3. 点击"Run workflow"按钮

## 环境变量

- `GOOGLE_SCHOLAR_ID`: 你的Google Scholar ID（必需）
- `SERPAPI_API_KEY`: SerpAPI密钥（可选，但推荐使用）
- `SCHOLAR_TIMEOUT_SECONDS`: 脚本超时时间，默认600秒（10分钟）

## 在网页中显示引用数据

### 方法1: 动态显示系统（推荐）

新的动态显示系统会自动：
- 按引用数排序论文
- 显示论文标题、年份和引用数
- 提供论文链接
- 自动处理错误情况

在 `_pages/about.md` 中添加：
```markdown
# Google Scholar Statistics

<!-- Google Scholar徽章 -->
<p>
  <img 
    alt="Google Scholar Citations"
    src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/StatXzy7/StatXzy7.github.io/google-scholar-stats/gs_data_shieldsio.json">
</p>

<!-- 动态Google Scholar数据显示 -->
<div id="google-scholar-stats">
  <p><strong>Total Citations: <span id="total_cit">Loading...</span></strong></p>
  <p><strong>h-index: <span id="h_index">Loading...</span></strong> | <strong>i10-index: <span id="i10_index">Loading...</span></strong></p>
</div>

<!-- 动态论文引用显示 -->
<div id="dynamic-publications">
  <h3>Publications with Citations</h3>
  <div id="publications-list">
    <!-- 这里会被JavaScript动态填充 -->
  </div>
</div>
```

### 方法2: 手动指定论文（传统方式）

如果需要手动指定特定论文：

1. **获取正确的paper_id**
   ```bash
   cd google_scholar_crawler
   python test_data_format.py
   ```

2. **在HTML中添加**
   ```html
   <span id="total_cit">Loading...</span>
   <span class="show_paper_citations" data="实际的paper_id">Loading...</span>
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

## 频率调整说明

为了减少失败邮件，已将运行频率从：
- **每天运行** → **每周一运行**
- **移除page_build触发** → 避免每次提交都触发
- **添加手动触发选项** → 需要时可立即更新

这样可以大大减少失败邮件的频率，同时保持数据的相对新鲜度。
