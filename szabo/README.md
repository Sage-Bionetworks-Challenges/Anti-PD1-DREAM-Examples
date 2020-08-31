# Example model for Anti-PD1 DREAM: Question 1

## Overview

Here we describe how to build and run locally a simple four gene inflammation model provided for Challenge Question 1 of the [Anti-PD1 DREAM Challenge](https://www.synapse.org/#!Synapse:syn18404605/wiki/589611). The goal ...

## Description of the model

The model is a simple four gene inflammation model that uses the median of the scaled TMM of CD8A, PD-L1 (CD274), STAT4 and LAG3. 
F. Stephen Hodi, Jedd D. Wolchok, Dirk Schadendorf, James Larkin, Max Qian, Abdel Saci, Tina C. Young, Sujaya Srinivasan, Han Chang, Megan Wind-Rotolo, Jasmine I. Rizzo, Donald G. Jackson, Paolo A. Ascierto. Genomic analyses and immunotherapy in advanced melanoma. In: Proceedings of the American Association for Cancer Research Annual Meeting 2019; 2019 Mar 29-Apr 3; Atlanta, GA. Philadelphia (PA): AACR; Cancer Res 2019;79(13 Suppl):Abstract nr CT037.

## Dockerize the model

1. Start by cloning this repository.

2. Move to this example folder

3. Build the Docker image that will contain the move with the following command:

    ```bash
    docker build -t awesome-antipd1-q1-model:v1 .
    ```

## Run the model locally on synthetic EHR data

1. Go to the page of the [synthetic dataset](https://www.synapse.org/#!Synapse:syn21978034) provided by the Anti-PD1 DREAM challenge. This page provides useful information about the format and content of the synthetic data.

2. Download the file [synthetic_data.tar.gz]() to the location of this example folder (only available to registered participants).

3. Extract the content of the archive

    ```bash
    $ tar xvf synthetic_data.tar.gz
    x synthetic_data/
    ```

4. Create an `output` folder

    ```bash
    mkdir output
    ```

5. Run the dockerized model

    ```bash
    docker run \
        -v $(pwd)/synthetic_data/:/data:ro \
        -v $(pwd)/output:/output:rw \
        awesome-antipd1-q1-model:v1
    ```

6. The predictions generated are saved to `/output/predictions.csv`. The column `patientID` includes the ID of the patient and the column `prediction` the probabily for the patient to be COVID-19 positive.

    ```text
    $ cat output/predictions.csv
    patientID,prediction
    p267,100
    p315,10
    p15,4
    ...
    ```

## Submit this model to the Anti-PD1 DREAM Challenge

This model meets the requirements for models to be submitted to Question 1 of the Anti-PD1 DREAM Challenge. Please see [this page]() for instructions on how to submit this model.
