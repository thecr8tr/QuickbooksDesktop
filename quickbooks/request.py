__author__ = 'thecr8tr'

from quickbooks import Quickbooks
import xml.etree.ElementTree as ET
from warnings import warn
import sys

##########################################
# TODO Need to add requestID as an attribute of request
##########################################

class search_parameter():
    def __init__(self):
        pass

    def set_CustomerQueryRq_attributes(self):
        '''
        My IDE sure does hate me doing this, but it sure does work
        Any suggestions on a better way to do this???
        '''
        self.qbcom.QBXMLMsgRq.set('onError', self.onError)
        self.qbcom.CustomerQueryRq = ET.SubElement(self.qbcom.QBXMLMsgRq, self.request_ID)
        self.qbcom.CustomerQueryRq.set('metaData', self.metaData)
        if self.qbcom.iterator:
            self.qbcom.CustomerQueryRq.set('iterator', self.qbcom.iterator)
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

class query(object):

    def __init__(self, file):
        '''There are more of these to map, but I just entered the first few to see how things go'''
        self.qbcom = Quickbooks(qb_file=file)
        self.request_ID = ''
        self.set_attributes()
        self.query_dict = {'AccountQueryRq': 'Working',
                           'AccountTaxLineInfoQueryRq': 'Working',
                           'AgingReportQueryRq': 'DOES NOT WORK',
                           'ARRefundCreditCardQueryRq': 'Working',
                           'BarCodeQueryRq': 'Working',
                           'BillingRateQueryRq': 'Working',
                           'BillPaymentCheckQueryRq': 'Working',
                           'BillPaymentCreditCardQueryRq': 'Working',
                           'BillQueryRq': 'Working',
                           'BillToPayQueryRq': 'DOES NOT WORK', # Returns the TxnID for open bills and credits
                           'BudgetSummaryReportQueryRq': 'DOES NOT WORK',
                           'BuildAssemblyQueryRq': 'Working',
                           'ChargeQueryRq': 'Working',
                           'CheckQueryRq': 'Working',
                           'ClassQueryRq': 'Working',
                           'CompanyQueryRq': 'Working', # Returns Basic info about QB company file
                           'CompanyActivityQueryRq': 'Working', # Determines the date the company file was last restored
                           'CreditCardChargeQueryRq': 'Working',
                           'CreditCardCreditQueryRq': 'Working',
                           'CreditMemoQueryRq': 'Working',
                           'CurrencyQueryRq': 'Working',
                           'CustomDetailReportQueryRq': 'DOES NOT WORK',
                           'CustomerQueryRq': 'Working',
                           'CustomerMsgQueryRq': 'Working',
                           'CustomerTypeQueryRq': 'Working',
                           'CustomSummaryReportQueryRq': 'DOES NOT WORK',
                           'DataEventRecoveryInfoQueryRq': 'DOES NOT WORK',
                           'DataExtDefQueryRq': 'Working',
                           'DateDrivenTermsQueryRq': 'Working',
                           'DepositQueryRq': 'Working',
                           'EmployeeQueryRq': 'Working',
                           'EntityQueryRq': 'Working',
                           'EstimateQueryRq': 'Working',
                           'Form1099CategoryAccountMappingQueryRq': 'Working',
                           'GeneralDetailReportQueryRq': 'DOES NOT WORK',
                           'HostQueryRq': 'Working', # returns QB product info & version & qbXML specs
                           'InventoryAdjustmentQueryRq': 'Working',
                           'InventorySiteQueryRq': 'Working',
                           'InvoiceQueryRq': 'Working',
                           'ItemQueryRq': 'Working',
                           'ItemAssembliesCanBuildQueryRq': 'DOES NOT WORK',
                           'ItemDiscountQueryRq': 'Working',
                           'ItemFixedAssetQueryRq': 'Working',
                           'ItemGroupQueryRq': 'Working',
                           'ItemInventoryQueryRq': 'Working',
                           'ItemInventoryAssemblyQueryRq': 'Working',
                           'ItemNonInventoryQueryRq': 'Working',
                           'ItemOtherChargeQueryRq': 'Working',
                           'ItemPaymentQueryRq': 'Working',
                           'ItemReceiptQueryRq': 'Working',
                           'ItemSalesTaxQueryRq': 'Working',
                           'ItemSalesTaxGroupQueryRq': 'Working',
                           'ItemServiceQueryRq': 'Working',
                           'ItemSitesQueryRq': 'Working',
                           'ItemSubtotalQueryRq': 'Working',
                           'JobReportQueryRq': 'DOES NOT WORK',
                           'JobTypeQueryRq': 'Working',
                           'JournalEntryQueryRq': 'Working',
                           'LeadQueryRq': 'Working',
                           'ListDeletedQueryRq': 'DOES NOT WORK',
                           'OtherNameQueryRq': 'Working',
                           'PaymentMethodQueryRq': 'Working',
                           'PayrollDetailReportQueryRq': 'DOES NOT WORK',
                           'PayrollItemNonWageQueryRq': 'Working',
                           'PayrollItemWageQueryRq': 'Working',
                           'PayrollSummaryReportQueryRq': 'DOES NOT WORK',
                           'PreferencesQueryRq': 'Working', # allows user to check if an operation can be performed
                           'PriceLevelQueryRq': 'Working',
                           'PurchaseOrderQueryRq': 'Working',
                           'ReceivePaymentQueryRq': 'Working',
                           'ReceivePaymentToDepositQueryRq': 'Working', # returns TxnID of payments to be deposited
                           'SalesOrderQueryRq': 'Working',
                           'SalesReceiptQueryRq': 'Working',
                           'SalesRepQueryRq': 'Working',
                           'SalesTaxCodeQueryRq': 'Working',
                           'SalesTaxPayableQueryRq': 'Working',
                           'SalesTaxPaymentCheckQueryRq': 'Working',
                           'ShipMethodQueryRq': 'Working',
                           'StandardTermsQueryRq': 'Working',
                           'TemplateQueryRq': 'Working',
                           'TermsQueryRq': 'Working',
                           'TimeReportQueryRq': 'DOES NOT WORK',
                           'TimeTrackingQueryRq': 'Working',
                           'ToDoQueryRq': 'Working',
                           'TransactionQueryRq': 'Working',
                           'TransferQueryRq': 'Working', # Returns all Txn types with data generic to all
                           'TransferInventoryQueryRq': 'Working',
                           'TxnDeletedQueryRq': 'DOES NOT WORK',
                           'UnitOfMeasureSetQueryRq': 'Working',
                           'VehicleQueryRq': 'Working',
                           'VehicleMileageQueryRq': 'Working',
                           'VendorQueryRq': 'Working',
                           'VendorCreditQueryRq': 'Working',
                           'VendorTypeQueryRq': 'Working',
                           'WorkersCompCodeQueryRq': 'Working',
        }

    def set_attributes(self):

        # how to proceed once qbxml encounters an error
        self.onError = 'stopOnError' #options = continueOnError

        # returns a count of items to be returned
        self.metaData = 'NoMetaData' #options = MetaDataOnly, MetaDataAndResponseData

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
        self.NameFilter = search_parameter()

        # NameFilter search parameters
        self.NameFilter.MatchCriterion = None # options = StartsWith, Contains, EndsWith

        # NameFilter search value (can be all or part)
        self.NameFilter.Name = None # user supplied string to match from

        # filters for object name between two user supplied names
        self.NameRangeFilter = search_parameter()

        # NameRangeFilter search start value (omit to search from beginning of list)
        self.NameRangeFilter.FromName = None # user supplied string to start match

        # NameRangeFilter search end value (omit to search to end of list)
        self.NameRangeFilter.ToName = None # user supplied string to end match

        # Filters based on the amount of the total balance (includes sub accounts)
        self.TotalBalanceFilter = search_parameter()

        # TotalBalanceFilter
        self.TotalBalanceFilter.Operator = None # options = LessThan, LessThanEqual, Equal, GreaterThan,
                                                          # GreaterThanEqual

        # TotalBalanceFilter amount to search for (customers and vendors only)
        self.TotalBalanceFilter.Amount = None # user supplied string of a 2 decimal place dollar amount

        # filters for object name between two user supplied names
        self.CurrencyFilter = search_parameter()

        # CurrencyFilter
        self.CurrencyFilter.ListID = None # ListID comes from QB File

        # CurrencyFilter
        self.CurrencyFilter.FullName = None # FullName comes from QB File and Must include Parents if applicable

        # filters for object name between two user supplied names
        self.ClassFilter = search_parameter()

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
        self.ModifiedDateRangeFilter = search_parameter()

        # This is based on a QuickBooks Supplied Date/Time
        self.ModifiedDateRangeFilter.FromModifiedDate = None #options = YYYY+'-'+MM+'-'+DD[+'T'+hh[+':'+mm[+':'+ss[+'-'+hh+':'+mm]]]]

        # This is based on a QuickBooks Supplied Date/Time
        self.ModifiedDateRangeFilter.ToModifiedDate = None #options = YYYY+'-'+MM+'-'+DD[+'T'+hh[+':'+mm[+':'+ss[+'-'+hh+':'+mm]]]]

        # This is based on the user Supplied Date
        self.TxnDateRangeFilter = search_parameter()

        # This is based on a QuickBooks Supplied Date/Time
        self.TxnDateRangeFilter.FromTxnDate = None #options = YYYY+'-'+MM+'-'+DD

        # This is based on a QuickBooks Supplied Date/Time
        self.TxnDateRangeFilter.ToTxnDate = None #options = YYYY+'-'+MM+'-'+DD

        #
        self.DateMacro = None # options ThisWeekToDate, ThisMonthToDate, LastWeek, LastFiscalQuarter, LastFiscalYear...

        # EntityFilter
        self.EntityFilter = search_parameter() # options FullName, ListID, FullNameWithChildren, or ListIDWithChildren

        # EntityFilter
        self.EntityFilter.ListID = None # ListID comes from QB File

        # EntityFilter
        self.EntityFilter.FullName = None # FullName comes from QB File and Must include Parents if applicable

        # EntityFilter Returns item w/ ListID and its decendants
        self.EntityFilter.ListIDWithChildren = None # ListID comes from QB File

        # EntityFilter Returns item w/ FullName and its decendants
        self.EntityFilter.FullNameWithChildren = None # FullName comes from QB File and Must include Parents if applicable

        # AccountFilter --- Only works on the main account Associated with trans (ie, bank account for check or deposit)
        self.AccountFilter = search_parameter() # options FullName, ListID, FullNameWithChildren, or ListIDWithChildren

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

    def query_request(self):
        '''
        This function does a name validation, sets the attributes, starts a session,
        submits the request, catches the response, closes the session
        '''
        if not self.request_ID in self.query_dict:
            raise ValueError('Requested ID : {} not in the list'.format(self.request_ID))
        elif self.query_dict[self.request_ID] != 'Working':
            warn('Requested ID status is: {}'.format(self.query_dict[self.request_ID]))
        try:
            # Dynamically call the function to set the attributes for the object (ie search_parameter.set_CustomerQueryRq_attributes())
            getattr(search_parameter, 'set_{}_attributes'.format(self.request_ID))(self)
        except AttributeError:
            warn('set_{}_attributes does not exist'.format(self.request_ID))

        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

