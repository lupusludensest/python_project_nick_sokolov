# Python_project_Nick_Sokolov
Python_project_Nick_Sokolov

Nikolay Sokolov  7:05 AM
Домашка к уроку 2.
Представим, что мы разрабатываем игру и нам нужно создать несколько типов персонажей: лучник, медик и пехотинец. 
Каждый обладает уникальными свойствами, первый умеет поражать цели на дистанции, 
второй восстанавливать здоровье свое и других персонажей, третий может сражаться только в ближнем бою.
Разумеется всех троих объединяют некоторые параметры, все имеют объем здоровья, 
умеют перемещаться(достаточно просто выводить сообщение об этом), терять и прибавлять здоровье.
Задача, реализовать описание выше в ООП код на python.

# Deploying the virtual environment of Django. Commands. Установка вирт среды и установка джанго. Команды.

python -m venv les3env # folder with the local environment

C:\Everything\IT\Testing\Automation_08_09_2019\Python_project_Nick_Sokolov\Lesson_3>les3env\Scripts\activate.bat

pip install django

django-admin startproject core . # . dot is here to do not create excessive folder/s

# Go to UI and make active python.exe from C:\Everything\IT\Testing\Automation_08_09_2019\Python_project_Nick_Sokolov\Lesson_4_1\les4_1env\Scripts 

python manage.py startapp landing # opens the app "landing"

python manage.py runserver

# Call help and commands

python manage.py 

python manage.py startapp landing

python manage.py runserver 127.0.0.1:8001 # port rendering on itself, local machine, loopback. 127.0.0.1(host):8001(port)

http://127.0.0.1:8001/test/

http://127.0.0.1:8001/json/

http://127.0.0.1:8001/carma/

# Admin panel works with database db.sqlite3-created when we start server first time

python manage.py createsuperuser 

Username (leave blank to use 'rapid'): lupusludens

Email address: gurovvic@gmail.com

Password: MyUSA2020!@

http://127.0.0.1:8001/admin

python manage.py changepassword user_name # change password

# Model describes the structure of database 0001_initial.py

python manage.py makemigrations # creates instructions for migration, correlates with the folder "migrations"

python manage.py migrate # creates tables for administrative panel which works with the database

# Add column names/s into landing/admin.py, correlates with the admin web-app dashboard(synchronize admin.py with models.py)

# Work with the GitHub using UI, Git/GitHub/Share Project on GitHub

# Postman # Swagger

# DataBases
users
---
id pk int
login varchar(25)
password varchar(35)

person_data
---
id pk int
user_id int FK - users.id
name varchar(40)
age int
b_day datetime
salary decimal

contacts
---
id pk int
first_name varchar(50)
last_name varchar(50)

users_contacts
---
id pk int
user_id int FK >- users.id
contacts_id int FK >- contacts.id

phones
---
id pk int
contact_id int FK >- contacts.id
phone int 
time_update datetime


