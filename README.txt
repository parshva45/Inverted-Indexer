- The three tasks of the IR HW3 are performed by:

1) Three python files task1.py, task2.py, task3.py
   performing each of the tasks 1, 2, 3 respectively

2) A directory named "Raw_HTML_Downloads" which contains 1000 files each
   containing raw html code of 1000 URLs crawled in IR HW1 Task1
      (Input for HW3 Task 1)

3) A directory named "Tokenization_Outputs" which contains 1000 files which are
   output files of Task 1

4) A directory named "Indexing_Outputs" which contains 3 files:
   - Unigrams.txt - containing unigrams of all the tokens from 1000 output
                    files in "Tokenization_Outputs" folder along with Document IDs
                    of the documents in which it was found and corresponding
                    term frequency in that document.

   - Bigrams.txt  - containing bigrams of all the tokens from 1000 output
                    files in "Tokenization_Outputs" folder along with Document IDs
                    of the documents in which it was found and corresponding
                    term frequency in that document.

   - Trigrams.txt - containing trigrams of all the tokens from 1000 output
                    files in "Tokenization_Outputs" folder along with Document IDs
                    of the documents in which it was found and corresponding
                    term frequency in that document.

5) A directory named "Frequency_Tables" which contains 6 files:
   - Unigrams_Term_Frequency_Table.txt
     - contains unigrams and corresponding total of term frequencies of each unigram
       using Task 2 output

   - Unigrams_Document_Frequency_Table.txt
     - contains unigrams, list of Document IDs of the documents in which it was found
       and its corresponding document frequency

   - Bigrams_Term_Frequency_Table.txt
     - contains bigrams and corresponding total of term frequencies of each bigram
       using Task 2 output

   - Bigrams_Document_Frequency_Table.txt
     - contains bigrams, list of Document IDs of the documents in which it was found
       and its corresponding document frequency

   - Trigrams_Term_Frequency_Table.txt
     - contains trigrams and corresponding total of term frequencies of each trigram
       using Task 2 output

   - Trigrams_Document_Frequency_Table.txt
     - contains trigrams, list of Document IDs of the documents in which it was found
       and its corresponding document frequency

6) A file "Global_statistics.txt" containing total number of unigrams, bigrams and trigrams

7) A file "Stop_Words.txt" containing a list of stop words with appropriate explanation

Setup :

- You should have a Python programming environment set up on your machine.


Run the code:

- Run from your Terminal or Comand Prompt.

- For performing Task 1
  Go to to the directory where task1.py resides and use the command
  > python task1.py
  to run.

  Type 1,2,3 or 4 depending on whether you wish to perform depunctuation and/or case-folding
  and press Enter

- For performing Task 2
  Go to to the directory where task2.py resides and use the command
  > python task2.py
  to run.

- For performing Task 3
  Go to to the directory where task3.py resides and use the command
  > python task3.py
  to run.

Results:

The results for Task 1 are generated in "Tokenization_Outputs" directory
The results for Task 2 are generated in "Indexing_Outputs" directory
The results for Task 3 are generated in "Frequency_Tables" directory
The file "Global_statistics.txt" is generated in Task 2

DESIGN CHOICES:

General:

- While naming files according to its URL, some URLs had '/' in it, which couldnt
  be kept as file name as it is invalid. So, each '/' in the URL has been replaced by '_'
  Eg. For saving raw html of "https://en.wikipedia.org/wiki/C/2011_W3_(Lovejoy)""
      the name given to the file is "C_2011_W3_(Lovejoy)""

Task 1:

- For running Task 1, the options for depunctuation and case-folding are provided to the
  user by asking to choose option by pressing 1,2,3 or 4 where:

  Enter 1 if you want to perform both case-folding and punctuation handling
  Enter 2 if you want to perform just case-folding
  Enter 3 if you want to perform just punctuation handling
  Enter 4 if you dont want to perform case-folding or punctuation handling

  Any other input shows message as "Invalid input"

- As special symbols are denoted differently in UTF-8 format, for eg like '\xe2',
  they are chose to be removed

- If the token starts with '$' '+' '.' or '-' the respective punctuation is not stripped

- If the token ends with '+' or '%' the respective punctuation is not stripped

- If a token contains only numbers and punctuations, following things are 
  taken care of even if depunctuation is to be done:

  1) '.' and '-' within the numbers are all preserved always
     Eg. 245.56 27-12-1994
  2) If the number starts with '$' '+' '.' or '-' and ends with '+' or '%'
     both the start and end punctuations are preserved, rest start/end punctuations are replaced by space
     Eg. +50% $250+
  3) If the number just starts with '$' '+' '.' or '-' and does not end with '+' or '%'
     only the start punctuation is preserved, rest start/end punctuations are replaced by space
     Eg. $500 -20.5
  4) If the number does not start with '$' '+' '.' or '-' and just ends with '+' or '%'
     only the end punctuation is preserved, rest start/end punctuations are replaced by space
     Eg. 25% 100+

Task 2:

- Each output file contains each entry as:
  term -> (docID1,tf1) (docID2,tf2) .... (docIDn,tfn)
  where tf1 is term frequency of term in docID1
  Eg. enumerating -> (Hurricane_Janet,1) (New_York_City,2)

- Along with generation of output files "Unigrams.txt", "Bigrams.txt" and "Trigrams.txt", of Task 2,
  "Trigrams_Document_Frequency_Table.txt" which contains document frequency table of trigrams (Task 3 deliverable)
   is also generated in Task 2 due to the following reason:
  - The trigrams document frequency table is not possible to store in a dictionary because of high number
    of trigrams and corresponding list of document IDs (given MemoryError if tried to). So, this table is
    generated in runtime by writing into file while traversing the list of trigrams without storing
  - Format : Term -> List of Document ID(s) -> Document Frequency
    Eg. officials opened shelters -> ['Hurricane_Ingrid', 'Hurricane_Matthew'] -> 2

- "Global_statistics.txt" mentions total number of unigrams, bigrams, trigrams

Task 3:

- Format for Term Frequency Table:
  Term -> Sum of all Term frequencies
  Eg. august -> 7260
      hurricane center -> 2780
      of use and -> 1001

- Format for Document Frequency Table:
  Term -> List of Document ID(s) -> Document Frequency
  Eg. disarmed -> ['Mexico', 'World_War_II'] -> 2
      $10,000 in -> ['Hurricane_Georges', 'Lewes,_Delaware'] -> 2