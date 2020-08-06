import os
import sqlite3
from character_map import *
from scipy import stats
import numpy as np

path = os.getcwd()

class JapaneseWord():

	def __init__(self, idx = None, romaji = '', hiragana = '', meaning = '', pdf_weight = 100):
		self.idx 		= idx 
		self.romaji 	= romaji.lower()
		self.hiragana 	= ''
		self.meaning 	= meaning
		self.pdf_weight = pdf_weight
		if hiragana == '' :
			self.hiragana = self.translate_to_hiragana()
		else :
			self.hiragana = hiragana


	def translate_to_hiragana(self):
		hiragana_token = self.tokenize(self.romaji)
		if False not in hiragana_token :
			translation = ''
			for token in hiragana_token :
				translation += hiragana_sound_map[token]
			return translation
		else :
			print("Word could not be tokenized ==> ", self.romaji)

	def translate_to_katakan(self):
		pass

	def tokenize(self, string, char_map = 'hiragana'):
		if(string == ''):
			return []
		i = min(3, len(string))
		while(i>=0):
			if(string[:i] in sound_root_map[char_map]) :
				current_str 	= string[:i]
				modified_string = string[i:]
				return [current_str] + self.tokenize(modified_string)
			i = i - 1 

		## Check for sukuon if no match found
		if len(string) > 1:
			if string[0]==string[1]:
				modified_string = string[1:]
				return ['sukuon_tsu'] + self.tokenize(modified_string)

		return [False]




class DatabaseHandler():

	def __init__(self):
		self.conn   = None
		self.cursor = None

	def create_connection(self, db_file):
	    """ create a database connection to a SQLite database """
	    first_time = not os.path.isfile(db_file) 

	    conn = None
	    try:
	        conn = sqlite3.connect(db_file)
	        if first_time :
	        	conn.execute('''CREATE TABLE vocabulary (serial_no integer PRIMARY KEY AUTOINCREMENT, romaji text, hiragana text, meaning text, pdf_weight int, example text)''')

	    except Error as e:
	    	print("Data base connection error")

	    self.conn 	= conn
	    self.cursor	= self.conn.cursor()

	    return self.conn

	def close_connection(self):
		self.conn.close()

	def insert_entries(self, entries):
		for entry in entries :
			romaji  	= entry.romaji
			hiragana 	= entry.hiragana
			meaning		= entry.meaning
			pdf_weight	= entry.pdf_weight
			self.cursor.execute("INSERT INTO vocabulary (romaji, hiragana, meaning, pdf_weight) VALUES (?,?,?,?)", (romaji, hiragana, meaning, pdf_weight))
		self.conn.commit()

	def get_data(self, idx_list = True):
		data_list = []
		data 	  = None
		if idx_list == True :
			self.cursor.execute("SELECT * FROM vocabulary")
		else :
			query_string = "SELECT * FROM vocabulary where serial_no in " + str(tuple(idx_list))
			self.cursor.execute(query_string)
			
		data = self.cursor.fetchall()
		for word in data :
			idx			= word[0]
			romaji 		= word[1]
			hiragana	= word[2]
			meaning 	= word[3]
			pdf_weight	= word[4]
			japanese_word = JapaneseWord(idx, romaji, hiragana, meaning, pdf_weight)
			data_list.append(japanese_word)

		return data_list

	def update_pdf_weights(self, pdf_dict):
		""" Update pdf of given idx """
		""" pdf_list is dict of idx : new weight """
		for idx in pdf_dict :
			weight = pdf_dict[idx]
			self.cursor.execute("UPDATE vocabulary SET pdf_weight = ? WHERE serial_no = ?", (weight,idx) )
		self.conn.commit()


	def get_idx_pdf_dict(self, idx_list):
		data_list = self.get_data(idx_list)
		return {data.idx : data.pdf_weight for data in data_list }


	def get_idx_data_dict(self, idx_list):
		data_list = self.get_data(idx_list)
		return {data.idx : data for data in data_list}

	def get_idx_list(self):
		self.cursor.execute("SELECT serial_no FROM vocabulary")
		data = self.cursor.fetchall()
		idx_list = [word[0] for word in data ]
		return idx_list


