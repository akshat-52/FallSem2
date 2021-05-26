x={b'Emplid': b'12345', b'Name': b'Paras', b'Company':b'Cyware'}
x={y.decode('ascii'): x.get(y).decode('ascii') for y in x.keys() }
print(x)