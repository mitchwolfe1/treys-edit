from treys import Card
from treys import Evaluator

board = [
	Card.new('As'),
	Card.new('Kd'),
	Card.new('Jh')
]

hand = [
	Card.new('Qc'),
	Card.new('Th')
]

Card.print_pretty_cards(board + hand)

evaluator = Evaluator()
print(evaluator.evaluate(board, hand))
