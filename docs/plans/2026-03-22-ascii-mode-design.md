# ASCII Mode Design Document

**Date:** 2026-03-22
**Project:** ASCII Comic MCP Server
**Feature:** ASCII Mode for AI Assistant Responses

---

## Overview

ASCII Mode is a toggleable feature that transforms AI assistant responses into ASCII art-enriched format. When activated, all responses pass through a transformation pipeline that wraps content in ASCII boxes, converts key text to banner letters, and adds complementary ASCII art decorations.

---

## Architecture

### Components

1. **ASCIIModeManager** - Central state manager for ASCII mode
2. **ASCIIModeConfig** - Configuration for features and dialog behavior
3. **TransformPipeline** - Response transformation engine
4. **InteractiveDialog** - Feature selection interface

### State Machine

```
                    ┌──────────────────┐
                    │                  │
    ┌───────────────>│     INACTIVE     │<───────────────┐
    │                │                  │                │
    │                └────────┬─────────┘                │
    │                         │                           │
    │            "enter ASCII mode"                       │
    │                         │                           │
    │                         v                           │
    │                ┌──────────────────┐                │
    │                │                  │                │
    │                │  ACTIVE (config)  │───────────────>│
    │                │                  │  "exit ASCII   │
    │                └──────────────────┘   mode"          │
    │                         │                           │
    │                         │ "enter ASCII mode          │
    │                         │  with options"             │
    │                         v                           │
    │                ┌──────────────────┐                │
    │                │                  │                │
    │                │   SHOWING_DIALOG  │────────────────┘
    │                │                  │
    │                └──────────────────┘
```

---

## Configuration

### ASCIIModeConfig

```python
@dataclass
class ASCIIModeConfig:
    features: Set[Literal['box', 'banner', 'art']] = {'box', 'banner', 'art'}
    show_dialog_on_entry: DialogBehavior = 'first'  # 'always', 'first', 'never'
    has_entered_before: bool = False
```

### Features

| Feature | Description | Transformation |
|---------|-------------|----------------|
| `box` (A) | Wrap responses in bordered box | `create_ascii_box()` |
| `banner` (B) | Transform text to block letters | `create_comic_banner()` |
| `art` (C) | Add complementary ASCII art | Shape generation + composition |

### Dialog Behavior Options

| Value | Behavior |
|-------|----------|
| `always` | Show dialog every time user enters ASCII mode |
| `first` | Show dialog only on first entry, remember for subsequent uses |
| `never` | Never show dialog, use saved configuration |

---

## Commands

### Mode Commands

| Command | Action |
|---------|--------|
| `enter ASCII mode` | Activate ASCII mode with config/dialog logic |
| `enter ASCII mode with options` | Force show feature selection dialog |
| `exit ASCII mode` | Deactivate ASCII mode |
| `ascii config show` | Display current configuration |
| `ascii config set <key>=<value>` | Modify configuration |

### Config Command Syntax

```
ascii config set features=box,banner        # Enable box + banner only
ascii config set features=all               # Enable all features (A+B+C)
ascii config set dialog=always             # Show dialog on every entry
ascii config set dialog=first               # Show dialog only first time
ascii config set dialog=never               # Never show dialog
ascii config show                           # Display current config
```

---

## Interactive Dialog

When shown, the dialog presents:

```
╔═══════════════════════════════════════════════════════════════╗
║                    ASCII MODE - Select Features                 ║
╠═══════════════════════════════════════════════════════════════╣
║  [X] A) Box Wrapping    - Wrap responses in bordered box        ║
║  [X] B) Banner Text    - Transform text to block letters       ║
║  [X] C) ASCII Art      - Add complementary ASCII drawings      ║
╠═══════════════════════════════════════════════════════════════╣
║  Dialog Behavior: First time only                              ║
║  [>] Change                                                  ║
╠═══════════════════════════════════════════════════════════════╣
║  [S] Save & Continue    [C] Cancel                             ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## Response Transformation Pipeline

When ASCII mode is active, responses are processed through:

1. **Banner Processing** - Identify key phrases, transform to block letters
2. **Art Generation** - Generate complementary shapes based on content context
3. **Box Wrapping** - Wrap the final composed output in bordered box

### Example Transformation

**Input:** `"Hello World! This is ASCII mode."`

**Output:**
```
┌─────────────────────────────────────────┐
│                                         │
│   HHH   EEE   LLL   LLL   OOO          │
│   H  E    L     L    O   O             │
│   H  E    L     L    O   O             │
│   HHH   EEE   L     L    OOO           │
│                                         │
│   TTT   HHH   I   S   BBB   OOO   X    │
│    T    H  I  S   T    B   O   O   X   │
│    T    HHH  I     T   BBB  OOO   X    │
│                                         │
│   [Complementary ASCII art based on     │
│    content - e.g., speech bubble]       │
│                                         │
└─────────────────────────────────────────┘
```

---

## Implementation Details

### Location

- `server.py` - Main MCP server with all tools
- New classes: `ASCIIModeManager`, `ASCIIModeConfig`, `InteractiveDialog`

### New MCP Tools

| Tool | Purpose |
|------|---------|
| `enter_ascii_mode(options: bool)` | Activate ASCII mode |
| `exit_ascii_mode()` | Deactivate ASCII mode |
| `get_ascii_mode_status()` | Return current mode state and config |
| `ascii_config_show()` | Display configuration |
| `ascii_config_set(key: str, value: str)` | Modify configuration |
| `show_ascii_mode_dialog()` | Display interactive feature selection |

### Integration with Existing Tools

The ASCII mode leverages existing tools:
- `create_ascii_box()` for box wrapping
- `create_comic_banner()` for banner text
- `draw_shape()`, `compose_elements()` for art generation

---

## Deactivation

ASCII mode remains active until:
1. User explicitly types `exit ASCII mode`
2. User enters a different mode
3. Session ends

---

## Default Behavior

On first `enter ASCII mode`:
1. Show interactive dialog (default behavior)
2. User selects features and saves
3. Mode activates with selected configuration

On subsequent `enter ASCII mode`:
1. Mode activates immediately with saved configuration
2. No dialog shown (unless `dialog=always` is set)

---

## Files Modified

| File | Changes |
|------|---------|
| `server.py` | Add ASCIIModeManager, ASCIIModeConfig, InteractiveDialog, new MCP tools |
| `SKILL.md` | Document ASCII mode feature |
| `README.md` | Add ASCII mode usage documentation |
