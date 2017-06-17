from .html_ops import *
from .conv_units import *
from .img_insert import *
from .lines_to_list import *

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

    def preview_new_tab(self):
        do_preview_browser(False)

    def preview_new_window(self):
        do_preview_browser(True)

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
