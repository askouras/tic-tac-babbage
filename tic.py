import random

#  This didn't need to be a class, but this represents the tic-tac-toe board
#  in this game
class Board():
	#  Keep track of the states of each position on the board, where the
	#  string indexes translate into the "spaces" referred to later. 0 is
	#  the top left position, 1 the top center and 2 the top right, and so
	#  on from left to right
	state = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

	#  To check for wins/loses, and open spaces for blocks and wins, an 
	#  array of strings details the spaces of each row, each column, and 
	#  each diagonal on the board
	row_map = {
		'r1': [0,1,2],
		'r2': [3,4,5],
		'r3': [6,7,8],
		'c1': [0,3,6],
		'c2': [1,4,7],
		'c3': [2,5,8],
		'd1': [0,4,8],
		'd2': [2,4,6],
	}

	#  Print the board with a grid
	def print_board(self):
		print self.state[0] + '|' + self.state[1]  + '|' + self.state[2] 
		print '-+-+-'
		print self.state[3]  + '|' + self.state[4]  + '|' + self.state[5] 
		print '-+-+-'
		print self.state[6]  + '|' + self.state[7]  + '|' + self.state[8]

	#  Get the user input in the form of a row and a column, and translate
	#  it into a position on the board (see states above)
	def get_input(self):
		#  Append an r to the given row number, and a c to the given 
		#  given column number
		row = 'r' + raw_input('which row? ')
		col = 'c' + raw_input('which column? ')

		#  Take the row and column information given by the user, and 
		#  compare the corresponding elements in the row_map above
		space = set(self.row_map[row]) & set(self.row_map[col])	
		return int(space.pop())
		
	#  Take the user input, confirm the space is free, and, if the space
	#  is free, place an X in it
	def input_move(self):
		move_okay = False
		while not move_okay:
			space = self.get_input()
	
			#  If space is free, place an X there and exit while loop
			if self.state[space] != 'X' and self.state[space] != 'O':
				self.state[space] = 'X'
				move_okay = True
			else :
				# Move is invalid if the space isn't free
				print 'INVALID MOVE'

	#  Given a specific arrangement of X's or O's and empty spaces 
	#  (such as 'O O' or 'XX ' where spaces indicate empty spaces)
	#  append to a list of rows/columns/diagonals that match the 
	#  description (whose name reflects the variables of the the row_map)
	def check(self,what):
		matches = []
		sps = self.state
		if sps[0] + sps[1] + sps[2] == what:
			matches.append('r1')
		if sps[3] + sps[4] + sps[5] == what:
			matches.append('r2')
		if sps[6] + sps[7] + sps[8] == what:
			matches.append('r3')
		if sps[0] + sps[3] + sps[6] == what:
			matches.append('c1')
		if sps[1] + sps[4] + sps[7] == what:
			matches.append('c2')
		if sps[2] + sps[5] + sps[8] == what:
			matches.append('c3')
		if sps[0] + sps[4] + sps[8] == what:
			matches.append('d1')
		if sps[2] + sps[4] + sps[6] == what:
			matches.append('d2')
		return matches
	
	#  AI looks for a winning move, by searching for opportunites 
	#  in rows, columns, and diagonals that already have two O's
	#  pick the first possible winning move
	def find_win(self):
		space = -1
		winning_rows = self.check('OO ')
		if len(winning_rows):
			space = self.row_map[winning_rows[0]][2]
		else:
			winning_rows = self.check('O O')
			if len(winning_rows):
				space = self.row_map[winning_rows[0]][1]
			else:
				winning_rows = self.check(' OO')
				if len(winning_rows):
					space = self.row_map[winning_rows[0]][0]
		return space

	#  AI looks for a blocking move, by searching for opportunites 
	#  in rows, columns, and diagonals that already have two X's
	#  pick the first possible blocking move	
	def find_block(self):
		space = -1
		blocking_rows = self.check('XX ')
		if len(blocking_rows):
			space = self.row_map[blocking_rows[0]][2]
		else:
			blocking_rows = self.check('X X')
			if len(blocking_rows):
				space = self.row_map[blocking_rows[0]][1]
			else:
				blocking_rows = self.check(' XX')
				if len(blocking_rows):
					space = self.row_map[blocking_rows[0]][0]
		return space

	#  Finds the next available space with the highest number of 
	#  possible blocks. The AI is trying to tie at worst, and win at best
	def find_opportunity(self):
		spaces = []
		space_list = []
		opportunities = ['X  ',' X ','  X']
		option = 0
		#  For each found opportunity (a row with only one X, and two 
		#  free spaces), add each free space to a list of spaces
		while (option < len(opportunities)):
			opportunistic_rows = self.check(opportunities[option])
			if   opportunistic_rows is 'X  ':
				for row in opportunistic_rows:
					space_list.append(spaces[self.row_map[opportunistic_rows[row]][2]])
					space_list.append(spaces[self.row_map[opportunistic_rows[row]][1]])
			elif opportunistic_rows is ' X ':
				for row in opportunistic_rows:
					space_list.append(spaces[self.row_map[opportunistic_rows[row]][0]])
					space_list.append(spaces[self.row_map[opportunistic_rows[row]][2]])
			elif opportunistic_rows is '  X':
				for row in opportunistic_rows:
					space_list.append(spaces[self.row_map[opportunistic_rows[row]][0]])
					space_list.append(spaces[self.row_map[opportunistic_rows[row]][1]])
			option = option + 1
		#  Given that there are opportunistic spaces, count the 
		#  number of times each space occurs in the list of 
		#  opportunities, pick the space with the highest number
		#  of possible blocks
		if len(space_list):
			space_pos = 0
			while (space_pos < 9):
				spaces.append(space_list.count(space_pos))
				space = index(max(spaces))
		else:
			space = -1
		return space

	def find_cross(self):
		space = -1
