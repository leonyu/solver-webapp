from typing import Iterable, Optional, Tuple, Dict, List

Coord = Tuple[int, int]


class Coloring:
    def __init__(self, data):
        # type: (List[List[int]]) -> None
        self.data = {}  # type: Dict[Coord, int]
        self.size = (len(data), max(len(row_data) for row_data in data))
        for r in range(0, self.size[0]):
            for c in range(0, self.size[1]):
                self.data[(r, c)] = data[r][c]

    def get_adjacent(self, coord):
        # type: (Coord) -> Iterable[Coord]
        (r, c) = coord
        result = [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]
        return filter(lambda c: c in self.data, result)

    def _color(self, coord, result, palette, brush=None):
        # type: (Coord, Dict[Coord, int], Dict[int, List[Coord]], Optional[int]) -> None

        # check if cell is color, if it is return
        if coord in result:
            return
        if brush is None:
            brush = len(palette)
            palette[brush] = []
        result[coord] = brush
        palette[brush].append(coord)
        queue = []
        # enumerate all adjacent uncolored pixels
        for adj_coord in self.get_adjacent(coord):
            if self.data[coord] == self.data[adj_coord]:
                # color all pixels of same value with same color
                self._color(adj_coord, result, palette, brush)
            else:
                # queue pixels with different color
                queue.append(adj_coord)
        for c in queue:
            self._color(c, result, palette)

    def color(self):
        # type: () -> Dict[Coord, int]
        result = {}  # type: Dict[Coord, int]
        palette = {}  # type: Dict[int, List[Coord]]
        self._color((0, 0), result, palette)
        return result
