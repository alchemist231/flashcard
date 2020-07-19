import os
import sqlite3
import character_map

path = os.getcwd()

# class JapaneseWordMap():

# 	def __init__(self, idx = None, romaji = '', hiragana = '', meaning = '', pdf_weight = 0):
# 		self.

# 	def return 


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
	        	conn.execute('''CREATE TABLE vocabulary (serial_no integer PRIMARY KEY AUTOINCREMENT, romaji text, hiragana text, meaning text, pdf_weight int)''')

	    except Error as e:
	        print(e)

	    self.conn 	= conn
	    self.cursor	= self.conn.cursor()

	    return self.conn

	def close_connection(self):
		self.conn.close()

	def insert_entries(self, entries):
		for entry in entries :
			romaji  	= entry['romaji']
			hiragana 	= entry['hiragana']
			meaning		= entry['meaning']
			pdf_weight	= entry['pdf_weight']
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
			data_entry 	= {}
			data_entry['romaji'] 		= word[1]
			data_entry['hiragana']		= word[2]
			data_entry['meaning'] 		= word[3]
			data_entry['pdf_weight']	= word[4]
			data_list.append(data_entry)

		return data_list

	def update_pdf_weights(self, )







# def FlashCard():

# 	def __init__(self):




# 	def randomize ## (key : meaning)
# 		based on pdf
# 		# check pdf used or not , if no , pdf random, with no pdf update





# if __name__ == '__main__':

db = DatabaseHandler()

english_vocab_path	= path + '/db/' + "english_vocab.db"
japanese_vocab_path = path + '/' + "japanese_vocab.db"


conn = db.create_connection(japanese_vocab_path)




# c = conn.cursor()

# c1 = {'romaji' : 'shigoto' , 'hiragana' : 'しごと' , 'meaning' : 'work' , 'pdf_weight' : 1}
# c2 = {'romaji' : 'kaisha' , 'hiragana' : 'かいしや' , 'meaning' : 'company' , 'pdf_weight' : 2}
# c3 = {'romaji' : 'denwa' , 'hiragana' : 'でんわ' , 'meaning' : 'phone call' , 'pdf_weight' : 4}
# db.insert_entries([c1,c2,c3])

print(db.get_data())
print(db.get_data([1,3,7]))
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

