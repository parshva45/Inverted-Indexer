import os, operator

def uni_frequency_tables_generator():

	uni_path = r'Indexing_Outputs/Unigrams.txt'
	uni_content = open(uni_path, 'r').read()
	uni_tokens_dict = {}
	uni_term_freq_table_dict = {}
	uni_doc_freq_table_dict = {}
	lines = uni_content.split('\n')
	lines = [l for l in lines if l != ""]
	for line in lines:
		divide = line.split(' -> ')
		term = divide[0]
		uni_tokens_dict[term] = []
		uni_term_freq_table_dict[term] = 0
		uni_doc_freq_table_dict[term] = []
		uni_doc_freq_table_dict[term].append([]) # docid(s)
		each = divide[1].replace(')','').replace('(','').split(' ')
		uni_doc_freq_table_dict[term].append(len(each))
		for e in each:
			key_value = e.rsplit(',', 1)
			docid = key_value[0]
			tf = key_value[1]
			uni_tokens_dict[term].append({"docid":docid,"tf":tf})
			uni_term_freq_table_dict[term]+=int(tf)
			uni_doc_freq_table_dict[term][0].append(docid)

	# sort term frequency tables in decreasing order of total term frequencies (values)
	uni_term_freq_table_dict = sorted(uni_term_freq_table_dict.items(), key=operator.itemgetter(1), reverse=True)
	# reverse = True for sorting in decreasing order of total term frequency

	# write frequency tables

	uni_tft = open("Frequency_Tables/Unigrams_Term_Frequency_Table.txt","w")
	uni_tft.write("Format : Term -> Sum of all Term frequencies\n")
	for i in uni_term_freq_table_dict:
		uni_tft.write("\n"+i[0]+" -> "+str(i[1]))
	uni_tft.close()

	uni_dft = open("Frequency_Tables/Unigrams_Document_Frequency_Table.txt","w")
	uni_dft.write("Format : Term -> List of Document ID(s) -> Document Frequency\n")
	for key,value in uni_doc_freq_table_dict.items():
		uni_dft.write("\n"+key+" -> "+str(value[0])+" -> "+str(value[1]))
	uni_dft.close()


def bi_frequency_tables_generator():

	bi_path = r'Indexing_Outputs/Bigrams.txt'
	bi_content = open(bi_path, 'r').read()
	bi_tokens_dict = {}
	bi_term_freq_table_dict = {}
	bi_doc_freq_table_dict = {}
	lines = bi_content.split('\n')
	lines = [l for l in lines if l != ""]
	for line in lines:
		divide = line.split(' -> ')
		term = divide[0]
		bi_tokens_dict[term] = []
		bi_term_freq_table_dict[term] = 0
		bi_doc_freq_table_dict[term] = []
		bi_doc_freq_table_dict[term].append([]) # docid(s)
		each = divide[1].replace(')','').replace('(','').split(' ')
		bi_doc_freq_table_dict[term].append(len(each))
		for e in each:
			key_value = e.rsplit(',', 1)
			docid = key_value[0]
			tf = key_value[1]
			bi_tokens_dict[term].append({"docid":docid,"tf":tf})
			bi_term_freq_table_dict[term]+=int(tf)
			bi_doc_freq_table_dict[term][0].append(docid)

	# sort term frequency tables in decreasing order of total term frequencies (values)
	bi_term_freq_table_dict = sorted(bi_term_freq_table_dict.items(), key=operator.itemgetter(1), reverse=True)
	# reverse = True for sorting in decreasing order of total term frequency

	# write frequency tables

	bi_tft = open("Frequency_Tables/Bigrams_Term_Frequency_Table.txt","w")
	bi_tft.write("Format : Term -> Sum of all Term frequencies\n")
	for i in bi_term_freq_table_dict:
		bi_tft.write("\n"+i[0]+" -> "+str(i[1]))
	bi_tft.close()

	bi_dft = open("Frequency_Tables/Bigrams_Document_Frequency_Table.txt","w")
	bi_dft.write("Format : Term -> List of Document ID(s) -> Document Frequency\n")
	for key,value in bi_doc_freq_table_dict.items():
		bi_dft.write("\n"+key+" -> "+str(value[0])+" -> "+str(value[1]))
	bi_dft.close()

def tri_term_frequency_table_generator():

	tri_path = r'Indexing_Outputs/Trigrams.txt'
	tri_content = open(tri_path, 'r').read()
	tri_tokens_dict = {}
	tri_term_freq_table_dict = {}
	lines = tri_content.split('\n')
	lines = [l for l in lines if l != ""]
	for line in lines:
		divide = line.split(' -> ')
		term = divide[0]
		tri_tokens_dict[term] = []
		tri_term_freq_table_dict[term] = 0
		each = divide[1].replace(')','').replace('(','').split(' ')
		for e in each:
			key_value = e.rsplit(',', 1)
			docid = key_value[0]
			tf = key_value[1]
			tri_tokens_dict[term].append({"docid":docid,"tf":tf})
			tri_term_freq_table_dict[term]+=int(tf)

	# sort term frequency tables in decreasing order of total term frequencies (values)
	tri_term_freq_table_dict = sorted(tri_term_freq_table_dict.items(), key=operator.itemgetter(1), reverse=True)
	# reverse = True for sorting in decreasing order of total term frequency

	# write term frequency table

	tri_tft = open("Frequency_Tables/Trigrams_Term_Frequency_Table.txt","w")
	tri_tft.write("Format : Term -> Sum of all Term frequencies\n")
	for i in tri_term_freq_table_dict:
		tri_tft.write("\n"+i[0]+" -> "+str(i[1]))
	tri_tft.close()


# run the program as:
# python task3.py

newpath = r'Frequency_Tables'
if not os.path.exists(newpath):
	os.makedirs(newpath)

uni_frequency_tables_generator()
bi_frequency_tables_generator()
tri_term_frequency_table_generator()