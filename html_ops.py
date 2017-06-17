import os
import webbrowser
from cudatext import *

fn_ini = 'cuda_html_ops.ini'
fn_preview = '_cudatext_preview.html'


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


def do_preview_browser(app, new_window):

    fn = ed.get_filename()
    if not fn:
        msg_box('Cannot preview untitled tab', MB_OK)
        return

    #if selection- write it to file
    text = ed.get_text_sel()
    if text:
        fn = os.path.join(os.path.dirname(fn), fn_preview)
        if os.path.isfile(fn):
            os.remove(fn)
        with open(fn, 'w') as f:
            f.write(text)

    if not os.path.isfile(fn):
        msg_status('Cannot open file: '+fn)
        return

    if new_window:
        if app:
            webbrowser.get(app).open_new(fn)
        else:
            webbrowser.open_new(fn)
    else:
        if app:
            webbrowser.get(app).open_new_tab(fn)
        else:
            webbrowser.open_new_tab(fn)

    s = ' ('+app+')' if app else ''
    msg_status('Opened preview in browser'+s)
