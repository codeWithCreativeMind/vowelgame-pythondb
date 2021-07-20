import mysql.connector


con_obj=mysql.connector.connect(host='localhost',username='root',password="root123",database='gamedb')
cursor=con_obj.cursor()

inp=int(input("enter 1--> to play GAME, enter 2--> to see result\n"))
if (inp==1):
    while True:
        user=input("enter your name:\n").lower()
        querry="select NAME from students where NAME='"+user+"'"
        cursor.execute(querry)
        data=cursor.fetchone()
        if data != None:
                print("data exists")
                print(" NAME already exists.!,try with DIFFERENT NAME")
        elif data ==None:
            print("NAME  doesnot exists,INSERTING..,")
            score=[]  
            while True:   
                c=input("enter a one charecter\n",).upper()
                v=['A','E','I','O','U']
                if ord(c)>=65 and ord(c)<=90:
                    f=[]
                    for i in v:
                        if i==c:
                            f.append(0) 
                        d= ord(i)-ord(c)
                        #print(f"entered charecter {c} minimum {d}")
                        f.append(abs(d))
                    print("list",f)
                    min=f[0]   #f=[1,2,3,4]
                    for value in f:
                        if min>value:
                            min=value
                        else:
                            min=min
                    print(f'entered charecter is {c} step {min}')
                    g={0:110,1:100,2:90,3:80,4:70,5:60,6:50,7:40,8:30,9:20}
                    for key in g:
                        if key==min:
                            points=g[key]
                            #print("points",points)
                score.append(points)
                break
            print("score:",score)
            while True:   
                c=input("enter second charecter\n",).upper()
                v=['A','E','I','O','U']
                if ord(c)>=65 and ord(c)<=90:
                    f=[]
                    for i in v:
                        if i==c:
                            f.append(0) 
                        d= ord(i)-ord(c)
                        f.append(abs(d))
                    print("list",f)
                    min=f[0]
                    for value in f:
                        if min>value:
                            min=value
                        min=min
                    print(f'entered charecter is {c} step {min}')
                    g={0:110,1:100,2:90,3:80,4:70,5:60,6:50,7:40,8:30,9:20}
                    for key in g:
                        if key==min:
                            points=g[key]
                            #print("points",points)
                score.append(points)
                break
            print("score:",score)
            while True:   
                c=input("enter third charecter\n",).upper()
                v=['A','E','I','O','U'] 
                if ord(c)>=65 and ord(c)<=90:
                    f=[]
                    for i in v:
                        if i==c:
                            f.append(0) 
                        d= ord(i)-ord(c)
                        f.append(abs(d))
                    print("list",f)
                    min=f[0]
                    for value in f:
                        if min>value:
                            min=value
                        min=min
                    print(f'entered charecter is {c} step {min}')
                    g={0:110,1:100,2:90,3:80,4:70,5:60,6:50,7:40,8:30,9:20}
                    for key in g:
                        if key==min:
                            points=g[key]
                            #print("points",points)
                score.append(points)
                break
            print("score:",score)
            sum=0
            for i in score:
                sum +=i
            print(f"your NAME: {user} and TOTAL_SCORE:{sum},YOUR DATA IS INSERTING..!")
            insert_querry="insert into students(NAME,SCORE)VALUES(%s,%s)"
            insert_data=[(user,sum)]
            try:
                print("entered inner try block")
                cursor.executemany(insert_querry,insert_data)
                print("data inserted ")
                con_obj.commit()
            except Exception:
                    print("data not inserted ")
elif(inp==2):
    cursor.execute("select * from students")
    game_details=cursor.fetchall()
    for game in game_details:
        print("\n",game)
else:
    print("you did not enter correct value")
con_obj.close()


