# nets_scraper

## About

## Setting up the environment
After cloning the repo, initial the environment:

``` python<version> -m venv scraper_env```

```source scraper_env/bin/activate ```

``` pip install -r .\ requirements. txt```

Every other time after initial settup, activate the environment:

```source scraper_env/bin/activate ```

When you are done working, deactivate the environment

```deactivate```

# Files
## players_tables_scraper.py
from https://www.basketball-reference.com/players/

Goes through all players on site and creates the following table as a .csv file.

|   |Games|Points|Total Rebounds|Assists|Field Goal Percentage| 3pt Field Goal Percentage|Effective Field Goal Percentage|
|----|----|----|----|----|----| ----| ----|
|Player 1|    |    |    |    |    |     |     |
|Player 2|    |    |    |    |    |     |     |
|Player 3|    |    |    |    |    |     |     |

