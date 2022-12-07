import sys

def decode(dec_string):
  ans = ''
  i = 0
  
  try:
    while(i != len(dec_string)):
      split = dec_string[i] + dec_string[i + 1]
      if(int(split) >= 32):
        ans += chr(int(split))
        i += 2
      else:
        split += dec_string[i + 2]
        if(int(split) <= 126):
          ans += chr(int(split))
          i += 3
        else:
          raise Exception
    
    return ans

  except:
    print("Invalid ASCII found!")
    sys.exit(1)


def check(ascii_string):
  keywords = ['ctf', 'flag', '_', '{', '}']
  
  for i in keywords:
    if(i in ascii_string.lower()):
      return "Uff! That looks like a flag! Hope it helps you solve your CTF challenge :)\n\n"

  return ""