1.	Introduction

A billing system is a software program or platform that is used to manage and process invoices, payments, and other financial transactions for a business. Here are some key features that a billing system might include:

Security: Measures to protect sensitive financial data, such as encryption and secure login protocols.

Bill generation: The ability to create and send invoices to customers, either manually or automatically regularly.

Payment processing: The ability to accept and track payments from customers, including support for various payment methods such as credit cards, bank transfers, and more.

Customer Management: A database of customer information, including contact details, billing and shipping addresses, and purchase history.

Financial Report: Tools for generating reports on sales, revenue, and other financial metrics, as well as the ability to track expenses and profits.


Overall, a billing system can help a business streamline its financial processes, improve accuracy and efficiency, and provide better customer service by making it easy for customers to view and pay invoices. The seller does not need to maintain soft copies of cache books or customer information as all the information will be securely stored in a database that can be retrieved whenever needed.

As python is a very hot topic nowadays, we used python3 to develop the front end of a system. For storing data, we used MySQL 8.0 as the back end of the project.
In this project, we developed features: for Payment, Transactions History, Customer, etc., which reduce human efforts and increase efficiency.
Python3
Python3 is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built-in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components. Python's simple, easy-to-learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms and can be freely distributed.
Python is a very high-level programming language, yet it is effortless to learn
•	Easy to Code.
•	Easy to Read.
•	Free and Open-Source.
•	Robust Standard Library.

Visit this website to learn more about python /https://www.python.org/doc/
MySQL 8.0
MySQL, the most popular Open-Source SQL database management system, is developed, distributed, and supported by Oracle Corporation.
MySQL is a database management system.  It may be anything from a simple shopping list to a picture gallery or the vast amounts of information in a corporate network. To add, access, and process data stored in a computer database, you need a database management system such as MySQL Server.
MySQL is an Oracle-backed open-source relational database management system (RDBMS) based on Structured Query Language (SQL). MySQL runs on virtually all platforms, including Linux, UNIX, and Windows. Although it can be used in a wide range of applications, MySQL is most often associated with web applications and online publishing.
MySQL is an important component of an open-source enterprise stack called LAMP. LAMP is a web development platform that uses Linux as the operating system, Apache as the web server, MySQL as the relational database management system, and PHP as the object-oriented scripting language. (Sometimes Perl or Python is used instead of PHP.)

1.1 Module

A billing system typically consists of several modules that work together to handle the various aspects of billing and invoicing. These modules may include:

•	Login System: This module is the first module of the system It manages the login functionalities. If the user is not verified it doesn’t allow him/her to proceed further.

1.2 Sub modules
•	Invoicing: This module generates and sends invoices to customers, either manually or automatically based on predefined billing schedules.


•	Customer management: This module stores and manages information about customers, including contact details, billing and shipping addresses, and payment preferences.


•	Product management: This module stores and manages information about the products or services being offered, including pricing, descriptions, and availability.



•	Payment processing: This module handles the acceptance and processing of payments from customers, including the integration of various payment gateways and the reconciliation of payments with invoices.


•	Reporting and analysis: This module generates reports and analytics on various aspects of the billing process, including sales, customer activity, and payment trends.


2. Purpose

A billing system is a tool that is used to track, process, and manage invoices and payments for goods or services. Its main purpose is to facilitate the billing and payment process, making it more efficient and accurate.

Here are some specific purposes of a billing system:


•	Generating invoices: A billing system can automatically generate invoices for goods or services provided, based on information entered into the system. This can save time and reduce the risk of errors.



•	Tracking payments: A billing system can track payments made by customers and alert the business when a payment is overdue.



•	Managing customer accounts: A billing system can store customer information and track the products or services they have purchased, as well as the amount they owe.



•	Providing Transactional reports: A billing system can generate reports on the financial performance of a business, including sales, expenses, and profits.



Case Study Report

“Billing System”

Submitted by
KHAJA NOMAN AHMED (160320737039)
SHADAAB AHMED (160320737033)
SYED ANNAS MOHI UDDIN (160320737034)
MOHAMMED ABDUS SALAM MISBAH (160320737035)
SAMEER KHAJA NIZAM UDDIN (160320737038)


UNDER THE GUIDANCE OF
MS. TANVEER SULTANA

DEPARTMENT OF
INFORMATION TECHNOLOGY

