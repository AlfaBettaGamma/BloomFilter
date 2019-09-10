class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_arr = [0] * self.filter_len
        # создаём битовый массив длиной f_len ...

    def hash1(self, str1):
      m, n = 17, 0
        # 17
      for c in str1:
        code = ord(c)
        n = n*m + code
      n = n % self.filter_len
      return n
        # реализация ...

    def hash2(self, str1):
      m, n = 223, 0
        # 223 
      for c in str1:
        code = ord(c)
        n = n*m + code
      n = n % self.filter_len
      return n
        # ...

    def add(self, str1):
      hash_arr = [self.hash1,self.hash2]
      for i in hash_arr:
        self.bit_arr[i(str1)] = 1
        # добавляем строку str1 в фильтр

    def is_value(self, str1):
      hash_arr = [self.hash1,self.hash2]
      summ = 0
      for i in hash_arr:
        if self.bit_arr[i(str1)] == 1:
          summ += 1
      if summ == len(hash_arr):
        return True
      return False
        # проверка, имеется ли строка str1 в фильтре