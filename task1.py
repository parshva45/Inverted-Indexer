from bs4 import BeautifulSoup
import re
import os
import string

def abc():
	global_name = open("Global_statistics.txt","w")
	path = r'Tokenization_Outputs'
	total = 0
	for file in os.listdir(path):
		current_file = os.path.join(path, file)
		# extract the content of the file, which is the raw html
		content = open(current_file, 'r').read()
		dc = content.split(" ")
		dc = [w for w in dc if w != ""]
		total+=len(dc)
		global_name.write("\n"+str(len(dc)))
	global_name.write("\n\n"+str(total))
	global_name.write("\n"+str(total/1000))

def tokenizer(case_fold, remove_punctuate):
	path = r'Raw_HTML_Downloads'
	for file in os.listdir(path):
		current_file = os.path.join(path, file)
		print(current_file)
		# extract the content of the file, which is the raw html
		content = open(current_file, 'r').read()
		content = content.replace('\\n','')
		# convert it into soup
		soup = BeautifulSoup(content,"html.parser")
		# a list of tags to be ignored while tokenizing
		invalid_tags = ['script','img','annotation']
		for tag in invalid_tags: 
		    for match in soup.findAll(tag):
		    	# remove if found
		    	match.decompose()
		# get the text part from the soup
		soup = soup.get_text(separator=u" ", strip=True)
		soup_string = str(soup)
		# remove the b' part in the start of each raw html
		soup_string = soup_string[2:]

		# translator for replacing each occurrence of punctuation with space		
		translator = str.maketrans(string.punctuation, ' '*len(string.punctuation)) #map punctuation to space
		# array to hold tokens
		final = []
		# list of punctuations to be allowed if at beginning or end of digits
		allowed_before = ['$','+','.','-']
		allowed_after = ['+','%']

		for ele in soup_string.split(' '):

			# if to remove punctuations and doesnt start/end with $ or +, strip leading, trailing punctuations
			if remove_punctuate and ele[:1] not in allowed_before and ele[-1:] not in allowed_after:
				stripped_ele = ele.strip(string.punctuation)
			# if ele is just punctuations, remove it
			elif ele.strip(string.punctuation) == '':
				stripped_ele = ''
			# else keep ele as it is
			else:
				stripped_ele = ele

			# if case-folding to be performed
			if case_fold:
				stripped_ele = stripped_ele.lower()

			# dont consider ele with \ to avoid tokens like \xe2 which are UTF-8 formats of special symbols
			if '\\' not in stripped_ele and stripped_ele != '':
				# if to remove punctuations and contains alphabets
				if remove_punctuate and not re.match('[0-9/.+,$%-]+$', stripped_ele):
					# if contains allowed punctuations between alphabets, replace each with space
					if '-'or'/'or'.'or','or'$'or'+'or'%' in stripped_ele:
						for e in stripped_ele.translate(translator).split(' '):
							e = e.strip(string.punctuation)
							final.append(e)
				# just numbers and allowed punctuations with them
				else:
					# if starts with $, +, . or -
					# like $500 +50% -20.5 $250+
					if stripped_ele.startswith('$') or stripped_ele.startswith('+') or stripped_ele.startswith('.') or stripped_ele.startswith('-'):
						# if also ends with % or +
						# like +50% $250+
						if stripped_ele.endswith('%') or stripped_ele.endswith('+'):
							# replace the just start/end punctuations in between by spaces
							strr = stripped_ele[1:-1].replace('$',' ').replace('%',' ').replace('+',' ').split(' ')
							# append ending with character to last array element
							strr[-1]+=stripped_ele[-1:]
						# just starts with $, +, . or -
						# like $500 -20.5
						else:
							# replace the just start/end punctuations except for the starts with character by spaces
							strr = stripped_ele[1:].replace('$',' ').replace('%',' ').replace('+',' ').split(' ')
						# append first array element to starts with character
						strr[0] = stripped_ele[:1]+strr[0]
					# if just ends with % or +
					# like 25% 100+
					elif stripped_ele.endswith('%') or stripped_ele.endswith('+'):
						# replace the just start/end punctuations except for the ends with character by spaces
						strr = stripped_ele[:-1].replace('$',' ').replace('%',' ').replace('+',' ').split(' ')
						# append ending with character to last array element
						strr[-1]+=stripped_ele[-1:]
					# no starts or ends with punctuations
					# like 245.56 600
					else:
						# replace the just start/end punctuations with spaces
						strr = stripped_ele.replace('$',' ').replace('%',' ').replace('+',' ').split(' ')

					# appending all non-empty e to get final
					for e in strr:
						if e.strip(string.punctuation) != '':
							final.append(e)

		# appending all final elements to get final_str
		final_str = ''
		for ele in final:
			final_str+=(ele+" ")

		# replace multiple spaces with single space
		final_string = re.sub(' +',' ',final_str)

		name = open("Tokenization_Outputs/"+file,"w")
		name.write(final_string)
		name.close()
		

# run the program as:
# python task1.py
# then decide if you want to perform case-folding and/or punctuation handling or none

newpath = r'Tokenization_Outputs'
if not os.path.exists(newpath):
	os.makedirs(newpath)

# print("\nDecide if you want to perform case-folding and/or punctuation handling or none:\n")
# print("Enter 1 if you want to perform both case-folding and punctuation handling")
# print("Enter 2 if you want to perform just case-folding")
# print("Enter 3 if you want to perform just punctuation handling")
# print("Enter 4 if you dont want to perform case-folding or punctuation handling\n")

# value = input()

# if value == '1':
# 	tokenizer(True,True)
# elif value == '2':
# 	tokenizer(True,False)
# elif value == '3':
# 	tokenizer(False,True)
# elif value == '4':
# 	tokenizer(False,False)
# else:
# 	print("Invalid input")

abc()