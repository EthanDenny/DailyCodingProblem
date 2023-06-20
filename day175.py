from random import random

class TransProb:
    def __init__(self, start_state: str, end_state: str, probability: float):
        self.start_state: str = start_state
        self.end_state: str = end_state
        self.probability: float = probability

TRANSITIONS: list[TransProb] = [
    TransProb('a', 'a', 0.9),
    TransProb('a', 'b', 0.075),
    TransProb('a', 'c', 0.025),
    TransProb('b', 'a', 0.15),
    TransProb('b', 'b', 0.8),
    TransProb('b', 'c', 0.05),
    TransProb('c', 'a', 0.25),
    TransProb('c', 'b', 0.25),
    TransProb('c', 'c', 0.5)
]

"""
Run a Markov chain with the given 'start' state for a given number of 'steps'.

Works by getting a random float between 0 and 1 for each step. If the
the probability of a given transition is less than the random float, it
subtracts that probability from the float. Example:

Float = 0.9, this transition's probability = 0.5 => Subtract
Float = 0.4, this transition's probability = 0.2 => Subtract
Float = 0.2, this transition's probability = 0.3 => Change state

This allows us to run the Markov chain in O(n)O(k) where 'n' is the number of
transitions and 'k' is the number of steps.
"""
def run_chain(start: str, steps: int = 1) -> dict[str, int]:
    state: str = start
    state_visits: dict[str, int] = {}

    for _ in range(steps):
        remaining_chance: float = random()

        for trans in TRANSITIONS:
            if trans.start_state == state:
                if trans.probability <= remaining_chance:
                    remaining_chance -= trans.probability
                else:
                    state = trans.end_state

                    if trans.end_state in state_visits:
                        state_visits[trans.end_state] += 1
                    else:
                        state_visits[trans.end_state] = 1

                    break

    return state_visits

if __name__ == '__main__':
    state_visits = run_chain('a', steps=5000)
    print(state_visits)
