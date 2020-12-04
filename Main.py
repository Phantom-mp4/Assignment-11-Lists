#=- Problem 1 -=#

    #Songs = ["Song1", "Song2", "Song3", "Song4", "Song5"]

    #print(Songs[4])
    #print(Songs[3])
    #print(Songs[2])
    #print(Songs[1])
    #print(Songs[0])

    #print(Songs[0])
    #print(Songs[1])
    #print(Songs[2])
    #print(Songs[3])
    #print(Songs[4])

#=- Problem 2 -=#

    #Songs = ["Song1", "Song2", "Song3", "Song4", "Song5"]

    #for x in Songs:
        #print(x)

#=- Problem 3 -=#

    #Songs = ["Song1", "Song2", "Song3", "Song4", "Song5"]

    #Songs.remove("Song5")

    #Songs.insert(2, "NewSong")

    #print(Songs)

#=- Problem 4 -=#

    #Songs = ["Song1", "Song2", "Song3", "Song4", "Song5"]

    #Variable = (4)

    #for x in Songs:
        #print(x)

    #print(" ")

    #while Variable >= 0:
        #print(Songs[Variable])

        #Variable -= 1

#=- Problem 5 -=#

    #Songs = ["Song1", "Song2", "Song3", "Song4", "Song5"]

    #SongsLength = len(Songs)

    #Half = SongsLength//2

    #print(Songs[0:Half])
    #print(" ")
    #print(Songs[Half:SongsLength])

#=- Problem 6 -=#

    #NumberList = [11, 22, 33, 44, 55, 66, 77]

    #Variable = 0 

    #Length = len(NumberList)

    #while Variable <= Length:
        #if NumberList[Variable] % 2 == 0:
            #print(NumberList[Variable])

        #Variable += 1

#=- Problem 7 -=#
    #Max = 7

    #InputList = ""

    #Length = "0"

    #NumberList = [11, 22, 33, 44, 55, 66, 77]

    #while Length <= Max:
        #InputList = int(input("Input a number. "))
        #Length += 1

        #if len(InputList) == len(NumberList):
            #print("Both lists are equal size.")
            #break
        
#=- Problem 8 -=#


    #NumberList = [11, 22, 33, 44, 55, 66, 77]

    #Variable = 0 

    #Length = len(NumberList)

    #while Variable <= Length:
        #if NumberList[Variable] % 2 == 0:
            #print(NumberList[Variable], "Is even.")
            #Variable += 1

        #else:
            #print(NumberList[Variable], "Is odd.")
            #Variable += 1

#=- Problem 9 -=#

    #NumberList = [5, 9, 4, 7, 9, 2, 9, 9, 6]

    #NumberSum = sum(NumberList, 0)

    #print("The sum is", NumberSum)

    #NumberAdverage = NumberSum / len(NumberList)

    #print("The adverage is", NumberAdverage)

#=- Problem 10 -=#

    #NumberList = [5, 9, 4, 7, 9, 2, 9, 9, 6]

    #Variable = 0 

    #Length = len(NumberList)

    #NumbersNine = 0

    #while Variable <= Length:
        #if NumberList[Variable] == 9:
            #NumbersNine += 1
            #Variable += 1

    #print(NumbersNine, "of the numbers are nines.")

    #print(Length - NumbersNine, "of the numbers are not nines.")

#=- Problem 11 -=#

    #NumberList = [5, 9, 4, 7, 9, 2, 9, 9, 6]

    #Even = 0

    #Odd = 0

    #Length = len(NumberList)

    #Number = 0

    #while Number <= Length:
        #if Number[Number] % 2 == 0:
            #Even += 1
            #Number += 1
        #else:
            #Odd += 1
            #Number += 1

    #print(Even, "Are even.")

    #print(Odd, "Are odd.")