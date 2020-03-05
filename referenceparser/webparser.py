from html.parser import HTMLParser


class ScriptureParser(HTMLParser):
    """

    """
    def error(self, message):
        raise ValueError('AH!')

    def __init__(self):
        super().__init__()
        self.text = ''
        self.state = 'start'

    def handle_starttag(self, tag, attrs):
        if self.state == 'start' and tag == 'p':
            self.state = 'find_verse_num'
            return
        if self.state == 'find_verse_num' and tag == 'span':
            self.state = 'get_verse_num'
            return
        if self.state == 'get_verse_text' and tag == 'sup':
            self.state = 'ignore_text'
            return

    def handle_data(self, data):
        if self.state in ('get_verse_num', 'get_verse_text'):
            self.text += data

    def handle_endtag(self, tag):
        if self.state == 'get_verse_num' and tag == 'span':
            self.state = 'get_verse_text'
        if self.state == 'ignore_text' and tag == 'sup':
            self.state = 'get_verse_text'
