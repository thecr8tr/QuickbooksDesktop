__author__ = 'thecr8tr'


from quickbooks import request


q = request.query('C:\\Users\\Travis\\Desktop\\QB Sandbox\\Fast Trac Pizza, Inc. 04-14-2015QBW.QBW')

q.WorkersCompCode()

print(q.response)
