count_of_progress=0
count_of_trailing=0
count_of_retriever=0
count_of_excluded=0

passed = 0
defer = 0
fail = 0


def do():
    print("\n" "----------------------TRY AGAIN----------------------")                        

def progres_report():                                                                 #this function will help to find the progress of every student 
    if passed==120:
        print("\n" "student progression is 'Progress' ")
    elif passed==100:
        print("\n" "student progression is 'Progress – module trailer' ")
    elif fail>=80:
        print("\n" "student progression is 'Exclude' ")
    else:
        print("\n" "student progression is 'Do not progress – module retriever' ")
 

while True:
    print("\n" "-------------------------------------------WELCOME-------------------------------------------")
    print("\n" "this program will help you to predict progression outcomes for multiple students." "\n")
    x=input("if you want to end the program enter q(lower case letter) or enter any other keys:")
    if x!="q":
            try:
                passed=int(input("\n" "enter your pass Credits:"))
                if passed not in range(0,121,20):
                    print("\n" "Range error")
                    do()
                    continue
                defer=int(input("enter your defer credits:"))
                if defer not in range(0,121,20):
                    print("\n" "Range error")
                    do()
                    continue
                fail=int(input("enter your fail credits:"))
                if fail not in range(0,121,20):
                    print("\n" "Range error ")
                    do()
                    continue
                else:
                    
                    total=passed+defer+fail

                if total==120:
                     progres_report()
                    
                else:
                    print("\n" "Total incorrect")
                    do()
            except ValueError:
                    print("\n" "Integers required")
                    do()
    if x=="q":
        
         print("\n" "Progress",count_of_progress,":",end = "" );
         for i in range (0,count_of_progress):
             Progress = "*";
             print(Progress,end="");
             
    
         print("\n" "Trailing",count_of_trailing,":",end = "" );
         for i in range (0,count_of_trailing):
             Trailing = "*";
             print(Trailing,end="");
            

         print("\n" "Retriver",count_of_retriever,":",end = "" );
         for i in range (0,count_of_retriever):
             Retriver = "*";
             print(Retriver,end ="");
                    
        
         print("\n" "Exclude",count_of_excluded," " ":",end = "" );
         for i in range (0,count_of_excluded):
             Exclude = "*";
             print(Exclude,end="");

         count_of_total = count_of_progress + count_of_trailing + count_of_retriever + count_of_excluded
         print("\n""\n",count_of_total,"outcomes in total.")

         print("\n" "meet you soon ")
         print("\n" "----------------------------------------------END--------------------------------------------------")
         break


    

        
