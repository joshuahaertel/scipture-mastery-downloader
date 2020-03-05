from scriptureref import ScriptureRef


class FilePersistor:
    def __init__(self, file_base):
        self.file_base = file_base
        self.language = None
        self.book = None

    def persist(self, reference: ScriptureRef):
        with open(self.get_file_name(reference), 'w') as file:
            file.write(reference.text)

    def get_file_name(self, reference):
        return (
            f'{self.file_base}/'
            f'{self.book}/'
            f'{self.language}/'
            f'{reference.file_name}.txt'
        )
