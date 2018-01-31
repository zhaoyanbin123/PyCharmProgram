# coding=utf-8
def format_str(s):
    return s[:1].upper() + s[1::].lower()

print map(format_str, ['adam', 'LISA', 'barT'])


def format_str_1(s):
    return s.capitalize()

print map(format_str, ['adam', 'LISA', 'barT'])

for i in [1,2,3]:
    print i,