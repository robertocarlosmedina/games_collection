


class Hamiltonian_Algorithm:

    counter :int
    algorithm_type :str
    table_info :dict
    possible_move :list
    previus_move :str
    current_direction :str
    snake_step :int

    def __init__(self, algorithm_type :str, table_info :dict, snake_step :int) -> None:
        self.counter = 0
        self.algorithm_type = algorithm_type
        self.table_info = table_info
        self.snake_step = snake_step
        self.previus_move = ""
        self.aux = 0
        self.distribution = {
            "hamiltonian_horizontal": self.hamiltonian_horizontal, 
            "hamiltonian_vertical": self.hamiltonian_vertical, 
            "hamiltonian_spiral": self.hamiltonian_spiral
        }
        self.setup_possible_moves()
    
    def setup_possible_moves(self):
        if(self.algorithm_type == "hamiltonian_horizontal"):
            self.possible_move = {
                "up": {
                    "right": [
                        self.table_info["x_position"], 
                        self.table_info["x_position"] + self.snake_step*2,
                        self.table_info["y_position"] ,
                        self.table_info["y_position"] + self.table_info["height"],
                    ],
                    "left": [
                        self.table_info["x_position"] + self.table_info["widht"] - self.snake_step*5,
                        self.table_info["x_position"] + self.table_info["widht"] - self.snake_step,
                        self.table_info["y_position"] ,
                        self.table_info["y_position"] + self.table_info["height"],
                    ]
                }, 
                "left": {
                    "up": [
                        self.table_info["x_position"],
                        self.table_info["x_position"] + self.snake_step*2,
                        self.table_info["y_position"] ,
                        self.table_info["y_position"] + self.table_info["height"],
                    ]

                }, 
                "down": {
                    "left": [
                        self.table_info["x_position"] + self.table_info["widht"] - self.snake_step*2,
                        self.table_info["x_position"] + self.table_info["widht"] ,
                        self.table_info["y_position"] + self.table_info["height"] - self.snake_step*2,
                        self.table_info["y_position"] + self.table_info["height"],
                    ]
                },
                "right": {
                    "down": [
                        self.table_info["x_position"] + self.table_info["widht"] - self.snake_step*2,
                        self.table_info["x_position"] + self.table_info["widht"],
                        self.table_info["y_position"],
                        self.table_info["y_position"] + self.snake_step,
                    ],
                    "up": [
                        self.table_info["x_position"] + self.table_info["widht"] - self.snake_step*3,
                        self.table_info["x_position"] + self.table_info["widht"] - self.snake_step*2,
                        self.table_info["y_position"] + self.snake_step*2,
                        self.table_info["y_position"] + self.table_info["height"],
                    ]
                },
            }

    def hamiltonian_horizontal(self, snake_head_position :dict) -> str:
        for key,values in self.possible_move[self.current_direction].items():
            if(snake_head_position["x"] in range(values[0], values[1]) and snake_head_position["y"] in range(values[2], values[3])):
                return key

        return ""

    def hamiltonian_vertical(self):
        pass

    def hamiltonian_spiral(self, ):
        pass

    def execute_algorithm(self, snake_head_position :dict, current_direction :str):
        self.current_direction = current_direction
        for key,value in self.distribution.items():
            if (key == self.algorithm_type):
                return value(snake_head_position)
