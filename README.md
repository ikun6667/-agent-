# -agent-
由helloagent框架搭建自动规划旅游路线的agent
基于阿里云通义千问 + 高德地图 MCP 工具实现的 AI 自动旅行规划助手
✨ 功能介绍
智能景点搜索（高德地图真实数据）
自动查询目的地未来几天天气
酒店智能推荐（按位置、价格、舒适度）
3 日 / 多日行程自动规划
输出干净无符号文本，直接可用
支持景点、美食、人文、自然等偏好
🚀 技术栈
Python 3.10+
阿里云百炼通义千问 LLM（qwen3.6-flash）
高德地图 MCP 工具（amap-mcp-server）
hello_agents 多智能体框架
Pydantic 数据解析
📦 快速开始
安装依赖
bash
运行
pip install -r requirements.txt
配置高德 API Key
plaintext
AMAP_MAPS_API_KEY=你的高德key
启动 MCP 服务
bash
运行
uvx amap-mcp-server
运行主程序
bash
运行
python 1.py
🎯 使用示例
输入：
目的地：上海
时间：2025-10-01 ~ 2025-10-03
偏好：景点、美食
输出：
plaintext
第1天：外滩 → 南京路步行街 → 豫园
交通：地铁+步行
住宿：一间森林酒店(人民广场店)
...
📁 项目结构
plaintext
1.py                 # 主程序
trip_planner_agent.py # 多智能体核心逻辑
README.md            # 项目说明
requirements.txt     # 依赖
🛠️ 常见问题
LLM 调用报错 400：更换模型为 qwen3.6-flash
MCP 连接失败：先启动 uvx amap-mcp-server
解析失败：系统会自动使用备用计划
📄 许可证
MIT License — 自由使用、修改、分享
