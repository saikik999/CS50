import numpy as np
import random

class Nim:
    def __init__(self, heaps):
        self.heaps = heaps
    
    def get_possible_actions(self):
        actions = []
        for heap_index, heap_size in enumerate(self.heaps):
            for i in range(1, heap_size + 1):
                actions.append((heap_index, i))
        return actions

    def is_terminal(self):
        return all(heap == 0 for heap in self.heaps)

    def perform_action(self, action):
        heap_index, amount = action
        if self.heaps[heap_index] >= amount:
            self.heaps[heap_index] -= amount
        else:
            raise ValueError("Invalid action")
    
    def get_state(self):
        return tuple(self.heaps)

class QLearningAgent:
    def __init__(self, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0, exploration_decay=0.99):
        self.q_table = {}
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay

    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def choose_action(self, state, possible_actions):
        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice(possible_actions)
        q_values = [self.get_q_value(state, action) for action in possible_actions]
        max_q = max(q_values)
        return random.choice([action for action, q in zip(possible_actions, q_values) if q == max_q])

    def update_q_table(self, state, action, reward, next_state, next_possible_actions):
        old_q = self.get_q_value(state, action)
        future_q = 0 if not next_possible_actions else max(self.get_q_value(next_state, next_action) for next_action in next_possible_actions)
        new_q = old_q + self.learning_rate * (reward + self.discount_factor * future_q - old_q)
        self.q_table[(state, action)] = new_q

    def decay_exploration_rate(self):
        self.exploration_rate *= self.exploration_decay

def train_agent(episodes, heaps):
    agent = QLearningAgent()
    for episode in range(episodes):
        game = Nim(heaps.copy())
        state = game.get_state()
        while not game.is_terminal():
            possible_actions = game.get_possible_actions()
            action = agent.choose_action(state, possible_actions)
            game.perform_action(action)
            next_state = game.get_state()
            reward = 1 if game.is_terminal() else 0
            next_possible_actions = game.get_possible_actions()
            agent.update_q_table(state, action, reward, next_state, next_possible_actions)
            state = next_state
        agent.decay_exploration_rate()
    return agent

if __name__ == "__main__":
    episodes = 10000
    heaps = [3, 4, 5]
    agent = train_agent(episodes, heaps)

    test_game = Nim(heaps.copy())
    while not test_game.is_terminal():
        state = test_game.get_state()
        possible_actions = test_game.get_possible_actions()
        action = agent.choose_action(state, possible_actions)
        test_game.perform_action(action)
        print(f"State: {state}, Action: {action}, New State: {test_game.get_state()}")
    print("Game over!")