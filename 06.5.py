text = "X-DSPAM-Confidence:    0.8475";
s = text.find("0")
str = text[s:len(text)]
num = float(str)
print num
