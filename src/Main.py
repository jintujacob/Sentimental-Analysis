
from src.gui import UIManager
from src.tokenizer import Tokenizer
from src.postagger import PosTagger, TnTManager


def preLaunch():
    TnTManager.trainTnTPosTagger()

def fetchUserInput():
    # method uses the module - uimanager.py to get the user inputs
    reviewList = UIManager.populateUI()
    filmName = reviewList[0]
    print("[1] Loading the Review comments for processing completed.")
    print("[1.1] Name of the Film :"+ filmName)
    return reviewList

def tokenizeUserInput(filmReviewList):
    print("[2] Tokenization of the Token Review Started")
    tokenList = Tokenizer.doTokenization(filmReviewList)
    print("[2] Tokenization of the Review comments completed. Tokens: "+str(tokenList))
    return tokenList
    
def performPOSTagging(tokenList):
    print("[3] Tagging of the Token List Started")
    taggedTokens = []
    for reviewTokens in tokenList:
        taggedTokens.append(PosTagger.performPOSTagging(reviewTokens))
    print("[3] Tagging of the Token Lis completed. \n[3] Tagged Tokens: "+str(taggedTokens))
    return taggedTokens

def runSentimentalAnalysis():
    # starting point of the sentimental analysis application
    #preLaunch()
    
    #step1 : get the user reviews as a list from uimanager module
    reviewList = fetchUserInput()
    
    #step2 : tokenize the reviews using the tokenizer module
    tokenList = tokenizeUserInput(reviewList[1:len(reviewList)])
    
    #step3 : Pos Tag tokens
    taggedTokens  = performPOSTagging(tokenList) 
    



runSentimentalAnalysis()
    
    
