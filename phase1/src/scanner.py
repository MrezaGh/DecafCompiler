from lark import Lark, Token, Tree, common
import lark

# TODO:
#     1. Add the keys needed for scanner using Docs
#     2. add regex for distinguishing tokens
grammar = r"""
start: (T_BOOLEANLITERAL | T_KEYWORD | T_ID | T_INTLITERAL | T_DOUBLELITERAL | T_STRINGLITERAL | T_COMMENT | T_OPR | T_OTHERS | UNDEFINED_TOKEN ) start |
T_SPEC_ID.3: (T_KEYWORD /[0-9]+/)| T_BOOLEANLITERAL /[0-9]+/
T_BOOLEANLITERAL.2: ("true" | "false")
T_KEYWORD.2: ("void" | "interface" | "int" | "double" | "bool" | "string" | "class" | "null" | "this" | "extends" | "implements" | "for" | "while" | "if" | "else" | "return" | "break" | "continue" | "new" | "NewArray" | "Print" | "ReadInteger" | "ReadLine" | "dtoi" | "itod" | "btoi" | "itob" | "private" | "protected" | "public")
T_ID: CNAME | T_SPEC_ID
T_INTLITERAL.2: /0[xX][0-9a-fA-F]+/ | /[0-9]+/
T_DOUBLELITERAL.2:  /[0-9]+[\.][0-9]*[eE][+ | -]?[0-9]+/ | /[0-9]+\.[0-9]*/
T_STRINGLITERAL: /"(?:[^\\"]|\\.)*"/
T_COMMENT: /\/\/.*/
T_OPR: /[<>!=]=/ | /[+*-=()%<>;:!,]/ | "||" | "]" | "[" | "." | "/" | "&&"
T_OTHERS: "(" | ")" | "{" | "}"
UNDEFINED_TOKEN: (T_INTLITERAL CNAME) | (T_DOUBLELITERAL CNAME)
%import common.WORD   // imports from terminal library
%import common.CNAME
%import common.WS
%ignore WS
"""

code = """
Hello, World!
"""
code = """
int inta aint ainta int2 2int 2inta 2aint
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
            if token.type == "T_OPR" or token.type == "T_KEYWORD" or token.type == "T_OTHERS":
                # print(token)
                tokens.append(str(token))
            elif token.type == "T_COMMENT":
                pass
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
