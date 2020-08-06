

hiragana_dict = { 	  'あ' : 'a'  , 'い' : 'i / ee' , 'う' : 'u / ooo' , 'え' : 'e / ae' , 'お' : 'o',
					  'か' : 'ka' , 'き' : 'ki' , 'く' : 'ku' , 'こ' : 'ko' , 'け' : 'ke',
					  'が' : 'ga' , 'ぎ' : 'gi' , 'ぐ' : 'gu' , 'げ' : 'ge' , 'ご' : 'go',
					  'さ' : 'sa' , 'し' : 'shi', 'す' : 'su' , 'せ' : 'se' , 'そ' : 'so',
					  'た' : 'ta' , 'ち' : 'chi', 'つ' : 'tsu', 'て' : 'te' , 'と' : 'to',
					  'だ' : 'da' , 'ぢ' : 'ji' , 'づ' : 'zu' , 'で' : 'de' , 'ど' : 'do',
					  'な' : 'na' , 'に' : 'ni' , 'ぬ' : 'nu' , 'ね' : 'ne' , 'の' : 'no',
					  'は' : 'ha' , 'ひ' : 'hi' , 'ふ' : 'fu' , 'へ' : 'he' , 'ほ' : 'ho',
					  'ぶ' : 'bu' ,
					  'ま' : 'ma' , 'み' : 'mi' , 'む' : 'mu' , 'め' : 'me' , 'も' : 'mo',
					  'や' : 'ya' , 'ゆ' : 'yu' , 'よ' : 'yo' ,
					  'ら' : 'la/ra' , 'り' : 'li/ri' , 'る' : 'lu/ru' , 'れ' : 'le/re' , 'ろ' : 'lo/ro' ,
					  'わ' : 'wa', 'を' : 'oh' , 'ん' : 'n'
				}



hiragana_vocab_dict = {'あ' :'a'  , 'い' : 'i'  , 'う' : 'u'  , 'え' : 'e'  , 'お' : 'o' ,
					  'か' : 'ka' , 'き' : 'ki' , 'く' : 'ku' , 'こ' : 'ko' , 'け' : 'ke',
					  'が' : 'ga' , 'ぎ' : 'gi' , 'ぐ' : 'gu' , 'げ' : 'ge' , 'ご' : 'go',
					  'さ' : 'sa' , 'し' : 'shi', 'す' : 'su' , 'せ' : 'se' , 'そ' : 'so',
					  'ざ' : 'za' , 'じ' : 'ji' , 'ず' : 'zu' , 'ぜ' : 'ze' , 'ぞ' : 'zo',
					  'た' : 'ta' , 'ち' : 'chi', 'つ' : 'tsu', 'て' : 'te' , 'と' : 'to',
					  'だ' : 'da' , 'ぢ' : 'ji' , 'づ' : 'zu' , 'で' : 'de' , 'ど' : 'do',
					  'な' : 'na' , 'に' : 'ni' , 'ぬ' : 'nu' , 'ね' : 'ne' , 'の' : 'no',
					  'は' : 'ha' , 'ひ' : 'hi' , 'ふ' : 'fu' , 'へ' : 'he' , 'ほ' : 'ho',
					  'ば' : 'ba' , 'び' : 'bi' , 'ぶ' : 'bu' , 'べ' : 'be' , 'ぼ' : 'bo',
					  'ま' : 'ma' , 'み' : 'mi' , 'む' : 'mu' , 'め' : 'me' , 'も' : 'mo',
					  'や' : 'ya' , 'ゆ' : 'yu' , 'よ' : 'yo' ,
					  'ら' : 'ra' , 'り' : 'ri' , 'る' : 'ru' , 'れ' : 're' , 'ろ' : 'ro',
					  'わ' : 'wa' , 'を' : 'oh' , 'ん' : 'n'	 ,
					  'ぱ' : 'pa' , 'ぴ' : 'pi' , 'ぷ' : 'pu' , 'ぺ' : 'pe' , 'ぽ' : 'po',
					  'きや' : 'kya' , 'きゆ' : 'kyu' , 'きよ' : 'kyo', 
					  'しや' : 'sha' , 'しゆ' : 'shu' , 'しよ' : 'sho',
					  'ちや' : 'cha' , 'ちゆ' : 'chu' , 'ちよ' : 'cho',					  
					  'にや' : 'nya' , 'にゆ' : 'nyu' , 'によ' : 'nyo',
					  'ひや' : 'hya' , 'ひゆ' : 'hyu' , 'ひよ' : 'hyo',
					  'みや' : 'mya' , 'みゆ' : 'myu' , 'みよ' : 'myo',
					  'りや' : 'rya' , 'りゆ' : 'ryu' , 'りよ' : 'ryo',
					  'ぎや' : 'gya' , 'ぎゆ' : 'gyu' , 'ぎよ' : 'gyo',	
					  'じや' : 'ja'  , 'じゆ' : 'ju'  , 'じよ' : 'jo' ,
					  'びや' : 'bya' , 'びゆ' : 'byu' , 'びよ' : 'byo',
					  'ぴや' : 'pya' , 'ぴゆ' : 'pyu' , 'ぴよ' : 'pyo',
					  'っ'   : 'sukuon_tsu'									##	Small tsu for sukuon		  					  						  				  					  					  					  
					}

# sukuon = {'tsu' : 'っ' }   ##	Small tsu for sukuon

hiragana_sound_map = { value : key for key, value in hiragana_vocab_dict.items()}
# katakana_sound_map = [katakana_vocab_dict[keys] for keys in katakana_vocab_dict.keys()]

sound_root_map = {'hiragana' : hiragana_sound_map.keys()}

