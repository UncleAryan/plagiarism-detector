from difflib import SequenceMatcher
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

data_set_path = os.path.join(current_dir, 'data-set.txt')
file_path = os.path.join(current_dir, 'plagiarism-check.txt')

with open(data_set_path) as file_data_set, open(file_path) as file:
    data_set = file_data_set.read()
    file_data = file.read()
    check_similarity = (SequenceMatcher(None, data_set, file_data).ratio()) * 100
    print(f'The plagiarized content is {check_similarity}%')