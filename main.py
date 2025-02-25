import requests
from bs4 import BeautifulSoup

url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"

def decode(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")  # Use html.parser if you're working with local files or response.text
    table = soup.find("table")
    rows = table.find_all("tr")[1:]  # Skip the first row (header)

    output = []
    dict = {}
    max_x = 0
    max_y = 0
    for row in rows:
        cols = row.find_all("td")
        x = cols[0].text.strip()
        y = cols[2].text.strip()
        char = cols[1].text.strip()
        max_x = max(max_x, int(x))
        max_y = max(max_y, int(y))
        dict[f"{x},{y}"] = char

    dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[0])} 

    for y in range(max_y + 1):
        output.append([])
        for x in range(max_x + 1):
            if (f"{x},{y}" in dict):
                output[y].append(dict[f"{x},{y}"])
            else:
                output[y].append(" ")

    output = reversed(output)

    for row in output:
        print("".join(row))

goodies = decode(url)
