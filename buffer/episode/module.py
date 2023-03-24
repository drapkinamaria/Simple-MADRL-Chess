from buffer.base import Buffer
import numpy as np


class Episode:
    def __init__(self) -> None:
        self.goals = []
        self.probs = []
        self.values = []
        self.states = []
        self.rewards = []
        self.actions = []

    def add(
        self,
        state: np.ndarray,
        reward: float,
        action,
        goal: bool,
        prob: float = None,
        value: float = None,
    ):
        self.goals.append(goal)
        self.states.append(state)
        self.rewards.append(reward)
        self.actions.append(action)

        if prob is not None:
            self.probs.append(prob)
        if value is not None:
            self.values.append(value)
        
        
    def calc_advantage(self, gamma: float, gae_lambda: float) -> np.ndarray:
        n = len(self.rewards)
        advantages = np.zeros(n)
        for t in range(n - 1):
            discount = 1 
            for k in range(t, n - 1):
                advantages[t] += (
                    discount
                    * (
                        self.reward[k]
                        + gamma * self.value[k + 1] * (1 - int(self.goal[k]))
                    )
                    - self.value[k]
                )
                discount *= gamma * gae_lambda
        return advantages
