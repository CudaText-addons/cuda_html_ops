from cudatext import *
import html

from cudax_lib import get_translation
_ = get_translation(__file__)  # I18N

max_columns = 100
mode_ol = 1
mode_ul = 2
mode_table1 = 3
mode_table2 = 4

def esc(s):
    return html.escape(s, False)

def get_columns():
    s = dlg_input(_('Table columns:'), '3')
    if not s: return
    try:
        n = int(s)
    except:
        msg_status(_('Incorrect number: ')+s)
        return
    if not 1<=n<=max_columns:
        msg_status(_('Incorrect number: ')+s)
        return
    return n

def do_list_lines(l, is_ul, indent):
    tag = 'ul' if is_ul else 'ol'
    return ['<'+tag+'>'] + [indent+'<li>'+esc(s)+'</li>' for s in l] + ['</'+tag+'>']

def do_table_lines(l, n_cols, indent, by_lines):
    n_lines = len(l) // n_cols
    if len(l) % n_cols:
        n_lines += 1

    res = []
    for y in range(n_lines):
        res += ['<tr>']
        for x in range(n_cols):
            if by_lines:
                index = x + y*n_cols
            else:
                index = y + x*n_lines
            if index<len(l):
                cell = l[index]
            else:
                cell = ''
            res += [indent+'<td>'+esc(cell)+'</td>']
        res += ['</tr>']
    return ['<table border="1">'] + res + ['</table>']

def do_list(mode):
    text = ed.get_text_sel()
    if not text:
        msg_status(_('Text not selected'))
        return

    eol = '\n'
    indent = '  ' #'\t' if not ed.get_prop(PROP_TAB_SPACES) else ' '*ed.get_prop(PROP_TAB_SIZE)

    n1, n2 = ed.get_sel_lines()
    l = [ed.get_text_line(i) for i in range(n1, n2+1)]
    if not l: return

    if mode in [mode_table1, mode_table2]:
        n_cols = get_columns()
        if not n_cols: return
        l_out = do_table_lines(l, n_cols, indent, mode==mode_table1)
    else:
        l_out = do_list_lines(l, mode==mode_ul, indent)

    text = eol.join(l_out) + eol

    ed.set_caret(0, n1)
    ed.replace_lines(n1, n2, l_out)
