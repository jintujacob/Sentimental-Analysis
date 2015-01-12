
"""5 movies which has 5 files to store their review....when review button is click..then the file content copies to  new """

import tkinter
import os

#global variables
MASTER = tkinter.Tk()
REVIEW_CONTENT_RAW = []
REVIEWS_SEL_FILM = []


#function defenitions
def getReviewFileName(filmNum):
    basepath = os.path.abspath("..").split("/src")
    filepath = basepath[0] + "/resources/reviews"
    filename = filepath + "/review_film" + str(filmNum) +".txt";
    return filename


def loadReviewContents():
    global REVIEW_CONTENT
    for i in range(1,6):
        f = open(getReviewFileName(i), mode='r')
        fileContent = f.read().split("\n")
        REVIEW_CONTENT_RAW.append(fileContent)
    
def getFilmName(filmIndex):
    content = REVIEW_CONTENT_RAW[filmIndex]
    fTitle = content[0]
    return fTitle 

def getReviewListByMovie(filmIndex):
    reviewList = REVIEW_CONTENT_RAW[filmIndex]
    return reviewList

def setReviewsForSelectedFilm(filmIndex):
    global REVIEWS_SEL_FILM
    REVIEWS_SEL_FILM = getReviewListByMovie(filmIndex) 
    #print(REVIEWS_SEL_FILM)

def getReviewsForSelectedFilm():
    return REVIEWS_SEL_FILM

def populateUI():
    loadReviewContents()
    tkinter.Button(MASTER, text=getFilmName(0), 
                   command=buttonClickActionforFilm1).grid(row=1, column=0, sticky=tkinter.W, pady=4)
    tkinter.Button(MASTER, text=getFilmName(1), 
                   command=buttonClickActionforFilm2).grid(row=2, column=0, sticky=tkinter.W, pady=4)
    tkinter.Button(MASTER, text=getFilmName(2), 
                   command=buttonClickActionforFilm3).grid(row=3, column=0, sticky=tkinter.W, pady=4)
    tkinter.Button(MASTER, text=getFilmName(3), 
                   command=buttonClickActionforFilm4).grid(row=4, column=0, sticky=tkinter.W, pady=4)
    tkinter.Button(MASTER, text=getFilmName(4), 
                   command=buttonClickActionforFilm5).grid(row=5, column=0, sticky=tkinter.W, pady=4)
    tkinter.mainloop()
    
    return getReviewsForSelectedFilm()
    
    
def buttonClickActionforFilm1():
    global MASTER
    setReviewsForSelectedFilm(0)
    MASTER.destroy()
    
def buttonClickActionforFilm2():
    setReviewsForSelectedFilm(1)
    MASTER.destroy()

def buttonClickActionforFilm3():
    setReviewsForSelectedFilm(2)
    MASTER.destroy()
    
def buttonClickActionforFilm4():
    setReviewsForSelectedFilm(3)
    MASTER.destroy()
 
def buttonClickActionforFilm5():
    setReviewsForSelectedFilm(4)
    MASTER.destroy()
    


#control logic
"""

x = populateUI()
print(x)
"""

          