2022-2023

 
DECCAN COLLEGE OF ENGINEERING AND TECHNOLOGY
DAR-US-SALAM, AGAPURA, HYDERABAD, TELANGANA 500001
7.Reference

[1]	Guido van Rossum, and Fred L. Drake, Jr. (Editor) “The Python Language Reference Manual” Network Theory Ltd (Revised November 2006).


[2]	Doug Hellman “Python 3 Standard Library by Example” Addison-Wesley Professional; June 11, 2017.


[3]	Sandeep Jain GeeksforGeeks “Python Programming Language”


[4]	Google IT Automation Crash Course on Python -Coursera


[5]	“MySQL Connector/Python Revealed” by Jasper Wisborg Krogh



[6]	“Python Tutorial” by Anand at YouTube channel @codeitup



[7]	“Database Management system Manual” Mohd Abdul Aleem -professor at Deccan college of engineering and technology, Hyderabad (Revised November 2021).


3.Flow chats
Login Module:  
Billing Module
 
4. Sample Code

import mysql.connector as connector
from datetime import date 
import time
from termcolor import colored

global conn, cursor
conn = connector.connect(host="localhost", database="prod",
                         user="root", password="Example@2022#")
cursor = conn.cursor()

#login

def login():
    print("                              📺    DECCAN ELECTRONICS   📺                     ")
    print('-' *100)
    print("                            💴    Automated Billing-System    💴               ")
    print('-' *100)
    username = input(' Enter  Username 👤: ')
    if username == 'admin': 
        print("checking username.....")
        time.sleep(0.5)
        print("Verified ✅") 
    else:
        text= colored('⚠⚠           Invalid Username            ⚠⚠','red')
        print(text)
        text = colored('-'*100, 'red') 
        print(text)
        return login()
    password = input(' Type your password: ')
    if password == '1234':
        time.sleep(0.5) 
        print("Logged in Successfully ✅")
        return main_menu() 
    else:
        print("Incorrect Password")
        return password  

def clear():
    for _ in range(65):
        print()

def last_bill_no():
    cursor.execute('select max(bill_id) from bills')
    record = cursor.fetchone()
    return record

def find_item(no):
    cursor.execute('select * from items where id ={}'.format(no))
    record = cursor.fetchone()
    return record

def add_item():
    clear()
    print('Add New Item - Screen')
    print('-'*100)
    item_name = input('Enter new Item Name :')
    item_price = input('Enter Item Price :')
    sql = 'select * from items where item_name like "%{}%"'.format(item_name)
    cursor.execute(sql)
    record = cursor.fetchone()
    if record == None:
        sql = 'insert into items(item_name,price) values("{}",{});'.format(
            item_name, item_price)
        cursor.execute(sql)
        print('\n\nNew Item added successfully.....\nPress any key to continue....')
    else:
        print('\n\nItem Name already Exist.....\nPress any key to continue....')
    wait = input()

#   function name       : modify_item
#   purpose             : change item details in items table

def modify_item():
    clear()
    print("                 Item List             " )
    text=colored('-'*100,'blue')
    print(text)
    query='select * from items'
    cursor.execute(query)
    records = cursor.fetchall()
    for row in records:
        print(row)
    print('-'*100)
    print('-'*100)
    print('Modify Item Details - Screen')
    print('-'*100)
    item_id = input('Enter Item ID :')
    item_name = input('Enter new Item Name :')
    item_price = input('Enter Item Price :')
    sql = 'update items set item_name = "{}", price ={} where id={}'.format(
        item_id, item_name, item_price)
    cursor.execute(sql)
    print('\n\nRecord Updated Successfully............')

#   function name           : item_list
#   purpose                 : To display all the items in items tables

def item_list():
    clear()
    sql = "select * from items"
    cursor.execute(sql)
    records = cursor.fetchall()
    for row in records:
        print(row)
    print('\nPress any key to continue.....')
    wait = input()

#   function name       : billing
#   purpose             : To generate bills

