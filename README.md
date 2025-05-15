# QuixoBot - Minimax AI for Quixo

QuixoBot is a Python implementation of an AI agent for the board game [Quixo]([https://en.wikipedia.org/wiki/Quixo](https://www.artofplay.com/products/quixo?srsltid=AfmBOoose3LRfh4u9d10AUDmMKg2IYw--_TQpov9mfNuOi5Cs4fwM6Qw)). It uses the **Minimax algorithm with alpha-beta pruning** to play competitively on a 5x5 board, evaluating possible moves and selecting the most strategic option each turn.

---

## Features

- Implements **Minimax algorithm** with alpha-beta pruning.
- Board evaluation includes:
  - Row, column, and diagonal scoring.
  - Bonuses for center control.
  - Penalties for opponent alignment threats.
- Supports directional moves (Up, Down, Left, Right) for edge pieces.
- Detects win conditions and simulates moves using deep copies.

---

## Project Structure
quixobot/
├── quixo_bot.py # Core AI logic (QuixoBot class)
├── README.md # Project overview


---

## How It Works

- The bot chooses only **edge tiles** to push into the board, in any of four directions (`U`, `D`, `L`, `R`).
- Only tiles that are empty or belong to the bot can be moved.
- The board is a 5x5 grid where:
  - `1` = Bot's symbol
  - `-1` = Opponent
  - `0` = Empty

---

## Sample Usage

```python
from quixo_bot import QuixoBot

# Initialize bot as player 1
bot = QuixoBot(symbol=1)

# Create empty board
board = [[0]*5 for _ in range(5)]

# Ask the bot to make a move
new_board = bot.play_turn(board)
