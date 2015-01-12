
from nltk.tag import tnt
import pickle

from src.postagger import TnTCorpusGenerator
from src.appconfig import ApplicationConfig


#---------------------------------------Global Variables

#-------------------------------------------------------#



def loadMalayalamTaggedCorpus(corpus_file):
    train_data = []
 
    train_data_local = []
    f = open(corpus_file,'r')
    for line in f:
        if line != "":
            st1 = TnTCorpusGenerator.replaceChillu(line)[:-1]
            stList = st1.split("\t")
            if len(stList) == 2 :
                item_tupl = tuple(stList)
                train_data_local.append(item_tupl)
    train_data.append(train_data_local)
    return train_data
    
    
def saveTaggerModelToDisk(tnt_pos_tagger):
    fileRef = open(ApplicationConfig.POS_TAGGER_MODEL_PICKLE_PATH, "wb")
    pickle.dump(tnt_pos_tagger, fileRef)
    fileRef.close()
    


def trainTnTPosTagger():
    
    tnt_pos_tagger = tnt.TnT()
    
    #reload all tagged corpus file - malayalam_corpus.tt
    TnTCorpusGenerator.generateCorpusForTnT()
    
    print("[1/3] Loading the tagged corpus - malayalam_corpus.tt started! " )
    train_data = loadMalayalamTaggedCorpus(ApplicationConfig.MALAYALAM_TAGGED_CORPUS_PATH)
    
    print("[2/3] Training of the POS Tagger Started: Data depth " + str(len(train_data[0])))
    tnt_pos_tagger.train(train_data)
    
    print("[3/3] Writing POS_TAGGER_MODEL to disk. File Name: pos_tagger_model.pickle" )
    saveTaggerModelToDisk(tnt_pos_tagger)
    
    print("Operation -  Train POS Tagger completed. " )
   
   
#trainTnTPosTagger() 
    