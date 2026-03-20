# ASCII Comic MCP Server

A FastMCP server for generating comic-style ASCII art with speech bubbles, bold banners, action effects, and more.

> 🎨 This project was developed with [TRAE IDE](https://trae.ai) - making MCP development easier and more enjoyable.

## Features

- **Speech Bubbles**: Create comic-style speech bubbles with various shapes (oval, rectangular, cloud, thought)
- **Bold Banners**: Generate stylized multi-line text banners with emphasis effects
- **Action Effects**: Create comic action words like BANG, BOOM, POW, WHAM, CRASH, ZAP
- **ASCII Boxes**: Create bordered boxes with gradient shading
- **Data Tables**: Generate ASCII tables with headers and rows
- **Shapes**: Draw circles, rectangles, stars, arrows, and clouds
- **Composition**: Combine multiple ASCII art elements together
- **Visual Effects**: Add motion lines, sparkles, skid marks, and shadows

## Installation

### Using pip

```bash
pip install ascii-comic-mcp
```

### Using FastMCP CLI

```bash
fastmcp install server.py
```

### From Source

```bash
git clone https://github.com/francistse/ascii-comic-mcp.git
cd ascii-comic-mcp
pip install -e .
```

## Usage

### Running the Server

```bash
# Using FastMCP CLI
fastmcp run server.py

# Or directly with Python
python server.py

# Development mode with inspector
fastmcp dev server.py inspector
```

### Integration with Claude Desktop

Add to your Claude Desktop configuration (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

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

### Integration with TRAE

Add to your TRAE MCP configuration:

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

## Available Tools

### `create_ascii_box`

Create ASCII art boxes with borders and optional shading.

```python
create_ascii_box(
    width=50,
    height=15,
    title="Status",
    line_style='double',
    shading_palette='blocks',
    shading_direction='radial',
    contrast=0.8
)
```

### `create_ascii_table`

Create ASCII tables with headers and data rows.

```python
create_ascii_table(
    headers=["Name", "Status", "Progress"],
    rows=[
        ["Task 1", "Complete", "100%"],
        ["Task 2", "Running", "65%"],
        ["Task 3", "Pending", "0%"]
    ],
    line_style='double'
)
```

### `create_speech_bubble`

Create comic-style speech bubbles.

```python
create_speech_bubble(
    text="HELLO WORLD!",
    bubble_style='oval',
    tail_position='bottom-left',
    line_style='rounded'
)
```

### `create_comic_banner`

Create bold, stylized text banners.

```python
create_comic_banner(
    text="HELLO WORLD!!!",
    font_style='block',
    emphasis='stars'
)
```

### `create_action_effect`

Create comic action effects.

```python
create_action_effect(
    effect_text='BANG',
    size='large',
    style='bold'
)
```

### `draw_shape`

Draw various shapes.

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

Compose multiple ASCII art elements together.

```python
compose_elements(
    elements=[banner, speech_bubble],
    layout='vertical',
    spacing=2
)
```

### `add_effect`

Add visual effects to existing ASCII art.

```python
add_effect(
    ascii_art=art,
    effect_type='motion_lines',
    position='left',
    intensity=4
)
```

### `create_comic_panel`

Create comic panel frames.

```python
create_comic_panel(
    title="EPISODE 1",
    top_text="Meanwhile...",
    bottom_text="To be continued..."
)
```

### `list_ascii_styles`

List all available ASCII art styles with their visual properties.

## Style Options

### Line Styles
- `light`: Clean, minimal, professional
- `heavy`: Bold, emphatic
- `double`: Formal, structured
- `rounded`: Friendly, approachable

### Shading Palettes
- `ascii_standard`: Classic ASCII art - universally compatible
- `blocks`: Smooth gradients - modern terminal aesthetics
- `dots`: Geometric precision - technical diagrams
- `density`: High detail - complex shading
- `braille`: Ultra-fine detail - maximum resolution

## Examples

### Speech Bubble

```
╭──────────────────╮
│  HELLO WORLD!    │
╰──────────────────╯
   \/
    \
```

### Action Effect

```
█████   █████  █████  █████
█   █   █      █   █  █   █
█████   █████  █████  █████
    █   █      █   █      █
█████   █████  █   █  █████
```

### Banner with Stars

```
★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★
★ █████   █   █████  █████ ★
★ █       █   █      █     ★
★ ███     █   ███    ███   ★
★ █       █   █      █     ★
★ █       █   █████  █████ ★
★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★
```

## Requirements

- Python >= 3.10
- fastmcp >= 0.1.0

## License

MIT License

## Acknowledgments

This project is inspired by and references the codebase from [dmarsters/ascii-art-mcp](https://github.com/dmarsters/ascii-art-mcp). Special thanks to the original author for the excellent implementation of the Lushy Pattern 2 architecture and categorical composition system.

### Special Thanks

- **[dmarsters/ascii-art-mcp](https://github.com/dmarsters/ascii-art-mcp)** - The original ASCII Art MCP Server that inspired this comic-focused variant
- **[TRAE IDE](https://trae.ai)** - This project was built entirely with TRAE IDE, which made the development process smooth and efficient

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Links

- [GitHub Repository](https://github.com/francistse/ascii-comic-mcp)
- [FastMCP Documentation](https://gofastmcp.com)
- [Model Context Protocol](https://modelcontextprotocol.io)
