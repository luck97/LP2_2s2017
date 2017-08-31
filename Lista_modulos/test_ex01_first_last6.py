# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# A. first_last6
# verifica se 6 é o primeiro ou último elemento da lista nums
# first_last6([1, 2, 6]) -> True
# first_last6([6, 1, 2, 3]) -> True
# first_last6([3, 2, 1]) -> False
def first_last6(nums):
  retorno = True
  if not 6 in nums:
    retorno = False
  else: 
    if nums [0] == 6 or nums [-1] == 6:
      retorno = True
    else:
      retorno = False
  return retorno

def test_ex01():
  print ('First_last6')
  assert first_last6([1, 2, 6]) == True
  assert first_last6([6, 1, 2, 3]) == True
  assert first_last6([3, 2, 1]) == False
  assert first_last6([3, 6, 1]) == False
  assert first_last6([3, 6]) == True
  assert first_last6([6]) == True
  assert first_last6([3]) == False


