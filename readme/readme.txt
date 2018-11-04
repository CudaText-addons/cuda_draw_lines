plugin for CudaText.
allows to draw preudo-graphic frames in text, using Unicode "box" chars,
which were available in DOS codepage ages ago.

example of frames:
       ╒════╦═╗
       │   ╔╬═╬╦═╦═════╗
   ╒═╕ │   ╠╩╤╩╩═╩─┬─┐ ║
   └─┴─┤ ┌┬┴─┤    ┌┼─┼─╜
  ─────┴─┴┴──┴────┴┴─┘

activate/deactivate plugin using menu item: Plugins - Draw Lines.
when active, plugin allows 2 modes: single lines, double lines,
toggle this mode by F9 (no command in plugin, just a hotkey 
while plugin is active).
use Shift+arrows to draw line, single or double, in any of 4 directions:
up/down/left/right. line intersections are handled, so some chars will
be "crosses" or "angles" when you intersect other lines.

author: Alexey (CudaText)
license: MIT
