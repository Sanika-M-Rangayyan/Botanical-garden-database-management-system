import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="botanical_gardeb"
)
c = mydb.cursor()
def add_data(plant_id,scientific_name,local_name,garden_id):
    c.execute('INSERT INTO PLANT VALUES (%s,%s,%s)',(plant_id,scientific_name,local_name))
    mydb.commit()
    c.execute('INSERT INTO CULTIVATED_IN VALUES (%s,%s)',(plant_id,garden_id))
    mydb.commit()
def add_parent_kid_data(baby_plant,mother_plant):
    c.execute('INSERT INTO PARENT_PLANT VALUES (%s,%s)',(baby_plant,mother_plant))
    mydb.commit()
def delete_plant(plant,garden_id):
    c.execute('DELETE FROM cultivated_in where plant_id=%s',(plant))
    mydb.commit()
    c.execute('DELETE FROM vouchers where voucher_id={}'.plant)
    mydb.commit()