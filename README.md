# Anti-PD1-DREAM-Examples

## Overview

Here we describe how to build and locally run example models provided for Challenge Question 1 of the [Anti-PD1 DREAM Challenge](https://www.synapse.org/#!Synapse:syn18404605/wiki/589611).

* [szabo model](szabo) (R example)
* [tide](tide) (Python example)


## Dockerizing the model

1. Start by cloning this repository.

2. Go to one of the example folders

3. Build the Docker image that will contain the model with the following command:

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
