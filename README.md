# catcount.py
Concatenate count tables for RNA-seq reads mapped to features by htseq-count  

## Usage  

**catcount [-h] [-i INFILES [INFILES ...]] [-o OUTNAME] [-d OUTDIR] [-n FEATURENAMES]**  

Takes a list of files containing counts by feature name and concatenates into
single table. Can merge counts from comma separated pairs of file names.

**Required arguments**:  
&nbsp;&nbsp;&nbsp;-i, --inFiles [INFILES ...]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; List of count files or pairs of files.  

**Optional arguments**:  
&nbsp;&nbsp;&nbsp;-h, --help  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Show this help message and exit  
&nbsp;&nbsp;&nbsp;-o, --outName *OUTNAME*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Write concatenated count table to this file.  
&nbsp;&nbsp;&nbsp;-d, --outDir *OUTDIR*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Directory for output file to be written to.  
&nbsp;&nbsp;&nbsp;-n, --featureNames *FEATURENAMES*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Keep feature names that start with this string. i.e. 'ge' will return 'gene_001'  

## Example  

```bash
./catcount.py -n gene_ -d results -o catcounttable.tab \
-i Con1_rep1.txt,Con1_rep1_unpaired_reads.txt Con1_rep2.txt Con2_rep1.txt Con2_rep2.txt,Con2_rep2_unpaired_reads.txt
```

- Only report counts for features beginning with the string "gene_"
- Output concatenated counts to _results/catcounttable.tab_
- Merge counts from htseq-count runs for paired and unpaired reads from samples Con1_rep1 and Con2_rep2.
- Concatenate count tables for all four samples