import random

computerChoice = random.randint(1, 2)

print("Hello, and welcome to a simple game of Heads or Tails!\n")

headsOrTails = input("Which one do you choose? Heads or tails:\t")

headsOrTailsLowercase = headsOrTails.lower()




if headsOrTailsLowercase == "heads":
    print(f'''You chose {headsOrTails}:\n
        _____-----_____
      ..;;;--'~~~`--;;;..
    /;-~IN GOD WE TRUST~-.
   //      ,;;;;;;;;      \\
 .//      ;;;;;    \       \\
 ||       ;;;;(   /.|       ||
 ||       ;;;;;;;   _\      ||
 ||       ';;  ;;;;=        ||
 ||LIBERTY | ''\;;;;;;      ||
  \\     ,| '\  '|><| 1995 //
   \\   |     |      \  A //
    \;.,|.    |      '\.-'/
      \~;;;,._|___.,-;;;~/
       ----''=--'--------
          ''')

    print(f"Computer chose {computerChoice}:\n")
    
else:
    print(f'''You chose {headsOrTails}:\n
                 _.oood"""""""booo._
             _.o""       __        ""o._
           oP"          //\\ E U R O   "Yo
         o8       _.-":||    __ _  _ ___ `8o
        d'     ,-"    :||   |__ |\ |  |    `b
       d'   .-"      :  \\_/|__ | \|  |     `b
      8'     """"":  :                    ,*,`8
     8           :  :                   ,',*,*,8
    ,8           :  :                 ,',',',*,8.
    8'          :  :                ,',',',',* `8
    8           :  :             ____',',','    8
    8          :  :           ,-: /\ :-.        8
    8          :  :         ,',' :"<: `.`.      8
    8.        /   |        /\/  :)"" :  \/\     8
    `8      .'    \       : /`-(__/\ _,-'\ :   8'
     8   _.'       `-.    |:   :----.-: _ :|   8
      8.(_________dd__)   :|  (:     \:__)|:  ,8
       Y.           ,', , ,\._ :":    :/_./  .P
        Y.        ,',',',','`.`:-:__.-:','  ,P
         "8.    ,',',',','    "-\:___/-"  ,8"
           "Y_,*,*,*,','                _P"
             `'"oo_*,*            _oo""'
                  `"""boooooood"""'
          ''')

    print(f"Computer chose {computerChoice}:\n")
    
if computerChoice == 1:
    print('''
        _____-----_____
      ..;;;--'~~~`--;;;..
    /;-~IN GOD WE TRUST~-.
   //      ,;;;;;;;;      \\
 .//      ;;;;;    \       \\
 ||       ;;;;(   /.|       ||
 ||       ;;;;;;;   _\      ||
 ||       ';;  ;;;;=        ||
 ||LIBERTY | ''\;;;;;;      ||
  \\     ,| '\  '|><| 1995 //
   \\   |     |      \  A //
    \;.,|.    |      '\.-'/
      \~;;;,._|___.,-;;;~/
       ----''=--'--------
          ''')

elif computerChoice == 2:
    print('''
                 _.oood"""""""booo._
             _.o""       __        ""o._
           oP"          //\\ E U R O   "Yo
         o8       _.-":||    __ _  _ ___ `8o
        d'     ,-"    :||   |__ |\ |  |    `b
       d'   .-"      :  \\_/|__ | \|  |     `b
      8'     """"":  :                    ,*,`8
     8           :  :                   ,',*,*,8
    ,8           :  :                 ,',',',*,8.
    8'          :  :                ,',',',',* `8
    8           :  :             ____',',','    8
    8          :  :           ,-: /\ :-.        8
    8          :  :         ,',' :"<: `.`.      8
    8.        /   |        /\/  :)"" :  \/\     8
    `8      .'    \       : /`-(__/\ _,-'\ :   8'
     8   _.'       `-.    |:   :----.-: _ :|   8
      8.(_________dd__)   :|  (:     \:__)|:  ,8
       Y.           ,', , ,\._ :":    :/_./  .P
        Y.        ,',',',','`.`:-:__.-:','  ,P
         "8.    ,',',',','    "-\:___/-"  ,8"
           "Y_,*,*,*,','                _P"
             `'"oo_*,*            _oo""'
                  `"""boooooood"""'
''')