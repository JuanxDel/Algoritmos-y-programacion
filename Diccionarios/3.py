d = {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5}

l = []

for valor in d.values():
    if valor not in l:
        l = l + [valor]

print(l)