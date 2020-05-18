from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time
import requests
import sys
import pathlib
from colorama import Fore, Style, init
start = time.time() #will count after end

## "Usage: {sys.argv[0]} [count] [tags]"

## example character tags accrording safebootu:
## incorrect statement ["miyamoto musashi"],["miyamoto_musashi_(fate/grand_order)"]
## correct statement ["miyamoto_musashi+"],["miyamoto_musashi_%28fate%2fgrand_order%29+"]
## according to your needs,adjust it, there's so many tags


print(Fore.RED)
print("""

 _____           _   _                _     
/  ___|         | | | |              | |    
\ `--.  ___ __ _| |_| |__   __ _  ___| |__  
 `--. \/ __/ _` | __| '_ \ / _` |/ __| '_ \ 
/\__/ / (_| (_| | |_| | | | (_| | (__| | | |
\____/ \___\__,_|\__|_| |_|\__,_|\___|_| |_|                                                                                   
                            Safebooru scraper -Sin""")
print(Style.RESET_ALL)
print(Fore.GREEN)

init()
if len(sys.argv) < 3:
    sys.exit(f"Usage: {sys.argv[0]} [count] [tags]")
    print(Style.RESET_ALL)

for tag in sys.argv[2:]:
    pathlib.Path(f"./{tag}").mkdir(exist_ok=True)

    for pid in range(0, int(sys.argv[1])):
        response = requests.get(f"https://safebooru.org/index.php?page=dapi&s=post&q=index&limit=100&tags={tag}&pid={pid}") #api
        content = BeautifulSoup(response.content, "html.parser")

        for link in content.find_all("post"):
            image_url = link.get("file_url")
            image_url_split = urlparse(image_url).path.split("/")
            file = image_url_split[len(image_url_split) - 1]

            image = requests.get(image_url)

            dog = image_url.replace('https://safebooru.org/', '/')
            print(f"Stealing {dog} === {file}")

            open(f"./{tag}/{file}", "wb").write(image.content)

end = time.time() #tutup

hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))            