import sys
import dec2ascii

if(len(sys.argv) == 1):
  print("Please enter a Decimal!")
  sys.exit(1)

else:
  if(sys.argv[1].isnumeric()):
    decoded = dec2ascii.decode(sys.argv[1])
    print(f"{decoded}")
    # print(f"{dec2ascii.check(decoded)}")
    sys.exit(0)

  else:
    print(f"Invalid Decimal entered!")
    sys.exit(1)