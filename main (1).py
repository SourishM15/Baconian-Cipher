"""
Baconian Cipher
By: Sourish Mukherji
"""

encrypt = ""
Alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Baconion = ['aaaaa', 'aaaab', 'aaaba', 'aaabb', 'aabaa', 'aabab', 'aabba', 'aabbb', 'abaaa', 'abaab', 'ababa', 'ababb', 'abbaa', 'abbab', 'abbba', 'abbbb', 'baaaa', 'baaab', 'baaba', 'baabb', 'babaa', 'babab', 'babba', 'babbb', 'bbaaa', 'bbaab']
print("Type a word of your choice:")
UI = input().upper()
charArr = [char for char in UI]
for x in range(len(charArr)):
  for y in range(len(Alpha)):
    if charArr[x] == Alpha[y]:
      encrypt += Baconion[y]
print(encrypt)
      

