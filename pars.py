import requests
from bs4 import BeautifulSoup


link = "https://github.com/Newbilius/Old-Games_DOS_Game_Gauntlet/blob/master/GAMES.csv"
responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id="repo-content-pjax-container")


check_game = block.find('table')


print()

#with open("1.txt", "w", encoding="utf-8") as file:
    #file.write(check_game)

