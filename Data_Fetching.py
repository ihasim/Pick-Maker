import pandas as pd
import requests
from bs4 import BeautifulSoup 
import pandas as pd

champion_to_lanes = {
    "aatrox": ["top"],
    "ahri": ["mid"],
    "akali": ["top", "mid"],
    "akshan": ["mid","top"],
    "alistar": ["support"],
    "amumu": ["jungle","support"],
    "anivia": ["mid"],
    "annie": ["mid", "support"],
    "aphelios": ["adc"],
    "ashe": ["adc", "support"],
    "aurelionsol": ["mid"],
    "aurora" : ["top", "mid"],
    "azir": ["mid"],
    "bard": ["support"],
    "belveth": ["jungle"],
    "blitzcrank": ["support"],
    "brand": ["support"],
    "braum": ["support"],
    "caitlyn": ["adc"],
    "camille": ["top"],
    "cassiopeia": ["mid","mid"],
    "chogath": ["top"],
    "corki": ["mid"],
    "darius": ["top"],
    "diana": ["mid", "jungle"],
    "drmundo": ["top"],
    "draven": ["adc"],
    "ekko": ["mid", "jungle"],
    "elise": ["jungle"],
    "evelynn": ["jungle"],
    "ezreal": ["adc","mid"],
    "fiddlesticks": ["jungle"],
    "fiora": ["top"],
    "fizz": ["mid"],
    "galio": ["mid"],
    "gangplank": ["top"],
    "garen": ["top"],
    "gnar": ["top"],
    "gragas": ["top", "jungle","mid"],
    "graves": ["jungle"],
    "gwen": ["top"],
    "hecarim": ["jungle"],
    "heimerdinger": ["mid","top"],
    "illaoi": ["top"],
    "irelia": ["top", "mid"],
    "ivern": ["jungle"],
    "janna": ["support"],
    "jarvaniv": ["jungle"],
    "jax": ["top"],
    "jayce": ["top", "mid"],
    "jhin": ["adc"],
    "jinx": ["adc"],
    "ksante": ["top"],
    "kaisa": ["adc"],
    "kalista": ["adc"],
    "karma": ["support", "mid"],
    "karthus": ["jungle"],
    "kassadin": ["mid"],
    "katarina": ["mid"],
    "kayle": ["top", "mid"],
    "kayn": ["jungle"],
    "kennen": ["top"],
    "khazix": ["jungle"],
    "kindred": ["jungle"],
    "kled": ["top"],
    "kogmaw": ["adc"],
    "leblanc": ["mid"],
    "leesin": ["jungle"],
    "leona": ["support"],
    "lillia": ["jungle"],
    "lissandra": ["mid"],
    "lucian": ["adc"],
    "lulu": ["support"],
    "lux": ["mid", "support"],
    "malphite": ["top"],
    "malzahar": ["mid"],
    "maokai": ["top", "jungle", "support"],
    "masteryi": ["jungle"],
    "milio": ["support"],
    "missfortune": ["adc"],
    "mordekaiser": ["top"],
    "morgana": ["support"],
    "nami": ["support"],
    "nasus": ["top"],
    "nautilus": ["support"],
    "neeko": ["mid"],
    "nidalee": ["jungle"],
    "nilah": ["adc"],
    "nocturne": ["jungle"],
    "nunu": ["jungle"],
    "olaf": ["top", "jungle"],
    "orianna": ["mid"],
    "ornn": ["top"],
    "pantheon": ["top", "support", "mid"],
    "poppy": ["top", "jungle"],
    "pyke": ["support"],
    "qiyana": ["mid"],
    "quinn": ["top"],
    "rakan": ["support"],
    "rammus": ["jungle"],
    "reksai": ["jungle"],
    "rell": ["support", "jungle"],
    "renata": ["support"],
    "renekton": ["top"],
    "rengar": ["jungle"],
    "riven": ["top"],
    "rumble": ["top"],
    "ryze": ["mid", "top"],
    "samira": ["adc"],
    "sejuani": ["jungle"],
    "senna": ["adc", "support"],
    "seraphine": ["mid", "support"],
    "sett": ["top"],
    "shaco": ["jungle"],
    "shen": ["top"],
    "shyvana": ["jungle"],
    "singed": ["top"],
    "sion": ["top"],
    "sivir": ["adc"],
    "skarner": ["jungle"],
    "sona": ["support"],
    "soraka": ["support"],
    "swain": ["mid", "support"],
    "sylas": ["mid"],
    "syndra": ["mid"],
    "tahmkench": ["support", "top"],
    "taliyah": ["mid", "jungle"],
    "talon": ["mid", "jungle"],
    "taric": ["support"],
    "teemo": ["top"],
    "thresh": ["support"],
    "tristana": ["adc", "mid"],
    "trundle": ["jungle", "jungle"],
    "tryndamere": ["top"],
    "twistedfate": ["mid", "top"],
    "twitch": ["adc", "jungle"],
    "udyr": ["jungle"],
    "urgot": ["top"],
    "varus": ["adc"],
    "vayne": ["adc","top"],
    "veigar": ["mid"],
    "velkoz": ["mid", "support"],
    "vex": ["mid"],
    "vi": ["jungle"],
    "viego": ["jungle"],
    "viktor": ["mid"],
    "vladimir": ["top", "mid"],
    "volibear": ["top", "jungle"],
    "warwick": ["jungle"],
    "monkeyking": ["top", "jungle"],
    "xayah": ["adc"],
    "xerath": ["mid","support"],
    "xinzhao": ["jungle"],
    "yasuo": ["top", "mid"],
    "yone": ["top", "mid"],
    "yorick": ["top"],
    "yuumi": ["support"],
    "zac": ["jungle", "support", "top"],
    "zed": ["mid","jungle"],
    "zeri": ["adc", "mid"],
    "ziggs": ["mid","adc"],
    "zilean": ["support", "mid"],
    "zoe": ["mid"],
    "zyra": ["support", "mid", "jungle"]
}

