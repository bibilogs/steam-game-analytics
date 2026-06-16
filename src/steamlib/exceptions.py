class SteamRepositoryException(Exception):
    pass

class InvalidCsvError(SteamRepositoryException):
    pass

class InvalidGameError(SteamRepositoryException):
    pass