#		if self.state[0] and self.state[2]
#
#		if self.state[0] and self.state[6]
#
		if self.state[0] is 'X' and self.state[8] is 'X':
			space = 3
		if self.state[2] is 'X' and self.state[6] is 'X':
			space = 5
#		if self.state[2] and self.state[8]
#	
#		if self.state[6] and self.state[8]
		return space
		
	#  AI makes decisions by first searching for winning moves, then
	#  blocking moves, and if neither are available, search for the most
	#  opportunistic (pre-emptive strategic blocking) move. 
	#  If there isn't a best pick, first look for corners, then edges
	def ai_move(self):
		space = self.find_win()
		if space > -1:
			self.state[space] = 'O'
		else:
			space = self.find_block()
			if space > -1:
				self.state[space] = 'O'
			else:
				if self.state[4] != 'X' and self.state[4] != 'O':
					self.state[4] = 'O'
				else: 
					space = self.find_cross()
					if space > -1:
						self.state[space] = 'O'
					else:
						space = self.find_opportunity()
						if space > -1:
							self.state[space] = 'O'
						#  Only hits else case in probable ties
						else:
							if  self.state[0] != 'X' and self.state[0] != 'O':
								self.state[0] = 'O'
							elif self.state[2] != 'X' and self.state[2] != 'O':
								self.state[2] = 'O'
							elif self.state[6] != 'X' and self.state[6] != 'O':
								self.state[6] = 'O'
							elif self.state[8] != 'X' and self.state[8] != 'O':
								self.state[8] = 'O'
							elif self.state[1] != 'X' and self.state[1] != 'O':
								self.state[1] = 'O'
							elif self.state[3] != 'X' and self.state[3] != 'O':
								self.state[3] = 'O'
							elif self.state[5] != 'X' and self.state[5] != 'O':
								self.state[5] = 'O'
							elif self.state[7] != 'X' and self.state[7] != 'O':
								self.state[7] = 'O'

	#  Stop the game and print a win if user wins or lose if BABBAGE wins
	#  or if the board is full
	def check_victory(self):
		is_full = True
		if   len(self.check('XXX')):
			result = 'WIN'
		elif len(self.check('OOO')):
			result = 'LOSE'
		else:
			for space in self.state:
				if space != 'X' and space != 'O': 
					is_full = False
					#  This will never be printed
					result = ' '
			if is_full:
				result = 'TIE'
		return is_full, result
	
	#  Print a greeting and the board. While play continues:
	#  Ask user to input their move, print the board, check for victory
	#  Ask AI to select a move, print the board, check for victory
	def play_game(self):
		who_plays = round(random.random())
		print "Your friendly Tic-Tac-Toe Artificial Intelligence, BABBAGE"
		self.print_board()
		game_over = False
		if who_plays == 0:
			while not game_over: 
				print "Your move"
				self.input_move()
				self.print_board()
				game_over,result = self.check_victory()
				if result == 'WIN':
					game_over = True
					break
				if game_over: break
				print "BABBAGE is deliberating..."
				self.ai_move()
				self.print_board()
				game_over,result = self.check_victory()
				if result == 'LOSE':
					game_over = True
					break
				if game_over: break
			print 'GAME OVER: ' + result
		else:
			while not game_over: 
				print "BABBAGE is deliberating..."
				self.ai_move()
				self.print_board()
				game_over,result = self.check_victory()
				if result == 'LOSE':
					game_over = True
					break
				if game_over: break
				print "Your move"
				self.input_move()
				self.print_board()
				game_over,result = self.check_victory()
				if result == 'WIN':
					game_over = True
					break
				if game_over: break
			print 'GAME OVER: ' + result

#  Initialise board
board = Board()
#  Start game when the file is opened
board.play_game()
	
