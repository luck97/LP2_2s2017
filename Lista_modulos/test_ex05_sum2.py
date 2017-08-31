# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# E. sum2
# Dada uma lista de inteiros de qualquer tamanho
# retorna a soma dos dois primeiros elementos
# se a lista tiver menos de dois elementos, soma o que for possível
def sum2(nums):
  if len(nums) >= 2:
    return nums[0] + nums[1]
  else:
    if len(nums) == 1:
      return nums[0]
    else:
      if len(nums)==0:
        return 0
    
def test_ex05():
  print ('sum2')
  assert sum2([1, 2, 3]) == 3
  assert sum2([1, 1]) == 2
  assert sum2([1, 1, 1, 1]) == 2
  assert sum2([1, 2]) == 3
  assert sum2([1]) == 1
  assert sum2([]) == 0
  assert sum2([4, 5, 6]) == 9
  assert sum2([4]) == 4