def billing():
    clear()
    items = []
    bill_no = last_bill_no()
    if bill_no[0] == None:
        bill_no = 1
    else:
        bill_no = bill_no[0]+1
    print("                 Item List             " )
    text=colored('-'*100,'blue')
    print(text)
    query='select * from items'
    cursor.execute(query)
    records = cursor.fetchall()
    for row in records:
        print(row)
    print('-'*100)
    print('-'*100)
    name = input('Enter customer Name :')
    phone = input('Enter Phone No :')
    today = date.today()
    while True:
        no = int(input('Enter item No (0 to stop) :'))
        if no <= 0:
            break
        else:
            item = find_item(no)
            if item == None:
                print('Item Not found  ')
            else:
                qty = int(input('Enter Item Qty :'))
                item = list(item)
                item.append(qty)
                items.append(item)

    clear()
    print('                      📺    Deccan Electronics    📺              ')
    print('                              📍 Panjagutta,Hyd     ')
    print('                     📞 : 9871816901, Email: deccan@electronics.com')
    print('Bill No :{}        Date :{}'.format(bill_no, today))
    print('-'*100)
    print('Customer Name :{}          Phone No :{}'.format(name, phone))
    print('-'*100)
    print('Item Id     Item Name                Price            Qty         Amount ')
    print('-'*100)
    total = 0
    for item in items:
        print('{:<10d} {:25s} {:.2f} {:>10d}          {:>.2f} \
            '.format(item[0], item[1], item[2], item[3], item[2]*item[3]))
        total = total + item[2]*item[3]
    print('-'*100)
    print('Total Payable amount : {}'.format(total))
    print('\nPress any key to continue........')
    # insert data into tables
    sql = 'insert into bills(name,phone,bill_date) values("{}","{}","{}");'.format(
        name, phone, today)
    cursor.execute(sql)
    for item in items:
        sql = 'insert into transaction(item_id,qty,bill_id) values({},{},{});'.format(
            item[0], item[3], bill_no)
        cursor.execute(sql)
    wait = input()

#   function      : Date_wise_sell
#   purpose       : Create a report on date wise sell or sell between two dates

def date_wise_sell():
    clear()
    print('Sell Between Two Dates -- Screen')
    print('-'*100)
    start_date = input('Enter start Date (yyyy-mm-dd) :')
    end_date = input('Enter End Date (yyyy-mm-dd) :')
    sql = 'select * from bills where bill_date between "{}" and "{}"'.format(
        start_date, end_date)
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Bill No         Customer Name          Phone No          Bill Date')
    print('-'*100)
    for row in records:
        print('{:10d} {:30s} {:20s} {}'.format(row[0], row[1], row[2], row[3]))
    print('-'*100)
    print('\n\nPress any key to continue....')
    wait = input()

# function name        : bill information
# purpose               : display details of any bill

def bill_information():
    clear()
    bill_no = input('Enter Bill Number :')
    sql = 'select b.bill_id,b.name,b.phone,b.bill_date,t.item_id,t.qty,i.item_name,i.price from bills b,transaction t,items i \
           where b.bill_id = t.bill_id AND t.item_id= i.id AND \
           b.bill_id ={};'.format(bill_no)
    cursor.execute(sql) 
    records = cursor.fetchall()
    n = cursor.rowcount
    clear()
    print("Bill No :",bill_no)
    print('-'*100)
    if n<=0:
        print('Bill number {} does not exists'.format(bill_no))
    else:
        print('Customer Name : {}  Phone No :{}'.format(records[0][1],records[0][2]))
        print('Bill Date : {}'.format(records[0][3]))
        print('-'*100)
        print('{:10s} {:30s} {:20s} {:10s} {:30s}'.format('ID','Item Name','Qty','Price','Amount'))
        print('-'*100)
        for row in records:
            print('{:<10d} {:30s} {:<20d} {:.2f} {:>.2f}'.format(row[4],row[6],row[5],row[7],row[5]*row[7]))
        print('-'*100)
    print('\nPress any key to continue....')
    wait = input()   


#  function name    : amount_collected
#  purpose          : Function to display amount collected between two dates

def amount_collected():
    clear()
    start_date = input('Enter start Date (yyyy-mm-dd) :')
    end_date   = input('Enter End   Date (yyyy-mm-dd) :')
    clear()
    print('Amount collected between: {} and {}'.format(start_date,end_date))
    print('-'*100)
    sql = 'select sum(t.qty*i.price) from bills b,transaction t,items i \
           where b.bill_date between "{}" AND "{}" AND b.bill_id = t.bill_id AND \
           t.item_id = i.id;'.format(start_date,end_date)
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    print('\nPress any key to continue.....')
    wait= input()

