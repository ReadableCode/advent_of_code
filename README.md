# advent_of_code

My solutions to [Advent of Code](https://adventofcode.com/) puzzles in Python,
plus a few HackerRank practice problems. Each puzzle lives in its own folder
with the puzzle text, the example input, my input and the script that solves
it. It exists as a record of working through the puzzles, not as a library.

## What is here

| Folder | Contents |
| --- | --- |
| `2024/` | Advent of Code 2024, days 1 to 11 |
| `2025/` | Advent of Code 2025, days 1 to 8 (day 8 is in progress) |
| `hackerrank/` | HackerRank practice problems: Python, one SQL query and a React exercise |

### Advent of Code

2024:

| Day | Puzzle |
| --- | --- |
| 01 | Historian Hysteria |
| 02 | Red-Nosed Reports |
| 03 | Mull It Over |
| 04 | Ceres Search |
| 05 | Print Queue |
| 06 | Guard Gallivant |
| 07 | Bridge Repair |
| 08 | Resonant Collinearity |
| 09 | Disk Fragmenter |
| 10 | Hoof It |
| 11 | Plutonian Pebbles |

2025:

| Day | Puzzle |
| --- | --- |
| 01 | Secret Entrance |
| 02 | Gift Shop |
| 03 | Lobby |
| 04 | Printing Department |
| 05 | Cafeteria |
| 06 | Trash Compactor |
| 07 | Laboratories |
| 08 | Started, not finished |

Each day folder follows one layout:

- `day_NN_prompt.txt`: the puzzle text
- `day_NN_input_test.txt`: the small example input from the puzzle text
- `day_NN_input.txt`: the full puzzle input
- `day_NN.py`: the solution

2025 splits the solution by part: `day_NN_part_01.py` and, where part 2 needed
its own script, `day_NN_part_02.py`. Its inputs are named
`day_NN_part_01_input.txt` and `day_NN_part_01_input_test.txt`. A few 2024 days
name the example input differently (`day_03_input_sample.txt`,
`day_06_input_text.txt`).

### HackerRank

- `count_the_employees/`: SQL query
- `fizzbuzz/`: FizzBuzz
- `items_in_containers/`: count items between container walls in a string
- `minimize_system_cost/`: remove k consecutive machines to minimize the
  connection cost
- `optimizing_bow_weights/`: split weights into the smallest, heaviest set
- `react_sort_articles/`: React app that sorts articles by upvotes or date; its
  own `README.md` has the requirements and `npm` commands

## How it works

The scripts are plain Python split into `# %%` cells, so they run top to bottom
as a script or cell by cell in an editor with Jupyter support (`ipykernel` is
a dependency for this). Each one reads its input with a relative path, prints
its intermediate steps and ends by printing the answer. There is no shared
helper module; each day carries its own input parsing.

Switching between the example and the full input is done in the script: some
days have a `TEST_MODE` flag near the bottom, others pass the file name
directly. Some scripts also have a `debug` flag for extra output.

A few scripts do more than print:

- 2024 day 06 can animate the guard walking the map in the terminal
  (`ANIMATE = True`).
- 2025 day 04 can redraw the grid in the terminal as rolls are removed (`watch`).
- 2024 day 09 writes its intermediate disk layouts to `day_09_output_*.txt`
  and `day_09_output_*files.json` in its folder.

## Running

Requires Python 3.13 and [uv](https://docs.astral.sh/uv/). Dependencies are
`numpy`, `tqdm` and `ipykernel`.

```bash
uv sync
cd 2024/day_01
uv run python day_01.py
```

Run from the day's folder, since inputs are opened by relative path.

Lint settings are in `.flake8` (max line length 120).

## License

MIT, see `LICENSE`.
