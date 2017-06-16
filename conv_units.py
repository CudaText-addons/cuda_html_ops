from cudatext import *

def _convert_px_rem(s):
    s = s.lower()
    if "rem" in s:
        s = s.replace("rem", "")
        n = round(float(s) * 16, 4)
        return str(n) + 'px'

    if "px" in s:
        s = s.replace("px", "")
        n = round(float(s) / 16, 4)
        return str(n) + 'rem'


def do_convert_px_rem():
    """
    Takes selection, changes it if it's with "px" or "rem",
    puts new text back
    """
    s = ed.get_text_sel()
    if not s: return

    if '\n' in s or ' ' in s:
        msg_status('Cannot convert selection')
        return

    carets = ed.get_carets()
    if len(carets)>1:
        msg_status('Need single caret')
        return

    x1, y1, x2, y2 = carets[0]
    if (y1, x1)>(y2, x2):
        x1, y1, x2, y2 = x2, y2, x1, y1

    s = _convert_px_rem(s)
    if not s: return

    ed.replace(x1, y1, x2, y2, s)
    ed.set_caret(x1+len(s), y1, x1, y1)
    msg_status('Converted px<->rem')
