from antlr4 import *
from Repository.ast_to_networkx_graph import show_ast
from Repository.post_order_ast_traverser import PostOrderASTTraverser
from gen.SlrLexer import SlrLexer
from gen.SlrParser import SlrParser
from Code.SlrCodeGenerator import SlrCodeGenerator
from Code.SlrCustomListener import SlrCustomListener

class Argument:
	def __init__(self, _in, _out):
		self.input = _in
		self.output = _out

def main(argument):
	stream = FileStream(argument.input, encoding='utf8')
	lexer = SlrLexer(stream)
	token_stream = CommonTokenStream(lexer)
	parser = SlrParser(token_stream)
	parse_tree = parser.program()
	# ast
	ast_builder_listener = SlrCustomListener(parser.ruleNames)
	walker = ParseTreeWalker()
	walker.walk(t=parse_tree, listener=ast_builder_listener)
	ast = ast_builder_listener.ast
	show_ast(ast.root)
	# post order
	post_order_ast_traverser = PostOrderASTTraverser()
	post_order_ast_traverser.node_attributes = ['label', 'text', 'number']
	traversal = post_order_ast_traverser.traverse_ast(ast.root)
	# code generation
	dsl_config = ast_builder_listener.dsl_config
	code_generator = SlrCodeGenerator()
	generated_code = code_generator.generate_code(dsl_config)
	with open(argument.output, 'w',encoding='utf-8') as output_file:
		output_file.write(generated_code)

if __name__ == '__main__':
	for i in range(1, 11):
		arg = Argument(f"tests/in/{i}.slr", f"tests/out/{i}.py")
		main(arg)
