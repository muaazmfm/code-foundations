# bad
class DatabaseWriterBad:
    def __init__(self, database):
        self.database = database

    def write(self, content):
        try:
            self.database.write(content)
        except Exception as e:
            open('error.log', 'a').write(e.message)

# good
class FileWriter:
    def __init__(self, file):
        self.file = file

    def write(self, content):
        self.file.write(content)

class DatabaseWriterGood:
    def __init__(self, database, log_writer):
        self.database = database
        self.log_writer = log_writer

    def write(self, content):
        try:
            self.database.write(content)
        except Exception as e:
            self.log_writer.write(e.message)
