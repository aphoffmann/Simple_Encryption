# Simple_Encryption
  Chunk(S)
  
Splits a sentence into syllables. 


  key = genKey(len(chunk(S)))

Generates random key based on number of possible permutations of syllables. 

  E = encode(S, key)

Returns encoded sentence string E

  D = decode(E, key)
  
Returns decoded original sentence S
