class TxtDataProxy:
    def __init__(self, file_path):
        self.file_path = file_path
        self.txt_data = None

    def read_data(self):
        if self.txt_data is None:
            with open(self.file_path, 'r') as file:
                self.txt_data = file.readlines()
        return self.txt_data

    def get_fields(self):
        data = self.read_data()
        return data[0].strip().split(',')

    def get_records(self):
        data = self.read_data()
        records = []
        for line in data[1:]:
            values = line.strip().split(',')
            record = dict(zip(self.get_fields(), values))
            records.append(record)
        return records
