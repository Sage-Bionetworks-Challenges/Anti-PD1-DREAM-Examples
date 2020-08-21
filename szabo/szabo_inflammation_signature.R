#!/usr/bin/env Rscript
# simple inflammation signature from Peter Szabo at BMS: reference below
# F. Stephen Hodi, Jedd D. Wolchok, Dirk Schadendorf, James Larkin, Max Qian, Abdel Saci, Tina C. Young, Sujaya Srinivasan, Han Chang, 
# Megan Wind-Rotolo, Jasmine I. Rizzo, Donald G. Jackson, Paolo A. Ascierto. Genomic analyses and immunotherapy in advanced melanoma. 
# In: Proceedings of the American Association for Cancer Research Annual Meeting 2019; 
# 2019 Mar 29-Apr 3; Atlanta, GA. Philadelphia (PA): AACR; Cancer Res 2019;79(13 Suppl):Abstract nr CT037.
# using NOISeq library to get tmm since it is simpler
# to run from command line: Rscript --quiet --vanilla szabo_inflammation_signature.R "input_counts_rna_seq.txt" "output.csv"

suppressMessages(library(NOISeq))
suppressMessages(library(data.table))

# get command line args: args[1] input rna-seq gene level count data, args[2] output file: two column(patient id, inflammation score) .csv file
args        <- commandArgs(trailingOnly=TRUE)
counts      <- fread(args[1],data.table = F); rownames(counts) <- counts[,1]; counts <- counts[,-1]; print("done reading in counts")
tmm         <- NOISeq::tmm(counts); print("done computing TMM")
inflam_sig  <- rowMedians(scale(t(log2(tmm[rownames(tmm)  %in% c("CD274", "CD8A", "LAG3","STAT1"),]+1)))); print("done computing inflamation signatrue")

inflam_sig  <- data.frame("patientID" = colnames(tmm) ,"prediction"=inflam_sig)

# write out inflammation signature to prediciton file
write.csv(inflam_sig, file = args[2], quote = F, row.names = F); print("done writing out signature")

rm(tmm,counts)

