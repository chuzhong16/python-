text = "X-DSPAM-Confidence:    0.8475"  
space = text.find(" ")  
num = text[space:]  
num = strip()  
  
num = float(num)  
print num