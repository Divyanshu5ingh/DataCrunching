For this program I have used a very simple approach

I have divided this program in 3 parts

    1.Load the data
    2.Merge the data
    3.Generate output

I have used pandas library to solve this program
As pandas is one of the best library for data analysis

    LOAD THE DATA

As I was given with three data file, I have used .read_csv() function of pandas libray and used '/t' to check the delemeter, I have done this with all of the three files

    MERGE THE DATA

As given in the question that "user_email_hash.tsv" and "plain_32m.tsv" file is common with "email" and "ip_1m.tsv" file is common with "id"
So I have merged emailFile and plainPWFile with email, and again merge ipFile with id
To merge these three data files into a single file I have used .merge() function

    GENERATE OUTPUT

Now to save that output data file I have used .to_csv() function with the seperator "sep = '\t'"

By using these three step I was able to solve the program
