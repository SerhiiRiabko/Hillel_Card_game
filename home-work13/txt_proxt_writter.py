class TxtWriterProxy:

    def __init__(self, filename):
        self.file_path = filename
        self.data = []
        self.modified = False

    def add_log(self, log_message):
        self.data.append(log_message)
        self.modified = True

    def save_data(self):
        if not self.modified:
            return  # No need to write if the data has not been modified

        with open(self.file_path, 'w') as file:
            for record in self.data:
                file.write(record + '\n')

        self.modified = False
