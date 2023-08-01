class TxtData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_data()

    def read_data(self):
        with open(self.file_path, 'r') as file:
            return file.readlines()

    def get_fields(self):
        return self.data[0].strip().split(',')

    def get_records(self):
        records = []
        for line in self.data[1:]:
            values = line.strip().split(',')
            record = dict(zip(self.get_fields(), values))
            records.append(record)
        return records
