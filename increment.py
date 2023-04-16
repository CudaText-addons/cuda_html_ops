from cudatext import *
from decimal import Decimal as D

from cudax_lib import get_translation
_ = get_translation(__file__)  # I18N


def get_result(text, is_inc):
    try:
        num = int(text)
        inc = 1 if is_inc else -1
        if num==0 and not is_inc:
            return
        return str(num + inc)
    except:
        try:
            if text.startswith('.'):
                text = '0' + text
            num = D(text)
            digits = len(text) - text.find('.') - 1
            inc = D('0.' + '0'*(digits-1) + '1')
            if not is_inc:
                inc = -inc
            num += inc
            if float(num)<0:
                return
            return str(num)
        except:
            return


def is_digit(ch):
    return ch in '1234567890.'

def get_text(x0, y0):
    line = ed.get_text_line(y0)
    if not line: return

    #support caret after "100px"
    while x0>0 and line[x0-1].isalpha(): x0-=1
    #support caret after "%"
    if x0>0 and line[x0-1] == '%': x0-=1

    x2 = x0
    while x2<len(line) and is_digit(line[x2]): x2+=1
    x1 = x0
    while x1>0 and is_digit(line[x1-1]): x1-=1
    text = line[x1:x2]
    if not text: return
    return (text, x1, y0)


def do_increment(is_inc):
    carets = ed.get_carets()
    if not carets:
        msg_status(_('No carets'))
        return
    run_carets(is_inc, carets)


def run_carets(is_inc, carets):
    is_simple = len(carets)==1
    carets = list(reversed(carets))

    ed.lock()
    for caret in carets:
        res = run_simple(is_inc, caret[0], caret[1], is_simple)
        if is_simple:
            msg_status(res)
    ed.unlock()

    if not is_simple:
        msg_status(_('Changed %d values') % len(carets))


def run_simple(is_inc, x0, y0, is_simple):
    info = get_text(x0, y0)
    if not info:
        return _('Place caret under number')
    text, x1, y1 = info
    res = get_result(text, is_inc)
    if res is None:
        return _('Incorrect number or zero: ')+text

    if is_simple:
        if len(res) < len(text):
            ed.set_caret(x1, y1)
    ed.delete(x1, y1, x1+len(text), y1)
    ed.insert(x1, y1, res)
    return _('Increased value') if is_inc else _('Decreased value')

