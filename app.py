from flask import Flask
from structures import Company, Player

app = Flask(__name__)

@app.route("/api/company/<company_name>")
def get_company(company_name:str):
    return f"Got data for company! {company_name}"

@app.route("/api/player/<player_name>")
def get_player(player_name:str):
    return f"Got data for player! {player_name}"

@app.route("/api/update/<company_name>")
def update_company(company_name:str, methods=["POST"]):
    ## TODO: Handle the request
    return f"Update Data for: {company_name}"
    

@app.route("/")
def index():
    return "Hello, world"


    """
        Data Structure:
            Update: {
                company_name:str
                player_name:str
                action: str ("Sell" || "Buy")
            }
        
            Company: {
                name: str
                value: float
                clicks: int
            }
            
            Player: {
                name: str
                cash: float
                portfolio_value: float
                current_holding: list[tuple[str, float]] # (name, bought_for)
                history: list[tuple(str, float, float)] # (name, bought_for, sold_for)
            }
    """