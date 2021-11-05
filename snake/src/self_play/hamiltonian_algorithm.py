


class Hamiltonian_Algorithm:

    counter :int
    algorithm_type :str
    table_info :dict
    possible_move :list
    previus_move :str

    def __init__(self, algorithm_type :str, table_info :dict) -> None:
        self.counter = 0
        self.algorithm_type = algorithm_type
        self.table_info = table_info
        self.possible_move = ["up", "left", "down", "right"]
        self.previus_move = ""
        self.aux = 0
        self.distribution = {
            "hamiltonian_horizontal": self.hamiltonian_horizontal, 
            "hamiltonian_vertical": self.hamiltonian_vertical, 
            "hamiltonian_spiral": self.hamiltonian_spiral
        }

    def hamiltonian_horizontal(self, snake_head_position :dict) -> str:
        if(self.previus_move == self.possible_move[0] and snake_head_position["x"] >= self.table_info["x_position"]+28):
            self.previus_move = self.possible_move[1]
            return self.possible_move[1]

        elif(self.previus_move == self.possible_move[0] and snake_head_position["x"] <= self.table_info["x_position"]+28):
            self.previus_move = self.possible_move[3]
            return self.possible_move[3]

        elif(snake_head_position["x"] >= self.table_info["x_position"]+self.table_info["widht"]-28):
            self.previus_move = self.possible_move[0]
            return self.possible_move[0]

        elif(snake_head_position["x"] <= self.table_info["x_position"]+28):
            self.previus_move = self.possible_move[0]
            return self.possible_move[0]
        
        print("Previus: ", self.previus_move)
        

        return ""

    def hamiltonian_vertical(self, ):
        pass

    def hamiltonian_spiral(self, ):
        pass

    def execute_algorithm(self, snake_head_position :dict):
        for key,value in self.distribution.items():
            if (key == self.algorithm_type):
                return value(snake_head_position)
