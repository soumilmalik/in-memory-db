# In-Memory Database

A simple key-value store that runs in the terminal. You type commands and it stores and fetches data from memory. I built this for the EHAX society project at DTU.

It's basically a dictionary with a command interface on top of it. Everything lives in memory while the program is running, and you can save it to a file so that you can use that data again after closing.

## How to run

```
python in_memory_db.py
```

That's it, no installing anything. It only uses everything inbuilt into Python.

## Commands

| Command | What it does |
|---|---|
| `SET key value` | stores a value under a key |
| `GET key` | gives you the value back |
| `DEL key` | deletes a key |
| `EXISTS key` | checks if a key is there (prints True/False) |
| `SAVE filename` | saves everything to a file |
| `LOAD filename` | loads data back in from a file |
| `HELP` | shows the list of commands |
| `QUIT` | exits |

Commands aren't case sensitive so `set` and `SET` both work. `EXIST` also works if you forget the S.

## Example

```
Enter command: SET name SOUMIL
done
Enter command: GET name
Ashmita
Enter command: EXISTS name
True
Enter command: SAVE data.json
done
Enter command: QUIT
see you!
```

Open it again and run `LOAD data.json` to get everything back.

### Sample file

I've put a sample file `states.json` in the repo with some Indian states and their capitals, so you can test LOAD without typing everything in yourself:

```
Enter command: LOAD states.json
done
Enter command: GET delhi
new delhi
Enter command: EXISTS punjab
True
```

## Some notes

- No database or caching libraries used (no SQLite, Redis, TinyDB etc.) like the project rules said. Just plain Python.
- `json` is only there for saving and loading the file. It's a standard built-in, not a storage library, so it's within the rules.
- Data stays in memory, which means it's gone once you close the program unless you SAVE it first.
- Values can have spaces in them (like `SET greeting hello world`) because of how the input is split.
