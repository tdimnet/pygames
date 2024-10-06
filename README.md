# pygames
Collection of games built with Python on my Raspberry Pi.

You can run them on Linux, Mac, and Windows, as long as Python is installed on your machine.


## Prerequisites

- Python (version 3.9 and more should work fine).
- Virtualenv.


## How to install

Once the repo has been cloned on your computer, cd into on the game, e.g. `cd 02-boing`.


- Setting up venv

```
$ python3 -m venv venv
```


- Launching the virtual environment

```
$ source venv/bin/activate
```


- Installing the dependencies

```
$ pip install -r requirements.txt
```


To exit the virtual env (once you finish playing with the games).

```
deactivate
```


## How to play?

- All the games are located into specific folders. For example, the Pong clone, called **Boing!**, is located in the `02-boing` folder.
- Open a terminal and cd into it, e.g. `cd 02-boing`.
- Then launch the game by calling the app file with python, e.g. `python app.py`.
- To exit the game, close the game window.


## Games

- [Boing](./02-boing): **WIP** - A Pong clone.

