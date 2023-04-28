from flask import Flask, render_template, request, redirect, url_for
from structures import Company, Player

app = Flask(__name__)

# Initialize DUMMY company data
companies = [
    {'name': 'Company A', 'value': 100.0, 'clicks': 0},
    {'name': 'Company B', 'value': 200.0, 'clicks': 0},
    {'name': 'Company C', 'value': 300.0, 'clicks': 0}
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
    

# FRONT-END ROUTES

@app.route("/")
def index():
    return render_template('index.html', companies=companies)

@app.route('/vote', methods=['POST'])
def vote():
    company_name = request.form.get('company')
    for company in companies:
        if company['name'] == company_name:
            company['clicks'] += 1
            break
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


if __name__ == '__main__':
    app.run(debug=True)