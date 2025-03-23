


def arithmetic_arranger(problems, show_answers=False):
    line_two = ""
    line_one = ""
    line_three = ""
    line_four = "\n"


    

    if len(problems)>5:
        return("Error: Too many problems.")
    else:

        for i in range(len(problems)) :






            Leer_zeichen = ""
            number_one = problems[i].split()[0] 
            number_two = problems[i].split()[2]
            Rechen_zeichen = problems[i].split()[1]
            number_four = ""
            

            if len (number_one)>=5 or len(number_two) >=5:
                return('Error: Numbers cannot be more than four digits.')




            if Rechen_zeichen != "+" and Rechen_zeichen !=  "-":
                return("Error: Operator must be '+' or '-'.")

            try:
                int(number_one)
                int(number_two)
            except:
                return("Error: Numbers must only contain digits.")
            





                
            if show_answers == True:
                
                if Rechen_zeichen == "+": 
                    number_four = str(int(number_one) + int(number_two))  
                elif Rechen_zeichen == "-":
                    number_four = str(int(number_one) - int(number_two))

        
            
                
            max_breite = max(len(number_one),len(number_two))

            for x in range(max_breite):
                Leer_zeichen += "-"



            line_one += f"{number_one:>{2+max_breite}}    "
            line_two += f"{Rechen_zeichen} {number_two:>{max_breite}}    "
            line_three += f"--{Leer_zeichen:>{max_breite}}    "
            line_four += f"{number_four:>{2+max_breite}}    "
                


        



            

        return(f"{line_one.rstrip()}\n{line_two.rstrip()}\n{line_three.rstrip()}{line_four.rstrip()}")


    



#print(repr(f'{arithmetic_arranger(["32 + 698", "3801 - 23", "45 + 43", "123 + 49"], True)}'))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))