__author__ = 'thecr8tr'

### See request.query.__init__.query_dict for a dict of attributes to pass

from quickbooks import request

#### List request and xmlfile writer
#q = request.query('')
#q.request_ID = 'PaymentMethodQueryRq'
#q.query_request()
#xmlfile = open('C:\\Users\\Travis\\Desktop\\QB Sandbox\\PaymentMethod.xml', 'w')
#xmlfile.write(q.response)
#xmlfile.close()


### Most Basic Deposit Entry
#q = request.add('')
#q.request_ID = 'DepositAddRq'
#q.TxnDate = '2015-06-07' # Date
#q.DepositToAccountRef.ListID = '80000044-1303832760' #Bank Account ///Operating
#q.DepositLineAdd.AccountRef.ListID = '800000B8-1357931163' # Split Account ///Suspense
#q.DepositLineAdd.Amount = '20.00' # Split Amount
#q.DepositLineAdd.Memo = 'Test Memo' # Memo
#q.add_request()


### Most Basic Check Entry
#q = request.add('')
#q.request_ID = 'CheckAddRq'
#q.AccountRef.ListID = '80000044-1303832760' #Bank Account ///Operating
#q.RefNumber = 'Debit' # Check Number
#q.TxnDate = '2015-06-07' # Date
#q.PayeeEntityRef.ListID = '800000CC-1414505910' # Payee by ListID
#q.ExpenseLineAdd.AccountRef.ListID = '800000B8-1357931163' # Split Account ///Suspense
#q.ExpenseLineAdd.Amount = '20.00' # Split Amount
#q.ExpenseLineAdd.Memo = 'Test Memo' # Memo
#q.add_request()


### Most Basic Credit Card Charge Entry
#q = request.add('')
#q.request_ID = 'CreditCardChargeAddRq'
#q.AccountRef.ListID = '800000CE-1429728073' #Credit Card Account ///Credit Card:Suntrust
#q.TxnDate = '2015-06-07' # Date
#q.PayeeEntityRef.ListID = '800000CC-1414505910' # Payee by ListID
#q.ExpenseLineAdd.AccountRef.ListID = '800000B8-1357931163' # Split Account ///Suspense
#q.ExpenseLineAdd.Amount = '20.00' # Split Amount
#q.ExpenseLineAdd.Memo = 'Test Memo' # Memo
#q.add_request()


### Most Basic Credit Card Charge Entry
#q = request.add('')
#q.request_ID = 'CreditCardCreditAddRq'
#q.AccountRef.ListID = '800000CE-1429728073' #Credit Card Account ///Credit Card:Suntrust
#q.TxnDate = '2015-06-07' # Date
#q.PayeeEntityRef.ListID = '800000CC-1414505910' # Payee by ListID
#q.ExpenseLineAdd.AccountRef.ListID = '800000B8-1357931163' # Split Account ///Suspense
#q.ExpenseLineAdd.Amount = '20.00' # Split Amount
#q.ExpenseLineAdd.Memo = 'Test Memo' # Memo
#q.add_request()


### Most Sales Receipt Entry
#q = request.add('')
#q.request_ID = 'SalesReceiptAddRq'
#q.CustomerRef.ListID = '800002A1-1418418550'
#q.AccountRef.ListID = '8000011A-1307586914' #Accounts Payable
#q.TxnDate = '2015-06-07' # Date
#q.SalesReceiptLineAdd.ItemRef.ListID = '8000006B-1418418514' # Item ID
#q.SalesReceiptLineAdd.Amount = '20.00' # Split Amount
#q.SalesReceiptLineAdd.Desc = 'Test Memo' # Memo
#q.add_request()


### Most Credit Memo Entry
#q = request.add('')
#q.request_ID = 'CreditMemoAddRq'
#q.CustomerRef.ListID = '800002A1-1418418550'
#q.AccountRef.ListID = '8000011A-1307586914' #Accounts Payable
#q.TxnDate = '2015-06-07' # Date
#q.CreditMemoLineAdd.ItemRef.ListID = '8000006B-1418418514' # Item ID
#q.CreditMemoLineAdd.Amount = '20.00' # Split Amount
#q.CreditMemoLineAdd.Desc = 'Test Memo' # Memo
#q.add_request()


print(q.response)
