import sys
import random
import signal
import time
import copy
import traceback

class Team26():
	
	def __init__(self):
		self.infi = 10000000000000
		self.start = 0
		self.endflag = 0
		pass

	def change_flag(self, flag):
		if flag == 'x':
			flag = 'o'
		else:
			flag = 'x'
		return flag

	def dashcounter(self,board):
		ret=0
		for i in board.small_boards_status:
			for j in i:
				for k in j:
					if k == '-':
						ret+=1
		return ret

	def smallboardeval(self,board,i,j,k,mainflag, dpl):
		ret=0
		tmp=[]
		for x in range(i,i+3):
			z=[]
			for y in range(j,j+3):
				z.append(board.big_boards_status[k][x][y])
			tmp.append(z)
		tmp1=[]
		for x in range(0,3):
			z=[]
			for y in range(0,3):
				z.append(tmp[y][x])
			tmp1.append(z)		
		
		lis=[]
		lis.append([tmp[0][0],tmp[1][1],tmp[2][2]])	
		lis.append([tmp[2][0],tmp[1][1],tmp[0][2]])

		for j in tmp:
			j.sort()
			j=''.join(j)
			if j == '-xx' and mainflag == 'x':
				ret += 4
			elif j == '-oo' and mainflag == 'x':
				ret -= 5		
			elif j == '-xx' and mainflag == 'o':
				ret += 5
			elif j == '-oo' and mainflag == 'o':
				ret -= 4
			
			elif j == 'oox':
				ret += 13
			elif j == 'oxx':
				ret -= 13
			elif j == 'xxx':
				ret += 60
			elif j == 'ooo':
				ret -= 60
			# elif j == '--x':
			# 	ret += 1.1
			# elif j == '--o':
			# 	ret -= 1.1
			elif j == '-ox' and mainflag == 'x':
				ret += 1
			elif j == '-ox' and mainflag == 'o':
				ret -= 1		

		for j in tmp1:
			j.sort()
			j=''.join(j)

			if j == '-xx' and mainflag == 'x':
				ret += 4
			elif j == '-oo' and mainflag == 'x':
				ret -= 5
			elif j == '-oo' and mainflag == 'o':
				ret -= 4
			elif j == '-xx' and mainflag == 'o':
				ret += 5
			
			elif j == 'oox':
				ret += 13
			elif j == 'oxx':
				ret -= 13
			elif j == 'xxx':
				ret += 60
			elif j == 'ooo':
				ret -= 60
			# elif j == '--x':
			# 	ret += 1.1
			# elif j == '--o':
			# 	ret -= 1.1
			elif j == '-ox' and mainflag == 'x':
				ret += 1
			elif j == '-ox' and mainflag == 'o':
				ret -= 1		

		# print(lis)
		for j in lis:			
			j.sort()
			j=''.join(j)
			
			if j == '-xx' and mainflag == 'x':
				ret += 6
			elif j == '-oo' and mainflag == 'x':
				ret -= 7
			elif j == '-oo' and mainflag == 'o':
				ret -= 6
			elif j == '-xx' and mainflag == 'o':
				ret += 7
			
			elif j == 'oox':
				ret += 19
			elif j == 'oxx':
				ret -= 19
			elif j == 'xxx':
				ret += 70
			elif j == 'ooo':
				ret -= 70
			# elif j == '--x':
			# 	ret += 2.1
			# elif j == '--o':
			# 	ret -= 2.1
			elif j == '-ox' and mainflag == 'x':
				ret += 2
			elif j == '-ox' and mainflag == 'o':
				ret -= 2 		

		return ret		

	#takes into account the score associated with each smallboard win	
	def smallboardscore(self, board, mainflag, dpl):
		
		ret = 0
		tmp = copy.deepcopy(board.small_boards_status)
		tmp1=[]

		for i in tmp:
			tp=[]
			for x in range(0,3):
				z=[]
				for y in range(0,3):
					z.append(i[y][x])
				tp.append(z)
			tmp1.append(tp)				

		
		lis=[]
		lis.append([tmp[0][0][0],tmp[0][1][1],tmp[0][2][2]])	
		lis.append([tmp[1][0][0],tmp[1][1][1],tmp[1][2][2]])
		lis.append([tmp[0][2][0],tmp[0][1][1],tmp[0][0][2]])	
		lis.append([tmp[1][2][0],tmp[1][1][1],tmp[1][0][2]])	

		#checking for v-patterns in smallboard
		for i in tmp:
			for j in i:
				j.sort()
				j=''.join(j)

				if j == '-xx' and mainflag == 'x':
					ret += 3000
				elif j == '-oo' and mainflag == 'x':
					ret -= 15000
				elif j == '-oo' and mainflag == 'o':
					ret -= 3000
				elif j == '-xx' and mainflag == 'o':
					ret += 15000	
				elif j == 'oox':
					ret += 9400
				elif j == 'oxx':
					ret -= 9400
				elif j == 'xxx':
					ret += 400000
				elif j == 'ooo':
					ret -= 400000
				elif j == '--x':
					ret += 600
				elif j == '--o':
					ret -= 600
				elif j == 'doo' :
					ret += 9100
				elif j == 'dxx' :
					ret -= 9100
				elif j == 'ddx' :
					ret += 400
				elif j == 'ddo' :
					ret -= 400	
				elif j == '-ox' and mainflag == 'x':
					ret += 100
				elif j == '-ox' and mainflag == 'o':
					ret -= 100

		for i in tmp1:
			for j in i:
				j.sort()
				j=''.join(j)

				if j == '-xx' and mainflag == 'x':
					ret += 3000
				elif j == '-oo' and mainflag == 'x':
					ret -= 15000
				elif j == '-oo' and mainflag == 'o':
					ret -= 3000
				elif j == '-xx' and mainflag == 'o':
					ret += 15000
				elif j == 'oox':
					ret += 9400
				elif j == 'oxx':
					ret -= 9400
				elif j == 'xxx':
					ret += 400000
				elif j == 'ooo':
					ret -= 400000
				elif j == '--x':
					ret += 600
				elif j == '--o':
					ret -= 600
				elif j == 'doo':
					ret += 9100
				elif j == 'dxx':
					ret -= 9100
				elif j == 'ddx':
					ret += 400
				elif j == 'ddo':
					ret -= 400
				elif j == '-ox' and mainflag == 'x':
					ret += 100
				elif j == '-ox' and mainflag == 'o':
					ret -= 100

		for j in lis:
			j.sort()
			j=''.join(j)

			if j == '-xx' and mainflag == 'x':
				ret += 3100
			elif j == '-oo' and mainflag == 'x':
				ret -= 21000
			elif j == '-oo' and mainflag == 'o':
				ret -= 3100
			elif j == '-xx' and mainflag == 'o':
				ret += 21000
			elif j == 'oox':
				ret += 11200
			elif j == 'oxx':
				ret -= 11200
			elif j == 'xxx':
				ret += 400000
			elif j == 'ooo':
				ret -= 400000
			elif j == '--x':
				ret += 800
			elif j == '--o':
				ret -= 800
			elif j == 'doo':
				ret += 11000
			elif j == 'dxx':
				ret -= 11000
			elif j == 'ddx':
				ret += 600
			elif j == 'ddo':
				ret -= 600
			elif j == '-ox' and mainflag == 'x':
				ret += 200
			elif j == '-ox' and mainflag == 'o':
				ret -= 200
		##now start the part of individual small boards
		for k in range(0,2):
			for i in range(0,9,3):
				for j in range(0,9,3):
					temp = self.smallboardeval(board,i,j,k,mainflag,dpl)
					ret += temp
		return ret							

	def big_win_loss_check(self, board, mainflag):	
		ret = 0
		status = board.find_terminal_state()
		if status[0] == mainflag and status[1] == 'WON':
			ret = 1
		elif status[0] != mainflag and status[1] == 'WON':
			ret = -1
		return ret

	def heuristic(self, mainflag, board, dpl):
		
		heuristic_val = 0
		
		small_val = self.smallboardscore(board, mainflag, dpl)
		# print(small_val)
		heuristic_val += small_val
		large_val = self.big_win_loss_check(board,mainflag) * self.infi
		if large_val != 0:
			return [large_val, 1]			
		return [heuristic_val, 0]

	def minmax_recur(self, board, move, mainflag, flag, depth, alpha, beta, dpl, allow):

		if self.endflag == 1 or time.time() - self.start > 6:
			self.endflag = 1
			val = self.heuristic(mainflag, board, dpl)
			return val[0]

		if depth >= dpl:
			val = 0
			val = self.heuristic(mainflag, board, dpl)
			return val[0]
		
		cells = board.find_valid_move_cells(move);

		mx = -10000000000000 
		mn = 10000000000000
		
		if len(cells) == 0:
			if mainflag == 'x':
				return mx
			else:
				return mn

		best1 = []		
		best2 = []		
		best1.append(cells[0])
		best2.append(cells[0])

		for cell in cells:
			temp_small_boards_status = copy.deepcopy(board.small_boards_status)
			
			dash_count = copy.deepcopy(self.dashcounter(board))
			board.update(move, cell, flag)
			tmpflag = flag
			
			if dash_count != self.dashcounter(board) and allow == 0:
				tmpflag = self.change_flag(flag)
				allow = 1
			elif allow == 1:
				allow = 0

			check = self.heuristic(mainflag, board, dpl)
			
			ret = 0
			if check[1] == 1:
				ret = check[0]
			else:
				ret = self.minmax_recur(board, cell, mainflag, self.change_flag(tmpflag), depth + 1, alpha, beta, dpl, allow)
			
			if flag == 'x':
				if mx < ret:
					best1 = []
					best1.append(cell)
					mx = ret
				if alpha <= mx:
					alpha = mx
				if mx == ret:
					best1.append(cell)
			else:
				if mn > ret:
					best2 = []
					best2.append(cell)
					mn = ret
				if beta >= mn:
					beta = mn
				if mn == ret:
					best2.append(cell)
			board.small_boards_status = temp_small_boards_status
			board.big_boards_status[cell[0]][cell[1]][cell[2]] = '-'
			if beta <= alpha or self.endflag == 1:
				break

		if depth == 0:
			if flag == 'x':
				return [best1[0],mx]
			else:
				return [best2[0],mn]
		else:
			if flag == 'x':
				return mx
			else:
				return mn	

	def move(self, board, old_move, flag):
		self.start = time.time()
		self.endflag = 0

		var = (self.minmax_recur(board, old_move, flag, flag, 0, -10000000, 10000000, 2, 0))
		# print var
		
		mx = var[1]
		mn = var[1]
		cell_select=var[0]
		for i in range(3, 5):
			tmp = self.minmax_recur(board, old_move, flag, flag, 0, -10000000, 10000000, i, 0)
			if tmp[1] > mx and flag == 'x':
				mx = tmp[1]
				cell_select = tmp[0]
			if tmp[1] < mn and flag == 'o':
				mn = tmp[1]
				cell_select = tmp[0]
			if self.endflag == 1:
				break
		# print cell_select	
		return cell_select


	