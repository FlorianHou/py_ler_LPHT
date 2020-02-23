dict = {}
dict['florian'] = 175
dict['lisa'] = 165
print(dict.keys())

filename = 'DictWriteInFile.txt'
with open(filename,'w') as file_object:
	file_object.write(str(dict.keys()))