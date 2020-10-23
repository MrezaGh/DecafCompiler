from lark import Lark, Token, Tree, common
import lark

# TODO:
#     1. Add the keys needed for scanner using Docs
#     2. add regex for distinguishing tokens
grammar = r"""
start: (T_BOOLEANLITERAL | T_KEYWORD | T_ID | T_INTLITERAL | T_DOUBLELITERAL | T_STRINGLITERAL | T_COMMENT | T_OPR) start |
T_BOOLEANLITERAL: "true" | "false"
T_KEYWORD: "void" | "int" | "bool" | "string" | "class" | "interface" | "null" | "this" | "extends" | "implements" | "for" | "while" | "if" | "else" | "return" | "break" | "continue" | "new" | "NewArray" | "Print" | "ReadInteger" | "ReadLine" | "dtoi" | "itod" | "btoi" | "itob" | "private" | "protected" | "public"
T_ID: CNAME
T_INTLITERAL: /0[xX][0-9a-fA-F]+/ | /[0-9]+/
T_DOUBLELITERAL:  /[0-9]*[\.][0-9]+[eE][+][0-9]+/ | /[0-9]+\.[0-9]*/
T_STRINGLITERAL: /"(?:[^\\"]|\\.)*"/
T_COMMENT: /\/\/.*/
T_OPR: /[<>!=]=/ | /[+*-=()%<>;:!,]/ | "&&" |"||" | "]" | "[" | "." | "/"
%import common.CNAME
%import common.WORD   // imports from terminal library
%import common.WS
%ignore WS

"""

code = """
Hello, World!
"""
code = """
void
int
double
bool
string
class
interface
null
this
extends
implements
for
while
if
else
return
break
new
NewArray
Print
ReadInteger
ReadLine
"""


def scan(code: str):
    parser = Lark(grammar=grammar, parser="lalr", transformer=None, debug=True)
    tree = parser.parse(code)
    tokens = pretty_print(tree)
    return tokens


# TODO: build the needed output format that matches project desc
def pretty_print(tree: lark.Tree):
    """use the calculated tree to output in Decaf format"""
    # can use tree.children.type for finding types
    # TODO: implement...
    tokens = []
    for token in tree.children:
        if type(token) == lark.tree.Tree:
            # pretty_print(token)
            tokens.extend(pretty_print(token))
        else:
            if token.type == "T_OPR" or token.type == "T_KEYWORD":
                # print(token)
                tokens.append(str(token))
            else:
                # print(token.type, token)
                tokens.append(str(token.type) + " " + str(token))
    return tokens


# TODO: other TODOS
#     1. handle Exceptions when UNAUTHORIZED token is given
#     2. integrate tests


if __name__ == '__main__':
    tokens = scan(code)
    print("\n".join(tokens))
