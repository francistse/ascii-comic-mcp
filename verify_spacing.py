#!/usr/bin/env python3
"""
Spacing Verification Script for ASCII Art

This script verifies that ASCII art output has proper spacing and no indentation issues.
It checks for common problems like:
- Inconsistent line lengths
- Misaligned borders
- Improper character spacing
- Broken box drawing characters
"""

import sys
import re
from typing import List, Tuple, Dict, Any


def check_line_lengths(lines: List[str]) -> Dict[str, Any]:
    """Check if all lines have consistent lengths within expected tolerances."""
    if not lines:
        return {"status": "error", "message": "No lines to check"}

    lengths = [len(line) for line in lines]
    unique_lengths = set(lengths)

    issues = []
    most_common_length = max(set(lengths), key=lengths.count)

    for i, line_len in enumerate(lengths):
        if line_len < most_common_length * 0.7:
            issues.append(f"Line {i+1}: length {line_len} is too short (< 70% of max)")

    return {
        "status": "pass" if not issues else "fail",
        "all_lengths": lengths,
        "unique_lengths": list(unique_lengths),
        "most_common_length": most_common_length,
        "issues": issues
    }


def check_box_alignment(lines: List[str]) -> Dict[str, Any]:
    """Check if box drawing characters are properly aligned."""
    box_chars = set('╔╗╚╝═║│┌┐└┘─┃')
    border_positions = []

    for i, line in enumerate(lines):
        positions = [j for j, c in enumerate(line) if c in box_chars]
        if positions:
            border_positions.append((i, positions))

    issues = []
    if border_positions:
        first_positions = [positions[0] for _, positions in border_positions]
        if len(set(first_positions)) > 1:
            issues.append(f"Box borders not aligned - found start positions: {set(first_positions)}")

        last_positions = [positions[-1] for _, positions in border_positions]
        if len(set(last_positions)) > 1:
            issues.append(f"Box borders not consistent - found end positions: {set(last_positions)}")

    return {
        "status": "pass" if not issues else "fail",
        "issues": issues
    }


def check_character_spacing(text: str) -> Dict[str, Any]:
    """Check for proper character spacing (no missing spaces between elements)."""
    lines = text.split('\n')
    issues = []

    box_chars = set('╔╗╚╝═║│┌┐└┘─┃')

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c in box_chars:
                if j > 0 and line[j-1] not in (' ', '═', '─') and line[j-1] not in box_chars:
                    if j < len(line) - 1 and line[j+1] not in (' ', '═', '─') and line[j+1] not in box_chars:
                        issues.append(f"Line {i+1}: Box char '{c}' missing space separation")

    return {
        "status": "pass" if not issues else "warn",
        "issues": issues
    }


def check_vertical_spacing(text: str) -> Dict[str, Any]:
    """Check for consistent vertical spacing."""
    lines = text.split('\n')
    issues = []

    consecutive_empty = 0
    max_consecutive_empty = 3

    for i, line in enumerate(lines):
        if not line.strip():
            consecutive_empty += 1
            if consecutive_empty > max_consecutive_empty:
                issues.append(f"Line {i+1}: Too many consecutive empty lines ({consecutive_empty})")
        else:
            consecutive_empty = 0

    return {
        "status": "pass" if not issues else "warn",
        "issues": issues
    }


def check_braille_spacing(text: str) -> Dict[str, Any]:
    """Check for proper Braille character spacing."""
    lines = text.split('\n')
    issues = []

    braille_chars = set('⠀⠁⠃⠇⠏⠟⠿⣿')

    for i, line in enumerate(lines):
        if any(c in braille_chars for c in line):
            has_space = ' ' in line
            has_other_content = any(c not in braille_chars and c != ' ' for c in line)

            if has_other_content and not has_space:
                issues.append(f"Line {i+1}: Braille characters without space separator")

    return {
        "status": "pass" if not issues else "warn",
        "issues": issues
    }


