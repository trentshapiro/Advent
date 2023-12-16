import numpy as np
from dataclasses import dataclass

with open("day16_input_sample.txt") as f:
    a = f.readlines()
    a = [list(i.replace("\n", "")) for i in a]

BOARD = np.matrix(a)

BOARD_MAP = {
    ("/", (0, 1)): (-1, 0),
    ("/", (0, -1)): (1, 0),
    ("/", (1, 0)): (0, -1),
    ("/", (-1, 0)): (0, 1),
    ("\\", (0, 1)): (1, 0),
    ("\\", (0, -1)): (-1, 0),
    ("\\", (1, 0)): (0, 1),
    ("\\", (-1, 0)): (0, -1),
    (".", (0, 1)): (0, 1),
    (".", (0, -1)): (0, -1),
    (".", (1, 0)): (1, 0),
    (".", (-1, 0)): (-1, 0),
    ("-", (0, 1)): (0, 1),
    ("-", (0, -1)): (0, -1),
    ("|", (1, 0)): (1, 0),
    ("|", (-1, 0)): (-1, 0),
}

SPLIT_MAP = {
    "-": [(0, 1), (0, -1)],
    "|": [(1, 0), (-1, 0)],
}


@dataclass
class Beam:
    position: tuple[int, int]
    direction: tuple[int, int]
    active: bool = True

    def follow_path(self) -> None:
        while self.active:
            # been here from same incoming direction, already lit
            if (self.position, self.direction) in SEEN_TILES:
                self.active = False
                return

            # hit edge
            if (
                (self.position[0] > np.shape(BOARD)[0] - 1)
                or (self.position[0] < 0)
                or (self.position[1] > np.shape(BOARD)[1] - 1)
                or (self.position[1] < 0)
            ):
                self.active = False
                return

            SEEN_TILES.append((self.position, self.direction))

            current_tile = BOARD[self.position]
            if (current_tile, self.direction) in BOARD_MAP.keys():
                self.direction = BOARD_MAP[(current_tile, self.direction)]
                self.position = tuple([x + y for x, y in zip(self.position, self.direction)])
                self.follow_path()
            else:
                for heading in SPLIT_MAP[current_tile]:
                    new_pos = tuple([x + y for x, y in zip(self.position, heading)])
                    BEAMS.append(Beam(new_pos, heading))
                self.active = False


max_light = 0
board_size = BOARD.shape[0]
hor_1 = [((0, i), (1, 0)) for i in range(0, board_size)]
hor_2 = [((board_size - 1, i), (-1, 0)) for i in range(0, board_size)]
ver_1 = [((i, 0), (0, 1)) for i in range(0, board_size)]
ver_2 = [((i, board_size - 1), (0, -1)) for i in range(0, board_size)]

starts = hor_1 + hor_2 + ver_1 + ver_2

for start_pos, start_heading in starts:
    BEAMS = []
    SEEN_TILES = []
    BEAMS.append(Beam(start_pos, start_heading, True))

    while any([i.active for i in BEAMS]):
        for beam in BEAMS:
            beam.follow_path()

    output = np.full_like(BOARD, 0, int)
    for i, _ in SEEN_TILES:
        output[i] = 1

    if output.sum() > max_light:
        max_light = output.sum()
    if (start_pos, start_heading) == ((0, 0), (0, 1)):
        print(output.sum())

print(max_light)
