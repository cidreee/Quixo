# QuixoBot - Minimax AI for Quixo

QuixoBot is a Python implementation of an AI agent for the board game [Quixo](https://en.wikipedia.org/wiki/Quixo). It uses the **Minimax algorithm with alpha-beta pruning** to play competitively on a 5x5 board, evaluating possible moves and selecting the most strategic option each turn.

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

