"""utility functions for tide"""
import argparse
import os
import subprocess

import pandas as pd
import numpy as np


def read_pickle_file(filepath):
    """Read pickle file"""
    pickle_data = pd.read_pickle(filepath)
    return pickle_data


def tide_normalize(filepath, log_trans_flag=True):
    """Normalize refseq genes TPM data (GRCh37ERCC_refseq105_genes_tpm.csv)"""
    tpmdf = pd.read_csv(filepath, index_col=0)
    if log_trans_flag:
        tpmdf = np.log2(tpmdf + 1)
    # Get row average
    row_averages = tpmdf.mean(axis=1)
    # Subtract row mean from each value in row
    tpmdf = tpmdf.sub(row_averages, axis=0)
    tpmdf.transpose().to_csv("log_2_mean_normed.txt",
                             sep="\t")

def cli():
    """Build CLI"""
    parser = argparse.ArgumentParser(description='Run Tide')

    parser.add_argument("tpm_file", type=str, help='Synapse username')

    return parser.parse_args()


def main():
    """Invoke tide"""
    args = cli()
    normalized_tpm_path = tide_normalize(args.tpm_file)
    tide_cmd = ["tidepy", normalized_tpm_path, "output.txt", "-c", "NSCLC"]
    subprocess.check_call(tide_cmd)

    tide_scoresdf = pd.read_csv("output.txt")
    final_prediction = tide_scoresdf[["V1", "TIDE"]]


# tide_scores        <- fread("temp_tide_output.txt", data.table = F)[,c("V1","TIDE")]
# names(tide_scores) <- c("patientID","prediction")

# # make sure the predictions are ordered like the expression data based on patientID.
# tide_scores        <- tide_scores[match(colnames(seq_dat), tide_scores$patientID),]; rm(seq_dat)


# # write out just TIDE scores (not other signatrues like CTL or MDSC)
# write.csv(tide_scores[,1:2], file = args[2], col.names = T, quote = F, row.names = F)

# file.remove("temp_tide_output.txt")
# file.remove("log2_mean_normed.txt")
# print("completed TIDE wrapper")


if __name__ == "__main__":
    main()


