---
name: "ascii-art"
description: "Creates comic-style ASCII art with speech bubbles, bold banners, action effects. Invoke when user wants to express text, comics, memes, or any content in artistic ASCII format, or asks for boxes, tables, speech bubbles, comic text, or text-based visual representations."
---

# ASCII Comic Skill - Generic & Composable Edition

This skill empowers the AI to create visual ASCII art using a **component-based approach**. Instead of pre-built scenes, you get reusable primitives, composition tools, and effect layers to build custom scenes.

## Two Ways to Create ASCII Art

This system provides **two distinct approaches** for creating ASCII art:

### 1. **Template-Based Generation** (Quick & Recognizable)
Use pre-built templates for common objects - perfect for immediate results.

### 2. **Component-Based Composition** (Custom & Flexible)
Build custom scenes from primitives - perfect for unique creations.

---

## PART 1: Template-Based Generation

Use these tools when you need **instant, recognizable ASCII art** of common subjects.

### `generate_ascii_art`

Generate ASCII art from pre-defined templates for recognizable objects.

```
Parameters:
- subject: Description of what to draw (e.g., 'a dog', 'a cat', 'a tree', 'a house')
- style: Art style (default, detailed, simple) - default: 'default'

Returns: ASCII art string
```

**Examples:**
```python
# Generate animals
generate_ascii_art(subject='a dog')
generate_ascii_art(subject='a cat sitting')
generate_ascii_art(subject='a bird flying')
generate_ascii_art(subject='a fish swimming')

# Generate nature
generate_ascii_art(subject='a tree')
generate_ascii_art(subject='a flower')
generate_ascii_art(subject='mountains')
generate_ascii_art(subject='the sun')

# Generate buildings & vehicles
generate_ascii_art(subject='a house')
generate_ascii_art(subject='a car')
generate_ascii_art(subject='a rocket')

# Generate objects
generate_ascii_art(subject='a heart')
generate_ascii_art(subject='a star')
generate_ascii_art(subject='a computer')
```

### `list_ascii_art_templates`

Get all available templates and their categories.

```
Returns: Dictionary with available templates organized by category

Example response:
{
    'available_templates': ['dog', 'cat', 'bird', ...],
    'by_category': {
        'animals': ['dog', 'cat', 'bird', 'fish', 'person'],
        'nature': ['tree', 'flower', 'mountain', 'sun', 'moon', 'cloud'],
        'buildings_vehicles': ['house', 'car', 'rocket', 'boat'],
        'objects': ['heart', 'star', 'computer', 'phone', 'book', 'cup', 'bottle']
    },
    'total_count': 21,
    'example_usage': "generate_ascii_art(subject='a dog')"
}
```

### `get_database_stats`

Get statistics about the ASCII art database and available templates.

```
Returns: Dictionary with database statistics and template count

Example response:
{
    'status': 'connected',
    'total_ascii_art': 150,
    'categories': [{'category': 'animals', 'count': 45}, ...],
    'averages': {'avg_width': 50.2, 'avg_height': 25.3, 'avg_complexity': 0.65},
    'available_templates': 21
}
```

### Available Templates (21 Total)

**Animals:**
- `dog` - Multiple variations
- `cat` - Classic cat face
- `bird` - Simple bird
- `fish` - Swimming fish
- `person` - Stick figure

**Nature:**
- `tree` - Pine tree
- `flower` - Simple flower
- `mountain` - Mountain range
- `sun` - Sun with rays
- `moon` - Crescent moon
- `cloud` - Fluffy cloud

**Buildings & Vehicles:**
- `house` - Simple house
- `car` - Side view car
- `rocket` - Space rocket
- `boat` - Sailboat

**Objects:**
- `heart` - Heart shape
- `star` - Star shape
- `computer` - Desktop PC
- `phone` - Mobile phone
- `book` - Open book
- `cup` - Coffee cup
- `bottle` - Water bottle

### When to Use Template-Based Generation

✅ **Use when:**
- User asks for a specific, common object ("draw a dog", "make a cat")
- Quick results are needed
- Recognizable objects are acceptable
- User describes a single subject

