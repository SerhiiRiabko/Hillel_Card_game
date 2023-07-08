class TxtWriterProxy:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def write_data(self, record):
        self.data.append(record)

    def save_data(self):
        with open(self.file_path, 'w') as file:
            for record in self.data:
                file.write(record + '\n')
