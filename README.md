This was a small project to build command line output in a cartesian plot based off of simple data in a table coming from a url.
Unicode blocks could be positioned anywhere, full, half upper or half lower resulting in the lower image.
| x | char | y |
| 0 |  █   | 0 |
| 0 |  ▄   | 1 |
| 0 |  ■   | 2 |


### Create the virtual environment

```python -m venv venv```

### Activate the virtual environment

```source venv/bin/activate```

### Install the required package `BeautifulSoup`. It's used to make the request and process the table

```pip install BeautifulSoup```

### Run it

```python main.py```

![alt text](image.png)