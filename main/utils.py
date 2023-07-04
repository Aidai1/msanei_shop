import csv


# Функция для записи в csv файл
class WriteToCsv:
    # file_name, title, data_list[]
    def __init__(self, file_name, title, data):
        self.file_name = file_name
        self.title = title
        self.data = data
    
    def write(self):
        pass