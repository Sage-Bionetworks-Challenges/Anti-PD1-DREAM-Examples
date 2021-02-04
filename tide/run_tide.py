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
    tpmdf.to_csv("log_2_mean_normed.txt", sep="\t")
    return "log_2_mean_normed.txt"


def cli():
    """Build CLI"""
    parser = argparse.ArgumentParser(description='Run Tide')

    parser.add_argument("tpm_file", type=str, help='TPM input file')
    parser.add_argument("output", type=str, help='output prediction file')

    return parser.parse_args()


def main():
    """Invoke tide"""
    args = cli()
    normalized_tpm_path = tide_normalize(args.tpm_file)
    tide_cmd = ["tidepy", normalized_tpm_path, "-o", "output.txt", "-c", "NSCLC"]
    subprocess.check_call(tide_cmd)

    tide_scoresdf = pd.read_table("output.txt", index_col=0)
    preddf = tide_scoresdf["TIDE"]
    preddf = preddf.reset_index()
    preddf.rename(columns={"index": "patientID",
                           "TIDE": "prediction"}, inplace=True)
    preddf['prediction'] = preddf['prediction'] * -1
    preddf.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
