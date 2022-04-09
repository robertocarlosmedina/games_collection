__author__ = "Roberto Medina, Rafael Pires"
__copyright__ = "Copyright 2021, Roberto Carlos Medina"
__version__ = "0.0.1"
__maintainer__ = "Roberto Medina"
__email__ = "robertocarlosmedina.dev@gmail.com "
__status__ = "Production"

class tower_of_hamoi :
    def __init__( self , n ):
        self.n = n
        self.towers =[ [ x for x in range( n , 0 , -1 ) ], [], [] ]

    def move( self , start , dest ):
        """
            Move's the disk from the origin stack to the distination one.
        """
        self.towers[ dest ].append( self.towers[ start ].pop() )



class AI_play:
    def __init__(self, n) -> None:
        self.mytower = tower_of_hamoi( n )
        self.move_list = []
    
    def solve_tower(self,  hanoi, n, start, aux, dest ):
        """
            Solve the tower recursively, byt deviding the problem in sub problem.
            If the by example n = 3, it moves the disk's 1 and 2 of the firts peg
            to the secund peg making use of the peg 3 as an auxiliar, 
            and then moving the disk 3 to the peg 3, and to finish the disk's 1 and 2
            are moved to the peg 3 using the peg 1 as an auxiliar.
        """
        if n == 0 : return 
        self.solve_tower( hanoi, n - 1, start, dest, aux )
        hanoi.move( start , dest )
        # print(hanoi.towers)
        self.move_list.append((start, dest))
        self.solve_tower( hanoi, n - 1 , aux, start, dest )
    
    def get_all_moves(self) -> list:
        """
            Method's the retunr a list of all the moves.
        """
        # print( self.mytower.towers )
        self.solve_tower( self.mytower , self.mytower.n , 0 , 1 , 2 )
        # print( self.mytower.towers )
        # print(self.move_list)
        return self.move_list

# ai_play = AI_play(10)
# print(ai_play.get_all_moves())
