# catcount
Concatenate count tables for RNA-seq reads mapped to features by htseq-count

## Usage
```bash
catcount [-h] [-i INFILES [INFILES ...]] [-o OUTNAME] [-d OUTDIR]
                [-n FEATURENAMES]
```
Takes a list of files containing counts by feature name and concatenates into
single table. Can merge counts from comma separated pairs of file names.

**Optional arguments**:
  -h, --help            show this help message and exit  
  -i INFILES [INFILES ...], --inFiles INFILES [INFILES ...]  
                        List of count files or pairs of files.  
  -o OUTNAME, --outName OUTNAME  
                        Write concatenated count table to this file.  
  -d OUTDIR, --outDir OUTDIR  
                        Directory for output file to be written to.  
  -n FEATURENAMES, --featureNames FEATURENAMES  
                        Keep feature names that start with this string. i.e.  
                        'ge' will return 'gene_001'  

## Example  

```bash
catcount.py -n gene_ -d results -o catcounttable.tab -i Con1_rep1.txt,Con1_rep1_unpaired_reads.txt Con1_rep2.txt Con2_rep1.txt Con2_rep2.txt,Con2_rep2_unpaired_reads.txt
```

- Only report counts for features beginning with the string "gene_"
- Output concatenated counts to _results/catcounttable.tab_
- Merge counts from htseq-count runs for paired and unpaired reads from samples Con1_rep1 and Con2_rep2.
- Concatenate count tables for all four samples