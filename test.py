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

test = BloomFilter(32)
test.add("0123456789")
test.add("1234567890")
test.add("2345678901")
test.add("3456789012")
test.add("4567890123")
test.add("5678901234")
test.add("6789012345")
test.add("7890123456")
test.add("8901234567")
test.add("9012345678")

print(test.is_value('6789012354'))