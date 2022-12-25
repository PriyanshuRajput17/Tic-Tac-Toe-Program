#Python program for tac toc toe between 2 people
from numpy import *

#Function comes into action during X's turn
def tictactoeX(n,m=matrix("'1' '2' '3' ; '4' '5' '6' ; '7' '8' '9'")):
    if n>9 or n<1:
        print("Please Enter a number between 1 to 9 only ")
    else:
        if n<4:
            m[0,n-1]='X'
        if n<7 and n>3:
            n=n-3
            m[1,n-1]='X'
        if n<10 and n>6:
            n=n-6
            m[2,n-1]='X'   
    temp=m
    print(temp)
    if horizontal_win(temp) or vertical_win(temp) or Diagonal_win(temp):
        print("X is the Winner")  
    else:
        if SpaceOnBoard(temp):
            n1=int(input("Enter position for O and press Enter: "))
            tictactoeO(n1,temp)
        else:
            print("Match Drawn")

#Function comes into action during O's turn
def tictactoeO(n,m=matrix("'1' '2' '3' ; '4' '5' '6' ; '7' '8' '9'")):
    print(m)
    if n>9 or n<1:
        print("Please Enter a number between 1 to 9 only ")
    else:
        if n<4:
            m[0,n-1]='O'
        if n<7 and n>3:
            n=n-3
            m[1,n-1]='O'
        if n<10 and n>6:
            n=n-6
            m[2,n-1]='O'   
    temp1=m
    print("Final Board")
    print(temp1)
    if horizontal_win(temp1) or vertical_win(temp1) or Diagonal_win(temp1):
        print("O is the Winner")
    else:
        if SpaceOnBoard(temp1):
            n1=int(input("Enter position for X and press Enter: "))
            tictactoeX(n1,temp1)
        else:
            print("Match Drawn")


#Functions Checking all the Winning possibilities
def horizontal_win(mat):
    if (mat[0,0]==mat[0,1]==mat[0,2] or mat[1,0]==mat[1,1]==mat[1,2] or mat[2,0]==mat[2,1]==mat[2,2]):
        return True
    return False

def vertical_win(mat):
    if (mat[0,0]==mat[1,0]==mat[2,0] or mat[0,1]==mat[1,1]==mat[2,1] or mat[0,2]==mat[1,2]==mat[2,2]):
        return True
    return False

def Diagonal_win(mat):
    if (mat[0,0]==mat[1,1]==mat[2,2] or mat[0,2]==mat[1,1]==mat[2,0]):
        return True
    return False

def SpaceOnBoard(mat):
    for i in range(3):
        for j in range(3):
            if mat[i,j].isdigit():
                return True


print(matrix("'1' '2' '3' ; '4' '5' '6' ; '7' '8' '9'"))
n=int(input("Enter position for 1st X and press enter: "))
tictactoeX(n,m=matrix("'1' '2' '3' ; '4' '5' '6' ; '7' '8' '9'"))









