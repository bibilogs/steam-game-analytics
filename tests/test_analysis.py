import unittest
from src.steamlib import SteamAnalysis
from src.steamlib import SteamRepository

class TestSteamAnalysis(unittest.TestCase):
    def setUp(self):
        repository = SteamRepository('data\sample_games.csv')
        self.analysis = SteamAnalysis(repository.games)
    
    def test_free_paid_percent(self):
        result = self.analysis.free_paid_percent()
        
        self.assertEqual(result['free'], 20.0)
        self.assertEqual(result['paid'], 80.0)
        
    def test_year_with_more_releases(self):
        years, quantity = self.analysis.year_with_more_releases()
        
        self.assertEqual(years, [2022])
        self.assertEqual(quantity, 5)
        
    def test_most_common_genre(self):
        genre, count = self.analysis.most_common_genre()
        
        self.assertEqual(genre, 'Indie')
        self.assertEqual(count, 15)
        
if __name__ == "__main__":
    unittest.main()
        
        