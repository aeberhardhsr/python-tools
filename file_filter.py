import os
import glob



with open('trainlog.txt', 'rb') as file_in:
    with open("filtered_training_results.txt", "wb") as file_out:
        file_out.writelines(filter(lambda line: b'avg loss' in line, file_in))