❌ **Don't use when:**
- User wants a custom scene or composition
- Specific artistic vision is needed
- Multiple objects need to be combined
- Unique positioning or styling is required

---

## PART 2: Component-Based Composition

Use these tools when you need **custom, flexible ASCII art** built from primitives.

## When to Invoke

**Invoke this skill when:**
- User asks to create a box, frame, or bordered content
- User wants text presented in an artistic/visual way
- User requests ASCII diagrams, tables, or visual layouts
- User asks to make something "look nice" in text form
- User wants comic strips, meme templates, or text art
- User wants speech bubbles (with tails pointing to speakers)
- User wants bold/banner-style text
- User wants action effects like BANG!, BOOM!, POW!
- User wants superhero or comic-style presentations
- User wants to build custom scenes from reusable components

## Core Philosophy: Composable Building Blocks

This system uses a **component-based approach**. Instead of pre-built scenes, you get:

1. **Primitive shapes** - Draw individual elements (clouds, rectangles, stars, arrows, etc.)
2. **Composition tools** - Combine elements together (vertical, horizontal, overlap)
3. **Effect layers** - Add motion, sparkles, skid marks, and other effects

## Primitive Shapes

### `draw_shape`
Draw a single reusable shape.

```
Parameters:
- shape_type: circle | oval | rectangle | star | arrow | cloud
- width: width in characters (default: 20)
- height: height in characters (default: 10)
- fill_char: character for filling (default: '█')
- border_char: character for borders (default: '─')
```

**Examples:**
```python
# Draw a cloud
draw_shape(shape_type='cloud', width=30, height=5, fill_char=' ', border_char='.')

# Draw a car-like rectangle
draw_shape(shape_type='rectangle', width=40, height=8, fill_char='█', border_char='┃')

# Draw an arrow for motion
draw_shape(shape_type='arrow', width=15, height=5, fill_char='>')
```

## Composition Tools

### `compose_elements`
Combine multiple ASCII art elements together.

```
Parameters:
- elements: list of ASCII art strings
- layout: vertical | horizontal | overlap
- spacing: number of empty lines/spaces between elements
```

**Examples:**
```python
# Stack elements vertically
compose_elements([cloud1, car, speech_bubble], layout='vertical', spacing=2)

# Place elements side by side
compose_elements([cloud1, cloud2, cloud3], layout='horizontal', spacing=3)
```

## Effect Tools

### `add_effect`
Add visual effects to existing ASCII art.

```
Parameters:
- ascii_art: the ASCII art to modify
- effect_type: motion_lines | sparkles | skid_marks | shadow
- position: top | bottom | left | right
- intensity: 1-5 (default: 3)
```

**Examples:**
```python
# Add motion lines to a car
add_effect(car_art, effect_type='motion_lines', position='left', intensity=4)

# Add skid marks to a drifting car
add_effect(car_art, effect_type='skid_marks', position='bottom', intensity=3)

# Add sparkles for emphasis
add_effect(title_art, effect_type='sparkles', position='top', intensity=2)
```

## High-Level Comic Tools

### `create_speech_bubble`
Creates a comic-style speech bubble with a tail pointing to a speaker.

```
Parameters:
- text: The text content of the bubble
- bubble_style: oval | rectangular | cloud | thought
- tail_position: bottom-left | bottom-right | bottom-center | left | right
- line_style: light | heavy | double | rounded
```

### `create_comic_banner`
Creates bold, stylized multi-line text.

```
Parameters:
- text: Text to convert to banner style
- font_style: block | outline
- emphasis: none | stars | underline | border
```

### `create_action_effect`
Creates comic-style action words.

```
Parameters:
- effect_text: BANG | BOOM | POW | WHAM | CRASH | ZAP
- size: small | medium | large | huge
- style: bold | outlined | filled
```

### `create_ascii_box`
Creates a bordered box with optional shading.

