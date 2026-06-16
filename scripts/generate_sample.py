import csv
import random

def generate_sample(input_path, ouput_path, sample_size):
    random.seed(42)
                    
    with open(input_path, newline='', encoding='utf-8') as csvfile:
        reader = list(csv.DictReader(csvfile))
        
    sample = random.sample(reader[20:], sample_size)
    
    with open(ouput_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=reader[0].keys()
            )
        
        writer.writeheader()
        writer.writerows(sample)
        
generate_sample(
    'data/steam_games.csv',
    'data/sample_games.csv',
    sample_size=20
)