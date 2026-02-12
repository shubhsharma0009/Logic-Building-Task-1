names = [" Alice ", "bob", " CHARLIE "]

clean_names = []

for name in names:
    n = name.strip()      # remove extra spaces
    n = n.lower()         # convert to lowercase
    clean_names.append(n)

print("Cleaned Names:", clean_names)