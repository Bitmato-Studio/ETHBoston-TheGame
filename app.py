from flask import Flask, render_template, request, redirect, url_for
from structures import Company, Player

app = Flask(__name__)

# Define the Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.cash = 100000
        self.portfolio_value = 0
        self.current_holding = {}
        self.history = []

# Initialize the DUMMY player
player = Player("John Doe")

# Initialize company data - FOR 14 Companies = 14 Sponsors
companies = [
    {'name': 'Company A', 'value': 100.0, 'clicks': 0, 'total_shares': 1000},
    {'name': 'Company B', 'value': 200.0, 'clicks': 0, 'total_shares': 2000},
    {'name': 'Company C', 'value': 300.0, 'clicks': 0, 'total_shares': 1500},
    {'name': 'Company D', 'value': 400.0, 'clicks': 0, 'total_shares': 3000},
    {'name': 'Company E', 'value': 250.0, 'clicks': 0, 'total_shares': 2500},
    {'name': 'Company F', 'value': 350.0, 'clicks': 0, 'total_shares': 1200},
    {'name': 'Company G', 'value': 175.0, 'clicks': 0, 'total_shares': 500},
    {'name': 'Company H', 'value': 450.0, 'clicks': 0, 'total_shares': 600},
    {'name': 'Company I', 'value': 125.0, 'clicks': 0, 'total_shares': 1800},
    {'name': 'Company J', 'value': 275.0, 'clicks': 0, 'total_shares': 1400},
    {'name': 'Company K', 'value': 320.0, 'clicks': 0, 'total_shares': 2300},
    {'name': 'Company L', 'value': 210.0, 'clicks': 0, 'total_shares': 1700},
    {'name': 'Company M', 'value': 190.0, 'clicks': 0, 'total_shares': 900},
    {'name': 'Company N', 'value': 220.0, 'clicks': 0, 'total_shares': 2600}
]


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


@app.route('/') #authored by: @pshroff 
def index():
    sorted_companies = sorted(companies, key=lambda x: x['value'], reverse=True)

    # Calculate the total value of shares for each holding
    holdings_with_value = []
    for company_name, shares in player.current_holding.items():
        company = next((c for c in companies if c['name'] == company_name), None)
        total_value = shares * company['value']
        holdings_with_value.append((company_name, shares, total_value))

    return render_template('index.html', companies=sorted_companies, player=player, holdings_with_value=holdings_with_value)

@app.route('/vote', methods=['POST']) #authored by: @pshroff 
def vote():
    company_name = request.form.get('company')
    for company in companies:
        if company['name'] == company_name:
            company['clicks'] += 1
            break
    return redirect(url_for('index'))


@app.route('/trade', methods=['POST']) #authored by: @pshroff 
def trade():
    company_name = request.form.get('company')
    action = request.form.get('action')
    shares = int(request.form.get('shares'))

    company = next((c for c in companies if c['name'] == company_name), None)

    if action == "Buy":
        cost = company['value'] * shares
        if player.cash >= cost and company['total_shares'] >= shares:
            player.cash -= cost
            player.portfolio_value += cost
            player.current_holding[company_name] = player.current_holding.get(company_name, 0) + shares
            company['total_shares'] -= shares
    elif action == "Sell":
        current_shares = player.current_holding.get(company_name, 0)
        if current_shares >= shares:
            value_per_share = company['value']
            total_value = value_per_share * shares
            player.cash += total_value
            player.portfolio_value -= total_value
            player.current_holding[company_name] -= shares
            if player.current_holding[company_name] == 0:
                del player.current_holding[company_name]
            company['total_shares'] += shares

    return redirect(url_for('index'))


    """
        Data Structure:
            Update: {
                company_name:str
                player_name:str
                action: str ("Sell" || "Buy")
            }
        
            Company: {
                name: str
                value: int
                clicks: int
                total_shares: int
            }
            
            Player: {
                name: str
                cash: int
                portfolio_value: int
                current_holding: list[tuple[str, int]] # (name, bought_for)
                history: list[tuple(str, int, int)] # (name, bought_for, sold_for)
            }
    """


if __name__ == '__main__':
    app.run(debug=True)