def search_item():
    clear()
    item_name =input('Enter Item Name :')
    sql ='select * from items where item_name like "%{}%";'.format(item_name)
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Item Names start with :',item_name)
    print('-'*100)
    print('{:10s} {:30s} {:20s}'.format('Item ID','Item Name','Item Price'))
    print('-'*100)
    for row in records:
        print('{:<10d} {:30s} {:.2f}'.format(row[0],row[1],row[2]))
    print('-'*100)
    print('\nPress any key to continue....')
    wait= input()

def search_customer():
    clear()
    cust_name =input('Enter customer Name :')
    sql ='select * from bills where name like "%{}%";'.format(cust_name)
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Customer Names started with :',cust_name)
    print('-'*100)
    print('{:10s} {:30s} {:20s} {:20s}'.format('Bill No','Customer Name','Phone No','Bill Date'))
    print('-'*100)
    for row in records:
        print('{:<10d} {:30s} {:20s} {:20s}'.format(row[0],row[1],row[2],str(row[3])))
    print('-'*100)
    print('\nPress any key to continue....')
    wait= input()

# function name      : search_bill
# purpose            : function to find out bill information

def search_bill():
    clear()
    bill_no = input('Enter Bill Number :')
    sql = 'select b.bill_id,b.name,b.phone,b.bill_date,t.item_id,t.qty,i.item_name,i.price from bills b,transaction t,items i \
           where b.bill_id = t.bill_id AND t.item_id= i.id AND \
           b.bill_id ={};'.format(bill_no)
    cursor.execute(sql) 
    records = cursor.fetchall()
    n = cursor.rowcount
    clear()
    print("Bill No :",bill_no)
    print('-'*100)
    if n<=0:
        print('Bill number {} does not exists'.format(bill_no))
    else:
        print('Customer Name : {}  Phone No :{}'.format(records[0][1],records[0][2]))
        print('Bill Date : {}'.format(records[0][3]))
        print('-'*100)
        print('{:10s} {:30s} {:20s} {:10s} {:30s}'.format('ID','Item Name','Qty','Price','Amount'))
        print('-'*100)
        for row in records:
            print('{:<10d} {:30s} {:<20d} {:.2f} {:>.2f}'.format(row[4],row[6],row[5],row[7],row[5]*row[7]))
        print('-'*100)
    print('\nPress any key to continue....')
    wait = input()   

#  function name    : search_menu
#  purpose          : Display search menu on the screen

def search_menu():
    while True:
        clear()
        print('      S E A R C H    M E N U ')
        print('-'*100)
        print('1.   Item Name')
        print('2.   Customer information')
        print('3.   Bill information')
        print('4.   Back to main Menu')
        choice = int(input('\n\n Enter your choice (1..4): '))
        if choice==1:
            search_item()
        if choice==2:
            search_customer()
        if choice==3:
            search_bill()
        if choice==4:
            break

#  function name    : report menu
#  purpose          : Display report menu on the screen
def report_menu():
    while True:
        clear()
        print('   R E P O R T   &  A N A L Y S I S ')
        print('-'*100)
        print('1.   Item List')
        print('2.   Sell Between Dates')
        print('3.   Amount collected')
        print('4.   Back to main Menu')
        choice = int(input('\n\nEnter your choice (1..5): '))
        if choice==1:
            item_list()
        if choice==2:
            date_wise_sell()
        
        if choice==3:
            amount_collected()
        if choice==4:
            break

def main_menu():
    while True:
        clear()
        print("                           📺    Deccan Electronics    📺                     ")
        print("                            💴    Billing   System    💴               ")
        print('*' *100)
        print('                                  M A I N   M E N U                                    ')
        print('-'*100)
        print('1.   Billing')
        print('2.   Products Management')
        print('3.   Add Product')
        print('4.   Search Menu')
        print('5.   Report & Analysis')
        print('6.   Exit')
        choice = int(input('\n\nEnter your choice (1..6): '))
        if choice==1:
            billing()
        if choice==2:
            modify_item()
        if choice==3:
            add_item()
        if choice==4:
            search_menu()
        if choice==5:
            report_menu()
        if choice==6:
            break

if __name__=="__main__":
    clear()
    login()





