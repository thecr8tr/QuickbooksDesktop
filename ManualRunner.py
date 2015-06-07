__author__ = 'thecr8tr'

### See request.query.__init__.query_dict for a dict of attributes to pass

from quickbooks import request

### List request and xmlfile writer
#q = request.query('C:\\Users\\Travis\\Desktop\\QB Sandbox\\Fast Trac Pizza, Inc. 04-14-2015QBW.QBW')
#q.request_ID = 'AccountQueryRq'
#q.query_request()
#xmlfile = open('C:\\Users\\Travis\\Desktop\\QB Sandbox\\Account.xml', 'w')
#xmlfile.write(q.response)
#xmlfile.close()


### Most Basic Check Entry
#q = request.add('C:\\Users\\Travis\\Desktop\\QB Sandbox\\Fast Trac Pizza, Inc. 04-14-2015QBW.QBW')
#q.request_ID = 'CheckAddRq'
#q.AccountRef.ListID = '80000044-1303832760' #Bank Account ///Operating
#q.RefNumber = 'Debit' # Check Number
#q.TxnDate = '2015-06-07' # Date
#q.PayeeEntityRef.ListID = '800000CC-1414505910' # Payee by ListID
#q.ExpenseLineAdd.AccountRef.ListID = '800000B8-1357931163' # Split Account ///Suspense
#q.ExpenseLineAdd.Amount = '20.00' # Split Amount
#q.ExpenseLineAdd.Memo = 'Test Memo' # Memo
#q.add_request()


print(q.response)
