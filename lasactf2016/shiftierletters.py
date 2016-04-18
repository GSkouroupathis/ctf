import requests, re, socket


def make_post_request(params, site="http://www.xarg.org/tools/caesar-cipher/"):
    r = requests.post(site, data=params)
    return r.text

def get_scrapped(response):
    #print response
    decrypted = re.findall(r'Output:</strong><br />(.*)\n</p>', response)[0]
    return decrypted

if __name__ == "__main__":
    s = socket.socket()
    s.connect(("web.lasactf.com", 4056))
    encrypted = s.recv(1024)

    print encrypted
    print "----"
    print

    for i in range(55):
        decrypted_resp = make_post_request({'key':0, 'text':encrypted})
        decrypted = get_scrapped(decrypted_resp)

        print decrypted
        print "####"
        print

        sent = s.send(decrypted+'\n')
        if sent == 0:
            raise RuntimeError("socket connection broken")
        print sent

        encrypted = s.recv(1024)

        print encrypted
        print "----"
        print

    s.close()
