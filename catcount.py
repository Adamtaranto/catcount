#!/usr/bin/env python
#python 2.7.5
#catcount.py
#Version 1. Adam Taranto, Feb 2017
#Contact, Adam Taranto, adam.taranto@anu.edu.au

#############################################
# Concatenate count tables from HTSeq-count #
#############################################

import csv
import sys
import os
import copy
import argparse
import pandas as pd

def tempPathCheck(args):
	absOutDir = os.path.abspath(args.outDir)
	if not os.path.isdir(absOutDir):
		os.makedirs(absOutDir)
	return absOutDir

def getbasename(path):
	base = os.path.splitext(os.path.basename(path))[0]
	return base

def fetchrows(indexlist,filepath,args):
	''' Add rownames to indexlist, make unique '''
	newrows = list()
	with open(filepath) as f:
		c = csv.reader(f, delimiter='\t')
		for line in c:
			if args.featureNames:
				if line[0].startswith(args.featureNames):
					newrows.append(line[0])
			else:
				newrows.append(line[0])
	oldrows = copy.deepcopy(indexlist)
	catlist = oldrows + newrows
	uniq_rows = set(catlist)
	return list(uniq_rows)

def makeblankdf(args):
	index = list()
	columns = list()
	for sample in args.inFiles:
		setcount = 0
		for split_sample in sample.split(','):
			setcount += 1
			if setcount == 1:
				columns = columns + [getbasename(split_sample)]
				index = fetchrows(index,split_sample,args)
			elif setcount > 1:
				index = fetchrows(index,split_sample,args)
	index.sort()
	columns.sort()
	df = pd.DataFrame(index=index, columns=columns)
	df = df.fillna(0).astype(int)
	return df

def readcounts(colID,filepath,args):
	rowcounts = dict()
	with open(filepath) as f:
		c = csv.reader(f, delimiter='\t')
		for line in c:
			if args.featureNames:
				if line[0].startswith(args.featureNames):
					rowcounts[line[0]] = line[1]
			else:
				rowcounts[line[0]] = line[1]

	counts_df = pd.DataFrame.from_dict(rowcounts, orient='index', dtype='int64').astype(int)
	counts_df.columns = [colID]
	return counts_df

def populatetable(mastertable,filelist,args):
	filledtable = copy.deepcopy(mastertable)
	for sample in filelist:
		setcount = 0
		for merge_sample in sample.split(','):
			setcount += 1
			if setcount == 1:
				sample_name = getbasename(merge_sample)
				temp_df = readcounts(sample_name,merge_sample,args)
				filledtable = filledtable.add(temp_df, fill_value=0)
			elif setcount > 1:
				temp_df = readcounts(sample_name,merge_sample,args)
				filledtable = filledtable.add(temp_df, fill_value=0)

	return filledtable.astype(int)

def main(args):

	if args.inFiles is None:
		sys.exit('No input files provided')	

	if args.outDir:
		outdir = tempPathCheck(args)
		outpath = os.path.join(outdir,args.outName)
	else:
		outpath = args.outName

	mastertable = makeblankdf(args)

	filledtable = populatetable(mastertable,args.inFiles,args)

	filledtable.to_csv(path_or_buf=outpath, sep='\t', header=True, index=True, line_terminator='\n')

if __name__== '__main__':
	###Argument handling.
	parser = argparse.ArgumentParser(
		description='Takes a list of files containing counts by feature name and concatenates into single table. Can merge counts from comma separated pairs of file names.',
		prog='catcount')
	parser.add_argument("-i", "--inFiles",
		type=str,
		default=None,
		nargs='+',
		help="List of count files or pairs of files.")
	parser.add_argument("-o", "--outName",
		type=str,
		default= "CatCounts.txt", 
		help="Write concatenated count table to this file.")
	parser.add_argument("-d", "--outDir",
		type=str,
		default= None, 
		help="Directory for output file to be written to.")
	parser.add_argument("-n", "--featureNames",
		type=str,
		default= None, 
		help="Keep feature names that start with this string. i.e. 'ge' will return 'gene_001'")
	args = parser.parse_args()

	main(args);