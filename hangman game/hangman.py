from random import randint
from SimpleGraphics import *

def hangmangraphics(chances):
	MakeWindow(10,10,bgcolor=BLACK)
	if chances == 7:
		DrawLineSeg(5,10,5,6,Linecolor=WHITE,Linewidth=2)
	if chances == 6:
		DrawLineSeg(5,10,5,6,Linecolor=WHITE,Linewidth=2)
		DrawDisk(5,4,2,Linecolor=WHITE,Linewidth=2)
	ShowWindow(time=2000)



if __name__ == '__main__':
	with open('/Users/pranavjain/Documents/hangman game/countries.txt', 'r') as f:
	    content=f.readlines()
	list_string=[]
	random_number=randint(1,201)
	string=content[random_number]
	string=string.lower()
	length=len(string)
	chances=7
	history=""
	counter=1
	for i in range(0,length-1):
		if(string[i]==" "):
			list_string=list_string + list(" ")
		else:
			list_string=list_string + list("_")


	while(counter<=7):
		if(chances==1):
			print("\n\nYou have", chances, "chance left")
		else:
			print("\n\nYou have", chances, "chances left")
		if(history!=""):
			print("You have used the following letters:",history)
		else:
			print(''.join(list_string))
		letter=input(("Enter a letter: "))
		letter=letter.lower()
		
		while(letter.isalpha()==False or len(letter)!=1):
			letter=input("Please enter a single alphabet: ")

		while(letter in history or (letter.isalpha()==False or len(letter)!=1)):
			letter=input("This letter has already been used. Please enter a different letter: ")
		for i in range(0,length):
			if(string[i]==letter):
				list_string[i]=letter
		if(letter not in string):
			chances=chances-1
			counter=counter+1
		s=''.join(list_string)
		print("\n",s)
		history=history + letter + ","
		if("_" not in s):
			break
		MakeWindow(50,50,bgcolor=BLACK)
		if chances == 7:
			DrawLineSeg(25,50,25,45,LineColor=WHITE,LineWidth=2)
		elif chances == 6:
			DrawLineSeg(25,50,25,45,LineColor=WHITE,LineWidth=2)
			DrawDisk(25,40,5,EdgeColor=WHITE,EdgeWidth=2)
		elif chances == 5:
			DrawLineSeg(25,50,25,45,LineColor=WHITE,LineWidth=2)
			DrawDisk(25,40,5,EdgeColor=WHITE,EdgeWidth=2)
			DrawLineSeg(25,35,25,15,LineColor=WHITE,LineWidth=2)
		elif chances == 4:
			DrawLineSeg(25,50,25,45,LineColor=WHITE,LineWidth=2)
			DrawDisk(25,40,5,EdgeColor=WHITE,EdgeWidth=2)
			DrawLineSeg(25,35,25,15,LineColor=WHITE,LineWidth=2)
			DrawLineSeg(25,28,15,24,LineColor=WHITE,LineWidth=2)
		elif chances == 3:
			DrawLineSeg(25,50,25,45,LineColor=WHITE,LineWidth=2)
			DrawDisk(25,40,5,EdgeColor=WHITE,EdgeWidth=2)
			DrawLineSeg(25,35,25,15,LineColor=WHITE,LineWidth=2)
			DrawLineSeg(25,28,15,24,LineColor=WHITE,LineWidth=2)
			DrawLineSeg(25,28,35,24,LineColor=WHITE,LineWidth=2)
		elif chances == 2:
			DrawLineSeg(25,50,25,45,LineColor=WHITE,LineWidth=2)
			DrawDisk(25,40,5,EdgeColor=WHITE,EdgeWidth=2)
			DrawLineSeg(25,35,25,15,LineColor=WHITE,LineWidth=2)
			DrawLineSeg(25,28,15,24,LineColor=WHITE,LineWidth=2)
			DrawLineSeg(25,28,35,24,LineColor=WHITE,LineWidth=2)
			DrawLineSeg(25,15,15,8,LineColor=WHITE,LineWidth=2)
		elif chances == 1:
			DrawLineSeg(25,50,25,45,LineColor=WHITE,LineWidth=2)
			DrawDisk(25,40,5,EdgeColor=WHITE,EdgeWidth=2)
			DrawLineSeg(25,35,25,15,LineColor=WHITE,LineWidth=2)
			DrawLineSeg(25,28,15,24,LineColor=WHITE,LineWidth=2)
			DrawLineSeg(25,28,35,24,LineColor=WHITE,LineWidth=2)
			DrawLineSeg(25,15,15,8,LineColor=WHITE,LineWidth=2)
			DrawLineSeg(25,15,35,8,LineColor=WHITE,LineWidth=2)
		ShowWindow(2)
		CloseWindow()
	


	if(counter>7):
		print("\nYou Lose")
		print("The country was",string)
	else:
		print("\nYou Won with" , chances , "chances left")