1: Action 0:12:35: INSTALL. 
1: 1: MySQL Server 8.0 2: {3476AEF8-4E53-40FE-90C4-5179DF0DFA3F} 
1: Action 0:12:35: FindRelatedProducts. Searching for related applications
1: Action 0:12:35: AppSearch. Searching for installed applications
1: Action 0:12:35: DwordToNumber. 
1: Action 0:12:35: LaunchConditions. Evaluating launch conditions
1: Action 0:12:35: ValidateProductID. 
1: Action 0:12:35: CostInitialize. Computing space requirements
1: Action 0:12:35: FileCost. Computing space requirements
1: Action 0:12:35: CostFinalize. Computing space requirements
1: Action 0:12:35: MigrateFeatureStates. Migrating feature states from related applications
1: Action 0:12:35: InstallValidate. Validating install
1: Action 0:12:36: SaveTargetDir. 
1: Action 0:12:36: InstallInitialize. 
1: Action 0:12:36: SetQtRemoveService. 
1: Action 0:12:36: RemoveExistingProducts. Removing applications
1: Action 0:12:36: ProcessComponents. Updating component registration
1: Action 0:12:37: GenerateScript. Generating script operations for action:
1: Updating component registration
1: Action 0:12:37: UnpublishFeatures. Unpublishing Product Features
1: Action 0:12:37: RemoveRegistryValues. Removing system registry values
1: Action 0:12:37: RemoveShortcuts. Removing shortcuts
1: Action 0:12:37: RemoveFiles. Removing files
1: Action 0:12:37: InstallFiles. Copying new files
1: File: Copying new files,  Directory: ,  Size: 
1: Action 0:12:39: CreateShortcuts. Creating shortcuts
1: Shortcut: Creating shortcuts
1: Action 0:12:39: WriteRegistryValues. Writing system registry values
1: Key: Writing system registry values, Name: , Value: 
1: Action 0:12:39: RegisterUser. Registering user
1: Action 0:12:39: RegisterProduct. Registering product
1: Registering product
1: Action 0:12:39: PublishFeatures. Publishing Product Features
1: Feature: Publishing Product Features
1: Action 0:12:39: PublishProduct. Publishing product information
1: Action 0:12:39: InstallFinalize. 
1: Action 0:12:39: ProcessComponents. Updating component registration
1: Action 0:12:40: InstallFiles. Copying new files
1: File: harness-library.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 659456
1: File: ibd2sdi.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6379624
1: File: innochecksum.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6366840
1: File: libcrypto-1_1-x64.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 3422720
1: File: libmecab.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 1839616
1: File: libprotobuf.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 2832896
1: File: libprotobuf.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 4179030
1: File: libprotobuf-debug.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6872064
1: File: libprotobuf-lite.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 553472
1: File: libprotobuf-lite.lib,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 898420
1: File: libprotobuf-lite-debug.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 1358336
1: File: libssl-1_1-x64.dll,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 686592
1: File: lz4_decompress.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6311544
1: File: my_print_defaults.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6251648
1: File: myisam_ftdump.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6508664
1: File: myisamchk.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6633584
1: File: myisamlog.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6477936
1: File: myisampack.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6531696
1: File: mysql.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6948968
1: File: mysql_config_editor.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6266496
1: File: mysql_secure_installation.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6834320
1: File: mysql_ssl_rsa_setup.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6293120
1: File: mysql_tzinfo_to_sql.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6207104
1: File: mysql_upgrade.exe,  Directory: C:\Program Files\MySQL\MySQL Server 8.0\bin\,  Size: 6925432
1: File: mysqladmin.exe,  Directory: C:\Program Files\M

# HW_2_dt_19_dec_2020
Домашка:
Создать ER-диаграму интернет магазина.
Основные сущности:
1. Товар
2. Категория
3. Корзина
4. Заказ
5. Покупатель
Поля на ваше усмотрение, здесь главное потренироваться строить структуру и связи. 
Послушать про нормализацию: https://www.youtube.com/watch?v=gDDrpL75LJY&t=1s
good
---
id pk int 
upc int
name varchar(35)
model varchar(25)
price float
status varchar(3)

category
---
id pk int
category_id int FK -< good.id
name varchar(35)
description varchar(40)

cart
---
id pk int FK -< order.id
good varchar(35)

order
---
id pk int FK -< good.id
order_number int
date datetime
good varchar(35)
quantity_of_units int

customer
---
id pk int FK - cart.id
first_name varchar(25)
last_name varchar(25)
date_of_birth datetime
gender varchar(5)
phone int
login varchar(25)
password varchar(25)


Products
---
id int PK
category_id int FK >- Product_category
product_name varchar(50)
product_brand varchar(40)
year_of_manufacture int
color char(25)
description text
price money

Product_category
---
id int PK
category varchar(30)
description text

Orders
---
id int PK
client_id int FK >- Client
date datetime
pyment_method char(20)
delivery_method char(30)
delivery_date datetime
total_price money

Carts
---
id int PK
order_id int FK >- Orders
product_id int FK >- Products
date datetime
item_price money
product_quantity int
sub_total money

Client
---
id int PK
first_name char(60)
last_name char(60)
nick_name varchar(60)
email varchar(60)
password varchar(25)
address varchar(40)
city char(80)
provice char(50)
country char(40)
postal_code varchar(7)


