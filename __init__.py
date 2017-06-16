import os
import webbrowser
from cudatext import *

temp_fn = '_cudatext_preview.html'


def do_tag_new_or_wrap():
    """
    Does what SublimeText does on hotkey Alt+Shift+W:
    on selection: wrap selection with <p></p> and place 2 selections to rename tag
    w/o selection: add <p></p> with 2 selections and 2 markers:
      1st TAB press goes into tag,
      2nd TAB press goes after tag
    """

    carets = ed.get_carets()
    if len(carets)!=1: return msg_status('Need single caret')

    x1, y1, x2, y2 = carets[0]

    sel = ed.get_text_sel()
    if sel:
        if (y1, x1)>(y2, x2):
            x1, y1, x2, y2 = x2, y2, x1, y1
        text = '<p>%s</p>' % sel
        ed.replace(x1, y1, x2, y2, text)
        ed.set_caret(x1+2, y1, x1+1, y1, CARET_SET_ONE)
        ed.set_caret(x1+len(sel)+6, y1, x1+len(sel)+5, y1, CARET_ADD)
        msg_status('Wrapped selection into tag')
    else:
        ed.insert(x1, y1, '<p></p>')
        ed.set_caret(x1+2, y1, x1+1, y1, CARET_SET_ONE)
        ed.set_caret(x1+6, y1, x1+5, y1, CARET_ADD)
        ed.markers(MARKERS_DELETE_ALL)
        ed.markers(MARKERS_ADD, x=x1+7, y=y1, tag=2, len_x=0, len_y=0)
        ed.markers(MARKERS_ADD, x=x1+3, y=y1, tag=1, len_x=0, len_y=0)
        ed.set_prop(PROP_TAB_COLLECT_MARKERS, True)
        msg_status('Added new tag')



def do_tag(tag):
    """
    For selection only: wraps selection into tag: <tag>selected</tag>
    """
    s = ed.get_text_sel()
    if not s: return msg_status('Text not selected')
    carets = ed.get_carets()
    if len(carets)!=1: return msg_status('Need single caret')
    x1, y1, x2, y2 = carets[0]

    if (y1, x1)>(y2, x2):
        x1, y1, x2, y2 = x2, y2, x1, y1

    text = '<%s>%s</%s>' % (tag, s, tag)
    ed.replace(x1, y1, x2, y2, text)
    ed.set_caret(x1, y1, x1+len(text), y1)
    msg_status('Added tag <%s>'%tag)


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


def do_preview(new_window):

    fn = ed.get_filename()
    if not fn:
        msg_box('Cannot preview untitled tab', MB_OK)
        return

    #if selection- write it to file
    text = ed.get_text_sel()
    if text:
        fn = os.path.join(os.path.dirname(fn), temp_fn)
        if os.path.isfile(fn):
            os.remove(fn)
        with open(fn, 'w') as f:
            f.write(text)

    if not os.path.isfile(fn):
        msg_status('Cannot open file: '+fn)
        return

    if new_window:
        webbrowser.open(fn)
    else:
        webbrowser.open_new_tab(fn)
    msg_status('Opened preview in browser')


class Command:
    def do_b(self):
        do_tag('b')

    def do_i(self):
        do_tag('i')

    def do_u(self):
        do_tag('u')

    def tag_new_or_wrap(self):
        do_tag_new_or_wrap()

    def convert_px_rem(self):
        do_convert_px_rem()

    def preview_new_tab(self):
        do_preview(False)
    def preview_new_window(self):
        do_preview(True)
