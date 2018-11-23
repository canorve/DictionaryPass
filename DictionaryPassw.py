#!/usr/bin/env python


import numpy as np
import sys
import os
import stat
import subprocess as sp
import os.path
from astropy.io import fits
import scipy
import scipy.special

import itertools

################
#  main code:  #
################
def main():


    if len(sys.argv[1:]) != 1:
        print ('Missing arguments')
        print ("Usage:\n %s [WordFile] " % (sys.argv[0]))
        print ("Example:\n %s words.txt " % (sys.argv[0]))

        sys.exit()


    InFile= sys.argv[1]


    filhd = open("tempwords.txt", "w")

    filhdin = open(InFile)

    lines = (line.rstrip() for line in filhdin)
    lines = (line.split('#', 1)[0] for line in lines)  # remove comments
        # remove lines containing only comments
    lines = (line.rstrip() for line in lines)
    lines = (line for line in lines if line)  # Non-blank lines

    newword="q"
    newworda=newworde=newwordi=newwordo="w"
    for line in lines:

        (params) = line.split()

        word= params[0]

        linprint="{} \n".format(word)
        filhd.write(linprint)

        newword=word

        flag=False

        for idx, letter in enumerate(word):


            if letter is "a" or letter is "A":

                newworda=word

                newword_list=list(newword)
                newword_list[idx]="4"
                newword=("").join(newword_list)

                newword_list=list(newworda)
                newword_list[idx]="4"
                newworda=("").join(newword_list)


                linprint="{} \n".format(newworda)
                filhd.write(linprint)
                flag=True


            if letter is "o" or letter is "O":

                newwordo=word


                newword_list=list(newword)
                newword_list[idx]="0"
                newword=("").join(newword_list)


                newword_list=list(newwordo)
                newword_list[idx]="0"
                newwordo=("").join(newword_list)

                flag=True



                linprint="{} \n".format(newwordo)
                filhd.write(linprint)

#            newword2=word
            if letter is "e" or letter is "E":

                newworde=word

                newword_list=list(newword)
                newword_list[idx]="3"
                newword=("").join(newword_list)


                newword_list=list(newworde)
                newword_list[idx]="3"
                newworde=("").join(newword_list)

                flag=True


                linprint="{} \n".format(newworde)
                filhd.write(linprint)

#            newword2=word
            if letter is "i" or letter is "I":


                newwordi=word

                newword_list=list(newword)
                newword_list[idx]="1"
                newword=("").join(newword_list)


                newword_list=list(newwordi)
                newword_list[idx]="1"
                newwordi=("").join(newword_list)

                flag=True

                linprint="{} \n".format(newwordi)
                filhd.write(linprint)



        if newword != newworda and newword != newworde and newword != newwordi and newword != newwordo and flag==True:
            linprint="{} \n".format(newword)
            filhd.write(linprint)

    filhdin.close()
    filhd.close()

### second part

    filhdin = open("tempwords.txt")
    filhdout = open("tempwords2.txt", "w")

    lines = (line.rstrip() for line in filhdin)
    lines = (line.split('#', 1)[0] for line in lines)  # remove comments
    lines = (line.rstrip() for line in lines)
    lines = (line for line in lines if line)  # Non-blank lines



    for line in lines:

        (params) = line.split()

        word= params[0]

#        print(line)

#        linprint="{} \n".format(word)
#        filhdout.write(linprint)


        for idx, letter in enumerate(word):

            tot=len(word)

            cont=idx+1
            while(cont <= tot):

                newword=word[idx:cont]
                linprint="{} \n".format(newword)
                filhdout.write(linprint)

                cont=cont+1


    filhdin.close()
    filhdout.close()

###
###

## Include a third part
## uppper case and lower case

##

###################################
####################################


    filhdin = open("tempwords2.txt")
    filhdout = open("wordspassw.txt", "w")

    lines = (line.rstrip() for line in filhdin)
    lines = (line.split('#', 1)[0] for line in lines)  # remove comments
    lines = (line.rstrip() for line in lines)
    lines = (line for line in lines if line)  # Non-blank lines

#    lines, lines2 = itertools.tee(lines)

    lines=list(lines)

    lines2=lines

    for line in lines:

        (params) = line.split()

        word= params[0]

        if (len(word) >= 5):
            linprint="{} \n".format(word)
            filhdout.write(linprint)
#            print(word)


        for line2 in lines2:

            (params2) = line2.split()

            word2= params2[0]

            newword=word+word2

            if (len(newword) >= 5):
                linprint="{} \n".format(newword)
                filhdout.write(linprint)
#                print(newword)

    filhdin.close()
    filhdout.close()



    os.remove("tempwords.txt")
    os.remove("tempwords2.txt")







#############################################################################
######################### End of program  ###################################


#     ______________________________________________________________________
#    /___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/___/_/|
#   |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__/|
#   |_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|/|
#   |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__/|
#   |_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|/|
#   |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__/|
#   |_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|/


##############################################################################

#end of program
if __name__ == '__main__':
    main()
