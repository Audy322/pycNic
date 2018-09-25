'''
Created on May 16, 2018

@author: Odelin Charron, Vincent Noblet
'''
import ConfigParser
import StringIO
import os

from mri_processing import Utilities
from mri_processing.MRI_Tools import MRI_viewing


def getAsList(config, Name, section="root"):
    try:
        list0 = config.get(section, Name)[1:-1].split(",\n")
        return [e[1:-1] for e in list0]
    except:
        return None


def getAsBool(config, Name, section="root"):
    try:
        bool0 = config.get(section, Name)
        if bool0 == "True":
            return True
        else:
            return False
    except:
        return None


def getAsString(config, Name, section="root"):
    try:
        str0 = config.get(section, Name)[1:-1]
        return str0
    except:
        return None


def getAsPath(config, Name, section="root"):
    try:
        str0 = config.get(section, Name)[1:-1]
        str0 = os.path.abspath(str0)
        return str0
    except:
        return None


def run(cfgFile):
    '''

    '''
    #=========================================================================
    # Initialization
    #=========================================================================
    print "Reading configuration file : ", cfgFile

    ini_str = '[root]\n' + open(cfgFile, 'r').read()
    ini_fp = StringIO.StringIO(ini_str)
    config = ConfigParser.RawConfigParser()
    config.readfp(ini_fp)

    UseLikertScale = getAsBool(config, "UseLikertScale")
    Overwrite = getAsBool(config, "Overwrite")
    AlwaysReady = getAsBool(config, "AlwaysReady")
    listOfQuestions = getAsList(config, "listOfQuestions")
    dirOfImages = getAsPath(config, "dirOfImages")
    listNameOfTheOtherImages = getAsList(config, "listNameOfTheOtherImages")
    Viewer = getAsString(config, "Viewer")
    csvFilename = getAsString(config, "csvFilename")
    nameMainImage = getAsString(config, "nameMainImage")
    NameOfTheSegmentationFile = getAsString(
        config, "NameOfTheSegmentationFile")

    #=========================================================================
    # Overwrite checking
    #=========================================================================
    CreateCSVQuiz = False
    if os.path.isfile(csvFilename):
        if Overwrite:
            print "Overwrite is set, creating a new quiz..."
            CreateCSVQuiz = True
        else:
            "Previous quiz found ..."
            CreateCSVQuiz = False
    else:
        CreateCSVQuiz = True

    #=========================================================================
    # Viewer selection
    #=========================================================================
    if Viewer == "JIM":
        print "JIM will be used as viewer"
        Viewer = MRI_viewing.ViewImagesUsingJim
    elif Viewer == "ITKSnap":
        print "ITKSnap will be used as viewer"
        Viewer = MRI_viewing.ViewImagesUsingITKsnap
    else:
        print "FSLView will be used as viewer"
        Viewer = MRI_viewing.ViewImagesUsingFSL

    #=========================================================================
    # Quiz creation
    #=========================================================================
    if CreateCSVQuiz:
        print "Finding files..."
        print 4 * " ", "dirOfImages : ", dirOfImages
        print 4 * " ", "nameMainImage : ", nameMainImage
        X_mainImage = Utilities.Find_Name(dirOfImages, nameMainImage)
        if type(X_mainImage) != list:
            X_mainImage = [X_mainImage]

        print "Creating the quiz"
        print 4 * " ", "csvFilename : ", csvFilename
        print 4 * " ", "Working directory : ", os.getcwd()
        MRI_viewing.createCsvQuizz(csvFilename,
                                   X_mainImage,
                                   listOfQuestions)

    print(4 * "*", "Starting the quiz", 4 * "*")
    print 4 * " ", "Working directory : ", os.getcwd()
    print("")
    MRI_viewing.fillCsvFile(csvFilename,
                            range(2, len(listOfQuestions) + 2),
                            Viewer=Viewer,
                            UseLikertScale=UseLikertScale,
                            AlwaysReady=AlwaysReady,
                            ListNameOfTheOtherMRI=listNameOfTheOtherImages,
                            NameOfTheSegmentationMRI=NameOfTheSegmentationFile)

    print(4 * "*", "End of the quiz", 4 * "*")


if __name__ == '__main__':
    print __doc__
    os.chdir("../examples/")
    exampleCfgFile = "cfg_pycNic_example.cfg"
    run(exampleCfgFile)
