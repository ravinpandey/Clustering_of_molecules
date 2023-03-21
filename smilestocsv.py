import argparse
import pandas as pd

#create the argument parser 
parser=argparse.ArgumentParser(description="convert smiles file to CSV file")


# add the arguments to further process
parser.add_argument('-i','input_file',help="Input file name for conversion")
parser.add_argument('-o','output_file',help="Output file name for conversion")

# parse the arguments 
args=parser.args()


# read the smile file into pandas datframe
df=pd.read_csv(args.input_file,sep=" ",header=None,names=['smile','smileID'])


#remove the index column
df.index.name=None


# write the DataFrame to CSV file 
df.to_csv(args.output_file,index=False)


