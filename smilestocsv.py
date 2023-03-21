import argparse
import pandas as pd

#create the argument parser 
parser=argparse.ArgumentParser(description="convert smiles file to CSV file")


# add the arguments to further process
args=parser.args()


# read the smile file into pandas datframe
df=pd.read_csv(args.input_file,sep=" ",header=None,names=['smile','smileID'])


#remove the index column
df.index.name=None


# write the DataFrame to CSV file 
df.to_csv(args.output_file,index=False)


