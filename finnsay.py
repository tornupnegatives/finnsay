#!/usr/bin/env python3
# Author: Joseph Bellahcen <joeclb@icloud.com>

"""Finnsay (n): A silly little cowsay clone featuring Finn the Human"""

import sys
import textwrap


finn = r"""
        \    ***                 ***
         \  *   *  ***********  *   *
          \ *   ***          ** *   *
           \*      .---------.      *
            *  _.-'           `--.  *
            * /                   \ *
            *;     *         *     :*
            *:                     ;*
            * \     *********     / *
            *  \                 /  *
            *   `--.         _.-'   *
            *       `-------'       *
             ***********************
"""


def create_textbox(body: str, n_cols: int) -> str:
    """
    Formats body of text into a simple ASCII textbox

    Args:
        body (str): Text to place in textbox
        n_cols (int): Maximum width (in characters) of textbox

    Returns:
        str: Text encased in box, with lines of maximum width n_cols
    """
    margin = 4
    new_text = "\n"

    # Use the TextWrapper to slice the body into a list of lines, each with
    # a maximum width which is slightly less than the given number of columns,
    # to leave room for the margin and the textbox border
    text_wrapper = textwrap.TextWrapper(n_cols - margin)
    lines = text_wrapper.wrap(body)

    # If the longest line is shorter than the number of columns, use that
    # line's length as the new maximum column width (including the margin)
    max_line_length = n_cols if (len(lines) > 1) else (len(lines[0]) + margin)

    # Re-wrap the lines to fit the new minimum size
    if max_line_length != n_cols:
        text_wrapper = textwrap.TextWrapper(max_line_length - margin)
        lines = text_wrapper.wrap(body)

    for line in lines:
        # When determining the number of whitespace characters necessary to pad
        # the line, consider one less character than the margin, since the
        # added whitespace will essentially comprise the margin
        n_pad = max_line_length - len(line) - margin - 1
        new_text += f"| {line}{' ' * n_pad}|\n"

    # Draw the textbox border on the top and bottom of the body
    text_box = (
        f"/{'-' * (max_line_length - 2)}\\"
        f"{new_text}"
        f"\\{'-' * (max_line_length - 2)}/"
    )

    return text_box


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        # Interpret all command-line arguments as a single string to display
        text = " ".join(sys.argv[1:])

    elif not sys.stdin.isatty():
        # In the absence of command-line arguments, try to read from a pipe
        text = " ".join(sys.stdin.readlines())

    else:
        # No data received :(
        exit()

    textbox = create_textbox(text, 45)
    print(textbox, finn)
