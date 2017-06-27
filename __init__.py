from .ops import *
from .preview_browser import *
from .conv_units import *
from .img_insert import *
from .lines_to_list import *
from .validator import *
from .increment import do_increment
from .on_key import *

class Command:

    def wrap_b(self):              do_tag_wrap_sel('b')
    def wrap_i(self):              do_tag_wrap_sel('i')
    def wrap_u(self):              do_tag_wrap_sel('u')
    def wrap_p(self):              do_tag_wrap_sel('p')
    def wrap_div(self):            do_tag_wrap_sel('div')
    def wrap_span(self):           do_tag_wrap_sel('span')
    def wrap_pre(self):            do_tag_wrap_sel('pre')
    def wrap_strong(self):         do_tag_wrap_sel('strong')
    def wrap_em(self):             do_tag_wrap_sel('em')
    def wrap_ul(self):             do_tag_wrap_sel('ul')
    def wrap_ol(self):             do_tag_wrap_sel('ol')
    def wrap_li(self):             do_tag_wrap_sel('li')
    def wrap_sub(self):            do_tag_wrap_sel('sub')
    def wrap_sup(self):            do_tag_wrap_sel('sup')
    def wrap_small(self):          do_tag_wrap_sel('small')
    def wrap_bdi(self):            do_tag_wrap_sel('bdi')
    def wrap_h1(self):             do_tag_wrap_sel('h1')
    def wrap_h2(self):             do_tag_wrap_sel('h2')
    def wrap_h3(self):             do_tag_wrap_sel('h3')
    def wrap_h4(self):             do_tag_wrap_sel('h4')
    def wrap_h5(self):             do_tag_wrap_sel('h5')
    def wrap_h6(self):             do_tag_wrap_sel('h6')
    def wrap_blockquote(self):     do_tag_wrap_sel('blockquote')
    def wrap_q(self):              do_tag_wrap_sel('q')
    def wrap_cite(self):           do_tag_wrap_sel('cite')

    def tag_new_or_wrap(self):     do_tag_sublime_action()
    def convert_px_rem(self):      do_convert_px_rem()
    def insert_image_info(self):   do_insert_image_info()


    def preview_tab(self):                 do_preview_browser('', False)
    def preview_window(self):              do_preview_browser('', True)

    def preview_tab_safari(self):          do_preview_browser('safari', False)
    def preview_window_safari(self):       do_preview_browser('safari', True)

    def preview_tab_firefox(self):         do_preview_browser('firefox', False)
    def preview_window_firefox(self):      do_preview_browser('firefox', True)

    def preview_tab_chrome(self):          do_preview_browser('chrome', False)
    def preview_window_chrome(self):       do_preview_browser('chrome', True)

    def preview_tab_opera(self):           do_preview_browser('opera', False)
    def preview_window_opera(self):        do_preview_browser('opera', True)

    def preview_tab_windows(self):         do_preview_browser('windows-default', False)
    def preview_window_windows(self):      do_preview_browser('windows-default', True)


    def to_list_o(self):      do_list(mode_ol)
    def to_list_u(self):      do_list(mode_ul)
    def to_table_lines(self): do_list(mode_table1)
    def to_table_cols(self):  do_list(mode_table2)

    def validate_html5(self):          do_validate(ed, 'html5', URL_W3C)
    def validate_html4_strict(self):   do_validate(ed, 'html4', URL_W3C)
    def validate_html4_tran(self):     do_validate(ed, 'html4tr', URL_W3C)

    def increment(self): do_increment(True)
    def decrement(self): do_increment(False)

    def on_key(self, ed_self, key, state):
        return handle_on_key(ed_self, key, state)
