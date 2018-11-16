from nltk import CFG, ChartParser

cfg = CFG.fromstring("""\
S -> NP VP | CONJ S S | ADV VP VP | NP VP S
NP -> ProperNoun | Noun | ADJ NP | NP CONJ NP | DET NP | Noun PP
ProperNoun -> 'Homer' | 'Bart' | 'Lisa'
Noun -> 'milk' | 'shoes' | 'salad' | 'midnight' | 'table' | 'kitchen'
ADJ -> 'blue' | 'healthy' | 'green'
CONJ -> 'and' | 'when'
DET ->  'a' | 'the'

VP -> Verb | ADV VP | Verb NP | Verb NP NP
Verb -> 'laughs' | 'runs' | 'laughed' | 'serves' | 'wears' | 'drinks' | 'drink' | 'thinks' | 'serves' | 'do' | 'does' | 'wear'
ADV -> 'always' | 'when' | 'never'

PP -> PREP NP
PREP -> 'on' | 'in' | 'before'
""")
cfparser = ChartParser(cfg)
text = """\
Bart laughs
Homer laughed
Bart and Lisa drink milk
Bart wears blue shoes
Lisa serves Bart a healthy green salad
Homer serves Lisa
Bart always drinks milk
Lisa thinks Homer thinks Bart drinks milk
Homer never drinks milk in the kitchen before midnight
when Homer drinks milk Bart laughs
when does Lisa drink the milk on the table
when do Lisa and Bart wear shoes
"""
sents = text.splitlines()
for sent in sents:
    parses = cfparser.parse(sent.split())
    print('\n\n')
    print(sent)
    for tree in parses:
        print(tree)
