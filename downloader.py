import logging
from typing import Dict, List

import requests

from referencelistparser.webparser import ScriptureListParser
from filepersistor import FilePersistor
from scriptureref import ScriptureRef


class Downloader:
    def run(self):
        logging.basicConfig(level=logging.DEBUG)
        file_persistor = FilePersistor(
            '/home/joshua/PycharmProjects/scripturedownloader/downloads'
        )
        for language in ('deu',):  # ('eng', 'spa')
            file_persistor.language = language
            book_references = self.book_references(language)
            for book, references in book_references.items():
                file_persistor.book = book
                for reference in references:
                    reference.get_text()
                    file_persistor.persist(reference)

    @staticmethod
    def book_references(language: str) -> Dict[str, List[ScriptureRef]]:
        book_references = {
            'BookOfMormon': [],
            'DoctrineAndCovenants': [],
            'OldTestament': [],
            'NewTestament': [],
        }
        url = (
            'https://www.churchofjesuschrist.org/study/manual/'
            'new-testament-seminary-teacher-manual/appendix/'
            '100-scripture-mastery-passages'
        )
        resp = requests.get(url, params={'lang': language})
        scripture_parser = ScriptureListParser(book_references)
        scripture_parser.feed(resp.content.decode('utf-8'))
        return book_references


if __name__ == '__main__':
    Downloader().run()
