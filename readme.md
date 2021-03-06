Quickbooks Python
==================

Use this to connect to your quickbooks and read data.

###Requirments:

- Windows
- win32com
- xml
- Quickbooks > Pro Version, Enterprise edition
- Administrator account
- It really helps to have the SDK and Desktop Reference for QB

- ReportsQueryRq tables pg 93-98

======================================================================================

With the addition of attributes, only the following request are funcitonal:
-AccountQuery
-CheckQuery
-CustomerQuery
-VendorQuery
-CheckAdd
-CustomerAdd

06/07/2015
Notes:
-Session currently starts and stops with each request.  This may not be desirable bc user
        may want to iterate over data, or perform multiple requests and w/out waiting for the 
        session to restart every time
-Session complete much faster if the company file is open in QuickBooks.

Changes:
-Created add attributes and a few more Requests
-Created xml2csv.py to allow transfer from xml data to csv format to open with excel

======================================================================================

All item queries are weakly supported.  Requests may or may not work properly.

06/02/2015
Notes:
-Session currently starts and stops with each request.  This may not be desirable bc user
        may want to iterate over data, or perform multiple requests and w/out waiting for the 
        session to restart every time

Changes:
-minor additions and modifications to response attributes

======================================================================================

06/01/2015:
Changes:
- refactored request.query.req.* to match new format
- added variables to the quickbooks.request.query.__init__ for attribute passing

Additions:
- Created quickbooks.request.set_Customer_request_attributes to parse for set attributes and 
            build xml nodes for them.

======================================================================================

05/31/2015:
Changes:  
- Turned quickbooks.Quickbooks into a set of functions that supplies basic request tools

Additions:
- Created quickbooks.request to build a library of requests.  Added all query sets under
            query class.  All query requests do not currently work and only pull all data
- Created ManualRunner.  This is a simple implementation to show basic usage 
            and for manual testing
- TODO.  I like to have an idea of where I want to go.

======================================================================================

To install :
- clone this repo

install win32com
go into the folder and run python setup.py install

in your code write this:

```
from quickbooks import Quickbooks

Quickbooks(qb_file='path_to_your_file').get_all()
```

it does more than that read the source.

This is it, I will add more when my client ask me more ;)

Please note this will take longtime to load all your data.

Plan :
- Want to be able to create, remove and modify data
- Insert everything into database
- save the state so the next time I can get increment data (Faster)
- Make it work with qbwc (Should be easy I have a working version)
- implement in django and admin