class FlashCard():

	def __init__(self, db_file):
		self.db 			= DatabaseHandler()
		self.reverse 		= 0 
		self.quit_flag		= False
		self.pdf_random_gen	= False		
		self.db.create_connection(db_file)
		self.idx_list 		= []
		self.pdf_dict 		= {} 
		self.word_dict 		= {}


	def display_flashcard(self, match_input = True, recieve_input = True):
		quit_flag 	= False

		# update_pdf = {key : value.pdf_weight for key, value in self.word_list.items()}

		while quit_flag == False :
			word_idx 	= self.pdf_random_gen.rvs()
			word 		= self.word_dict[word_idx]
			print("Japanese Word : ", word.romaji)
			check_feedback = input("Enter Meaning (or quit) : ").upper()
			if check_feedback == 'QUIT' :
				quit_flag = True
			else :
				if check_feedback == 'Y':
					self.pdf_dict[word_idx] -= 1
				else:
					self.pdf_dict[word_idx] += 1
				print("Answer : ", word.meaning , "\n")
			self.spaced_repetition_random()

		print(self.pdf_dict)
		print(self.word_dict)
		self.db.update_pdf_weights(self.pdf_dict)


	def insert_word(self):
		word_list = []
		exit_write_mode = False
		while exit_write_mode == False :
			word = input("Enter Japanese word or 'quit' : ")   # use self.input_msg in future for english compatibility
			if word.upper() == 'QUIT':
				exit_write_mode = True
			else :
				# wd = self.additional_data(word)
				wd = JapaneseWord(romaji = word)
				print("Hiragana : ", wd.hiragana)
				meaning = input("Meaning : ")
				wd.meaning = meaning
				word_list.append(wd)

		self.db.insert_entries(word_list)

	def meaning_match(self):
		return True
	# def additional_data(self, word):
	# 	wd = JapaneseWord(romaji = word)
	# 	print("Hiragana : ", wd.hiragana)

	def start_flash(self):
		idx_list = self.db.get_idx_list()

		### choose last index or random index based on choice
		### modify idx_list

		num = int(input("Number of last words you want to revise ( enter 0 for all / -1 for random) : "))
		random_idx_list = idx_list

		if num != -1 : 
			random_idx_list =  idx_list[-1*num:]
		else :
			practice_count 	= int(input("Enter number of random words you want to practise"))
			random_idx_list = random.sample(idx_list, practice_count) 

		self.load_data_from_db(random_idx_list)
		self.spaced_repetition_random()
		self.display_flashcard()

	def load_data_from_db(self, idx_list):
		## word_list_set would be tuple of (pdf_value, word_object)
		""" zip splits list of tuples into two individual lists"""
		self.idx_list 	= idx_list			
		self.pdf_dict 	= self.db.get_idx_pdf_dict(idx_list)
		self.word_dict 	= self.db.get_idx_data_dict(idx_list)			

	def spaced_repetition_random(self):
		if(self.pdf_dict != {} ):
			idx_list , pdf_list = zip(*self.pdf_dict.items())
			pdf_list = np.array(pdf_list)/sum(pdf_list)		## Ensure sum(pdf_list) != 0
			self.pdf_random_gen = stats.rv_discrete(name='discrete_gen', values=(idx_list, pdf_list))
		else :
			print("PMF generation failed")

	
	def load_from_file(self, filename):
		fp 		= open(filename,'r')
		word_list 	= []
		for line in fp :
			word, meaning = line.split(':',1)
			word 	= word.lower()
			meaning = meaning.upper().strip()

			wd = JapaneseWord(romaji = word)
			wd.meaning = meaning

			word_list.append(wd)

		fp.close()

		self.db.insert_entries(word_list)



# if __name__ == '__main__':

# db = DatabaseHandler()

# english_vocab_path	= path + '/db/' + "english_vocab.db"
japanese_vocab_path = path + '/' + "japanese_vocab.db"
japanese_vocab_path = path + '/' + "japanese_vocab_practice.db"


# word_list = ['otto', 'kitte', 'kekka', 'nikki' , 'gakki', 'zasshi', 'kesseki' ]

# for word in word_list:
# 	jw = JapaneseWord(romaji = word)
# 	print(jw.hiragana)

flash_card = FlashCard(japanese_vocab_path)
flash_card.start_flash()

# # # flash_card.insert_word()
# flash_card.load_from_file('/Users/sushilsrivastava/Documents/chandra/Double_pendulum/jap_voc_test.txt')

# import numpy as np
# xk = np.array([1,3,8,9,10,11,25])
# pk = [20,10,50,5,10,0,5]
# pk = np.array(pk)/sum(pk)


# # stats.rv_discrete()

# custm = stats.rv_discrete(name='custm', values=(xk, pk))

# import matplotlib.pyplot as plt

# # fig, ax = plt.subplots(1, 1)
# # ax.plot(xk, custm.pmf(xk), 'ro', ms=12, mec='r')
# # ax.vlines(xk, 0, custm.pmf(xk), colors='r', lw=4)
# # plt.show()

# R = custm.rvs(size=100)
# print(len(R))


# print(R)

# plt.hist(R,7)
# plt.show()















# conn = db.create_connection(japanese_vocab_path)




# c = conn.cursor()

# c1 = {'romaji' : 'shigoto' , 'hiragana' : 'しごと' , 'meaning' : 'work' , 'pdf_weight' : 1}
# c2 = {'romaji' : 'kaisha' , 'hiragana' : 'かいしや' , 'meaning' : 'company' , 'pdf_weight' : 2}
# c3 = {'romaji' : 'denwa' , 'hiragana' : 'でんわ' , 'meaning' : 'phone call' , 'pdf_weight' : 4}
# db.insert_entries([c1,c2,c3])

# print(db.get_data())
# print(db.get_data([1,3,7]))

# db.update_pdf_weights([(1,-4),(3,100),(8,50)])

# print(hiragana_dict)

# db.close_connection()

# # Create table
# c.execute('''CREATE TABLE stocks
#              (date text, trans text, symbol text, qty real, price real)''')

# # Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# # Save (commit) the changes
# conn.commit()

# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# conn.close()



# t = ('RHAT',)
# c.execute('SELECT * FROM stocks WHERE symbol=?', t)
# print(c.fetchone())

