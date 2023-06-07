class State:
    def __init__(self, id: str, name: str, transitions: dict[str, str], is_accepting: bool) -> None:
        self.id = id
        self.name = name
        self.transitions = transitions
        self.is_accepting = is_accepting
