"""
ASCII Comic MCP Server

Comic-style ASCII art with speech bubbles, bold banners, and action effects.
Uses categorical composition of aesthetic functors with zero rendering dependencies.

Functors:
- box_drawing: Border styles, line weights, corner treatments
- ascii_shading: Character gradients, contrast, patterns
- layout_composition: Canvas size, alignment, spatial organization
"""

from fastmcp import FastMCP
from typing import Dict, Any, List, Optional, Literal
from dataclasses import dataclass
import math
import os
import json
import sqlite3
import random
from datetime import datetime
import pyfiglet

# Initialize MCP server
mcp = FastMCP("ASCII Comic Generator")


# ============================================================================
# ASCII ART TEMPLATES (Standalone Generator)
# ============================================================================

ASCII_TEMPLATES = {
    'dog': [
"""      __      __
     /  \\    /  \\
    |    \\__/    |
    |  o    o  |
    |     <     |
    |   \\___/   |
     \\  \\___/  /
      \\  ---  /
       | | | |
       | | | |""",
"""  __      __
 /  \\____/  \\
|  __    __  |
| |  |  |  | |
| |  |__|  | |
|  \\______/  /
 \\  \\    /  /
  \\  \\__/  /
   | |  | |
   |_|  |_|"""
    ],
    'cat': [
"""      /\\_/\\
     ( o.o )
      > ^ <
     /|   |\\
    ( |   | )
    | |   | |
    |_|   |_|""",
"""  /\\_/\\
 ( >.< )
 (  "  )
 /|   |\\
/ |   | \\
  |   |
  |   |"""
    ],
    'bird': [
"""   __
 _'  >
  \\/
   \\/\\
    \\""",
"""  __
 /  \\
|    |
 \\__/
  ||
  ||
  ||"""
    ],
    'fish': [
"""      __
   _ /  \\_
  / /    \\ \\
 | |      | |
  \\ \\____/ /
   \\______/""",
"""   __
 _/  \\_
/      \\
|  ()  |
\\______/"""
    ],
    'tree': [
"""
    *
   ***
  *****
 *******
*********
    |
    |
    |
""",
"""   ***
  *****
 *******
*********
    |
    |""",
"""    *
   ***
  *****
 *******
*********
    |
    |
    |"""
    ],
    'house': [
"""
   /\\
  /  \\
 /____\\
 |    |
 |    |
 |____|
""",
"""    /\\
   /  \\
  /____\\
  | [] |
  |    |
  |____|"""
    ],
    'car': [
"""      ______
     /|_||_\\`.__
    (   _    _\\
    =`-(_)--(_)-'
""",
"""    ______
   /|_||_\\`.__
  (   _    _)
  =`-(_)--(_)-'"""
    ],
    'flower': [
"""    __
 _-(  )-_
/  \\||/  \\
|  / || \\  |
 \\_/  ||  \\_/
      ||
      ||
""",
"""   _-_
  (   )
 _/ | \\_
|  /|\\  |
 \\_/|\\_/
   | |
   | |"""
    ],
    'heart': [
"""
 __  __
/  \\/  \\
\\      /
 \\    /
  \\  /
   \\/
""",
""" **   **
**** ****
*********
 ********
  *******
   *****
    ***
     *"""
    ],
    'star': [
"""    *
   ***
  *****
*******
 *****
  ***
   *""",
"""  *
 * *
*****
 * *
  *"""
    ],
    'sun': [
"""      _
   _ ( ) _
  (  ___  )
   (_____)
      |""",
"""   \\ | /
 -  *  -
   / | \\"""
    ],
    'moon': [
"""   _
 _' >
/ /
\\ \\
 \\_\\
""",
"""   __
 _'  >
/  /
\\  \\
 \\__\\"""
    ],
    'person': [
"""   O
  /|\\
  / \\""",
"""  _O_
   |
  / \\""",
"""   ___
  /   \\
  | O |
  \\___/
    |
   / \\
  /   \\"""
    ],
    'mountain': [
"""    /\\
   /  \\
  /    \\
 /      \\
/________\\
""",
"""     /\\
    /  \\
   /    \\
  /      \\
 /   /\\   \\
/___/  \\___\\"""
    ],
    'cloud': [
"""   _____
  /     \\
 /       \\
/         \\
\\         /
 \\_______/""",
"""  ______
 /      \\
/        \\
\\        /
 \\______/"""
    ],
    'rocket': [
"""   /\\
  /  \\
 |    |
 |    |
 |    |
/|    |\\
""",
"""   /\\
  /  \\
 |    |
 |    |
/|    |\\
| |  | |
| |  | |"""
    ],
    'computer': [
""" _______
|       |
|       |
|_______|
   | |
   | |
  /___\\
""",
""" ________
|        |
|        |
|________|
   ____
  |    |
  |____|"""
    ],
    'phone': [
""" _______
|       |
|       |
|       |
|_______|
  [___]
""",
""" _______
|       |
|  ___  |
| |   | |
| |___| |
|_______|
"""
    ],
    'book': [
""" _______
|  ___  |
| |   | |
| |   | |
| |___| |
|_______|
""",
"""  _____
 |   |
 |   |
_|   |_
|_____|"""
    ],
    'cup': [
""" ______
|      |
|      |
|______|
   ||
   ||
   ||
""",
"""  ____
 |    |
 |    |
 |____|
   ||
   ||"""
    ],
    'bottle': [
"""   __
  |  |
  |  |
  |  |
  |__|
 /    \\
|      |
 \\____/
""",
"""   __
  |  |
  |  |
  |__|
 /    \\
|      |
 \\____/"""
    ]
}


def get_template(subject: str) -> Optional[str]:
    """Get an ASCII art template for a subject"""
    subject_lower = subject.lower()

    for key in ASCII_TEMPLATES.keys():
        if key in subject_lower:
            return random.choice(ASCII_TEMPLATES[key])

    return None


def list_available_templates() -> List[str]:
    """List all available template names"""
    return sorted(list(ASCII_TEMPLATES.keys()))


# ============================================================================
# LAYER 1: Data Structures (Categorical Objects)
# ============================================================================

@dataclass
class BoxDrawingParams:
    """Box drawing aesthetic parameters"""
    line_style: Literal['light', 'heavy', 'double', 'rounded']
    corner_type: Literal['sharp', 'rounded', 'beveled']
    symmetry: Literal['bilateral', 'radial', 'asymmetric']


@dataclass
class ShadingParams:
    """ASCII shading parameters"""
    palette_type: Literal['ascii_standard', 'blocks', 'dots', 'density', 'braille']
    contrast: float  # 0.0-1.0
    direction: Literal['horizontal', 'vertical', 'radial', 'diagonal']
    dither: bool


@dataclass
class LayoutParams:
    """Layout composition parameters"""
    width: int
    height: int
    horizontal_align: Literal['left', 'center', 'right']
    vertical_align: Literal['top', 'middle', 'bottom']
    padding: int


# ============================================================================
# LAYER 2: Intentionality (Visual Vocabularies)
# ============================================================================

UNICODE_SETS = {
    'light': {
        'horizontal': '─', 'vertical': '│',
        'top_left': '┌', 'top_right': '┐',
        'bottom_left': '└', 'bottom_right': '┘',
        'cross': '┼', 't_down': '┬', 't_up': '┴', 't_left': '┤', 't_right': '├',
        'intentionality': 'Clean, minimal, professional - optimal for documentation'
    },
    'heavy': {
        'horizontal': '━', 'vertical': '┃',
        'top_left': '┏', 'top_right': '┓',
        'bottom_left': '┗', 'bottom_right': '┛',
        'cross': '╋', 't_down': '┳', 't_up': '┻', 't_left': '┫', 't_right': '┣',
        'intentionality': 'Bold, emphatic - draws attention and establishes hierarchy'
    },
    'double': {
        'horizontal': '═', 'vertical': '║',
        'top_left': '╔', 'top_right': '╗',
        'bottom_left': '╚', 'bottom_right': '╝',
        'cross': '╬', 't_down': '╦', 't_up': '╩', 't_left': '╣', 't_right': '╠',
        'intentionality': 'Formal, structured - conveys authority and permanence'
    },
    'rounded': {
        'horizontal': '─', 'vertical': '│',
        'top_left': '╭', 'top_right': '╮',
        'bottom_left': '╰', 'bottom_right': '╯',
        'cross': '┼', 't_down': '┬', 't_up': '┴', 't_left': '┤', 't_right': '├',
        'intentionality': 'Friendly, approachable - reduces visual tension'
    }
}

SHADING_PALETTES = {
    'ascii_standard': {
        'chars': ' .:-=+*#%@',
        'texture': 'grainy',
        'intentionality': 'Classic ASCII art - universally compatible'
    },
    'blocks': {
        'chars': ' ░▒▓█',
        'texture': 'smooth',
        'intentionality': 'Smooth gradients - modern terminal aesthetics'
    },
    'dots': {
        'chars': ' ·∘○●◉',
        'texture': 'dotted',
        'intentionality': 'Geometric precision - technical diagrams'
    },
    'density': {
        'chars': ' .,;!lI$@',
        'texture': 'dense',
        'intentionality': 'High detail - complex shading'
    },
    'braille': {
        'chars': '⠀⠁⠃⠇⠏⠟⠿⣿',
        'texture': 'fine',
        'intentionality': 'Ultra-fine detail - maximum resolution'
    }
}


# ============================================================================
# LAYER 3: Rendering Engine
# ============================================================================

