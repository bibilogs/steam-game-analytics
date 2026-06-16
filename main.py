from src.steamlib import SteamAnalysis
from src.steamlib import SteamRepository

def main():
    repository = SteamRepository('data\steam_games.csv')
    analysis = SteamAnalysis(repository.games)
    
    print('------------------------------------------\n')
    print('A N A L Y S I S'.center(42))
    print('\n------------------------------------------\n')
    
    # First question.
    percentages = analysis.free_paid_percent()
    print('What percentage of the games on the platform are free and what are paid?')
    print(f"Free games: {percentages['free']:.2f}%")
    print(f"Paid games: {percentages['paid']:.2f}%\n")
    
    # Second question.
    years, count = analysis.year_with_more_releases()
    print('Which year had the highest number of new games?')
    print(f"Year(s) with most releases: {', '.join(str(year) for year in years)}\n" )
    
    # Third question.
    genre, count = analysis.most_common_genre()
    print('What is the most common genre on the platform?')
    print(f"Most common genre: {genre} ({count} games)")
    

if __name__ == "__main__":
    main()