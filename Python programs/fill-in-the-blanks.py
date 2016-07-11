
# list containing paragraph of each level
Paragraph = ['''A __1__ is something that holds a value that may change.
 In simplest terms, a __1__ is just a box that you can put stuff in.
 __2__ of the __1__ is always on the left side of the __4__ sign ,
  and the __3__ of the __1__ on the right side of the __4__ sign ''',
  '''__1__ is a high level language. __1__ was created by Guido van Rossum. To print anything in __1__ we use __2__ statement. __3__ is a data type in __1__ which is used to store  sequence of character. __4__ is a function which is used to convert a sentence in to __5__  of __3__''',
  ''' __1__ is a __2__ language. Which is used to make __3__ pages.
  __1__ document is composed of __1__ __4__ and __1__ __5__ define the type of __1__ __4__ and they begin with '__6__' symbol and end with '__7__' symbol.
  ''']



# list containing answer of each level
check_list= [['easy',['variable' , 'name' , 'value' , 'equal']],['medium',['python','print','string','split()','list']],
['hard',['html','markup','web','elements','tags','<','>']]]




""" Function Name: input_level()
	INPUT: Nothing
	OUTPUT: user input for level
	Behaviour: check user input for level is correct or not"""		
def input_level():
	print "Please select a difficulty level by typing in it"
	print 'Your option is Easy, Medium and hard'
	level = raw_input()
	if level not in ['Easy','easy','Medium','medium','Hard','hard']:
		print 'That is not an option!'
		return input_level()
	print 'You selects ' + level + '!'
	return level



""" Function Name: input_guesses()
	INPUT: Nothing
	OUTPUT: user input of guesses
	Behaviour: check user input for guesses is integer or not"""	
def input_guesses():
	print 'How many guesses would you like per problem?'
	guesses = raw_input("Please enter a positive no. ")
	try:
		guesses = int(guesses)
		if guesses < 0:
			print 'Please selects at least one guess'
			return input_guesses()
	except:		
		print 'That is not an integer !'
		return input_guesses()
	return guesses



""" Function Name: word_in_pos(word1, word2)
	INPUT: two words word1 and wod2
     OUTPUT: return word2 if word2 is substring of word1
     Behaviour: check substring"""
def word_in_pos(word1, word2):
    if word2 in word1:
        return word2
    return None


        

"""
Function Name:  upadate_paragraph(ans,ques_num,paragraph)
INPUT: input of the function is user answer, question no. and paragraph which has to be update
OUTPUT : Output is replaced paragraph from which blank string is replaced by ans string 
Behaviour :Replace the blank string by ans string in paragraph. """ 
def upadate_paragraph(ans,ques_num,paragraph):    
    replaced = []
    paragraph = paragraph.split()
    blank = '__' + str(ques_num) + '__'
    for word in paragraph:
        replacement = word_in_pos(word, blank)
        if replacement != None:
            word = word.replace(replacement, ans)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced	


""" Function Name: check_answer(word,check_list,pos)
	INPUT: user answer, list containing answers for paragraph and question no.
	OUTPUT: True or False
	Behaviour: Check answer of user is correct or not"""
def check_answer(word,check_list,pos):
	if word == check_list[pos-1]:
		return True
	else:
		return False




""" Function Name: play_game(guesses)
	INPUT: Take number of guesses that user selects
	OUTPUT: Print game over or you won 
	Behaviour: check user answered correctly or not if yes update paragraph else decrease guesses
	by 1"""
def play_game(guesses):
	ques_num = 1
	# check till all guesses end or game end[guesses,paragraph,]
	while guesses:
		# print the paragraph
		print '\nThe current paragraph reads as such:\n\n' + Paragraph[level] + '\n\n'
		# ask question to user
		ans = raw_input('What should be substituted in for __' + str(ques_num) + '__?  ')
		# check answer is correct or not
		if check_answer(ans,check_list[level][1],ques_num): 
			print '\nCorrect!\n\n'
	        # repalace the blank string with user answer
			Paragraph[level] =  upadate_paragraph(ans,ques_num,Paragraph[level])
			# print won if all question is answered correctly
			if ques_num == total_question:
				print 'The current paragraph reads as such:\n\n' + Paragraph[level] + '\n\nYou Won!\n' 
				return
			ques_num += 1
		# if answer is not correct decrease guesses or print GAME OVER if guesses remain zero	
		else:	
			guesses = guesses - 1
			if guesses == 0:
				print "\nThat isn't the correct answer!  You have " + str(guesses) + " trys left!\n" +'GAME OVER!'
				return
			print "\nThat isn't the correct answer!  Let's try again; you have " + str(guesses) + " trys left!"




# MAIN CODE FOR GAME USING THE FUCTION DEFINE ABOVE




	
level =  input_level()
levels = ['easy','medium','hard','Easy','Medium','Hard']
level = levels.index(level)
# assign level a intger value 
level %= 3
if level == 0:
	total_question = 4
if level == 1:
	total_question = 5
if level == 2:
	total_question = 7
# Take input of guesses
guesses =  input_guesses()
# initialize question number by 1
play_game(guesses)