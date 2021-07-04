# Easy way to convert a string into a list
>>> names = 'James Anita Ray Stephen Lisa'.split()
>>> names
['James', 'Anita', 'Ray', 'Stephen', 'Lisa']

# Zip names with scores
>>> scores = (22, 45, 76, 34)

>>> list(zip(names, scores))
[('James', 22), ('Anita', 45), ('Ray', 76), ('Stephen', 34)]
>>> dict(zip(names, scores))
{'James': 22, 'Anita': 45, 'Ray': 76, 'Stephen': 34}

# Use zip_longest to pair the extra name with None
>>> from itertools import zip_longest
>>> list(zip_longest(names, scores))
[('James', 22), ('Anita', 45), ('Ray', 76), ('Stephen', 34), ('Lisa', None)]