class ASCIIArtRenderer:
    """Deterministic ASCII art generation from categorical parameters"""
    
    def __init__(
        self,
        box_params: BoxDrawingParams,
        shading_params: ShadingParams,
        layout_params: LayoutParams
    ):
        self.box = box_params
        self.shading = shading_params
        self.layout = layout_params
        self.chars = UNICODE_SETS[box_params.line_style]
        self.palette = SHADING_PALETTES[shading_params.palette_type]['chars']
    
    def render_bordered_box(self, title: Optional[str] = None) -> str:
        """Render a bordered box with optional shading"""
        
        lines = []
        w = self.layout.width
        h = self.layout.height
        
        # Top border
        if title:
            title_display = f" {title} "
            title_len = len(title_display)
            left_line = self.chars['horizontal'] * ((w - 2 - title_len) // 2)
            right_line = self.chars['horizontal'] * ((w - 2 - title_len + 1) // 2)
            top = self.chars['top_left'] + left_line + title_display + right_line + self.chars['top_right']
        else:
            top = self.chars['top_left'] + (self.chars['horizontal'] * (w - 2)) + self.chars['top_right']
        lines.append(top)
        
        # Middle rows with shading
        for y in range(h - 2):
            row = self.chars['vertical']
            
            for x in range(w - 2):
                # Calculate shading value based on direction
                shade_value = self._calculate_shade_value(x, y, w - 2, h - 2)
                
                # Apply contrast
                shade_value = self._apply_contrast(shade_value)
                
                # Map to character
                char_idx = int(shade_value * (len(self.palette) - 1))
                char_idx = max(0, min(char_idx, len(self.palette) - 1))
                
                row += self.palette[char_idx]
            
            row += self.chars['vertical']
            lines.append(row)
        
        # Bottom border
        bottom = self.chars['bottom_left'] + (self.chars['horizontal'] * (w - 2)) + self.chars['bottom_right']
        lines.append(bottom)
        
        return '\n'.join(lines)
    
    def _calculate_shade_value(self, x: int, y: int, width: int, height: int) -> float:
        """Calculate shading value 0.0-1.0 based on position and direction"""
        
        center_x = width / 2
        center_y = height / 2
        
        if self.shading.direction == 'horizontal':
            return x / width if width > 0 else 0
        
        elif self.shading.direction == 'vertical':
            return y / height if height > 0 else 0
        
        elif self.shading.direction == 'radial':
            dx = (x - center_x) / center_x if center_x > 0 else 0
            dy = (y - center_y) / center_y if center_y > 0 else 0
            dist = math.sqrt(dx * dx + dy * dy)
            return min(dist, 1.0)
        
        elif self.shading.direction == 'diagonal':
            return (x + y) / (width + height) if (width + height) > 0 else 0
        
        else:
            return 0.5
    
    def _apply_contrast(self, value: float) -> float:
        """Apply contrast adjustment to shade value"""
        
        # Apply contrast curve
        if self.shading.contrast < 0.5:
            # Reduce contrast - compress to middle
            range_compress = self.shading.contrast * 2
            return 0.5 + (value - 0.5) * range_compress
        else:
            # Increase contrast - expand from middle
            range_expand = (self.shading.contrast - 0.5) * 2 + 1
            if value < 0.5:
                return 0.5 - (0.5 - value) * range_expand
            else:
                return 0.5 + (value - 0.5) * range_expand
        
        return max(0.0, min(1.0, value))
    
    def render_table(self, headers: List[str], rows: List[List[str]]) -> str:
        """Render a data table with borders"""
        
        # Calculate column widths
        col_widths = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                if i < len(col_widths):
                    col_widths[i] = max(col_widths[i], len(str(cell)))
        
        lines = []
        
        # Top border
        top = self.chars['top_left']
        for i, width in enumerate(col_widths):
            top += self.chars['horizontal'] * (width + 2)
            if i < len(col_widths) - 1:
                top += self.chars['t_down']
        top += self.chars['top_right']
        lines.append(top)
        
        # Header row
        header_row = self.chars['vertical']
        for i, header in enumerate(headers):
            header_row += f" {header.ljust(col_widths[i])} "
            if i < len(headers) - 1:
                header_row += self.chars['vertical']
        header_row += self.chars['vertical']
        lines.append(header_row)
        
        # Header separator
        sep = self.chars['t_right']
        for i, width in enumerate(col_widths):
            sep += self.chars['horizontal'] * (width + 2)
            if i < len(col_widths) - 1:
                sep += self.chars['cross']
        sep += self.chars['t_left']
        lines.append(sep)
        
        # Data rows
        for row in rows:
            data_row = self.chars['vertical']
            for i, cell in enumerate(row):
                if i < len(col_widths):
                    data_row += f" {str(cell).ljust(col_widths[i])} "
                    if i < len(row) - 1:
                        data_row += self.chars['vertical']
            data_row += self.chars['vertical']
            lines.append(data_row)
        
        # Bottom border
        bottom = self.chars['bottom_left']
        for i, width in enumerate(col_widths):
            bottom += self.chars['horizontal'] * (width + 2)
            if i < len(col_widths) - 1:
                bottom += self.chars['t_up']
        bottom += self.chars['bottom_right']
        lines.append(bottom)
        
        return '\n'.join(lines)


# ============================================================================
# MCP TOOLS
# ============================================================================

@mcp.tool()
def create_ascii_box(
    width: int = 50,
    height: int = 15,
    title: str = "",
    line_style: Literal['light', 'heavy', 'double', 'rounded'] = 'light',
    shading_palette: Literal['ascii_standard', 'blocks', 'dots', 'density', 'braille'] = 'ascii_standard',
    shading_direction: Literal['horizontal', 'vertical', 'radial', 'diagonal'] = 'radial',
    contrast: float = 0.7
) -> str:
    """
    Create ASCII art box with border and optional shading.
    
    Args:
        width: Box width in characters (20-120)
        height: Box height in characters (5-50)
        title: Optional title text in top border
        line_style: Border style (light=minimal, heavy=bold, double=formal, rounded=friendly)
        shading_palette: Character set for shading (ascii_standard, blocks, dots, density, braille)
        shading_direction: Gradient direction (horizontal, vertical, radial, diagonal)
        contrast: Shading contrast 0.0-1.0 (low=subtle, high=dramatic)
    
    Returns:
        ASCII art as multi-line string
    
    Example:
        create_ascii_box(width=40, height=10, title="Status", line_style='double', 
                        shading_palette='blocks', contrast=0.8)
    """
    
    # Clamp parameters
    width = max(20, min(120, width))
    height = max(5, min(50, height))
    contrast = max(0.0, min(1.0, contrast))
    
    # Create parameter objects
    box_params = BoxDrawingParams(
        line_style=line_style,
        corner_type='sharp' if line_style in ['light', 'heavy', 'double'] else 'rounded',
        symmetry='bilateral'
    )
    
    shading_params = ShadingParams(
        palette_type=shading_palette,
        contrast=contrast,
        direction=shading_direction,
        dither=False
    )
    
    layout_params = LayoutParams(
        width=width,
        height=height,
        horizontal_align='center',
        vertical_align='middle',
        padding=1
    )
    
    # Render
    renderer = ASCIIArtRenderer(box_params, shading_params, layout_params)
    return renderer.render_bordered_box(title if title else None)


@mcp.tool()
def create_ascii_table(
    headers: list[str],
    rows: list[list[str]],
    line_style: Literal['light', 'heavy', 'double', 'rounded'] = 'light'
) -> str:
    """
    Create ASCII table with headers and data rows.
    
    Args:
        headers: List of column headers
        rows: List of rows, each row is a list of cell values
        line_style: Border style (light, heavy, double, rounded)
    
    Returns:
        ASCII table as multi-line string
    
    Example:
        create_ascii_table(
            headers=["Name", "Status", "Progress"],
            rows=[
                ["Task 1", "Complete", "100%"],
                ["Task 2", "Running", "65%"],
                ["Task 3", "Pending", "0%"]
            ],
            line_style='double'
        )
    """
    
    box_params = BoxDrawingParams(
        line_style=line_style,
        corner_type='sharp' if line_style != 'rounded' else 'rounded',
        symmetry='bilateral'
    )
    
    shading_params = ShadingParams(
        palette_type='ascii_standard',
        contrast=0.5,
        direction='horizontal',
        dither=False
    )
    
    layout_params = LayoutParams(
        width=80,
        height=20,
        horizontal_align='left',
        vertical_align='top',
        padding=1
    )
    
    renderer = ASCIIArtRenderer(box_params, shading_params, layout_params)
    return renderer.render_table(headers, rows)


@mcp.tool()
def list_ascii_styles() -> dict:
    """
    List all available ASCII art styles with their intentionality.

    Returns:
        Dictionary of styles and their visual/semantic properties
    """

    return {
        "box_styles": {
            style: {
                "sample_chars": f"{chars['top_left']}{chars['horizontal']*3}{chars['top_right']}",
                "intentionality": chars['intentionality']
            }
            for style, chars in UNICODE_SETS.items()
        },
        "shading_palettes": {
            name: {
                "characters": palette['chars'],
                "texture": palette['texture'],
                "intentionality": palette['intentionality']
            }
            for name, palette in SHADING_PALETTES.items()
        }
    }


@mcp.tool()
def create_speech_bubble(
    text: str,
    bubble_style: Literal['oval', 'rectangular', 'cloud', 'thought'] = 'oval',
    tail_position: Literal['bottom-left', 'bottom-right', 'bottom-center', 'left', 'right'] = 'bottom-left',
    line_style: Literal['light', 'heavy', 'double', 'rounded'] = 'rounded'
) -> str:
    """
    Create a comic-style speech bubble with a tail pointing to the speaker.

    Args:
        text: The text content of the bubble
        bubble_style: Shape of bubble (oval, rectangular, cloud, thought)
        tail_position: Where the tail points (bottom-left, bottom-right, bottom-center, left, right)
        line_style: Border style (light, heavy, double, rounded)

    Returns:
        ASCII speech bubble as multi-line string

    Example:
        create_speech_bubble(text="HELLO WORLD!", bubble_style='oval',
                           tail_position='bottom-left', line_style='rounded')
    """

    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    width = max(max_len + 4, 10)
    height = len(lines)

    chars = UNICODE_SETS[line_style]

    if bubble_style == 'oval':
        return _render_oval_bubble(lines, width, height, tail_position, chars)
    elif bubble_style == 'rectangular':
        return _render_rectangular_bubble(lines, width, height, tail_position, chars)
    elif bubble_style == 'cloud' or bubble_style == 'thought':
        return _render_thought_bubble(lines, width, height, tail_position, chars)
    else:
        return _render_oval_bubble(lines, width, height, tail_position, chars)


def _render_oval_bubble(lines: List[str], width: int, height: int, tail_pos: str, chars: dict) -> str:
    """Render an oval speech bubble with tail"""
    result = []

    top_line = chars['top_left'] + chars['horizontal'] * (width - 2) + chars['top_right']
    result.append(top_line)

    for i, line in enumerate(lines):
        padded = line.center(width - 4)
        result.append(chars['vertical'] + padded + chars['vertical'])

    bottom_line = chars['bottom_left'] + chars['horizontal'] * (width - 2) + chars['bottom_right']
    result.append(bottom_line)

    result = _add_tail_to_bubble(result, tail_pos, chars)

    return '\n'.join(result)


def _render_rectangular_bubble(lines: List[str], width: int, height: int, tail_pos: str, chars: dict) -> str:
    """Render a rectangular speech bubble with tail"""
    result = []

    top_line = chars['top_left'] + chars['horizontal'] * (width - 2) + chars['top_right']
    result.append(top_line)

    for line in lines:
        padded = line.ljust(width - 4)
        result.append(chars['vertical'] + ' ' + padded[:width - 4] + ' ' + chars['vertical'])

    bottom_line = chars['bottom_left'] + chars['horizontal'] * (width - 2) + chars['bottom_right']
    result.append(bottom_line)

    result = _add_tail_to_bubble(result, tail_pos, chars)

    return '\n'.join(result)


def _render_thought_bubble(lines: List[str], width: int, height: int, tail_pos: str, chars: dict) -> str:
    """Render a thought cloud bubble with small circles as tail"""
    result = []

    top = '    ' + chars['top_left'] + chars['horizontal'] * (width - 2) + chars['top_right']
    result.append(top)

    for line in lines:
        padded = line.center(width - 4)
        result.append(chars['vertical'] + ' ' + padded + ' ' + chars['vertical'])

    bottom = '    ' + chars['bottom_left'] + chars['horizontal'] * (width - 2) + chars['bottom_right']
    result.append(bottom)

    if tail_pos == 'bottom-right':
        result.append('                         o   o')
        result.append('                          o')
    else:
        result.append('o   o')
        result.append(' o')

    return '\n'.join(result)


def _add_tail_to_bubble(bubble: List[str], tail_pos: str, chars: dict) -> List[str]:
    """Add a speech tail to the bottom of a bubble"""
    width = len(bubble[0])

    if tail_pos == 'bottom-left':
        tail_line1 = ' ' * 3 + '\\'
        tail_line2 = ' ' * 2 + '\\'
        tail_line3 = ' ' * 1 + '\\'
    elif tail_pos == 'bottom-right':
        tail_line1 = ' ' * (width - 4) + '/'
        tail_line2 = ' ' * (width - 3) + '/'
        tail_line3 = ' ' * (width - 2) + '/'
    elif tail_pos == 'bottom-center':
        tail_line1 = ' ' * (width // 2 - 1) + '\\/'
        tail_line2 = ' ' * (width // 2) + '\\'
        tail_line3 = ' ' * (width // 2 + 1) + '\\'
    else:
        return bubble

    bubble.append(tail_line1)
    if len(bubble) < 5:
        bubble.append(tail_line2)
    bubble.append(tail_line3)

    return bubble


BANNER_FONTS = {
    'block': {
        'A': ['AAAAA', 'A   A', 'AAAAA', 'A   A', 'A   A'],
        'B': ['BBBB', 'B  B', 'BBBB', 'B  B', 'BBBB'],
        'C': [' CCC', 'C   ', 'C   ', 'C   ', ' CCC'],
        'D': ['DDDD', 'D  D', 'D   D', 'D  D', 'DDDD'],
        'E': ['EEEEE', 'E    ', 'EEE  ', 'E    ', 'EEEEE'],
        'F': ['FFFFF', 'F    ', 'FFF  ', 'F    ', 'F    '],
        'G': [' GGG', 'G   ', 'G  GG', 'G   G', ' GGG'],
        'H': ['H   H', 'H   H', 'HHHHH', 'H   H', 'H   H'],
        'I': ['IIIII', '  I  ', '  I  ', '  I  ', 'IIIII'],
        'J': ['JJJJJ', '   J ', '   J ', 'J  J ', ' JJ '],
        'K': ['K   K', 'K  K ', 'KK   ', 'K  K ', 'K   K'],
        'L': ['L    ', 'L    ', 'L    ', 'L    ', 'LLLLL'],
        'M': ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M'],
        'N': ['N   N', 'NN  N', 'N N N', 'N  NN', 'N   N'],
        'O': [' OOO', 'O   O', 'O   O', 'O   O', ' OOO'],
        'P': ['PPPP', 'P  P', 'PPPP', 'P   ', 'P   '],
        'Q': [' QQQ', 'Q   Q', 'Q Q Q', 'Q  Q ', ' QQ Q'],
        'R': ['RRRR', 'R  R', 'RRRR', 'R  R', 'R   R'],
        'S': [' SSS', 'S   ', ' SSS', '   S', 'SSS '],
        'T': ['TTTTT', '  T  ', '  T  ', '  T  ', '  T  '],
        'U': ['U   U', 'U   U', 'U   U', 'U   U', ' UUU'],
        'V': ['V   V', 'V   V', 'V   V', ' V V ', '  V  '],
        'W': ['W   W', 'W   W', 'W W W', 'WW WW', 'W   W'],
        'X': ['X   X', 'X   X', ' X X ', 'X   X', 'X   X'],
        'Y': ['Y   Y', ' Y Y ', '  Y  ', '  Y  ', '  Y  '],
        'Z': ['ZZZZZ', '   Z ', '  Z  ', ' Z   ', 'ZZZZZ'],
        '0': [' 000', '0   0', '0   0', '0   0', ' 000'],
        '1': ['  1 ', ' 11 ', '  1 ', '  1 ', '11111'],
        '2': [' 222', '2   2', '  22', ' 2  ', '22222'],
        '3': ['3333', '   3', ' 333', '   3', '3333'],
        '4': ['4  4', '4  4', '44444', '   4', '   4'],
        '5': ['55555', '5    ', '5555 ', '    5', '5555 '],
        '6': [' 666', '6   ', '6666 ', '6   6', ' 666'],
        '7': ['77777', '   7 ', '  7  ', ' 7   ', ' 7   '],
        '8': [' 888', '8   8', ' 888', '8   8', ' 888'],
        '9': [' 999', '9   9', ' 9999', '    9', ' 999'],
        '!': ['  !', '  !', '  !', '    ', '  !'],
        '?': [' ???', '   ?', '  ??', '    ?', '  ?'],
        ' ': ['   ', '   ', '   ', '   ', '   '],
        '.': ['   ', '   ', '   ', '   ', ' . '],
        ',': ['   ', '   ', '   ', '  ,', ' ,'],
        "'": [' . ', '  .', '   ', '   ', '   '],
        ':': ['   ', ' . ', '   ', ' . ', '   '],
        '-': ['    ', '    ', 'EEE ', '    ', '    '],
        '_': ['    ', '    ', '    ', '    ', '____'],
    }
}


@mcp.tool()
def create_comic_banner(
    text: str,
    font_style: Literal['block', 'banner1', 'banner2', 'standard'] = 'block',
    emphasis: Literal['none', 'stars', 'underline', 'border'] = 'none',
    align: Literal['left', 'center', 'right'] = 'center',
    width: Optional[int] = None
) -> str:
    """
    Create bold, stylized multi-line text banner in comic style.

    Args:
        text: Text to convert to banner style (uppercase works best)
        font_style: Font style (block=block letters, banner1/banner2=variations, standard=spaced)
        emphasis: Decoration (none, stars, underline, border)
        align: Text alignment within the banner (left, center, right)
        width: Optional minimum width for the banner

    Returns:
        ASCII banner as multi-line string

    Example:
        create_comic_banner(text="HELLO WORLD!!!", font_style='block', emphasis='stars')
    """

    text = text.upper()
    font = BANNER_FONTS.get(font_style, BANNER_FONTS['block'])

    words = text.split()
    char_patterns = []
    for word_idx, word in enumerate(words):
        for char_idx, char in enumerate(word):
            if char in font:
                char_patterns.append(font[char])
            else:
                char_patterns.append(font.get(char.upper(), font[' ']))
        if word_idx < len(words) - 1:
            char_patterns.append(font[' '])

    if not char_patterns:
        return text

    num_lines = len(char_patterns[0])
    result_lines = []

    for line_idx in range(num_lines):
        line = ''
        for pattern in char_patterns:
            if line_idx < len(pattern):
                line += pattern[line_idx] + ' '
        result_lines.append(line.rstrip())

    if width:
        max_len = max(len(line) for line in result_lines)
        padding = width - max_len
        if padding > 0:
            if align == 'center':
                pad_left = padding // 2
                pad_right = padding - pad_left
                result_lines = [' ' * pad_left + line + ' ' * pad_right for line in result_lines]
            elif align == 'right':
                result_lines = [' ' * padding + line for line in result_lines]

    if emphasis == 'stars':
        max_len = max(len(line) for line in result_lines)
        star_line = '★ ' * ((max_len // 2) + 1)
        result_lines.insert(0, star_line[:max_len + 2])
        result_lines.append(star_line[:max_len + 2])
        result_lines = [f'★ {line:<{max_len}} ★' for line in result_lines]
    elif emphasis == 'underline':
        max_len = max(len(line) for line in result_lines)
        result_lines.append('★' * (max_len + 4))
    elif emphasis == 'border':
        max_len = max(len(line) for line in result_lines)
        border_line = '┌' + '─' * (max_len + 2) + '┐'
        result_lines = [f'│ {line:<{max_len}} │' for line in result_lines]
        result_lines.insert(0, border_line)
        result_lines.append('└' + '─' * (max_len + 2) + '┘')

    return '\n'.join(result_lines)


ACTION_EFFECTS = {
    'BANG': [
        ['█████', '█      ', '█████', '    █', '█████'],
        ['█   █', '█      ', '█   █', '█    █', '█   █'],
        ['█   █', '█      ', '█████', '    █', '█   █'],
        ['█   █', '█      ', '█   █', '    █', '█   █'],
        ['█████', '█████ ', '█   █', '    █', '█████'],
    ],
    'BOOM': [
        ['█████', '█   █', '█████', '█   █', '█   █'],
        ['█   █', '█   █', '█   █', '█   █', '█   █'],
        ['█████', '█████', '█████', '█████', '█████'],
        ['█   █', '█   █', '█   █', '█   █', '█   █'],
        ['█   █', '█   █', '█   █', '█   █', '█   █'],
    ],
    'POW': [
        ['█████', '    █', '█████', '    █', '█████'],
        ['█   █', '   █ ', '█████', '   █ ', '█   █'],
        ['█████', '  █  ', ' ███ ', '  █  ', '█████'],
        ['    █', ' █   ', '█████', ' █   ', '    █'],
        ['█████', '█    ', '█████', '█    ', '█████'],
    ],
    'WHAM': [
        ['█████', '█   █', '█████', '█   █', '█   █'],
        ['█   █', '█   █', '█   █', '█   █', '█   █'],
        ['█████', '█████', '█████', '█████', '█████'],
        ['█   █', '█   █', '█   █', '█   █', '█   █'],
        ['█   █', '█   █', '█   █', '█   █', '█   █'],
    ],
    'CRASH': [
        ['█████', '█  ██', '█████', '█  ██', '█   █'],
        ['█   █', '█ █ █', '█   █', '██  █', '█   █'],
        ['█████', '██  █', '█████', '█ █ █', '█   █'],
        ['    █', '█   █', '█   █', '█  ██', '█   █'],
        ['█████', '█   █', '█████', '█   █', '█████'],
    ],
    'ZAP': [
        ['█████', '    █', '█████', '█   █', '█████'],
        ['█   █', '   █ ', '█████', '██  █', '█   █'],
        ['█████', '  █  ', ' ███ ', '█ █ █', '█████'],
        ['    █', ' █   ', '█████', '█  ██', '    █'],
        ['█████', '█    ', '█████', '█   █', '█████'],
    ],
}


@mcp.tool()
def create_action_effect(
    effect_text: Literal['BANG', 'BOOM', 'POW', 'WHAM', 'CRASH', 'ZAP', 'CUSTOM'] = 'BANG',
    size: Literal['small', 'medium', 'large', 'huge'] = 'large',
    style: Literal['bold', 'outlined', 'filled'] = 'bold',
    custom_text: str = ""
) -> str:
    """
    Create comic-style action effect text.

    Args:
        effect_text: Predefined effect word or CUSTOM
        size: Size of the effect (small, medium, large, huge)
        style: Effect style (bold=█, outlined=█ with spacing, filled=full block)
        custom_text: Custom text to display (when effect_text='CUSTOM')

    Returns:
        ASCII action effect as multi-line string

    Example:
        create_action_effect(effect_text='BANG', size='large', style='bold')
    """

    if effect_text == 'CUSTOM':
        text = custom_text.upper() if custom_text else "ZAP"
    else:
        text = effect_text

    size_multipliers = {
        'small': 1,
        'medium': 1,
        'large': 2,
        'huge': 3
    }

    multiplier = size_multipliers.get(size, 1)

    if style == 'filled':
        return _render_filled_effect(text, multiplier)
    elif style == 'outlined':
        return _render_outlined_effect(text, multiplier)
    else:
        return _render_bold_effect(text, multiplier)


def _render_bold_effect(text: str, multiplier: int) -> str:
    """Render bold block letter effect"""
    patterns = []

    for char in text:
        if char in ACTION_EFFECTS:
            patterns.append(ACTION_EFFECTS[char])
        else:
            patterns.append(BANNER_FONTS['block'].get(char, BANNER_FONTS['block'][' ']))

    if not patterns:
        return text

    result_lines = []
    num_lines = len(patterns[0])

    for line_idx in range(num_lines):
        line = ''
        for pattern in patterns:
            if line_idx < len(pattern):
                scaled_line = _scale_line(pattern[line_idx], multiplier)
                line += scaled_line + '  '
        result_lines.append(line.rstrip())

    return '\n'.join(result_lines)


def _render_outlined_effect(text: str, multiplier: int) -> str:
    """Render outlined effect"""
    patterns = []

    for char in text:
        if char in ACTION_EFFECTS:
            patterns.append(ACTION_EFFECTS[char])
        else:
            patterns.append(BANNER_FONTS['block'].get(char, BANNER_FONTS['block'][' ']))

    if not patterns:
        return text

    result_lines = []
    num_lines = len(patterns[0])

    for line_idx in range(num_lines):
        line = ''
        for pattern in patterns:
            if line_idx < len(pattern):
                scaled = _scale_line(pattern[line_idx], multiplier)
                outlined = _make_outlined(scaled)
                line += outlined + '  '
        result_lines.append(line.rstrip())

    return '\n'.join(result_lines)


def _render_filled_effect(text: str, multiplier: int) -> str:
    """Render fully filled effect (no internal spaces)"""
    patterns = []

    for char in text:
        if char in ACTION_EFFECTS:
            patterns.append(ACTION_EFFECTS[char])
        else:
            patterns.append(BANNER_FONTS['block'].get(char, BANNER_FONTS['block'][' ']))

    if not patterns:
        return text

    result_lines = []
    num_lines = len(patterns[0])

    for line_idx in range(num_lines):
        line = ''
        for pattern in patterns:
            if line_idx < len(pattern):
                filled = _fill_line(pattern[line_idx], multiplier)
                line += filled + '  '
        result_lines.append(line.rstrip())

    return '\n'.join(result_lines)


def _scale_line(line: str, multiplier: int) -> str:
    """Scale a line horizontally"""
    result = ''
    for char in line:
        result += char * multiplier
    return result


def _make_outlined(line: str) -> str:
    """Convert solid line to outlined version"""
    result = ''
    for char in line:
        if char == ' ':
            result += ' '
        else:
            result += '█'
    return result


def _fill_line(line: str, multiplier: int) -> str:
    """Fill all non-space characters"""
    result = ''
    for char in line:
        if char == ' ':
            result += ' ' * multiplier
        else:
            result += '█' * multiplier
    return result


@mcp.tool()
def create_comic_panel(
    title: str = "",
    top_text: str = "",
    bottom_text: str = "",
    panel_count: int = 1
) -> str:
    """
    Create a comic panel frame with optional title and text areas.

    Args:
        title: Optional title at top of panel
        top_text: Text in upper area of panel
        bottom_text: Text in lower area of panel
        panel_count: Number of panels to create (1-3)

    Returns:
        ASCII comic panel as multi-line string

    Example:
        create_comic_panel(title="EPISODE 1", top_text="Meanwhile...",
                         bottom_text="To be continued...")
    """

    width = 60
    chars = UNICODE_SETS['heavy']

    lines = []

    top_border = chars['top_left'] + chars['horizontal'] * (width - 2) + chars['top_right']
    lines.append(top_border)

    if title:
        title_line = f"│{title.center(width - 4)}│"
        lines.append(title_line)
        sep = chars['t_right'] + chars['horizontal'] * (width - 2) + chars['t_left']
        lines.append(sep)

    if top_text:
        for text_line in top_text.split('\n'):
            padded = text_line.center(width - 4)
            lines.append(f"│{padded}│")

    mid_line = chars['cross'] + chars['horizontal'] * (width - 2) + chars['cross']
    lines.append(mid_line)

    if bottom_text:
        for text_line in bottom_text.split('\n'):
            padded = text_line.center(width - 4)
            lines.append(f"│{padded}│")

    bottom_border = chars['bottom_left'] + chars['horizontal'] * (width - 2) + chars['bottom_right']
    lines.append(bottom_border)

    return '\n'.join(lines)


@mcp.tool()
def draw_shape(
    shape_type: Literal['circle', 'oval', 'rectangle', 'star', 'arrow', 'cloud'],
    width: int = 20,
    height: int = 10,
    fill_char: str = '█',
    border_char: str = '─'
) -> str:
    """
    Draw a generic shape that can be used in compositions.

    Args:
        shape_type: Type of shape to draw
        width: Width of shape in characters
        height: Height of shape in characters
        fill_char: Character to use for filling
        border_char: Character to use for borders

    Returns:
        Shape as multi-line ASCII art

    Example:
        draw_shape(shape_type='cloud', width=30, height=5)
    """

    if shape_type == 'circle' or shape_type == 'oval':
        return _draw_ellipse(width, height, fill_char, border_char)
    elif shape_type == 'rectangle':
        return _draw_rectangle(width, height, fill_char, border_char)
    elif shape_type == 'star':
        return _draw_star(width, height, fill_char)
    elif shape_type == 'arrow':
        return _draw_arrow(width, height, fill_char)
    elif shape_type == 'cloud':
        return _draw_cloud(width, height, fill_char, border_char)
    else:
        return _draw_rectangle(width, height, fill_char, border_char)


def _draw_ellipse(width: int, height: int, fill: str, border: str) -> str:
    """Draw an ellipse shape"""
    lines = []
    center_x = width / 2
    center_y = height / 2
    radius_x = width / 2 - 1
    radius_y = height / 2 - 1

    for y in range(height):
        line = ''
        for x in range(width):
            dx = (x - center_x) / (radius_x if radius_x > 0 else 1)
            dy = (y - center_y) / (radius_y if radius_y > 0 else 1)
            dist = dx * dx + dy * dy
            if dist < 0.9:
                line += fill
            elif dist < 1.1:
                line += border
            else:
                line += ' '
        lines.append(line)
    return '\n'.join(lines)


def _draw_rectangle(width: int, height: int, fill: str, border: str) -> str:
    """Draw a rectangle shape"""
    lines = []
    lines.append(border * width)
    for y in range(height - 2):
        lines.append(border + fill * (width - 2) + border)
    lines.append(border * width)
    return '\n'.join(lines)


def _draw_star(width: int, height: int, fill: str) -> str:
    """Draw a star shape"""
    lines = []
    center = width // 2
    for y in range(height):
        line = ' ' * width
        if y < height // 3:
            line_list = list(line)
            line_list[center] = fill
            if center - 1 >= 0:
                line_list[center - 1] = fill
            if center + 1 < width:
                line_list[center + 1] = fill
            line = ''.join(line_list)
        elif y < height * 2 // 3:
            line = fill * width
        else:
            line_list = list(line)
            line_list[center] = fill
            line = ''.join(line_list)
        lines.append(line)
    return '\n'.join(lines)


def _draw_arrow(width: int, height: int, fill: str) -> str:
    """Draw an arrow shape (for motion/direction)"""
    lines = []
    for y in range(height):
        line = ' ' * width
        if y == height // 2:
            line = fill * width
        elif y < height // 2:
            line_list = list(line)
            pos = width - 1 - (height // 2 - y)
            if 0 <= pos < width:
                line_list[pos] = fill
            line = ''.join(line_list)
        else:
            line_list = list(line)
            pos = width - 1 - (y - height // 2)
            if 0 <= pos < width:
                line_list[pos] = fill
            line = ''.join(line_list)
        lines.append(line)
    return '\n'.join(lines)


def _draw_cloud(width: int, height: int, fill: str, border: str) -> str:
    """Draw a cloud shape (generic, customizable)"""
    lines = []
    for y in range(height):
        line = ''
        for x in range(width):
            y_center = height / 2
            x_center1 = width / 4
            x_center2 = width / 2
            x_center3 = width * 3 / 4
            
            dx1 = (x - x_center1) / (width / 4)
            dy1 = (y - y_center) / (height / 2)
            dist1 = dx1 * dx1 + dy1 * dy1
            
            dx2 = (x - x_center2) / (width / 3)
            dy2 = (y - y_center) / (height / 3)
            dist2 = dx2 * dx2 + dy2 * dy2
            
            dx3 = (x - x_center3) / (width / 4)
            dy3 = (y - y_center) / (height / 2)
            dist3 = dx3 * dx3 + dy3 * dy3
            
            if dist1 < 0.8 or dist2 < 0.7 or dist3 < 0.8:
                line += fill
            elif dist1 < 1.0 or dist2 < 0.9 or dist3 < 1.0:
                line += border
            else:
                line += ' '
        lines.append(line)
    return '\n'.join(lines)


@mcp.tool()
def compose_elements(
    elements: List[str],
    layout: Literal['vertical', 'horizontal', 'overlap'] = 'vertical',
    spacing: int = 1
) -> str:
    """
    Compose multiple ASCII art elements together.

    Args:
        elements: List of ASCII art strings to compose
        layout: How to arrange the elements
        spacing: Number of empty lines between elements

    Returns:
        Composed ASCII art as multi-line string

    Example:
        compose_elements([cloud1, car, speech_bubble], layout='vertical')
    """

    def get_element_dims(element: str):
        lines = element.split('\n')
        max_width = max(len(line) for line in lines) if lines else 0
        return lines, max_width

    if layout == 'vertical':
        if not elements:
            return ''

        element_data = [get_element_dims(e) for e in elements]
        max_width = max(width for _, width in element_data)

        result = []
        for i, (lines, _) in enumerate(element_data):
            for line in lines:
                if len(line) < max_width:
                    result.append(line + ' ' * (max_width - len(line)))
                else:
                    result.append(line)
            if i < len(elements) - 1:
                result.extend([''] * spacing)
        return '\n'.join(result)

    elif layout == 'horizontal':
        element_lines_list = []
        element_widths = []
        for e in elements:
            lines, width = get_element_dims(e)
            element_widths.append(width)
            element_lines_list.append(lines)

        max_height = max(len(lines) for lines in element_lines_list)
        result = []
        for y in range(max_height):
            line = ''
            for i, lines in enumerate(element_lines_list):
                if y < len(lines):
                    line += lines[y]
                else:
                    line += ' ' * element_widths[i]
                if i < len(elements) - 1:
                    line += ' ' * spacing
            result.append(line)
        return '\n'.join(result)

    else:
        return elements[0] if elements else ''


@mcp.tool()
def add_effect(
    ascii_art: str,
    effect_type: Literal['motion_lines', 'sparkles', 'skid_marks', 'shadow'],
    position: Literal['top', 'bottom', 'left', 'right'] = 'bottom',
    intensity: int = 3
) -> str:
    """
    Add visual effects to existing ASCII art.

    Args:
        ascii_art: The ASCII art to modify
        effect_type: Type of effect to add
        position: Where to place the effect
        intensity: Intensity of the effect (1-5)

    Returns:
        Modified ASCII art with effects

    Example:
        add_effect(car_art, effect_type='motion_lines', position='left', intensity=4)
    """

    lines = ascii_art.split('\n')
    if not lines:
        return ascii_art

    width = max(len(line) for line in lines)
    result = lines.copy()

    if effect_type == 'motion_lines':
        if position == 'left':
            for y in range(len(result)):
                line = result[y]
                prefix = '~' * intensity if y % 2 == 0 else '-' * intensity
                result[y] = prefix + line
        elif position == 'right':
            for y in range(len(result)):
                line = result[y]
                suffix = '~' * intensity if y % 2 == 0 else '-' * intensity
                result[y] = line + suffix

    elif effect_type == 'skid_marks':
        skid_line = '  ' * intensity + '─' * (width // 2) + '  ' * intensity
        for _ in range(intensity):
            result.append(skid_line)

    elif effect_type == 'sparkles':
        for y in range(len(result)):
            if y % 3 == 0:
                line_list = list(result[y].ljust(width))
                for x in range(0, width, 4):
                    if x < len(line_list):
                        line_list[x] = '*' if line_list[x] == ' ' else line_list[x]
                result[y] = ''.join(line_list)

    return '\n'.join(result)


# ============================================================================
# ASCII MODE - Toggleable ASCII Art Response Enhancement
# ============================================================================

from dataclasses import dataclass, field
from typing import Set, Literal, Optional
import re

@dataclass
class ASCIIModeConfig:
    features: Set[Literal['box', 'banner', 'art']] = field(default_factory=lambda: {'box', 'banner', 'art'})
    show_dialog_on_entry: Literal['always', 'first', 'never'] = 'first'
    has_entered_before: bool = False
    line_style: Literal['light', 'heavy', 'double', 'rounded'] = 'rounded'
    max_width: int = 40


class ASCIIModeManager:
    _instance: Optional['ASCIIModeManager'] = None

    def __init__(self):
        self.state: Literal['inactive', 'active', 'showing_dialog'] = 'inactive'
        self.config = ASCIIModeConfig()
        ASCIIModeManager._instance = self

    @classmethod
    def get_instance(cls) -> 'ASCIIModeManager':
        if cls._instance is None:
            cls._instance = ASCIIModeManager()
        return cls._instance

    def enter_mode(self, force_dialog: bool = False) -> str:
        should_show_dialog = False

        if force_dialog:
            should_show_dialog = True
        elif self.config.show_dialog_on_entry == 'always':
            should_show_dialog = True
        elif self.config.show_dialog_on_entry == 'first' and not self.config.has_entered_before:
            should_show_dialog = True

        if should_show_dialog:
            self.state = 'showing_dialog'
            return self._show_dialog()
        else:
            self.state = 'active'
            return self._get_activation_message()

    def _show_dialog(self) -> str:
        return INTERACTIVE_DIALOG

    def _get_activation_message(self) -> str:
        features_str = ', '.join(sorted(self.config.features))
        return (
            f"╔═══════════════════════════════════════════════════════════════╗\n"
            f"║                 ASCII MODE ACTIVATED                          ║\n"
            f"╠═══════════════════════════════════════════════════════════════╣\n"
            f"║  Features: {features_str:<48} ║\n"
            f"║  Style: {self.config.line_style:<51} ║\n"
            f"╠═══════════════════════════════════════════════════════════════╣\n"
            f"║  All responses will be enhanced with ASCII art formatting.   ║\n"
            f"║  Type 'exit ASCII mode' to deactivate.                       ║\n"
            f"║  Type 'ascii config show' to view configuration.            ║\n"
            f"╚═══════════════════════════════════════════════════════════════╝"
        )

    def exit_mode(self) -> str:
        self.state = 'inactive'
        return (
            "╔═══════════════════════════════════════════════════════════════╗\n"
            "║                 ASCII MODE DEACTIVATED                         ║\n"
            "╠═══════════════════════════════════════════════════════════════╣\n"
            "║  Responses will return to normal text format.                 ║\n"
            "║  Type 'enter ASCII mode' to reactivate.                       ║\n"
            "╚═══════════════════════════════════════════════════════════════╝"
        )

    def handle_dialog_choice(self, choice: str) -> str:
        self.state = 'active'
        self.config.has_entered_before = True
        return self._get_activation_message()

    def get_status(self) -> dict:
        return {
            "state": self.state,
            "is_active": self.state == 'active',
            "config": {
                "features": list(self.config.features),
                "show_dialog_on_entry": self.config.show_dialog_on_entry,
                "has_entered_before": self.config.has_entered_before,
                "line_style": self.config.line_style,
                "max_width": self.config.max_width
            }
        }

    def set_config(self, key: str, value: str) -> str:
        if key == 'features':
            if value == 'all':
                self.config.features = {'box', 'banner', 'art'}
            else:
                features = [f.strip() for f in value.split(',')]
                valid = {'box', 'banner', 'art'}
                self.config.features = set(f for f in features if f in valid)
            return f"Features updated to: {', '.join(sorted(self.config.features))}"

        elif key == 'dialog':
            if value in ('always', 'first', 'never'):
                self.config.show_dialog_on_entry = value
                return f"Dialog behavior set to: {value}"
            else:
                return f"Invalid dialog value. Use: always, first, never"

        elif key == 'style':
            if value in ('light', 'heavy', 'double', 'rounded'):
                self.config.line_style = value
                return f"Line style set to: {value}"
            else:
                return f"Invalid style. Use: light, heavy, double, rounded"

        elif key == 'width':
            try:
                width = int(value)
                if 20 <= width <= 120:
                    self.config.max_width = width
                    return f"Max width set to: {width}"
                else:
                    return f"Invalid width. Use a value between 20 and 120"
            except ValueError:
                return f"Invalid width. Use a number between 20 and 120"

        else:
            return f"Unknown config key: {key}. Use: features, dialog, style, width"

    def transform_response(self, text: str, is_ai_response: bool = True) -> str:
        if self.state != 'active':
            return text

        if not text.strip():
            return text

        lines_to_box = []

        # Feature B: Banner Text - extract key phrase and create banner
        if 'banner' in self.config.features:
            banner_text = self._extract_key_phrase(text)
            if banner_text:
                try:
                    banner = pyfiglet.figlet_format(banner_text, font='mini')
                    lines_to_box.append(banner)
                except Exception:
                    pass

        # Feature C: ASCII Art - generate complementary art
        if 'art' in self.config.features:
            art = self._generate_complementary_art(text)
            if art:
                lines_to_box.append(art)

        # Always add the original text
        lines_to_box.append(text)

        composed = '\n\n'.join(lines_to_box)

        # Feature A: Box Wrapping - wrap everything in a box
        if 'box' in self.config.features:
            lines = composed.split('\n')

            art_chars = set('░▒▓█★╭╮╰╯─│┌┐└┘★•○●◉')
            max_box_width = self.config.max_width
            max_text_width = max_box_width - 2

            def is_decorative_line(line):
                if not line:
                    return False
                art_count = sum(1 for c in line if c in art_chars)
                return art_count > len(line) * 0.3

            wrapped_lines = []
            for line in lines:
                if is_decorative_line(line):
                    # Truncate decorative lines to fit box width
                    if len(line) > max_box_width - 4:
                        wrapped_lines.append(('art', line[:max_box_width - 6] + '..'))
                    else:
                        wrapped_lines.append(('art', line))
                else:
                    # Wrap text at 38 chars
                    if len(line) <= max_text_width:
                        wrapped_lines.append(('text', line))
                    else:
                        words = line.split()
                        current = ''
                        for word in words:
                            if len(current) + len(word) + 1 <= max_text_width:
                                current = (current + ' ' + word).strip()
                            else:
                                if current:
                                    wrapped_lines.append(('text', current))
                                current = word
                        if current:
                            wrapped_lines.append(('text', current))

            chars = UNICODE_SETS[self.config.line_style]
            box_width = max_box_width

            box_lines = []
            top_border = chars['top_left'] + chars['horizontal'] * (box_width - 2) + chars['top_right']
            box_lines.append(top_border)

            inner_width = box_width - 2
            for line_type, line in wrapped_lines:
                if len(line) <= inner_width:
                    padding = (inner_width - len(line)) // 2
                    box_lines.append(chars['vertical'] + ' ' * padding + line + ' ' * (inner_width - len(line) - padding) + chars['vertical'])
                else:
                    box_lines.append(chars['vertical'] + line[:inner_width-2] + '..' + chars['vertical'])

            bottom_border = chars['bottom_left'] + chars['horizontal'] * (box_width - 2) + chars['bottom_right']
            box_lines.append(bottom_border)

            return '\n'.join(box_lines)

        return composed

    def _extract_key_phrase(self, text: str) -> str:
        text_clean = re.sub(r'[^\w\s]', '', text)
        words = text_clean.split()

        priority_keywords = ['thank', 'hello', 'hi', 'hey', 'wow', 'amazing', 'awesome', 'great', 'yes', 'cool', 'correct', 'love', 'happy', 'sorry', 'wrong', 'no', 'error', 'great']

        for word in words:
            if len(word) < 4:
                continue
            word_lower = word.lower()
            if any(keyword in word_lower for keyword in priority_keywords):
                return word.upper()

        return ''

    def _generate_complementary_art(self, text: str) -> str:
        text_lower = text.lower()

        if any(word in text_lower for word in ['hello', 'hi', 'hey', 'greetings']):
            return create_speech_bubble(
                text="HOWDY!",
                bubble_style='oval',
                tail_position='bottom-left',
                line_style='rounded'
            )
        elif any(word in text_lower for word in ['thank', 'thanks', 'appreciate']):
            return create_speech_bubble(
                text="MUCH obliged!",
                bubble_style='oval',
                tail_position='bottom-right',
                line_style='rounded'
            )
        elif any(word in text_lower for word in ['great', 'awesome', 'fantastic']):
            return create_speech_bubble(
                text="RIGHT ON!",
                bubble_style='rectangular',
                tail_position='bottom-left',
                line_style='rounded'
            )
        elif any(word in text_lower for word in ['yes', 'yeah', 'yep', 'correct']):
            return create_speech_bubble(
                text="YEP!",
                bubble_style='cloud',
                tail_position='bottom-right',
                line_style='rounded'
            )
        elif any(word in text_lower for word in ['wow', 'amazing', 'cool']):
            return create_action_effect('BOOM', size='medium', style='bold')
        elif any(word in text_lower for word in ['no', 'nope', 'not', 'wrong', 'error']):
            return create_action_effect('ERROR', size='medium', style='bold')

        return ''


INTERACTIVE_DIALOG = """╔═══════════════════════════════════════════════════════════════╗
║                    ASCII MODE - Select Features                   ║
╠═══════════════════════════════════════════════════════════════╣
║  [X] A) Box Wrapping    - Wrap responses in bordered box        ║
║  [X] B) Banner Text     - Transform text to block letters       ║
║  [X] C) ASCII Art       - Add complementary ASCII drawings     ║
╠═══════════════════════════════════════════════════════════════╣
║  Dialog Behavior: First time only                               ║
║  [>] Change                                                           ║
╠═══════════════════════════════════════════════════════════════╣
║  [S] Save & Continue (Default: A+B+C)    [C] Cancel              ║
╚═══════════════════════════════════════════════════════════════╝

To customize features, use: ascii config set features=box,banner,art
To change dialog behavior: ascii config set dialog=always|first|never"""


@mcp.tool()
def enter_ascii_mode(options: bool = False) -> str:
    """
    Enter ASCII mode to enable ASCII art-enhanced responses.

    When active, all responses will be formatted with ASCII art elements
    including bordered boxes, banner text, and complementary drawings.

    Args:
        options: If True, force showing the feature selection dialog

    Returns:
        ASCII art confirmation message

    Example:
        enter_ascii_mode()           # Enter with default settings
        enter_ascii_mode(options=True)  # Force show feature dialog
    """
    manager = ASCIIModeManager.get_instance()
    return manager.enter_mode(force_dialog=options)


@mcp.tool()
def exit_ascii_mode() -> str:
    """
    Exit ASCII mode and return to normal text responses.

    Returns:
        ASCII art confirmation message

    Example:
        exit_ascii_mode()
    """
    manager = ASCIIModeManager.get_instance()
    return manager.exit_mode()


@mcp.tool()
def get_ascii_mode_status() -> dict:
    """
    Get the current ASCII mode status and configuration.

    Returns:
        Dictionary containing mode state and configuration

    Example:
        get_ascii_mode_status()
    """
    manager = ASCIIModeManager.get_instance()
    return manager.get_status()


@mcp.tool()
def ascii_config_show() -> str:
    """
    Display the current ASCII mode configuration.

    Returns:
        ASCII art formatted configuration display

    Example:
        ascii_config_show()
    """
    manager = ASCIIModeManager.get_instance()
    status = manager.get_status()
    config = status['config']

    features_str = ', '.join(config['features']) if config['features'] else 'none'

    return (
        f"╔═══════════════════════════════════════════════════════════════╗\n"
        f"║                 ASCII MODE CONFIGURATION                        ║\n"
        f"╠═══════════════════════════════════════════════════════════════╣\n"
        f"║  State: {status['state']:<51} ║\n"
        f"║  Active: {str(config['has_entered_before']).upper():<48} ║\n"
        f"╠═══════════════════════════════════════════════════════════════╣\n"
        f"║  Features:                                                     ║\n"
        f"║    [X] Box Wrapping (A)                                        ║\n"
        f"║    [X] Banner Text (B)                                          ║\n"
        f"║    [X] ASCII Art (C)                                            ║\n"
        f"╠═══════════════════════════════════════════════════════════════╣\n"
        f"║  Dialog Behavior: {config['show_dialog_on_entry']:<41} ║\n"
        f"║  Line Style: {config['line_style']:<47} ║\n"
        f"║  Max Width: {config['max_width']:<47} ║\n"
        f"╠═══════════════════════════════════════════════════════════════╣\n"
        f"║  Commands:                                                     ║\n"
        f"║    ascii config set features=box,banner,art    (customize)     ║\n"
        f"║    ascii config set dialog=always|first|never (dialog behavior)║\n"
        f"║    ascii config set style=rounded|heavy|light|double          ║\n"
        f"║    ascii config set width=40                (20-120, default)  ║\n"
        f"╚═══════════════════════════════════════════════════════════════╝"
    )


@mcp.tool()
def ascii_config_set(key: str, value: str) -> str:
    """
    Set ASCII mode configuration options.

    Args:
        key: Configuration key (features, dialog, style, width)
        value: Configuration value

    Returns:
        ASCII art confirmation message

    Example:
        ascii_config_set(key='features', value='box,banner')
        ascii_config_set(key='dialog', value='always')
        ascii_config_set(key='style', value='heavy')
        ascii_config_set(key='width', value='60')
    """
    manager = ASCIIModeManager.get_instance()
    result = manager.set_config(key, value)

    return (
        f"╔═══════════════════════════════════════════════════════════════╗\n"
        f"║                 ASCII MODE CONFIG UPDATED                       ║\n"
        f"╠═══════════════════════════════════════════════════════════════╣\n"
        f"║  {result:<60} ║\n"
        f"╚═══════════════════════════════════════════════════════════════╝"
    )


@mcp.tool()
def transform_to_ascii_mode(text: str) -> str:
    """
    Transform arbitrary text using the ASCII mode pipeline.
    This allows testing the transformation without entering ASCII mode.

    Args:
        text: The text to transform

    Returns:
        ASCII art transformed text

    Example:
        transform_to_ascii_mode(text="Hello World!")
    """
    manager = ASCIIModeManager.get_instance()
    return manager.transform_response(text, is_ai_response=True)


# ============================================================================
# PIP-BOY MODE - Fallout-style Vault Boy with Speech Bubble
# ============================================================================

PIP_BOY_CHARS = {
    'horizontal': '═', 'vertical': '║',
    'top_left': '╔', 'top_right': '╗',
    'bottom_left': '╚', 'bottom_right': '╝',
}


class PipBoyModeManager:
    """
    Pip-Boy mode renders Vault Boy with a speech bubble containing user text.
    Text is properly wrapped to fit within the bubble without indentation issues.
    """

    _instance: Optional['PipBoyModeManager'] = None

    def __init__(self):
        self.state: Literal['inactive', 'active'] = 'inactive'
        PipBoyModeManager._instance = self

    @classmethod
    def get_instance(cls) -> 'PipBoyModeManager':
        if cls._instance is None:
            cls._instance = PipBoyModeManager()
        return cls._instance

    def enter_mode(self) -> str:
        self.state = 'active'
        return self._get_activation_message()

    def _get_activation_message(self) -> str:
        boot_lines = [
            "ROBCO INDUSTRIES (TM) TERMALIST",
            "PIP-BOY 3000 MARK V v1.0",
            "(C)2075-2077 ROBCO INDUSTRIES",
            "- SERVER 1 -",
            "",
            "INITIALIZING PIP-OS...",
            "LOADING USER PROFILE...",
            "VAULT BOY MASCOT READY",
        ]

        width = 58
        lines = []
        lines.append("╔" + "═" * (width - 2) + "╗")
        lines.append("║" + " " * (width - 2) + "║")

        for boot_line in boot_lines:
            padding = width - 2 - len(boot_line)
            lines.append("║  " + boot_line + " " * (padding - 2) + "║")

        lines.append("║" + " " * (width - 2) + "║")
        lines.append("╠" + "═" * (width - 2) + "╣")
        lines.append("║  PIP-BOY MODE ACTIVATED                                     ║")
        lines.append("║  Vault Boy will appear with speech bubbles for responses.    ║")
        lines.append("║  Type 'exit pip-boy mode' to deactivate.                   ║")
        lines.append("╚" + "═" * (width - 2) + "╝")

        return '\n'.join(lines)

    def exit_mode(self) -> str:
        self.state = 'inactive'
        lines = []
        width = 58
        lines.append("╔" + "═" * (width - 2) + "╗")
        lines.append("║" + " " * (width - 2) + "║")
        lines.append("║  PIP-BOY MODE DEACTIVATED                                   ║")
        lines.append("║  Responses will return to normal text format.              ║")
        lines.append("║  Type 'enter pip-boy mode' to reactivate.                   ║")
        lines.append("║" + " " * (width - 2) + "║")
        lines.append("║  SAVING DATA...                                              ║")
        lines.append("║  CLOSING PIP-OS...                                          ║")
        lines.append("║  GOODBYE!                                                    ║")
        lines.append("║" + " " * (width - 2) + "║")
        lines.append("╚" + "═" * (width - 2) + "╝")
        return '\n'.join(lines)

    def get_status(self) -> dict:
        return {
            "state": self.state,
            "is_active": self.state == 'active',
        }

    def _wrap_text(self, text: str, max_width: int) -> List[str]:
        """
        Wrap text to fit within max_width without indentation problems.
        Handles long words by breaking them at max_width.
        """
        wrapped_lines = []
        lines = text.split('\n')

        for line in lines:
            if not line:
                wrapped_lines.append('')
                continue

            words = line.split()
            current_line = ''
            current_len = 0

            for word in words:
                word_len = len(word)

                if current_len == 0:
                    if word_len > max_width:
                        while word_len > max_width:
                            wrapped_lines.append(word[:max_width])
                            word = word[max_width:]
                            word_len = len(word)
                        current_line = word
                        current_len = word_len
                    else:
                        current_line = word
                        current_len = word_len
                elif current_len + 1 + word_len <= max_width:
                    current_line += ' ' + word
                    current_len += 1 + word_len
                else:
                    wrapped_lines.append(current_line)
                    current_line = word
                    current_len = word_len

            if current_line:
                wrapped_lines.append(current_line)

        return wrapped_lines

    def _create_speech_bubble(self, text: str, max_width: int = 36) -> str:
        """
        Create a Fallout-style speech bubble with properly wrapped text.
        """
        wrapped_lines = self._wrap_text(text, max_width)

        if not wrapped_lines:
            wrapped_lines = ['']

        bubble_width = min(max(len(line) for line in wrapped_lines) + 4, max_width + 4)

        lines = []
        top_border = f"╔{'═' * (bubble_width - 2)}╗"
        lines.append(top_border)

        for line in wrapped_lines:
            padding = bubble_width - 2 - len(line)
            left_pad = padding // 2
            right_pad = padding - left_pad
            lines.append(f"║{' ' * left_pad}{line}{' ' * right_pad}║")

        bottom_border = f"╚{'═' * (bubble_width - 2)}╝"
        lines.append(bottom_border)

        tail_line1 = ' ' * 4 + '╚' + '═' * 3 + '╝'
        tail_line2 = ' ' * 3 + '╚' + '═' * 5 + '╝'
        tail_line3 = ' ' * 2 + '╚' + '═' * 7 + '╝'

        lines.append(tail_line1)
        lines.append(tail_line2)
        lines.append(tail_line3)

        return '\n'.join(lines)

    def transform_response(self, text: str, force: bool = False) -> str:
        """
        Transform response by adding Vault Boy with speech bubble.
        Fallout-style Pip-Boy 3000 interface with speech bubble.

        Args:
            text: The text to transform
            force: If True, always transform regardless of mode state
        """
        if self.state != 'active' and not force:
            return text

        if not text.strip():
            return text

        vault_boy = generate_vault_boy(size='small')
        speech_bubble = self._create_speech_bubble(text, max_width=24)

        combined = compose_elements([vault_boy, speech_bubble], layout='horizontal', spacing=2)

        width = 64
        inner_width = width - 2

        lines = []
        lines.append("╔" + "═" * inner_width + "╗")

        header_line = "  ═══ PIP-BOY 3000 MARK V ═══"
        header_padding = inner_width - len(header_line)
        lines.append("║" + header_line + " " * header_padding + "║")

        divider_content = "─" * (inner_width - 4)
        lines.append("║  " + divider_content + "  ║")

        lines.append("║" + " " * inner_width + "║")

        content_lines = combined.split('\n')
        max_content_lines = 14

        for line in content_lines[:max_content_lines]:
            line_len = len(line)
            if line_len > inner_width - 4:
                line = line[:inner_width - 7] + "..."
                line_len = len(line)

            padding = inner_width - 2 - line_len
            lines.append("║ " + line + " " * padding + " ║")

        lines.append("║" + " " * inner_width + "║")
        lines.append("║  " + divider_content + "  ║")

        nav_buttons = "[RADIO] [STATUS] [DATA] [MAP]"
        nav_padding = inner_width - len(nav_buttons)
        lines.append("║" + nav_buttons + " " * nav_padding + "║")

        lines.append("╚" + "═" * inner_width + "╝")

        return '\n'.join(lines)


_pip_boy_manager: Optional[PipBoyModeManager] = None


def get_pip_boy_manager() -> PipBoyModeManager:
    """Get or create the Pip-Boy manager singleton."""
    global _pip_boy_manager
    if _pip_boy_manager is None:
        _pip_boy_manager = PipBoyModeManager()
    return _pip_boy_manager


@mcp.tool()
def enter_pip_boy_mode() -> str:
    """
    Enter Pip-Boy mode to enable Vault Boy responses with speech bubbles.

    When active, Vault Boy will appear with speech bubbles containing responses.
    Text is automatically wrapped to fit within the bubble.

    Returns:
        ASCII art confirmation message

    Example:
        enter_pip_boy_mode()
    """
    manager = get_pip_boy_manager()
    return manager.enter_mode()


@mcp.tool()
def exit_pip_boy_mode() -> str:
    """
    Exit Pip-Boy mode and return to normal text responses.

    Returns:
        ASCII art confirmation message

    Example:
        exit_pip_boy_mode()
    """
    manager = get_pip_boy_manager()
    return manager.exit_mode()


@mcp.tool()
def get_pip_boy_status() -> dict:
    """
    Get the current Pip-Boy mode status.

    Returns:
        Dictionary containing mode state

    Example:
        get_pip_boy_status()
    """
    manager = get_pip_boy_manager()
    return manager.get_status()


@mcp.tool()
def transform_to_pip_boy(text: str) -> str:
    """
    Transform text using Pip-Boy mode (Vault Boy with speech bubble).
    This allows testing the transformation without entering Pip-Boy mode.

    Args:
        text: The text to transform

    Returns:
        Vault Boy ASCII art with speech bubble

    Example:
        transform_to_pip_boy(text="Hello, world!")
    """
    manager = get_pip_boy_manager()
    return manager.transform_response(text, force=True)


# ============================================================================
# ASCII Art Generator Tools
# ============================================================================

@mcp.tool()
def generate_ascii_art(
    subject: str,
    style: Literal['default', 'detailed', 'simple'] = 'default'
) -> str:
    """
    Generate ASCII art based on a subject description.
    Uses pre-defined templates for recognizable objects like animals, nature, vehicles, etc.

    Args:
        subject: Description of what to draw (e.g., 'a dog', 'a cat', 'a tree', 'a house')
        style: Art style (default, detailed, simple)

    Returns:
        ASCII art representation of the subject

    Example:
        generate_ascii_art(subject='a dog running')
        generate_ascii_art(subject='a cat')
        generate_ascii_art(subject='a house')
    """
    template = get_template(subject)

    if template:
        return template

    return f"Sorry, I don't have a template for '{subject}'. Try: {', '.join(list_available_templates()[:5])}..."


@mcp.tool()
def list_ascii_art_templates() -> Dict[str, Any]:
    """
    List all available ASCII art templates that can be generated.

    Returns:
        Dictionary of available templates with descriptions

    Example:
        list_ascii_art_templates()
    """
    templates = list_available_templates()

    categories = {
        'animals': ['dog', 'cat', 'bird', 'fish', 'person'],
        'nature': ['tree', 'flower', 'mountain', 'sun', 'moon', 'cloud'],
        'buildings_vehicles': ['house', 'car', 'rocket', 'boat'],
        'objects': ['heart', 'star', 'computer', 'phone', 'book', 'cup', 'bottle']
    }

    result = {"available_templates": templates, "by_category": {}}

    for category, items in categories.items():
        result["by_category"][category] = [t for t in items if t in templates]

    result["total_count"] = len(templates)
    result["example_usage"] = "generate_ascii_art(subject='a dog')"

    return result


# ============================================================================
# Database Management Tools
# ============================================================================

@mcp.tool()
def get_database_stats() -> Dict[str, Any]:
    """
    Get statistics about the ASCII art database.

    Returns:
        Dictionary with database statistics

    Example:
        get_database_stats()
    """
    db_path = os.path.join(os.path.dirname(__file__), 'ascii_art.db')

    if not os.path.exists(db_path):
        return {
            "status": "no_database",
            "message": "Database not initialized yet",
            "available_templates": len(ASCII_TEMPLATES)
        }

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('SELECT COUNT(*) as count FROM ascii_art')
        total_count = cursor.fetchone()[0]

        cursor.execute('''
            SELECT category, COUNT(*) as count
            FROM ascii_art
            GROUP BY category
            ORDER BY count DESC
            LIMIT 10
        ''')
        categories = [{"category": row[0], "count": row[1]} for row in cursor.fetchall()]

        cursor.execute('''
            SELECT
                AVG(width) as avg_width,
                AVG(height) as avg_height,
                AVG(complexity_score) as avg_complexity
            FROM ascii_art
        ''')
        row = cursor.fetchone()
        averages = {
            "avg_width": round(row[0] or 0, 1),
            "avg_height": round(row[1] or 0, 1),
            "avg_complexity": round(row[2] or 0, 2)
        }

        conn.close()

        return {
            "status": "connected",
            "total_ascii_art": total_count,
            "categories": categories,
            "averages": averages,
            "available_templates": len(ASCII_TEMPLATES)
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "available_templates": len(ASCII_TEMPLATES)
        }


# ============================================================================
# VAULT BOY ASCII ART - Scalable Character Rendering
# ============================================================================

VAULT_BOY_ART = """
Vault Boy
⢀⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾
⣿⠟⠋⠉⠉⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠻⣿⣿
⣿⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣿
⣿⣾⣿⣿⣿⣿⣿⡟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻⣿⣿⣿
⣿⡿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻⣿
⣿⣇⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣸
⣿⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿
⣿⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀
⣿⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉
⣿⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀
⣿⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻
"""


class VaultBoyScaler:
    """
    Scalable rendering engine for Vault Boy ASCII art.
    Maintains visual integrity across different scaling factors.
    """

    PRESERVED_CHARACTERS = {
        'empty': ' ',
        'light_shade': '░',
        'medium_shade': '▒',
        'dark_shade': '▓',
        'full_block': '█',
        'braille_blank': '⠀',
    }

    SCALING_MODES = {
        'fast': 'Nearest neighbor scaling - fastest but lowest quality',
        'quality': 'Bilinear interpolation - balanced speed and quality',
        'high_quality': 'Anti-aliased scaling - best visual fidelity',
    }

    def __init__(self, art_data: str):
        self.original_art = art_data
        self.original_lines = art_data.strip().split('\n')
        self.original_height = len(self.original_lines)
        self.original_width = max(len(line) for line in self.original_lines) if self.original_lines else 0
        self.header = self.original_lines[0] if self.original_lines else ""
        self.art_lines = self.original_lines[1:] if len(self.original_lines) > 1 else []

    def get_dimensions(self) -> Dict[str, int]:
        """Get original dimensions of the ASCII art."""
        return {
            "width": self.original_width,
            "height": self.original_height,
            "header_length": len(self.header) if self.header else 0,
            "art_height": len(self.art_lines)
        }

    def scale(self, target_width: Optional[int] = None, target_height: Optional[int] = None,
              scale_factor: Optional[float] = None, mode: str = 'quality') -> str:
        """
        Scale the ASCII art to target dimensions or by a scale factor.

        Args:
            target_width: Target width in characters (None to calculate from target_height)
            target_height: Target height in characters (None to calculate from target_width)
            scale_factor: Alternative to dimensions - scale by this factor (e.g., 0.5 for half)
            mode: Scaling mode ('fast', 'quality', 'high_quality')

        Returns:
            Scaled ASCII art string
        """
        if scale_factor is not None:
            new_width = int(self.original_width * scale_factor)
            new_height = int(self.original_height * scale_factor)
        elif target_width is not None:
            new_width = target_width
            new_height = target_height if target_height else int(target_width * (self.original_height / self.original_width))
        elif target_height is not None:
            new_height = target_height
            new_width = int(target_height * (self.original_width / self.original_height))
        else:
            return self.original_art

        new_width = max(10, min(200, new_width))
        new_height = max(5, min(150, new_height))

        if mode == 'fast':
            return self._scale_nearest(new_width, new_height)
        elif mode == 'high_quality':
            return self._scale_anti_aliased(new_width, new_height)
        else:
            return self._scale_bilinear(new_width, new_height)

    def _scale_nearest(self, new_width: int, new_height: int) -> str:
        """Fast nearest-neighbor scaling."""
        if not self.art_lines:
            return self.original_art

        result_lines = []
        height_ratio = len(self.art_lines) / new_height
        width_ratio = self.original_width / new_width

        for y in range(new_height):
            src_y = min(int(y * height_ratio), len(self.art_lines) - 1)
            src_line = self.art_lines[src_y].ljust(self.original_width)

            new_line = ''
            for x in range(new_width):
                src_x = min(int(x * width_ratio), self.original_width - 1)
                new_line += src_line[src_x] if src_x < len(src_line) else ' '

            result_lines.append(new_line)

        return '\n'.join(result_lines)

    def _scale_bilinear(self, new_width: int, new_height: int) -> str:
        """Bilinear interpolation for smoother scaling."""
        if not self.art_lines:
            return self.original_art

        height_ratio = (len(self.art_lines) - 1) / max(1, new_height - 1)
        width_ratio = (self.original_width - 1) / max(1, new_width - 1)

        result_lines = []

        for y in range(new_height):
            src_y = y * height_ratio
            y0 = min(int(src_y), len(self.art_lines) - 1)
            y1 = min(y0 + 1, len(self.art_lines) - 1)
            y_frac = src_y - y0

            line0 = self.art_lines[y0].ljust(self.original_width)
            line1 = self.art_lines[y1].ljust(self.original_width)

            new_line = ''
            for x in range(new_width):
                src_x = x * width_ratio
                x0 = min(int(src_x), self.original_width - 1)
                x1 = min(x0 + 1, self.original_width - 1)
                x_frac = src_x - x0

                c00 = line0[x0] if x0 < len(line0) else ' '
                c10 = line0[x1] if x1 < len(line0) else ' '
                c01 = line1[x0] if x0 < len(line1) else ' '
                c11 = line1[x1] if x1 < len(line1) else ' '

                top = self._interpolate_chars(c00, c10, x_frac)
                bottom = self._interpolate_chars(c01, c11, x_frac)
                final_char = self._interpolate_chars(top, bottom, y_frac)

                new_line += final_char

            result_lines.append(new_line)

        return '\n'.join(result_lines)

    def _scale_anti_aliased(self, new_width: int, new_height: int) -> str:
        """Anti-aliased scaling using character density analysis."""
        if not self.art_lines:
            return self.original_art

        density_map = self._build_density_map()

        height_ratio = len(self.art_lines) / new_height
        width_ratio = self.original_width / new_width

        result_lines = []

        for y in range(new_height):
            src_y = y * height_ratio
            y0 = max(0, int(src_y) - 1)
            y1 = min(int(src_y), len(self.art_lines) - 1)
            y2 = min(int(src_y) + 1, len(self.art_lines) - 1)
            y_frac = src_y - int(src_y)

            line0 = self.art_lines[y0].ljust(self.original_width) if y0 < len(self.art_lines) else ' ' * self.original_width
            line1 = self.art_lines[y1].ljust(self.original_width) if y1 < len(self.art_lines) else ' ' * self.original_width
            line2 = self.art_lines[y2].ljust(self.original_width) if y2 < len(self.art_lines) else ' ' * self.original_width

            new_line = ''
            for x in range(new_width):
                src_x = x * width_ratio
                x0 = max(0, int(src_x) - 1)
                x1 = min(int(src_x), self.original_width - 1)
                x2 = min(int(src_x) + 1, self.original_width - 1)
                x_frac = src_x - int(src_x)

                samples = [
                    line1[x1] if x1 < len(line1) else ' ',
                    line1[x2] if x2 < len(line1) else ' ',
                    line0[x1] if x1 < len(line0) else ' ',
                    line2[x1] if x1 < len(line2) else ' ',
                ]

                weights = [
                    (1 - x_frac) * (1 - y_frac),
                    x_frac * (1 - y_frac),
                    (1 - x_frac) * y_frac,
                    x_frac * y_frac,
                ]

                final_char = self._weighted_sample(samples, weights)
                new_line += final_char

            result_lines.append(new_line)

        return '\n'.join(result_lines)

    def _build_density_map(self) -> Dict[tuple, float]:
        """Build a density map for anti-aliased scaling."""
        density = {}
        char_weights = {
            ' ': 0.0, '⠀': 0.0, '⠄': 0.25, '⠂': 0.33, '⠁': 0.5,
            '⠃': 0.5, '⠇': 0.6, '⠏': 0.7, '⠟': 0.8, '⠿': 0.9, '⣿': 1.0,
        }

        for y, line in enumerate(self.art_lines):
            for x, char in enumerate(line):
                density[(y, x)] = char_weights.get(char, 0.5)

        return density

    def _interpolate_chars(self, c1: str, c2: str, frac: float) -> str:
        """Interpolate between two characters based on density."""
        d1 = self._char_density(c1)
        d2 = self._char_density(c2)
        result = d1 + (d2 - d1) * frac

        return self._density_to_char(result)

    def _char_density(self, char: str) -> float:
        """Get density value for a character."""
        if char in ' ⠀':
            return 0.0
        elif char in '⠄⠂⠁⠃⠈⠘⠰⠠':
            return 0.3
        elif char in '⠆⠄⠂⠇⠐⠘⠰⠸':
            return 0.5
        elif char in '⠇⠏⠛�셃':
            return 0.7
        elif char in '⠟⠿⣿░':
            return 0.85
        elif char in '▓█▒':
            return 1.0
        return 0.5

    def _density_to_char(self, density: float) -> str:
        """Convert density value to appropriate character."""
        if density < 0.1:
            return ' '
        elif density < 0.3:
            return '⠄'
        elif density < 0.5:
            return '⠂'
        elif density < 0.6:
            return '⠁'
        elif density < 0.7:
            return '⠇'
        elif density < 0.8:
            return '⠏'
        elif density < 0.9:
            return '⠟'
        elif density < 0.95:
            return '⠿'
        else:
            return '⣿'

    def _weighted_sample(self, samples: List[str], weights: List[float]) -> str:
        """Perform weighted sampling of characters."""
        total_weight = sum(weights)
        if total_weight == 0:
            return ' '

        densities = [self._char_density(s) for s in samples]
        weighted_sum = sum(d * w for d, w in zip(densities, weights)) / total_weight

        return self._density_to_char(weighted_sum)

    def generate_variants(self) -> Dict[str, str]:
        """Generate pre-defined size variants."""
        variants = {}

        variants['tiny'] = self.scale(scale_factor=0.25, mode='fast')
        variants['small'] = self.scale(scale_factor=0.5, mode='fast')
        variants['medium'] = self.scale(scale_factor=1.0, mode='quality')
        variants['large'] = self.scale(scale_factor=1.5, mode='quality')
        variants['extra_large'] = self.scale(scale_factor=2.0, mode='high_quality')

        return variants


_vault_boy_scaler: Optional[VaultBoyScaler] = None


def get_vault_boy_scaler() -> VaultBoyScaler:
    """Get or create the Vault Boy scaler singleton."""
    global _vault_boy_scaler
    if _vault_boy_scaler is None:
        vault_boy_path = os.path.join(os.path.dirname(__file__), 'vault_boy_ascii.txt')

        if os.path.exists(vault_boy_path):
            with open(vault_boy_path, 'r', encoding='utf-8') as f:
                all_lines = f.read().split('\n')
            if len(all_lines) > 1:
                header = all_lines[0]
                art_lines = all_lines[1:]
                i = 0
                while i < len(art_lines) and not (
                    art_lines[i].strip() == '' or 
                    i > 60
                ):
                    i += 1
                art_data = header + '\n' + '\n'.join(art_lines[:i])
            else:
                art_data = all_lines[0]
        else:
            art_data = VAULT_BOY_ART

        _vault_boy_scaler = VaultBoyScaler(art_data)

    return _vault_boy_scaler


@mcp.tool()
def generate_vault_boy(
    size: Literal['tiny', 'small', 'medium', 'large', 'extra_large', 'custom'] = 'medium',
    custom_width: Optional[int] = None,
    custom_height: Optional[int] = None,
    scale_factor: Optional[float] = None,
    scaling_mode: Literal['fast', 'quality', 'high_quality'] = 'quality'
) -> str:
    """
    Generate Vault Boy ASCII art at various sizes.

    Args:
        size: Pre-defined size variant (tiny=25%, small=50%, medium=100%,
              large=150%, extra_large=200%, custom=use custom dimensions)
        custom_width: Target width for custom size (required if size='custom')
        custom_height: Target height for custom size (optional, auto-calculated)
        scale_factor: Override scaling with a specific factor (e.g., 0.75)
        scaling_mode: Scaling algorithm quality ('fast', 'quality', 'high_quality')

    Returns:
        Vault Boy ASCII art at requested size

    Example:
        generate_vault_boy(size='small')
        generate_vault_boy(size='custom', custom_width=60)
        generate_vault_boy(scale_factor=0.5, scaling_mode='fast')
    """
    scaler = get_vault_boy_scaler()

    if size == 'custom':
        if custom_width is None and scale_factor is None:
            return "Error: custom_width or scale_factor required for custom size"
        return scaler.scale(
            target_width=custom_width,
            target_height=custom_height,
            scale_factor=scale_factor,
            mode=scaling_mode
        )

    if scale_factor is not None:
        return scaler.scale(scale_factor=scale_factor, mode=scaling_mode)

    variants = scaler.generate_variants()
    return variants.get(size, variants['medium'])


@mcp.tool()
def get_vault_boy_info() -> Dict[str, Any]:
    """
    Get information about the Vault Boy ASCII art and available scaling options.

    Returns:
        Dictionary with dimensions, scaling modes, and size options

    Example:
        get_vault_boy_info()
    """
    scaler = get_vault_boy_scaler()
    dimensions = scaler.get_dimensions()

    return {
        "character": "Vault Boy",
        "original_dimensions": dimensions,
        "scaling_modes": VaultBoyScaler.SCALING_MODES,
        "size_variants": {
            "tiny": {"scale": 0.25, "approx_width": int(dimensions['width'] * 0.25)},
            "small": {"scale": 0.5, "approx_width": int(dimensions['width'] * 0.5)},
            "medium": {"scale": 1.0, "approx_width": dimensions['width']},
            "large": {"scale": 1.5, "approx_width": int(dimensions['width'] * 1.5)},
            "extra_large": {"scale": 2.0, "approx_width": int(dimensions['width'] * 2.0)},
        },
        "usage": "Use generate_vault_boy(size='variant') to render at specific size"
    }


@mcp.tool()
def scale_vault_boy(
    target_width: Optional[int] = None,
    target_height: Optional[int] = None,
    scale_factor: Optional[float] = None,
    scaling_mode: Literal['fast', 'quality', 'high_quality'] = 'quality'
) -> str:
    """
    Scale Vault Boy ASCII art to specific dimensions.

    Args:
        target_width: Desired output width in characters (None to use scale_factor)
        target_height: Desired output height (auto-calculated if None)
        scale_factor: Alternative - scale by this factor
        scaling_mode: Algorithm quality ('fast', 'quality', 'high_quality')

    Returns:
        Scaled Vault Boy ASCII art

    Example:
        scale_vault_boy(target_width=80)
        scale_vault_boy(scale_factor=0.75)
        scale_vault_boy(target_height=30, scaling_mode='high_quality')
    """
    scaler = get_vault_boy_scaler()

    return scaler.scale(
        target_width=target_width,
        target_height=target_height,
        scale_factor=scale_factor,
        mode=scaling_mode
    )


@mcp.tool()
def list_character_art() -> Dict[str, Any]:
    """
    List all available character art templates.

    Returns:
        Dictionary with available character art options

    Example:
        list_character_art()
    """
    return {
        "characters": [
            {
                "name": "vault_boy",
                "description": "Vault Boy from Fallout series",
                "dimensions": get_vault_boy_scaler().get_dimensions(),
                "sizes": ["tiny", "small", "medium", "large", "extra_large"],
                "usage": "generate_vault_boy(size='medium')"
            }
        ],
        "total_count": 1,
        "example_usage": "generate_vault_boy(size='small')"
    }


# ============================================================================
# Run Server
# ============================================================================

if __name__ == "__main__":
    mcp.run()
