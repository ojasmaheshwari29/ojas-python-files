#1
s = input()
vowels = "aeiouAEIOU"
v_count = c_count = d_count = s_count = o_count = 0

for ch in s:
  if ch in vowels:
    v_count += 1
  elif ch.isalpha():
    c_count += 1
  elif ch.isdigit():
    d_count += 1
  elif ch.isspace():
    s_count += 1
  else:
    o_count += 1

print(f"Vowels: {v_count}")
print(f"Consonants: {c_count}")
print(f"Digits: {d_count}")
print(f"Spaces: {s_count}")
print(f"Others: {o_count}")
#2
