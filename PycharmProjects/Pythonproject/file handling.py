#f = open'./files/reading_file_example.txt'
#print(f)

f = open './files/reading_file_example.txt'
txt = f.read()
print(type(txt))
f.close()