import bayes
import re

emailText = open('email/ham/6.txt', encoding='utf-8', errors='ignore').read()
# emailText = 'this book is the best book on Python or M.L.'
# listOfTokens = bayes.textParse(emailText)
# print(listOfTokens)

import re
listOfTokens = re.split(r'\W', emailText)
# print([tok.lower() for tok in listOfTokens])
print([tok.lower() for tok in listOfTokens if len(tok) > 2])