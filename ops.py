import os
from cudatext import *

fn_ini = 'cuda_html_ops.ini'
HTML_INDENT = 2 #2 spaces indent on Enter


def do_tag_sublime_action():
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


def do_tag_wrap_sel(tag):
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


def handle_on_key(ed, key, state):
    """
    Handle Enter between tags, and make HTML indent:
    <tag>|</tag> must convert to
    <tag>
      |
    </tag>

    <a href="#GlossTop">|Top</a> must convert to
    <a href="#GlossTop">
      |Top
    </a>
    """
    #Enter is 13
    if (state!='') or (key!=13): return

    carets = ed.get_carets()
    if len(carets)>1: return #dont work on mul-carets

    x, y, x1, y1 = carets[0]
    if x1>=0 or y1>=0: return #dont work on selection

    s = ed.get_text_line(y)
    if not 3<=x<len(s)-1: return
    if (s[x-1]!='>'): return

    indent = s[:x].rfind('<')
    if indent<0: return

    text_len = s[x:].find('<')
    if text_len<0: return

    is_closing = s[indent+1]=='/'
    if is_closing: return

    text = '\n' + ' '*indent
    ed.insert(x+text_len, y, text)

    text = '\n' + ' '*(indent+HTML_INDENT)
    ed.insert(x, y, text)
    ed.set_caret(indent+HTML_INDENT, y+1)

    msg_status('Smart HTML indent')
    return False #block Enter
