from __future__ import print_function
from nltk.grammar import FeatureGrammar
from nltk import FeatureChartParser


ugrammar = FeatureGrammar.fromstring("""\
S -> NP[NUM=?n] VP[SUBCAT=nil,Form=?n] | NP[NUM=?n] V_specialP[SUBCAT=nil,Form=?n] | Multi_ProperNoun[NUM=plural] VP[SUBCAT=nil,Form=plural] | Wh_conj S S | Wh_adv AUX[NUM=?n] QS[NUM=?n]
QS[NUM=?n] -> NP[NUM=?n] VP[SUBCAT=nil,Form=base] | Multi_ProperNoun[NUM=plural] VP[SUBCAT=nil,Form=base]

AUX[NUM=third_singular_present]-> 'does'
AUX[NUM=plural]-> 'do'

NP[NUM=?n] -> DET Nominal[NUM=?n] | Nominal[NUM=?n]
Nominal[NUM=?n] -> ProperNoun[NUM=?n] | Noun[NUM=?n] | Nominal[NUM=?n] PP | ADJ Nominal[NUM=?n]
Multi_ProperNoun[NUM=plural] -> Nominal[NUM=?n] CONJ Nominal[NUM=?n]

ProperNoun[NUM=third_singular_present] -> 'Homer' | 'Bart' | 'Lisa'
ProperNoun[NUM=third_singular_past] -> 'Homer' | 'Bart' | 'Lisa'
Noun[NUM=singular] -> 'milk' | 'salad' | 'midnight' | 'table' | 'kitchen' | 'bread'
Noun[NUM=plural] -> 'shoes'

ADJ -> 'blue' | 'healthy' | 'green'
CONJ -> 'and'
Wh_conj -> 'when'
Wh_adv -> 'when' | 'what' | 'whom'
DET ->  'a' | 'the'

VP[SUBCAT=?rest,Form=?n] -> VP[SUBCAT=[HEAD=?arg, TAIL=?rest],Form=?n] ARG[CAT=?arg]
VP[SUBCAT=?rest,Form=?n] -> ADV VP[SUBCAT=[HEAD=?arg, TAIL=?rest], Form=?n] ARG[CAT=?arg]
VP[SUBCAT=?args,Form=?n] -> V[SUBCAT=?args,Form=?n]

V_specialP[SUBCAT=?rest,Form=?n] -> V_specialP[SUBCAT=[HEAD=?arg, TAIL=?rest],Form=?n] ARG[CAT=?arg]
V_specialP[SUBCAT=?args,Form=?n] -> V_special[SUBCAT=?args,Form=?n]

PP -> PREP NP
PREP -> 'on' | 'in' | 'before'

ARG[CAT=NP] -> NP
ARG[CAT=PP] -> PP
ARG[CAT=S] -> S

ADV -> 'always' | 'when' | 'never'

V[SUBCAT=nil, Form=third_singular_present] -> 'laughs'
V[SUBCAT=[HEAD=NP, TAIL=nil], Form=third_singular_present] -> 'drinks' | 'serves' | 'wears'
V[SUBCAT=[HEAD=S, TAIL=nil],Form=third_singular_present] -> 'thinks'
V[SUBCAT=[HEAD=NP, TAIL=[HEAD=NP, TAIL=nil]],Form=third_singular_present] -> 'serves'

V_special[SUBCAT=[HEAD=V_ingP, TAIL=[HEAD=NP, TAIL=nil]],Form=third_singular_present] -> 'likes'

V_ing -> 'drinking'


V[SUBCAT=nil, Form=third_singular_past] -> 'laughed'

V[SUBCAT=nil, Form=plural ] -> 'laugh'|'laughed'|'drink' | 'serve' | 'wear'
V[SUBCAT=[HEAD=NP, TAIL=nil], Form=plural] -> 'drink' | 'serve' | 'wear'
V[SUBCAT=[HEAD=S, TAIL=nil],Form=plural] -> 'think'|'laughed'|'drink' | 'serve' | 'wear'
V[SUBCAT=[HEAD=NP, TAIL=[HEAD=NP, TAIL=nil]],Form=plural] -> 'serve'

V[SUBCAT=nil, Form=base ] -> 'laugh'|'drink' | 'serve' | 'wear'
V[SUBCAT=[HEAD=NP, TAIL=nil], Form=base] -> 'drink' | 'serve' | 'wear'
V[SUBCAT=[HEAD=S, TAIL=nil],Form=base] -> 'think'
V[SUBCAT=[HEAD=NP, TAIL=[HEAD=NP, TAIL=nil]],Form=base] -> 'serve'
""")
uparser = FeatureChartParser(ugrammar)
text = """\
Bart laugh
when do Homer drinks milk
Bart laughs the kitchen

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

what does Homer drink
whom does Homer serve salad
whom do Homer and Lisa serve
Bart likes drinking milk
"""
sents = text.splitlines()
for sent in sents:
    parses = uparser.parse(sent.split())
    print(sent)
    for tree in parses:
        print(tree,end='\n\n\n')
