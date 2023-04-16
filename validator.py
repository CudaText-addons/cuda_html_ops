from cudatext import *
from cudatext_cmd import *
import sys
import json
from urllib.request import urlopen, Request
from urllib.parse import urlencode

from cudax_lib import get_translation
_ = get_translation(__file__)  # I18N

URL_W3C = 'https://validator.w3.org/nu/?out=json'

def do_validate(ed, format, validator_url):

    p = LOG_PANEL_VALIDATE
    app_log(LOG_CLEAR, '', panel=p)

    text = ed.get_text_all()
    req = Request(
        validator_url,
        data=text.encode('utf-8'),
        method='POST',
        headers={'Content-type': 'text/html; charset=utf-8'}
    )
    output = urlopen(req).read()
    
    output = output.decode('utf-8')
    if not output:
        msg_status(_('Cannot open validator URL'))
        return

    #with open('/home/user/er.html', 'w') as f:
        #f.write(output)

    try:
        results = json.loads(output)
    except:
        msg_status(_('Cannot parse validator reply'))
        return

    if not results['messages']:
        msg_box(_('Document successfully checked as %s') % format, MB_OK+MB_ICONINFO)
        return

    app_log(LOG_SET_REGEX, r'Line (\d+):.+', panel=p)
    app_log(LOG_SET_LINE_ID, '1', panel=p)
    app_log(LOG_SET_NAME_ID, '0', panel=p)
    app_log(LOG_SET_FILENAME, ed.get_filename(), panel=p)
    app_log(LOG_SET_ZEROBASE, '0', panel=p)

    app_log(LOG_ADD, 'Errors found while checking document as %s:' % format, panel=p)
    app_log(LOG_ADD, '', panel=p)
    for message in results['messages']:
        app_log(LOG_ADD, 'Line %s: %s' % (message['lastLine'], message['message']), panel=p)

    ed.focus()
    ed.cmd(cmd_ShowPanelValidate)

