from structures import Player
from datahandler import PersistentDataHandler

handler = PersistentDataHandler("test.json") 
player = handler.create_player("Paul2")


handler.write()