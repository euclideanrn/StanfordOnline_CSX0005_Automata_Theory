from typing import List

from paprika import data, to_string


@data
class State:
    is_final: bool = False
    name: str

    def __init__(self, name: str, is_final: bool = False):
        self.is_final = False if not is_final else True
        self.name = name


class DFA:
    def __init__(self, init_state: State):
        self.transitions = {}
        self.states = {}
        self.init_state = init_state
        self.current_state = init_state

    @staticmethod
    def __build_transition_key(from_state: State, symbol: str) -> str:
        return f'{from_state.name}_{symbol}'

    def add_transition(self, from_state: State, to_state: State, symbol: str) -> None:
        if not self.states.get(from_state.name):
            self.states.update({from_state.name: from_state})
        if not self.states.get(to_state.name):
            self.states.update({to_state.name: to_state})
        transition_key: str = self.__build_transition_key(from_state, symbol)
        if self.transitions.get(transition_key):
            raise DuplicatedTransitionError(
                f'Transition δ({from_state.name}, {symbol})->{self.transitions.get(transition_key).name} already exist.')
        self.transitions.update({f'{from_state.name}_{symbol}': to_state})

    def apply(self, string: str):
        for symbol in string:
            transition_key: str = self.__build_transition_key(self.current_state, symbol)
            target_state: State = self.transitions.get(transition_key)
            if not target_state:
                raise UndefinedTransitionError(f'No transition defined for symbol: {symbol}')
            self.current_state = target_state

    def is_final(self) -> bool:
        return self.current_state.is_final

    def is_acceptable(self, w: str):
        """
        :param w: a string over an alphabet ∑. Each element in the string is a symbol of ∑.
        :return: True if for the string w, δ(start, w) is in F.
        """
        self.apply(w)
        is_acceptable = self.is_final()
        self.reset()
        return is_acceptable

    def is_language(self, strings: List[str]):
        """
        :param strings: the set of strings
        :return: True if for every string w in the set of strings, δ(start, w) is in F.
        """
        for string in strings:
            if not self.is_acceptable(string):
                return False
        return True

    def reset(self):
        self.current_state = self.init_state


class UndefinedTransitionError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class DuplicatedTransitionError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)
