import os
from cudatext import *

from cudax_lib import get_translation
_ = get_translation(__file__)  # I18N

fn_ini = 'cuda_html_ops.ini'


def do_tag_sublime_action():
    """
    Does what SublimeText does on hotkey Alt+Shift+W:
    on selection: wrap selection with <p></p> and place 2 selections to rename tag
    w/o selection: add <p></p> with 2 selections and 2 markers:
      1st TAB press goes into tag,
      2nd TAB press goes after tag
    """

    carets = ed.get_carets()
    if len(carets)!=1: return msg_status(_('Need single caret'))

    x1, y1, x2, y2 = carets[0]

    sel = ed.get_text_sel()
    if sel:
        if (y1, x1)>(y2, x2):
            x1, y1, x2, y2 = x2, y2, x1, y1
        text = '<p>%s</p>' % sel
        ed.replace(x1, y1, x2, y2, text)
        ed.set_caret(x1+2, y1, x1+1, y1, CARET_SET_ONE)
        ed.set_caret(x1+len(sel)+6, y1, x1+len(sel)+5, y1, CARET_ADD)
        msg_status(_('Wrapped selection into tag'))
    else:
        ed.insert(x1, y1, '<p></p>')
        ed.set_caret(x1+2, y1, x1+1, y1, CARET_SET_ONE)
        ed.set_caret(x1+6, y1, x1+5, y1, CARET_ADD)
        ed.markers(MARKERS_DELETE_ALL)
        ed.markers(MARKERS_ADD, x=x1+7, y=y1, tag=2, len_x=0, len_y=0)
        ed.markers(MARKERS_ADD, x=x1+3, y=y1, tag=1, len_x=0, len_y=0)
        ed.set_prop(PROP_TAB_COLLECT_MARKERS, True)
        msg_status(_('Added new tag'))


def do_tag_wrap_sel(tag):
    """
    For selection only: wraps selection into tag: <tag>selected</tag>
    """
    s = ed.get_text_sel()
    if not s: return msg_status(_('Text not selected'))
    carets = ed.get_carets()
    if len(carets)!=1: return msg_status(_('Need single caret'))
    x1, y1, x2, y2 = carets[0]

    if (y1, x1)>(y2, x2):
        x1, y1, x2, y2 = x2, y2, x1, y1

    text = '<%s>%s</%s>' % (tag, s, tag)
    ed.replace(x1, y1, x2, y2, text)
    ed.set_caret(x1, y1, x1+len(text), y1)
    msg_status(_('Added tag <%s>') % tag)
