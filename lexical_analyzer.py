from state import State
from csv import reader as csv_reader
from string import ascii_letters, digits, whitespace


class LexicalAnalyzer:
    reserved_words = set(("int", "float", "string", "for", "if", "else", "while", "return", "read", "write", "void"))

    def __init__(self, transitions_filename: str) -> None:
        self.load_transitions(transitions_filename)
        self.intial_state = self.states["0"]

    def _generate_transitions_for_state(self, state_transitions: list[str]):
        transitions: dict[str, str] = {}
        character_sets = {
            "letter": ascii_letters,
            "digit": digits,
            "whitespace": whitespace
        }

        for i, c in enumerate(state_transitions):
            if c:
                # 3 places offset caused by skipping state_id, state_name and is_accepting columns
                transition_character = self.transitions[i+3]

                if transition_character in character_sets:
                    for d in character_sets[transition_character]:
                        transitions[d] = c
                else:
                    transitions[transition_character] = c

        return transitions

    def load_transitions(self, filename: str):
        with open(filename, "r") as f:
            self.states: dict[str, State] = dict()
            reader = csv_reader(f)
            self.transitions = next(reader)

            for state in reader:
                state_id, state_name, is_accepting, *state_transitions = state

                self.states[state_id] = State(
                    id=state_id,
                    name=state_name,
                    is_accepting=is_accepting == "TRUE",
                    transitions=self._generate_transitions_for_state(state_transitions)
                )

    def analyze(self, prompt: str) -> list[str]:
        prompt = LexicalAnalyzer._add_newline_to_end_of_string_if_not_present(prompt)
        tokens = []
        current_state = self.intial_state
        l = ""

        for character in prompt:
            if current_state == self.intial_state and LexicalAnalyzer._is_space_delimiter(character):
                continue

            next_state = self.states.get(current_state.transitions.get(character))  # type: ignore

            if next_state and next_state.is_accepting:
                if LexicalAnalyzer._is_reserved_word(l):
                    pass
                # tokens.append(l)
                l = ""
                current_state = self.intial_state
            else:
                l += character
                current_state = next_state

        # Reaching end of file and comment wasn't closed
        if current_state != self.intial_state:
            tokens.append(["error"])

        return tokens

    def analyze_from_file(self, filename: str):
        with open(filename) as f:
            return self.analyze(f.read())

    @staticmethod
    def _is_space_delimiter(c: str):
        return c == "\n" or c == "\t" or c == " "

    @staticmethod
    def _is_reserved_word(s: str):
        return s.lower() in LexicalAnalyzer.reserved_words

    @staticmethod
    def _add_newline_to_end_of_string_if_not_present(s: str):
        if s and s[-1] != "\n":
            s += "\n"
        return s
