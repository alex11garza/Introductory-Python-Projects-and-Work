#  File: ExpressionTree.py
#  Student Name: Alex Garza
#  Student UT EID: ang3489

import sys

# list of valid operators
operators = ['+', '-', '*', '/', '//', '%', '**']


# Input: Elements of a simple expression
#        operator (String) and two operands (numbers)
# Output: result of evaluation of the expression
def operation(operator, n, m):
    expression = str(n) + operator + str(m)
    return eval(expression)


# Stack Class - DO NOT CHANGE
# Traditional Stack implementation containing list of data items
# Used to keep track of items in nested expressions.
class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


# Node Class
# Purpose: Used by the Tree Class to represent one operand or operators
#          in a binary expression. It includes data (a character) and
#          two pointers, to the left and right child nodes.
# You do not need to make changes to this class.
class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


# Tree Class
# Purpose: To represent the string representation of operators and operands
#          of a binary expression so it can be evaluated.
# You need to make a lot f changes to this class!
class Tree (object):
    def __init__(self):
        self.root = Node(None)

    # Input: a string expression
    # Output: an expression tree
    def create_tree(self, expr):
        pass
        '''##### ADD CODE HERE #####'''
        stack = Stack()
        expr = expr.split()

        for token in expr:
            if token == '(':
                continue
            elif token == ')':
                right_node = stack.pop()
                operator_node = stack.pop()
                left_node = stack.pop()
                operator_node.lChild = left_node
                operator_node.rChild = right_node
                stack.push(operator_node)
            elif token in operators:
                node = Node(token)
                stack.push(node)
            else:
                operand = float(token) if '.' in token else int(token)
                node = Node(operand)
                stack.push(node)

        self.root = stack.pop()


    # Input: A node in an expression tree
    # Output: The result of evaluating the expression
    #         with this node as the root
    def evaluate(self, current):
        pass
        '''##### ADD CODE HERE #####'''
        if current.lChild is None and current.rChild is None:
            return current.data

        left_result = self.evaluate(current.lChild)
        right_result = self.evaluate(current.rChild)

        if type(left_result) == float or type(right_result) == float:
            return float(operation(current.data, left_result, right_result))
        else:
            return float(operation(current.data, left_result, right_result))

    # Starter Method for pre_order
    # Input: a node in an expression tree
    # Output: (string) the preorder notation of the expression
    #                  with this node a the root
    def pre_order(self, current):
        pass
        '''##### ADD CODE HERE #####'''
        if current is None:
            return ''

        result = str(current.data) + ' '

        if current.lChild is not None:
            result += self.pre_order(current.lChild)

        if current.rChild is not None:
            result += self.pre_order(current.rChild)

        return result
    # Starter Method for post_order
    # Input: a node in an expression tree
    # Output: (string) the post order notation of the expression
    #                  with this node a the root
    def post_order(self, current):
        pass
        '''##### ADD CODE HERE #####'''
        if current is None:
            return ''

        result = ''

        if current.lChild is not None:
            result += self.post_order(current.lChild)

        if current.rChild is not None:
            result += self.post_order(current.rChild)

        result += str(current.data) + ' '

        return result


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

   # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('expression.in')
    else:
        in_data = sys.stdin

    # read infix expression
    line = in_data.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
