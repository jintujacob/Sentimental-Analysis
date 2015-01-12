# File to hold all the application constants

import os

def getAppRoot():
    return os.path.abspath("..").split("/src")[0]

# global variables




APPLICATION_ROOT = getAppRoot()

RESOURCES_DIR = "/resources"
RESOURCE_PATH_POSTAGGER = APPLICATION_ROOT + RESOURCES_DIR + "/postagger"
RESOURCE_PATH_REVIEWS = APPLICATION_ROOT + RESOURCES_DIR + "/reviews"
RESOURCE_PATH_TOKENIZER = APPLICATION_ROOT + RESOURCES_DIR +  "/tokenizer" 


MALAYALAM_TAGGED_CORPUS_PATH = RESOURCE_PATH_POSTAGGER + "/malayalam_copus.tt"
MALAYALAM_RAW_DATUK_CORPUS_PATH = RESOURCE_PATH_POSTAGGER + "/datuk.corpus"
MALAYALAM_FORMATED_USER_CORPUS_PATH = RESOURCE_PATH_POSTAGGER + "/user.corpus"
POS_TAGGER_MODEL_PICKLE_PATH = RESOURCE_PATH_POSTAGGER+"/pos_tagger_model.pickle"

SCRIPTS_PATH = APPLICATION_ROOT + "/scripts"

