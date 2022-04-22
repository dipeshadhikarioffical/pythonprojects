from file1_randompassword import Password
import argparse

# to take input from cmd this file only run through cmd
# go to this file location on c drive and then in path type cmd then follow the image which is inside  same folder
args = argparse.ArgumentParser("Usage: python file2_passwordgenerator.py -c CHARSET(eg. lud) -l LENGTH(eg 8)")
args.add_argument('-c', '--charset', required=True)
args.add_argument('-l', '--length', default=8)
options = args.parse_args()
print(options.charset)
print(options.length)

password = Password(options.charset, int(options.length))
password.set_the_charset()
password.generate_password()
print("YOUR RANDOM PASSWORD IS: ", password.get_password())
