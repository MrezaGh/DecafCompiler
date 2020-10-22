from lark import Lark, Token, Tree, common

# TODO:
#     1. Add the keys needed for scanner using Docs
#     2. add regex for distinguishing tokens
grammar = r"""
start: WORD "," WORD "!"

%import common.WORD   // imports from terminal library
%import common.WS
%ignore WS

"""

code = """
Hello, World!
"""


def main():
    parser = Lark(grammar=grammar, parser="lalr", transformer=None, debug=True)
    tree = parser.parse(code)
    pretty_print(tree)


# TODO: build the needed output format that matches project desc
def pretty_print(tree: Tree):
    """use the calculated tree to output in Decaf format"""
    # can use tree.children.type for finding types
    # TODO: implement...
    for token in tree.children:
        # print(token.type, token)
        print(token)


# TODO: other TODOS
#     1. handle Exceptions when UNAUTHORIZED token is given
#     2. integrate tests


if __name__ == '__main__':
    main()
