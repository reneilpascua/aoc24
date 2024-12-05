"""
Day 3: Mull It Over
https://adventofcode.com/2024/day/3
"""
import re

class Solution:
  MUL = r"mul\(\d{1,3},\d{1,3}\)"
  DO = r"do\(\)"
  DONT = r"don't\(\)"
  NUM = r"\d{1,3}"
  
  def _isDo(self, instruction: str) -> bool:
    return re.match(self.DO, instruction)

  def _isDont(self, instruction: str) -> bool:
    return re.match(self.DONT, instruction)

  def _mul(self, nums: list[str]):
    return int(nums[0])*int(nums[1])
  
  def pt1(self, instructions) -> int:
    muls = re.findall(self.MUL, instructions)
    
    s = 0
    for mul in muls:
      nums = re.findall(self.NUM, mul)
      s += self._mul(nums) # assume exactly 2 nums found
    return s
  
  def pt2(self, instructions) -> int:
    matches = re.findall(f'{self.MUL}|{self.DO}|{self.DONT}', instructions)
    
    s = 0
    do = True
    for match in matches:
      if not do: # search for do
        if self._isDo(match):
          do = True
        continue

      if self._isDont(match):
        do = False
        continue

      # can be mul or another do
      if self._isDo(match): continue
      nums = re.findall(self.NUM, match)
      s += self._mul(nums) # assume exactly 2 nums found
    
    return s

if __name__ == '__main__':
  s = Solution()

  test_input1 = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
  print(s.pt1(test_input1), 'should be 161')
  
  test_input2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
  print(s.pt2(test_input2), 'should be 48')

  # exit() # comment out to test real input

  path = "./3/input.txt" # assumes running from aoc24 root
  with open(path, 'r') as file:
    my_input = file.read()
    print(s.pt1(my_input)) # 161085926
    print(s.pt2(my_input)) # ?

