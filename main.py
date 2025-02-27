import requests
import asyncio

from bs4 import BeautifulSoup

url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
# url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"

async def decode(url):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, lambda url: requests.get(url), url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")[1:]

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

async def main():
    await decode(url)

asyncio.run(main())