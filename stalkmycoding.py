import webbrowser
c=str(input('codechef: '))
g=str(input('geeksforgeeks id: '))
while ' ' in c or g:
    print('enter valid usernames without spaces!')
    c = str(input('codechef: '))
    g = str(input('geeksforgeeks id: '))
cdc='https://codechef.com/users/'+c
gfg='https://auth.geeksforgeeks.org/user/'+g+'/practice/'
webbrowser.open(cdc)
webbrowser.open(gfg)
