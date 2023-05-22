def isSafe(i, j):
	for k in range(0, N):
		if (board[i][k] == 1 or board[k][j] == 1):
			return False
		
	for k in range(0, N):
		for l in range(0, N):
			if k+l == i+j or k-l == i-j:
				if board[k][l] == 1:
					return False
	
	return True

def NQueens(n):
	if n==0:
		return True
	
	for i in range(0, N):
		for j in range(0, N):
			if(isSafe(i, j) and board[i][j]!=1):
				board[i][j]=1
				if NQueens(n-1):
					return True
				board[i][j]=0
	
	return False
	
N = int(input('Enter number of queens: '))

board = [[0]*N for _ in range(N)]

NQueens(N)

for i in board:
	print(i)
