"""
Day 6: Guard Gallivant
https://adventofcode.com/2024/day/6
"""
from typing import List, Tuple, Dict
from io import StringIO, TextIOWrapper
from utils import timer

class Solution:
  
  TURNS = {'^':'>', '>':'v', 'v':'<', '<':'^'}
  NEXT_CELL = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}

  def __init__(self, my_map: List[List[str]]):
    self.positions = set()
    self.map = my_map
    self.M, self.N = len(my_map), len(my_map[0])
    self.guard = self._find_guard()
    self.positions.add((self.guard['i'], self.guard['j']))

  def _find_guard(self) -> Dict:
    for i,row in enumerate(self.map):
      for j,item in enumerate(row):
        if item not in ['.','#']:
          return {'i':i, 'j':j, 'dir':item}

  def _mapget(self, i, j):
    return self.map[i][j]

  def _turn(self) -> None:
    self.guard['dir'] = self.TURNS[self.guard['dir']]

  def _inside(self, coords) -> bool:
    return (-1 < coords[0] < self.M) and (-1 < coords[1] < self.N)

  def _walk(self) -> bool:
    """
    Simulates a guard's uni-directional walk.

    Returns False if they exit the map.
    """
    d = self.NEXT_CELL[self.guard['dir']] # delta
    
    p = (self.guard['i'], self.guard['j'])
    while self._inside(p) and self._mapget(*p) != '#':
      self.positions.add(p)
      p = (p[0]+d[0], p[1]+d[1])

    # while-loop has stopped meaning the guard is an invalid position.
    if not self._inside(p): return False
    elif self._mapget(*p): # should always be the case...
      self.guard['i'],self.guard['j'] = p[0]-d[0],p[1]-d[1]
    return True
  
  def full_walk(self) -> None:
    p = self._walk()
    while p:
      self._turn()
      p = self._walk()
    print('done walking')

def create_map(buffer: TextIOWrapper):
  my_map = []
  line = buffer.readline().strip()
  while line:
    my_map.append([c for c in line])
    line = buffer.readline().strip()
  return my_map

if __name__=='__main__':

  test_input = "\
    ....#.....\n\
    .........#\n\
    ..........\n\
    ..#.......\n\
    .......#..\n\
    ..........\n\
    .#..^.....\n\
    ........#.\n\
    #.........\n\
    ......#...\n\
  "
  my_map = create_map(StringIO(test_input))
  for row in my_map: print(row);print('\n')
  # s = Solution(my_map)
  # s.full_walk()
  # print(len(s.positions))

  exit()
  
  path = "./6/input.txt" # assumes running from aoc24 root
  with open(path, 'r') as file:
    # create the map
    my_map = create_map(file)
    s = Solution(my_map)
    s.full_walk()
    print(len(s.positions))
    