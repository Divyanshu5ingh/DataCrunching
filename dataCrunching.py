import pandas as pd

# Now to read the file, I am using pandas .read_csv() function for that as mentioned that "TSV files are same
# as CSV file with only difference of tabs instead of commas" and .read_csv function is availabe in pandas

#Firstly I have taken the user_email_hash file, and as it is a TSV(Tab Separated Values) so I have to check the delemeter "\t" for that
#for this I have used "sep" paramater of pandas library ("sep" stands for separator)
# Here I have also used "names" parameter of pandas library as it is used to specify the column names of the file
emailFile = pd.read_csv('user_email_hash.1m.tsv', sep='\t', names=['id','username','email','hashed_password'], low_memory=False)

#Same concept I have used to read the ip_1m TSV file
ipFile = pd.read_csv('ip_1m.tsv', sep='\t', names=['id','ip'], low_memory=False)

#And here also I have used same concept to read the third file which is "plain_32m" TSV file
plainPWFile = pd.read_csv('plain_32m.tsv', sep='\t', names=['email', 'plaintext_password'], low_memory=False)
#So by using this method I was able to read all the 3 input file

#Now to merge these three data files into a single file I have used .merge() function
#As mentioned in the question that "user_email_hash.tsv" and "plain_32m.tsv" file is common with "email"
#And "ip_1m.tsv" file is common with "id"
# So to get desired output as "Id, username, email, hashed_password, plaintext_password, ip"
#I have merged the emailFile and plainPWFile with email, and again merge ipFile with id
output = pd.merge(emailFile, plainPWFile, on='email').merge(ipFile, on='id')

#Now to save that output data file I have used .to_csv() function with the seperator "sep = "\t"
#Here 1 more thing I have written which is index = False this is because to prevent the index column from being written to the output file
#By default "pandas" includes the index column to the output file
output.to_csv('output1.tsv', sep='\t', index=False)
