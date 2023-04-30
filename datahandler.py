from structures import Company, Player
from _thread import start_new_thread ## timed writes
from typing import Union, NoReturn
from types import NoneType
import time
import json
import os

class PersistentDataHandler:
    def __init__(self, data_file:str, write_interval:float=10):
        self.data_filename = data_file
        
        self.data:list[dict[str, Company], dict[str, Player]] = [{}, {}]
        
        if not os.path.exists(self.data_filename):
            with open(self.data_filename, "w+") as writer:
                writer.write("[]")
            
        else:
            with open(self.data_filename, "r+") as reader:
                tmpData = json.load(reader)
                
                if tmpData != []:
                
                    company_data = {x['name']: Company.from_dict(x) for x in tmpData[0]}
                    player_data = {x['name']: Player.from_dict(x) for x in tmpData[1]}
                    
                    self.data = [company_data, player_data]
        
        start_new_thread(self.write_handler, (write_interval,))
        
    def get_player(self, name:str) -> Union[Player, NoneType]:
        return self.data[1].get(name, None)
    
    def get_company(self, name:str) -> Union[Company, NoneType]:
        return self.data[0].get(name, None)
    
    def create_player(self, name:str) -> Player:
        if (player := self.get_player(name)):
            return player ## Just so other stuff can still work
        
        new_player = Player(name, 10)
        
        self.data[1][name] = new_player
        return new_player
    
    def add_company(self, name:str, logo:str, value:float, total_shares:int) -> Company:
        if (company := self.get_company(name)):
            return company
        
        new_company = Company(name, logo, value, 0, total_shares)
        self.data[0][name] = new_company
        return new_company
    
    def new_holdings(self, player_name:str, company_name:str, shares:int, cost:float) -> NoReturn:
        player = self.get_player(player_name)
        cmp = self.get_company(company_name)
        
        if company_name in player.holdings:
            player.holdings[company_name] += shares
        else:
            player.holdings[company_name] = shares
    
        player.cash -= cost
        player.portfolio_value += cost
        
        share_percent = shares/cmp.total_shares
        cmp.total_shares -= shares
        cmp.value *= shares * (share_percent + 0.1)
        

    def sell_holdings(self, player_name:str, company_name:str, shares:int) -> NoReturn:
        cmp = self.get_company(company_name)
        player = self.get_player(player_name)
        
        share_value:float = cmp.value
        total_value = share_value * shares
        player.cash += total_value
        player.portfolio_value -= total_value
        
        player.holdings[company_name] -= shares
        if player.holdings[company_name] == 0:
            del player.holdings[company_name]
            
        share_percent = shares / cmp.total_shares
        cmp.total_shares += shares
        cmp.value /= shares * (share_percent + 0.1)
    
    def write(self):
        with open(self.data_filename, "w") as writer:
            json.dump([
                    [dt.dict() for dt in self.data[0].values()],
                    [dt.dict() for dt in self.data[1].values()]
                ], writer, indent=2)
    
    ## Just some cleanup
    def __del__(self):
        self.write()
    
    def write_handler(self, write_delay:float):
        
        while True:
            time.sleep(write_delay)
            self.write()
            

