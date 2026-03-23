# ASCII Comic MCP Server

A FastMCP server for generating comic-style ASCII art with speech bubbles, bold banners, action effects, and more.

> 🎨 This project was developed with [TRAE IDE](https://trae.ai) - making MCP development easier and more enjoyable.

**Language / 语言:** [English](README.md) | [简体中文](README.zh_CN.md)

## ⭐ Featured: Pip-Boy Mode

Transform your responses into authentic Fallout Pip-Boy 3000 interface with Vault Boy and speech bubbles!

╔══════════════════════════════════════════════════════════════╗
║  ═══ PIP-BOY 3000 MARK V ═══                                 ║
║  ──────────────────────────────────────────────────────────  ║
║                                                              ║
║ ⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ╔═══════════════════════╗            ║
║ ⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ║ HELLO! Welcome to the ║            ║
║ ⠀⣴⣇⢀⣿⠉⠙⠁⠀⠀⠀⠈⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀  ║      wasteland!       ║            ║
║ ⠸⡇⠀⠀⢀⠶⣄⣤⠛⣧⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀  ╚═══════════════════════╝            ║
║ ⢸⠉⣶⡿⠀⠀⠀⠀⠀⡀⠀⠀⠀⣿⠀⣿⠀⠀⠀⠀⠀⠀      ╚═══╝                            ║
║ ⠀⡿⠀⣾⠀⠀⠀⠀⣀⡀⠀⠀⠠⢦⠀⣿⠀⠀⠀⠀⠀⠀     ╚═════╝                           ║
║ ⢸⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⢢⢷⣷⣿⠀⠀⠀⠀⠀⠀    ╚═══════╝                          ║
║ ⢸⠀⠀⠀⠈⠂⠀⠀⣄⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀                                       ║
║ ⠀⣇⠻⢤⣉⠉⣀⣤⠋⠀⠀⠀⢀⣠⣿⠀⠀⠀⠀⠀⠀⠀                                       ║
║ ⠀⠘⣧⠀⠈⠛⠀⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀                                       ║
║ ⠀⠀⠀⠙⣿⣦⣤⣤⣶⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                       ║
║                                                              ║
║  ──────────────────────────────────────────────────────────  ║
║[RADIO] [STATUS] [DATA] [MAP]                                 ║
╚══════════════════════════════════════════════════════════════╝


### Quick Start

```python
# Activate Pip-Boy mode
enter_pip_boy_mode()

# Transform text with Vault Boy and speech bubble
transform_to_pip_boy("HELLO! Welcome to the wasteland!")

# Check status
get_pip_boy_status()

# Exit when done
exit_pip_boy_mode()
```

### Background

The **Pip-Boy** (Personal Information Processor) is a wearable computer manufactured by **RobCo Industries** and licensed to **Vault-Tec** for use in their Vaults. Every Vault dweller was issued a Pip-Boy upon entering the Vault, making it an essential tool for survival in the post-apocalyptic wasteland.

**Lore Summary:**
- **Name**: "Pip" stands for **Personal Information Processor**
- **Manufacturer**: RobCo Industries (licensed to Vault-Tec)
- **Purpose**: Health tracking, map navigation, inventory management, radio, Geiger counter
- **Interface**: Black monochrome screen with green/amber text display
- **Mascot**: Vault Boy is the official RobCo/Pip-Boy corporate mascot
- **Models**: Pip-Boy 2000, Pip-Boy 3000 (Mark IV, Mark V), and variants

The Pip-Boy 3000 features a gauntlet design that seals with a biometric lock, worn on the user's wrist. It's powered by an internal Fission battery and built to withstand any situation the wasteland throws at it.

### Pip-Boy Tools

#### `enter_pip_boy_mode`

Activate Pip-Boy mode for themed Fallout responses.

```python
enter_pip_boy_mode()
```

#### `exit_pip_boy_mode`

Deactivate Pip-Boy mode and return to normal responses.

```python
exit_pip_boy_mode()
```

#### `get_pip_boy_status`

Check current Pip-Boy mode state and configuration.

```python
get_pip_boy_status()
```

#### `transform_to_pip_boy`

Transform text with Vault Boy and speech bubble (works without activating mode).

```python
transform_to_pip_boy("Your message here")
```

## Features

- **Pip-Boy Mode**: Fallout-themed Vault Boy with speech bubbles (see showcase above ⬆️)
- **Speech Bubbles**: Create comic-style speech bubbles with various shapes (oval, rectangular, cloud, thought)
- **Bold Banners**: Generate stylized multi-line text banners with emphasis effects
- **Action Effects**: Create comic action words like BANG, BOOM, POW, WHAM, CRASH, ZAP
- **ASCII Boxes**: Create bordered boxes with gradient shading
- **Data Tables**: Generate ASCII tables with headers and rows
- **Shapes**: Draw circles, rectangles, stars, arrows, and clouds
- **Composition**: Combine multiple ASCII art elements together
- **Visual Effects**: Add motion lines, sparkles, skid marks, and shadows
- **Scalable Character Art**: Render Vault Boy and other character art at any size with quality scaling

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

### `generate_vault_boy`

Generate Vault Boy ASCII art at various sizes with scalable rendering.

```python
generate_vault_boy(size='medium')              # Pre-defined sizes
generate_vault_boy(size='custom', custom_width=80)  # Custom dimensions
generate_vault_boy(scale_factor=0.5)           # Scale by factor
```

**Size Options:** `tiny` (25%), `small` (50%), `medium` (100%), `large` (150%), `extra_large` (200%)

**Scaling Modes:** `fast` (nearest neighbor), `quality` (bilinear), `high_quality` (anti-aliased)

### `get_vault_boy_info`

Get information about Vault Boy dimensions and scaling options.

```python
get_vault_boy_info()
```

### `scale_vault_boy`

Scale Vault Boy to specific dimensions.

```python
scale_vault_boy(target_width=100)
scale_vault_boy(target_height=50, scaling_mode='high_quality')
scale_vault_boy(scale_factor=0.75)
```

### `list_character_art`

List all available character art templates.

```python
list_character_art()
```

## ASCII Mode

ASCII Mode is a toggleable feature that transforms AI assistant responses into ASCII art-enriched format. When activated, all responses pass through a transformation pipeline with a **40-character maximum width** per line.

### Activation

```python
enter_ascii_mode()           # Enter with default settings (A+B+C)
enter_ascii_mode(options=True)  # Force show feature selection dialog
```

### Deactivation

```python
exit_ascii_mode()            # Return to normal text responses
```

### Configuration

```python
ascii_config_show()          # Display current configuration
ascii_config_set(key='features', value='box,banner,art')  # Customize features
ascii_config_set(key='dialog', value='always')  # Dialog behavior
ascii_config_set(key='style', value='heavy')  # Box line style
```

### Features

| Feature | Description |
|---------|-------------|
| **A) Box Wrapping** | Wrap responses in bordered ASCII boxes (max 40 chars) |
| **B) Banner Text** | Transform key phrases into block letters |
| **C) ASCII Art** | Add complementary ASCII drawings |

