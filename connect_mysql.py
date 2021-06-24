import mysql.connector as mysql

HOST = "10.1.0.50"
DATABASE = "snmptt"
USER = "admin"
PASSWORD = "1qaz2wsx"
##connect database
db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
print("Connected to: ", db_connection.get_server_info())

select_data = db_connection.cursor()
select_data.execute("select * from snmptt order by hostname limit 1;")
#select_data.execute("select * from snmptt_unknown")
#for x in select_data:
#    print(select_data.fetchone())

print(select_data.fetchmany())
