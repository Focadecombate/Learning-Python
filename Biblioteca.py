###projeto de livraria
###27/02/2019 
###Feito por: Foca_de_combate
print('Welcome to the Library')
name = input("What is your name?\n ").title()
date_today = 8
current_month = "March"
Books = ['elon musk','shung tzu']
welcome_msg = "Hi " + name + ", Welcome Back Today is " + str(date_today) + " of " + current_month
Books.sort()
print(welcome_msg)
print("We have "+ str(len(Books)) +" Books currently avaliable in the Library\n")
print(Books[0].title()+"\n"+Books[1].title()+"\n")
msg3 = "Thank you " + name +" for your time."
Shung_tzu = "Date of first publication: 5th century BC\n"+ "Author: Sun Tzu\n"+"Original language: Mandarin\n"+"Genres: Fiction,self help"
Elon_musk = "Data da primeira publicação: 16 de setembro de 2015\n"+"Author: Ashley Vance\n"+ "Genre: Biography\n"+"Indications: Goodreads Choice Award of the best about Science and Tecnology"
msg2 = input("Would you like to know more information about one of them ?\n ")
if (msg2.lower()) != ('yes'):
        print(msg3)
        exit
else:
        msg4 = input("Please type the name of the book in the list\n ".title())
        msg4=msg4.lower()
        if (msg4.lower()) == ('elon musk'):
                print(Elon_musk)
        elif (msg4.lower()) == ('shung tzu'):
                print(Shung_tzu)
        msg5 = input("Would you like to reserve it?\n")
        if (msg5.lower()) !=("yes"):
                        print(msg3)
                        exit
        else:
                        print("Thanks for using our system.")
                        exit
