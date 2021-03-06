from xml.etree import ElementTree as ET

__author__ = 'thecr8tr'

class empty_class():
    def __init__(self):
        pass

class search_parameter():
    def __init__(self):
        pass

    def set_attributes(self):

        # how to proceed once qbxml encounters an error
        self.onError = 'stopOnError' #options = stopOnError, continueOnError

        # returns a count of items to be returned
        self.metaData = 'NoMetaData' #options = NoMetaData, MetaDataOnly, MetaDataAndResponseData

        # sets request as an iterator/use Max Return to control how many items are sent at a time
        self.iterator = None #options = Start, Continue, Stop

        # returns only items with indicated name
        self.FullName = None #FullName comes from QB File and Must include Parents if applicable

        # returns only items with indicated list id number.
        # Be careful!!!, List ID's are only specific within lists.
        # (An id may be for a name and a transaction)
        self.ListID = None #ListID comes from QB File

        # limits the number of items returned
        self.MaxReturned = None #options = any integer greater than zero as a string

        # filters active status, default is ActiveOnly
        self.ActiveStatus = None #options = ActiveOnly, InactiveOnly, All

        # filters for items on or after specified date
        self.FromModifiedDate = None #options = YYYY+'-'+MM+'-'+DD[+'T'+hh[+':'+mm[+':'+ss[+'-'+hh+':'+mm]]]]

        # filters for items on or before specified date
        self.ToModifiedDate = None #options = YYYY+'-'+MM+'-'+DD[+'T'+hh[+':'+mm[+':'+ss[+'-'+hh+':'+mm]]]]

        # filters for object name
        self.NameFilter = empty_class()

        # NameFilter search parameters
        self.NameFilter.MatchCriterion = None # options = StartsWith, Contains, EndsWith

        # NameFilter search value (can be all or part)
        self.NameFilter.Name = None # user supplied string to match from

        # filters for object name between two user supplied names
        self.NameRangeFilter = empty_class()

        # NameRangeFilter search start value (omit to search from beginning of list)
        self.NameRangeFilter.FromName = None # user supplied string to start match

        # NameRangeFilter search end value (omit to search to end of list)
        self.NameRangeFilter.ToName = None # user supplied string to end match

        # Filters based on the amount of the total balance (includes sub accounts)
        self.TotalBalanceFilter = empty_class()

        # TotalBalanceFilter
        self.TotalBalanceFilter.Operator = None # options = LessThan, LessThanEqual, Equal, GreaterThan,
                                                          # GreaterThanEqual

        # TotalBalanceFilter amount to search for (customers and vendors only)
        self.TotalBalanceFilter.Amount = None # user supplied string of a 2 decimal place dollar amount

        # filters for object name between two user supplied names
        self.CurrencyFilter = empty_class()

        # CurrencyFilter
        self.CurrencyFilter.ListID = None # ListID comes from QB File

        # CurrencyFilter
        self.CurrencyFilter.FullName = None # FullName comes from QB File and Must include Parents if applicable

        # filters for object name between two user supplied names
        self.ClassFilter = empty_class()

        # ClassFilter
        self.ClassFilter.ListID = None # ListID comes from QB File

        # ClassFilter
        self.ClassFilter.FullName = None # FullName comes from QB File and Must include Parents if applicable

        # ClassFilter Returns item w/ ListID and its decendants
        self.ClassFilter.ListIDWithChildren = None # ListID comes from QB File

        # ClassFilter Returns item w/ FullName and its decendants
        self.ClassFilter.FullNameWithChildren = None # FullName comes from QB File and Must include Parents if applicable

        # Allows you to filter data
        self.IncludeRetElement = None # options = xml tags as a list

        # Refers to the owner of a data extension:
        # If OwnerID is 0, this is a public data extension, also known as a custom field. Custom fields appear
                # in the QuickBooks UI.
        # If OwnerID is a GUID, for example {6B063959-81B0-4622-85D6-F548C8CCB517}, this field is a private data
                # extension defined by an integrated application. Private data extensions do not appear in the
                # QuickBooks UI.
        # Note that OwnerID values are not case-sensitive, meaning that if you enter an OwnerID value with lower-case
                # letters, the value will be saved and returned with upper-case letters.
        # When you share a private data extension with another application, the other application must know both the
                # OwnerID and the DataExtName, as these together form a data extension's unique name.
        self.OwnerID = None # options = ????

        # Allows specification of Account type in AccountQueryRq only
        self.AccountType = None # options = Accounts Payable, Accounts Receivable, Bank, Credit Card....

        # Applicable to the ToDoQueryRq returns a done, not done, or both list of elements
        self.DoneStatus = None # options = NotDoneOnly(default), DoneOnly, All

        # filter for a certain transaction id or reference number, TxnID are unique
        self.TxnID = None # QuickBooks set item

        # This is based on a QuickBooks Supplied Date/Time
        self.ModifiedDateRangeFilter = empty_class()

        # This is based on a QuickBooks Supplied Date/Time
        self.ModifiedDateRangeFilter.FromModifiedDate = None #options = YYYY+'-'+MM+'-'+DD[+'T'+hh[+':'+mm[+':'+ss[+'-'+hh+':'+mm]]]]

        # This is based on a QuickBooks Supplied Date/Time
        self.ModifiedDateRangeFilter.ToModifiedDate = None #options = YYYY+'-'+MM+'-'+DD[+'T'+hh[+':'+mm[+':'+ss[+'-'+hh+':'+mm]]]]

        # This is based on the user Supplied Date
        self.TxnDateRangeFilter = empty_class()

        # This is based on a QuickBooks Supplied Date/Time
        self.TxnDateRangeFilter.FromTxnDate = None #options = YYYY+'-'+MM+'-'+DD

        # This is based on a QuickBooks Supplied Date/Time
        self.TxnDateRangeFilter.ToTxnDate = None #options = YYYY+'-'+MM+'-'+DD

        #
        self.DateMacro = None # options ThisWeekToDate, ThisMonthToDate, LastWeek, LastFiscalQuarter, LastFiscalYear...

        # EntityFilter
        self.EntityFilter = empty_class() # options FullName, ListID, FullNameWithChildren, or ListIDWithChildren

        # EntityFilter
        self.EntityFilter.ListID = None # ListID comes from QB File

        # EntityFilter
        self.EntityFilter.FullName = None # FullName comes from QB File and Must include Parents if applicable

        # EntityFilter Returns item w/ ListID and its decendants
        self.EntityFilter.ListIDWithChildren = None # ListID comes from QB File

        # EntityFilter Returns item w/ FullName and its decendants
        self.EntityFilter.FullNameWithChildren = None # FullName comes from QB File and Must include Parents if applicable

        # AccountFilter --- Only works on the main account Associated with trans (ie, bank account for check or deposit)
        self.AccountFilter = empty_class() # options FullName, ListID, FullNameWithChildren, or ListIDWithChildren

        # AccountFilter
        self.AccountFilter.ListID = None # ListID comes from QB File

        # AccountFilter
        self.AccountFilter.FullName = None # FullName comes from QB File and Must include Parents if applicable

        # AccountFilter Returns item w/ ListID and its decendants
        self.AccountFilter.ListIDWithChildren = None # ListID comes from QB File

        # AccountFilter Returns item w/ FullName and its decendants
        self.AccountFilter.FullNameWithChildren = None # FullName comes from QB File and Must include Parents if applicable

        # PaidStatus searches for invoices or bills that have been paid
        self.PaidStatus = None # options = All (default), PaidOnly, NotPaidOnly

        # IncludeLinkedTxns will show transactions that are linked to filtered transactions (ie a check that pays a bill)
        self.IncludeLinkedTxns = None # options = False (default), True

        # IncludeLineItems will show the transaction splits
        self.IncludeLineItems = None # option = False (default), True

        # TransactionQueryRq Specific
        self.TransactionFilter = None # options = specific transaction types or All

        # TransactionQueryRq Specific
        self.TransactionDetailLevelFilter = None # All, SummaryOnly, AllExceptSummary

        # TransactionQueryRq Specific
        self.TransactionPostingStatusFilter = None # Either, NonPosting, Posting

        # TransactionQueryRq Specific
        self.TransactionPaidStatusFilter = None # Either, Closed, Open

        # Insert value to define the case-insensitive name of a new list object
        self.Name = None # XML String type

        # This is a string not a python boolean
        self.RefNumber = None # true, false, 1, 0

        # CustomerAdd.ClassRef
        self.ClassRef = empty_class()

        # According to the docs, this is set automatically by QB when you add the item
        self.ClassRef.ListID = None

        # Use this to designate the hierarchy for the new item
        self.ClassRef.FullName = None

        # CustomerAdd.ClassRef
        self.ParentRef = empty_class()

        # According to the docs, this is set automatically by QB when you add the item
        self.ParentRef.ListID = None

        # Use this to designate the hierarchy for the new item
        self.ParentRef.FullName = None

        #
        self.CompanyName = None #

        #
        self.Salutation = None #

        #
        self.FirstName = None #

        #
        self.MiddleName = None #

        #
        self.LastName = None #

        #
        self.JobTitle = None #

        #
        self.BillAddress = empty_class() #

        #
        self.BillAddress.Addr1 = None #

        #
        self.BillAddress.Addr2 = None #

        #
        self.BillAddress.Addr3 = None #

        #
        self.BillAddress.Addr4 = None #

        #
        self.BillAddress.Addr5 = None #

        #
        self.BillAddress.City = None #

        #
        self.BillAddress.State = None #

        #
        self.BillAddress.PostalCode = None #

        #
        self.BillAddress.Country = None #

        #
        self.BillAddress.Note = None #

        #
        self.ShipAddress = empty_class() #

        #
        self.ShipAddress.Addr1 = None #

        #
        self.ShipAddress.Addr2 = None #

        #
        self.ShipAddress.Addr3 = None #

        #
        self.ShipAddress.Addr4 = None #

        #
        self.ShipAddress.Addr5 = None #

        #
        self.ShipAddress.City = None #

        #
        self.ShipAddress.State = None #

        #
        self.ShipAddress.PostalCode = None #

        #
        self.ShipAddress.Country = None #

        #
        self.ShipAddress.Note = None #

        #
        self.ShipToAddress = empty_class() #

        #
        self.ShipToAddress.Addr1 = None #

        #
        self.ShipToAddress.Addr2 = None #

        #
        self.ShipToAddress.Addr3 = None #

        #
        self.ShipToAddress.Addr4 = None #

        #
        self.ShipToAddress.Addr5 = None #

        #
        self.ShipToAddress.City = None #

        #
        self.ShipToAddress.State = None #

        #
        self.ShipToAddress.PostalCode = None #

        #
        self.ShipToAddress.Country = None #

        #
        self.ShipToAddress.Note = None #

        #
        self.ShipToAddress.DefaultShipTo = None #

        #
        self.Phone = None

        #
        self.AltPhone = None

        #
        self.Fax = None

        #
        self.Email = None

        #
        self.Cc = None

        #
        self.Contact = None

        #
        self.AltContact = None

        #
        self.AdditionalContactRef = empty_class() #

        #
        self.AdditionalContactRef.ContactName = None #

        #
        self.AdditionalContactRef.ContactValue = None #

        #
        self.Contacts = empty_class() #

        #
        self.Contacts.Salutation = None #

        #
        self.Contacts.FirstName = None #

        #
        self.Contacts.MiddleName = None #

        #
        self.Contacts.LastName = None #

        #
        self.Contacts.JobTitle = None #

        #
        self.Contacts.AdditionalContactRef = empty_class() #

        #
        self.Contacts.AdditionalContactRef.ContactName = None #

        #
        self.Contacts.AdditionalContactRef.ContactValue = None #

        #
        self.CustomerTypeRef = empty_class() #

        #
        self.CustomerTypeRef.ListID = None #

        #
        self.CustomerTypeRef.FullName = None #

        #
        self.TermsRef = empty_class() #

        #
        self.TermsRef.ListID = None #

        #
        self.TermsRef.FullName = None #

        #
        self.SalesRepRef = empty_class() #

        #
        self.SalesRepRef.ListID = None #

        #
        self.SalesRepRef.FullName = None #

        #
        self.OpenBalance = None #

        #
        self.OpenBalanceDate = None #

        #
        self.SalesTaxCodeRef = empty_class() #

        #
        self.SalesTaxCodeRef.ListID = None #

        #
        self.SalesTaxCodeRef.FullName = None #

        #
        self.ItemSalesTaxRef = empty_class() #

        #
        self.ItemSalesTaxRef.ListID = None #

        #
        self.ItemSalesTaxRef.FullName = None #

        #
        self.ResaleNumber = None #

        #
        self.AccountNumber = None #

        #
        self.CreditLimit = None #

        #
        self.PreferredPaymentMethodRef = empty_class() #

        #
        self.PreferredPaymentMethodRef.ListID = None #

        #
        self.PreferredPaymentMethodRef.FullName = None #

        #
        self.CreditCardInfo = empty_class() #

        #
        self.CreditCardInfo.CreditCardNumber = None #

        #
        self.CreditCardInfo.ExpirationMonth = None #

        #
        self.CreditCardInfo.ExpirationYear = None #

        #
        self.CreditCardInfo.NameOnCard = None #

        #
        self.CreditCardInfo.CreditCardAddress = None #

        #
        self.CreditCardInfo.CreditCardPostalCode = None #

        #
        self.JobStatus = None #

        #
        self.JobStartDate = None #

        #
        self.JobProjectedEndDate = None #

        #
        self.JobEndDate = None #

        #
        self.JobDesc = None #

        #
        self.JobTypeRef = empty_class() #

        #
        self.JobTypeRef.ListID = None #

        #
        self.JobTypeRef.FullName = None #

        #
        self.Notes = None #

        #
        self.AdditionalNotes = empty_class() #

        #
        self.AdditionalNotes.Notes = None #

        #
        self.PreferredDeliveryMethod = None #

        #
        self.PriceLevelRef = empty_class() #

        #
        self.PriceLevelRef.ListID = None #

        #
        self.PriceLevelRef.FullName = None #

        #
        self.ExternalGUID = None #

        #
        self.CurrencyRef = empty_class() #

        #
        self.CurrencyRef.ListID = None #

        #
        self.CurrencyRef.FullName = None #

        #
        self.AccountRef = empty_class() #

        #
        self.AccountRef.ListID = None #

        #
        self.AccountRef.FullName = None #

        #
        self.PayeeEntityRef = empty_class() #

        #
        self.PayeeEntityRef.ListID = None #

        #
        self.PayeeEntityRef.FullName = None #

        #
        self.TxnDate = None #

        #
        self.Memo = None #

        #
        self.Address = empty_class() #

        #
        self.Address.Addr1 = None #

        #
        self.Address.Addr2 = None #

        #
        self.Address.Addr3 = None #

        #
        self.Address.Addr4 = None #

        #
        self.Address.Addr5 = None #

        #
        self.Address.City = None #

        #
        self.Address.State = None #

        #
        self.Address.PostalCode = None #

        #
        self.Address.Country = None #

        #
        self.Address.Note = None #

        #
        self.IsToBePrinted = None #

        #
        self.ExchangeRate = None #

        #
        self.ApplyCheckToTxnAdd = empty_class() #

        #
        self.ApplyCheckToTxnAdd.TxnID = None #

        #
        self.ApplyCheckToTxnAdd.Amount = None #

        #
        self.ExpenseLineAdd = empty_class()#

        #
        self.ExpenseLineAdd.AccountRef = empty_class() #

        #
        self.ExpenseLineAdd.AccountRef.ListID = None #

        #
        self.ExpenseLineAdd.AccountRef.FullName = None #

        #
        self.ExpenseLineAdd.Amount = None #

        #
        self.ExpenseLineAdd.Memo = None #

        #
        self.ExpenseLineAdd.CustomerRef = empty_class() #

        #
        self.ExpenseLineAdd.CustomerRef.ListID = None #

        #
        self.ExpenseLineAdd.CustomerRef.FullName = None #

        #
        self.ExpenseLineAdd.ClassRef = empty_class() #

        #
        self.ExpenseLineAdd.ClassRef.ListID = None #

        #
        self.ExpenseLineAdd.ClassRef.FullName = None #

        #
        self.ExpenseLineAdd.BillableStatus = None #

        #
        self.ExpenseLineAdd.SalesRepRef = empty_class() #

        #
        self.ExpenseLineAdd.SalesRepRef.ListID = None #

        #
        self.ExpenseLineAdd.SalesRepRef.FullName = None #

        #
        self.ExpenseLineAdd.DataExt = empty_class() #

        #
        self.ExpenseLineAdd.DataExt.OwnerID = None #

        #
        self.ExpenseLineAdd.DataExt.DataExtName = None #

        #
        self.ExpenseLineAdd.DataExt.DataExtValue = None #

        #
        self.ItemLineAdd = empty_class() #

        #
        self.ItemLineAdd.ItemRef = empty_class() #

        #
        self.ItemLineAdd.ItemRef.ListID = None #

        #
        self.ItemLineAdd.ItemRef.FullName = None #

        #
        self.ItemLineAdd.InventorySiteRef = empty_class() #

        #
        self.ItemLineAdd.InventorySiteRef.ListID = None #

        #
        self.ItemLineAdd.InventorySiteRef.FullName = None #

        #
        self.ItemLineAdd.InventorySiteLocationRef = empty_class() #

        #
        self.ItemLineAdd.InventorySiteLocationRef.ListID = None #

        #
        self.ItemLineAdd.InventorySiteLocationRef.FullName = None #

        #
        self.ItemLineAdd.SerialNumber = None #

        #
        self.ItemLineAdd.LotNumber = None #

        #
        self.ItemLineAdd.Desc = None #

        #
        self.ItemLineAdd.Quantity = None #

        #
        self.ItemLineAdd.UnitOfMeasure = None #

        #
        self.ItemLineAdd.Cost = None #

        #
        self.ItemLineAdd.Amount = None #

        #
        self.ItemLineAdd.CustomerRef = empty_class() #

        #
        self.ItemLineAdd.CustomerRef.ListID = None #

        #
        self.ItemLineAdd.CustomerRef.FullName = None #

        #
        self.ItemLineAdd.ClassRef = empty_class() #

        #
        self.ItemLineAdd.ClassRef.ListID = None #

        #
        self.ItemLineAdd.ClassRef.FullName = None #

        #
        self.ItemLineAdd.BillableStatus = None #

        #
        self.ItemLineAdd.OverrideItemAccountRef = empty_class() #

        #
        self.ItemLineAdd.OverrideItemAccountRef.ListID = None #

        #
        self.ItemLineAdd.OverrideItemAccountRef.FullName = None #

        #
        self.ItemLineAdd.SalesRepRef = empty_class() #

        #
        self.ItemLineAdd.SalesRepRef.ListID = None #

        #
        self.ItemLineAdd.SalesRepRef.FullName = None #

        #
        self.ItemLineAdd.DataExt = empty_class() #

        #
        self.ItemLineAdd.DataExt.OwnerID = None #

        #
        self.ItemLineAdd.DataExt.DataExtName = None #

        #
        self.ItemLineAdd.DataExt.DataExtValue = None #

        #
        self.ItemGroupLineAdd = empty_class() #

        #
        self.ItemGroupLineAdd.ItemGroupRef = empty_class() #

        #
        self.ItemGroupLineAdd.ItemGroupRef.ListID = None #

        #
        self.ItemGroupLineAdd.ItemGroupRef.FullName = None #

        #
        self.ItemGroupLineAdd.Quantity = None #

        #
        self.ItemGroupLineAdd.UnitOfMeasure = None #

        #
        self.ItemGroupLineAdd.InventorySiteRef = empty_class() #

        #
        self.ItemGroupLineAdd.InventorySiteRef.ListID = None #

        #
        self.ItemGroupLineAdd.InventorySiteRef.FullName = None #

        #
        self.ItemGroupLineAdd.InventorySiteLocationRef = empty_class() #

        #
        self.ItemGroupLineAdd.InventorySiteLocationRef.ListID = None #

        #
        self.ItemGroupLineAdd.InventorySiteLocationRef.FullName = None #

        #
        self.ItemGroupLineAdd.DataExt = empty_class() #

        #
        self.ItemGroupLineAdd.DataExt.OwnerID = None #

        #
        self.ItemGroupLineAdd.DataExt.DataExtName = None #

        #
        self.ItemGroupLineAdd.DataExt.DataExtValue = None #

        #
        self.DepositToAccountRef = empty_class() #

        #
        self.DepositToAccountRef.ListID = None #

        #
        self.DepositToAccountRef.FullName = None #

        #
        self.DepositLineAdd = empty_class()

        #
        self.DepositLineAdd.PaymentTxnID = None #

        #
        self.DepositLineAdd.PaymentTxnLineID = None #

        #
        self.DepositLineAdd.OverrideMemo = None #

        #
        self.DepositLineAdd.OverrideCheckNumber = None #

        #
        self.DepositLineAdd.OverrideClassRef = empty_class() #

        #
        self.DepositLineAdd.OverrideClassRef.ListID = None #

        #
        self.DepositLineAdd.OverrideClassRef.FullName = None #

        #
        self.DepositLineAdd.EntityRef = empty_class() #

        #
        self.DepositLineAdd.EntityRef.ListID = None #

        #
        self.DepositLineAdd.EntityRef.FullName = None #

        #
        self.DepositLineAdd.AccountRef = empty_class() #

        #
        self.DepositLineAdd.AccountRef.ListID = None #

        #
        self.DepositLineAdd.AccountRef.FullName = None #

        #
        self.DepositLineAdd.Memo = None #

        #
        self.DepositLineAdd.CheckNumber = None #

        #
        self.DepositLineAdd.PaymentMethodRef = empty_class() #

        #
        self.DepositLineAdd.PaymentMethodRef.ListID = None #

        #
        self.DepositLineAdd.PaymentMethodRef.FullName = None #

        #
        self.DepositLineAdd.ClassRef = empty_class() #

        #
        self.DepositLineAdd.ClassRef.ListID = None #

        #
        self.DepositLineAdd.ClassRef.FullName = None #

        #
        self.DepositLineAdd.Amount = None #

        #
        self.CashBackInfoAdd = empty_class() #

        #
        self.CashBackInfoAdd.AccountRef = empty_class() #

        #
        self.CashBackInfoAdd.AccountRef.ListID = None #

        #
        self.CashBackInfoAdd.AccountRef.FullName = None #

        #
        self.CashBackInfoAdd.Memo = None #

        #
        self.CashBackInfoAdd.Amount = None #

        #
        self.CustomerRef = empty_class()

        #
        self.CustomerRef.ListID = None

        #
        self.CustomerRef.FullName = None

        #
        self.SalesReceiptLineAdd = empty_class()

        #
        self.SalesReceiptLineAdd.ItemRef = empty_class()

        #
        self.SalesReceiptLineAdd.ItemRef.ListID = None

        #
        self.SalesReceiptLineAdd.ItemRef.FullName = None

        #
        self.SalesReceiptLineAdd.Desc = None

        #
        self.SalesReceiptLineAdd.Quantity = None

        #
        self.SalesReceiptLineAdd.UnitOfMeasure = None

        #
        self.SalesReceiptLineAdd.Rate = None

        #
        self.SalesReceiptLineAdd.RatePercent = None

        #
        self.SalesReceiptLineAdd.PriceLevelRef = empty_class()

        #
        self.SalesReceiptLineAdd.PriceLevelRef.ListID = None

        #
        self.SalesReceiptLineAdd.PriceLevelRef.FullName = None

        #
        self.SalesReceiptLineAdd.ClassRef = empty_class()

        #
        self.SalesReceiptLineAdd.ClassRef.ListID = None

        #
        self.SalesReceiptLineAdd.ClassRef.FullName = None

        #
        self.SalesReceiptLineAdd.Amount = None

        #
        self.SalesReceiptLineAdd.OptionForPriceRuleConflict = None

        #
        self.SalesReceiptLineAdd.InventorySiteRef = empty_class()

        #
        self.SalesReceiptLineAdd.InventorySiteRef.ListID = None

        #
        self.SalesReceiptLineAdd.InventorySiteRef.FullName = None

        #
        self.SalesReceiptLineAdd.InventorySiteLocationRef = empty_class()

        #
        self.SalesReceiptLineAdd.InventorySiteLocationRef.ListID = None

        #
        self.SalesReceiptLineAdd.InventorySiteLocationRef.FullName = None

        #
        self.SalesReceiptLineAdd.SerialNumber = None

        #
        self.SalesReceiptLineAdd.LotNumber = None

        #
        self.SalesReceiptLineAdd.ServiceDate = None

        #
        self.SalesReceiptLineAdd.SalesTaxCodeRef = empty_class()

        #
        self.SalesReceiptLineAdd.SalesTaxCodeRef.ListID = None

        #
        self.SalesReceiptLineAdd.SalesTaxCodeRef.FullName = None

        #
        self.SalesReceiptLineAdd.OverrideItemAccountRef = empty_class()

        #
        self.SalesReceiptLineAdd.OverrideItemAccountRef.ListID = None

        #
        self.SalesReceiptLineAdd.OverrideItemAccountRef.FullName = None

        #
        self.SalesReceiptLineAdd.Other1 = None

        #
        self.SalesReceiptLineAdd.Other2 = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo = empty_class()

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo = empty_class()

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardNumber = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationMonth = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationYear = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.NameOnCard = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardAddress = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardPostalCode = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CommercialCardCode = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.TransactionMode = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardTxnType = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo = empty_class()

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultCode = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultMessage = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.CreditCardTransID = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.MerchantAccountNumber = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AuthorizationCode = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSStreet = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSZip = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.CardSecurityCodeMatch = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ReconBatchID = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentGroupingCode = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentStatus = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationTime = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationStamp = None

        #
        self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ClientTransID = None

        #
        self.SalesReceiptLineAdd.DataExt = empty_class()

        #
        self.SalesReceiptLineAdd.DataExt.OwnerID = None

        #
        self.SalesReceiptLineAdd.DataExt.DataExtName = None

        #
        self.SalesReceiptLineAdd.DataExt.DataExtValue = None

        #
        self.SalesReceiptLineAdd.ItemGroupRef = empty_class() #

        #
        self.SalesReceiptLineAdd.ItemGroupRef.ListID = None #

        #
        self.SalesReceiptLineAdd.ItemGroupRef.FullName = None #

        #
        self.SalesReceiptLineAdd.Quantity = None #

        #
        self.SalesReceiptLineAdd.UnitOfMeasure = None #

        #
        self.SalesReceiptLineAdd.InventorySiteRef = empty_class() #

        #
        self.SalesReceiptLineAdd.InventorySiteRef.ListID = None #

        #
        self.SalesReceiptLineAdd.InventorySiteRef.FullName = None #

        #
        self.SalesReceiptLineAdd.InventorySiteLocationRef = empty_class() #

        #
        self.SalesReceiptLineAdd.InventorySiteLocationRef.ListID = None #

        #
        self.SalesReceiptLineAdd.InventorySiteLocationRef.FullName = None #

        #
        self.SalesReceiptLineAdd.DataExt = empty_class() #

        #
        self.SalesReceiptLineAdd.DataExt.OwnerID = None #

        #
        self.SalesReceiptLineAdd.DataExt.DataExtName = None #

        #
        self.SalesReceiptLineAdd.DataExt.DataExtValue = None #

        #
        self.TemplateRef = empty_class()

        #
        self.TemplateRef.ListID = None

        #
        self.TemplateRef.FullName = None

        #
        self.IsPending = None

        #
        self.CheckNumber = None

        #
        self.PaymentMethodRef = empty_class()

        #
        self.PaymentMethodRef.ListID = None

        #
        self.PaymentMethodRef.FullName = None

        #
        self.DueDate = None

        #
        self.ShipDate = None

        #
        self.ShipMethodRef = empty_class()

        #
        self.ShipMethodRef.ListID = None

        #
        self.ShipMethodRef.FullName = None

        #
        self.FOB = None

        #
        self.CustomerMsgRef = empty_class()

        #
        self.CustomerMsgRef.ListID = None

        #
        self.CustomerMsgRef.FullName = None

        #
        self.IsToBeEmailed = None

        #
        self.CustomerSalesTaxCodeRef = empty_class()

        #
        self.CustomerSalesTaxCodeRef.ListID = None

        #
        self.CustomerSalesTaxCodeRef.FullName = None

        #
        self.CreditCardTxnInfo = empty_class()

        #
        self.CreditCardTxnInfo.CreditCardTxnInputInfo = empty_class()

        #
        self.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardNumber = None

        #
        self.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationMonth = None

        #
        self.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationYear = None

        #
        self.CreditCardTxnInfo.CreditCardTxnInputInfo.NameOnCard = None

        #
        self.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardAddress = None

        #
        self.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardPostalCode = None

        #
        self.CreditCardTxnInfo.CreditCardTxnInputInfo.CommercialCardCode = None

        #
        self.CreditCardTxnInfo.CreditCardTxnInputInfo.TransactionMode = None

        #
        self.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardTxnType = None

        #
        self.CreditCardTxnInfo.CreditCardTxnResultInfo = empty_class()

        #
        self.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultCode = None

        #
        self.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultMessage = None

        #
        self.CreditCardTxnInfo.CreditCardTxnResultInfo.CreditCardTransID = None

        #
        self.CreditCardTxnInfo.CreditCardTxnResultInfo.MerchantAccountNumber = None

        #
        self.CreditCardTxnInfo.CreditCardTxnResultInfo.AuthorizationCode = None

        #
        self.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSStreet = None

        #
        self.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSZip = None

        #
        self.CreditCardTxnInfo.CreditCardTxnResultInfo.CardSecurityCodeMatch = None

        #
        self.CreditCardTxnInfo.CreditCardTxnResultInfo.ReconBatchID = None

        #
        self.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentGroupingCode = None

        #
        self.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentStatus = None

        #
        self.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationTime = None

        #
        self.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationStamp = None

        #
        self.CreditCardTxnInfo.CreditCardTxnResultInfo.ClientTransID = None

        #
        self.Other = None

        #
        self.PaymentMethodType = None

        #
        self.CreditMemoLineAdd = empty_class()

        #
        self.CreditMemoLineAdd.ItemRef = empty_class()

        #
        self.CreditMemoLineAdd.ItemRef.ListID = None

        #
        self.CreditMemoLineAdd.ItemRef.FullName = None

        #
        self.CreditMemoLineAdd.Desc = None

        #
        self.CreditMemoLineAdd.Quantity = None

        #
        self.CreditMemoLineAdd.UnitOfMeasure = None

        #
        self.CreditMemoLineAdd.Rate = None

        #
        self.CreditMemoLineAdd.RatePercent = None

        #
        self.CreditMemoLineAdd.PriceLevelRef = empty_class()

        #
        self.CreditMemoLineAdd.PriceLevelRef.ListID = None

        #
        self.CreditMemoLineAdd.PriceLevelRef.FullName = None

        #
        self.CreditMemoLineAdd.ClassRef = empty_class()

        #
        self.CreditMemoLineAdd.ClassRef.ListID = None

        #
        self.CreditMemoLineAdd.ClassRef.FullName = None

        #
        self.CreditMemoLineAdd.Amount = None

        #
        self.CreditMemoLineAdd.InventorySiteRef = empty_class()

        #
        self.CreditMemoLineAdd.InventorySiteRef.ListID = None

        #
        self.CreditMemoLineAdd.InventorySiteRef.FullName = None

        #
        self.CreditMemoLineAdd.InventorySiteLocationRef = empty_class()

        #
        self.CreditMemoLineAdd.InventorySiteLocationRef.ListID = None

        #
        self.CreditMemoLineAdd.InventorySiteLocationRef.FullName = None

        #
        self.CreditMemoLineAdd.SerialNumber = None

        #
        self.CreditMemoLineAdd.LotNumber = None

        #
        self.CreditMemoLineAdd.ServiceDate = None

        #
        self.CreditMemoLineAdd.SalesTaxCodeRef = empty_class()

        #
        self.CreditMemoLineAdd.SalesTaxCodeRef.ListID = None

        #
        self.CreditMemoLineAdd.SalesTaxCodeRef.FullName = None

        #
        self.CreditMemoLineAdd.OverrideItemAccountRef = empty_class()

        #
        self.CreditMemoLineAdd.OverrideItemAccountRef.ListID = None

        #
        self.CreditMemoLineAdd.OverrideItemAccountRef.FullName = None

        #
        self.CreditMemoLineAdd.Other1 = None

        #
        self.CreditMemoLineAdd.Other2 = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo = empty_class()

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo = empty_class()

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardNumber = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationMonth = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationYear = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.NameOnCard = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardAddress = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardPostalCode = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CommercialCardCode = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.TransactionMode = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardTxnType = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo = empty_class()

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultCode = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultMessage = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.CreditCardTransID = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.MerchantAccountNumber = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AuthorizationCode = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSStreet = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSZip = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.CardSecurityCodeMatch = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ReconBatchID = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentGroupingCode = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentStatus = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationTime = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationStamp = None

        #
        self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ClientTransID = None

        #
        self.CreditMemoLineAdd.DataExt = empty_class()

        #
        self.CreditMemoLineAdd.DataExt.OwnerID = None

        #
        self.CreditMemoLineAdd.DataExt.DataExtName = None

        #
        self.CreditMemoLineAdd.DataExt.DataExtValue = None

        #
        self.CreditMemoLineAdd.ItemGroupRef = empty_class() #

        #
        self.CreditMemoLineAdd.ItemGroupRef.ListID = None #

        #
        self.CreditMemoLineAdd.ItemGroupRef.FullName = None #

        #
        self.CreditMemoLineAdd.Quantity = None #

        #
        self.CreditMemoLineAdd.UnitOfMeasure = None #

        #
        self.CreditMemoLineAdd.InventorySiteRef = empty_class() #

        #
        self.CreditMemoLineAdd.InventorySiteRef.ListID = None #

        #
        self.CreditMemoLineAdd.InventorySiteRef.FullName = None #

        #
        self.CreditMemoLineAdd.InventorySiteLocationRef = empty_class() #

        #
        self.CreditMemoLineAdd.InventorySiteLocationRef.ListID = None #

        #
        self.CreditMemoLineAdd.InventorySiteLocationRef.FullName = None #

        #
        self.CreditMemoLineAdd.DataExt = empty_class() #

        #
        self.CreditMemoLineAdd.DataExt.OwnerID = None #

        #
        self.CreditMemoLineAdd.DataExt.DataExtName = None #

        #
        self.CreditMemoLineAdd.DataExt.DataExtValue = None #

        #
        self.ARAccountRef = empty_class()

        #
        self.ARAccountRef.ListID = None

        #
        self.ARAccountRef.FullName = None

        #
        self.PONumber = None

    def set_AccountQueryRq_attributes(self):
        '''
        WARNING NEED TO CHECK ATTRIBUTES
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.AccountQueryRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, self.request_ID)
        self.qbcom.AccountQueryRq.set('metaData', self.metaData)
        if self.iterator:
            self.qbcom.AccountQueryRq.set('iterator', self.iterator)
        if self.ListID:
            self.qbcom.ListID = ET.SubElement(self.qbcom.AccountQueryRq, 'ListID')
            self.qbcom.ListID.text = self.ListID
        elif self.FullName:
            self.qbcom.FullName = ET.SubElement(self.qbcom.AccountQueryRq, 'FullName')
            self.qbcom.FullName.text = self.FullName
        else:
            if self.MaxReturned:
                self.qbcom.MaxReturned = ET.SubElement(self.qbcom.AccountQueryRq, 'MaxReturned')
                self.qbcom.MaxReturned.text = self.MaxReturned
            if self.ActiveStatus:
                self.qbcom.ActiveStatus = ET.SubElement(self.qbcom.AccountQueryRq, 'ActiveStatus')
                self.qbcom.ActiveStatus.text = self.ActiveStatus
            if self.FromModifiedDate:
                self.qbcom.FromModifiedDate = ET.SubElement(self.qbcom.AccountQueryRq, 'FromModifiedDate')
                self.qbcom.FromModifiedDate.text = self.FromModifiedDate
            if self.ToModifiedDate:
                self.qbcom.ToModifiedDate = ET.SubElement(self.qbcom.AccountQueryRq, 'ToModifiedDate')
                self.qbcom.ToModifiedDate.text = self.ToModifiedDate
            if self.NameFilter.MatchCriterion and self.Namefilter.Name:
                self.qbcom.NameFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'NameFilter')
                self.qbcom.NameFilter.text = self.NameFilter
                self.qbcom.MatchCriterion = ET.SubElement(self.qbcom.NameFilter, 'MatchCriterion')
                self.qbcom.MatchCriterion.text = self.MatchCriterion
                self.qbcom.Name = ET.SubElement(self.qbcom.NameFilter, 'Name')
                self.qbcom.Name.text = self.Name
            elif self.NameRangeFilter.FromName and self.NameRangeFilter.ToName:
                self.qbcom.NameRangeFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'NameRangeFilter')
                self.qbcom.NameRangeFilter.text = self.NameRangeFilter
                self.qbcom.FromName = ET.SubElement(self.qbcom.NameRangeFilter, 'FromName')
                self.qbcom.FromName.text = self.FromName
                self.qbcom.ToName = ET.SubElement(self.qbcom.NameRangeFilter, 'ToName')
                self.qbcom.ToName.text = self.ToName
            if self.TotalBalanceFilter.Operator and self.TotalBalanceFilter.Amount:
                self.qbcom.TotalBalanceFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'TotalBalanceFilter')
                self.qbcom.TotalBalanceFilter.text = self.TotalBalanceFilter
                self.qbcom.Operator = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Operator')
                self.qbcom.Operator.text = self.Operator
                self.qbcom.Amount = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Amount')
                self.qbcom.Amount.text = self.Amount
            if self.CurrencyFilter.ListID:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.CurrencyFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.CurrencyFilter.FullName:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.CurrencyFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            if self.ClassFilter.ListID:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.ClassFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.ClassFilter.FullName:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.ClassFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            elif self.ClassFilter.ListIDWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListIDWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'ListIDWithChildren')
                self.qbcom.ListIDWithChildren.text = self.ListIDWithChildren
            elif self.ClassFilter.FullNameWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.AccountQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullNameWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'FullNameWithChildren')
                self.qbcom.FullNameWithChildren.text = self.FullNameWithChildren
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.AccountQueryRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item
        if self.OwnerID:
                self.qbcom.OwnerID = ET.SubElement(self.qbcom.AccountQueryRq, 'OwnerID')
                self.qbcom.OwnerID.text = self.OwnerID

    def set_CheckQueryRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.CheckQueryRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, self.request_ID)
        self.qbcom.CheckQueryRq.set('metaData', self.metaData)
        if self.iterator:
            self.qbcom.CheckQueryRq.set('iterator', self.iterator)
        if self.ListID:
            self.qbcom.ListID = ET.SubElement(self.qbcom.CheckQueryRq, 'ListID')
            self.qbcom.ListID.text = self.ListID
        elif self.FullName:
            self.qbcom.FullName = ET.SubElement(self.qbcom.CheckQueryRq, 'FullName')
            self.qbcom.FullName.text = self.FullName
        else:
            if self.MaxReturned:
                self.qbcom.MaxReturned = ET.SubElement(self.qbcom.CheckQueryRq, 'MaxReturned')
                self.qbcom.MaxReturned.text = self.MaxReturned
            if self.ActiveStatus:
                self.qbcom.ActiveStatus = ET.SubElement(self.qbcom.CheckQueryRq, 'ActiveStatus')
                self.qbcom.ActiveStatus.text = self.ActiveStatus
            if self.FromModifiedDate:
                self.qbcom.FromModifiedDate = ET.SubElement(self.qbcom.CheckQueryRq, 'FromModifiedDate')
                self.qbcom.FromModifiedDate.text = self.FromModifiedDate
            if self.ToModifiedDate:
                self.qbcom.ToModifiedDate = ET.SubElement(self.qbcom.CheckQueryRq, 'ToModifiedDate')
                self.qbcom.ToModifiedDate.text = self.ToModifiedDate
            if self.NameFilter.MatchCriterion and self.Namefilter.Name:
                self.qbcom.NameFilter = ET.SubElement(self.qbcom.CheckQueryRq, 'NameFilter')
                self.qbcom.NameFilter.text = self.NameFilter
                self.qbcom.MatchCriterion = ET.SubElement(self.qbcom.NameFilter, 'MatchCriterion')
                self.qbcom.MatchCriterion.text = self.MatchCriterion
                self.qbcom.Name = ET.SubElement(self.qbcom.NameFilter, 'Name')
                self.qbcom.Name.text = self.Name
            elif self.NameRangeFilter.FromName and self.NameRangeFilter.ToName:
                self.qbcom.NameRangeFilter = ET.SubElement(self.qbcom.CheckQueryRq, 'NameRangeFilter')
                self.qbcom.NameRangeFilter.text = self.NameRangeFilter
                self.qbcom.FromName = ET.SubElement(self.qbcom.NameRangeFilter, 'FromName')
                self.qbcom.FromName.text = self.FromName
                self.qbcom.ToName = ET.SubElement(self.qbcom.NameRangeFilter, 'ToName')
                self.qbcom.ToName.text = self.ToName
            if self.TotalBalanceFilter.Operator and self.TotalBalanceFilter.Amount:
                self.qbcom.TotalBalanceFilter = ET.SubElement(self.qbcom.CheckQueryRq, 'TotalBalanceFilter')
                self.qbcom.TotalBalanceFilter.text = self.TotalBalanceFilter
                self.qbcom.Operator = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Operator')
                self.qbcom.Operator.text = self.Operator
                self.qbcom.Amount = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Amount')
                self.qbcom.Amount.text = self.Amount
            if self.CurrencyFilter.ListID:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.CheckQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.CurrencyFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.CurrencyFilter.FullName:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.CheckQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.CurrencyFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            if self.ClassFilter.ListID:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.CheckQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.ClassFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.ClassFilter.FullName:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.CheckQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.ClassFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            elif self.ClassFilter.ListIDWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.CheckQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListIDWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'ListIDWithChildren')
                self.qbcom.ListIDWithChildren.text = self.ListIDWithChildren
            elif self.ClassFilter.FullNameWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.CheckQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullNameWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'FullNameWithChildren')
                self.qbcom.FullNameWithChildren.text = self.FullNameWithChildren
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.CheckQueryRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item
        if self.OwnerID:
                self.qbcom.OwnerID = ET.SubElement(self.qbcom.CheckQueryRq, 'OwnerID')
                self.qbcom.OwnerID.text = self.OwnerID

    def set_CustomerQueryRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        if self.onError:
            self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.CustomerQueryRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, self.request_ID)
        if self.metaData:
            self.qbcom.CustomerQueryRq.set('metaData', self.metaData)
        if self.iterator:
            self.qbcom.CustomerQueryRq.set('iterator', self.iterator)
        if self.ListID:
            self.qbcom.ListID = ET.SubElement(self.qbcom.CustomerQueryRq, 'ListID')
            self.qbcom.ListID.text = self.ListID
        elif self.FullName:
            self.qbcom.FullName = ET.SubElement(self.qbcom.CustomerQueryRq, 'FullName')
            self.qbcom.FullName.text = self.FullName
        else:
            if self.MaxReturned:
                self.qbcom.MaxReturned = ET.SubElement(self.qbcom.CustomerQueryRq, 'MaxReturned')
                self.qbcom.MaxReturned.text = self.MaxReturned
            if self.ActiveStatus:
                self.qbcom.ActiveStatus = ET.SubElement(self.qbcom.CustomerQueryRq, 'ActiveStatus')
                self.qbcom.ActiveStatus.text = self.ActiveStatus
            if self.FromModifiedDate:
                self.qbcom.FromModifiedDate = ET.SubElement(self.qbcom.CustomerQueryRq, 'FromModifiedDate')
                self.qbcom.FromModifiedDate.text = self.FromModifiedDate
            if self.ToModifiedDate:
                self.qbcom.ToModifiedDate = ET.SubElement(self.qbcom.CustomerQueryRq, 'ToModifiedDate')
                self.qbcom.ToModifiedDate.text = self.ToModifiedDate
            if self.NameFilter.MatchCriterion and self.Namefilter.Name:
                self.qbcom.NameFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'NameFilter')
                self.qbcom.NameFilter.text = self.NameFilter
                self.qbcom.MatchCriterion = ET.SubElement(self.qbcom.NameFilter, 'MatchCriterion')
                self.qbcom.MatchCriterion.text = self.MatchCriterion
                self.qbcom.Name = ET.SubElement(self.qbcom.NameFilter, 'Name')
                self.qbcom.Name.text = self.Name
            elif self.NameRangeFilter.FromName and self.NameRangeFilter.ToName:
                self.qbcom.NameRangeFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'NameRangeFilter')
                self.qbcom.NameRangeFilter.text = self.NameRangeFilter
                self.qbcom.FromName = ET.SubElement(self.qbcom.NameRangeFilter, 'FromName')
                self.qbcom.FromName.text = self.FromName
                self.qbcom.ToName = ET.SubElement(self.qbcom.NameRangeFilter, 'ToName')
                self.qbcom.ToName.text = self.ToName
            if self.TotalBalanceFilter.Operator and self.TotalBalanceFilter.Amount:
                self.qbcom.TotalBalanceFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'TotalBalanceFilter')
                self.qbcom.TotalBalanceFilter.text = self.TotalBalanceFilter
                self.qbcom.Operator = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Operator')
                self.qbcom.Operator.text = self.Operator
                self.qbcom.Amount = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Amount')
                self.qbcom.Amount.text = self.Amount
            if self.CurrencyFilter.ListID:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.CurrencyFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.CurrencyFilter.FullName:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.CurrencyFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            if self.ClassFilter.ListID:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.ClassFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.ClassFilter.FullName:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.ClassFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            elif self.ClassFilter.ListIDWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListIDWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'ListIDWithChildren')
                self.qbcom.ListIDWithChildren.text = self.ListIDWithChildren
            elif self.ClassFilter.FullNameWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.CustomerQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullNameWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'FullNameWithChildren')
                self.qbcom.FullNameWithChildren.text = self.FullNameWithChildren
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.CustomerQueryRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item
        if self.OwnerID:
                self.qbcom.OwnerID = ET.SubElement(self.qbcom.CustomerQueryRq, 'OwnerID')
                self.qbcom.OwnerID.text = self.OwnerID

    def set_DepositQueryRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.DepositQueryRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, self.request_ID)
        self.qbcom.DepositQueryRq.set('metaData', self.metaData)
        if self.iterator:
            self.qbcom.DepositQueryRq.set('iterator', self.iterator)
        if self.ListID:
            self.qbcom.ListID = ET.SubElement(self.qbcom.DepositQueryRq, 'ListID')
            self.qbcom.ListID.text = self.ListID
        elif self.FullName:
            self.qbcom.FullName = ET.SubElement(self.qbcom.DepositQueryRq, 'FullName')
            self.qbcom.FullName.text = self.FullName
        else:
            if self.MaxReturned:
                self.qbcom.MaxReturned = ET.SubElement(self.qbcom.DepositQueryRq, 'MaxReturned')
                self.qbcom.MaxReturned.text = self.MaxReturned
            if self.ActiveStatus:
                self.qbcom.ActiveStatus = ET.SubElement(self.qbcom.DepositQueryRq, 'ActiveStatus')
                self.qbcom.ActiveStatus.text = self.ActiveStatus
            if self.FromModifiedDate:
                self.qbcom.FromModifiedDate = ET.SubElement(self.qbcom.DepositQueryRq, 'FromModifiedDate')
                self.qbcom.FromModifiedDate.text = self.FromModifiedDate
            if self.ToModifiedDate:
                self.qbcom.ToModifiedDate = ET.SubElement(self.qbcom.DepositQueryRq, 'ToModifiedDate')
                self.qbcom.ToModifiedDate.text = self.ToModifiedDate
            if self.NameFilter.MatchCriterion and self.Namefilter.Name:
                self.qbcom.NameFilter = ET.SubElement(self.qbcom.DepositQueryRq, 'NameFilter')
                self.qbcom.NameFilter.text = self.NameFilter
                self.qbcom.MatchCriterion = ET.SubElement(self.qbcom.NameFilter, 'MatchCriterion')
                self.qbcom.MatchCriterion.text = self.MatchCriterion
                self.qbcom.Name = ET.SubElement(self.qbcom.NameFilter, 'Name')
                self.qbcom.Name.text = self.Name
            elif self.NameRangeFilter.FromName and self.NameRangeFilter.ToName:
                self.qbcom.NameRangeFilter = ET.SubElement(self.qbcom.DepositQueryRq, 'NameRangeFilter')
                self.qbcom.NameRangeFilter.text = self.NameRangeFilter
                self.qbcom.FromName = ET.SubElement(self.qbcom.NameRangeFilter, 'FromName')
                self.qbcom.FromName.text = self.FromName
                self.qbcom.ToName = ET.SubElement(self.qbcom.NameRangeFilter, 'ToName')
                self.qbcom.ToName.text = self.ToName
            if self.TotalBalanceFilter.Operator and self.TotalBalanceFilter.Amount:
                self.qbcom.TotalBalanceFilter = ET.SubElement(self.qbcom.DepositQueryRq, 'TotalBalanceFilter')
                self.qbcom.TotalBalanceFilter.text = self.TotalBalanceFilter
                self.qbcom.Operator = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Operator')
                self.qbcom.Operator.text = self.Operator
                self.qbcom.Amount = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Amount')
                self.qbcom.Amount.text = self.Amount
            if self.CurrencyFilter.ListID:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.DepositQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.CurrencyFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.CurrencyFilter.FullName:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.DepositQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.CurrencyFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            if self.ClassFilter.ListID:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.DepositQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.ClassFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.ClassFilter.FullName:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.DepositQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.ClassFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            elif self.ClassFilter.ListIDWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.DepositQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListIDWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'ListIDWithChildren')
                self.qbcom.ListIDWithChildren.text = self.ListIDWithChildren
            elif self.ClassFilter.FullNameWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.DepositQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullNameWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'FullNameWithChildren')
                self.qbcom.FullNameWithChildren.text = self.FullNameWithChildren
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.DepositQueryRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item
        if self.OwnerID:
                self.qbcom.OwnerID = ET.SubElement(self.qbcom.DepositQueryRq, 'OwnerID')
                self.qbcom.OwnerID.text = self.OwnerID

    def set_ItemQueryRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.ItemQueryRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, self.request_ID)
        self.qbcom.ItemQueryRq.set('metaData', self.metaData)
        if self.iterator:
            self.qbcom.ItemQueryRq.set('iterator', self.iterator)
        if self.ListID:
            self.qbcom.ListID = ET.SubElement(self.qbcom.ItemQueryRq, 'ListID')
            self.qbcom.ListID.text = self.ListID
        elif self.FullName:
            self.qbcom.FullName = ET.SubElement(self.qbcom.ItemQueryRq, 'FullName')
            self.qbcom.FullName.text = self.FullName
        else:
            if self.MaxReturned:
                self.qbcom.MaxReturned = ET.SubElement(self.qbcom.ItemQueryRq, 'MaxReturned')
                self.qbcom.MaxReturned.text = self.MaxReturned
            if self.ActiveStatus:
                self.qbcom.ActiveStatus = ET.SubElement(self.qbcom.ItemQueryRq, 'ActiveStatus')
                self.qbcom.ActiveStatus.text = self.ActiveStatus
            if self.FromModifiedDate:
                self.qbcom.FromModifiedDate = ET.SubElement(self.qbcom.ItemQueryRq, 'FromModifiedDate')
                self.qbcom.FromModifiedDate.text = self.FromModifiedDate
            if self.ToModifiedDate:
                self.qbcom.ToModifiedDate = ET.SubElement(self.qbcom.ItemQueryRq, 'ToModifiedDate')
                self.qbcom.ToModifiedDate.text = self.ToModifiedDate
            if self.NameFilter.MatchCriterion and self.Namefilter.Name:
                self.qbcom.NameFilter = ET.SubElement(self.qbcom.ItemQueryRq, 'NameFilter')
                self.qbcom.NameFilter.text = self.NameFilter
                self.qbcom.MatchCriterion = ET.SubElement(self.qbcom.NameFilter, 'MatchCriterion')
                self.qbcom.MatchCriterion.text = self.MatchCriterion
                self.qbcom.Name = ET.SubElement(self.qbcom.NameFilter, 'Name')
                self.qbcom.Name.text = self.Name
            elif self.NameRangeFilter.FromName and self.NameRangeFilter.ToName:
                self.qbcom.NameRangeFilter = ET.SubElement(self.qbcom.ItemQueryRq, 'NameRangeFilter')
                self.qbcom.NameRangeFilter.text = self.NameRangeFilter
                self.qbcom.FromName = ET.SubElement(self.qbcom.NameRangeFilter, 'FromName')
                self.qbcom.FromName.text = self.FromName
                self.qbcom.ToName = ET.SubElement(self.qbcom.NameRangeFilter, 'ToName')
                self.qbcom.ToName.text = self.ToName
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.ItemQueryRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item
        if self.OwnerID:
                self.qbcom.OwnerID = ET.SubElement(self.qbcom.ItemQueryRq, 'OwnerID')
                self.qbcom.OwnerID.text = self.OwnerID

    def set_PaymentMethodQueryRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.PaymentMethodQueryRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, self.request_ID)
        self.qbcom.PaymentMethodQueryRq.set('metaData', self.metaData)
        if self.ListID:
            self.qbcom.ListID = ET.SubElement(self.qbcom.PaymentMethodQueryRq, 'ListID')
            self.qbcom.ListID.text = self.ListID
        elif self.FullName:
            self.qbcom.FullName = ET.SubElement(self.qbcom.PaymentMethodQueryRq, 'FullName')
            self.qbcom.FullName.text = self.FullName
        else:
            if self.MaxReturned:
                self.qbcom.MaxReturned = ET.SubElement(self.qbcom.PaymentMethodQueryRq, 'MaxReturned')
                self.qbcom.MaxReturned.text = self.MaxReturned
            if self.ActiveStatus:
                self.qbcom.ActiveStatus = ET.SubElement(self.qbcom.PaymentMethodQueryRq, 'ActiveStatus')
                self.qbcom.ActiveStatus.text = self.ActiveStatus
            if self.FromModifiedDate:
                self.qbcom.FromModifiedDate = ET.SubElement(self.qbcom.PaymentMethodQueryRq, 'FromModifiedDate')
                self.qbcom.FromModifiedDate.text = self.FromModifiedDate
            if self.ToModifiedDate:
                self.qbcom.ToModifiedDate = ET.SubElement(self.qbcom.PaymentMethodQueryRq, 'ToModifiedDate')
                self.qbcom.ToModifiedDate.text = self.ToModifiedDate
            if self.NameFilter.MatchCriterion and self.Namefilter.Name:
                self.qbcom.NameFilter = ET.SubElement(self.qbcom.PaymentMethodQueryRq, 'NameFilter')
                self.qbcom.NameFilter.text = self.NameFilter
                self.qbcom.MatchCriterion = ET.SubElement(self.qbcom.NameFilter, 'MatchCriterion')
                self.qbcom.MatchCriterion.text = self.MatchCriterion
                self.qbcom.Name = ET.SubElement(self.qbcom.NameFilter, 'Name')
                self.qbcom.Name.text = self.Name
            elif self.NameRangeFilter.FromName and self.NameRangeFilter.ToName:
                self.qbcom.NameRangeFilter = ET.SubElement(self.qbcom.PaymentMethodQueryRq, 'NameRangeFilter')
                self.qbcom.NameRangeFilter.text = self.NameRangeFilter
                self.qbcom.FromName = ET.SubElement(self.qbcom.NameRangeFilter, 'FromName')
                self.qbcom.FromName.text = self.FromName
                self.qbcom.ToName = ET.SubElement(self.qbcom.NameRangeFilter, 'ToName')
                self.qbcom.ToName.text = self.ToName
        if self.PaymentMethodType:
            self.qbcom.PaymentMethodType = ET.SubElement(self.qbcom.PaymentMethodQueryRq, 'PaymentMethodType')
            self.qbcom.PaymentMethodType.text = self.PaymentMethodType
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.PaymentMethodQueryRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item

    def set_VendorQueryRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        if self.onError:
            self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.VendorQueryRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, self.request_ID)
        if self.metaData:
            self.qbcom.VendorQueryRq.set('metaData', self.metaData)
        if self.iterator:
            self.qbcom.VendorQueryRq.set('iterator', self.iterator)
        if self.ListID:
            self.qbcom.ListID = ET.SubElement(self.qbcom.VendorQueryRq, 'ListID')
            self.qbcom.ListID.text = self.ListID
        elif self.FullName:
            self.qbcom.FullName = ET.SubElement(self.qbcom.VendorQueryRq, 'FullName')
            self.qbcom.FullName.text = self.FullName
        else:
            if self.MaxReturned:
                self.qbcom.MaxReturned = ET.SubElement(self.qbcom.VendorQueryRq, 'MaxReturned')
                self.qbcom.MaxReturned.text = self.MaxReturned
            if self.ActiveStatus:
                self.qbcom.ActiveStatus = ET.SubElement(self.qbcom.VendorQueryRq, 'ActiveStatus')
                self.qbcom.ActiveStatus.text = self.ActiveStatus
            if self.FromModifiedDate:
                self.qbcom.FromModifiedDate = ET.SubElement(self.qbcom.VendorQueryRq, 'FromModifiedDate')
                self.qbcom.FromModifiedDate.text = self.FromModifiedDate
            if self.ToModifiedDate:
                self.qbcom.ToModifiedDate = ET.SubElement(self.qbcom.VendorQueryRq, 'ToModifiedDate')
                self.qbcom.ToModifiedDate.text = self.ToModifiedDate
            if self.NameFilter.MatchCriterion and self.Namefilter.Name:
                self.qbcom.NameFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'NameFilter')
                self.qbcom.NameFilter.text = self.NameFilter
                self.qbcom.MatchCriterion = ET.SubElement(self.qbcom.NameFilter, 'MatchCriterion')
                self.qbcom.MatchCriterion.text = self.MatchCriterion
                self.qbcom.Name = ET.SubElement(self.qbcom.NameFilter, 'Name')
                self.qbcom.Name.text = self.Name
            elif self.NameRangeFilter.FromName and self.NameRangeFilter.ToName:
                self.qbcom.NameRangeFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'NameRangeFilter')
                self.qbcom.NameRangeFilter.text = self.NameRangeFilter
                self.qbcom.FromName = ET.SubElement(self.qbcom.NameRangeFilter, 'FromName')
                self.qbcom.FromName.text = self.FromName
                self.qbcom.ToName = ET.SubElement(self.qbcom.NameRangeFilter, 'ToName')
                self.qbcom.ToName.text = self.ToName
            if self.TotalBalanceFilter.Operator and self.TotalBalanceFilter.Amount:
                self.qbcom.TotalBalanceFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'TotalBalanceFilter')
                self.qbcom.TotalBalanceFilter.text = self.TotalBalanceFilter
                self.qbcom.Operator = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Operator')
                self.qbcom.Operator.text = self.Operator
                self.qbcom.Amount = ET.SubElement(self.qbcom.TotalBalanceFilter, 'Amount')
                self.qbcom.Amount.text = self.Amount
            if self.CurrencyFilter.ListID:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.CurrencyFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.CurrencyFilter.FullName:
                self.qbcom.CurrencyFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'CurrencyFilter')
                self.qbcom.CurrencyFilter.text = self.CurrencyFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.CurrencyFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            if self.ClassFilter.ListID:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListID = ET.SubElement(self.qbcom.ClassFilter, 'ListID')
                self.qbcom.ListID.text = self.ListID
            elif self.ClassFilter.FullName:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullName = ET.SubElement(self.qbcom.ClassFilter, 'FullName')
                self.qbcom.FullName.text = self.FullName
            elif self.ClassFilter.ListIDWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.ListIDWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'ListIDWithChildren')
                self.qbcom.ListIDWithChildren.text = self.ListIDWithChildren
            elif self.ClassFilter.FullNameWithChildren:
                self.qbcom.ClassFilter = ET.SubElement(self.qbcom.VendorQueryRq, 'ClassFilter')
                self.qbcom.ClassFilter.text = self.ClassFilter
                self.qbcom.FullNameWithChildren = ET.SubElement(self.qbcom.ClassFilter, 'FullNameWithChildren')
                self.qbcom.FullNameWithChildren.text = self.FullNameWithChildren
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.VendorQueryRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item
        if self.OwnerID:
                self.qbcom.OwnerID = ET.SubElement(self.qbcom.VendorQueryRq, 'OwnerID')
                self.qbcom.OwnerID.text = self.OwnerID

    def set_CheckAddRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.CheckAddRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, 'CheckAddRq')
        self.qbcom.CheckAdd = ET.SubElement(self.qbcom.CheckAddRq, 'CheckAdd')
        if self.AccountRef.ListID or self.AccountRef.FullName:
            self.qbcom.AccountRef = ET.SubElement(self.qbcom.CheckAdd, 'AccountRef')
            if self.AccountRef.ListID:
                self.qbcom.AccountRef_ListID = ET.SubElement(self.qbcom.AccountRef, 'ListID')
                self.qbcom.AccountRef_ListID.text = self.AccountRef.ListID
            elif self.AccountRef.FullName:
                self.qbcom.AccountRef_FullName = ET.SubElement(self.qbcom.AccountRef, 'FullName')
                self.qbcom.AccountRef_FullName.text = self.AccountRef.FullName
        if self.PayeeEntityRef.ListID or self.PayeeEntityRef.FullName:
            self.qbcom.PayeeEntityRef = ET.SubElement(self.qbcom.CheckAdd, 'PayeeEntityRef')
            if self.PayeeEntityRef.ListID:
                self.qbcom.PayeeEntityRef_ListID = ET.SubElement(self.qbcom.PayeeEntityRef, 'ListID')
                self.qbcom.PayeeEntityRef_ListID.text = self.PayeeEntityRef.ListID
            elif self.PayeeEntityRef.FullName:
                self.qbcom.PayeeEntityRef_FullName = ET.SubElement(self.qbcom.PayeeEntityRef, 'FullName')
                self.qbcom.PayeeEntityRef_FullName.text = self.PayeeEntityRef.FullName
        if self.RefNumber:
            self.qbcom.RefNumber = ET.SubElement(self.qbcom.CheckAdd, 'RefNumber')
            self.qbcom.RefNumber.text = self.RefNumber
        if self.TxnDate:
            self.qbcom.TxnDate = ET.SubElement(self.qbcom.CheckAdd, 'TxnDate')
            self.qbcom.TxnDate.text = self.TxnDate
        if self.Memo:
            self.qbcom.Memo = ET.SubElement(self.qbcom.CheckAdd, 'Memo')
            self.qbcom.Memo.text = self.Memo
        if (self.Address.Addr1 and
                self.Address.Addr2 and
                self.Address.Addr3 and
                self.Address.Addr4 and
                self.Address.Addr5 and
                self.Address.City and
                self.Address.State and
                self.Address.PostalCode):
            self.qbcom.Address = ET.SubElement(self.qbcom.CheckAdd, 'Address')
            self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'Addr1')
            self.qbcom.Address_Addr1.text = self.Address.Addr1
            self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'Addr2')
            self.qbcom.Address_Addr2.text = self.Address.Addr2
            self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'Addr3')
            self.qbcom.Address_Addr3.text = self.Address.Addr3
            self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'Addr4')
            self.qbcom.Address_Addr4.text = self.Address.Addr4
            self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'Addr5')
            self.qbcom.Address_Addr5.text = self.Address.Addr5
            self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'City')
            self.qbcom.Address_City.text = self.Address.City
            self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'State')
            self.qbcom.Address_State.text = self.Address.State
            self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'PostalCode')
            self.qbcom.Address_PostalCode.text = self.Address.PostalCode
            if self.Address.Country:
                self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'Country')
                self.qbcom.Address_Country.text = self.Address.Country
            if self.Address.Note:
                self.qbcom.Address = ET.SubElement(self.qbcom.Address, 'Note')
                self.qbcom.Address_Note.text = self.Address.Note
        if self.IsToBePrinted:
            self.qbcom.IsToBePrinted = ET.SubElement(self.qbcom.CheckAdd, 'IsToBePrinted')
            self.qbcom.IsToBePrinted.text = self.IsToBePrinted
        if self.ExchangeRate:
            self.qbcom.ExchangeRate = ET.SubElement(self.qbcom.CheckAdd, 'ExchangeRate')
            self.qbcom.ExchangeRate.text = self.ExchangeRate
        if self.ExternalGUID:
            self.qbcom.ExternalGUID = ET.SubElement(self.qbcom.CheckAdd, 'ExternalGUID')
            self.qbcom.ExternalGUID.text = self.ExternalGUID
        if self.ApplyCheckToTxnAdd.TxnID or self.ApplyCheckToTxnAdd.Amount:
            self.qbcom.ApplyCheckToTxnAdd = ET.SubElement(self.qbcom.CheckAdd, 'ApplyCheckToTxnAdd')
            self.qbcom.ApplyCheckToTxnAdd_TxnID = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'TxnID')
            self.qbcom.ApplyCheckToTxnAdd_TxnID.text = self.ApplyCheckToTxnAdd.TxnID
            self.qbcom.ApplyCheckToTxnAdd_Amount = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'Amount')
            self.qbcom.ApplyCheckToTxnAdd_Amount.text = self.ApplyCheckToTxnAdd.Amount
        if (self.ExpenseLineAdd.AccountRef.ListID or 
                self.ExpenseLineAdd.AccountRef.FullName):
            self.qbcom.ExpenseLineAdd = ET.SubElement(self.qbcom.CheckAdd, 'ExpenseLineAdd')
            if self.ExpenseLineAdd.AccountRef.ListID or self.ExpenseLineAdd.AccountRef.FullName:
                self.qbcom.ExpenseLineAdd_AccountRef = ET.SubElement(self.qbcom.ExpenseLineAdd, 'AccountRef')
                self.qbcom.ExpenseLineAdd_AccountRef_ListID = ET.SubElement(self.qbcom.ExpenseLineAdd_AccountRef, 'ListID')
                self.qbcom.ExpenseLineAdd_AccountRef_ListID.text = self.ExpenseLineAdd.AccountRef.ListID
                self.qbcom.ExpenseLineAdd_AccountRef_FullName = ET.SubElement(self.qbcom.ExpenseLineAdd_AccountRef, 'FullName')
                self.qbcom.ExpenseLineAdd_AccountRef_FullName.text = self.ExpenseLineAdd.AccountRef.FullName
            if self.ExpenseLineAdd.Amount:
                self.qbcom.ExpenseLineAdd_Amount = ET.SubElement(self.qbcom.ExpenseLineAdd, 'Amount')
                self.qbcom.ExpenseLineAdd_Amount.text = self.ExpenseLineAdd.Amount
            if self.ExpenseLineAdd.Memo:
                self.qbcom.ExpenseLineAdd_Memo = ET.SubElement(self.qbcom.ExpenseLineAdd, 'Memo')
                self.qbcom.ExpenseLineAdd_Memo.text = self.ExpenseLineAdd.Memo
            if self.ExpenseLineAdd.CustomerRef.ListID or self.ExpenseLineAdd.CustomerRef.FullName:
                self.qbcom.ExpenseLineAdd_CustomerRef = ET.SubElement(self.qbcom.ExpenseLineAdd, 'CustomerRef')
                self.qbcom.ExpenseLineAdd_CustomerRef_ListID = ET.SubElement(self.qbcom.ExpenseLineAdd_CustomerRef, 'ListID')
                self.qbcom.ExpenseLineAdd_CustomerRef_ListID.text = self.ExpenseLineAdd.CustomerRef.ListID
                self.qbcom.ExpenseLineAdd_CustomerRef_FullName = ET.SubElement(self.qbcom.ExpenseLineAdd_CustomerRef, 'FullName')
                self.qbcom.ExpenseLineAdd_CustomerRef_FullName.text = self.ExpenseLineAdd.CustomerRef.FullName
            if self.ExpenseLineAdd.ClassRef.ListID or self.ExpenseLineAdd.ClassRef.FullName:
                self.qbcom.ExpenseLineAdd_ClassRef = ET.SubElement(self.qbcom.ExpenseLineAdd, 'ClassRef')
                self.qbcom.ExpenseLineAdd_ClassRef_ListID = ET.SubElement(self.qbcom.ExpenseLineAdd_ClassRef, 'ListID')
                self.qbcom.ExpenseLineAdd_ClassRef_ListID.text = self.ExpenseLineAdd.ClassRef.ListID
                self.qbcom.ExpenseLineAdd_ClassRef_FullName = ET.SubElement(self.qbcom.ExpenseLineAdd_ClassRef, 'FullName')
                self.qbcom.ExpenseLineAdd_ClassRef_FullName.text = self.ExpenseLineAdd.ClassRef.FullName
            if self.ExpenseLineAdd.BillableStatus:
                self.qbcom.ExpenseLineAdd_BillableStatus = ET.SubElement(self.qbcom.ExpenseLineAdd, 'BillableStatus')
                self.qbcom.ExpenseLineAdd_BillableStatus.text = self.ExpenseLineAdd.BillableStatus
            if self.ExpenseLineAdd.SalesRepRef.ListID or self.ExpenseLineAdd.SalesRepRef.FullName:
                self.qbcom.ExpenseLineAdd_SalesRepRef = ET.SubElement(self.qbcom.ExpenseLineAdd, 'SalesRepRef')
                self.qbcom.ExpenseLineAdd_SalesRepRef_ListID = ET.SubElement(self.qbcom.ExpenseLineAdd_SalesRepRef, 'ListID')
                self.qbcom.ExpenseLineAdd_SalesRepRef_ListID.text = self.ExpenseLineAdd.SalesRepRef.ListID
                self.qbcom.ExpenseLineAdd_SalesRepRef_FullName = ET.SubElement(self.qbcom.ExpenseLineAdd_SalesRepRef, 'FullName')
                self.qbcom.ExpenseLineAdd_SalesRepRef_FullName.text = self.ExpenseLineAdd.SalesRepRef.FullName
            if (self.ExpenseLineAdd.DataExt.OwnerID or
                    self.ExpenseLineAdd.DataExt.DataExtName or
                    self.ExpenseLineAdd.DataExt.DataExtValue):
                self.qbcom.ExpenseLineAdd_DataExt = ET.SubElement(self.qbcom.ExpenseLineAdd, 'DataExt')
                self.qbcom.ExpenseLineAdd_DataExt_OwnerID = ET.SubElement(self.qbcom.ExpenseLineAdd_DataExt, 'OwnerID')
                self.qbcom.ExpenseLineAdd_DataExt_OwnerID.text = self.ExpenseLineAdd.DataExt.OwnerID
                self.qbcom.ExpenseLineAdd_DataExt_DataExtName = ET.SubElement(self.qbcom.ExpenseLineAdd_DataExt, 'DataExtName')
                self.qbcom.ExpenseLineAdd_DataExt_DataExtName.text = self.ExpenseLineAdd.DataExt.DataExtName
                self.qbcom.ExpenseLineAdd_DataExt_DataExtValue = ET.SubElement(self.qbcom.ExpenseLineAdd_DataExt, 'DataExtValue')
                self.qbcom.ExpenseLineAdd_DataExt_DataExtValue.text = self.ExpenseLineAdd.DataExt.DataExtValue
        elif (self.ItemLineAdd.ItemRef.ListID or
                self.ItemLineAdd.ItemRef.FullName):
            self.qbcom.ItemLineAdd = ET.SubElement(self.qbcom.CheckAdd, 'ItemLineAdd')
            if self.ItemLineAdd.ItemRef.ListID or self.ItemLineAdd.ItemRef.FullName:
                self.qbcom.ItemLineAdd_ItemRef = ET.SubElement(self.qbcom.CheckAdd, 'ItemRef')
                self.qbcom.ItemLineAdd_ItemRef_ListID = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'ListID')
                self.qbcom.ItemLineAdd_ItemRef_ListID.text = self.ItemLineAdd.ItemRef.ListID
                self.qbcom.ItemLineAdd_ItemRef_FullName = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'FullName')
                self.qbcom.ItemLineAdd_ItemRef_FullName.text = self.ItemLineAdd.ItemRef.FullName
            if self.ItemLineAdd.InventorySiteRef.ListID or self.ItemLineAdd.InventorySiteRef.FullName:
                self.qbcom.ItemLineAdd_InventorySiteRef = ET.SubElement(self.qbcom.CheckAdd, 'InventorySiteRef')
                self.qbcom.ItemLineAdd_InventorySiteRef_ListID = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'ListID')
                self.qbcom.ItemLineAdd_InventorySiteRef_ListID.text = self.ItemLineAdd.InventorySiteRef.ListID
                self.qbcom.ItemLineAdd_InventorySiteRef_FullName = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'FullName')
                self.qbcom.ItemLineAdd_InventorySiteRef_FullName.text = self.ItemLineAdd.InventorySiteRef.FullName
            if self.ItemLineAdd.InventorySiteLocationRef.ListID or self.ItemLineAdd.InventorySiteLocationRef.FullName:
                self.qbcom.ItemLineAdd_InventorySiteLocationRef = ET.SubElement(self.qbcom.CheckAdd, 'InventorySiteLocationRef')
                self.qbcom.ItemLineAdd_InventorySiteLocationRef_ListID = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'ListID')
                self.qbcom.ItemLineAdd_InventorySiteLocationRef_ListID.text = self.ItemLineAdd.InventorySiteLocationRef.ListID
                self.qbcom.ItemLineAdd_InventorySiteLocationRef_FullName = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'FullName')
                self.qbcom.ItemLineAdd_InventorySiteLocationRef_FullName.text = self.ItemLineAdd.InventorySiteLocationRef.FullName
            if self.ItemLineAdd.SerialNumber:
                self.qbcom.ItemLineAdd_SerialNumber = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'SerialNumber')
                self.qbcom.ItemLineAdd_SerialNumber.text = self.ItemLineAdd.SerialNumber
            elif self.ItemLineAdd.LotNumber:
                self.qbcom.ItemLineAdd_LotNumber = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'LotNumber')
                self.qbcom.ItemLineAdd_LotNumber.text = self.ItemLineAdd.LotNumber
            if self.ItemLineAdd.Desc:
                self.qbcom.ItemLineAdd_Desc = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'Desc')
                self.qbcom.ItemLineAdd_Desc.text = self.ItemLineAdd.Desc
            if self.ItemLineAdd.Quantity:
                self.qbcom.ItemLineAdd_Quantity = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'Quantity')
                self.qbcom.ItemLineAdd_Quantity.text = self.ItemLineAdd.Quantity
            if self.ItemLineAdd.UnitOfMeasure:
                self.qbcom.ItemLineAdd_UnitOfMeasure = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'UnitOfMeasure')
                self.qbcom.ItemLineAdd_UnitOfMeasure.text = self.ItemLineAdd.UnitOfMeasure
            if self.ItemLineAdd.Cost:
                self.qbcom.ItemLineAdd_Cost = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'Cost')
                self.qbcom.ItemLineAdd_Cost.text = self.ItemLineAdd.Cost
            if self.ItemLineAdd.Amount:
                self.qbcom.ItemLineAdd_Amount = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'Amount')
                self.qbcom.ItemLineAdd_Amount.text = self.ItemLineAdd.Amount
            if self.ItemLineAdd.CustomerRef.ListID or self.ItemLineAdd.CustomerRef.FullName:
                self.qbcom.ItemLineAdd_CustomerRef = ET.SubElement(self.qbcom.CheckAdd, 'CustomerRef')
                self.qbcom.ItemLineAdd_CustomerRef_ListID = ET.SubElement(self.qbcom.ItemLineAdd.CustomerRef, 'ListID')
                self.qbcom.ItemLineAdd_CustomerRef_ListID.text = self.ItemLineAdd.CustomerRef.ListID
                self.qbcom.ItemLineAdd_CustomerRef_FullName = ET.SubElement(self.qbcom.ItemLineAdd.CustomerRef, 'FullName')
                self.qbcom.ItemLineAdd_CustomerRef_FullName.text = self.ItemLineAdd.CustomerRef.FullName
            if self.ItemLineAdd.ClassRef.ListID or self.ItemLineAdd.ClassRef.FullName:
                self.qbcom.ItemLineAdd_ClassRef = ET.SubElement(self.qbcom.CheckAdd, 'ClassRef')
                self.qbcom.ItemLineAdd_ClassRef_ListID = ET.SubElement(self.qbcom.ItemLineAdd.ClassRef, 'ListID')
                self.qbcom.ItemLineAdd_ClassRef_ListID.text = self.ItemLineAdd.ClassRef.ListID
                self.qbcom.ItemLineAdd_ClassRef_FullName = ET.SubElement(self.qbcom.ItemLineAdd.ClassRef, 'FullName')
                self.qbcom.ItemLineAdd_ClassRef_FullName.text = self.ItemLineAdd.ClassRef.FullName
            if self.ItemLineAdd.BillableStatus:
                self.qbcom.ItemLineAdd_BillableStatus = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'BillableStatus')
                self.qbcom.ItemLineAdd_BillableStatus.text = self.ItemLineAdd.BillableStatus
            if self.ItemLineAdd.OverrideItemAccountRef.ListID or self.ItemLineAdd.OverrideItemAccountRef.FullName:
                self.qbcom.ItemLineAdd_OverrideItemAccountRef = ET.SubElement(self.qbcom.CheckAdd, 'OverrideItemAccountRef')
                self.qbcom.ItemLineAdd_OverrideItemAccountRef_ListID = ET.SubElement(self.qbcom.ItemLineAdd.OverrideItemAccountRef, 'ListID')
                self.qbcom.ItemLineAdd_OverrideItemAccountRef_ListID.text = self.ItemLineAdd.OverrideItemAccountRef.ListID
                self.qbcom.ItemLineAdd_OverrideItemAccountRef_FullName = ET.SubElement(self.qbcom.ItemLineAdd.OverrideItemAccountRef, 'FullName')
                self.qbcom.ItemLineAdd_OverrideItemAccountRef_FullName.text = self.ItemLineAdd.OverrideItemAccountRef.FullName
            if self.ItemLineAdd.SalesRepRef.ListID or self.ItemLineAdd.SalesRepRef.FullName:
                self.qbcom.ItemLineAdd_SalesRepRef = ET.SubElement(self.qbcom.CheckAdd, 'SalesRepRef')
                self.qbcom.ItemLineAdd_SalesRepRef_ListID = ET.SubElement(self.qbcom.ItemLineAdd.SalesRepRef, 'ListID')
                self.qbcom.ItemLineAdd_SalesRepRef_ListID.text = self.ItemLineAdd.SalesRepRef.ListID
                self.qbcom.ItemLineAdd_SalesRepRef_FullName = ET.SubElement(self.qbcom.ItemLineAdd.SalesRepRef, 'FullName')
                self.qbcom.ItemLineAdd_SalesRepRef_FullName.text = self.ItemLineAdd.SalesRepRef.FullName
            if self.ItemLineAdd.DataExt.ListID or self.ItemLineAdd.DataExt.FullName:
                self.qbcom.ItemLineAdd_DataExt = ET.SubElement(self.qbcom.CheckAdd, 'DataExt')
                self.qbcom.ItemLineAdd_DataExt_OwnerID = ET.SubElement(self.qbcom.ItemLineAdd.DataExt, 'OwnerID')
                self.qbcom.ItemLineAdd_DataExt_OwnerID.text = self.ItemLineAdd.DataExt.OwnerID
                self.qbcom.ItemLineAdd_DataExt_DataExtName = ET.SubElement(self.qbcom.ItemLineAdd.DataExt, 'DataExtName')
                self.qbcom.ItemLineAdd_DataExt_DataExtName.text = self.ItemLineAdd.DataExt.DataExtName
                self.qbcom.ItemLineAdd_DataExt_DataExtValue = ET.SubElement(self.qbcom.ItemLineAdd.DataExt, 'DataExtValue')
                self.qbcom.ItemLineAdd_DataExt_DataExtValue.text = self.ItemLineAdd.DataExt.DataExtValue
        elif (self.ItemGroupLineAdd.ItemGroupRef.ListID or
                self.ItemGroupLineAdd.ItemGroupRef.FullName):
            self.qbcom.ItemGroupLineAdd = ET.SubElement(self.qbcom.CheckAdd, 'ItemGroupLineAdd')
            if self.ItemGroupLineAdd.ItemGroupRef.ListID or self.ItemGroupLineAdd.ItemGroupRef.FullName:
                self.qbcom.ItemGroupLineAdd_ItemGroupRef = ET.SubElement(self.qbcom.CheckAdd, 'ItemGroupRef')
                self.qbcom.ItemGroupLineAdd_ItemGroupRef_ListID = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'ListID')
                self.qbcom.ItemGroupLineAdd_ItemGroupRef_ListID.text = self.ItemGroupLineAdd.ItemGroupRef.ListID
                self.qbcom.ItemGroupLineAdd_ItemGroupRef_FullName = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'FullName')
                self.qbcom.ItemGroupLineAdd_ItemGroupRef_FullName.text = self.ItemGroupLineAdd.ItemGroupRef.FullName
            if self.ItemGroupLineAdd.Quantity:
                self.qbcom.ItemGroupLineAdd_Quantity = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'Quantity')
                self.qbcom.ItemGroupLineAdd_Quantity.text = self.ItemGroupLineAdd.Quantity
            if self.ItemGroupLineAdd.UnitOfMeasure:
                self.qbcom.ItemGroupLineAdd_UnitOfMeasure = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'UnitOfMeasure')
                self.qbcom.ItemGroupLineAdd_UnitOfMeasure.text = self.ItemGroupLineAdd.UnitOfMeasure
            if self.ItemGroupLineAdd.InventorySiteRef.ListID or self.ItemGroupLineAdd.InventorySiteRef.FullName:
                self.qbcom.ItemGroupLineAdd_InventorySiteRef = ET.SubElement(self.qbcom.CheckAdd, 'InventorySiteRef')
                self.qbcom.ItemGroupLineAdd_InventorySiteRef_ListID = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'ListID')
                self.qbcom.ItemGroupLineAdd_InventorySiteRef_ListID.text = self.ItemGroupLineAdd.InventorySiteRef.ListID
                self.qbcom.ItemGroupLineAdd_InventorySiteRef_FullName = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'FullName')
                self.qbcom.ItemGroupLineAdd_InventorySiteRef_FullName.text = self.ItemGroupLineAdd.InventorySiteRef.FullName
            if self.ItemGroupLineAdd.InventorySiteLocationRef.ListID or self.ItemGroupLineAdd.InventorySiteLocationRef.FullName:
                self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef = ET.SubElement(self.qbcom.CheckAdd, 'InventorySiteLocationRef')
                self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef_ListID = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'ListID')
                self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef_ListID.text = self.ItemGroupLineAdd.InventorySiteLocationRef.ListID
                self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef_FullName = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'FullName')
                self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef_FullName.text = self.ItemGroupLineAdd.InventorySiteLocationRef.FullName
            if self.ItemGroupLineAdd.DataExt.ListID or self.ItemGroupLineAdd.DataExt.FullName:
                self.qbcom.ItemGroupLineAdd_DataExt = ET.SubElement(self.qbcom.CheckAdd, 'DataExt')
                self.qbcom.ItemGroupLineAdd_DataExt_OwnerID = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'OwnerID')
                self.qbcom.ItemGroupLineAdd_DataExt = ET.SubElement(self.qbcom.CheckAdd, 'DataExt')
                self.qbcom.ItemGroupLineAdd_DataExt_DataExtName = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'DataExtName')
                self.qbcom.ItemGroupLineAdd_DataExt = ET.SubElement(self.qbcom.CheckAdd, 'DataExt')
                self.qbcom.ItemGroupLineAdd_DataExt_DataExtValue = ET.SubElement(self.qbcom.ApplyCheckToTxnAdd, 'DataExtValue')
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.CheckAddRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item

    def set_CustomerAddRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.CustomerAddRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, 'CustomerAddRq')
        self.qbcom.CustomerAdd = ET.SubElement(self.qbcom.CustomerAddRq, 'CustomerAdd')
        if self.Name:
            self.qbcom.Name = ET.SubElement(self.qbcom.CustomerAdd, 'Name')
            self.qbcom.Name.text = self.Name
        if self.ClassRef.ListID or self.ClassRef.FullName:
            self.qbcom.ClassRef = ET.SubElement(self.qbcom.CustomerAdd, 'ClassRef')
            self.qbcom.ClassRef_ListID = ET.SubElement(self.qbcom.ClassRef, 'ListID')
            self.qbcom.ClassRef_ListID.text = self.ClassRef.ListID
            self.qbcom.ClassRef_FullName = ET.SubElement(self.qbcom.ClassRef, 'FullName')
            self.qbcom.ClassRef_FullName.text = self.ClassRef.FullName
        if self.ParentRef.ListID or self.ParentRef.FullName:
            self.qbcom.ParentRef = ET.SubElement(self.qbcom.CustomerAdd, 'ParentRef')
            self.qbcom.ParentRef_ListID = ET.SubElement(self.qbcom.ParentRef, 'ListID')
            self.qbcom.ParentRef_ListID.text = self.ParentRef.ListID
            self.qbcom.ParentRef_FullName = ET.SubElement(self.qbcom.ParentRef, 'FullName')
            self.qbcom.ParentRef_FullName.text = self.ParentRef.FullName
        if self.CompanyName:
            self.qbcom.CompanyName = ET.SubElement(self.qbcom.CustomerAdd, 'CompanyName')
            self.qbcom.CompanyName.text = self.CompanyName
        if self.Salutation:
            self.qbcom.Salutation = ET.SubElement(self.qbcom.CustomerAdd, 'Salutation')
            self.qbcom.Salutation.text = self.Salutation
        if self.FirstName:
            self.qbcom.FirstName = ET.SubElement(self.qbcom.CustomerAdd, 'FirstName')
            self.qbcom.FirstName.text = self.FirstName
        if self.MiddleName:
            self.qbcom.MiddleName = ET.SubElement(self.qbcom.CustomerAdd, 'MiddleName')
            self.qbcom.MiddleName.text = self.MiddleName
        if self.LastName:
            self.qbcom.LastName = ET.SubElement(self.qbcom.CustomerAdd, 'LastName')
            self.qbcom.LastName.text = self.LastName
        if self.JobTitle:
            self.qbcom.JobTitle = ET.SubElement(self.qbcom.CustomerAdd, 'JobTitle')
            self.qbcom.JobTitle.text = self.JobTitle
        if (    self.BillAddress.Addr1 and
                self.BillAddress.Addr2 and
                self.BillAddress.Addr3 and
                self.BillAddress.City and
                self.BillAddress.State and
                self.BillAddress.PostalCode and
                self.BillAddress.Country and
                not self.BillAddress.Addr4 and
                not self.BillAddress.Addr5):
            self.qbcom.BillAddress = ET.SubElement(self.qbcom.CustomerAdd, 'BillAddress')
            self.qbcom.BillAddress_Addr1 = ET.SubElement(self.qbcom.BillAddress, 'Addr1')
            self.qbcom.BillAddress_Addr1.text = self.BillAddress.Addr1
            self.qbcom.BillAddress_Addr2 = ET.SubElement(self.qbcom.BillAddress, 'Addr2')
            self.qbcom.BillAddress_Addr2.text = self.BillAddress.Addr2
            self.qbcom.BillAddress_Addr3 = ET.SubElement(self.qbcom.BillAddress, 'Addr3')
            self.qbcom.BillAddress_Addr3.text = self.BillAddress.Addr3
            self.qbcom.BillAddress_City = ET.SubElement(self.qbcom.BillAddress, 'City')
            self.qbcom.BillAddress_City.text = self.BillAddress.City
            self.qbcom.BillAddress_State = ET.SubElement(self.qbcom.BillAddress, 'State')
            self.qbcom.BillAddress_State.text = self.BillAddress.State
            self.qbcom.BillAddress_PostalCode = ET.SubElement(self.qbcom.BillAddress, 'PostalCode')
            self.qbcom.BillAddress_PostalCode.text = self.BillAddress.PostalCode
            if self.BillAddress.Country:
                self.qbcom.BillAddress_Country = ET.SubElement(self.qbcom.BillAddress, 'Country')
                self.qbcom.BillAddress_Country.text = self.BillAddress.Country
            if self.BillAddress.Note:
                self.qbcom.BillAddress_Note = ET.SubElement(self.qbcom.BillAddress, 'Note')
                self.qbcom.BillAddress_Note.text = self.BillAddress.Note
        if (    self.BillAddress.Addr1 and
                self.BillAddress.Addr2 and
                self.BillAddress.Addr3 and
                self.BillAddress.Addr4 and
                self.BillAddress.Addr5 and
                not self.BillAddress.City and
                not self.BillAddress.State and
                not self.BillAddress.PostalCode and
                not self.BillAddress.Country):
            self.qbcom.BillAddress_ = ET.SubElement(self.qbcom.CustomerAdd, 'BillAddress')
            self.qbcom.BillAddress_Addr1 = ET.SubElement(self.qbcom.BillAddress, 'Addr1')
            self.qbcom.BillAddress_Addr1.text = self.BillAddress.Addr1
            self.qbcom.BillAddress_Addr2 = ET.SubElement(self.qbcom.BillAddress, 'Addr2')
            self.qbcom.BillAddress_Addr2.text = self.BillAddress.Addr2
            self.qbcom.BillAddress_Addr3 = ET.SubElement(self.qbcom.BillAddress, 'Addr3')
            self.qbcom.BillAddress_Addr3.text = self.BillAddress.Addr3
            self.qbcom.BillAddress_Addr4 = ET.SubElement(self.qbcom.BillAddress, 'Addr4')
            self.qbcom.BillAddress_Addr4.text = self.BillAddress.Addr4
            self.qbcom.BillAddress_Addr5 = ET.SubElement(self.qbcom.BillAddress, 'Addr5')
            self.qbcom.BillAddress_Addr5.text = self.BillAddress.Addr5
            if self.BillAddress.Note:
                self.qbcom.BillAddress_Note = ET.SubElement(self.qbcom.BillAddress, 'Note')
                self.qbcom.BillAddress_Note.text = self.BillAddress.Note
        if (    self.ShipAddress.Addr1 and
                self.ShipAddress.Addr2 and
                self.ShipAddress.Addr3 and
                self.ShipAddress.City and
                self.ShipAddress.State and
                self.ShipAddress.PostalCode and
                not self.ShipAddress.Addr4 and
                not self.ShipAddress.Addr5):
            self.qbcom.ShipAddress = ET.SubElement(self.qbcom.CustomerAdd, 'ShipAddress')
            self.qbcom.ShipAddress_Addr1 = ET.SubElement(self.qbcom.ShipAddress, 'Addr1')
            self.qbcom.ShipAddress_Addr1.text = self.ShipAddress.Addr1
            self.qbcom.ShipAddress_Addr2 = ET.SubElement(self.qbcom.ShipAddress, 'Addr2')
            self.qbcom.ShipAddress_Addr2.text = self.ShipAddress.Addr2
            self.qbcom.ShipAddress_Addr3 = ET.SubElement(self.qbcom.ShipAddress, 'Addr3')
            self.qbcom.ShipAddress_Addr3.text = self.ShipAddress.Addr3
            self.qbcom.ShipAddress_City = ET.SubElement(self.qbcom.ShipAddress, 'City')
            self.qbcom.ShipAddress_City.text = self.ShipAddress.City
            self.qbcom.ShipAddress_State = ET.SubElement(self.qbcom.ShipAddress, 'State')
            self.qbcom.ShipAddress_State.text = self.ShipAddress.State
            self.qbcom.ShipAddress_PostalCode = ET.SubElement(self.qbcom.ShipAddress, 'PostalCode')
            self.qbcom.ShipAddress_PostalCode.text = self.ShipAddress.PostalCode
            if self.ShipAddress.Country:
                self.qbcom.ShipAddress_Country = ET.SubElement(self.qbcom.ShipAddress, 'Country')
                self.qbcom.ShipAddress_Country.text = self.ShipAddress.Country
            if self.ShipAddress.Note:
                self.qbcom.ShipAddress_Note = ET.SubElement(self.qbcom.ShipAddress, 'Note')
                self.qbcom.ShipAddress_Note.text = self.ShipAddress.Note
        if (    self.ShipAddress.Addr1 and
                self.ShipAddress.Addr2 and
                self.ShipAddress.Addr3 and
                self.ShipAddress.Addr4 and
                self.ShipAddress.Addr5 and
                not self.ShipAddress.City and
                not self.ShipAddress.State and
                not self.ShipAddress.PostalCode and
                not self.ShipAddress.Country):
            self.qbcom.ShipAddress = ET.SubElement(self.qbcom.CustomerAdd, 'ShipAddress')
            self.qbcom.ShipAddress_Addr1 = ET.SubElement(self.qbcom.ShipAddress, 'Addr1')
            self.qbcom.ShipAddress_Addr1.text = self.ShipAddress.Addr1
            self.qbcom.ShipAddress_Addr2 = ET.SubElement(self.qbcom.ShipAddress, 'Addr2')
            self.qbcom.ShipAddress_Addr2.text = self.ShipAddress.Addr2
            self.qbcom.ShipAddress_Addr3 = ET.SubElement(self.qbcom.ShipAddress, 'Addr3')
            self.qbcom.ShipAddress_Addr3.text = self.ShipAddress.Addr3
            self.qbcom.ShipAddress_Addr4 = ET.SubElement(self.qbcom.ShipAddress, 'Addr4')
            self.qbcom.ShipAddress_Addr4.text = self.ShipAddress.Addr4
            self.qbcom.ShipAddress_Addr5 = ET.SubElement(self.qbcom.ShipAddress, 'Addr5')
            self.qbcom.ShipAddress_Addr5.text = self.ShipAddress.Addr5
            if self.ShipAddress.Note:
                self.qbcom.ShipAddress_Note = ET.SubElement(self.qbcom.ShipAddress, 'Note')
                self.qbcom.ShipAddress_Note.text = self.ShipAddress.Note
        if (    self.ShipToAddress.Addr1 and
                self.ShipToAddress.Addr2 and
                self.ShipToAddress.Addr3 and
                self.ShipToAddress.City and
                self.ShipToAddress.State and
                self.ShipToAddress.PostalCode and
                not self.ShipToAddress.Addr4 and
                not self.ShipToAddress.Addr5):
            self.qbcom.ShipToAddress = ET.SubElement(self.qbcom.CustomerAdd, 'ShipToAddress')
            self.qbcom.ShipToAddress_Addr1 = ET.SubElement(self.qbcom.ShipToAddress, 'Addr1')
            self.qbcom.ShipToAddress_Addr1.text = self.ShipToAddress.Addr1
            self.qbcom.ShipToAddress_Addr2 = ET.SubElement(self.qbcom.ShipToAddress, 'Addr2')
            self.qbcom.ShipToAddress_Addr2.text = self.ShipToAddress.Addr2
            self.qbcom.ShipToAddress_Addr3 = ET.SubElement(self.qbcom.ShipToAddress, 'Addr3')
            self.qbcom.ShipToAddress_Addr3.text = self.ShipToAddress.Addr3
            self.qbcom.ShipToAddress_City = ET.SubElement(self.qbcom.ShipToAddress, 'City')
            self.qbcom.ShipToAddress_City.text = self.ShipToAddress.City
            self.qbcom.ShipToAddress_State = ET.SubElement(self.qbcom.ShipToAddress, 'State')
            self.qbcom.ShipToAddress_State.text = self.ShipToAddress.State
            self.qbcom.ShipToAddress_PostalCode = ET.SubElement(self.qbcom.ShipToAddress, 'PostalCode')
            self.qbcom.ShipToAddress_PostalCode.text = self.ShipToAddress.PostalCode
            if self.ShipToAddress.Country:
                self.qbcom.ShipToAddress_Country = ET.SubElement(self.qbcom.ShipToAddress, 'Country')
                self.qbcom.ShipToAddress_Country.text = self.ShipToAddress.Country
            if self.ShipToAddress.Note:
                self.qbcom.ShipToAddress_Note = ET.SubElement(self.qbcom.ShipToAddress, 'Note')
                self.qbcom.ShipToAddress_Note.text = self.ShipToAddress.Note
            if self.ShipToAddress.DefaultShipTo:
                self.qbcom.ShipToAddress_DefaultShipTo = ET.SubElement(self.qbcom.ShipToAddress, 'DefaultShipTo')
                self.qbcom.ShipToAddress_DefaultShipTo.text = self.ShipToAddress.Note
        if (    self.ShipToAddress.Addr1 and
                self.ShipToAddress.Addr2 and
                self.ShipToAddress.Addr3 and
                self.ShipToAddress.Addr4 and
                self.ShipToAddress.Addr5 and
                not self.ShipToAddress.City and
                not self.ShipToAddress.State and
                not self.ShipToAddress.PostalCode and
                not self.ShipToAddress.Country):
            self.qbcom.ShipToAddress = ET.SubElement(self.qbcom.CustomerAdd, 'ShipToAddress')
            self.qbcom.ShipToAddress_Addr1 = ET.SubElement(self.qbcom.ShipToAddress, 'Addr1')
            self.qbcom.ShipToAddress_Addr1.text = self.ShipToAddress.Addr1
            self.qbcom.ShipToAddress_Addr2 = ET.SubElement(self.qbcom.ShipToAddress, 'Addr2')
            self.qbcom.ShipToAddress_Addr2.text = self.ShipToAddress.Addr2
            self.qbcom.ShipToAddress_Addr3 = ET.SubElement(self.qbcom.ShipToAddress, 'Addr3')
            self.qbcom.ShipToAddress_Addr3.text = self.ShipToAddress.Addr3
            self.qbcom.ShipToAddress_Addr4 = ET.SubElement(self.qbcom.ShipToAddress, 'Addr4')
            self.qbcom.ShipToAddress_Addr4.text = self.ShipToAddress.Addr4
            self.qbcom.ShipToAddress_Addr5 = ET.SubElement(self.qbcom.ShipToAddress, 'Addr5')
            self.qbcom.ShipToAddress_Addr5.text = self.ShipToAddress.Addr5
            if self.ShipToAddress.Note:
                self.qbcom.ShipToAddress_Note = ET.SubElement(self.qbcom.ShipToAddress, 'Note')
                self.qbcom.ShipToAddress_Note.text = self.ShipToAddress.Note
            if self.ShipToAddress.DefaultShipTo:
                self.qbcom.ShipToAddress_DefaultShipTo = ET.SubElement(self.qbcom.ShipToAddress, 'DefaultShipTo')
                self.qbcom.ShipToAddress_DefaultShipTo.text = self.ShipToAddress.DefaultShipTo
        if self.Phone:
            self.qbcom.Phone = ET.SubElement(self.qbcom.CustomerAdd, 'Phone')
            self.qbcom.Phone.text = self.Phone
        if self.AltPhone:
            self.qbcom.AltPhone = ET.SubElement(self.qbcom.CustomerAdd, 'AltPhone')
            self.qbcom.AltPhone.text = self.AltPhone
        if self.Fax:
            self.qbcom.Fax = ET.SubElement(self.qbcom.CustomerAdd, 'Fax')
            self.qbcom.Fax.text = self.Fax
        if self.Email:
            self.qbcom.Email = ET.SubElement(self.qbcom.CustomerAdd, 'Email')
            self.qbcom.Email.text = self.Email
        if self.Cc:
            self.qbcom.Cc = ET.SubElement(self.qbcom.CustomerAdd, 'Cc')
            self.qbcom.Cc.text = self.Cc
        if self.Contact:
            self.qbcom.Contact = ET.SubElement(self.qbcom.CustomerAdd, 'Contact')
            self.qbcom.Contact.text = self.Contact
        if self.AltContact:
            self.qbcom.AltContact = ET.SubElement(self.qbcom.CustomerAdd, 'AltContact')
            self.qbcom.AltContact.text = self.AltContact
        if self.AdditionalContactRef.ContactName or self.AdditionalContactRef.ContactValue:
            self.qbcom.AdditionalContactRef = ET.SubElement(self.qbcom.CustomerAdd, 'AdditionalContactRef')
            self.qbcom.AdditionalContactRef_ContactName = ET.SubElement(self.qbcom.AdditionalContactRef, 'ContactName')
            self.qbcom.AdditionalContactRef_ContactName.text = self.AdditionalContactRef.ContactName
            self.qbcom.AdditionalContactRef_ContactValue = ET.SubElement(self.qbcom.AdditionalContactRef, 'ContactValue')
            self.qbcom.AdditionalContactRef_ContactValue.text = self.AdditionalContactRef.ContactValue
        if (self.Contacts.Salutation or
                self.Contacts.FirstName or
                self.Contacts.MiddleName or
                self.Contacts.LastName or
                self.Contacts.JobTitle):
            self.qbcom.Contacts = ET.SubElement(self.qbcom.CustomerAdd, 'Contacts')
            self.qbcom.Contacts_Salutation = ET.SubElement(self.qbcom.Contacts, 'Salutation')
            self.qbcom.Contacts_Salutation.text = self.Contacts.Salutation
            self.qbcom.Contacts_FirstName = ET.SubElement(self.qbcom.Contacts, 'FirstName')
            self.qbcom.Contacts_FirstName.text = self.Contacts.FirstName
            self.qbcom.Contacts_MiddleName = ET.SubElement(self.qbcom.Contacts, 'MiddleName')
            self.qbcom.Contacts_MiddleName.text = self.Contacts.MiddleName
            self.qbcom.Contacts_LastName = ET.SubElement(self.qbcom.Contacts, 'LastName')
            self.qbcom.Contacts_LastName.text = self.Contacts.LastName
            self.qbcom.Contacts_JobTitle = ET.SubElement(self.qbcom.Contacts, 'JobTitle')
            self.qbcom.Contacts_JobTitle.text = self.Contacts.JobTitle
            if self.Contacts.AdditionalContactRef.ContactName or self.Contacts.AdditionalContactRef.ContactValue:
                self.qbcom.Contacts_AdditionalContactRef = ET.SubElement(self.qbcom.Contacts, 'AdditionalContactRef')
                self.qbcom.Contacts_AdditionalContactRef_ContactName = ET.SubElement(self.qbcom.Contacts.AdditionalContactRef, 'ContactName')
                self.qbcom.Contacts_AdditionalContactRef_ContactName.text = self.Contacts.AdditionalContactRef.ContactName
                self.qbcom.Contacts_AdditionalContactRef_ContactValue = ET.SubElement(self.qbcom.Contacts.AdditionalContactRef, 'ContactValue')
                self.qbcom.Contacts_AdditionalContactRef_ContactValue.text = self.Contacts.AdditionalContactRef.ContactValue
        if self.CustomerTypeRef.ListID or self.CustomerTypeRef.FullName:
            self.qbcom.CustomerTypeRef = ET.SubElement(self.qbcom.CustomerAdd, 'CustomerTypeRef')
            self.qbcom.CustomerTypeRef_ListID = ET.SubElement(self.qbcom.CustomerTypeRef, 'ListID')
            self.qbcom.CustomerTypeRef_ListID.text = self.CustomerTypeRef.ListID
            self.qbcom.CustomerTypeRef_FullName = ET.SubElement(self.qbcom.CustomerTypeRef, 'FullName')
            self.qbcom.CustomerTypeRef_FullName.text = self.CustomerTypeRef.FullName
        if self.TermsRef.ListID or self.TermsRef.FullName:
            self.qbcom.TermsRef = ET.SubElement(self.qbcom.CustomerAdd, 'TermsRef')
            self.qbcom.TermsRef_ListID = ET.SubElement(self.qbcom.TermsRef, 'ListID')
            self.qbcom.TermsRef_ListID.text = self.TermsRef.ListID
            self.qbcom.TermsRef_FullName = ET.SubElement(self.qbcom.TermsRef, 'FullName')
            self.qbcom.TermsRef_FullName.text = self.TermsRef.FullName
        if self.SalesRepRef.ListID or self.SalesRepRef.FullName:
            self.qbcom.SalesRepRef = ET.SubElement(self.qbcom.CustomerAdd, 'SalesRepRef')
            self.qbcom.SalesRepRef_ListID = ET.SubElement(self.qbcom.SalesRepRef, 'ListID')
            self.qbcom.SalesRepRef_ListID.text = self.SalesRepRef.ListID
            self.qbcom.SalesRepRef_FullName = ET.SubElement(self.qbcom.SalesRepRef, 'FullName')
            self.qbcom.SalesRepRef_FullName.text = self.SalesRepRef.FullName
        if self.OpenBalance:
            self.qbcom.OpenBalance = ET.SubElement(self.qbcom.CustomerAdd, 'OpenBalance')
            self.qbcom.OpenBalance.text = self.OpenBalance
        if self.OpenBalanceDate:
            self.qbcom.OpenBalanceDate = ET.SubElement(self.qbcom.CustomerAdd, 'OpenBalanceDate')
            self.qbcom.OpenBalanceDate.text = self.OpenBalanceDate
        if self.SalesTaxCodeRef.ListID or self.SalesTaxCodeRef.FullName:
            self.qbcom.SalesTaxCodeRef = ET.SubElement(self.qbcom.CustomerAdd, 'SalesTaxCodeRef')
            self.qbcom.SalesTaxCodeRef_ListID = ET.SubElement(self.qbcom.SalesTaxCodeRef, 'ListID')
            self.qbcom.SalesTaxCodeRef_ListID.text = self.SalesTaxCodeRef.ListID
            self.qbcom.SalesTaxCodeRef_FullName = ET.SubElement(self.qbcom.SalesTaxCodeRef, 'FullName')
            self.qbcom.SalesTaxCodeRef_FullName.text = self.SalesTaxCodeRef.FullName
        if self.ItemSalesTaxRef.ListID or self.ItemSalesTaxRef.FullName:
            self.qbcom.ItemSalesTaxRef = ET.SubElement(self.qbcom.CustomerAdd, 'ItemSalesTaxRef')
            self.qbcom.ItemSalesTaxRef_ListID = ET.SubElement(self.qbcom.ItemSalesTaxRef, 'ListID')
            self.qbcom.ItemSalesTaxRef_ListID.text = self.ItemSalesTaxRef.ListID
            self.qbcom.ItemSalesTaxRef_FullName = ET.SubElement(self.qbcom.ItemSalesTaxRef, 'FullName')
            self.qbcom.ItemSalesTaxRef_FullName.text = self.ItemSalesTaxRef.FullName
        if self.ResaleNumber:
            self.qbcom.ResaleNumber = ET.SubElement(self.qbcom.CustomerAdd, 'ResaleNumber')
            self.qbcom.ResaleNumber.text = self.ResaleNumber
        if self.AccountNumber:
            self.qbcom.AccountNumber = ET.SubElement(self.qbcom.CustomerAdd, 'AccountNumber')
            self.qbcom.AccountNumber.text = self.AccountNumber
        if self.CreditLimit:
            self.qbcom.CreditLimit = ET.SubElement(self.qbcom.CustomerAdd, 'CreditLimit')
            self.qbcom.CreditLimit.text = self.CreditLimit
        if self.PreferredPaymentMethodRef.ListID or self.PreferredPaymentMethodRef.FullName:
            self.qbcom.PreferredPaymentMethodRef = ET.SubElement(self.qbcom.CustomerAdd, 'PreferredPaymentMethodRef')
            self.qbcom.PreferredPaymentMethodRef_ListID = ET.SubElement(self.qbcom.PreferredPaymentMethodRef, 'ListID')
            self.qbcom.PreferredPaymentMethodRef_ListID.text = self.PreferredPaymentMethodRef.ListID
            self.qbcom.PreferredPaymentMethodRef_FullName = ET.SubElement(self.qbcom.PreferredPaymentMethodRef, 'FullName')
            self.qbcom.PreferredPaymentMethodRef_FullName.text = self.PreferredPaymentMethodRef.FullName
        if self.CreditCardInfo.CreditCardNumber or self.CreditCardInfo.ExpirationMonth:
            self.qbcom.CreditCardInfo = ET.SubElement(self.qbcom.CustomerAdd, 'CreditCardInfo')
            self.qbcom.CreditCardInfo_CreditCardNumber = ET.SubElement(self.qbcom.CreditCardInfo, 'CreditCardNumber')
            self.qbcom.CreditCardInfo_CreditCardNumber.text = self.CreditCardInfo.CreditCardNumber
            self.qbcom.CreditCardInfo_ExpirationMonth = ET.SubElement(self.qbcom.CreditCardInfo, 'ExpirationMonth')
            self.qbcom.CreditCardInfo_ExpirationMonth.text = self.CreditCardInfo.ExpirationMonth
            self.qbcom.CreditCardInfo_ExpirationYear = ET.SubElement(self.qbcom.CreditCardInfo, 'ExpirationYear')
            self.qbcom.CreditCardInfo_ExpirationYear.text = self.CreditCardInfo.ExpirationYear
            self.qbcom.CreditCardInfo_NameOnCard = ET.SubElement(self.qbcom.CreditCardInfo, 'NameOnCard')
            self.qbcom.CreditCardInfo_NameOnCard.text = self.CreditCardInfo.NameOnCard
            self.qbcom.CreditCardInfo_CreditCardAddress = ET.SubElement(self.qbcom.CreditCardInfo, 'CreditCardAddress')
            self.qbcom.CreditCardInfo_CreditCardAddress.text = self.CreditCardInfo.CreditCardAddress
            self.qbcom.CreditCardInfo_CreditCardPostalCode = ET.SubElement(self.qbcom.CreditCardInfo, 'CreditCardPostalCode')
            self.qbcom.CreditCardInfo_CreditCardPostalCode.text = self.CreditCardInfo.CreditCardPostalCode
        if self.JobStatus:
            self.qbcom.JobStatus = ET.SubElement(self.qbcom.CustomerAdd, 'JobStatus')
            self.qbcom.JobStatus.text = self.JobStatus
        if self.JobStartDate:
            self.qbcom.JobStartDate = ET.SubElement(self.qbcom.CustomerAdd, 'JobStartDate')
            self.qbcom.JobStartDate.text = self.JobStartDate
        if self.JobProjectedEndDate:
            self.qbcom.JobProjectedEndDate = ET.SubElement(self.qbcom.CustomerAdd, 'JobProjectedEndDate')
            self.qbcom.JobProjectedEndDate.text = self.JobProjectedEndDate
        if self.JobEndDate:
            self.qbcom.JobEndDate = ET.SubElement(self.qbcom.CustomerAdd, 'JobEndDate')
            self.qbcom.JobEndDate.text = self.JobEndDate
        if self.JobDesc:
            self.qbcom.JobDesc = ET.SubElement(self.qbcom.CustomerAdd, 'JobDesc')
            self.qbcom.JobDesc.text = self.JobDesc
            self.qbcom.JobTypeRef = ET.SubElement(self.qbcom.CustomerAdd, 'JobTypeRef')
            self.qbcom.JobTypeRef_ListID = ET.SubElement(self.qbcom.JobTypeRef, 'ListID')
            self.qbcom.JobTypeRef_ListID.text = self.JobTypeRef.ListID
            self.qbcom.JobTypeRef_FullName = ET.SubElement(self.qbcom.JobTypeRef, 'FullName')
            self.qbcom.JobTypeRef_FullName.text = self.JobTypeRef.FullName
        if self.Notes:
            self.qbcom.Notes = ET.SubElement(self.qbcom.CustomerAdd, 'Notes')
            self.qbcom.Notes.text = self.Notes
        if self.AdditionalNotes.Notes:
            self.qbcom.AdditionalNotes = ET.SubElement(self.qbcom.CustomerAdd, 'AdditionalNotes')
            self.qbcom.AdditionalNotes_Notes = ET.SubElement(self.qbcom.AdditionalNotes, 'Notes')
            self.qbcom.AdditionalNotes_Notes.text = self.AdditionalNotes.Notes
        if self.PreferredDeliveryMethod:
            self.qbcom.PreferredDeliveryMethod = ET.SubElement(self.qbcom.CustomerAdd, 'PreferredDeliveryMethod')
            self.qbcom.PreferredDeliveryMethod.text = self.PreferredDeliveryMethod
        if self.PriceLevelRef.ListID or self.PriceLevelRef.FullName:
            self.qbcom.PriceLevelRef = ET.SubElement(self.qbcom.CustomerAdd, 'PriceLevelRef')
            self.qbcom.PriceLevelRef_ListID = ET.SubElement(self.qbcom.PriceLevelRef, 'ListID')
            self.qbcom.PriceLevelRef_ListID.text = self.PriceLevelRef.ListID
            self.qbcom.PriceLevelRef_FullName = ET.SubElement(self.qbcom.PriceLevelRef, 'FullName')
            self.qbcom.PriceLevelRef_FullName.text = self.PriceLevelRef.FullName
        if self.ExternalGUID:
            self.qbcom.ExternalGUID = ET.SubElement(self.qbcom.CustomerAdd, 'ExternalGUID')
            self.qbcom.ExternalGUID.text = self.ExternalGUID
        if self.CurrencyRef.ListID or self.CurrencyRef.FullName:
            self.qbcom.CurrencyRef = ET.SubElement(self.qbcom.CustomerAdd, 'CurrencyRef')
            self.qbcom.CurrencyRef_ListID = ET.SubElement(self.qbcom.CurrencyRef, 'ListID')
            self.qbcom.CurrencyRef_ListID.text = self.CurrencyRef.ListID
            self.qbcom.CurrencyRef_FullName = ET.SubElement(self.qbcom.CurrencyRef, 'FullName')
            self.qbcom.CurrencyRef_FullName.text = self.CurrencyRef.FullName
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.CustomerAddRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item

    def set_CreditCardChargeAddRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.CreditCardChargeAddRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, 'CreditCardChargeAddRq')
        self.qbcom.CreditCardChargeAdd = ET.SubElement(self.qbcom.CreditCardChargeAddRq, 'CreditCardChargeAdd')
        if self.AccountRef.ListID or self.AccountRef.FullName:
            self.qbcom.AccountRef = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'AccountRef')
            if self.AccountRef.ListID:
                self.qbcom.AccountRef_ListID = ET.SubElement(self.qbcom.AccountRef, 'ListID')
                self.qbcom.AccountRef_ListID.text = self.AccountRef.ListID
            elif self.AccountRef.FullName:
                self.qbcom.AccountRef_FullName = ET.SubElement(self.qbcom.AccountRef, 'FullName')
                self.qbcom.AccountRef_FullName.text = self.AccountRef.FullName
        if self.PayeeEntityRef.ListID or self.PayeeEntityRef.FullName:
            self.qbcom.PayeeEntityRef = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'PayeeEntityRef')
            if self.PayeeEntityRef.ListID:
                self.qbcom.PayeeEntityRef_ListID = ET.SubElement(self.qbcom.PayeeEntityRef, 'ListID')
                self.qbcom.PayeeEntityRef_ListID.text = self.PayeeEntityRef.ListID
            elif self.PayeeEntityRef.FullName:
                self.qbcom.PayeeEntityRef_FullName = ET.SubElement(self.qbcom.PayeeEntityRef, 'FullName')
                self.qbcom.PayeeEntityRef_FullName.text = self.PayeeEntityRef.FullName
        if self.RefNumber:
            self.qbcom.RefNumber = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'RefNumber')
            self.qbcom.RefNumber.text = self.RefNumber
        if self.TxnDate:
            self.qbcom.TxnDate = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'TxnDate')
            self.qbcom.TxnDate.text = self.TxnDate
        if self.Memo:
            self.qbcom.Memo = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'Memo')
            self.qbcom.Memo.text = self.Memo
        if self.ExchangeRate:
            self.qbcom.ExchangeRate = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'ExchangeRate')
            self.qbcom.ExchangeRate.text = self.ExchangeRate
        if self.ExternalGUID:
            self.qbcom.ExternalGUID = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'ExternalGUID')
            self.qbcom.ExternalGUID.text = self.ExternalGUID
        if self.ExpenseLineAdd.AccountRef.ListID or self.ExpenseLineAdd.AccountRef.FullName:
            self.qbcom.ExpenseLineAdd = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'ExpenseLineAdd')
            if self.ExpenseLineAdd.AccountRef.ListID or self.ExpenseLineAdd.AccountRef.FullName:
                self.qbcom.ExpenseLineAdd_AccountRef = ET.SubElement(self.qbcom.ExpenseLineAdd, 'AccountRef')
                if self.ExpenseLineAdd.AccountRef.ListID:
                    self.qbcom.ExpenseLineAdd_AccountRef_ListID = ET.SubElement(self.qbcom.ExpenseLineAdd_AccountRef, 'ListID')
                    self.qbcom.ExpenseLineAdd_AccountRef_ListID.text = self.ExpenseLineAdd.AccountRef.ListID
                elif self.ExpenseLineAdd.AccountRef.FullName:
                    self.qbcom.ExpenseLineAdd_AccountRef_FullName = ET.SubElement(self.qbcom.ExpenseLineAdd_AccountRef, 'FullName')
                    self.qbcom.ExpenseLineAdd_AccountRef_FullName.text = self.ExpenseLineAdd.AccountRef.FullName
            if self.ExpenseLineAdd.Amount:
                self.qbcom.ExpenseLineAdd_Amount = ET.SubElement(self.qbcom.ExpenseLineAdd, 'Amount')
                self.qbcom.ExpenseLineAdd_Amount.text = self.ExpenseLineAdd.Amount
            if self.ExpenseLineAdd.Memo:
                self.qbcom.ExpenseLineAdd_Memo = ET.SubElement(self.qbcom.ExpenseLineAdd, 'Memo')
                self.qbcom.ExpenseLineAdd_Memo.text = self.ExpenseLineAdd.Memo
            if self.ExpenseLineAdd.CustomerRef.ListID or self.ExpenseLineAdd.CustomerRef.FullName:
                self.qbcom.ExpenseLineAdd_CustomerRef = ET.SubElement(self.qbcom.ExpenseLineAdd, 'CustomerRef')
                if self.ExpenseLineAdd.CustomerRef.ListID:
                    self.qbcom.ExpenseLineAdd_CustomerRef_ListID = ET.SubElement(self.qbcom.ExpenseLineAdd_CustomerRef, 'ListID')
                    self.qbcom.ExpenseLineAdd_CustomerRef_ListID.text = self.ExpenseLineAdd.CustomerRef.ListID
                elif self.ExpenseLineAdd.CustomerRef.FullName:
                    self.qbcom.ExpenseLineAdd_CustomerRef_FullName = ET.SubElement(self.qbcom.ExpenseLineAdd_CustomerRef, 'FullName')
                    self.qbcom.ExpenseLineAdd_CustomerRef_FullName.text = self.ExpenseLineAdd.CustomerRef.FullName
            if self.ExpenseLineAdd.ClassRef.ListID or self.ExpenseLineAdd.ClassRef.FullName:
                self.qbcom.ExpenseLineAdd_ClassRef = ET.SubElement(self.qbcom.ExpenseLineAdd, 'ClassRef')
                if self.ExpenseLineAdd.ClassRef.ListID:
                    self.qbcom.ExpenseLineAdd_ClassRef_ListID = ET.SubElement(self.qbcom.ExpenseLineAdd_ClassRef, 'ListID')
                    self.qbcom.ExpenseLineAdd_ClassRef_ListID.text = self.ExpenseLineAdd.ClassRef.ListID
                elif self.ExpenseLineAdd.ClassRef.FullName:
                    self.qbcom.ExpenseLineAdd_ClassRef_FullName = ET.SubElement(self.qbcom.ExpenseLineAdd_ClassRef, 'FullName')
                    self.qbcom.ExpenseLineAdd_ClassRef_FullName.text = self.ExpenseLineAdd.ClassRef.FullName
            if self.ExpenseLineAdd.BillableStatus:
                self.qbcom.ExpenseLineAdd_BillableStatus = ET.SubElement(self.qbcom.ExpenseLineAdd, 'BillableStatus')
                self.qbcom.ExpenseLineAdd_BillableStatus.text = self.ExpenseLineAdd.BillableStatus
            if self.ExpenseLineAdd.SalesRepRef.ListID or self.ExpenseLineAdd.SalesRepRef.FullName:
                self.qbcom.ExpenseLineAdd_SalesRepRef = ET.SubElement(self.qbcom.ExpenseLineAdd, 'SalesRepRef')
                if self.ExpenseLineAdd.SalesRepRef.ListID:
                    self.qbcom.ExpenseLineAdd_SalesRepRef_ListID = ET.SubElement(self.qbcom.ExpenseLineAdd_SalesRepRef, 'ListID')
                    self.qbcom.ExpenseLineAdd_SalesRepRef_ListID.text = self.ExpenseLineAdd.SalesRepRef.ListID
                elif self.ExpenseLineAdd.SalesRepRef.FullName:
                    self.qbcom.ExpenseLineAdd_SalesRepRef_FullName = ET.SubElement(self.qbcom.ExpenseLineAdd_SalesRepRef, 'FullName')
                    self.qbcom.ExpenseLineAdd_SalesRepRef_FullName.text = self.ExpenseLineAdd.SalesRepRef.FullName
            if (self.ExpenseLineAdd.DataExt.OwnerID or
                    self.ExpenseLineAdd.DataExt.DataExtName or
                    self.ExpenseLineAdd.DataExt.DataExtValue):
                self.qbcom.ExpenseLineAdd_DataExt = ET.SubElement(self.qbcom.ExpenseLineAdd, 'DataExt')
                if self.ExpenseLineAdd.DataExt.OwnerID:
                    self.qbcom.ExpenseLineAdd_DataExt_OwnerID = ET.SubElement(self.qbcom.ExpenseLineAdd_DataExt, 'OwnerID')
                    self.qbcom.ExpenseLineAdd_DataExt_OwnerID.text = self.ExpenseLineAdd.DataExt.OwnerID
                if self.ExpenseLineAdd.DataExt.DataExtName:
                    self.qbcom.ExpenseLineAdd_DataExt_DataExtName = ET.SubElement(self.qbcom.ExpenseLineAdd_DataExt, 'DataExtName')
                    self.qbcom.ExpenseLineAdd_DataExt_DataExtName.text = self.ExpenseLineAdd.DataExt.DataExtName
                if self.ExpenseLineAdd.DataExt.DataExtValue:
                    self.qbcom.ExpenseLineAdd_DataExt_DataExtValue = ET.SubElement(self.qbcom.ExpenseLineAdd_DataExt, 'DataExtValue')
                    self.qbcom.ExpenseLineAdd_DataExt_DataExtValue.text = self.ExpenseLineAdd.DataExt.DataExtValue
        elif (self.ItemLineAdd.ItemRef.ListID or
                self.ItemLineAdd.ItemRef.FullName):
            self.qbcom.ItemLineAdd = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'ItemLineAdd')
            if self.ItemLineAdd.ItemRef.ListID or self.ItemLineAdd.ItemRef.FullName:
                self.qbcom.ItemLineAdd_ItemRef = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'ItemRef')
                if self.ItemLineAdd.ItemRef.ListID:
                    self.qbcom.ItemLineAdd_ItemRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.ItemLineAdd_ItemRef_ListID.text = self.ItemLineAdd.ItemRef.ListID
                elif self.ItemLineAdd.ItemRef.FullName:
                    self.qbcom.ItemLineAdd_ItemRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.ItemLineAdd_ItemRef_FullName.text = self.ItemLineAdd.ItemRef.FullName
            if self.ItemLineAdd.InventorySiteRef.ListID or self.ItemLineAdd.InventorySiteRef.FullName:
                self.qbcom.ItemLineAdd.InventorySiteRef = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'InventorySiteRef')
                if self.ItemLineAdd.ItemLineAdd.InventorySiteRef.ListID:
                    self.qbcom.ItemLineAdd_InventorySiteRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.ItemLineAdd_InventorySiteRef_ListID.text = self.ItemLineAdd.InventorySiteRef.ListID
                elif self.ItemLineAdd.ItemLineAdd.InventorySiteRef.FullName:
                    self.qbcom.ItemLineAdd_InventorySiteRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.ItemLineAdd_InventorySiteRef_FullName.text = self.ItemLineAdd.InventorySiteRef.FullName
            if self.ItemLineAdd.InventorySiteLocationRef.ListID or self.ItemLineAdd.InventorySiteLocationRef.FullName:
                self.qbcom.ItemLineAdd_InventorySiteLocationRef = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'InventorySiteLocationRef')
                if self.ItemLineAdd.InventorySiteLocationRef.ListID:
                    self.qbcom.ItemLineAdd_InventorySiteLocationRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.ItemLineAdd_InventorySiteLocationRef_ListID.text = self.ItemLineAdd.InventorySiteLocationRef.ListID
                elif self.ItemLineAdd.InventorySiteLocationRef.FullName:
                    self.qbcom.ItemLineAdd_InventorySiteLocationRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.ItemLineAdd_InventorySiteLocationRef_FullName.text = self.ItemLineAdd.InventorySiteLocationRef.FullName
            if self.ItemLineAdd.SerialNumber:
                self.qbcom.ItemLineAdd_SerialNumber = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'SerialNumber')
                self.qbcom.ItemLineAdd_SerialNumber.text = self.ItemLineAdd.SerialNumber
            elif self.ItemLineAdd.LotNumber:
                self.qbcom.ItemLineAdd_LotNumber = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'LotNumber')
                self.qbcom.ItemLineAdd_LotNumber.text = self.ItemLineAdd.LotNumber
            if self.ItemLineAdd.Desc:
                self.qbcom.ItemLineAdd_Desc = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'Desc')
                self.qbcom.ItemLineAdd_Desc.text = self.ItemLineAdd.Desc
            if self.ItemLineAdd.Quantity:
                self.qbcom.ItemLineAdd_Quantity = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'Quantity')
                self.qbcom.ItemLineAdd_Quantity.text = self.ItemLineAdd.Quantity
            if self.ItemLineAdd.UnitOfMeasure:
                self.qbcom.ItemLineAdd_UnitOfMeasure = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'UnitOfMeasure')
                self.qbcom.ItemLineAdd_UnitOfMeasure.text = self.ItemLineAdd.UnitOfMeasure
            if self.ItemLineAdd.Cost:
                self.qbcom.ItemLineAdd_Cost = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'Cost')
                self.qbcom.ItemLineAdd_Cost.text = self.ItemLineAdd.Cost
            if self.ItemLineAdd.Amount:
                self.qbcom.ItemLineAdd_Amount = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'Amount')
                self.qbcom.ItemLineAdd_Amount.text = self.ItemLineAdd.Amount
            if self.ItemLineAdd.CustomerRef.ListID or self.ItemLineAdd.CustomerRef.FullName:
                self.qbcom.ItemLineAdd_CustomerRef = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'CustomerRef')
                if self.ItemLineAdd.CustomerRef.ListID:
                    self.qbcom.ItemLineAdd_CustomerRef_ListID = ET.SubElement(self.qbcom.ItemLineAdd.CustomerRef, 'ListID')
                    self.qbcom.ItemLineAdd_CustomerRef_ListID.text = self.ItemLineAdd.CustomerRef.ListID
                elif self.ItemLineAdd.CustomerRef.FullName:
                    self.qbcom.ItemLineAdd_CustomerRef_FullName = ET.SubElement(self.qbcom.ItemLineAdd.CustomerRef, 'FullName')
                    self.qbcom.ItemLineAdd_CustomerRef_FullName.text = self.ItemLineAdd.CustomerRef.FullName
            if self.ItemLineAdd.ClassRef.ListID or self.ItemLineAdd.ClassRef.FullName:
                self.qbcom.ItemLineAdd_ClassRef = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'ClassRef')
                if self.ItemLineAdd.ClassRef.ListID:
                    self.qbcom.ItemLineAdd_ClassRef_ListID = ET.SubElement(self.qbcom.ItemLineAdd.ClassRef, 'ListID')
                    self.qbcom.ItemLineAdd_ClassRef_ListID.text = self.ItemLineAdd.ClassRef.ListID
                elif self.ItemLineAdd.ClassRef.FullName:
                    self.qbcom.ItemLineAdd_ClassRef_FullName = ET.SubElement(self.qbcom.ItemLineAdd.ClassRef, 'FullName')
                    self.qbcom.ItemLineAdd_ClassRef_FullName.text = self.ItemLineAdd.ClassRef.FullName
            if self.ItemLineAdd.BillableStatus:
                self.qbcom.ItemLineAdd_BillableStatus = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'BillableStatus')
                self.qbcom.ItemLineAdd_BillableStatus.text = self.ItemLineAdd.BillableStatus
            if self.ItemLineAdd.OverrideItemAccountRef.ListID or self.ItemLineAdd.OverrideItemAccountRef.FullName:
                self.qbcom.ItemLineAdd_OverrideItemAccountRef = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'OverrideItemAccountRef')
                if self.ItemLineAdd.OverrideItemAccountRef.ListID:
                    self.qbcom.ItemLineAdd_OverrideItemAccountRef_ListID = ET.SubElement(self.qbcom.ItemLineAdd.OverrideItemAccountRef, 'ListID')
                    self.qbcom.ItemLineAdd_OverrideItemAccountRef_ListID.text = self.ItemLineAdd.OverrideItemAccountRef.ListID
                elif self.ItemLineAdd.OverrideItemAccountRef.FullName:
                    self.qbcom.ItemLineAdd_OverrideItemAccountRef_FullName = ET.SubElement(self.qbcom.ItemLineAdd.OverrideItemAccountRef, 'FullName')
                    self.qbcom.ItemLineAdd_OverrideItemAccountRef_FullName.text = self.ItemLineAdd.OverrideItemAccountRef.FullName
            if self.ItemLineAdd.SalesRepRef.ListID or self.ItemLineAdd.SalesRepRef.FullName:
                self.qbcom.ItemLineAdd_SalesRepRef = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'SalesRepRef')
                if self.ItemLineAdd.SalesRepRef.ListID:
                    self.qbcom.ItemLineAdd_SalesRepRef_ListID = ET.SubElement(self.qbcom.ItemLineAdd.SalesRepRef, 'ListID')
                    self.qbcom.ItemLineAdd_SalesRepRef_ListID.text = self.ItemLineAdd.SalesRepRef.ListID
                elif self.ItemLineAdd.SalesRepRef.FullName:
                    self.qbcom.ItemLineAdd_SalesRepRef_FullName = ET.SubElement(self.qbcom.ItemLineAdd.SalesRepRef, 'FullName')
                    self.qbcom.ItemLineAdd_SalesRepRef_FullName.text = self.ItemLineAdd.SalesRepRef.FullName
            if self.ItemLineAdd.DataExt.OwnerID or self.ItemLineAdd.DataExt.DataExtName or self.ItemLineAdd.DataExt.DataExtValue:
                self.qbcom.ItemLineAdd_DataExt = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'DataExt')
                if self.ItemLineAdd.DataExt.OwnerID:
                    self.qbcom.ItemLineAdd_DataExt_OwnerID = ET.SubElement(self.qbcom.ItemLineAdd.DataExt, 'OwnerID')
                    self.qbcom.ItemLineAdd_DataExt_OwnerID.text = self.ItemLineAdd.DataExt.OwnerID
                if self.ItemLineAdd.DataExt.DataExtName:
                    self.qbcom.ItemLineAdd_DataExt_DataExtName = ET.SubElement(self.qbcom.ItemLineAdd.DataExt, 'DataExtName')
                    self.qbcom.ItemLineAdd_DataExt_DataExtName.text = self.ItemLineAdd.DataExt.DataExtName
                if self.ItemLineAdd.DataExt.DataExtValue:
                    self.qbcom.ItemLineAdd_DataExt_DataExtValue = ET.SubElement(self.qbcom.ItemLineAdd.DataExt, 'DataExtValue')
                    self.qbcom.ItemLineAdd_DataExt_DataExtValue.text = self.ItemLineAdd.DataExt.DataExtValue
        elif (self.ItemGroupLineAdd.ItemGroupRef.ListID or
                self.ItemGroupLineAdd.ItemGroupRef.FullName):
            self.qbcom.ItemGroupLineAdd = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'ItemGroupLineAdd')
            if self.ItemGroupLineAdd.ItemGroupRef.ListID or self.ItemGroupLineAdd.ItemGroupRef.FullName:
                self.qbcom.ItemGroupLineAdd_ItemGroupRef = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'ItemGroupRef')
                if self.ItemLineAdd.ItemGroupRef.ListID:
                    self.qbcom.ItemGroupLineAdd_ItemGroupRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.ItemGroupLineAdd_ItemGroupRef_ListID.text = self.ItemGroupLineAdd.ItemGroupRef.ListID
                elif self.ItemLineAdd.ItemGroupRef.FullName:
                    self.qbcom.ItemGroupLineAdd_ItemGroupRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.ItemGroupLineAdd_ItemGroupRef_FullName.text = self.ItemGroupLineAdd.ItemGroupRef.FullName
            if self.ItemGroupLineAdd.Quantity:
                self.qbcom.ItemGroupLineAdd_Quantity = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'Quantity')
                self.qbcom.ItemGroupLineAdd_Quantity.text = self.ItemGroupLineAdd.Quantity
            if self.ItemGroupLineAdd.UnitOfMeasure:
                self.qbcom.ItemGroupLineAdd_UnitOfMeasure = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'UnitOfMeasure')
                self.qbcom.ItemGroupLineAdd_UnitOfMeasure.text = self.ItemGroupLineAdd.UnitOfMeasure
            if self.ItemGroupLineAdd.InventorySiteRef.ListID or self.ItemGroupLineAdd.InventorySiteRef.FullName:
                self.qbcom.ItemGroupLineAdd_InventorySiteRef = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'InventorySiteRef')
                if self.ItemLineAdd.InventorySiteRef.ListID:
                    self.qbcom.ItemGroupLineAdd_InventorySiteRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.ItemGroupLineAdd_InventorySiteRef_ListID.text = self.ItemGroupLineAdd.InventorySiteRef.ListID
                elif self.ItemLineAdd.InventorySiteRef.FullName:
                    self.qbcom.ItemGroupLineAdd_InventorySiteRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.ItemGroupLineAdd_InventorySiteRef_FullName.text = self.ItemGroupLineAdd.InventorySiteRef.FullName
            if self.ItemGroupLineAdd.InventorySiteLocationRef.ListID or self.ItemGroupLineAdd.InventorySiteLocationRef.FullName:
                self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'InventorySiteLocationRef')
                if self.ItemLineAdd.InventorySiteLocationRef.ListID:
                    self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef_ListID.text = self.ItemGroupLineAdd.InventorySiteLocationRef.ListID
                elif self.ItemLineAdd.InventorySiteLocationRef.FullName:
                    self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef_FullName.text = self.ItemGroupLineAdd.InventorySiteLocationRef.FullName
            if self.ItemGroupLineAdd.DataExt.OwnerID or self.ItemGroupLineAdd.DataExt.DataExtName or self.ItemGroupLineAdd.DataExt.DataExtValue:
                self.qbcom.ItemGroupLineAdd_DataExt = ET.SubElement(self.qbcom.CreditCardChargeAdd, 'DataExt')
                if self.ItemGroupLineAdd.DataExt.OwnerID:
                    self.qbcom.ItemGroupLineAdd_DataExt_OwnerID = ET.SubElement(self.qbcom.ItemGroupLineAdd.DataExt, 'OwnerID')
                    self.qbcom.ItemGroupLineAdd_DataExt_OwnerID.text = self.ItemGroupLineAdd.DataExt.OwnerID
                if self.ItemGroupLineAdd.DataExt.DataExtName:
                    self.qbcom.ItemGroupLineAdd_DataExt_DataExtName = ET.SubElement(self.qbcom.ItemGroupLineAdd.DataExt, 'DataExtName')
                    self.qbcom.ItemGroupLineAdd_DataExt_DataExtName.text = self.ItemGroupLineAdd.DataExt.DataExtName
                if self.ItemGroupLineAdd.DataExt.DataExtValue:
                    self.qbcom.ItemGroupLineAdd_DataExt_DataExtValue = ET.SubElement(self.qbcom.ItemGroupLineAdd.DataExt, 'DataExtValue')
                    self.qbcom.ItemGroupLineAdd_DataExt_DataExtValue.text = self.ItemGroupLineAdd.DataExt.DataExtValue
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.CreditCardChargeAddRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item

    def set_CreditCardCreditAddRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.CreditCardCreditAddRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, 'CreditCardCreditAddRq')
        self.qbcom.CreditCardCreditAdd = ET.SubElement(self.qbcom.CreditCardCreditAddRq, 'CreditCardCreditAdd')
        if self.AccountRef.ListID or self.AccountRef.FullName:
            self.qbcom.AccountRef = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'AccountRef')
            if self.AccountRef.ListID:
                self.qbcom.AccountRef_ListID = ET.SubElement(self.qbcom.AccountRef, 'ListID')
                self.qbcom.AccountRef_ListID.text = self.AccountRef.ListID
            elif self.AccountRef.FullName:
                self.qbcom.AccountRef_FullName = ET.SubElement(self.qbcom.AccountRef, 'FullName')
                self.qbcom.AccountRef_FullName.text = self.AccountRef.FullName
        if self.PayeeEntityRef.ListID or self.PayeeEntityRef.FullName:
            self.qbcom.PayeeEntityRef = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'PayeeEntityRef')
            if self.PayeeEntityRef.ListID:
                self.qbcom.PayeeEntityRef_ListID = ET.SubElement(self.qbcom.PayeeEntityRef, 'ListID')
                self.qbcom.PayeeEntityRef_ListID.text = self.PayeeEntityRef.ListID
            elif self.PayeeEntityRef.FullName:
                self.qbcom.PayeeEntityRef_FullName = ET.SubElement(self.qbcom.PayeeEntityRef, 'FullName')
                self.qbcom.PayeeEntityRef_FullName.text = self.PayeeEntityRef.FullName
        if self.RefNumber:
            self.qbcom.RefNumber = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'RefNumber')
            self.qbcom.RefNumber.text = self.RefNumber
        if self.TxnDate:
            self.qbcom.TxnDate = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'TxnDate')
            self.qbcom.TxnDate.text = self.TxnDate
        if self.Memo:
            self.qbcom.Memo = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'Memo')
            self.qbcom.Memo.text = self.Memo
        if self.ExchangeRate:
            self.qbcom.ExchangeRate = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'ExchangeRate')
            self.qbcom.ExchangeRate.text = self.ExchangeRate
        if self.ExternalGUID:
            self.qbcom.ExternalGUID = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'ExternalGUID')
            self.qbcom.ExternalGUID.text = self.ExternalGUID
        if self.ExpenseLineAdd.AccountRef.ListID or self.ExpenseLineAdd.AccountRef.FullName:
            self.qbcom.ExpenseLineAdd = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'ExpenseLineAdd')
            if self.ExpenseLineAdd.AccountRef.ListID or self.ExpenseLineAdd.AccountRef.FullName:
                self.qbcom.ExpenseLineAdd_AccountRef = ET.SubElement(self.qbcom.ExpenseLineAdd, 'AccountRef')
                if self.ExpenseLineAdd.AccountRef.ListID:
                    self.qbcom.ExpenseLineAdd_AccountRef_ListID = ET.SubElement(self.qbcom.ExpenseLineAdd_AccountRef, 'ListID')
                    self.qbcom.ExpenseLineAdd_AccountRef_ListID.text = self.ExpenseLineAdd.AccountRef.ListID
                elif self.ExpenseLineAdd.AccountRef.FullName:
                    self.qbcom.ExpenseLineAdd_AccountRef_FullName = ET.SubElement(self.qbcom.ExpenseLineAdd_AccountRef, 'FullName')
                    self.qbcom.ExpenseLineAdd_AccountRef_FullName.text = self.ExpenseLineAdd.AccountRef.FullName
            if self.ExpenseLineAdd.Amount:
                self.qbcom.ExpenseLineAdd_Amount = ET.SubElement(self.qbcom.ExpenseLineAdd, 'Amount')
                self.qbcom.ExpenseLineAdd_Amount.text = self.ExpenseLineAdd.Amount
            if self.ExpenseLineAdd.Memo:
                self.qbcom.ExpenseLineAdd_Memo = ET.SubElement(self.qbcom.ExpenseLineAdd, 'Memo')
                self.qbcom.ExpenseLineAdd_Memo.text = self.ExpenseLineAdd.Memo
            if self.ExpenseLineAdd.CustomerRef.ListID or self.ExpenseLineAdd.CustomerRef.FullName:
                self.qbcom.ExpenseLineAdd_CustomerRef = ET.SubElement(self.qbcom.ExpenseLineAdd, 'CustomerRef')
                if self.ExpenseLineAdd.CustomerRef.ListID:
                    self.qbcom.ExpenseLineAdd_CustomerRef_ListID = ET.SubElement(self.qbcom.ExpenseLineAdd_CustomerRef, 'ListID')
                    self.qbcom.ExpenseLineAdd_CustomerRef_ListID.text = self.ExpenseLineAdd.CustomerRef.ListID
                elif self.ExpenseLineAdd.CustomerRef.FullName:
                    self.qbcom.ExpenseLineAdd_CustomerRef_FullName = ET.SubElement(self.qbcom.ExpenseLineAdd_CustomerRef, 'FullName')
                    self.qbcom.ExpenseLineAdd_CustomerRef_FullName.text = self.ExpenseLineAdd.CustomerRef.FullName
            if self.ExpenseLineAdd.ClassRef.ListID or self.ExpenseLineAdd.ClassRef.FullName:
                self.qbcom.ExpenseLineAdd_ClassRef = ET.SubElement(self.qbcom.ExpenseLineAdd, 'ClassRef')
                if self.ExpenseLineAdd.ClassRef.ListID:
                    self.qbcom.ExpenseLineAdd_ClassRef_ListID = ET.SubElement(self.qbcom.ExpenseLineAdd_ClassRef, 'ListID')
                    self.qbcom.ExpenseLineAdd_ClassRef_ListID.text = self.ExpenseLineAdd.ClassRef.ListID
                elif self.ExpenseLineAdd.ClassRef.FullName:
                    self.qbcom.ExpenseLineAdd_ClassRef_FullName = ET.SubElement(self.qbcom.ExpenseLineAdd_ClassRef, 'FullName')
                    self.qbcom.ExpenseLineAdd_ClassRef_FullName.text = self.ExpenseLineAdd.ClassRef.FullName
            if self.ExpenseLineAdd.BillableStatus:
                self.qbcom.ExpenseLineAdd_BillableStatus = ET.SubElement(self.qbcom.ExpenseLineAdd, 'BillableStatus')
                self.qbcom.ExpenseLineAdd_BillableStatus.text = self.ExpenseLineAdd.BillableStatus
            if self.ExpenseLineAdd.SalesRepRef.ListID or self.ExpenseLineAdd.SalesRepRef.FullName:
                self.qbcom.ExpenseLineAdd_SalesRepRef = ET.SubElement(self.qbcom.ExpenseLineAdd, 'SalesRepRef')
                if self.ExpenseLineAdd.SalesRepRef.ListID:
                    self.qbcom.ExpenseLineAdd_SalesRepRef_ListID = ET.SubElement(self.qbcom.ExpenseLineAdd_SalesRepRef, 'ListID')
                    self.qbcom.ExpenseLineAdd_SalesRepRef_ListID.text = self.ExpenseLineAdd.SalesRepRef.ListID
                elif self.ExpenseLineAdd.SalesRepRef.FullName:
                    self.qbcom.ExpenseLineAdd_SalesRepRef_FullName = ET.SubElement(self.qbcom.ExpenseLineAdd_SalesRepRef, 'FullName')
                    self.qbcom.ExpenseLineAdd_SalesRepRef_FullName.text = self.ExpenseLineAdd.SalesRepRef.FullName
            if (self.ExpenseLineAdd.DataExt.OwnerID or
                    self.ExpenseLineAdd.DataExt.DataExtName or
                    self.ExpenseLineAdd.DataExt.DataExtValue):
                self.qbcom.ExpenseLineAdd_DataExt = ET.SubElement(self.qbcom.ExpenseLineAdd, 'DataExt')
                if self.ExpenseLineAdd.DataExt.OwnerID:
                    self.qbcom.ExpenseLineAdd_DataExt_OwnerID = ET.SubElement(self.qbcom.ExpenseLineAdd_DataExt, 'OwnerID')
                    self.qbcom.ExpenseLineAdd_DataExt_OwnerID.text = self.ExpenseLineAdd.DataExt.OwnerID
                if self.ExpenseLineAdd.DataExt.DataExtName:
                    self.qbcom.ExpenseLineAdd_DataExt_DataExtName = ET.SubElement(self.qbcom.ExpenseLineAdd_DataExt, 'DataExtName')
                    self.qbcom.ExpenseLineAdd_DataExt_DataExtName.text = self.ExpenseLineAdd.DataExt.DataExtName
                if self.ExpenseLineAdd.DataExt.DataExtValue:
                    self.qbcom.ExpenseLineAdd_DataExt_DataExtValue = ET.SubElement(self.qbcom.ExpenseLineAdd_DataExt, 'DataExtValue')
                    self.qbcom.ExpenseLineAdd_DataExt_DataExtValue.text = self.ExpenseLineAdd.DataExt.DataExtValue
        elif (self.ItemLineAdd.ItemRef.ListID or
                self.ItemLineAdd.ItemRef.FullName):
            self.qbcom.ItemLineAdd = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'ItemLineAdd')
            if self.ItemLineAdd.ItemRef.ListID or self.ItemLineAdd.ItemRef.FullName:
                self.qbcom.ItemLineAdd_ItemRef = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'ItemRef')
                if self.ItemLineAdd.ItemRef.ListID:
                    self.qbcom.ItemLineAdd_ItemRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.ItemLineAdd_ItemRef_ListID.text = self.ItemLineAdd.ItemRef.ListID
                elif self.ItemLineAdd.ItemRef.FullName:
                    self.qbcom.ItemLineAdd_ItemRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.ItemLineAdd_ItemRef_FullName.text = self.ItemLineAdd.ItemRef.FullName
            if self.ItemLineAdd.InventorySiteRef.ListID or self.ItemLineAdd.InventorySiteRef.FullName:
                self.qbcom.ItemLineAdd.InventorySiteRef = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'InventorySiteRef')
                if self.ItemLineAdd.ItemLineAdd.InventorySiteRef.ListID:
                    self.qbcom.ItemLineAdd_InventorySiteRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.ItemLineAdd_InventorySiteRef_ListID.text = self.ItemLineAdd.InventorySiteRef.ListID
                elif self.ItemLineAdd.ItemLineAdd.InventorySiteRef.FullName:
                    self.qbcom.ItemLineAdd_InventorySiteRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.ItemLineAdd_InventorySiteRef_FullName.text = self.ItemLineAdd.InventorySiteRef.FullName
            if self.ItemLineAdd.InventorySiteLocationRef.ListID or self.ItemLineAdd.InventorySiteLocationRef.FullName:
                self.qbcom.ItemLineAdd_InventorySiteLocationRef = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'InventorySiteLocationRef')
                if self.ItemLineAdd.InventorySiteLocationRef.ListID:
                    self.qbcom.ItemLineAdd_InventorySiteLocationRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.ItemLineAdd_InventorySiteLocationRef_ListID.text = self.ItemLineAdd.InventorySiteLocationRef.ListID
                elif self.ItemLineAdd.InventorySiteLocationRef.FullName:
                    self.qbcom.ItemLineAdd_InventorySiteLocationRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.ItemLineAdd_InventorySiteLocationRef_FullName.text = self.ItemLineAdd.InventorySiteLocationRef.FullName
            if self.ItemLineAdd.SerialNumber:
                self.qbcom.ItemLineAdd_SerialNumber = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'SerialNumber')
                self.qbcom.ItemLineAdd_SerialNumber.text = self.ItemLineAdd.SerialNumber
            elif self.ItemLineAdd.LotNumber:
                self.qbcom.ItemLineAdd_LotNumber = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'LotNumber')
                self.qbcom.ItemLineAdd_LotNumber.text = self.ItemLineAdd.LotNumber
            if self.ItemLineAdd.Desc:
                self.qbcom.ItemLineAdd_Desc = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'Desc')
                self.qbcom.ItemLineAdd_Desc.text = self.ItemLineAdd.Desc
            if self.ItemLineAdd.Quantity:
                self.qbcom.ItemLineAdd_Quantity = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'Quantity')
                self.qbcom.ItemLineAdd_Quantity.text = self.ItemLineAdd.Quantity
            if self.ItemLineAdd.UnitOfMeasure:
                self.qbcom.ItemLineAdd_UnitOfMeasure = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'UnitOfMeasure')
                self.qbcom.ItemLineAdd_UnitOfMeasure.text = self.ItemLineAdd.UnitOfMeasure
            if self.ItemLineAdd.Cost:
                self.qbcom.ItemLineAdd_Cost = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'Cost')
                self.qbcom.ItemLineAdd_Cost.text = self.ItemLineAdd.Cost
            if self.ItemLineAdd.Amount:
                self.qbcom.ItemLineAdd_Amount = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'Amount')
                self.qbcom.ItemLineAdd_Amount.text = self.ItemLineAdd.Amount
            if self.ItemLineAdd.CustomerRef.ListID or self.ItemLineAdd.CustomerRef.FullName:
                self.qbcom.ItemLineAdd_CustomerRef = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'CustomerRef')
                if self.ItemLineAdd.CustomerRef.ListID:
                    self.qbcom.ItemLineAdd_CustomerRef_ListID = ET.SubElement(self.qbcom.ItemLineAdd.CustomerRef, 'ListID')
                    self.qbcom.ItemLineAdd_CustomerRef_ListID.text = self.ItemLineAdd.CustomerRef.ListID
                elif self.ItemLineAdd.CustomerRef.FullName:
                    self.qbcom.ItemLineAdd_CustomerRef_FullName = ET.SubElement(self.qbcom.ItemLineAdd.CustomerRef, 'FullName')
                    self.qbcom.ItemLineAdd_CustomerRef_FullName.text = self.ItemLineAdd.CustomerRef.FullName
            if self.ItemLineAdd.ClassRef.ListID or self.ItemLineAdd.ClassRef.FullName:
                self.qbcom.ItemLineAdd_ClassRef = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'ClassRef')
                if self.ItemLineAdd.ClassRef.ListID:
                    self.qbcom.ItemLineAdd_ClassRef_ListID = ET.SubElement(self.qbcom.ItemLineAdd.ClassRef, 'ListID')
                    self.qbcom.ItemLineAdd_ClassRef_ListID.text = self.ItemLineAdd.ClassRef.ListID
                elif self.ItemLineAdd.ClassRef.FullName:
                    self.qbcom.ItemLineAdd_ClassRef_FullName = ET.SubElement(self.qbcom.ItemLineAdd.ClassRef, 'FullName')
                    self.qbcom.ItemLineAdd_ClassRef_FullName.text = self.ItemLineAdd.ClassRef.FullName
            if self.ItemLineAdd.BillableStatus:
                self.qbcom.ItemLineAdd_BillableStatus = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'BillableStatus')
                self.qbcom.ItemLineAdd_BillableStatus.text = self.ItemLineAdd.BillableStatus
            if self.ItemLineAdd.OverrideItemAccountRef.ListID or self.ItemLineAdd.OverrideItemAccountRef.FullName:
                self.qbcom.ItemLineAdd_OverrideItemAccountRef = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'OverrideItemAccountRef')
                if self.ItemLineAdd.OverrideItemAccountRef.ListID:
                    self.qbcom.ItemLineAdd_OverrideItemAccountRef_ListID = ET.SubElement(self.qbcom.ItemLineAdd.OverrideItemAccountRef, 'ListID')
                    self.qbcom.ItemLineAdd_OverrideItemAccountRef_ListID.text = self.ItemLineAdd.OverrideItemAccountRef.ListID
                elif self.ItemLineAdd.OverrideItemAccountRef.FullName:
                    self.qbcom.ItemLineAdd_OverrideItemAccountRef_FullName = ET.SubElement(self.qbcom.ItemLineAdd.OverrideItemAccountRef, 'FullName')
                    self.qbcom.ItemLineAdd_OverrideItemAccountRef_FullName.text = self.ItemLineAdd.OverrideItemAccountRef.FullName
            if self.ItemLineAdd.SalesRepRef.ListID or self.ItemLineAdd.SalesRepRef.FullName:
                self.qbcom.ItemLineAdd_SalesRepRef = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'SalesRepRef')
                if self.ItemLineAdd.SalesRepRef.ListID:
                    self.qbcom.ItemLineAdd_SalesRepRef_ListID = ET.SubElement(self.qbcom.ItemLineAdd.SalesRepRef, 'ListID')
                    self.qbcom.ItemLineAdd_SalesRepRef_ListID.text = self.ItemLineAdd.SalesRepRef.ListID
                elif self.ItemLineAdd.SalesRepRef.FullName:
                    self.qbcom.ItemLineAdd_SalesRepRef_FullName = ET.SubElement(self.qbcom.ItemLineAdd.SalesRepRef, 'FullName')
                    self.qbcom.ItemLineAdd_SalesRepRef_FullName.text = self.ItemLineAdd.SalesRepRef.FullName
            if self.ItemLineAdd.DataExt.OwnerID or self.ItemLineAdd.DataExt.DataExtName or self.ItemLineAdd.DataExt.DataExtValue:
                self.qbcom.ItemLineAdd_DataExt = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'DataExt')
                if self.ItemLineAdd.DataExt.OwnerID:
                    self.qbcom.ItemLineAdd_DataExt_OwnerID = ET.SubElement(self.qbcom.ItemLineAdd.DataExt, 'OwnerID')
                    self.qbcom.ItemLineAdd_DataExt_OwnerID.text = self.ItemLineAdd.DataExt.OwnerID
                if self.ItemLineAdd.DataExt.DataExtName:
                    self.qbcom.ItemLineAdd_DataExt_DataExtName = ET.SubElement(self.qbcom.ItemLineAdd.DataExt, 'DataExtName')
                    self.qbcom.ItemLineAdd_DataExt_DataExtName.text = self.ItemLineAdd.DataExt.DataExtName
                if self.ItemLineAdd.DataExt.DataExtValue:
                    self.qbcom.ItemLineAdd_DataExt_DataExtValue = ET.SubElement(self.qbcom.ItemLineAdd.DataExt, 'DataExtValue')
                    self.qbcom.ItemLineAdd_DataExt_DataExtValue.text = self.ItemLineAdd.DataExt.DataExtValue
        elif (self.ItemGroupLineAdd.ItemGroupRef.ListID or
                self.ItemGroupLineAdd.ItemGroupRef.FullName):
            self.qbcom.ItemGroupLineAdd = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'ItemGroupLineAdd')
            if self.ItemGroupLineAdd.ItemGroupRef.ListID or self.ItemGroupLineAdd.ItemGroupRef.FullName:
                self.qbcom.ItemGroupLineAdd_ItemGroupRef = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'ItemGroupRef')
                if self.ItmeGroupLineAdd.ItemGroupRef.ListID:
                    self.qbcom.ItemGroupLineAdd_ItemGroupRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.ItemGroupLineAdd_ItemGroupRef_ListID.text = self.ItemGroupLineAdd.ItemGroupRef.ListID
                elif self.ItmeGroupLineAdd.ItemGroupRef.FullName:
                    self.qbcom.ItemGroupLineAdd_ItemGroupRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.ItemGroupLineAdd_ItemGroupRef_FullName.text = self.ItemGroupLineAdd.ItemGroupRef.FullName
            if self.ItemGroupLineAdd.Quantity:
                self.qbcom.ItemGroupLineAdd_Quantity = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'Quantity')
                self.qbcom.ItemGroupLineAdd_Quantity.text = self.ItemGroupLineAdd.Quantity
            if self.ItemGroupLineAdd.UnitOfMeasure:
                self.qbcom.ItemGroupLineAdd_UnitOfMeasure = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'UnitOfMeasure')
                self.qbcom.ItemGroupLineAdd_UnitOfMeasure.text = self.ItemGroupLineAdd.UnitOfMeasure
            if self.ItemGroupLineAdd.InventorySiteRef.ListID or self.ItemGroupLineAdd.InventorySiteRef.FullName:
                self.qbcom.ItemGroupLineAdd_InventorySiteRef = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'InventorySiteRef')
                if self.ItmeGroupLineAdd.InventorySiteRef.ListID:
                    self.qbcom.ItemGroupLineAdd_InventorySiteRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.ItemGroupLineAdd_InventorySiteRef_ListID.text = self.ItemGroupLineAdd.InventorySiteRef.ListID
                elif self.ItmeGroupLineAdd.InventorySiteRef.FullName:
                    self.qbcom.ItemGroupLineAdd_InventorySiteRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.ItemGroupLineAdd_InventorySiteRef_FullName.text = self.ItemGroupLineAdd.InventorySiteRef.FullName
            if self.ItemGroupLineAdd.InventorySiteLocationRef.ListID or self.ItemGroupLineAdd.InventorySiteLocationRef.FullName:
                self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'InventorySiteLocationRef')
                if self.ItmeGroupLineAdd.InventorySiteLocationRef.ListID:
                    self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef_ListID.text = self.ItemGroupLineAdd.InventorySiteLocationRef.ListID
                elif self.ItmeGroupLineAdd.InventorySiteLocationRef.FullName:
                    self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.ItemGroupLineAdd_InventorySiteLocationRef_FullName.text = self.ItemGroupLineAdd.InventorySiteLocationRef.FullName
            if self.ItemGroupLineAdd.DataExt.OwnerID or self.ItemGroupLineAdd.DataExt.DataExtName or self.ItemGroupLineAdd.DataExt.DataExtValue:
                self.qbcom.ItemGroupLineAdd_DataExt = ET.SubElement(self.qbcom.CreditCardCreditAdd, 'DataExt')
                if self.ItemGroupLineAdd.DataExt.OwnerID:
                    self.qbcom.ItemGroupLineAdd_DataExt_OwnerID = ET.SubElement(self.qbcom.ItemGroupLineAdd.DataExt, 'OwnerID')
                    self.qbcom.ItemGroupLineAdd_DataExt_OwnerID.text = self.ItemGroupLineAdd.DataExt.OwnerID
                if self.ItemGroupLineAdd.DataExt.DataExtName:
                    self.qbcom.ItemGroupLineAdd_DataExt_DataExtName = ET.SubElement(self.qbcom.ItemGroupLineAdd.DataExt, 'DataExtName')
                    self.qbcom.ItemGroupLineAdd_DataExt_DataExtName.text = self.ItemGroupLineAdd.DataExt.DataExtName
                if self.ItemGroupLineAdd.DataExt.DataExtValue:
                    self.qbcom.ItemGroupLineAdd_DataExt_DataExtValue = ET.SubElement(self.qbcom.ItemGroupLineAdd.DataExt, 'DataExtValue')
                    self.qbcom.ItemGroupLineAdd_DataExt_DataExtValue.text = self.ItemGroupLineAdd.DataExt.DataExtValue
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.CreditCardCreditAddRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item

    def set_CreditMemoAddRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.CreditMemoAddRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, 'CreditMemoAddRq')
        self.qbcom.CreditMemoAdd = ET.SubElement(self.qbcom.CreditMemoAddRq, 'CreditMemoAdd')
        if self.CustomerRef.ListID or self.CustomerRef.FullName:
            self.qbcom.CustomerRef = ET.SubElement(self.qbcom.CreditMemoAdd, 'CustomerRef')
            if self.CustomerRef.ListID:
                self.qbcom.CustomerRef_ListID = ET.SubElement(self.qbcom.CustomerRef, 'ListID')
                self.qbcom.CustomerRef_ListID.text = self.CustomerRef.ListID
            elif self.CustomerRef.FullName:
                self.qbcom.CustomerRef_FullName = ET.SubElement(self.qbcom.CustomerRef, 'FullName')
                self.qbcom.CustomerRef_FullName.text = self.CustomerRef.FullName
        if self.ClassRef.ListID or self.ClassRef.FullName:
            self.qbcom.ClassRef = ET.SubElement(self.qbcom.CreditMemoAdd, 'ClassRef')
            if self.ClassRef.ListID:
                self.qbcom.ClassRef_ListID = ET.SubElement(self.qbcom.ClassRef, 'ListID')
                self.qbcom.ClassRef_ListID.text = self.ClassRef.ListID
            elif self.ClassRef.FullName:
                self.qbcom.ClassRef_FullName = ET.SubElement(self.qbcom.ClassRef, 'FullName')
                self.qbcom.ClassRef_FullName.text = self.ClassRef.FullName
        if self.ARAccountRef.ListID or self.ARAccountRef.FullName:
            self.qbcom.ARAccountRef = ET.SubElement(self.qbcom.CreditMemoAdd, 'ARAccountRef')
            if self.ARAccountRef.ListID:
                self.qbcom.ARAccountRef_ListID = ET.SubElement(self.qbcom.ARAccountRef, 'ListID')
                self.qbcom.ARAccountRef_ListID.text = self.ARAccountRef.ListID
            elif self.ARAccountRef.FullName:
                self.qbcom.ARAccountRef_FullName = ET.SubElement(self.qbcom.ARAccountRef, 'FullName')
                self.qbcom.ARAccountRef_FullName.text = self.ARAccountRef.FullName
        if self.TemplateRef.ListID or self.TemplateRef.FullName:
            self.qbcom.TemplateRef = ET.SubElement(self.qbcom.CreditMemoAdd, 'TemplateRef')
            if self.TemplateRef.ListID:
                self.qbcom.TemplateRef_ListID = ET.SubElement(self.qbcom.TemplateRef, 'ListID')
                self.qbcom.TemplateRef_ListID.text = self.TemplateRef.ListID
            elif self.TemplateRef.FullName:
                self.qbcom.TemplateRef_FullName = ET.SubElement(self.qbcom.TemplateRef, 'FullName')
                self.qbcom.TemplateRef_FullName.text = self.TemplateRef.FullName
        if self.TxnDate:
            self.qbcom.TxnDate = ET.SubElement(self.qbcom.CreditMemoAdd, 'TxnDate')
            self.qbcom.TxnDate = self.TxnDate
        if self.RefNumber:
            self.qbcom.RefNumber = ET.SubElement(self.qbcom.CreditMemoAdd, 'RefNumber')
            self.qbcom.RefNumber = self.RefNumber
        if (    self.BillAddress.Addr1 and
                self.BillAddress.Addr2 and
                self.BillAddress.Addr3 and
                self.BillAddress.City and
                self.BillAddress.State and
                self.BillAddress.PostalCode and
                self.BillAddress.Country and
                not self.BillAddress.Addr4 and
                not self.BillAddress.Addr5):
            self.qbcom.BillAddress = ET.SubElement(self.qbcom.CreditMemoAdd, 'BillAddress')
            self.qbcom.BillAddress_Addr1 = ET.SubElement(self.qbcom.BillAddress, 'Addr1')
            self.qbcom.BillAddress_Addr1.text = self.BillAddress.Addr1
            self.qbcom.BillAddress_Addr2 = ET.SubElement(self.qbcom.BillAddress, 'Addr2')
            self.qbcom.BillAddress_Addr2.text = self.BillAddress.Addr2
            self.qbcom.BillAddress_Addr3 = ET.SubElement(self.qbcom.BillAddress, 'Addr3')
            self.qbcom.BillAddress_Addr3.text = self.BillAddress.Addr3
            self.qbcom.BillAddress_City = ET.SubElement(self.qbcom.BillAddress, 'City')
            self.qbcom.BillAddress_City.text = self.BillAddress.City
            self.qbcom.BillAddress_State = ET.SubElement(self.qbcom.BillAddress, 'State')
            self.qbcom.BillAddress_State.text = self.BillAddress.State
            self.qbcom.BillAddress_PostalCode = ET.SubElement(self.qbcom.BillAddress, 'PostalCode')
            self.qbcom.BillAddress_PostalCode.text = self.BillAddress.PostalCode
            if self.BillAddress.Country:
                self.qbcom.BillAddress_Country = ET.SubElement(self.qbcom.BillAddress, 'Country')
                self.qbcom.BillAddress_Country.text = self.BillAddress.Country
            if self.BillAddress.Note:
                self.qbcom.BillAddress_Note = ET.SubElement(self.qbcom.BillAddress, 'Note')
                self.qbcom.BillAddress_Note.text = self.BillAddress.Note
        if (    self.BillAddress.Addr1 and
                self.BillAddress.Addr2 and
                self.BillAddress.Addr3 and
                self.BillAddress.Addr4 and
                self.BillAddress.Addr5 and
                not self.BillAddress.City and
                not self.BillAddress.State and
                not self.BillAddress.PostalCode and
                not self.BillAddress.Country):
            self.qbcom.BillAddress_ = ET.SubElement(self.qbcom.CreditMemoAdd, 'BillAddress')
            self.qbcom.BillAddress_Addr1 = ET.SubElement(self.qbcom.BillAddress, 'Addr1')
            self.qbcom.BillAddress_Addr1.text = self.BillAddress.Addr1
            self.qbcom.BillAddress_Addr2 = ET.SubElement(self.qbcom.BillAddress, 'Addr2')
            self.qbcom.BillAddress_Addr2.text = self.BillAddress.Addr2
            self.qbcom.BillAddress_Addr3 = ET.SubElement(self.qbcom.BillAddress, 'Addr3')
            self.qbcom.BillAddress_Addr3.text = self.BillAddress.Addr3
            self.qbcom.BillAddress_Addr4 = ET.SubElement(self.qbcom.BillAddress, 'Addr4')
            self.qbcom.BillAddress_Addr4.text = self.BillAddress.Addr4
            self.qbcom.BillAddress_Addr5 = ET.SubElement(self.qbcom.BillAddress, 'Addr5')
            self.qbcom.BillAddress_Addr5.text = self.BillAddress.Addr5
            if self.BillAddress.Note:
                self.qbcom.BillAddress_Note = ET.SubElement(self.qbcom.BillAddress, 'Note')
                self.qbcom.BillAddress_Note.text = self.BillAddress.Note
        if (    self.ShipAddress.Addr1 and
                self.ShipAddress.Addr2 and
                self.ShipAddress.Addr3 and
                self.ShipAddress.City and
                self.ShipAddress.State and
                self.ShipAddress.PostalCode and
                not self.ShipAddress.Addr4 and
                not self.ShipAddress.Addr5):
            self.qbcom.ShipAddress = ET.SubElement(self.qbcom.CreditMemoAdd, 'ShipAddress')
            self.qbcom.ShipAddress_Addr1 = ET.SubElement(self.qbcom.ShipAddress, 'Addr1')
            self.qbcom.ShipAddress_Addr1.text = self.ShipAddress.Addr1
            self.qbcom.ShipAddress_Addr2 = ET.SubElement(self.qbcom.ShipAddress, 'Addr2')
            self.qbcom.ShipAddress_Addr2.text = self.ShipAddress.Addr2
            self.qbcom.ShipAddress_Addr3 = ET.SubElement(self.qbcom.ShipAddress, 'Addr3')
            self.qbcom.ShipAddress_Addr3.text = self.ShipAddress.Addr3
            self.qbcom.ShipAddress_City = ET.SubElement(self.qbcom.ShipAddress, 'City')
            self.qbcom.ShipAddress_City.text = self.ShipAddress.City
            self.qbcom.ShipAddress_State = ET.SubElement(self.qbcom.ShipAddress, 'State')
            self.qbcom.ShipAddress_State.text = self.ShipAddress.State
            self.qbcom.ShipAddress_PostalCode = ET.SubElement(self.qbcom.ShipAddress, 'PostalCode')
            self.qbcom.ShipAddress_PostalCode.text = self.ShipAddress.PostalCode
            if self.ShipAddress.Country:
                self.qbcom.ShipAddress_Country = ET.SubElement(self.qbcom.ShipAddress, 'Country')
                self.qbcom.ShipAddress_Country.text = self.ShipAddress.Country
            if self.ShipAddress.Note:
                self.qbcom.ShipAddress_Note = ET.SubElement(self.qbcom.ShipAddress, 'Note')
                self.qbcom.ShipAddress_Note.text = self.ShipAddress.Note
        if (    self.ShipAddress.Addr1 and
                self.ShipAddress.Addr2 and
                self.ShipAddress.Addr3 and
                self.ShipAddress.Addr4 and
                self.ShipAddress.Addr5 and
                not self.ShipAddress.City and
                not self.ShipAddress.State and
                not self.ShipAddress.PostalCode and
                not self.ShipAddress.Country):
            self.qbcom.ShipAddress = ET.SubElement(self.qbcom.CreditMemoAdd, 'ShipAddress')
            self.qbcom.ShipAddress_Addr1 = ET.SubElement(self.qbcom.ShipAddress, 'Addr1')
            self.qbcom.ShipAddress_Addr1.text = self.ShipAddress.Addr1
            self.qbcom.ShipAddress_Addr2 = ET.SubElement(self.qbcom.ShipAddress, 'Addr2')
            self.qbcom.ShipAddress_Addr2.text = self.ShipAddress.Addr2
            self.qbcom.ShipAddress_Addr3 = ET.SubElement(self.qbcom.ShipAddress, 'Addr3')
            self.qbcom.ShipAddress_Addr3.text = self.ShipAddress.Addr3
            self.qbcom.ShipAddress_Addr4 = ET.SubElement(self.qbcom.ShipAddress, 'Addr4')
            self.qbcom.ShipAddress_Addr4.text = self.ShipAddress.Addr4
            self.qbcom.ShipAddress_Addr5 = ET.SubElement(self.qbcom.ShipAddress, 'Addr5')
            self.qbcom.ShipAddress_Addr5.text = self.ShipAddress.Addr5
            if self.ShipAddress.Note:
                self.qbcom.ShipAddress_Note = ET.SubElement(self.qbcom.ShipAddress, 'Note')
                self.qbcom.ShipAddress_Note.text = self.ShipAddress.Note
        if self.IsPending:
            self.qbcom.IsPending = ET.SubElement(self.qbcom.CreditMemoAdd, 'IsPending')
            self.qbcom.IsPending.text = self.IsPending
        if self.PONumber:
            self.qbcom.PONumber = ET.SubElement(self.qbcom.CreditMemoAdd, 'PONumber')
            self.qbcom.PONumber.text = self.PONumber
        if self.TermsRef.ListID or self.TermsRef.FullName:
            self.qbcom.TermsRef = ET.SubElement(self.qbcom.CreditMemoAdd, 'TermsRef')
            if self.TermsRef.ListID:
                self.qbcom.TermsRef_ListID = ET.SubElement(self.qbcom.TermsRef, 'ListID')
                self.qbcom.TermsRef_ListID.text = self.TermsRef.ListID
            elif self.TermsRef.FullName:
                self.qbcom.TermsRef_FullName = ET.SubElement(self.qbcom.TermsRef, 'FullName')
                self.qbcom.TermsRef_FullName.text = self.TermsRef.FullName
        if self.DueDate:
            self.qbcom.DueDate = ET.SubElement(self.qbcom.CreditMemoAdd, 'DueDate')
            self.qbcom.DueDate.text = self.DueDate
        if self.SalesRepRef.ListID or self.SalesRepRef.FullName:
            self.qbcom.SalesRepRef = ET.SubElement(self.qbcom.CreditMemoAdd, 'SalesRepRef')
            if self.SalesRepRef.ListID:
                self.qbcom.SalesRepRef_ListID = ET.SubElement(self.qbcom.SalesRepRef, 'ListID')
                self.qbcom.SalesRepRef_ListID.text = self.SalesRepRef.ListID
            elif self.SalesRepRef.FullName:
                self.qbcom.SalesRepRef_FullName = ET.SubElement(self.qbcom.SalesRepRef, 'FullName')
                self.qbcom.SalesRepRef_FullName.text = self.SalesRepRef.FullName
        if self.FOB:
            self.qbcom.FOB = ET.SubElement(self.qbcom.CreditMemoAdd, 'FOB')
            self.qbcom.FOB.text = self.FOB
        if self.ShipDate:
            self.qbcom.ShipDate = ET.SubElement(self.qbcom.CreditMemoAdd, 'ShipDate')
            self.qbcom.ShipDate.text = self.ShipDate
        if self.ShipMethodRef.ListID or self.ShipMethodRef.FullName:
            self.qbcom.ShipMethodRef = ET.SubElement(self.qbcom.CreditMemoAdd, 'ShipMethodRef')
            if self.ShipMethodRef.ListID:
                self.qbcom.ShipMethodRef_ListID = ET.SubElement(self.qbcom.ShipMethodRef, 'ListID')
                self.qbcom.ShipMethodRef_ListID.text = self.ShipMethodRef.ListID
            elif self.ShipMethodRef.FullName:
                self.qbcom.ShipMethodRef_FullName = ET.SubElement(self.qbcom.ShipMethodRef, 'FullName')
                self.qbcom.ShipMethodRef_FullName.text = self.ShipMethodRef.FullName
        if self.ItemSalesTaxRef.ListID or self.ItemSalesTaxRef.FullName:
            self.qbcom.ItemSalesTaxRef = ET.SubElement(self.qbcom.CreditMemoAdd, 'ItemSalesTaxRef')
            if self.ItemSalesTaxRef.ListID:
                self.qbcom.ItemSalesTaxRef_ListID = ET.SubElement(self.qbcom.ItemSalesTaxRef, 'ListID')
                self.qbcom.ItemSalesTaxRef_ListID.text = self.ItemSalesTaxRef.ListID
            elif self.ItemSalesTaxRef.FullName:
                self.qbcom.ItemSalesTaxRef_FullName = ET.SubElement(self.qbcom.ItemSalesTaxRef, 'FullName')
                self.qbcom.ItemSalesTaxRef_FullName.text = self.ItemSalesTaxRef.FullName
        if self.Memo:
            self.qbcom.Memo = ET.SubElement(self.qbcom.CreditMemoAdd, 'Memo')
            self.qbcom.Memo.text = self.Memo
        if self.CustomerMsgRef.ListID or self.CustomerMsgRef.FullName:
            self.qbcom.CustomerMsgRef = ET.SubElement(self.qbcom.CreditMemoAdd, 'CustomerMsgRef')
            if self.CustomerMsgRef.ListID:
                self.qbcom.CustomerMsgRef_ListID = ET.SubElement(self.qbcom.CustomerMsgRef, 'ListID')
                self.qbcom.CustomerMsgRef_ListID.text = self.CustomerMsgRef.ListID
            elif self.CustomerMsgRef.FullName:
                self.qbcom.CustomerMsgRef_FullName = ET.SubElement(self.qbcom.CustomerMsgRef, 'FullName')
                self.qbcom.CustomerMsgRef_FullName.text = self.CustomerMsgRef.FullName
        if self.IsToBePrinted:
            self.qbcom.IsToBePrinted = ET.SubElement(self.qbcom.CreditIsToBePrintedAdd, 'IsToBePrinted')
            self.qbcom.IsToBePrinted.text = self.IsToBePrinted
        if self.IsToBeEmailed:
            self.qbcom.IsToBeEmailed = ET.SubElement(self.qbcom.CreditIsToBeEmailedAdd, 'IsToBeEmailed')
            self.qbcom.IsToBeEmailed.text = self.IsToBeEmailed
        if self.CustomerSalesTaxCodeRef.ListID or self.CustomerSalesTaxCodeRef.FullName:
            self.qbcom.CustomerSalesTaxCodeRef = ET.SubElement(self.qbcom.CreditMemoAdd, 'CustomerSalesTaxCodeRef')
            if self.CustomerSalesTaxCodeRef.ListID:
                self.qbcom.CustomerSalesTaxCodeRef_ListID = ET.SubElement(self.qbcom.CustomerSalesTaxCodeRef, 'ListID')
                self.qbcom.CustomerSalesTaxCodeRef_ListID.text = self.CustomerSalesTaxCodeRef.ListID
            elif self.CustomerSalesTaxCodeRef.FullName:
                self.qbcom.CustomerSalesTaxCodeRef_FullName = ET.SubElement(self.qbcom.CustomerSalesTaxCodeRef, 'FullName')
                self.qbcom.CustomerSalesTaxCodeRef_FullName.text = self.CustomerSalesTaxCodeRef.FullName
        if self.Other:
            self.qbcom.Other = ET.SubElement(self.qbcom.CreditOtherAdd, 'Other')
            self.qbcom.Other.text = self.Other
        if self.ExchangeRate:
            self.qbcom.ExchangeRate = ET.SubElement(self.qbcom.CreditExchangeRateAdd, 'ExchangeRate')
            self.qbcom.ExchangeRate.text = self.ExchangeRate
        if self.ExternalGUID:
            self.qbcom.ExternalGUID = ET.SubElement(self.qbcom.CreditExternalGUIDAdd, 'ExternalGUID')
            self.qbcom.ExternalGUID.text = self.ExternalGUID
        if self.CreditMemoLineAdd.ItemRef.ListID or self.CreditMemoLineAdd.ItemRef.FullName:
            self.qbcom.CreditMemoLineAdd = ET.SubElement(self.qbcom.CreditMemoAdd, 'CreditMemoLineAdd')
            if self.CreditMemoLineAdd.ItemRef.ListID or self.CreditMemoLineAdd.ItemRef.FullName:
                self.qbcom.CreditMemoLineAdd_ItemRef = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'ItemRef')
                if self.CreditMemoLineAdd.ItemRef.ListID:
                    self.qbcom.CreditMemoLineAdd_ItemRef_ListID = ET.SubElement(self.qbcom.CreditMemoLineAdd_ItemRef, 'ListID')
                    self.qbcom.CreditMemoLineAdd_ItemRef_ListID.text = self.CreditMemoLineAdd.ItemRef.ListID
                elif self.CreditMemoLineAdd.ItemRef.FullName:
                    self.qbcom.CreditMemoLineAdd_ItemRef_FullName = ET.SubElement(self.qbcom.CreditMemoLineAdd_ItemRef, 'FullName')
                    self.qbcom.CreditMemoLineAdd_ItemRef_FullName.text = self.CreditMemoLineAdd.ItemRef.FullName
            if self.CreditMemoLineAdd.Desc:
                self.qbcom.CreditMemoLineAdd_Desc = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'Desc')
                self.qbcom.CreditMemoLineAdd_Desc.text = self.CreditMemoLineAdd.Desc
            if self.CreditMemoLineAdd.Quantity:
                self.qbcom.CreditMemoLineAdd_Quantity = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'Quantity')
                self.qbcom.CreditMemoLineAdd_Quantity.text = self.CreditMemoLineAdd.Quantity
            if self.CreditMemoLineAdd.UnitOfMeasure:
                self.qbcom.CreditMemoLineAdd_UnitOfMeasure = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'UnitOfMeasure')
                self.qbcom.CreditMemoLineAdd_UnitOfMeasure.text = self.CreditMemoLineAdd.UnitOfMeasure
            if self.CreditMemoLineAdd.Rate:
                self.qbcom.CreditMemoLineAdd_Rate = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'Rate')
                self.qbcom.CreditMemoLineAdd_Rate.text = self.CreditMemoLineAdd.Rate
            elif self.CreditMemoLineAdd.RatePercent:
                self.qbcom.CreditMemoLineAdd_RatePercent = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'RatePercent')
                self.qbcom.CreditMemoLineAdd_RatePercent.text = self.CreditMemoLineAdd.RatePercent
            elif self.CreditMemoLineAdd.PriceLevelRef.ListID or self.CreditMemoLineAdd.PriceLevelRef.FullName:
                self.qbcom.CreditMemoLineAdd_PriceLevelRef = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'PriceLevelRef')
                if self.CreditMemoLineAdd.PriceLevelRef.ListID:
                    self.qbcom.CreditMemoLineAdd_PriceLevelRef_ListID = ET.SubElement(self.qbcom.CreditMemoLineAdd_PriceLevelRef, 'ListID')
                    self.qbcom.CreditMemoLineAdd_PriceLevelRef_ListID.text = self.CreditMemoLineAdd.PriceLevelRef.ListID
                elif self.CreditMemoLineAdd.PriceLevelRef.FullName:
                    self.qbcom.CreditMemoLineAdd_PriceLevelRef_FullName = ET.SubElement(self.qbcom.CreditMemoLineAdd_PriceLevelRef, 'FullName')
                    self.qbcom.CreditMemoLineAdd_PriceLevelRef_FullName.text = self.CreditMemoLineAdd.PriceLevelRef.FullName
            if self.CreditMemoLineAdd.ClassRef.ListID or self.CreditMemoLineAdd.ClassRef.FullName:
                self.qbcom.CreditMemoLineAdd_ClassRef = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'ClassRef')
                if self.CreditMemoLineAdd.ClassRef.ListID:
                    self.qbcom.CreditMemoLineAdd_ClassRef_ListID = ET.SubElement(self.qbcom.CreditMemoLineAdd_ClassRef, 'ListID')
                    self.qbcom.CreditMemoLineAdd_ClassRef_ListID.text = self.CreditMemoLineAdd.ClassRef.ListID
                elif self.CreditMemoLineAdd.ClassRef.FullName:
                    self.qbcom.CreditMemoLineAdd_ClassRef_FullName = ET.SubElement(self.qbcom.CreditMemoLineAdd_ClassRef, 'FullName')
                    self.qbcom.CreditMemoLineAdd_ClassRef_FullName.text = self.CreditMemoLineAdd.ClassRef.FullName
            if self.CreditMemoLineAdd.Amount:
                self.qbcom.CreditMemoLineAdd_Amount = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'Amount')
                self.qbcom.CreditMemoLineAdd_Amount.text = self.CreditMemoLineAdd.Amount
            if self.CreditMemoLineAdd.InventorySiteRef.ListID or self.CreditMemoLineAdd.InventorySiteRef.FullName:
                self.qbcom.CreditMemoLineAdd_InventorySiteRef = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'InventorySiteRef')
                if self.CreditMemoLineAdd.InventorySiteRef.ListID:
                    self.qbcom.CreditMemoLineAdd_InventorySiteRef_ListID = ET.SubElement(self.qbcom.CreditMemoLineAdd_InventorySiteRef, 'ListID')
                    self.qbcom.CreditMemoLineAdd_InventorySiteRef_ListID.text = self.CreditMemoLineAdd.InventorySiteRef.ListID
                elif self.CreditMemoLineAdd.InventorySiteRef.FullName:
                    self.qbcom.CreditMemoLineAdd_InventorySiteRef_FullName = ET.SubElement(self.qbcom.CreditMemoLineAdd_InventorySiteRef, 'FullName')
                    self.qbcom.CreditMemoLineAdd_InventorySiteRef_FullName.text = self.CreditMemoLineAdd.InventorySiteRef.FullName
            if self.CreditMemoLineAdd.InventorySiteLocationRef.ListID or self.CreditMemoLineAdd.InventorySiteLocationRef.FullName:
                self.qbcom.CreditMemoLineAdd_InventorySiteLocationRef = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'InventorySiteLocationRef')
                if self.CreditMemoLineAdd.InventorySiteLocationRef.ListID:
                    self.qbcom.CreditMemoLineAdd_InventorySiteLocationRef_ListID = ET.SubElement(self.qbcom.CreditMemoLineAdd_InventorySiteLocationRef, 'ListID')
                    self.qbcom.CreditMemoLineAdd_InventorySiteLocationRef_ListID.text = self.CreditMemoLineAdd.InventorySiteLocationRef.ListID
                elif self.CreditMemoLineAdd.InventorySiteLocationRef.FullName:
                    self.qbcom.CreditMemoLineAdd_InventorySiteLocationRef_FullName = ET.SubElement(self.qbcom.CreditMemoLineAdd_InventorySiteLocationRef, 'FullName')
                    self.qbcom.CreditMemoLineAdd_InventorySiteLocationRef_FullName.text = self.CreditMemoLineAdd.InventorySiteLocationRef.FullName
            if self.CreditMemoLineAdd.SerialNumber:
                self.qbcom.CreditMemoLineAdd_SerialNumber = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'SerialNumber')
                self.qbcom.CreditMemoLineAdd_SerialNumber.text = self.CreditMemoLineAdd.SerialNumber
            elif self.CreditMemoLineAdd.LotNumber:
                self.qbcom.CreditMemoLineAdd_LotNumber = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'LotNumber')
                self.qbcom.CreditMemoLineAdd_LotNumber.text = self.CreditMemoLineAdd.LotNumber
            if self.CreditMemoLineAdd.ServiceDate:
                self.qbcom.CreditMemoLineAdd_ServiceDate = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'ServiceDate')
                self.qbcom.CreditMemoLineAdd_ServiceDate.text = self.CreditMemoLineAdd.ServiceDate
            if self.CreditMemoLineAdd.SalesTaxCodeRef.ListID or self.CreditMemoLineAdd.SalesTaxCodeRef.FullName:
                self.qbcom.CreditMemoLineAdd_SalesTaxCodeRef = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'SalesTaxCodeRef')
                if self.CreditMemoLineAdd.SalesTaxCodeRef.ListID:
                    self.qbcom.CreditMemoLineAdd_SalesTaxCodeRef_ListID = ET.SubElement(self.qbcom.CreditMemoLineAdd_SalesTaxCodeRef, 'ListID')
                    self.qbcom.CreditMemoLineAdd_SalesTaxCodeRef_ListID.text = self.CreditMemoLineAdd.SalesTaxCodeRef.ListID
                elif self.CreditMemoLineAdd.SalesTaxCodeRef.FullName:
                    self.qbcom.CreditMemoLineAdd_SalesTaxCodeRef_FullName = ET.SubElement(self.qbcom.CreditMemoLineAdd_SalesTaxCodeRef, 'FullName')
                    self.qbcom.CreditMemoLineAdd_SalesTaxCodeRef_FullName.text = self.CreditMemoLineAdd.SalesTaxCodeRef.FullName
            if self.CreditMemoLineAdd.OverrideItemAccountRef.ListID or self.CreditMemoLineAdd.OverrideItemAccountRef.FullName:
                self.qbcom.CreditMemoLineAdd_OverrideItemAccountRef = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'OverrideItemAccountRef')
                if self.CreditMemoLineAdd.OverrideItemAccountRef.ListID:
                    self.qbcom.CreditMemoLineAdd_OverrideItemAccountRef_ListID = ET.SubElement(self.qbcom.CreditMemoLineAdd_OverrideItemAccountRef, 'ListID')
                    self.qbcom.CreditMemoLineAdd_OverrideItemAccountRef_ListID.text = self.CreditMemoLineAdd.OverrideItemAccountRef.ListID
                elif self.CreditMemoLineAdd.OverrideItemAccountRef.FullName:
                    self.qbcom.CreditMemoLineAdd_OverrideItemAccountRef_FullName = ET.SubElement(self.qbcom.CreditMemoLineAdd_OverrideItemAccountRef, 'FullName')
                    self.qbcom.CreditMemoLineAdd_OverrideItemAccountRef_FullName.text = self.CreditMemoLineAdd.OverrideItemAccountRef.FullName
            if self.CreditMemoLineAdd.Other1:
                self.qbcom.CreditMemoLineAdd_Other1 = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'Other1')
                self.qbcom.CreditMemoLineAdd_Other1.text = self.CreditMemoLineAdd.Other1
            if self.CreditMemoLineAdd.Other2:
                self.qbcom.CreditMemoLineAdd_Other2 = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'Other2')
                self.qbcom.CreditMemoLineAdd_Other2.text = self.CreditMemoLineAdd.Other2
            if (self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardNumber or
                self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultCode):
                self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'CreditCardTxnInfo')
                if (self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardNumber):
                    self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo = ET.SubElement(self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo, 'CreditCardTxnInputInfo')
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardNumber:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardNumber = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'CreditCardNumber')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardNumber.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardNumber
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationMonth:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_ExpirationMonth = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'ExpirationMonth')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_ExpirationMonth.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationMonth
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationYear:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_ExpirationYear = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'ExpirationYear')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_ExpirationYear.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationYear
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.NameOnCard:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_NameOnCard = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'NameOnCard')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_NameOnCard.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.NameOnCard
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardAddress:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardAddress = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'CreditCardAddress')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardAddress.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardAddress
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardPostalCode:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardPostalCode = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'CreditCardPostalCode')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardPostalCode.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardPostalCode
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CommercialCardCode:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CommercialCardCode = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'CommercialCardCode')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CommercialCardCode.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CommercialCardCode
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.TransactionMode:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_TransactionMode = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'TransactionMode')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_TransactionMode.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.TransactionMode
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CrediCardTxnType:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CrediCardTxnType = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'CrediCardTxnType')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CrediCardTxnType.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CrediCardTxnType
                if (self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultCode):
                    self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo = ET.SubElement(self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo, 'CreditCardTxnResultInfo')
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultCode:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_ResultCode = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'ResultCode')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_ResultCode.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultCode
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultMessage:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_ResultMessage = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'ResultMessage')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_ResultMessage.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultMessage
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.CreditCardTransID:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_CreditCardTransID = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'CreditCardTransID')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_CreditCardTransID.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.CreditCardTransID
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.MerchantAccountNumber:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_MerchantAccountNumber = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'MerchantAccountNumber')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_MerchantAccountNumber.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.MerchantAccountNumber
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AuthorizationCode:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_AuthorizationCode = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'AuthorizationCode')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_AuthorizationCode.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AuthorizationCode
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSStreet:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_AVSStreet = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'AVSStreet')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_AVSStreet.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSStreet
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSZip:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_AVSZip = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'AVSZip')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_AVSZip.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSZip
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.CardSecurityCodeMatch:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_CardSecurityCodeMatch = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'CardSecurityCodeMatch')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_CardSecurityCodeMatch.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.CardSecurityCodeMatch
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ReconBatchID:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_ReconBatchID = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'ReconBatchID')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_ReconBatchID.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ReconBatchID
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentGroupingCode:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_PaymentGroupingCode = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'PaymentGroupingCode')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_PaymentGroupingCode.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentGroupingCode
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentStatus:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_PaymentStatus = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'PaymentStatus')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_PaymentStatus.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentStatus
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationTime:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_TxnAuthorizationTime = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'TxnAuthorizationTime')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_TxnAuthorizationTime.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationTime
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationStamp:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_TxnAuthorizationStamp = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'TxnAuthorizationStamp')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_TxnAuthorizationStamp.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationStamp
                    if self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ClientTransID:
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_ClientTransID = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'ClientTransID')
                        self.qbcom.CreditMemoLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_ClientTransID.text = self.CreditMemoLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ClientTransID
            if (self.CreditMemoLineAdd.DataExt.OwnerID or
                    self.CreditMemoLineAdd.DataExt.DataExtName or
                    self.CreditMemoLineAdd.DataExt.DataExtValue):
                self.qbcom.CreditMemoLineAdd_DataExt = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'DataExt')
                if self.CreditMemoLineAdd.DataExt.OwnerID:
                    self.qbcom.CreditMemoLineAdd_DataExt_OwnerID = ET.SubElement(self.qbcom.CreditMemoLineAdd_DataExt, 'OwnerID')
                    self.qbcom.CreditMemoLineAdd_DataExt_OwnerID.text = self.CreditMemoLineAdd.DataExt.OwnerID
                if self.CreditMemoLineAdd.DataExt.DataExtName:
                    self.qbcom.CreditMemoLineAdd_DataExt_DataExtName = ET.SubElement(self.qbcom.CreditMemoLineAdd_DataExt, 'DataExtName')
                    self.qbcom.CreditMemoLineAdd_DataExt_DataExtName.text = self.CreditMemoLineAdd.DataExt.DataExtName
                if self.CreditMemoLineAdd.DataExt.DataExtValue:
                    self.qbcom.CreditMemoLineAdd_DataExt_DataExtValue = ET.SubElement(self.qbcom.CreditMemoLineAdd_DataExt, 'DataExtValue')
                    self.qbcom.CreditMemoLineAdd_DataExt_DataExtValue.text = self.CreditMemoLineAdd.DataExt.DataExtValue
        elif (self.CreditMemoLineAdd.ItemGroupRef.ListID or
                self.CreditMemoLineAdd.ItemGroupRef.FullName):
            self.qbcom.CreditMemoLineAdd = ET.SubElement(self.qbcom.CreditMemoAdd, 'CreditMemoLineAdd')
            if self.CreditMemoLineAdd.ItemGroupRef.ListID or self.CreditMemoLineAdd.ItemGroupRef.FullName:
                self.qbcom.CreditMemoLineAdd_ItemGroupRef = ET.SubElement(self.qbcom.CreditMemoLineAdd, 'ItemGroupRef')
                if self.CreditMemoLineAdd.ItemGroupRef.ListID:
                    self.qbcom.CreditMemoLineAdd_ItemGroupRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.CreditMemoLineAdd_ItemGroupRef_ListID.text = self.CreditMemoLineAdd.ItemGroupRef.ListID
                elif self.CreditMemoLineAdd.ItemGroupRef.FullName:
                    self.qbcom.CreditMemoLineAdd_ItemGroupRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.CreditMemoLineAdd_ItemGroupRef_FullName.text = self.CreditMemoLineAdd.ItemGroupRef.FullName
            if self.CreditMemoLineAdd.Quantity:
                self.qbcom.CreditMemoLineAdd_Quantity = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'Quantity')
                self.qbcom.CreditMemoLineAdd_Quantity.text = self.CreditMemoLineAdd.Quantity
            if self.CreditMemoLineAdd.UnitOfMeasure:
                self.qbcom.CreditMemoLineAdd_UnitOfMeasure = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'UnitOfMeasure')
                self.qbcom.CreditMemoLineAdd_UnitOfMeasure.text = self.CreditMemoLineAdd.UnitOfMeasure
            if self.CreditMemoLineAdd.InventorySiteRef.ListID or self.CreditMemoLineAdd.InventorySiteRef.FullName:
                self.qbcom.CreditMemoLineAdd_InventorySiteRef = ET.SubElement(self.qbcom.SalesReceiptAdd, 'InventorySiteRef')
                if self.CreditMemoLineAdd.InventorySiteRef.ListID:
                    self.qbcom.CreditMemoLineAdd_InventorySiteRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.CreditMemoLineAdd_InventorySiteRef_ListID.text = self.CreditMemoLineAdd.InventorySiteRef.ListID
                elif self.CreditMemoLineAdd.InventorySiteRef.FullName:
                    self.qbcom.CreditMemoLineAdd_InventorySiteRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.CreditMemoLineAdd_InventorySiteRef_FullName.text = self.CreditMemoLineAdd.InventorySiteRef.FullName
            if self.CreditMemoLineAdd.InventorySiteLocationRef.ListID or self.CreditMemoLineAdd.InventorySiteLocationRef.FullName:
                self.qbcom.CreditMemoLineAdd_InventorySiteLocationRef = ET.SubElement(self.qbcom.SalesReceiptAdd, 'InventorySiteLocationRef')
                if self.CreditMemoLineAdd.InventorySiteLocationRef.ListID:
                    self.qbcom.CreditMemoLineAdd_InventorySiteLocationRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.CreditMemoLineAdd_InventorySiteLocationRef_ListID.text = self.CreditMemoLineAdd.InventorySiteLocationRef.ListID
                elif self.CreditMemoLineAdd.InventorySiteLocationRef.FullName:
                    self.qbcom.CreditMemoLineAdd_InventorySiteLocationRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.CreditMemoLineAdd_InventorySiteLocationRef_FullName.text = self.CreditMemoLineAdd.InventorySiteLocationRef.FullName
            if self.CreditMemoLineAdd.DataExt.OwnerID or self.CreditMemoLineAdd.DataExt.DataExtName or self.CreditMemoLineAdd.DataExt.DataExtValue:
                self.qbcom.CreditMemoLineAdd_DataExt = ET.SubElement(self.qbcom.SalesReceiptAdd, 'DataExt')
                if self.CreditMemoLineAdd.DataExt.OwnerID:
                    self.qbcom.CreditMemoLineAdd_DataExt_OwnerID = ET.SubElement(self.qbcom.CreditMemoLineAdd_DataExt, 'OwnerID')
                    self.qbcom.CreditMemoLineAdd_DataExt_OwnerID.text = self.CreditMemoLineAdd.DataExt.OwnerID
                if self.CreditMemoLineAdd.DataExt.DataExtName:
                    self.qbcom.CreditMemoLineAdd_DataExt_DataExtName = ET.SubElement(self.qbcom.CreditMemoLineAdd_DataExt, 'DataExtName')
                    self.qbcom.CreditMemoLineAdd_DataExt_DataExtName.text = self.CreditMemoLineAdd.DataExt.DataExtName
                if self.CreditMemoLineAdd.DataExt.DataExtValue:
                    self.qbcom.CreditMemoLineAdd_DataExt_DataExtValue = ET.SubElement(self.qbcom.CreditMemoLineAdd_DataExt, 'DataExtValue')
                    self.qbcom.CreditMemoLineAdd_DataExt_DataExtValue.text = self.CreditMemoLineAdd.DataExt.DataExtValue
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.CreditMemoLineAddRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item

    def set_DepositAddRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.DepositAddRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, 'DepositAddRq')
        self.qbcom.DepositAdd = ET.SubElement(self.qbcom.DepositAddRq, 'DepositAdd')
        if self.TxnDate:
            self.qbcom.TxnDate = ET.SubElement(self.qbcom.DepositAdd, 'TxnDate')
            self.qbcom.TxnDate.text = self.TxnDate
        if self.DepositToAccountRef.ListID or self.DepositToAccountRef.FullName:
            self.qbcom.DepositToAccountRef = ET.SubElement(self.qbcom.DepositAdd, 'DepositToAccountRef')
            if self.DepositToAccountRef.ListID:
                self.qbcom.DepositToAccountRef_ListID = ET.SubElement(self.qbcom.DepositToAccountRef, 'ListID')
                self.qbcom.DepositToAccountRef_ListID.text = self.DepositToAccountRef.ListID
            elif self.DepositToAccountRef.FullName:
                self.qbcom.DepositToAccountRef_FullName = ET.SubElement(self.qbcom.DepositToAccountRef, 'FullName')
                self.qbcom.DepositToAccountRef_FullName.text = self.DepositToAccountRef.FullName
        if self.Memo:
            self.qbcom.Memo = ET.SubElement(self.qbcom.DepositAdd, 'Memo')
            self.qbcom.Memo.text = self.Memo
        if self.CashBackInfoAdd.AccountRef.ListID or self.CashBackInfoAdd.AccountRef.FullName:
            self.qbcom.CashBackInfoAdd = ET.SubElement(self.qbcom.DepositAdd, 'CashBackInfoAdd')
            self.qbcom.CashBackInfoAdd_AccountRef = ET.SubElement(self.qbcom.CashBackInfoAdd, 'AccountRef')
            if self.CashBackInfoAdd.AccountRef.ListID:
                self.qbcom.CashBackInfoAdd_AccountRef_ListID = ET.SubElement(self.qbcom.CashBackInfoAdd_AccountRef, 'ListID')
                self.qbcom.CashBackInfoAdd_AccountRef_ListID.text = self.CashBackInfoAdd.AccountRef.ListID
            elif self.CashBackInfoAdd.AccountRef.FullName:
                self.qbcom.CashBackInfoAdd_AccountRef_FullName = ET.SubElement((self.qbcom.CashBackInfoAdd_AccountRef, 'FullName'))
                self.qbcom.CashBackInfoAdd_AccountRef_FullName.text = self.CashBackInfoAdd.AccountRef.FullName
            if self.CashBackInfoAdd.AccountRef.Memo:
                self.qbcom.CashBackInfoAdd_AccountRef_Memo = ET.SubElement(self.qbcom.CashBackInfoAdd_AccountRef, 'Memo')
                self.qbcom.CashBackInfoAdd_AccountRef_Memo.text = self.CashBackInfoAdd.AccountRef.Memo
            self.qbcom.CashBackInfoAdd_AccountRef_Amount = ET.SubElement(self.qbcom.CashBackInfoAdd_AccountRef, 'Amount')
            self.qbcom.CashBackInfoAdd_AccountRef_Amount.text = self.CashBackInfoAdd.AccountRef.Amount
        if self.CurrencyRef.ListID or self.CurrencyRef.FullName:
            self.qbcom.CurrencyRef = ET.SubElement(self.qbcom.DepositAdd, 'CurrencyRef')
            self.qbcom.CurrencyRef_ListID = ET.SubElement(self.qbcom.CurrencyRef, 'ListID')
            self.qbcom.CurrencyRef_ListID.text = self.CurrencyRef.ListID
            self.qbcom.CurrencyRef_FullName = ET.SubElement(self.qbcom.CurrencyRef, 'FullName')
            self.qbcom.CurrencyRef_FullName.text = self.CurrencyRef.FullName
        if self.ExchangeRate:
            self.qbcom.ExchangeRate = ET.SubElement(self.qbcom.DepositAdd, 'ExchangeRate')
            self.qbcom.ExchangeRate.text = self.ExchangeRate
        if self.ExternalGUID:
            self.qbcom.ExternalGUID = ET.SubElement(self.qbcom.DepositAdd, 'ExternalGUID')
            self.qbcom.ExternalGUID.text = self.ExternalGUID
        if self.DepositLineAdd.PaymentTxnID or self.DepositLineAdd.PaymentTxnLineID or self.DepositLineAdd.Amount:
            self.qbcom.DepositLineAdd = ET.SubElement(self.qbcom.DepositAdd, 'DepositLineAdd')
            if self.DepositLineAdd.PaymentTxnID or self.DepositLineAdd.PaymentTxnLineID:
                if self.DepositLineAdd.PaymentTxnID:
                    self.qbcom.DepositLineAdd_PaymentTxnID = ET.SubElement(self.qbcom.DepositLineAdd, 'PaymentTxnID')
                    self.qbcom.DepositLineAdd_PaymentTxnID.text = self.DepositLineAdd.PaymentTxnID
                elif self.DepositLineAdd.PaymentTxnLineID:
                    self.qbcom.DepositLineAdd_PaymentTxnLineID = ET.SubElement(self.qbcom.DepositLineAdd, 'PaymentTxnLineID')
                    self.qbcom.DepositLineAdd_PaymentTxnLineID.text = self.DepositLineAdd.PaymentTxnLineID
                if self.DepositLineAdd.OverrideMemo:
                    self.qbcom.DepositLineAdd_OverrideMemo = ET.SubElement(self.qbcom.DepositLineAdd, 'OverrideMemo')
                    self.qbcom.DepositLineAdd_OverrideMemo.text = self.DepositLineAdd.OverrideMemo
                if self.DepositLineAdd.OverrideCheckNumber:
                    self.qbcom.DepositLineAdd_OverrideCheckNumber = ET.SubElement(self.qbcom.DepositLineAdd, 'OverrideCheckNumber')
                    self.qbcom.DepositLineAdd_OverrideCheckNumber.text = self.DepositLineAdd.OverrideCheckNumber
                if self.DepositLineAdd.OverrideClassRef.ListID or self.DepositLineAdd.OverrideClassRef.FullName:
                    self.qbcom.DepositLineAdd_OverrideClassRef = ET.SubElement(self.qbcom.DepositLineAdd, 'OverrideClassRef')
                    if self.DepositLineAdd.OverrideClassRef.ListID:
                        self.qbcom.DepositLineAdd_OverrideClassRef_ListID = ET.SubElement(self.qbcom.DepositLineAdd_OverrideClassRef, 'ListID')
                        self.qbcom.DepositLineAdd_OverrideClassRef_ListID.text = self.DepositLineAdd.OverrideClassRef.ListID
                    elif self.DepositLineAdd.OverrideClassRef.FullName:
                        self.qbcom.DepositLineAdd_OverrideClassRef_FullName = ET.SubElement(self.qbcom.DepositLineAdd_OverrideClassRef, 'FullName')
                        self.qbcom.DepositLineAdd_OverrideClassRef_FullName.text = self.DepositLineAdd.OverrideClassRef.FullName
            elif self.DepositLineAdd.Amount:
                if self.DepositLineAdd.EntityRef.ListID or self.DepositLineAdd.EntityRef.FullName:
                    self.qbcom.DeposiLineAdd_EntityRef = ET.SubElement(self.qbcom.DepositLineAdd, 'EntityRef')
                    if self.DepositLineAdd.EntityRef.ListID:
                        self.qbcom.DepositLineAdd_EntityRef_ListID = ET.SubElement(self.qbcom.DepositLineAdd_EntityRef, 'ListID')
                        self.qbcom.DepositLineAdd_EntityRef_ListID.text = self.DepositLineAdd.EntityRef.ListID
                    elif self.DepositLineAdd.EntityRef.FullName:
                        self.qbcom.DepositLineAdd_EntityRef_FullName = ET.SubElement(self.qbcom.DepositLineAdd_EntityRef, 'FullName')
                        self.qbcom.DepositLineAdd_EntityRef_FullName.text = self.DepositLineAdd.EntityRef.FullName
                if self.DepositLineAdd.AccountRef.ListID or self.DepositLineAdd.AccountRef.FullName:
                    self.qbcom.DepositLineAdd_AccountRef = ET.SubElement(self.qbcom.DepositLineAdd, 'AccountRef')
                    if self.DepositLineAdd.AccountRef.ListID:
                        self.qbcom.DepositLineAdd_AccountRef_ListID = ET.SubElement(self.qbcom.DepositLineAdd_AccountRef, 'ListID')
                        self.qbcom.DepositLineAdd_AccountRef_ListID.text = self.DepositLineAdd.AccountRef.ListID
                    elif self.DepositLineAdd.AccountRef.FullName:
                        self.qbcom.DepositLineAdd_AccountRef_FullName = ET.SubElement(self.qbcom.DepositLineAdd_AccountRef, 'FullName')
                        self.qbcom.DepositLineAdd_AccountRef_FullName.text = self.DepositLineAdd.AccountRef.FullName
                if self.DepositLineAdd.Memo:
                    self.qbcom.DepositLineAdd_Memo = ET.SubElement(self.qbcom.DepositLineAdd, 'Memo')
                    self.qbcom.DepositLineAdd_Memo.text = self.DepositLineAdd.Memo
                if self.DepositLineAdd.CheckNumber:
                    self.qbcom.DepositLineAdd_CheckNumber = ET.SubElement(self.qbcom.DepositLineAdd, 'CheckNumber')
                    self.qbcom.DepositLineAdd_CheckNumber.text = self.DepositLineAdd.CheckNumber
                if self.DepositLineAdd.PaymentMethodRef.ListID or self.DepositLineAdd.PaymentMethodRef.FullName:
                    self.qbcom.DeposiLineAdd_PaymentMethodRef = ET.SubElement(self.qbcom.DepositLineAdd, 'PaymentMethodRef')
                    if self.DepositLineAdd.PaymentMethodRef.ListID:
                        self.qbcom.DepositLineAdd_PaymentMethodRef_ListID = ET.SubElement(self.qbcom.DepositLineAdd_PaymentMethodRef, 'ListID')
                        self.qbcom.DepositLineAdd_PaymentMethodRef_ListID.text = self.DepositLineAdd.PaymentMethodRef.ListID
                    elif self.DepositLineAdd.PaymentMethodRef.FullName:
                        self.qbcom.DepositLineAdd_PaymentMethodRef_FullName = ET.SubElement(self.qbcom.DepositLineAdd_PaymentMethodRef, 'FullName')
                        self.qbcom.DepositLineAdd_PaymentMethodRef_FullName.text = self.DepositLineAdd.PaymentMethodRef.FullName
                if self.DepositLineAdd.ClassRef.ListID or self.DepositLineAdd.ClassRef.FullName:
                    self.qbcom.DeposiLineAdd_ClassRef = ET.SubElement(self.qbcom.DepositLineAdd, 'ClassRef')
                    if self.DepositLineAdd.ClassRef.ListID:
                        self.qbcom.DepositLineAdd_ClassRef_ListID = ET.SubElement(self.qbcom.DepositLineAdd_ClassRef, 'ListID')
                        self.qbcom.DepositLineAdd_ClassRef_ListID.text = self.DepositLineAdd.ClassRef.ListID
                    elif self.DepositLineAdd.ClassRef.FullName:
                        self.qbcom.DepositLineAdd_ClassRef_FullName = ET.SubElement(self.qbcom.DepositLineAdd_ClassRef, 'FullName')
                        self.qbcom.DepositLineAdd_ClassRef_FullName.text = self.DepositLineAdd.ClassRef.FullName
                if self.DepositLineAdd.Amount:
                    self.qbcom.DepositLineAdd_Amount = ET.SubElement(self.qbcom.DepositLineAdd, 'Amount')
                    self.qbcom.DepositLineAdd_Amount.text = self.DepositLineAdd.Amount
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.DepositAddRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item

    def set_SalesReceiptAddRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        self.qbcom.QBXMLMsgsRq.set('onError', self.onError)
        self.qbcom.SalesReceiptAddRq = ET.SubElement(self.qbcom.QBXMLMsgsRq, 'SalesReceiptAddRq')
        self.qbcom.SalesReceiptAdd = ET.SubElement(self.qbcom.SalesReceiptAddRq, 'SalesReceiptAdd')
        if self.CustomerRef.ListID or self.CustomerRef.FullName:
            self.qbcom.CustomerRef = ET.SubElement(self.qbcom.SalesReceiptAdd, 'CustomerRef')
            if self.CustomerRef.ListID:
                self.qbcom.CustomerRef_ListID = ET.SubElement(self.qbcom.CustomerRef, 'ListID')
                self.qbcom.CustomerRef_ListID.text = self.CustomerRef.ListID
            elif self.CustomerRef.FullName:
                self.qbcom.CustomerRef_FullName = ET.SubElement(self.qbcom.CustomerRef, 'FullName')
                self.qbcom.CustomerRef_FullName.text = self.CustomerRef.FullName
        if self.ClassRef.ListID or self.ClassRef.FullName:
            self.qbcom.ClassRef = ET.SubElement(self.qbcom.SalesReceiptAdd, 'ClassRef')
            if self.ClassRef.ListID:
                self.qbcom.ClassRef_ListID = ET.SubElement(self.qbcom.ClassRef, 'ListID')
                self.qbcom.ClassRef_ListID.text = self.ClassRef.ListID
            elif self.ClassRef.FullName:
                self.qbcom.ClassRef_FullName = ET.SubElement(self.qbcom.ClassRef, 'FullName')
                self.qbcom.ClassRef_FullName.text = self.ClassRef.FullName
        if self.TemplateRef.ListID or self.TemplateRef.FullName:
            self.qbcom.TemplateRef = ET.SubElement(self.qbcom.SalesReceiptAdd, 'TemplateRef')
            if self.TemplateRef.ListID:
                self.qbcom.TemplateRef_ListID = ET.SubElement(self.qbcom.TemplateRef, 'ListID')
                self.qbcom.TemplateRef_ListID.text = self.TemplateRef.ListID
            elif self.TemplateRef.FullName:
                self.qbcom.TemplateRef_FullName = ET.SubElement(self.qbcom.TemplateRef, 'FullName')
                self.qbcom.TemplateRef_FullName.text = self.TemplateRef.FullName
        if self.TxnDate:
            self.qbcom.TxnDate = ET.SubElement(self.qbcom.SalesReceiptAdd, 'TxnDate')
            self.qbcom.TxnDate.text = self.TxnDate
        if self.RefNumber:
            self.qbcom.RefNumber = ET.SubElement(self.qbcom.SalesReceiptAdd, 'RefNumber')
            self.qbcom.RefNumber.text = self.RefNumber
        if (    self.BillAddress.Addr1 and
                self.BillAddress.Addr2 and
                self.BillAddress.Addr3 and
                self.BillAddress.City and
                self.BillAddress.State and
                self.BillAddress.PostalCode and
                self.BillAddress.Country and
                not self.BillAddress.Addr4 and
                not self.BillAddress.Addr5):
            self.qbcom.BillAddress = ET.SubElement(self.qbcom.SalesReceiptAdd, 'BillAddress')
            self.qbcom.BillAddress_Addr1 = ET.SubElement(self.qbcom.BillAddress, 'Addr1')
            self.qbcom.BillAddress_Addr1.text = self.BillAddress.Addr1
            self.qbcom.BillAddress_Addr2 = ET.SubElement(self.qbcom.BillAddress, 'Addr2')
            self.qbcom.BillAddress_Addr2.text = self.BillAddress.Addr2
            self.qbcom.BillAddress_Addr3 = ET.SubElement(self.qbcom.BillAddress, 'Addr3')
            self.qbcom.BillAddress_Addr3.text = self.BillAddress.Addr3
            self.qbcom.BillAddress_City = ET.SubElement(self.qbcom.BillAddress, 'City')
            self.qbcom.BillAddress_City.text = self.BillAddress.City
            self.qbcom.BillAddress_State = ET.SubElement(self.qbcom.BillAddress, 'State')
            self.qbcom.BillAddress_State.text = self.BillAddress.State
            self.qbcom.BillAddress_PostalCode = ET.SubElement(self.qbcom.BillAddress, 'PostalCode')
            self.qbcom.BillAddress_PostalCode.text = self.BillAddress.PostalCode
            if self.BillAddress.Country:
                self.qbcom.BillAddress_Country = ET.SubElement(self.qbcom.BillAddress, 'Country')
                self.qbcom.BillAddress_Country.text = self.BillAddress.Country
            if self.BillAddress.Note:
                self.qbcom.BillAddress_Note = ET.SubElement(self.qbcom.BillAddress, 'Note')
                self.qbcom.BillAddress_Note.text = self.BillAddress.Note
        if (    self.BillAddress.Addr1 and
                self.BillAddress.Addr2 and
                self.BillAddress.Addr3 and
                self.BillAddress.Addr4 and
                self.BillAddress.Addr5 and
                not self.BillAddress.City and
                not self.BillAddress.State and
                not self.BillAddress.PostalCode and
                not self.BillAddress.Country):
            self.qbcom.BillAddress_ = ET.SubElement(self.qbcom.SalesReceiptAdd, 'BillAddress')
            self.qbcom.BillAddress_Addr1 = ET.SubElement(self.qbcom.BillAddress, 'Addr1')
            self.qbcom.BillAddress_Addr1.text = self.BillAddress.Addr1
            self.qbcom.BillAddress_Addr2 = ET.SubElement(self.qbcom.BillAddress, 'Addr2')
            self.qbcom.BillAddress_Addr2.text = self.BillAddress.Addr2
            self.qbcom.BillAddress_Addr3 = ET.SubElement(self.qbcom.BillAddress, 'Addr3')
            self.qbcom.BillAddress_Addr3.text = self.BillAddress.Addr3
            self.qbcom.BillAddress_Addr4 = ET.SubElement(self.qbcom.BillAddress, 'Addr4')
            self.qbcom.BillAddress_Addr4.text = self.BillAddress.Addr4
            self.qbcom.BillAddress_Addr5 = ET.SubElement(self.qbcom.BillAddress, 'Addr5')
            self.qbcom.BillAddress_Addr5.text = self.BillAddress.Addr5
            if self.BillAddress.Note:
                self.qbcom.BillAddress_Note = ET.SubElement(self.qbcom.BillAddress, 'Note')
                self.qbcom.BillAddress_Note.text = self.BillAddress.Note
        if (    self.ShipAddress.Addr1 and
                self.ShipAddress.Addr2 and
                self.ShipAddress.Addr3 and
                self.ShipAddress.City and
                self.ShipAddress.State and
                self.ShipAddress.PostalCode and
                not self.ShipAddress.Addr4 and
                not self.ShipAddress.Addr5):
            self.qbcom.ShipAddress = ET.SubElement(self.qbcom.SalesReceiptAdd, 'ShipAddress')
            self.qbcom.ShipAddress_Addr1 = ET.SubElement(self.qbcom.ShipAddress, 'Addr1')
            self.qbcom.ShipAddress_Addr1.text = self.ShipAddress.Addr1
            self.qbcom.ShipAddress_Addr2 = ET.SubElement(self.qbcom.ShipAddress, 'Addr2')
            self.qbcom.ShipAddress_Addr2.text = self.ShipAddress.Addr2
            self.qbcom.ShipAddress_Addr3 = ET.SubElement(self.qbcom.ShipAddress, 'Addr3')
            self.qbcom.ShipAddress_Addr3.text = self.ShipAddress.Addr3
            self.qbcom.ShipAddress_City = ET.SubElement(self.qbcom.ShipAddress, 'City')
            self.qbcom.ShipAddress_City.text = self.ShipAddress.City
            self.qbcom.ShipAddress_State = ET.SubElement(self.qbcom.ShipAddress, 'State')
            self.qbcom.ShipAddress_State.text = self.ShipAddress.State
            self.qbcom.ShipAddress_PostalCode = ET.SubElement(self.qbcom.ShipAddress, 'PostalCode')
            self.qbcom.ShipAddress_PostalCode.text = self.ShipAddress.PostalCode
            if self.ShipAddress.Country:
                self.qbcom.ShipAddress_Country = ET.SubElement(self.qbcom.ShipAddress, 'Country')
                self.qbcom.ShipAddress_Country.text = self.ShipAddress.Country
            if self.ShipAddress.Note:
                self.qbcom.ShipAddress_Note = ET.SubElement(self.qbcom.ShipAddress, 'Note')
                self.qbcom.ShipAddress_Note.text = self.ShipAddress.Note
        if (    self.ShipAddress.Addr1 and
                self.ShipAddress.Addr2 and
                self.ShipAddress.Addr3 and
                self.ShipAddress.Addr4 and
                self.ShipAddress.Addr5 and
                not self.ShipAddress.City and
                not self.ShipAddress.State and
                not self.ShipAddress.PostalCode and
                not self.ShipAddress.Country):
            self.qbcom.ShipAddress = ET.SubElement(self.qbcom.SalesReceiptAdd, 'ShipAddress')
            self.qbcom.ShipAddress_Addr1 = ET.SubElement(self.qbcom.ShipAddress, 'Addr1')
            self.qbcom.ShipAddress_Addr1.text = self.ShipAddress.Addr1
            self.qbcom.ShipAddress_Addr2 = ET.SubElement(self.qbcom.ShipAddress, 'Addr2')
            self.qbcom.ShipAddress_Addr2.text = self.ShipAddress.Addr2
            self.qbcom.ShipAddress_Addr3 = ET.SubElement(self.qbcom.ShipAddress, 'Addr3')
            self.qbcom.ShipAddress_Addr3.text = self.ShipAddress.Addr3
            self.qbcom.ShipAddress_Addr4 = ET.SubElement(self.qbcom.ShipAddress, 'Addr4')
            self.qbcom.ShipAddress_Addr4.text = self.ShipAddress.Addr4
            self.qbcom.ShipAddress_Addr5 = ET.SubElement(self.qbcom.ShipAddress, 'Addr5')
            self.qbcom.ShipAddress_Addr5.text = self.ShipAddress.Addr5
            if self.ShipAddress.Note:
                self.qbcom.ShipAddress_Note = ET.SubElement(self.qbcom.ShipAddress, 'Note')
                self.qbcom.ShipAddress_Note.text = self.ShipAddress.Note
        if self.IsPending:
            self.qbcom.IsPending = ET.SubElement(self.qbcom.SalesReceiptAdd, 'IsPending')
            self.qbcom.IsPending.text = self.IsPending
        if self.CheckNumber:
            self.qbcom.CheckNumber = ET.SubElement(self.qbcom.SalesReceiptAdd, 'CheckNumber')
            self.qbcom.CheckNumber.text = self.CheckNumber
        if self.PaymentMethodRef.ListID or self.PaymentMethodRef.FullName:
            self.qbcom.PaymentMethodRef = ET.SubElement(self.qbcom.SalesReceiptAdd, 'PaymentMethodRef')
            if self.PaymentMethodRef.ListID:
                self.qbcom.PaymentMethodRef_ListID = ET.SubElement(self.qbcom.PaymentMethodRef, 'ListID')
                self.qbcom.PaymentMethodRef_ListID.text = self.PaymentMethodRef.ListID
            elif self.PaymentMethodRef.FullName:
                self.qbcom.PaymentMethodRef_FullName = ET.SubElement(self.qbcom.PaymentMethodRef, 'FullName')
                self.qbcom.PaymentMethodRef_FullName.text = self.PaymentMethodRef.FullName
        if self.PaymentMethodRef.ListID or self.PaymentMethodRef.FullName:
            self.qbcom.PaymentMethodRef = ET.SubElement(self.qbcom.SalesReceiptAdd, 'PaymentMethodRef')
            if self.PaymentMethodRef.ListID:
                self.qbcom.PaymentMethodRef_ListID = ET.SubElement(self.qbcom.PaymentMethodRef, 'ListID')
                self.qbcom.PaymentMethodRef_ListID.text = self.PaymentMethodRef.ListID
            elif self.PaymentMethodRef.FullName:
                self.qbcom.PaymentMethodRef_FullName = ET.SubElement(self.qbcom.PaymentMethodRef, 'FullName')
                self.qbcom.PaymentMethodRef_FullName.text = self.PaymentMethodRef.FullName
        if self.DueDate:
            self.qbcom.DueDate = ET.SubElement(self.qbcom.SalesReceiptAdd, 'DueDate')
            self.qbcom.DueDate.text = self.DueDate
        if self.SalesRepRef.ListID or self.SalesRepRef.FullName:
            self.qbcom.SalesRepRef = ET.SubElement(self.qbcom.SalesReceiptAdd, 'SalesRepRef')
            if self.SalesRepRef.ListID:
                self.qbcom.SalesRepRef_ListID = ET.SubElement(self.qbcom.SalesRepRef, 'ListID')
                self.qbcom.SalesRepRef_ListID.text = self.SalesRepRef.ListID
            elif self.SalesRepRef.FullName:
                self.qbcom.SalesRepRef_FullName = ET.SubElement(self.qbcom.SalesRepRef, 'FullName')
                self.qbcom.SalesRepRef_FullName.text = self.SalesRepRef.FullName
        if self.ShipDate:
            self.qbcom.ShipDate = ET.SubElement(self.qbcom.SalesReceiptAdd, 'ShipDate')
            self.qbcom.ShipDate.text = self.ShipDate
        if self.ShipMethodRef.ListID or self.ShipMethodRef.FullName:
            self.qbcom.ShipMethodRef = ET.SubElement(self.qbcom.SalesReceiptAdd, 'ShipMethodRef')
            if self.ShipMethodRef.ListID:
                self.qbcom.ShipMethodRef_ListID = ET.SubElement(self.qbcom.ShipMethodRef, 'ListID')
                self.qbcom.ShipMethodRef_ListID.text = self.ShipMethodRef.ListID
            elif self.ShipMethodRef.FullName:
                self.qbcom.ShipMethodRef_FullName = ET.SubElement(self.qbcom.ShipMethodRef, 'FullName')
                self.qbcom.ShipMethodRef_FullName.text = self.ShipMethodRef.FullName
        if self.FOB:
            self.qbcom.FOB = ET.SubElement(self.qbcom.SalesReceiptAdd, 'FOB')
            self.qbcom.FOB.text = self.FOB
        if self.ItemSalesTaxRef.ListID or self.ItemSalesTaxRef.FullName:
            self.qbcom.ItemSalesTaxRef = ET.SubElement(self.qbcom.SalesReceiptAdd, 'ItemSalesTaxRef')
            if self.ItemSalesTaxRef.ListID:
                self.qbcom.ItemSalesTaxRef_ListID = ET.SubElement(self.qbcom.ItemSalesTaxRef, 'ListID')
                self.qbcom.ItemSalesTaxRef_ListID.text = self.ItemSalesTaxRef.ListID
            elif self.ItemSalesTaxRef.FullName:
                self.qbcom.ItemSalesTaxRef_FullName = ET.SubElement(self.qbcom.ItemSalesTaxRef, 'FullName')
                self.qbcom.ItemSalesTaxRef_FullName.text = self.ItemSalesTaxRef.FullName
        if self.Memo:
            self.qbcom.Memo = ET.SubElement(self.qbcom.SalesReceiptAdd, 'Memo')
            self.qbcom.Memo.text = self.Memo
        if self.CustomerMsgRef.ListID or self.CustomerMsgRef.FullName:
            self.qbcom.CustomerMsgRef = ET.SubElement(self.qbcom.SalesReceiptAdd, 'CustomerMsgRef')
            if self.CustomerMsgRef.ListID:
                self.qbcom.CustomerMsgRef_ListID = ET.SubElement(self.qbcom.CustomerMsgRef, 'ListID')
                self.qbcom.CustomerMsgRef_ListID.text = self.CustomerMsgRef.ListID
            elif self.CustomerMsgRef.FullName:
                self.qbcom.CustomerMsgRef_FullName = ET.SubElement(self.qbcom.CustomerMsgRef, 'FullName')
                self.qbcom.CustomerMsgRef_FullName.text = self.CustomerMsgRef.FullName
        if self.IsToBePrinted:
            self.qbcom.IsToBePrinted = ET.SubElement(self.qbcom.SalesReceiptAdd, 'IsToBePrinted')
            self.qbcom.IsToBePrinted.text = self.IsToBePrinted
        if self.IsToBeEmailed:
            self.qbcom.IsToBeEmailed = ET.SubElement(self.qbcom.SalesReceiptAdd, 'IsToBeEmailed')
            self.qbcom.IsToBeEmailed.text = self.IsToBeEmailed
        if self.CustomerSalesTaxCodeRef.ListID or self.CustomerSalesTaxCodeRef.FullName:
            self.qbcom.CustomerSalesTaxCodeRef = ET.SubElement(self.qbcom.SalesReceiptAdd, 'CustomerSalesTaxCodeRef')
            if self.CustomerSalesTaxCodeRef.ListID:
                self.qbcom.CustomerSalesTaxCodeRef_ListID = ET.SubElement(self.qbcom.CustomerSalesTaxCodeRef, 'ListID')
                self.qbcom.CustomerSalesTaxCodeRef_ListID.text = self.CustomerSalesTaxCodeRef.ListID
            elif self.CustomerSalesTaxCodeRef.FullName:
                self.qbcom.CustomerSalesTaxCodeRef_FullName = ET.SubElement(self.qbcom.CustomerSalesTaxCodeRef, 'FullName')
                self.qbcom.CustomerSalesTaxCodeRef_FullName.text = self.CustomerSalesTaxCodeRef.FullName
        if self.DepositToAccountRef.ListID or self.DepositToAccountRef.FullName:
            self.qbcom.DepositToAccountRef = ET.SubElement(self.qbcom.SalesReceiptAdd, 'DepositToAccountRef')
            if self.DepositToAccountRef.ListID:
                self.qbcom.DepositToAccountRef_ListID = ET.SubElement(self.qbcom.DepositToAccountRef, 'ListID')
                self.qbcom.DepositToAccountRef_ListID.text = self.DepositToAccountRef.ListID
            elif self.DepositToAccountRef.FullName:
                self.qbcom.DepositToAccountRef_FullName = ET.SubElement(self.qbcom.DepositToAccountRef, 'FullName')
                self.qbcom.DepositToAccountRef_FullName.text = self.DepositToAccountRef.FullName
        if (self.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardNumber or
            self.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultCode):
            self.qbcom.CreditCardTxnInfo = ET.SubElement(self.qbcom.SalesReceiptAdd, 'CreditCardTxnInfo')
            if (self.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardNumber):
                self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo = ET.SubElement(self.qbcom.CreditCardTxnInfo, 'CreditCardTxnInputInfo')
                if self.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardNumber:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardNumber = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'CreditCardNumber')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardNumber.text = self.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardNumber
                if self.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationMonth:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_ExpirationMonth = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'ExpirationMonth')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_ExpirationMonth.text = self.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationMonth
                if self.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationYear:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_ExpirationYear = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'ExpirationYear')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_ExpirationYear.text = self.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationYear
                if self.CreditCardTxnInfo.CreditCardTxnInputInfo.NameOnCard:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_NameOnCard = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'NameOnCard')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_NameOnCard.text = self.CreditCardTxnInfo.CreditCardTxnInputInfo.NameOnCard
                if self.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardAddress:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardAddress = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'CreditCardAddress')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardAddress.text = self.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardAddress
                if self.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardPostalCode:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardPostalCode = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'CreditCardPostalCode')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardPostalCode.text = self.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardPostalCode
                if self.CreditCardTxnInfo.CreditCardTxnInputInfo.CommercialCardCode:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_CommercialCardCode = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'CommercialCardCode')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_CommercialCardCode.text = self.CreditCardTxnInfo.CreditCardTxnInputInfo.CommercialCardCode
                if self.CreditCardTxnInfo.CreditCardTxnInputInfo.TransactionMode:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_TransactionMode = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'TransactionMode')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_TransactionMode.text = self.CreditCardTxnInfo.CreditCardTxnInputInfo.TransactionMode
                if self.CreditCardTxnInfo.CreditCardTxnInputInfo.CrediCardTxnType:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_CrediCardTxnType = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'CrediCardTxnType')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnInputInfo_CrediCardTxnType.text = self.CreditCardTxnInfo.CreditCardTxnInputInfo.CrediCardTxnType
            if (self.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultCode):
                self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo = ET.SubElement(self.qbcom.CreditCardTxnInfo, 'CreditCardTxnResultInfo')
                if self.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultCode:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_ResultCode = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'ResultCode')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_ResultCode.text = self.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultCode
                if self.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultMessage:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_ResultMessage = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'ResultMessage')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_ResultMessage.text = self.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultMessage
                if self.CreditCardTxnInfo.CreditCardTxnResultInfo.CreditCardTransID:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_CreditCardTransID = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'CreditCardTransID')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_CreditCardTransID.text = self.CreditCardTxnInfo.CreditCardTxnResultInfo.CreditCardTransID
                if self.CreditCardTxnInfo.CreditCardTxnResultInfo.MerchantAccountNumber:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_MerchantAccountNumber = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'MerchantAccountNumber')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_MerchantAccountNumber.text = self.CreditCardTxnInfo.CreditCardTxnResultInfo.MerchantAccountNumber
                if self.CreditCardTxnInfo.CreditCardTxnResultInfo.AuthorizationCode:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_AuthorizationCode = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'AuthorizationCode')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_AuthorizationCode.text = self.CreditCardTxnInfo.CreditCardTxnResultInfo.AuthorizationCode
                if self.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSStreet:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_AVSStreet = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'AVSStreet')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_AVSStreet.text = self.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSStreet
                if self.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSZip:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_AVSZip = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'AVSZip')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_AVSZip.text = self.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSZip
                if self.CreditCardTxnInfo.CreditCardTxnResultInfo.CardSecurityCodeMatch:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_CardSecurityCodeMatch = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'CardSecurityCodeMatch')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_CardSecurityCodeMatch.text = self.CreditCardTxnInfo.CreditCardTxnResultInfo.CardSecurityCodeMatch
                if self.CreditCardTxnInfo.CreditCardTxnResultInfo.ReconBatchID:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_ReconBatchID = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'ReconBatchID')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_ReconBatchID.text = self.CreditCardTxnInfo.CreditCardTxnResultInfo.ReconBatchID
                if self.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentGroupingCode:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_PaymentGroupingCode = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'PaymentGroupingCode')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_PaymentGroupingCode.text = self.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentGroupingCode
                if self.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentStatus:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_PaymentStatus = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'PaymentStatus')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_PaymentStatus.text = self.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentStatus
                if self.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationTime:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_TxnAuthorizationTime = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'TxnAuthorizationTime')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_TxnAuthorizationTime.text = self.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationTime
                if self.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationStamp:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_TxnAuthorizationStamp = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'TxnAuthorizationStamp')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_TxnAuthorizationStamp.text = self.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationStamp
                if self.CreditCardTxnInfo.CreditCardTxnResultInfo.ClientTransID:
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_ClientTransID = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'ClientTransID')
                    self.qbcom.CreditCardTxnInfo_CreditCardTxnResultInfo_ClientTransID.text = self.CreditCardTxnInfo.CreditCardTxnResultInfo.ClientTransID
        if (self.Other):
            self.qbcom.Other = ET.SubElement(self.qbcom.SalesReceiptAdd, 'Other')
            self.qbcom.Other.text = self.Other
        if (self.ExchangeRate):
            self.qbcom.ExchangeRate = ET.SubElement(self.qbcom.SalesReceiptAdd, 'ExchangeRate')
            self.qbcom.ExchangeRate.text = self.ExchangeRate
        if (self.ExternalGUID):
            self.qbcom.ExternalGUID = ET.SubElement(self.qbcom.SalesReceiptAdd, 'ExternalGUID')
            self.qbcom.ExternalGUID.text = self.ExternalGUID
        if self.SalesReceiptLineAdd.ItemRef.ListID or self.SalesReceiptLineAdd.ItemRef.FullName:
            self.qbcom.SalesReceiptLineAdd = ET.SubElement(self.qbcom.SalesReceiptAdd, 'SalesReceiptLineAdd')
            if self.SalesReceiptLineAdd.ItemRef.ListID or self.SalesReceiptLineAdd.ItemRef.FullName:
                self.qbcom.SalesReceiptLineAdd_ItemRef = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'ItemRef')
                if self.SalesReceiptLineAdd.ItemRef.ListID:
                    self.qbcom.SalesReceiptLineAdd_ItemRef_ListID = ET.SubElement(self.qbcom.SalesReceiptLineAdd_ItemRef, 'ListID')
                    self.qbcom.SalesReceiptLineAdd_ItemRef_ListID.text = self.SalesReceiptLineAdd.ItemRef.ListID
                elif self.SalesReceiptLineAdd.ItemRef.FullName:
                    self.qbcom.SalesReceiptLineAdd_ItemRef_FullName = ET.SubElement(self.qbcom.SalesReceiptLineAdd_ItemRef, 'FullName')
                    self.qbcom.SalesReceiptLineAdd_ItemRef_FullName.text = self.SalesReceiptLineAdd.ItemRef.FullName
            if self.SalesReceiptLineAdd.Desc:
                self.qbcom.SalesReceiptLineAdd_Desc = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'Desc')
                self.qbcom.SalesReceiptLineAdd_Desc.text = self.SalesReceiptLineAdd.Desc
            if self.SalesReceiptLineAdd.Quantity:
                self.qbcom.SalesReceiptLineAdd_Quantity = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'Quantity')
                self.qbcom.SalesReceiptLineAdd_Quantity.text = self.SalesReceiptLineAdd.Quantity
            if self.SalesReceiptLineAdd.UnitOfMeasure:
                self.qbcom.SalesReceiptLineAdd_UnitOfMeasure = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'UnitOfMeasure')
                self.qbcom.SalesReceiptLineAdd_UnitOfMeasure.text = self.SalesReceiptLineAdd.UnitOfMeasure
            if self.SalesReceiptLineAdd.Rate:
                self.qbcom.SalesReceiptLineAdd_Rate = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'Rate')
                self.qbcom.SalesReceiptLineAdd_Rate.text = self.SalesReceiptLineAdd.Rate
            elif self.SalesReceiptLineAdd.RatePercent:
                self.qbcom.SalesReceiptLineAdd_RatePercent = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'RatePercent')
                self.qbcom.SalesReceiptLineAdd_RatePercent.text = self.SalesReceiptLineAdd.RatePercent
            elif self.SalesReceiptLineAdd.PriceLevelRef.ListID or self.SalesReceiptLineAdd.PriceLevelRef.FullName:
                self.qbcom.SalesReceiptLineAdd_PriceLevelRef = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'PriceLevelRef')
                if self.SalesReceiptLineAdd.PriceLevelRef.ListID:
                    self.qbcom.SalesReceiptLineAdd_PriceLevelRef_ListID = ET.SubElement(self.qbcom.SalesReceiptLineAdd_PriceLevelRef, 'ListID')
                    self.qbcom.SalesReceiptLineAdd_PriceLevelRef_ListID.text = self.SalesReceiptLineAdd.PriceLevelRef.ListID
                elif self.SalesReceiptLineAdd.PriceLevelRef.FullName:
                    self.qbcom.SalesReceiptLineAdd_PriceLevelRef_FullName = ET.SubElement(self.qbcom.SalesReceiptLineAdd_PriceLevelRef, 'FullName')
                    self.qbcom.SalesReceiptLineAdd_PriceLevelRef_FullName.text = self.SalesReceiptLineAdd.PriceLevelRef.FullName
            if self.SalesReceiptLineAdd.ClassRef.ListID or self.SalesReceiptLineAdd.ClassRef.FullName:
                self.qbcom.SalesReceiptLineAdd_ClassRef = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'ClassRef')
                if self.SalesReceiptLineAdd.ClassRef.ListID:
                    self.qbcom.SalesReceiptLineAdd_ClassRef_ListID = ET.SubElement(self.qbcom.SalesReceiptLineAdd_ClassRef, 'ListID')
                    self.qbcom.SalesReceiptLineAdd_ClassRef_ListID.text = self.SalesReceiptLineAdd.ClassRef.ListID
                elif self.SalesReceiptLineAdd.ClassRef.FullName:
                    self.qbcom.SalesReceiptLineAdd_ClassRef_FullName = ET.SubElement(self.qbcom.SalesReceiptLineAdd_ClassRef, 'FullName')
                    self.qbcom.SalesReceiptLineAdd_ClassRef_FullName.text = self.SalesReceiptLineAdd.ClassRef.FullName
            if self.SalesReceiptLineAdd.Amount:
                self.qbcom.SalesReceiptLineAdd_Amount = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'Amount')
                self.qbcom.SalesReceiptLineAdd_Amount.text = self.SalesReceiptLineAdd.Amount
            if self.SalesReceiptLineAdd.OptionForPriceRuleConflict:
                self.qbcom.SalesReceiptLineAdd_OptionForPriceRuleConflict = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'OptionForPriceRuleConflict')
                self.qbcom.SalesReceiptLineAdd_OptionForPriceRuleConflict.text = self.SalesReceiptLineAdd.OptionForPriceRuleConflict
            if self.SalesReceiptLineAdd.InventorySiteRef.ListID or self.SalesReceiptLineAdd.InventorySiteRef.FullName:
                self.qbcom.SalesReceiptLineAdd_InventorySiteRef = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'InventorySiteRef')
                if self.SalesReceiptLineAdd.InventorySiteRef.ListID:
                    self.qbcom.SalesReceiptLineAdd_InventorySiteRef_ListID = ET.SubElement(self.qbcom.SalesReceiptLineAdd_InventorySiteRef, 'ListID')
                    self.qbcom.SalesReceiptLineAdd_InventorySiteRef_ListID.text = self.SalesReceiptLineAdd.InventorySiteRef.ListID
                elif self.SalesReceiptLineAdd.InventorySiteRef.FullName:
                    self.qbcom.SalesReceiptLineAdd_InventorySiteRef_FullName = ET.SubElement(self.qbcom.SalesReceiptLineAdd_InventorySiteRef, 'FullName')
                    self.qbcom.SalesReceiptLineAdd_InventorySiteRef_FullName.text = self.SalesReceiptLineAdd.InventorySiteRef.FullName
            if self.SalesReceiptLineAdd.InventorySiteLocationRef.ListID or self.SalesReceiptLineAdd.InventorySiteLocationRef.FullName:
                self.qbcom.SalesReceiptLineAdd_InventorySiteLocationRef = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'InventorySiteLocationRef')
                if self.SalesReceiptLineAdd.InventorySiteLocationRef.ListID:
                    self.qbcom.SalesReceiptLineAdd_InventorySiteLocationRef_ListID = ET.SubElement(self.qbcom.SalesReceiptLineAdd_InventorySiteLocationRef, 'ListID')
                    self.qbcom.SalesReceiptLineAdd_InventorySiteLocationRef_ListID.text = self.SalesReceiptLineAdd.InventorySiteLocationRef.ListID
                elif self.SalesReceiptLineAdd.InventorySiteLocationRef.FullName:
                    self.qbcom.SalesReceiptLineAdd_InventorySiteLocationRef_FullName = ET.SubElement(self.qbcom.SalesReceiptLineAdd_InventorySiteLocationRef, 'FullName')
                    self.qbcom.SalesReceiptLineAdd_InventorySiteLocationRef_FullName.text = self.SalesReceiptLineAdd.InventorySiteLocationRef.FullName
            if self.SalesReceiptLineAdd.SerialNumber:
                self.qbcom.SalesReceiptLineAdd_SerialNumber = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'SerialNumber')
                self.qbcom.SalesReceiptLineAdd_SerialNumber.text = self.SalesReceiptLineAdd.SerialNumber
            elif self.SalesReceiptLineAdd.LotNumber:
                self.qbcom.SalesReceiptLineAdd_LotNumber = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'LotNumber')
                self.qbcom.SalesReceiptLineAdd_LotNumber.text = self.SalesReceiptLineAdd.LotNumber
            if self.SalesReceiptLineAdd.SalesTaxCodeRef.ListID or self.SalesReceiptLineAdd.SalesTaxCodeRef.FullName:
                self.qbcom.SalesReceiptLineAdd_SalesTaxCodeRef = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'SalesTaxCodeRef')
                if self.SalesReceiptLineAdd.SalesTaxCodeRef.ListID:
                    self.qbcom.SalesReceiptLineAdd_SalesTaxCodeRef_ListID = ET.SubElement(self.qbcom.SalesReceiptLineAdd_SalesTaxCodeRef, 'ListID')
                    self.qbcom.SalesReceiptLineAdd_SalesTaxCodeRef_ListID.text = self.SalesReceiptLineAdd.SalesTaxCodeRef.ListID
                elif self.SalesReceiptLineAdd.SalesTaxCodeRef.FullName:
                    self.qbcom.SalesReceiptLineAdd_SalesTaxCodeRef_FullName = ET.SubElement(self.qbcom.SalesReceiptLineAdd_SalesTaxCodeRef, 'FullName')
                    self.qbcom.SalesReceiptLineAdd_SalesTaxCodeRef_FullName.text = self.SalesReceiptLineAdd.SalesTaxCodeRef.FullName
            if self.SalesReceiptLineAdd.OverrideItemAccountRef.ListID or self.SalesReceiptLineAdd.OverrideItemAccountRef.FullName:
                self.qbcom.SalesReceiptLineAdd_OverrideItemAccountRef = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'OverrideItemAccountRef')
                if self.SalesReceiptLineAdd.OverrideItemAccountRef.ListID:
                    self.qbcom.SalesReceiptLineAdd_OverrideItemAccountRef_ListID = ET.SubElement(self.qbcom.SalesReceiptLineAdd_OverrideItemAccountRef, 'ListID')
                    self.qbcom.SalesReceiptLineAdd_OverrideItemAccountRef_ListID.text = self.SalesReceiptLineAdd.OverrideItemAccountRef.ListID
                elif self.SalesReceiptLineAdd.OverrideItemAccountRef.FullName:
                    self.qbcom.SalesReceiptLineAdd_OverrideItemAccountRef_FullName = ET.SubElement(self.qbcom.SalesReceiptLineAdd_OverrideItemAccountRef, 'FullName')
                    self.qbcom.SalesReceiptLineAdd_OverrideItemAccountRef_FullName.text = self.SalesReceiptLineAdd.OverrideItemAccountRef.FullName
            if self.SalesReceiptLineAdd.Other1:
                self.qbcom.SalesReceiptLineAdd_Other1 = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'Other1')
                self.qbcom.SalesReceiptLineAdd_Other1.text = self.SalesReceiptLineAdd.Other1
            if self.SalesReceiptLineAdd.Other2:
                self.qbcom.SalesReceiptLineAdd_Other2 = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'Other2')
                self.qbcom.SalesReceiptLineAdd_Other2.text = self.SalesReceiptLineAdd.Other2
            if (self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardNumber or
                self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultCode):
                self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'CreditCardTxnInfo')
                if (self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardNumber):
                    self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo = ET.SubElement(self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo, 'CreditCardTxnInputInfo')
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardNumber:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardNumber = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'CreditCardNumber')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardNumber.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardNumber
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationMonth:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_ExpirationMonth = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'ExpirationMonth')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_ExpirationMonth.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationMonth
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationYear:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_ExpirationYear = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'ExpirationYear')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_ExpirationYear.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.ExpirationYear
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.NameOnCard:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_NameOnCard = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'NameOnCard')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_NameOnCard.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.NameOnCard
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardAddress:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardAddress = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'CreditCardAddress')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardAddress.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardAddress
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardPostalCode:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardPostalCode = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'CreditCardPostalCode')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CreditCardPostalCode.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CreditCardPostalCode
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CommercialCardCode:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CommercialCardCode = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'CommercialCardCode')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CommercialCardCode.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CommercialCardCode
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.TransactionMode:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_TransactionMode = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'TransactionMode')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_TransactionMode.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.TransactionMode
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CrediCardTxnType:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CrediCardTxnType = ET.SubElement(self.qbcom.CreditCardTxnInputInfo, 'CrediCardTxnType')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnInputInfo_CrediCardTxnType.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnInputInfo.CrediCardTxnType
                if (self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultCode):
                    self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo = ET.SubElement(self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo, 'CreditCardTxnResultInfo')
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultCode:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_ResultCode = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'ResultCode')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_ResultCode.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultCode
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultMessage:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_ResultMessage = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'ResultMessage')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_ResultMessage.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ResultMessage
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.CreditCardTransID:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_CreditCardTransID = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'CreditCardTransID')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_CreditCardTransID.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.CreditCardTransID
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.MerchantAccountNumber:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_MerchantAccountNumber = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'MerchantAccountNumber')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_MerchantAccountNumber.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.MerchantAccountNumber
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AuthorizationCode:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_AuthorizationCode = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'AuthorizationCode')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_AuthorizationCode.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AuthorizationCode
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSStreet:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_AVSStreet = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'AVSStreet')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_AVSStreet.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSStreet
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSZip:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_AVSZip = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'AVSZip')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_AVSZip.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.AVSZip
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.CardSecurityCodeMatch:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_CardSecurityCodeMatch = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'CardSecurityCodeMatch')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_CardSecurityCodeMatch.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.CardSecurityCodeMatch
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ReconBatchID:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_ReconBatchID = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'ReconBatchID')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_ReconBatchID.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ReconBatchID
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentGroupingCode:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_PaymentGroupingCode = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'PaymentGroupingCode')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_PaymentGroupingCode.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentGroupingCode
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentStatus:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_PaymentStatus = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'PaymentStatus')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_PaymentStatus.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.PaymentStatus
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationTime:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_TxnAuthorizationTime = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'TxnAuthorizationTime')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_TxnAuthorizationTime.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationTime
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationStamp:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_TxnAuthorizationStamp = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'TxnAuthorizationStamp')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_TxnAuthorizationStamp.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.TxnAuthorizationStamp
                    if self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ClientTransID:
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_ClientTransID = ET.SubElement(self.qbcom.CreditCardTxnResultInfo, 'ClientTransID')
                        self.qbcom.SalesReceiptLineAdd_CreditCardTxnInfo_CreditCardTxnResultInfo_ClientTransID.text = self.SalesReceiptLineAdd.CreditCardTxnInfo.CreditCardTxnResultInfo.ClientTransID
            if (self.SalesReceiptLineAdd.DataExt.OwnerID or
                    self.SalesReceiptLineAdd.DataExt.DataExtName or
                    self.SalesReceiptLineAdd.DataExt.DataExtValue):
                self.qbcom.SalesReceiptLineAdd_DataExt = ET.SubElement(self.qbcom.SalesReceiptLineAdd, 'DataExt')
                if self.SalesReceiptLineAdd.DataExt.OwnerID:
                    self.qbcom.SalesReceiptLineAdd_DataExt_OwnerID = ET.SubElement(self.qbcom.SalesReceiptLineAdd_DataExt, 'OwnerID')
                    self.qbcom.SalesReceiptLineAdd_DataExt_OwnerID.text = self.SalesReceiptLineAdd.DataExt.OwnerID
                if self.SalesReceiptLineAdd.DataExt.DataExtName:
                    self.qbcom.SalesReceiptLineAdd_DataExt_DataExtName = ET.SubElement(self.qbcom.SalesReceiptLineAdd_DataExt, 'DataExtName')
                    self.qbcom.SalesReceiptLineAdd_DataExt_DataExtName.text = self.SalesReceiptLineAdd.DataExt.DataExtName
                if self.SalesReceiptLineAdd.DataExt.DataExtValue:
                    self.qbcom.SalesReceiptLineAdd_DataExt_DataExtValue = ET.SubElement(self.qbcom.SalesReceiptLineAdd_DataExt, 'DataExtValue')
                    self.qbcom.SalesReceiptLineAdd_DataExt_DataExtValue.text = self.SalesReceiptLineAdd.DataExt.DataExtValue
        elif (self.SalesReceiptLineAdd.ItemGroupRef.ListID or
                self.SalesReceiptLineAdd.ItemGroupRef.FullName):
            self.qbcom.SalesReceiptLineAdd = ET.SubElement(self.qbcom.SalesReceiptAdd, 'SalesReceiptLineAdd')
            if self.SalesReceiptLineAdd.ItemGroupRef.ListID or self.SalesReceiptLineAdd.ItemGroupRef.FullName:
                self.qbcom.SalesReceiptLineAdd_ItemGroupRef = ET.SubElement(self.qbcom.SalesReceiptAdd, 'ItemGroupRef')
                if self.SalesReceiptLineAdd.ItemGroupRef.ListID:
                    self.qbcom.SalesReceiptLineAdd_ItemGroupRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.SalesReceiptLineAdd_ItemGroupRef_ListID.text = self.SalesReceiptLineAdd.ItemGroupRef.ListID
                elif self.SalesReceiptLineAdd.ItemGroupRef.FullName:
                    self.qbcom.SalesReceiptLineAdd_ItemGroupRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.SalesReceiptLineAdd_ItemGroupRef_FullName.text = self.SalesReceiptLineAdd.ItemGroupRef.FullName
            if self.SalesReceiptLineAdd.Quantity:
                self.qbcom.SalesReceiptLineAdd_Quantity = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'Quantity')
                self.qbcom.SalesReceiptLineAdd_Quantity.text = self.SalesReceiptLineAdd.Quantity
            if self.SalesReceiptLineAdd.UnitOfMeasure:
                self.qbcom.SalesReceiptLineAdd_UnitOfMeasure = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'UnitOfMeasure')
                self.qbcom.SalesReceiptLineAdd_UnitOfMeasure.text = self.SalesReceiptLineAdd.UnitOfMeasure
            if self.SalesReceiptLineAdd.InventorySiteRef.ListID or self.SalesReceiptLineAdd.InventorySiteRef.FullName:
                self.qbcom.SalesReceiptLineAdd_InventorySiteRef = ET.SubElement(self.qbcom.SalesReceiptAdd, 'InventorySiteRef')
                if self.SalesReceiptLineAdd.InventorySiteRef.ListID:
                    self.qbcom.SalesReceiptLineAdd_InventorySiteRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.SalesReceiptLineAdd_InventorySiteRef_ListID.text = self.SalesReceiptLineAdd.InventorySiteRef.ListID
                elif self.SalesReceiptLineAdd.InventorySiteRef.FullName:
                    self.qbcom.SalesReceiptLineAdd_InventorySiteRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.SalesReceiptLineAdd_InventorySiteRef_FullName.text = self.SalesReceiptLineAdd.InventorySiteRef.FullName
            if self.SalesReceiptLineAdd.InventorySiteLocationRef.ListID or self.SalesReceiptLineAdd.InventorySiteLocationRef.FullName:
                self.qbcom.SalesReceiptLineAdd_InventorySiteLocationRef = ET.SubElement(self.qbcom.SalesReceiptAdd, 'InventorySiteLocationRef')
                if self.SalesReceiptLineAdd.InventorySiteLocationRef.ListID:
                    self.qbcom.SalesReceiptLineAdd_InventorySiteLocationRef_ListID = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'ListID')
                    self.qbcom.SalesReceiptLineAdd_InventorySiteLocationRef_ListID.text = self.SalesReceiptLineAdd.InventorySiteLocationRef.ListID
                elif self.SalesReceiptLineAdd.InventorySiteLocationRef.FullName:
                    self.qbcom.SalesReceiptLineAdd_InventorySiteLocationRef_FullName = ET.SubElement(self.qbcom.ApplyCreditCardChargeToTxnAdd, 'FullName')
                    self.qbcom.SalesReceiptLineAdd_InventorySiteLocationRef_FullName.text = self.SalesReceiptLineAdd.InventorySiteLocationRef.FullName
            if self.SalesReceiptLineAdd.DataExt.OwnerID or self.SalesReceiptLineAdd.DataExt.DataExtName or self.SalesReceiptLineAdd.DataExt.DataExtValue:
                self.qbcom.SalesReceiptLineAdd_DataExt = ET.SubElement(self.qbcom.SalesReceiptAdd, 'DataExt')
                if self.SalesReceiptLineAdd.DataExt.OwnerID:
                    self.qbcom.SalesReceiptLineAdd_DataExt_OwnerID = ET.SubElement(self.qbcom.SalesReceiptLineAdd.DataExt, 'OwnerID')
                    self.qbcom.SalesReceiptLineAdd_DataExt_OwnerID.text = self.SalesReceiptLineAdd.DataExt.OwnerID
                if self.SalesReceiptLineAdd.DataExt.DataExtName:
                    self.qbcom.SalesReceiptLineAdd_DataExt_DataExtName = ET.SubElement(self.qbcom.SalesReceiptLineAdd.DataExt, 'DataExtName')
                    self.qbcom.SalesReceiptLineAdd_DataExt_DataExtName.text = self.SalesReceiptLineAdd.DataExt.DataExtName
                if self.SalesReceiptLineAdd.DataExt.DataExtValue:
                    self.qbcom.SalesReceiptLineAdd_DataExt_DataExtValue = ET.SubElement(self.qbcom.SalesReceiptLineAdd.DataExt, 'DataExtValue')
                    self.qbcom.SalesReceiptLineAdd_DataExt_DataExtValue.text = self.SalesReceiptLineAdd.DataExt.DataExtValue
        if self.IncludeRetElement:
            for item in self.IncludeRetElemenet:
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.SalesReceiptAddRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = item
