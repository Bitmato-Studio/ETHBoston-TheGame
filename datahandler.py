from structures import Company, Player
from _thread import start_new_thread ## timed writes
from typing import Union
from types import NoneType
import time
import json
import os

class PersistentDataHandler:
    def __init__(self, data_file:str):
        self.data_filename = data_file
        
        self.data:list[list[Company], list[Player]] = [[], []]
        
        if not os.path.exists(self.data_filename):
            with open(self.data_filename, "w+") as writer:
                writer.write("[]")
            
        else:
            with open(self.data_filename, "r+") as reader:
                tmpData = json.load(reader)
                
                company_data = [Company.from_dict(x) for x in tmpData[0]]
                player_data = [Player.from_dict(x) for x in tmpData[1]]
                
                self.data = [company_data, player_data]
        print(self.data )
    def get_player(self, name:str) -> Union[Player, NoneType]:
        p = [ply for ply in self.data[1] if ply and ply.name == name]
        
        return p[0] if len(p) >= 1 else None
    
    def create_player(self, name:str) -> Player:
        if (player := self.get_player(name)):
            return player ## Just so other stuff can still work
        
        new_player = Player(name)
        
        self.data[1].append(new_player)
        return new_player
    
    def update_holdings(self, player_name:str, company_name:str, total_new_holdings:int) -> NoneType:
        ...
    
    def write(self):
        with open(self.data_filename, "w") as writer:
            json.dump([
                    [dt.dict() for dt in self.data[0]],
                    [dt.dict() for dt in self.data[1]]
                ], writer, indent=2)
            
    def write_handler(self, write_delay:float):
        ## TODO: Timed writes
        ...

