from src.appconfig import ApplicationConfig

import nltk
from nltk.tag import tnt
import pickle

#---------------------------------------Global Variables
TNT_POS_TAGGER = tnt.TnT()
#-------------------------------------------------------#
           
def loadPOSTaggerModelFromDisk():
    fileRef = open(ApplicationConfig.POS_TAGGER_MODEL_PICKLE_PATH, "rb")
    tnt_pos_tagger = pickle.load(fileRef)
    fileRef.close()
    return tnt_pos_tagger
    
    
def performPOSTagging(tokenList):
    #tokenList = nltk.word_tokenize("അകത്തി അടിമയായിത്തീരുക നശിക്കുക അരികെ പാളി ഉച്ചത്തിലുള്ള യായിത്")
    tnt_pos_tagger = loadPOSTaggerModelFromDisk()
    taggedOutput = tnt_pos_tagger.tag(tokenList)
    return taggedOutput

    
# ------------------------- TESTING MODULE ------------#
    
def testPosTagging():
    tokenList = nltk.word_tokenize("അകത്തി അടിമയായിത്തീരുക നശിക്കുക അരികെ പാളി ഉച്ചത്തിലുള്ള യായിത്")
    performPOSTagging(tokenList)

#testPosTagging()