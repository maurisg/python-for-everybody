text = 'X-DSPAM-Confidence:0.8475'
colon = text.find(':')
number = text[colon+1:]

print(float(number))
