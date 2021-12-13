class tower_of_hamoi :
    def __init__( self , n ):
        self.n = n
        self.towers =[ [ x for x in range( n , 0 , -1 ) ], [], [] ]

    def move( self , start , dest ):
        """
            Move o disco da pilha de origem para a de destino.
        """
        self.towers[ dest ].append( self.towers[ start ].pop() )



class AI_play:
    def __init__(self, n) -> None:
        self.mytower = tower_of_hamoi( n )
        self.move_list = []
    
    def solve_tower(self,  hanoi, n, start, aux, dest ):
        """
            Resolve a torre recursivamente, dividindo o problema em sub problemas,
            usando exemplo d nro d discos é igual a 3 # Move os discos 1 e 2 do 
            primeiro pino para o segundo pino usando o pino tres como auxiliar, 
            depois o disco 3 é movido # para o terceiro pino, para finalizar os 
            disco 1 e 2 são movidos do segundo pino para o pino terceiro pino 
            usando o primeiro pino como auxiliar.
        """
        if n == 0 : return 
        self.solve_tower( hanoi, n - 1, start, dest, aux )
        hanoi.move( start , dest )
        # print(hanoi.towers)
        self.move_list.append((start, dest))
        self.solve_tower( hanoi, n - 1 , aux, start, dest )
    
    def get_all_moves(self) -> list:
        """
            Get a list of all the moves.
        """
        # print( self.mytower.towers )
        self.solve_tower( self.mytower , self.mytower.n , 0 , 1 , 2 )
        # print( self.mytower.towers )
        # print(self.move_list)
        return self.move_list


# ai_play = AI_play(2)
# print(ai_play.get_all_moves())
