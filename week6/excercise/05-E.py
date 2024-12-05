from abc import ABC, abstractmethod

class Species():
    def __init__(self, x, y) -> None:
        self.hour: int = 0
        self.x: int = x
        self.y: int = y
    
    @abstractmethod
    def move(self):
        pass

    def check_torus_shape(self):
        if self.x > 9:
            self.x = self.x - 10
        elif self.x < 0:
            self.x = self.x + 10
        if self.y > 9:
            self.y = self.y - 10
        elif self.y < 0:
            self.y = self.y + 10


class Asimovians(Species):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.species_short = "a"

    def move(self):
        if self.hour % 2 == 0:
            self.x += 3
        else:
            self.y -= 3
        
        self.check_torus_shape()
        
        self.hour += 1


class Lems(Species):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.species_short = "l"

    def move(self):
        if self.hour % 2 == 0:
            self.x -= 1
        else:
            self.y += 1
        
        self.check_torus_shape()
        
        self.hour += 1
    

class Julvers(Species):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.direction = 0 
        self.species_short = "j"

    def move(self):
        if self.direction == 0:  
            self.x += 2
        elif self.direction == 1:  
            self.y += 2
        elif self.direction == 2:  
            self.x -= 2
        elif self.direction == 3:  
            self.y -= 2
        
        # because of open grid (put that check in seperate method)
        self.check_torus_shape()

        self.direction = (self.direction + 1) % 4
        
        self.hour += 1
        

class PlayingGrid:

    def __init__(self, players):
        self.players = players
        self.grid = [["-" for _ in range(10)] for _ in range(10)]
        self.initialize_grid()
    
    def initialize_grid(self):
        for player in self.players:
            self.grid[player.y][player.x] = player.species_short

    def move_players(self):
        for player in self.players:
            previous_x = player.x
            previous_y = player.y
            player.move()
            if self.grid[player.y][player.x] == "-":
                self.grid[player.y][player.x] = f"{player.species_short}"
                self.grid[previous_y][previous_x] = "-"
            else:
                # reset move 
                player.y = previous_y
                player.x = previous_x

# mapping dictionary to create species
species_classes = {
    "asimovians": Asimovians,
    "lems": Lems,
    "julvers": Julvers
}

# initialize all species
play_config = input().split(sep=",")
#play_config = ['2', ' lems 4 2', ' julvers 3 2', ' asimovians 2 2', ' asimovians 8 3', ' julvers 4 0', ' lems 2 9', ' asimovians 1 4', ' lems 6 2', ' lems 5 3', ' lems 8 9', ' lems 5 6', ' julvers 5 1', ' lems 9 4', ' julvers 7 8', ' julvers 2 7', ' julvers 2 4', ' asimovians 2 8', ' lems 4 5', ' lems 4 9', ' lems 9 7', ' julvers 3 9', ' asimovians 3 5', ' asimovians 1 6', ' julvers 7 6', ' asimovians 6 0', ' asimovians 7 4', ' asimovians 6 4', ' lems 8 2', ' julvers 9 3', ' julvers 7 3']
total_rounds = int(play_config.pop(0))
playing_species = []
for specie in play_config:
    specie = specie.strip().split(sep=" ")
    species_name = specie[0]
    x = int(specie[1])
    y = int(specie[2])
    species_class = species_classes.get(species_name)
    if species_class:
        playing_species.append(species_class(x, y))

# configure grid
grid = PlayingGrid(players=playing_species)

# play
for i in range(0, total_rounds):
    grid.move_players()

for row in grid.grid:
    print(' '.join(row))

