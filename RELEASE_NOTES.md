# ASCII Comic MCP Server - Release Notes

## Version 1.1.0 - Pip-Boy Mode Added

**Release Date:** 2026-03-24

---

## Overview

Version 1.1.0 introduces **Pip-Boy Mode**, a Fallout-themed feature that transforms responses into authentic Pip-Boy 3000 interface with Vault Boy and speech bubbles. This release also includes the new Spacing Verification tool for ensuring ASCII art quality.

---

## New Features

### 🎮 Pip-Boy Mode

Transform your responses into authentic Fallout Pip-Boy 3000 interface!

**Sample Output:**

```
╔══════════════════════════════════════════════════════════════╗
║  ═══ PIP-BOY 3000 MARK V ═══                                 ║
║  ──────────────────────────────────────────────────────────  ║
║                                                              ║
║ ⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀  ╔═══════════════════════╗            ║
║ ⠀⠀⠀⠀⠀⠀⣶⣿⣷⣀⢀⣤⣤⣤⠶⠶⠶⠶  ║ HELLO! Welcome to the ║            ║
║ ⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉  ║      wasteland!       ║            ║
║ ⠀⠈⠉⠛⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿  ╚═══════════════════════╝            ║
║ ⠀⠈⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛  ╚═══╝                            ║
║ ⠀⠈⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛  ╚═════╝                           ║
║ ⠀⠈⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛  ╚═══════╝                          ║
║                                                              ║
║  ──────────────────────────────────────────────────────────  ║
║[RADIO] [STATUS] [DATA] [MAP]                                 ║
╚══════════════════════════════════════════════════════════════╝
```

### 📐 Spacing Verification Tool

New `verify_spacing.py` script for validating ASCII art output:

```bash
python verify_spacing.py
```

Checks for:
- Line length consistency
- Box drawing alignment
- Character spacing issues
- Vertical spacing problems
- Braille character spacing

### 🎯 Scalable Vault Boy Art

- Extracts single Vault Boy panel from multi-panel source
- Three scaling algorithms: fast, quality, high_quality
- Pre-defined size variants: tiny (25%), small (50%), medium (100%), large (150%), extra_large (200%)
- Character density preservation using Braille/Block mapping

---

## New MCP Tools

| Tool | Purpose |
|------|---------|
| `enter_pip_boy_mode()` | Activate Pip-Boy mode for themed Fallout responses |
| `exit_pip_boy_mode()` | Deactivate Pip-Boy mode |
| `get_pip_boy_status()` | Check current Pip-Boy mode state |
| `transform_to_pip_boy(text)` | Transform text with Vault Boy and speech bubble |
| `generate_vault_boy(size, scale_factor, scaling_mode)` | Generate Vault Boy at various sizes |
| `get_vault_boy_info()` | Get Vault Boy dimensions and scaling info |
| `scale_vault_boy(target_width, scaling_mode)` | Scale Vault Boy to specific dimensions |
| `list_character_art()` | List available character art templates |

---

## Pip-Boy Lore

The **Pip-Boy** (Personal Information Processor) is a wearable computer manufactured by **RobCo Industries** and licensed to **Vault-Tec**.

- **Name**: "Pip" = Personal Information Processor
- **Manufacturer**: RobCo Industries (Vault-Tec licensed)
- **Purpose**: Health tracking, map navigation, inventory, radio, Geiger counter
- **Interface**: Black monochrome with green/amber display
- **Mascot**: Vault Boy (RobCo official mascot)
- **Models**: Pip-Boy 2000, Pip-Boy 3000 (Mark IV, Mark V)

---

## Bug Fixes

### Version 1.1.0

- ✅ Fixed duplicate Vault Boy heads appearing in Pip-Boy output
- ✅ Fixed border alignment issues in Pip-Boy mode
- ✅ All lines now consistently 64 characters wide
- ✅ Proper text wrapping without indentation problems

### Version 1.0.0

- N/A - Initial release

---

## Technical Details

### Pip-Boy Implementation

- Singleton pattern for Vault Boy scaler
- First panel extraction from multi-panel source file
- Three scaling modes with different quality/speed tradeoffs
- Horizontal composition: Vault Boy left, speech bubble right
- Automatic text wrapping at word boundaries

### Spacing Verification

Automated checks for:
- Line length consistency (variations should be minimal)
- Box drawing character alignment
- Proper spacing around box characters
- Vertical spacing (no excessive empty lines)
- Braille pattern spacing in high-density art

---

## Migration Guide

### Upgrading from 1.0.0

No breaking changes. Pip-Boy mode is opt-in.

```python
# New in 1.1.0 - Try Pip-Boy mode!
enter_pip_boy_mode()
transform_to_pip_boy("Your message here")
exit_pip_boy_mode()
```

---

## Known Limitations

- Pip-Boy mode uses 64-character fixed width
- Speech bubble max width is 24 characters for proper display
- Vault Boy extraction works with specific file format (header + art lines)
- Spacing verification is informational only (warnings, not errors)

---

## Credits

**Project Maintainer:** Francis Tse

**Inspiration:**
- [dmarsters/ascii-art-mcp](https://github.com/dmarsters/ascii-art-mcp) - Original ASCII Art MCP Server
- Fallout Franchise - Pip-Boy concept and Vault Boy mascot

---

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
