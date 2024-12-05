"""
Day 3: Mull It Over
https://adventofcode.com/2024/day/3
"""
import re
from utils.utils import timer

MUL = r"mul\(\d{1,3},\d{1,3}\)"
DO = r"do\(\)"
DONT = r"don't\(\)"
NUM = r"\d{1,3}"

def _isDo(instruction: str) -> bool:
  return re.match(DO, instruction)

def _isDont(instruction: str) -> bool:
  return re.match(DONT, instruction)

def _mul(nums: list[str]):
  return int(nums[0])*int(nums[1])

def pt1(instructions: str) -> int:
  if not instructions: return 0 # ie. empty string
  muls = re.findall(MUL, instructions)
  
  s = 0
  for mul in muls:
    nums = re.findall(NUM, mul)
    s += _mul(nums) # assume exactly 2 nums found
  return s

@timer
def pt2(instructions: str) -> int:
  matches = re.findall(f'{MUL}|{DO}|{DONT}', instructions)
  
  s = 0
  do = True
  for match in matches:
    if not do: # search for do
      if _isDo(match):
        do = True
      continue

    if _isDont(match):
      do = False
      continue

    # can be mul or another do
    if _isDo(match): continue
    nums = re.findall(NUM, match)
    s += _mul(nums) # assume exactly 2 nums found
  
  return s

@timer
def pt2_1(instructions: str) -> int:
  # idea: split the string around 'do()'; within those, split the string before the first dont()
  dos = instructions.split("do()")

  s = 0
  for do in dos:
    before_dont = do.split("don't()")[0]
    s += pt1(before_dont)
  
  return s


if __name__ == '__main__':
  test_input1 = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
  print(pt1(test_input1), 'should be 161')
  
  test_input2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
  print(pt2(test_input2), 'should be 48')
  print(pt2_1(test_input2), 'should be 48')

  # exit() # comment out to test real input

  path = "./3/input.txt" # assumes running from aoc24 root
  with open(path, 'r') as file:
    my_input = file.read()
    print(pt1(my_input)) # 161085926
    print(pt2(my_input)) # 82045421
    print(pt2_1(my_input)) # 82045421

