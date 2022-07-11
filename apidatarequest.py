import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import pandas as pd
from pandas import json_normalize
from tqdm import tqdm
from datetime import datetime

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

data = pd.read_csv("kpn_hereditary_ability.csv", encoding="UTF-8")
kpn_list = data['kpn'].tolist()

apiData = pd.DataFrame()
home_url = 'https://chuksaro.nias.go.kr/openapi/brblInfoOk.jsp?dataType=json&brblNo='
current_time = datetime.now()

for i in tqdm(range(len(kpn_list))):
# for i in range(5):
    kpn_name = str(kpn_list[i])    
    url = home_url + kpn_name

    response = requests.get(url, verify=False)
    response.raise_for_status()
    response.encoding='utf-8'

    r_json = json.loads(response.text)
    plus_json = pd.DataFrame(json_normalize(r_json[1]))
    kpn_df = pd.DataFrame({'kpn' : [str(kpn_list[i])]})
    all_json = pd.concat([kpn_df,plus_json],axis=1)
    apiData = apiData.append(all_json)

apiData.set_index('kpn', inplace=True)
apiData.to_csv("apidata"+current_time.strftime('%Y%M%d')+".csv")
print(apiData.head())