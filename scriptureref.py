import logging

import requests

from referenceparser.webparser import ScriptureParser

logger = logging.getLogger(__name__)


class ScriptureRef:
    def __init__(self, url: str, reference):
        self.url = url
        self.reference = reference
        self.text = ''

    def get_text(self):
        logger.debug('Getting text for url: %s', self.url)
        # url = /study/scriptures/pgp/moses/1.39?lang=eng#p3
        full_url, url_directives = self.url.rsplit('?')  # type: str, str
        # full_url = /study/scriptures/pgp/moses/1.39
        _, _, api_url = full_url.split('/', 2)
        # api_url = scriptures/pgp/moses/1.39
        # url_directives = lang=eng#p3
        query_param, _ = url_directives.split('#')  # type: str, str
        # query_param = lang=eng
        _, language = query_param.split('=')

        uris_param = f'/{language}/{api_url}'
        logger.debug('Hitting api v2 with uris: %s', uris_param)

        response = requests.get(
            'https://www.churchofjesuschrist.org/content/api/v2',
            params={'uris': uris_param},
        )
        response_json = response.json()  # type: dict
        logger.debug('response json: %s', response_json)
        text_list = []
        for _, reference_data in response_json.items():
            for verse_content in reference_data['content']:  # type: dict
                parser = ScriptureParser()
                parser.feed(verse_content['markup'])
                text_list.append(parser.text)
        self.text = ' '.join(text_list)

    @property
    def file_name(self):
        return self.reference
