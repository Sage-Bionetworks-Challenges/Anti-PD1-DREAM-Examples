FROM python:3.7

RUN pip install tidepy numpy pandas==1.0.5

COPY run_tide.py /run_tide.py

CMD ["python", "/run_tide.py", "/data/GRCh37ERCC_refseq105_genes_tpm.csv", "/output/predictions.csv"]
