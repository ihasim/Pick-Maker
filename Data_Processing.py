import pandas as pd 

df = pd.read_csv("data.csv")

class Champion:

    def __init__(self, name:str, lane:str, build:list, counters: list, good_against: list, playable: list = None, runes:dict = None) -> None:
        self.name = name
        self.counters = counters
        self.good_against = good_against
        self.playable = playable
        self.build = build
        self.runes =runes
        self.lane = lane

def get_champ(champ_name, champ_lane):
    filtered_row= df[(df["champ_name"] == champ_name ) & (df["lane"] == champ_lane)]

    if not filtered_row.empty:
        row = filtered_row.iloc[0]
        champion = Champion(
            name = row["champ_name"],
            lane = row["lane"],
            counters=row['counters'],
            good_against=row['good against'],
            playable=row['playable'],
            build=row['build'],
            runes=row['runes']
    )
    else:
        return False, ("Wrong champ name or incorrect lane. Please check your input :)")
    
    return True , champion

print(get_champ("riven","top"))
print(get_champ("Riven","top"))