class add(object):

    def __init__(self, file):
        self.qbcom = Quickbooks(qb_file=file)
        self.request_ID = ''
        self.set_attributes()
        self.query_dict = {'AccountAddRq': 'Working',
                           'ARRefundCreditCardAddRq': 'Working',
                           'BillAddRq': 'Working',
                           'BillingRateAddRq': 'Working',
                           'BillPaymentCheckAddRq': 'Working',
                           'BillPaymentCreditCardAddRq': 'Working',
                           'BuildAssemblyAddRq': 'Working',
                           'ChargeAddRq': 'Working',
                           'CheckAddRq': 'Working',
                           'ClassAddRq': 'Working',
                           'CreditCardChargeAddRq': 'Working',
                           'CreditCardCreditAddRq': 'Working',
                           'CreditMemoAddRq': 'Working',
                           'CurrencyAddRq': 'Working',
                           'CustomerAddRq': 'Working',
                           'CustomerMsgAddRq': 'Working',
                           'CustomerTypeAddRq': 'Working',
                           'DataExtAddRq': 'Working',
                           'DataExtDefAddRq': 'Working',
                           'DateDrivenTermsAddRq': 'Working',
                           'DepositAddRq': 'Working',
                           'EmployeeAddRq': 'Working',
                           'EstimateAddRq': 'Working',
                           'InventoryAdjustmentAddRq': 'Working',
                           'InventorySiteAddRq': 'Working',
                           'InvoiceAddRq': 'Working',
                           'ItemDiscountAddRq': 'Working',
                           'ItemFixedAssetAddRq': 'Working',
                           'ItemGroupAddRq': 'Working',
                           'ItemInventoryAddRq': 'Working',
                           'ItemInventoryAssemblyAddRq': 'Working',
                           'ItemNonInventoryAddRq': 'Working',
                           'ItemOtherChargeAddRq': 'Working',
                           'ItemPaymentAddRq': 'Working',
                           'ItemReceiptAddRq': 'Working',
                           'ItemSalesTaxAddRq': 'Working',
                           'ItemSalesTaxGroupAddRq': 'Working',
                           'ItemServiceAddRq': 'Working',
                           'ItemSubtotalAddRq': 'Working',
                           'JobTypeAddRq': 'Working',
                           'JournalEntryAddRq': 'Working',
                           'LeadAddRq': 'Working',
                           'ListDisplayAddRq': 'DOES NOT WORK',
                           'OtherNameAddRq': 'Working',
                           'PaymentMethodAddRq': 'Working',
                           'PayrollItemWageAddRq': 'Working',
                           'PriceLevelAddRq': 'Working',
                           'PurchaseOrderAddRq': 'Working',
                           'ReceivePaymentAddRq': 'Working',
                           'SalesOrderAddRq': 'Working',
                           'SalesReceiptAddRq': 'Working',
                           'SalesRepAddRq': 'Working',
                           'SalesTaxCodeAddRq': 'Working',
                           'SalesTaxPaymentCheckAddRq': 'Working',
                           'ShipMethodAddRq': 'Working',
                           'StandardTermsAddRq': 'Working',
                           'TimeTrackingAddRq': 'Working',
                           'ToDoAddRq': 'Working',
                           'TransferAddRq': 'Working',
                           'TransferInventoryAddRq': 'Working',
                           'TxnDisplayAddRq': 'DOES NOT WORK',
                           'UnitOfMeasureSetAddRq': 'Working',
                           'VehicleAddRq': 'Working',
                           'VehicleMileageAddRq': 'Working',
                           'VendorAddRq': 'Working',
                           'VendorCreditAddRq': 'Working',
                           'VendorTypeAddRq': 'Working',
                           'WorkersCompCodeAddRq': 'Working',
        }

    def set_attributes(self):
        pass

    def add_request(self):

        if not self.request_ID in self.query_dict:
            raise ValueError('Requested ID : {} not in the list'.format(self.request_ID))
        elif self.query_dict[self.request_ID] != 'Working':
            warn('Requested ID status is: {}'.format(self.query_dict[self.request_ID]))
        try:
            # Dynamically call the function to set the attributes for the object (ie search_parameter.set_CustomerQueryRq_attributes())
            getattr(search_parameter, 'set_{}_attributes'.format(self.request_ID))(self)
        except AttributeError:
            warn('set_{}_attributes does not exist'.format(self.request_ID))

        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

