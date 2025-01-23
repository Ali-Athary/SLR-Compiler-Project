from antlr4 import *
import argparse
from Repository.ast_to_networkx_graph import show_ast
from Repository.post_order_ast_traverser import PostOrderASTTraverser
from gen.SlrLexer import SlrLexer
from gen.SlrParser import SlrParser
from Code.SlrCodeGenerator import SlrCodeGenerator
from Code.SlrCustomListener import SlrCustomListener


def main(arguments):
	stream = FileStream(arguments.input, encoding='utf8')
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
	code_generator = SlrCodeGenerator()
	generated_code = code_generator.generate_code(traversal)
	with open(arguments.output, 'w') as output_file:
		output_file.write(generated_code)


if __name__ == '__main__':
	argparser = argparse.ArgumentParser()
	argparser.add_argument('-i', '--input', help='Input source', default=r'test.slr')
	argparser.add_argument('-o', '--output', help='Output path', default=r'test_output.py')
	args = argparser.parse_args()
	main(args)
