import sys
from mathematica import mean

if __name__ == "__main__":
    if not len(sys.argv) >= 2:
        print("type: mean <args...>")
        sys.exit(0)
        
    print(mean(*map(lambda x: int(x), sys.argv[1:])))
