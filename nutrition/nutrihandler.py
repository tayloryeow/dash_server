import requests as rq
import re
from nutrition import nutritics_constants as nc

class NutriHandler:

    def __init__(self, clientID):
        # TODO: Get the client's preferred serving size, needed for some computations?
        # self.serving_size = getServingSize(clientID)
        print("created a client nutrition handler")



    def make_foodlist_request(self, foodname):

        # req = rq.get()
        print("created")


    def build_foodlist_request(self, foodname):

        reqstring = nc.BASE_URL + "LIST/&limit=1&food=" + foodname
        reqstring = reqstring + "&attr=name,energyKcal,carbohydrate,protein,fat"

    def build_authentication(self):
        authline = e.headers['www-authenticate']
        authobj = re.compile(r'''(?:\s*www-authenticate\s*:)?\s*(\w*)\s+realm=['"]([^'"]+)['"]''', re.IGNORECASE)
        matchobj = authobj.match(authline)