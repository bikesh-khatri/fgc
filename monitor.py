import requests
from lxml import html

URL = "https://first.global/volunteer/"
XPATH = '/html/body/div[2]/div/div/div/div[1]/div/div/div[8]/div/div/div/div/div/div[2]/div'

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=headers)
tree = html.fromstring(response.content)

elements = tree.xpath(XPATH)

current_text = ""
for el in elements:
    current_text = el.text_content().strip()

try:
    with open("last.txt") as f:
        last_text = f.read().strip()
except:
    last_text = ""

if current_text != last_text:
    print("Change detected!")

    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": "ak7udq19rd9tyzp394xse8kvcs215x",
            "user": "u2r3gg3ydq91m48m6527y5rgq7tahy",
            "message": f"Volunteer page changed:\n{current_text}"
        }
    )

    with open("last.txt", "w") as f:
        f.write(current_text)

else:
    print("No change detected.")
