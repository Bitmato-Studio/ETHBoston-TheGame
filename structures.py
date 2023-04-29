from dataclasses import dataclass, field, asdict

@dataclass
class Company:
    name: str    ## Name of the company
    price: float ## Current price of the stock
    clicks: int  ## Total people who have ever clicked it
    total_shares: int ## Total shares
    
    @staticmethod
    def from_dict(data:dict) -> object:
        return Company(
            data['name'],
            data['price'],
            data['clicks'],
            data['total_shares']
        )
    
    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}
    
@dataclass
class Player:
    name: str                  ## Name of the company
    cash: float = 100_000      ## Value to spend on shares
    portfolio_value: float = 0 ## Total value with shares
    ## What the player is currently holding
    ## (Name, total_shares)
    holdings: list[tuple[str, int]] = field(default_factory=list)
    ## What the player has held
    ## (Name, bought_for, sold_for)
    history: list[tuple[str, float, float]] = field(default_factory=list)
    
    @staticmethod
    def from_dict(data:dict) -> object:
        return Player(
            data['name'],
            ## For some reason asdict converts everything to string :/
            float(data['cash']),
            float(data['portfolio_value']),
            data['holdings'],
            data['history']
        )
    
    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}