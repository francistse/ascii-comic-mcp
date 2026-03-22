# ASCII Mode Release Notes

## Version 1.0.0 - ASCII Mode Launch

**Release Date:** 2026-03-23

---

## Overview

ASCII Mode is a toggleable feature that transforms AI assistant responses into ASCII art-enriched format. When activated, all responses pass through a transformation pipeline that wraps content in ASCII boxes, converts key text to banner letters, and adds complementary ASCII art decorations.

---

## New Features

### ASCII Mode Toggle

- **Enter ASCII Mode** - Activate ASCII mode with configurable features
- **Exit ASCII Mode** - Deactivate ASCII mode and return to normal text responses
- **Mode Status** - Check current ASCII mode state and configuration

### Feature Configuration

| Feature | Code | Description |
|---------|------|-------------|
| Box Wrapping | A | Wrap responses in bordered ASCII boxes (max 40 chars per line) |
| Banner Text | B | Transform key phrases into block letters |
| ASCII Art | C | Add complementary ASCII drawings |

### Interactive Dialog

Feature selection dialog on first entry (or with `options=True`):

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

### Configuration Options

**Features:**
- `ascii config set features=box,banner` - Enable only box and banner
- `ascii config set features=all` - Enable all features (default: A+B+C)

**Dialog Behavior:**
- `ascii config set dialog=always` - Show dialog on every entry
- `ascii config set dialog=first` - Show dialog only on first entry (default)
- `ascii config set dialog=never` - Never show dialog

**Line Styles:**
- `ascii config set style=light` - Minimal, clean lines
- `ascii config set style=heavy` - Bold, emphatic lines
- `ascii config set style=double` - Formal, double lines
- `ascii config set style=rounded` - Friendly, rounded corners (default)

---

## New MCP Tools

| Tool | Purpose |
|------|---------|
| `enter_ascii_mode(options: bool)` | Activate ASCII mode |
| `exit_ascii_mode()` | Deactivate ASCII mode |
| `get_ascii_mode_status()` | Return current mode state and config |
| `ascii_config_show()` | Display current configuration |
| `ascii_config_set(key: str, value: str)` | Modify configuration |

---

## Technical Details

### 40-Character Line Width

All ASCII mode responses are constrained to **40 characters maximum per line**, ensuring consistent formatting across different AI assistants and terminals.

- Decorative banners/art may be truncated with ".." if exceeding limits
- Text content is properly wrapped at word boundaries
- Content is centered within the bordered box

### State Persistence

ASCII mode remembers your configuration:
- First entry shows the feature selection dialog
- Subsequent entries activate immediately with saved configuration
- User can force-show dialog with `options=True`

### Integration with Existing Tools

ASCII mode leverages existing ASCII art tools:
- `create_ascii_box()` - Box wrapping with configurable line styles
- `create_comic_banner()` - Banner text transformation
- `draw_shape()`, `compose_elements()` - Art generation

---

## Migration Guide

### Upgrading from Previous Version

ASCII mode is enabled by explicit user command. No automatic migration required.

### Quick Start

```python
# Enter with default features (A+B+C)
enter_ascii_mode()

# Or force show feature selection
enter_ascii_mode(options=True)

# Exit when done
exit_ascii_mode()
```

---

## Bug Fixes

N/A - Initial release

---

## Known Limitations

- ASCII mode responses have a 40-character maximum line width
- Banner text transformation works best with English text
- Some complex ASCII art may be simplified to fit width constraints

---

## Credits

ASCII Mode was designed and implemented as part of the ASCII Comic MCP Server project.

**Contributors:**
- Francis Tse (Project Maintainer)

**Inspiration:**
- [dmarsters/ascii-art-mcp](https://github.com/dmarsters/ascii-art-mcp) - Original ASCII Art MCP Server
