from dataclasses import dataclass, field

@dataclass
class Company:
    Name: str    ## Name of the company
    Price: float ## Current price of the stock
    Clicks: int  ## Total people who have ever clicked it

@dataclass
class Player:
    Name: str             ## Name of the company
    Cash: float           ## Value to spend on shares
    Holdings_value: float ## Total value with shares
    ## What the player is currently holding
    ## (Name, total_shares)
    Holdings: list[tuple[str, int]] = field(default_factory=list)
    ## What the player has held
    ## (Name, bought_for, sold_for)
    History: list[tuple[str, float, float]] = field(default_factory=list)