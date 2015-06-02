__author__ = 'thecr8tr'


from quickbooks import request


q = request.query('C:\\Users\\Travis\\Desktop\\QB Sandbox\\Fast Trac Pizza, Inc. 04-14-2015QBW.QBW')
### See request.query.__init__.query_dict for a dict of attributes to pass
q.request_ID = 'ChargeQueryRq'
q.query_request()

print(q.response)
