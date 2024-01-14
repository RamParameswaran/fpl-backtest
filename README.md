# fpl-backtest

This is a simple backtesting tool for the Fantasy Premier League.
It uses player and fixture data compiled by the [Fantasy-Premier-League](https://github.com/vaastav/Fantasy-Premier-League) project.

## Usage

### Data fetching

Data is fetched from the Fantasy-Premier-League Github repo, which is updated after each FPL game week.

This command will fetch the latest data to the `./data` directory.

```bash
bash update-data.sh
```