from lexical_analyzer import LexicalAnalyzer
transitions_csv_path = "transitions.csv"

lex = LexicalAnalyzer(transitions_csv_path)
x = lex.states["0"].transitions

print(x)