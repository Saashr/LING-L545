# Survey of POS Taggers Performance on Shahmukhi Punjabi Corpus

This repository contains the research and analysis conducted in the project "Survey of POS Taggers Performance on Shahmukhi Punjabi Corpus". Our goal is to evaluate the performance of various Part-of-Speech (POS) taggers specifically designed for the Shahmukhi script of the Punjabi language.

## Introduction

Part-of-Speech tagging is a critical process in the pipeline of natural language processing (NLP) tasks. The performance of POS taggers on less-resourced languages like Punjabi in the Shahmukhi script is not well-documented, which motivates this survey.

## Project Structure

 

The data is a Punjabi shahmukhi annotated corpus publically available at :


https://github.com/toqeerehsan/Shahmukhi-POS-Tagging

This data is preprocessed to merge tokens with tags and then UPOS are added for each corresponding language specific tags.The sentences are then put in a .conllu format. 
The following taggers are implemented on the data. 
Perceptron: https://github.com/ftyers/conllu-perceptron-tagger
CRF : https://sklearn-crfsuite.readthedocs.io/en/latest/
MACHamp: https://github.com/machamp-nlp/machamp

## Usage: 
The command to run the taggers are as follows: 
Perceptron: python3 simple_eval.py pa-ud-test.conllu output.conllu 
CRF: python3 simple_eval.py pa-ud-test.conllu crf_pos_predictions.conllu
MACHamp:  python3 simple_eval.py pa-ud-test.conllu pa-upos-predictions-test.out 



The results show f1, precision , recall score and confusion matrix for all three taggers. 

##link to the project github repor: https://github.com/Saashr/POSTaggerSurvey-Shahmukhi/tree/master
