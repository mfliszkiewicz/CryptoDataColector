import requests
import pandas as pd

request = requests.get("https://api.viewbase.com/exchange").text

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', '{:.4f}'.format)
#pd.set_option('display.expand_frame_repr', False)

data = pd.read_json(request)



print(data)



