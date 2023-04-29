from structures import Player
from datahandler import PersistentDataHandler

handler = PersistentDataHandler("test.json") 
player = handler.get_player("Paul")
print(player)
player.name = "Paul2"


handler.write()