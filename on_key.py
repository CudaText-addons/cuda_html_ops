from cudatext import *

HTML_INDENT = 2 #two spaces


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
    #print('key', key)

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

    space = 0
    for i in range(indent):
        if not s[i] in ' \t': break
        space += 1

    text_len = s[x:].find('<')
    if text_len<0: return

    is_closing = s[indent+1]=='/'
    if is_closing: return

    #handle tabs at linestart
    text = '\n' + s[:space] + ' '*(indent-space)
    ed.insert(x+text_len, y, text)

    text += ' '*HTML_INDENT
    ed.insert(x, y, text)
    ed.set_caret(indent+HTML_INDENT, y+1)

    msg_status('Smart HTML indent')
    return False #block Enter
