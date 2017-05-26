def check_permutation(str1, str2):
    return sorted(str1.lower())==sorted(str2.lower())

#tests
print(check_permutation('Listen', 'Silent'))
print(check_permutation('pants', 'stamp'))
print(check_permutation('2', 'He21'))
print(check_permutation('cat', ''))
