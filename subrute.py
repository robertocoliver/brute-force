import sys
import dns.resolver

chamada = dns.resolver.Resolver()

try:
    url = sys.argv[1]
    wordlist = sys.argv[2]
except IndexError:
    print("Usage: python3 subrute.py url wordlist.txt")
    sys.exit(1)

try:
    with open(wordlist, 'r') as arquivo:
        linhas = arquivo.read().splitlines()
except FileNotFoundError:
    print("Arquivo não existe")
    sys.exit(1)

for sub in linhas:
    try:
        sub_domain = "{}.{}".format(sub, url)
        request = chamada.resolve(sub_domain, "A")
        for c in request:
            print(f"{sub_domain} >> {c}")
    except dns.resolver.NXDOMAIN:
        pass
