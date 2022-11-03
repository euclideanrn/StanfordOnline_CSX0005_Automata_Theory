import unittest
from enum import Enum

from week1.DFA import DFA, State


class DivisibleBy2TestCase(unittest.TestCase):
    class States(Enum):
        start = State(name='Start')
        q0 = State(name='q0', is_final=True)
        q1 = State(name='q1')

    def __init__(self, *args, **kwargs):
        super(DivisibleBy2TestCase, self).__init__(*args, **kwargs)
        self.dfa: DFA = DFA(self.States.start.value)
        self.dfa.add_transition(self.States.start.value, self.States.q0.value, '0')
        self.dfa.add_transition(self.States.start.value, self.States.q1.value, '1')
        self.dfa.add_transition(self.States.q0.value, self.States.q0.value, '0')
        self.dfa.add_transition(self.States.q0.value, self.States.q1.value, '1')
        self.dfa.add_transition(self.States.q1.value, self.States.q0.value, '0')
        self.dfa.add_transition(self.States.q1.value, self.States.q1.value, '1')

    def test_dfa(self):
        self.assertTrue(self.dfa.is_acceptable(bin(14).replace('0b', '')))
        self.assertFalse(self.dfa.is_acceptable(bin(15).replace('0b', '')))

    def test_states(self):
        self.assertEqual(self.States.start.value, State(name='Start'))


class DivisibleBy5TestCase(unittest.TestCase):
    class States(Enum):
        start = State(name='Start')
        q0 = State(name='q0', is_final=True)
        q1 = State(name='q1')
        q2 = State(name='q2')
        q3 = State(name='q3')
        q4 = State(name='q4')

    def __init__(self, *args, **kwargs):
        super(DivisibleBy5TestCase, self).__init__(*args, **kwargs)
        self.dfa: DFA = DFA(self.States.start.value)
        self.dfa.add_transition(self.States.start.value, self.States.q0.value, '0')
        # todo 1

    def test_dfa(self):
        # todo 2
        pass


if __name__ == '__main__':
    unittest.main()
