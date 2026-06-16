import csv
from .game import Game
from .exceptions import InvalidCsvError

class SteamRepository:

    def __init__(self, file_path):
        self._raw_data = []
        self._games = []
        
        self._load_csv(file_path)
        self._load_games()

    def _load_csv(self, file_path):
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                
                required_columns = [
                    'AppID', 
                    'Name', 
                    'Release date', 
                    'Price', 
                    'Genres'
                ]

                for column in required_columns:
                    if column not in reader.fieldnames:
                        raise InvalidCsvError(
                            f'Missing required column: {column}.'
                        )
                        
                for row in reader:
                    self._raw_data.append(row)
                    
        except FileNotFoundError:
            raise FileNotFoundError(
                f'File not found.'
            )
    
    def _load_games(self):        
        for row in self._raw_data:
            self._games.append(Game(row))
            
    @property
    def raw_data(self):
        return self._raw_data
    
    @property
    def games(self):
        return self._games