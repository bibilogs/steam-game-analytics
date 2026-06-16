from collections import Counter
from .game import Game

class SteamAnalysis:
    def __init__(self, games):
        self.games = games
    
    # First question.
    def free_paid_percent(self):
        total = len(self.games)
        free = sum(1 for game in self.games if game.is_free)
        paid = total - free
        
        return {
            'free': (free / total) * 100,
            'paid': (paid / total) * 100
        }
        
    # Second question.
    def year_with_more_releases(self):
        years = Counter()       # Using counter to deal with missing keys.
        
        for game in self.games:
            year = game.year
            
            if year:
                years[year] += 1
        
        max_games_qt = max(years.values())
        max_years = [year for year, quantity in years.items() if quantity == max_games_qt]
        
        return max_years, max_games_qt
        
    # Third question.
    def most_common_genre(self):
        genres = Counter()
        
        for game in self.games:
            for genre in game.genres.split(','):
                genre = genre.strip()
                if genre:
                    genres[genre] += 1
                
        return genres.most_common(1)[0]