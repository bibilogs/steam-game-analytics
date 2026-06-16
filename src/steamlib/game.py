from .exceptions import InvalidGameError

class Game:
    def __init__(self, data):
        if 'Name' not in data:
            raise InvalidGameError(
                    f'Game name cannot be empty.'
                )
            
        self._data = data
        self._price = float(self._data['Price'])
        self._year = int(self._data['Release date'][-4:])
        
    @property
    def app_id(self):
        return self._data['AppID']
    
    @property
    def name(self):
        return self._data['Name']
    
    @property
    def release_date(self):
        return self._data['Release date']
    
    @property
    def genres(self):
        return self._data['Genres']
    
    @property
    def price(self):
        return self._price
    
    @property
    def year(self):
        return self._year
    
    @property
    def is_free(self):
        return self.price == 0