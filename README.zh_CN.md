# ASCII Comic MCP Server

一个用于生成漫画风格 ASCII 艺术的 FastMCP 服务器，支持对话气泡、粗体横幅、动作特效等。

> 🎨 本项目使用 [TRAE IDE](https://trae.ai) 开发 - 让 MCP 开发变得更加简单愉快。

**语言 / 语言:** [English](README.md) | [简体中文](README.zh_CN.md)

## 功能特性

- **对话气泡**: 创建各种形状的漫画风格对话气泡（椭圆形、矩形、云朵形、思想形）
- **粗体横幅**: 生成带有强调效果的多行风格化文本横幅
- **动作特效**: 创建漫画动作词如 BANG、BOOM、POW、WHAM、CRASH、ZAP
- **ASCII 方框**: 创建带边框和渐变阴影的方框
- **数据表格**: 生成带标题和行的 ASCII 表格
- **形状绘制**: 绘制圆形、矩形、星星、箭头、云朵
- **元素组合**: 将多个 ASCII 艺术元素组合在一起
- **视觉效果**: 添加运动线、火花、刹车痕、阴影等效果

## 安装

### 使用 pip

```bash
pip install ascii-comic-mcp
```

### 使用 FastMCP CLI

```bash
fastmcp install server.py
```

### 从源代码安装

```bash
git clone https://github.com/francistse/ascii-comic-mcp.git
cd ascii-comic-mcp
pip install -e .
```

## 使用方法

### 运行服务器

```bash
# 使用 FastMCP CLI
fastmcp run server.py

# 或直接用 Python 运行
python server.py

# 开发模式（带检查器）
fastmcp dev server.py inspector
```

### 与 Claude Desktop 集成

添加到 Claude Desktop 配置文件（macOS 路径：`~/Library/Application Support/Claude/claude_desktop_config.json`）：

```json
{
  "mcpServers": {
    "ascii-comic": {
      "command": "fastmcp",
      "args": ["run", "/path/to/ascii-comic-mcp/server.py"]
    }
  }
}
```

### 与 TRAE 集成

添加到 TRAE MCP 配置文件：

```json
{
  "mcpServers": {
    "ascii-comic": {
      "command": "fastmcp",
      "args": ["run", "/path/to/ascii-comic-mcp/server.py"]
    }
  }
}
```

## 可用工具

### `create_ascii_box`

创建带边框和可选阴影的 ASCII 艺术方框。

```python
create_ascii_box(
    width=50,
    height=15,
    title="状态",
    line_style='double',
    shading_palette='blocks',
    shading_direction='radial',
    contrast=0.8
)
```

### `create_ascii_table`

创建带标题和数据行的 ASCII 表格。

```python
create_ascii_table(
    headers=["名称", "状态", "进度"],
    rows=[
        ["任务 1", "完成", "100%"],
        ["任务 2", "运行中", "65%"],
        ["任务 3", "待处理", "0%"]
    ],
    line_style='double'
)
```

### `create_speech_bubble`

创建漫画风格的对话气泡。

```python
create_speech_bubble(
    text="你好世界！",
    bubble_style='oval',
    tail_position='bottom-left',
    line_style='rounded'
)
```

### `create_comic_banner`

创建粗体风格化文本横幅。

```python
create_comic_banner(
    text="你好世界！！！",
    font_style='block',
    emphasis='stars'
)
```

### `create_action_effect`

创建漫画动作特效。

```python
create_action_effect(
    effect_text='BANG',
    size='large',
    style='bold'
)
```

### `draw_shape`

绘制各种形状。

```python
draw_shape(
    shape_type='circle',
    width=30,
    height=15,
    fill_char='█',
    border_char='●'
)
```

### `compose_elements`

组合多个 ASCII 艺术元素。

```python
compose_elements(
    elements=[banner, speech_bubble],
    layout='vertical',
    spacing=2
)
```

### `add_effect`

为现有 ASCII 艺术添加视觉效果。

```python
add_effect(
    ascii_art=art,
    effect_type='motion_lines',
    position='left',
    intensity=4
)
```

### `create_comic_panel`

创建漫画面板框架。

```python
create_comic_panel(
    title="第 1 集",
    top_text="与此同时...",
    bottom_text="未完待续..."
)
```

### `list_ascii_styles`

列出所有可用的 ASCII 艺术风格及其视觉属性。

## 风格选项

### 线条风格
- `light`: 简洁、极简、专业
- `heavy`: 粗体、醒目
- `double`: 正式、结构化
- `rounded`: 友好、亲切

### 阴影调色板
- `ascii_standard`: 经典 ASCII 艺术 - 通用兼容
- `blocks`: 平滑渐变 - 现代终端美学
- `dots`: 几何精度 - 技术图表
- `density`: 高细节 - 复杂阴影
- `braille`: 超精细 - 最高分辨率

## 示例

### 圆形

```
                              
           ●●●●●●●●●          
       ●●█████████████●●      
    ●●███████████████████●●   
   ●●█████████████████████●●  
  ●█████████████████████████● 
 ●●█████████████████████████●●
 ●███████████████████████████●
 ●███████████████████████████●
 ●●█████████████████████████●●
  ●█████████████████████████● 
   ●●█████████████████████●●  
    ●●███████████████████●●   
       ●●█████████████●●      
           ●●●●●●●●●          
```

### 对话气泡

```
╭──────────────────╮
│  HELLO WORLD!    │
╰──────────────────╯
   \/
    \
```

### 动作特效

```
█████   █████  █████  █████
█   █   █      █   █  █   █
█████   █████  █████  █████
    █   █      █   █      █
█████   █████  █   █  █████
```

### 进度条

```
[████████████░░░░░░░░░░░░] 50%
```

### 带星星的横幅

```
★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★
★ █████   █   █████  █████ ★
★ █       █   █      █     ★
★ ███     █   ███    ███   ★
★ █       █   █      █     ★
★ █       █   █████  █████ ★
★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★
```

### 感谢横幅

```
┌───────────────────────────────────────────────────────────────────────────────┐
│  ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★  │
│  ★                                                                         ★  │
│  ★   TTTTT   H   H   AAAAA   N   N   K   K   Y   Y   OOOOO   U   U   ★  │
│  ★     T     H   H   A   A   NN  N   K  K     Y Y    O   O   U   U   ★  │
│  ★     T     HHHHH   AAAAA   N N N   KKK       Y     O   O   U   U   ★  │
│  ★     T     H   H   A   A   N  NN   K  K      Y     O   O   U   U   ★  │
│  ★     T     H   H   A   A   N   N   K   K     Y      OOOOO   UUUUU   ★  │
│  ★                                                                         ★  │
│  ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★  │
└───────────────────────────────────────────────────────────────────────────────┘
```

## 系统要求

- Python >= 3.10
- fastmcp >= 0.1.0

## 许可证

MIT License

## 致谢

本项目的灵感来源于 [dmarsters/ascii-art-mcp](https://github.com/dmarsters/ascii-art-mcp) 的代码库。特别感谢原作者出色的 Lushy Pattern 2 架构和分类组合系统实现。

### 特别感谢

- **[dmarsters/ascii-art-mcp](https://github.com/dmarsters/ascii-art-mcp)** - 原始 ASCII艺术MCP服务器，为本项目提供了灵感
- **[TRAE IDE](https://trae.ai)** - 本项目完全使用 TRAE IDE 构建，使开发过程更加顺畅高效

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 📞 联系方式

**项目维护者：** Francis Tse

- **邮箱:** francis.tse.mc@gmail.com
- **领英:** [https://www.linkedin.com/in/francis-tse-6a399a47/](https://www.linkedin.com/in/francis-tse-6a399a47/)

如有问题、建议或合作机会，欢迎随时联系。

## 链接

- [GitHub 仓库](https://github.com/francistse/ascii-comic-mcp)
- [FastMCP 文档](https://gofastmcp.com)
- [模型上下文协议](https://modelcontextprotocol.io)
