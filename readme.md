Quickbooks Python
==================

Use this to connect to your quickbooks and read data.

###Requirments:

- Windows #ARGGGHH !
- win32com IMPORTANT !
- Quickbooks > Pro Version, Enterprise edition
- Administrator account

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
