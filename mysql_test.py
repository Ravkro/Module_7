Import mysql.connector
from mysql.connector import errorcode

config = {
  "user": "pysports user",
  "password": "MYSQL8IsGreat!",
  "host": "127.0.0.1",
  "databse": "pysports",
  "raise_on_warnings":True
}

db= mysql.connector.connect (**config)
print('\n databsae user {} connected to MySQL on host {} with database {}". format(config["user"], config["host"[, config["databse"]))
      input("\n\n press any key to continue...")
           
except mysql.connector.Error as err:
   if err.errno == errorcode.ER_access_Denied_error:
       print(" The supplied username or password are invalid")
      
    elif err.no == errorcode.ER_bad_DB_error:
      print(" the specified databsae does not exist")
      
    else:
        print(err)
     
finally:
      db.close()
      
  
  
