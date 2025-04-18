import numpy as np
import gym
from gym import spaces

class BlackJack(gym.Env):
    def __init__(self):
        super(BlackJack, self).__init__()
        self.action_space = spaces.Discrete(2)  # 0 Stick 1 Hit
        self.observation_space = spaces.Tuple((spaces.Discrete(13), spaces.Discrete(22)))
        self.reset()
    
    def draw_card(self):
        value = np.random.randint(1, 14)  # Card value between 1 and 13
        color = 'black' if np.random.rand() < 2/3 else 'red'  # 2/3 black 1/3 red
        return value, color
    
    def reset(self):
        self.dealer_first_card, _ = self.draw_card()
        self.dealer_sum = self.dealer_first_card  # Dealer starts with one black card
        self.player_cards = [self.draw_card()]
        self.player_sum = self.player_cards[0][0]  # Player starts with one black card
        self.dealer_cards = [(self.dealer_first_card, 'black')]
        self.terminal = False
        return (self.dealer_first_card, self.player_sum)
    
    def step(self, action):
        if self.terminal:
            raise ValueError("Game is over. Reset environment.")
        
        if action == 1:  # Hit
            value, color = self.draw_card()
            self.player_cards.append((value, color))
            self.player_sum += value if color == 'black' else -value
            if self.player_sum < 1 or self.player_sum > 21:
                self.terminal = True
                return (None, None), -1, True, {}
            return (self.dealer_first_card, self.player_sum), 0, False, {}
        
        elif action == 0:  # Stick
            # Dealer's turn
            while self.dealer_sum < 17:
                value, color = self.draw_card()
                self.dealer_cards.append((value, color))
                self.dealer_sum += value if color == 'black' else -value
                if self.dealer_sum < 1 or self.dealer_sum > 21:
                    self.terminal = True
                    return (None, None), 1, True, {}
            
            # Compare results
            self.terminal = True
            if self.dealer_sum > self.player_sum:
                return (None, None), -1, True, {}  # Player loses
            elif self.dealer_sum < self.player_sum:
                return (None, None), 1, True, {}  # Player wins
            else:
                return (None, None), 0, True, {}  # Draw
        
        else:
            raise ValueError("Invalid action. Use 0 (stick) or 1 (hit).")