print("****Secret-Code****")
word=input("Enter a word:")

print("Encode a code")
if(len(word)>=3):
 code=word[1:]+word[0]
 encode="ren"+"".join(code)+"ram"
 print("Encoded word is :",encode)
elif(len(word)<3):
  print("reversed word is :",reversed(word))

print("Decode a code")
if(len(word)<3):
  print("Original word is :",reversed(word))
elif(len(word)>=3):
  decode=encode[3:-3]
  decode=decode[len(code)-1]+decode[:-1]
  print("Decoded word is :",decode)
 