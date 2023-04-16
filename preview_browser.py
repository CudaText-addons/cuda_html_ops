import os
import webbrowser
from cudatext import *

from cudax_lib import get_translation
_ = get_translation(__file__)  # I18N


def do_preview_browser(app, new_window):

    fn_preview = '_cudatext_preview.html'
    fn = ed.get_filename()
    if not fn:
        msg_box(_('Cannot preview untitled tab'), MB_OK)
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
        msg_status(_('Cannot open file: ')+fn)
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
