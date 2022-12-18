class LWRCHAR:
    def __init__(self):
        self.expected = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']


class NUMBERCHAR:
    def __init__(self):
        self.expected = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


class PRFASOC:
    def __init__(self):
        self.expected = ['fx', 'fy']


class POFASOC:
    def __init__(self):
        self.expected = ['xf', 'yf']


class LEFASOC:
    def __init__(self):
        self.expected = ['yfx']


class INFASOC:
    def __init__(self):
        self.expected = ['xfx', 'yfy']


class RIFASOC:
    def __init__(self):
        self.expected = ['xfy']


class ARIOP:
    def __init__(self):
        self.expected = ['+', '-', '*', '/', 'mod', '^']


class RELOP:
    def __init__(self):
        self.expected = ['=', '\=', '<', '=<', '>', '>=', '=:=', '=\=', '==', '\==']


class SPECIALCHAR:
    def __init__(self):
        self.expected = ['@', '#', '$', '&', '=', '-', '+', '*', '/']


class UPRCHAR:
    def __init__(self):
        self.expected = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class ALPHACHAR:
    def __init__(self):
        self.expected = [LWRCHAR(), UPRCHAR()]


class NONSPECIALCHAR:
    def __init__(self):
        self.expected = [ALPHACHAR(), NUMBERCHAR(), '_']


class NONSPECIALCHARS:
    def __init__(self):
        self.expected = [[NONSPECIALCHAR(), NONSPECIALCHARS()], NONSPECIALCHAR()]


class SPECIALCHARS:
    def __init__(self):
        self.expected = [[SPECIALCHAR(), SPECIALCHARS()], SPECIALCHAR()]


class CHAR:
    def __init__(self):
        self.expected = [ALPHACHAR(), NUMBERCHAR(), SPECIALCHAR(), '_']


class CHARS:
    def __init__(self):
        self.expected = [[CHAR(), CHARS()], CHAR()]


class ATOM:
    def __init__(self):
        self.expected = [LWRCHAR(), [LWRCHAR(), NONSPECIALCHARS()], SPECIALCHARS(), ['\'', CHARS(), '\'']]


class OPNAME:
    def __init__(self):
        self.expected = [ATOM()]


class FUNCTOR:
    def __init__(self):
        self.expected = [ATOM(), '.']


class IDENTIFIER:
    def __init__(self):
        self.expected = [ATOM()]


class DIGIT:
    def __init__(self):
        self.expected = [NUMBERCHAR()]


class INTEGER:
    def __init__(self):
        self.expected = [[DIGIT(), INTEGER()], DIGIT()]


class TERM:
    def __init__(self):
        self.expected = [ATOM(), INTEGER(), IDENTIFIER(), STRUCTURE(), LIST()]


class ARGUMENT:
    def __init__(self):
        self.expected = [TERM()]


class ARGUMENTS:
    def __init__(self):
        self.expected = [[ARGUMENT(), ',', ARGUMENTS()], ARGUMENT()]


class STRUCTURE:
    def __init__(self):
        self.expected = [[FUNCTOR(), '(', ARGUMENTS(), ')'], STRUCTWITHOP(), LIST()]


class STRUCTWITHOP:
    def __init__(self):
        self.expected = [[PRFOP(), TERM()], [TERM(), POFOP()], [TERM(), INFOP(), TERM()]]


class PRFOP:
    def __init__(self):
        self.expected = ['?-', 'not', ':-', ATOM()]


class POFOP:
    def __init__(self):
        self.expected = [ATOM()]


class INFOP:
    def __init__(self):
        self.expected = [':-', ARIOP(), ';', ',', RELOP(), 'is', '=..', '.']


class LIST:
    def __init__(self):
        self.expected = ['[]', EASYLIST(), DIVIDEDLIST(), [TERM(), '.', LIST()]]


class EASYLIST:
    def __init__(self):
        self.expected = [['[', TERMS(), ']']]


class TERMS:
    def __init__(self):
        self.expected = [[TERM(), ',', TERMS()], TERM()]


class DIVIDEDLIST:
    def __init__(self):
        self.expected = [['[', TERMS()], [TERMS(), ']']]


class STRUCTURE:
    def __init__(self):
        self.expected = [[FUNCTOR(), '(', ARGUMENTS(), ')'], STRUCTWITHOP(), LIST()]


class PRIORITY:
    def __init__(self):
        self.expected = [INTEGER()]


class ALTERNATIVES:
    def __init__(self):
        self.expected = [[HEAD(), ';', ALTERNATIVES()], ALTERNATIVE()]


class HEAD:
    def __init__(self):
        self.expected = [ATOM(), STRUCTURE()]


class ALTERNATIVE:
    def __init__(self):
        self.expected = [[HEAD(), ';']]


class ALTERNATIVEBODY:
    def __init__(self):
        self.expected = [ALTERNATIVES()]


class QUERYBODY:
    def __init__(self):
        self.expected = [ALTERNATIVES()]


class RULEBODY:
    def __init__(self):
        self.expected = [[STRUCTURE(), ','], [STRUCTURE(), '.']]


class RULE:
    def __init__(self):
        self.expected = [[HEAD(), ':-', RULEBODY()]]


class FACT:
    def __init__(self):
        self.expected = [HEAD()]


class OPDECL:
    def __init__(self):
        self.expected = [[':-op', '(', PRIORITY()], ASOCIATIVITY(), [OPNAME(), ')']]


class ASOCIATIVITY:
    def __init__(self):
        self.expected = [PRFASOC(), POFASOC(), INFASOC(), LEFASOC(), RIFASOC()]


class QUERY:
    def __init__(self):
        self.expected = [['?-', QUERYBODY()]]


class CLAUSE:
    def __init__(self):
        self.expected = [FACT(), RULE()]


class COMMAND:
    def __init__(self):
        self.expected = [[CLAUSE(), '.'], [QUERY(), '.'], [OPDECL(), '.']]


class PROGRAM:
    def __init__(self):
        self.expected = [[COMMAND(), PROGRAM()], COMMAND()]
