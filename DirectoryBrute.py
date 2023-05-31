import sys
import requests
import socket

def check_website(url):
    try:
        socket.create_connection((url, 80), timeout=1)
        print("{} - SITE IS UP".format(url))
    except socket.error as e:
        print("{} - SITE IS DOWN".format(url))

if __name__ == "__main__":
    url = sys.argv[1]
    wordlist = sys.argv[2]
    cookie = sys.argv[3] if len(sys.argv) > 3 else None
    user_agent = sys.argv[4] if len(sys.argv) > 4 else None

    hostname = socket.gethostname()
    print("host:", hostname)
    
    ip = socket.gethostbyname(hostname)
    print("IP:", ip)

    with open(wordlist, "r") as file:
        wordlist = file.readlines()
        headers = {}
        if cookie:
            headers['Cookie'] = cookie
        if user_agent:
            headers['User-Agent'] = user_agent
        
        for word in wordlist:
            try:
                url_final = "{}/{}".format(url, word.strip())
                response = requests.get(url_final, headers=headers)
                code = response.status_code
                if code != 404:
                    check_website(url_final)
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as error:
                print(error)
                pass
