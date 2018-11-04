import os
from cudatext import *
import cudatext_keys as kk
import cudatext_cmd as cmds

MSG_OFF = 'Turned off' 
MSG_ONE = 'Shift+arrows: ├───┤' 
MSG_TWO = 'Shift+arrows: ╠═══╣'

CHAR_PROP = {
  '─': (1, 0, 1, 0),
  '│': (0, 1, 0, 1),
  '┌': (0, 0, 1, 1),
  '┐': (1, 0, 0, 1),
  '└': (0, 1, 1, 0),
  '┘': (1, 1, 0, 0),
  '├': (0, 1, 1, 1),
  '┤': (1, 1, 0, 1),
  '┬': (1, 0, 1, 1),
  '┴': (1, 1, 1, 0),
  '┼': (1, 1, 1, 1),
  '═': (2, 0, 2, 0),
  '║': (0, 2, 0, 2),
  '╒': (0, 0, 2, 1),
  '╓': (0, 0, 1, 2),
  '╔': (0, 0, 2, 2),
  '╕': (2, 0, 0, 1),
  '╖': (1, 0, 0, 2),
  '╗': (2, 0, 0, 2),
  '╘': (0, 1, 2, 0),
  '╙': (0, 2, 1, 0),
  '╚': (0, 2, 2, 0),
  '╛': (2, 1, 0, 0),
  '╜': (1, 2, 0, 0),
  '╝': (2, 2, 0, 0),
  '╞': (0, 1, 2, 1),
  '╟': (0, 2, 1, 2),
  '╠': (0, 2, 2, 2),
  '╡': (2, 1, 0, 1),
  '╢': (1, 2, 0, 2),
  '╣': (2, 2, 0, 2),
  '╤': (2, 0, 2, 1),
  '╥': (1, 0, 1, 2),
  '╦': (2, 0, 2, 2),
  '╧': (2, 1, 2, 0),
  '╨': (1, 2, 1, 0),
  '╩': (2, 2, 2, 0),
  '╪': (2, 1, 2, 1),
  '╫': (1, 2, 1, 2),
  '╬': (2, 2, 2, 2),
}

class Command:
    act = False
    mode = False
    
    def toggle(self):
    
        self.act = not self.act
        ev = 'on_key' if self.act else ''

        # react only to 4 arrow key codes: 37..40, 120=VK_F9
        app_proc(PROC_SET_EVENTS, 'cuda_draw_lines;'+ev+';;37,38,39,40,120')
        self.status()


    def status(self):
    
        msg_status('[Draw Lines] '+(MSG_OFF if not self.act else MSG_TWO if self.mode else MSG_ONE))


    def repl(self, x, y, ch):

        s = ed.get_text_line(y)
        if x<len(s):
            ed.replace(x, y, x+1, y, ch)
        else:
            ed.set_text_line(y, s+' '*(x-len(s))+ch)
    

    def on_key(self, ed_self, key, state):

        if state=='' and key==kk.VK_F9:
            self.mode = not self.mode
            self.status()
            return False 

        # require Shift key
        if 's' not in state: return

        carets = ed.get_carets()
        if len(carets)>1: return
        x, y, x1, y1 = carets[0]
    
        if key==kk.VK_LEFT:
            if x==0: return
            ch = '─'
            self.repl(x, y, ch)
            ed.cmd(cmds.cCommand_KeyLeft)

        elif key==kk.VK_UP:
            if y==0: return
            ch = '│'
            self.repl(x, y, ch)
            ed.cmd(cmds.cCommand_KeyUp)

        elif key==kk.VK_RIGHT:
            ch = '─'
            self.repl(x, y, ch)
            ed.cmd(cmds.cCommand_KeyRight)

        elif key==kk.VK_DOWN:
            if y==ed.get_line_count()-1: return
            ch = '│'
            self.repl(x, y, ch)
            ed.cmd(cmds.cCommand_KeyDown)
            
        return False
        