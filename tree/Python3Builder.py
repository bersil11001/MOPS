import sys
from antlr4 import *
from tree.Python3Lexer import Python3Lexer
from tree.Python3Parser import Python3Parser


class algTree:
    def __init__(self, ast = None):
        self.ast = ast
        self.childs = []
        self.data_type = ''
        self.data = ''
    
    def root(self, datapath):
        input_stream = FileStream(datapath)
        lexer = Python3Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        self.parser = Python3Parser(stream)
        self.ast = self.parser.file_input()
        self._build()
        
    def _build(self, rules = None):
        if not rules:
            rules = self.parser
        self.data = self.ast.getText()
        if self.ast.__class__.__name__ == 'TerminalNodeImpl':
            self.data_type = 'terminal'
            return
        else:
            self.data_type = rules.ruleNames[self.ast.getRuleIndex()] 
            for i in self.ast.children:
                child = algTree(i)
                child._build(rules)
                self.childs.append(child)
            return
    
    def visit(self):
        if self.data_type == 'terminal':
            if self.data == '\n':
                return
            print('\n', self.data)
            return
        else:
            print('(', end = "")
            print(self.data_type, end = "")
            for i in self.childs:
                i.visit()
            print(')', end = "")
            return
    
    def get_children(self):
        return self.childs
    
    def get_label(self):
        if self.data_type == 'terminal':
            return self.data
        else:
            return self.data_type
    
