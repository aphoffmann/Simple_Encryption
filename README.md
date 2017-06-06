# Simple_Encryption
1. Chunk(S)
  
Splits a sentence into syllables. 


2. key = genKey(len(chunk(S)))

Generates random key based on number of possible permutations of syllables. 

3. E = encode(S, key)

Returns encoded sentence string E

4. D = decode(E, key)
  
Returns decoded original sentence S