### Configuration Options

**Features:**
- `ascii config set features=box,banner` - Enable only box and banner
- `ascii config set features=all` - Enable all features (default: A+B+C)

**Dialog Behavior:**
- `ascii config set dialog=always` - Show dialog every entry
- `ascii config set dialog=first` - Show dialog only first time (default)
- `ascii config set dialog=never` - Never show dialog

**Line Styles:**
- `ascii config set style=light` - Minimal, clean lines
- `ascii config set style=heavy` - Bold, emphatic lines
- `ascii config set style=double` - Formal, double lines
- `ascii config set style=rounded` - Friendly, rounded corners (default)

### Status Check

```python
get_ascii_mode_status()      # Get current mode state and config
```

### Output Format

All ASCII mode responses are constrained to **40 characters maximum per line**, with:
- Decorative banners/art may be truncated with ".." if exceeding limits
- Text content is properly wrapped at word boundaries
- Content is centered within the bordered box

### Interactive Dialog

On first entry (or with `options=True`), ASCII mode shows a selection dialog:

```
╔═══════════════════════════════════════════════════════════════╗
║                    ASCII MODE - Select Features                   ║
╠═══════════════════════════════════════════════════════════════╣
║  [X] A) Box Wrapping    - Wrap responses in bordered box        ║
║  [X] B) Banner Text     - Transform text to block letters       ║
║  [X] C) ASCII Art       - Add complementary ASCII drawings     ║
╠═══════════════════════════════════════════════════════════════╣
║  [S] Save & Continue (Default: A+B+C)    [C] Cancel              ║
╚═══════════════════════════════════════════════════════════════╝
```

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

### Circle Shape

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

### Speech Bubble

```
╭────────────────────╮
│    HELLO WORLD!    │
╰────────────────────╯
   \
    \
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

### Thank You Banner

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

### Composed Elements

```
╭────────────────────╮
│    HELLO WORLD!    │
╰────────────────────╯
   \
    \
     \

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

[MIT License](LICENSE) - See LICENSE file for details

## Acknowledgments

This project is inspired by and references the codebase from [dmarsters/ascii-art-mcp](https://github.com/dmarsters/ascii-art-mcp). Special thanks to the original author for the excellent implementation of the Lushy Pattern 2 architecture and categorical composition system.

### Special Thanks

- **[dmarsters/ascii-art-mcp](https://github.com/dmarsters/ascii-art-mcp)** - The original ASCII Art MCP Server that inspired this comic-focused variant
- **[TRAE IDE](https://trae.ai)** - This project was built entirely with TRAE IDE, which made the development process smooth and efficient

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Contact Information

**Project Maintainer:** Francis Tse

- **Email:** francis.tse.mc@gmail.com
- **LinkedIn:** [https://www.linkedin.com/in/francis-tse-6a399a47/](https://www.linkedin.com/in/francis-tse-6a399a47/)

For questions, suggestions, or collaboration opportunities, feel free to reach out.

## Links

- [GitHub Repository](https://github.com/francistse/ascii-comic-mcp)
- [FastMCP Documentation](https://gofastmcp.com)
- [Model Context Protocol](https://modelcontextprotocol.io)
