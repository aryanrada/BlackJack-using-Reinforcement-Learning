# 🃏 Blackjack Reinforcement Learning

This project implements a simplified **Blackjack environment** and applies **Monte Carlo Control** and **SARSA(λ)** reinforcement learning algorithms to learn an optimal policy.

---

## 📂 Project Structure

- `game.py` — Custom OpenAI Gym-style environment for Blackjack with stochastic transitions.
- `BlackJack.ipynb` — Jupyter Notebook containing:
  - Monte Carlo Control
  - SARSA(λ) (forward-view)
  - Epsilon-greedy policy
  - MSE vs Lambda analysis
  - Learning curve visualization

---

## 🎮 Blackjack Environment

The environment is a variation of the classic Blackjack game with the following properties:

- Cards have values from 1 to 13.
- Cards are either:
  - **Black** with probability 2/3 (adds to sum)
  - **Red** with probability 1/3 (subtracts from sum)
- Player starts with one black card; dealer also starts with one black card.
- Player actions:
  - `0` — Stick (stop drawing)
  - `1` — Hit (draw another card)
- Episode ends if:
  - Player goes below 1 or above 21.
  - Dealer sticks or busts.
- Rewards:
  - `+1` for player win
  - `-1` for player loss
  - `0` for draw

---

## 🤖 Algorithms Implemented

### 🧮 Monte Carlo Control
- First-visit Monte Carlo
- Epsilon-greedy action selection
- Updates `Q(s, a)` using complete episodes
- Visualizes learned **state-value function**

### 🔁 SARSA(λ)
- Forward-view SARSA with n-step returns
- Lambda parameter for bias-variance trade-off
- Supports λ ∈ [0, 1] where:
  - `λ = 0`: TD(0)
  - `λ = 1`: Monte Carlo
- Compares performance to Monte Carlo `Q*`
