'''
Created on May 16, 2018

@author: audy
'''
from mri_processing import Utilities
from mri_processing.MRI_Tools import MRI_viewing
import os

Overwrite = False
CREATECSVQUIZ = True
dir00 = "/home/genu"

'''
/home/genu
/storage/odelin
/home/audy/Work/distant/neur02_storage 
'''
dir0 = dir00 + "/Work/sav_listIDNic_randomized7"
csvFilename = dir0 + "/Nick_randomized7.csv"
n_2DFLAIR = "Flirt_*AX*FLAIR*.nii.gz"
listMRI = ["Flirt_*AX*T1*POST*.nii.gz"]

# Is there any black hole in the DGM ?
listOfQuestions = ["Image quality [0 = bad]",
                   "How easy were the lesions to demarcate ? [0 = hard]",
                   "How easy was the software to use ? [0 = hard]",
                   "How tired are you ? [0 = not tired]",
                   "Is there T2 / FLAIR hyper-intense lesions ? [0 = No]",
                   "Is there FLAIR hypo-intense lesions ? [0 = No]",
                   "Is there Blackhole(s) ? [0 = No]",
                   "Is there Gd enhancing lesions ? [0 = No]",
                   "How much dirty white matter did the patient have ? [0 = low amount]",
                   "Was the registration good ? [0 = bad registration]",
                   "Comments",
                   "Date",
                   "Task Time",
                   "Pause",
                   "Stop"]


def run(dir0, csvFilename, n_2DFLAIR, listMRI, listOfQuestions, CreateCSVQuiz):
    if not Overwrite:
        if os.path.isfile(csvFilename):
            CreateCSVQuiz = False
    if CreateCSVQuiz:
        print("Finding files...")
        X_2DFLAIR = Utilities.Find_Name(dir0, n_2DFLAIR)
        if type(X_2DFLAIR) != list:
            X_2DFLAIR = [X_2DFLAIR]
        print "Creating the quiz"
        MRI_viewing.createCsvQuizz(csvFilename,
                                   X_2DFLAIR,
                                   listOfQuestions)

    print("Start...")
    MRI_viewing.fillCsvFile(csvFilename,
                            range(2, len(listOfQuestions) + 2),
                            Viewer=MRI_viewing.ViewImagesUsingJim,
                            ListNameOfTheOtherMRI=listMRI)

    print("end.")


if __name__ == '__main__':
    run(dir0, csvFilename, n_2DFLAIR, listMRI, listOfQuestions, CREATECSVQUIZ)
