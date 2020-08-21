FROM r-base:4.0.2

RUN R -e "install.packages('data.tables', repos = 'http://cran.us.r-project.org')"
RUN R -e "install.packages('BiocManager', repos = 'http://cran.us.r-project.org')"
RUN R -e "BiocManager::install('NOISeq')"

COPY szabo_inflammation_signature.R /szabo_inflammation_signature.R

CMD ["Rscript", "/szabo_inflammation_signature.R", "/data/GRCh37ERCC_refseq105_genes_count.csv", "/output/predictions.csv"]
