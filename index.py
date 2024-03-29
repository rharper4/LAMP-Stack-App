#!/usr/bin/python3

#debug mode on
import cgitb
cgitb.enable()

#print html headers
print('Content-Type:text/html\n\n')

#connect to the DB
import pymysql
con = pymysql.connect(
	db='yoga', user='root, passwd='Your Password Goes Here', host=localhost )
 
#fetch and print contents

try:
	with con.cursor() as cur:
			cur.execute(ÒSelect * from instructorsÓ)

			rows=cur.fetchall()
			for row in rows:
				print(f'{row[0]} {row[1]}')

finally:
		con.close()

