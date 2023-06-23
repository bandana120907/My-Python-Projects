import webbrowser
import sys 

c=sys.argv[1]
while ' ' in c:
    print('enter valid usernames without spaces!')
    c = str(input("Enter a username: "))

d={insta:'https://instagram.com/'+c}
for i in d:
    webbrowser.open(d.get(i))
    
'''c=str(input('codechef: '))
g=str(input('geeksforgeeks id: '))
while ' ' in c or ' ' in g:
    print('enter valid usernames without spaces!')
    c = str(input('codechef: '))
    g = str(input('geeksforgeeks id: '))
cdc='https://codechef.com/users/'+c
gfg='https://auth.geeksforgeeks.org/user/'+g+'/practice/'
webbrowser.open(cdc)
webbrowser.open(gfg)'''
