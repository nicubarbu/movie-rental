from dataclasses import dataclass

@dataclass
class ClientDTO:
    name: str
    rent_number: int
    

@dataclass
class MovieDTO:
    id_movie: int
    name: str
    description: str
    genre: str