```
Parameters:
- width: 20-120 characters
- height: 5-50 characters
- title: Optional centered title text
- line_style: light | heavy | double | rounded
- shading_palette: ascii_standard | blocks | dots | density | braille
- shading_direction: horizontal | vertical | radial | diagonal
- contrast: 0.0-1.0 (low=subtle, high=dramatic)
```

### `create_ascii_table`
Creates a formatted data table with headers.

```
Parameters:
- headers: List of column header strings
- rows: List of row data (each row is a list of strings)
- line_style: light | heavy | double | rounded
```

### `create_comic_panel`
Creates a complete comic panel with title and content area.

```
Parameters:
- title: optional panel title
- content: the main content text
- bottom_text: optional text at bottom of panel
- width: panel width
- height: panel height
- line_style: light | heavy | double | rounded
```

## Building Custom Scenes: Workflow

**Instead of pre-built scenes, you build scenes by combining primitives:**

### Example: Cloudy Sky with Running Car

```python
# Step 1: Draw individual elements
cloud1 = draw_shape(shape_type='cloud', width=25, height=4, fill_char=' ', border_char='.')
cloud2 = draw_shape(shape_type='cloud', width=30, height=5, fill_char=' ', border_char='.')
car = draw_shape(shape_type='rectangle', width=35, height=7, fill_char='█', border_char='┃')
speech = create_speech_bubble(text="VROOM!", bubble_style='oval', tail_position='bottom-left')

# Step 2: Add effects
car_with_motion = add_effect(car, effect_type='motion_lines', position='left', intensity=4)

# Step 3: Compose everything together
sky = compose_elements([cloud1, cloud2], layout='horizontal', spacing=5)
scene = compose_elements([sky, car_with_motion, speech], layout='vertical', spacing=2)
```

### Example: Drifting Car with Skid Marks

```python
# Step 1: Draw elements
car = draw_shape(shape_type='rectangle', width=40, height=8, fill_char='█', border_char='┃')
cloud = draw_shape(shape_type='cloud', width=30, height=5, fill_char=' ', border_char='.')

# Step 2: Add effects
drifting_car = add_effect(car, effect_type='skid_marks', position='bottom', intensity=5)
drifting_car = add_effect(drifting_car, effect_type='motion_lines', position='right', intensity=3)

# Step 3: Compose
scene = compose_elements([cloud, drifting_car], layout='vertical', spacing=3)
```

## System Architecture & How to Use

This ASCII art system has two main components:

1. **Skill File** (.trae/skills/ascii-art/SKILL.md)
   - Provides documentation and guidance
   - Explains when and how to use the tools
   - Includes examples and best practices

2. **MCP Server** (server.py)
   - Contains the actual implementation code
   - Exposes MCP tools that can be invoked programmatically
   - All the drawing logic lives here

**To generate ASCII art:**
- You need to invoke the MCP tools from server.py
- The skill file just tells you how and when to use them
- Build custom scenes by combining primitive shapes, effects, and composition
- No pre-built scenes are provided - the system is generic and composable

## Tips

- **Start with primitives**: Draw individual shapes first, then compose
- **Use effects strategically**: Add motion lines, skid marks, or sparkles for emphasis
- **Think in layers**: Sky → ground → objects → speech bubbles → effects
- **Customize with characters**: Change fill_char and border_char for different styles
- **Experiment with layout**: Try both vertical and horizontal composition
- **Speech bubbles go on top**: Place dialogue bubbles above or beside characters
- **Motion direction matters**: Left-side motion lines = car moving left, right-side = car moving right

## Lessons Learned (Important)

### Lesson 1: Word Spacing in Banners
When creating multi-word banners (e.g., "HELLO WORLD"), **proper word spacing is critical**:
- Split text by words before converting to block letters
- Add spacing between words (not just concatenation)
- Each word's letters should be properly separated

### Lesson 2: Vertical Alignment
Multi-line block letters **must maintain proper vertical alignment**:
- Each letter has a consistent height across all rows
- All letters in a word align at the baseline
- Don't mix letters with different heights without accounting for it