def counter_scrape_data(champ:str,lane:str, data: dict):
    url= "https://www.op.gg/champions/" + champ + "/counters/" + lane+ "?type=ranked"

    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    champ_names = soup.find_all("div" , class_ = "css-72rvq0 ezvw2kd4")
    win_rates = soup.find_all("span" , class_ = "css-ekbdas ezvw2kd2")
    games_played = soup.find_all("span", class_ ="css-1nfew2i ezvw2kd0")
    champ_stats = {}
    for index in range(len(champ_names)):
        champ_stats[champ_names[index].text] = [win_rates[index].text[:4],games_played[index].text]
    data["champ_name"].append(champ)
    counters = []
    good_against = []
    playable = []
    add = []
    for i in champ_stats:
        if float(champ_stats[i][0]) > 52 :
            good_against.append(i)
        elif float(champ_stats[i][0]) < 48 :
            counters.append(i)
        elif float(champ_stats[i][0]) > 49.5 :
            playable.append(i)
    add.append(counters.copy())
    add.append(good_against.copy())
    add.append(playable.copy())
    data[lane].append(add.copy())


def build_scrape_data(champ :str, lane:str, data:dict):
    url= "https://www.op.gg/champions/" + champ + "/build/" + lane+ "?type=ranked"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    core_items =soup.find("div" , class_ = "css-37vh9h e11gfon11").find_all("img")
    for index,i in enumerate(core_items):
        core_items[index] = i["alt"]
    data["build"].append(core_items.copy())
    


"""class champion:

    def __init__(self, name:str, build:list, counters: list, good_against: list, playable: list = None, runes:dict = None) -> None:
        self.name = name
        self.counters = counters
        self.good_against = good_against
        self.playable = playable
        self.build = build
        self.runes =runes
"""

data = {"champ_name": [],
        "top": [],
        "jungle": [],
        "mid": [],
        "adc": [],
        "support": [],
        "build": [],
        "runes": []

}
def overall(champ, lane, data):
    counter_scrape_data(champ, lane, data)
    build_scrape_data(champ , lane, data)
    for i in data :
        if i != lane and i != "champ_name" and i != "build":
            data[i].append(None)

for champ in champion_to_lanes:
    for lane in champion_to_lanes[champ]:
        overall(champ,lane,data)
print("scrape over")
df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)