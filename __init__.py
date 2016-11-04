from cudatext import *

def do_tag(tag):
    s = ed.get_text_sel()
    if not s: return msg_status('Text not selected')
    carets = ed.get_carets()
    if len(carets)!=1: return msg_status('Need single caret')
    x1, y1, x2, y2 = carets[0]

    if (y1, x1)>(y2, x2):
        x1, y1, x2, y2 = x2, y2, x1, y1

    text = '<%s>%s</%s>' % (tag, s, tag)
    ed.delete(x1, y1, x2, y2)
    ed.insert(x1, y1, text)
    ed.set_caret(x1, y1, x1+len(text), y1)
    msg_status('Added tag <%s>'%tag)


class Command:
    def do_b(self):
        do_tag('b')
    def do_i(self):
        do_tag('i')
    def do_u(self):
        do_tag('u')
