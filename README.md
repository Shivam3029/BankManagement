# BankManagement
Bank Management using File Handling - Python 


Write a MENU BASED (Main Menu consists of 3 options. A. Add a new Account, B. Transaction & C. Quit) complete
program in Python to perform the following task:

A. Add a new Account:
Program will ask the bank officer to enter Name of the Account Holder and Opening Balance to open his account.
The last record (line) of the text file Accounts.txt will be read and the account number of the new customer
will be one more than the account number of the last record.
[for the first record, account number will be 0001]

A New Line (Record) will be appended at the end of the text file Accounts.txt with all details.
A new text file with name ‘A’+ ‘New Account Number’+’.txt’ will be created
and the following entry will be written as the first record, if the opening balance is Rs 10,000.00
‘0.00’ + ‘:’ + ‘C’ + ’:’ + ’10000.00’ + ’:’ + ’10000.00’ + ‘:’ + ’\n’
OR “0.00:C:10000.00:10000.00:\n”

After an entry, the Program will ask the bank officer, whether the officer wants to add more Account or not.
If yes, all the steps of section (A) will be repeated.
If no, all the files will be closed and Main Menu will be displayed on the screen.

B. Transaction:
Program will ask the user to enter account number of the Account Holder.

If the item not found in the text file accounts.txt,
Appropriate message will be displayed.

If the item found in the text file accounts.txt,
Program will ask the user the amount and a choice of Deposit and Withdraw.

If the choice is withdraw and withdrawal amount is more than the current balance,
Appropriate message will be displayed as invalid transaction.

If amount is equal or less than the current balance,
New modified balance will be displayed.

The master file accounts.txt will be updated and a new entry will be appended in the individual text file.
In case of deposit, similar operations (without checking any condition with the assumption that all details are valid) Will be processed.

After a transaction, the Program will ask the bank officer, whether the officer wants to do more transaction or not.
If yes, all the steps of section (B) will be repeated.
If no, all the files will be closed and Main Menu will be displayed on the screen.


C. Quit from the program:
The Program will display a “Thank you” message for using the software,


This program will use following text files:
1. accounts.txt , the Master file to store the details of all account holders in the bank.
The text file accounts.txt having the following details in each line:

If the details of an account holder is:
A/c No: 1001 [a 4 digits number]
Name of the A/c Holder: Gautam Sarkar [a string]
Current balance: Rs. 50,000 [a floating number]

A record will be written as a line (a string) in the text file stock.txt as:
‘1001’ + ‘:’ + ‘Gautam Sarkar’ + ’:’ + ’50000’ + ‘:’ + ’\n’
OR
“1001:Gautam Sarkar:50000:\n”
