from cudatext import *
from cudatext_cmd import *
import sys
import json
from urllib.request import urlopen
from urllib.parse import urlencode

URL_W3C = 'http://validator.w3.org/check'

def do_validate(ed, format, validator_url):

    app_log(LOG_SET_PANEL, LOG_PANEL_VALIDATE)
    app_log(LOG_CLEAR, '')

    text = ed.get_text_all()
    params = {'fragment': text, 'parser': format, 'output': 'json'}
    encoded_params = urlencode(params).encode('utf-8')

    output = urlopen(validator_url, encoded_params).read()
    output = output.decode('utf-8')
    results = json.loads(output)

    if not results['messages']:
        msg_box('Document successfully checked as %s' % format, MB_OK+MB_ICONINFO)
        return

    app_log(LOG_SET_REGEX, r'Line (\d+):.+')
    app_log(LOG_SET_LINE_ID, '1')
    app_log(LOG_SET_NAME_ID, '0')
    app_log(LOG_SET_FILENAME, ed.get_filename())
    app_log(LOG_SET_ZEROBASE, '0')

    app_log(LOG_ADD, 'Errors found while checking document as %s:' % format)
    app_log(LOG_ADD, '')
    for message in results['messages']:
        app_log(LOG_ADD, 'Line %s: %s' % (message['lastLine'], message['message']))

    ed.focus()
    ed.cmd(cmd_ShowPanelValidate)

