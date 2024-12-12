"""
Day 11: Plutonian Pebbles
https://adventofcode.com/2024/day/11
"""
from typing import List, Tuple

def _count_digits(stone: int) -> bool:
  if stone == 0: return 1
  n = 0
  while stone:
    n += 1
    stone //= 10
  return n

def _split_stone(stone: int, N: int) -> Tuple[int]:
  # assume N is even number >=2
  n = 0
  r = 0
  while n < N//2:
    digit = stone%10
    r += digit*10**n
    stone //= 10
    n += 1
  return stone, r

def _blink(stones: List[int]) -> List[int]:
  new_stones = []
  for stone in stones:
    if stone == 0:
      new_stones.append(1)
      continue
    else:
      N = _count_digits(stone)
      if N%2 == 0:
        for new_stone in _split_stone(stone, N): new_stones.append(new_stone)
        continue
    # does not match above 2 cases
    new_stones.append(stone*2024)
  return new_stones

def multi_blink(stones: List[int], times: int = 0) -> List[int]:
  while times > 0:
    stones = _blink(stones)
    times -= 1
  return stones

if __name__ == '__main__':
  test_input1 = ([125,17], 25)
  # s = multi_blink(*test_input1)
  # print(s)
  # print(len(s)) # 55312

  puzzle_input = ([112, 1110, 163902, 0, 7656027, 83039, 9, 74], 25)
  s = multi_blink(*puzzle_input)
  print(len(s))
