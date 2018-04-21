import re
from cudatext import *

REGEX1 = r'\bclass\s*=\s*"(.+?)"'
REGEX2 = r"\bclass\s*=\s*'(.+?)'"

def do_html_to_css_clipboard(compact):

    text = ed.get_text_sel()
    if not text: return

    res = re.findall(REGEX1, text, 0) + re.findall(REGEX2, text, 0)
    res = sorted(list(set(res)))

    if not res:
        msg_status('No CSS classes found')
        app_proc(PROC_SET_CLIP, '')
        return

    text_in = '  ' if compact else '\n\n'
    out = ['.'+name+' {'+text_in+'}\n' for name in res]
    text = '\n'.join(out)+'\n'

    app_proc(PROC_SET_CLIP, text)
    msg_status('CSS styles ({}) copied to clipboard'.format(len(res)) )
