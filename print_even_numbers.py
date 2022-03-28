  def print_even_numbers_from_end(a):
    cnt = 0
    while a > 0:

      a //= 10
      cnt = cnt + 1
      if cnt % 2:
        c = a % 10
        print(c)
  print_even_numbers_from_end(17490345)
