from .html_ops import *
from .conv_units import *
from .img_insert import *
from .lines_to_list import *
from .validator import *

class Command:
    def do_b(self):
        do_tag_wrap_sel('b')

    def do_i(self):
        do_tag_wrap_sel('i')

    def do_u(self):
        do_tag_wrap_sel('u')

    def tag_new_or_wrap(self):
        do_tag_sublime_action()

    def convert_px_rem(self):
        do_convert_px_rem()


    def preview_tab(self):
        do_preview_browser('', False)
    def preview_window(self):
        do_preview_browser('', True)

    def preview_tab_safari(self):
        do_preview_browser('safari', False)
    def preview_window_safari(self):
        do_preview_browser('safari', True)

    def preview_tab_firefox(self):
        do_preview_browser('firefox', False)
    def preview_window_firefox(self):
        do_preview_browser('firefox', True)

    def preview_tab_chrome(self):
        do_preview_browser('chrome', False)
    def preview_window_chrome(self):
        do_preview_browser('chrome', True)

    def preview_tab_opera(self):
        do_preview_browser('opera', False)
    def preview_window_opera(self):
        do_preview_browser('opera', True)

    def preview_tab_windows(self):
        do_preview_browser('windows-default', False)
    def preview_window_windows(self):
        do_preview_browser('windows-default', True)


    def insert_image_info(self):
        do_insert_image_info()


    def to_list_o(self):
        do_list(mode_ol)
    def to_list_u(self):
        do_list(mode_ul)

    def to_table_lines(self):
        do_list(mode_table1)
    def to_table_cols(self):
        do_list(mode_table2)

    def validate_html5(self):
        do_validate(ed, 'html5', URL_W3C)
    def validate_html4_strict(self):
        do_validate(ed, 'html4', URL_W3C)
    def validate_html4_tran(self):
        do_validate(ed, 'html4tr', URL_W3C)
