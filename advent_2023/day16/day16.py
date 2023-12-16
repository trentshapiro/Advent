import numpy as np
from dataclasses import dataclass
from multiprocessing import Process, Manager
import time


with open("day16_input.txt") as f:
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


def eval_light(start_pos, start_heading, return_list):
    BEAMS = []
    SEEN_TILES = []

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

    BEAMS.append(Beam(start_pos, start_heading, True))

    while any([i.active for i in BEAMS]):
        for beam in BEAMS:
            beam.follow_path()

    output = np.full_like(BOARD, 0, int)
    for i, _ in SEEN_TILES:
        output[i] = 1
    if (start_pos, start_heading) == ((0, 0), (0, 1)):
        print(f"Part 1: {output.sum()}")

    return_list.append(output.sum())


# generate perimeter starts
hor_1 = [((0, i), (1, 0)) for i in range(0, BOARD.shape[0])]
hor_2 = [((BOARD.shape[0] - 1, i), (-1, 0)) for i in range(0, BOARD.shape[0])]
ver_1 = [((i, 0), (0, 1)) for i in range(0, BOARD.shape[1])]
ver_2 = [((i, BOARD.shape[1] - 1), (0, -1)) for i in range(0, BOARD.shape[1])]
starts = hor_1 + hor_2 + ver_1 + ver_2


if __name__ == "__main__":
    start_time = time.time()
    manager = Manager()
    return_list = manager.list()
    procs = []
    for start, heading in starts:
        new_proc = Process(target=eval_light, args=(start, heading, return_list))
        procs.append(new_proc)
        new_proc.start()

    for proc in procs:
        proc.join()

    max_light = max(return_list)
    print(f"Part 2: {max_light}")
    print(time.time() - start_time)
