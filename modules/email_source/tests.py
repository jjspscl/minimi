import os
from django.test import TestCase
from .csv_reader import process_csv

# generate temporary csv files for testing
# def generate_test_csv(file_name, data):
#     csv_file = open(file_name, 'w') 
#     for line in data:
#         csv_file.write(f"{line}\n")
#     csv_file.close()

# class CSVReaderTestCase(TestCase):
#     FILE_NAMES = ['test.csv', 'test_empty.csv', 'test_invalid.csv']
#     def setUp(self):
#         self.test_data = [
#             f'"test{x}"' for x in range(1, 1000)
#         ]
#         self.test_empty = []
#         self.test_invalid = [
#             f'test{x},' for x in range(1, 1000)
#         ]
        
#         generate_test_csv(self.FILE_NAMES[0], self.test_data)
#         generate_test_csv(self.FILE_NAMES[1], self.test_empty)
#         generate_test_csv(self.FILE_NAMES[2], self.test_invalid)

#     def tearDown(self):
#         for file in self.FILE_NAMES:
#             os.remove(file)


#     def test_csv_reader(self):
#         csv_file = open('test.csv', 'r')
#         data = process_csv(csv_file)
#         self.assertEqual(data, self.test_data)
#         csv_file.close()

    # def test_csv_reader_empty(self):
    #     csv_file = open('test_empty.csv', 'r')
    #     data = process_csv(csv_file)
    #     self.assertEqual(data, [])
    #     csv_file.close()

    # def test_csv_reader_invalid(self):
    #     csv_file = open('test_invalid.csv', 'r')
    #     data = process_csv(csv_file)
    #     self.assertEqual(data, [])
    #     csv_file.close()
