#import re

#txt =  'i love to teach python and javascript'

#match = re.match('i love to teach', txt, re.I)
#print(match)

#span = match.span()
#print(span)

#start, end = span
#print(start, end)
#substring = txt[start:end]
#print(substring)

#import re

#txt = ' I love to study python and english'
#match =  re.match('I like to study',txt, re.I)
#print(match)

#import re

#txt = ' I love to teach pythonand javascript'

#match = re.match('Ilove to teach',txt,re.I)
#print(match)

#import re

#txt ='''python is the most beautiful language that a human being has ever create.
#I recommend python for a first programming language'''

#match = re.search('first',txt,re.I)
#print(match)

#span = match.span()
#print(span)

#start, end = span
#print(start, end)
#substring = txt[start:end]
#print(substring)

#import re

#txt = '''python is the most beautiful language that a human being has ever create.
#I recommend python for a first programming language'''


#matches = re.findall('language',txt,re.I)
#print(matches)

#import re

#txt = '''python is the most beautiful language that a human being has ever create.
#I recommend python for a first programming language'''


#matches = re.findall('python',txt,re.I)
#print(matches)

#import re


#matches = re.findall('python|python',txt,re.I)
#print(matches)

#matches = re.findall('[Pp]ython',txt,re.I)
#print(matches)

#import re
#txt = '''python is the most beautiful language that a human being has ever create.
#I recommend python for a first programming language'''

#match_replaced = re.sub('python|python','javascript',txt,re.I)
#print(match_replaced)

#or
#match_replaced = re.sub('[Pp]ython','javascript',txt,re.I)
#print(match_replaced)
#import re


#txt = '''%I a%m te%%a%%ce%r% a%n%d %% I l%o%ve te%ach%ing.
#T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%eow%er%ing p%e%o%ie.
#I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
#D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

#matches = re.sub('%','', txt)
#print(matches)


#import re
#txt = '''I am teacer and  I love teaching.
#There is nothing as rewarding as educating and empowering peowering peoie.
#I found teaching more interesting than any other jobs.
#Does this motivate you to be a teacher?'''
#print(re.split('\n',txt))


#import re

#regex_pattern = r'apple'
#txt = 'Apple and banana are fruits. An old cliche say an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
#matches = re.findall (regex_pattern,txt)
#print(matches)

#matches = re.findall (regex_pattern,txt,re.I)
#print(matches)

#regex_pattern = r'[Aa]pple'
#matches = re.findall(regex_pattern,txt)
#print(matches)


#import re
#regex_pattern = r'\d'
#txt = 'this regular expression example was made on December 6, 2019 and revised on  sep 21, 2022'
#matches = re.findall(regex_pattern,txt)
#print(matches)

#import re
#regex_pattern = r'\d+'
#txt = 'this regular expression example was made on December 6, 2019 and revised on  sep 21, 2022'
#matches = re.findall(regex_pattern,txt)
#print(matches)

#import re


#regex_pattern = r'[a].'
#txt = '''Apple and banana are fruits'''
#matches = re.findall(regex_pattern,txt)
#print(matches)

#import re


#regex_pattern = r'[a].+'
#txt = '''Apple and banana are fruits'''
#matches = re.findall(regex_pattern,txt)
#print(matches)


#import re


#regex_pattern = r'[a].*'
#txt = '''Apple and banana are fruits'''
#matches = re.findall(regex_pattern,txt)
#print(matches)


#import re


#txt = '''I am mnot sure if there is a convention how to write he world e-mail
#some people write it as email others may write it as Email or E-mail.'''
#regex_pattern = r'[Ee]-?mail'
#matches = re.findall(regex_pattern,txt)
#print(matches)


#import re


#txt = 'tis regular expression example was made on december 6, 2021 and revised on sep 21, 2022'
#regex_pattern = r'\d{4}'
#matches = re.findall(regex_pattern,txt)
#print(matches)

import re

txt = 'tis regular expression example was made on december 6, 2021 and revised on sep 21, 2022'
regex_pattern = r'\d{1, 4}'
matches = re.findall(regex_pattern, 'txt')
print(matches)

import re


txt = 'This regular expression example was made on dec 6, 2021 and revised on july 8, 2022'
regex_pattern = r'^This'
matches = re.findall(regex_pattern, txt)
print(matches)

import re


txt = 'This regular expression example was made on dec 6, 2021 and revised on july 8, 2022'
regex_pattern = r'[^A-Za-z ]+'
matches = re.findall(regex_pattern, txt)
print(matches)