### Lesson 3: Proper Centering
When centering text in banners:
- Calculate the maximum line length first
- Apply equal padding on both sides
- Use consistent character widths for spacing

### Lesson 4: Decoration Consistency
When adding decorations (stars, borders):
- Decorations should surround ALL lines uniformly
- Don't add partial decorations or misaligned elements
- Test with different text lengths to ensure consistency

### Lesson 5: Use the Tools Correctly
The `create_comic_banner` tool now properly:
- Handles word splitting automatically
- Supports alignment options (left, center, right)
- Supports width specification for consistent sizing
- Provides better border decorations

**Example usage:**
```python
# This will now work correctly with proper word spacing
create_comic_banner(
    text="HELLO WORLD!!!",
    font_style="block",
    emphasis="stars",
    align="center"
)
```

## High-Resolution Braille/Unicode Character Style

In addition to the basic ASCII style, this system supports high-quality artwork using Braille patterns and Unicode block elements.

### Available Samples

Use `list_ascii_art_samples()` to see all available files:
- `batman.txt` - Batman symbol
- `dog.txt` - Detailed dog
- `robin.txt` - Robin bird
- `head1.txt` - Human head
- `arrow.txt` - Arrow

### Character Set Used

This style uses detailed characters including:
- **Braille patterns**: ⠀⠁⠃⠇⠏⠟⠿⣿
- **Unicode blocks**: ⣀⣄⣤⣴⣶⣾⣿⡀⡄⡤⡴⡶⡾⣿
- **Box drawing elements**: ⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿

### Tools for High-Resolution Style

#### `list_ascii_art_samples`
List all available high-quality ASCII art sample files.

```
Returns: List of available filenames
```

#### `load_ascii_art`
Load high-quality ASCII art from sample files.

```
Parameters:
- filename: batman.txt | dog.txt | robin.txt | head1.txt | arrow.txt
```

**Examples:**
```python
# Load Batman symbol
batman = load_ascii_art(filename='batman.txt')

# Load dog
dog = load_ascii_art(filename='dog.txt')
```

#### `combine_ascii_arts`
Combine multiple ASCII art pieces together (works with both basic and high-resolution styles).

```
Parameters:
- arts: List of ASCII art strings
- layout: vertical | horizontal
- spacing: Number of empty lines/spaces between elements
```

**Examples:**
```python
# Load two pieces and combine
dog = load_ascii_art('dog.txt')
arrow = load_ascii_art('arrow.txt')
combined = combine_ascii_arts([dog, arrow], layout='vertical', spacing=2)
```

### When to Use Which Style

- **Basic ASCII style** - Best for:
  - Speech bubbles and dialogue
  - Tables and diagrams
  - Simple banners and borders
  - Quick, universally compatible art

- **High-resolution Braille/Unicode style** - Best for:
  - Detailed character drawings (dogs, birds, people)
  - Intricate symbols and logos
  - Artwork requiring fine detail
  - When visual quality is a priority

---

## ASCII Mode

ASCII Mode is a toggleable feature that transforms AI assistant responses into ASCII art-enriched format. When activated, all responses pass through a transformation pipeline.

### Activation

```
enter_ascii_mode()           # Enter with default settings (A+B+C)
enter_ascii_mode(options=True)  # Force show feature selection dialog
```

### Deactivation

```
exit_ascii_mode()            # Return to normal text responses
```

### Configuration

```
ascii_config_show()          # Display current configuration
ascii_config_set(key='features', value='box,banner,art')  # Customize features
ascii_config_set(key='dialog', value='always')  # Dialog behavior
ascii_config_set(key='style', value='heavy')  # Box line style
```

### Features

| Feature | Description |
|---------|-------------|
| **A) Box Wrapping** | Wrap responses in bordered ASCII boxes |
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

```
get_ascii_mode_status()      # Get current mode state and config
```

### Example Usage

```python
# Activate ASCII mode
enter_ascii_mode()

# Now all responses are transformed with:
# - Bordered box wrapper
# - Key words converted to banner text
# - Complementary ASCII art decorations

# Deactivate when done
exit_ascii_mode()
```

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