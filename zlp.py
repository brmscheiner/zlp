import zulip
import sys

def setData(filename,content):
    with open(filename,'w+') as f:
        f.write(content)

def getData(filename):
    with open(filename,'r') as f:
        content = f.read().replace('\n','').replace(' ','')
    if content:
        return content
    sys.stdout.write('Error! no content in file '+filename)
    raise()


        

if __name__=='__main__':
    for i in sys.argv:
        print(i)
    key=getData('key.txt')
    email=getData('email.txt')
    print(key)
    print(email)
    
# # Send a private message
# client.send_message({
    # "type": "private" | "stream",
    # "to": "hamlet@example.com",
    # "subject": "hrtz" # stream messages only
    # "content": "I come not, friends, to steal away your hearts."
# })