def verify_ascii_art(text: str, name: str = "ASCII Art") -> bool:
    """
    Main verification function for ASCII art.

    Returns True if all checks pass, False otherwise.
    """
    print(f"\n{'='*60}")
    print(f"  SPACING VERIFICATION: {name}")
    print(f"{'='*60}")

    if not text or not text.strip():
        print(f"\n⚠️  WARNING: Empty text provided")
        return False

    lines = text.split('\n')
    print(f"\n📊 Statistics:")
    print(f"   Total lines: {len(lines)}")
    print(f"   Max line length: {max(len(l) for l in lines)}")
    print(f"   Min line length: {min(len(l) for l in lines)}")

    checks = [
        ("Line Length Consistency", check_line_lengths(lines)),
        ("Box Alignment", check_box_alignment(lines)),
        ("Character Spacing", check_character_spacing(text)),
        ("Vertical Spacing", check_vertical_spacing(text)),
        ("Braille Spacing", check_braille_spacing(text)),
    ]

    all_passed = True
    for check_name, result in checks:
        status_icon = "✅" if result["status"] == "pass" else "❌" if result["status"] == "fail" else "⚠️"
        print(f"\n{status_icon} {check_name}: {result['status'].upper()}")

        if result.get("issues"):
            for issue in result["issues"]:
                print(f"   - {issue}")
            if result["status"] == "fail":
                all_passed = False

    print(f"\n{'='*60}")
    if all_passed:
        print(f"✅ VERIFICATION PASSED - All checks successful!")
    else:
        print(f"❌ VERIFICATION FAILED - Issues found, please review above")
    print(f"{'='*60}\n")

    return all_passed


def verify_speech_bubble(text: str) -> bool:
    """Verify speech bubble specific formatting."""
    print(f"\n{'='*60}")
    print(f"  SPEECH BUBBLE VERIFICATION")
    print(f"{'='*60}")

    lines = text.strip().split('\n')
    if not lines:
        print(f"\n⚠️  WARNING: Empty text provided")
        return False

    issues = []

    if not lines[0].startswith('╔') or '╗' not in lines[0]:
        issues.append("Top border should start with ╔ and contain ╗")

    bottom_line = lines[-1]
    if not (bottom_line.startswith('╚') or bottom_line.startswith('║') or '╝' in bottom_line):
        issues.append("Bottom area should contain ╚ or ║ and ╝")

    middle_lines = lines[1:-1] if len(lines) > 2 else []
    for i, line in enumerate(middle_lines):
        if line.strip() and not (line.startswith('║') or line.startswith(' ')):
            issues.append(f"Content line {i+2} should start with ║ or space")

    main_lines = [l for l in lines if '║' in l or '═' in l]
    if main_lines:
        widths = [len(l) for l in main_lines]
        max_width = max(widths)
        min_width = min(widths)

        if max_width - min_width > 10:
            issues.append(f"Inconsistent box widths: {min_width} to {max_width}")

    print(f"\n📊 Statistics:")
    print(f"   Total lines: {len(lines)}")
    print(f"   Main box width: {len(lines[0]) if lines else 0}")

    if issues:
        print(f"\n❌ ISSUES FOUND:")
        for issue in issues:
            print(f"   - {issue}")
        print(f"\n{'='*60}")
        print(f"❌ VERIFICATION FAILED")
        print(f"{'='*60}\n")
        return False
    else:
        print(f"\n✅ VERIFICATION PASSED - Speech bubble properly formatted!")
        print(f"{'='*60}\n")
        return True


def verify_composed_art(art: str) -> bool:
    """Verify composed ASCII art with multiple elements."""
    print(f"\n{'='*60}")
    print(f"  COMPOSED ART VERIFICATION")
    print(f"{'='*60}")

    if not verify_ascii_art(art, "Composed Art"):
        return False

    lines = art.split('\n')
    max_len = max(len(l) for l in lines)
    min_len = min(len(l) for l in lines)

    if max_len - min_len > 5:
        print(f"\n⚠️  WARNING: Significant width variation ({min_len} to {max_len})")
        print(f"   This may indicate alignment issues in composed elements")

    print(f"\n✅ COMPOSED ART VERIFIED")
    return True


if __name__ == "__main__":
    test_box = """╔════════════════════════════╗
║                            ║
║   Hello, World!            ║
║   This is a test message.  ║
║                            ║
╚════════════════════════════╝"""

    test_bubble = """╔══════════════════════════════╗
║  Hello World How Are You   ║
║  This is a test           ║
╚══════════════════════════════╝"""

    print("Running verification tests...")

    result1 = verify_ascii_art(test_box, "Simple Box")
    result2 = verify_speech_bubble(test_bubble)

    if result1 and result2:
        print("\n🎉 All verification tests passed!")
        sys.exit(0)
    else:
        print("\n⚠️  Some verification tests failed.")
        sys.exit(1)