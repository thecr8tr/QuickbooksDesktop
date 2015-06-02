__author__ = 'thecr8tr'

from quickbooks import Quickbooks
import xml.etree.ElementTree as ET
from warnings import warn
import sys

##########################################
# TODO Update all methods like Customer
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
                self.qbcom.IncludeRetElement = ET.SubElement(self.qbcom.CustomerQueryRq, 'IncludeRetElement')
                self.qbcom.IncludeRetElement.text = self.IncludeRetElement
        if self.OwnerID:
                self.qbcom.OwnerID = ET.SubElement(self.qbcom.CustomerQueryRq, 'OwnerID')
                self.qbcom.OwnerID.text = self.OwnerID

class query(object):
    def __init__(self, file):
        '''There are more of these to map, but I just entered the first few to see how things go'''
        self.qbcom = Quickbooks(qb_file=file)
        self.request_ID = ''
        self.query_dict = {'AccountTaxLineInfoQueryRq': 'Working',
                           'AgingReportQueryRq': 'DOES NOT WORK',
                           'ARRefundCreditCardQueryRq': 'Working',
                           'BarCodeQueryRq': 'Working',
                           'BillingRateQueryRq': 'Working',
                           'BillPaymentCheckQueryRq': 'Working',
                           'BillPaymentCreditCardQueryRq': 'Working',
                           'BillToPayQueryRq': 'DOES NOT WORK',
                           'BudgetSummaryReportQueryRq': 'DOES NOT WORK',
                           'BuildAssemblyQueryRq': 'Working',
                           'ChargeQueryRq': 'Working',
                           'CheckQueryRq': 'Working',
                           'ClassQueryRq': 'Working',
                           'CompanyQueryRq': 'Working',
                           'CompanyActivityQueryRq': 'Working',
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
                           'HostQueryRq': 'Working',
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
                           'PreferencesQueryRq': 'Working',
                           'PriceLevelQueryRq': 'Working',
                           'PurchaseOrderQueryRq': 'Working',
                           'ReceivePaymentQueryRq': 'Working',
                           'ReceivePaymentToDepositQueryRq': 'Working',
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
                           'TransferQueryRq': 'Working',
                           'TransferInventoryQueryRq': 'Working',
                           'TxnDeletedQueryRq': 'DOES NOT WORK',
                           'UnitOfMeasureSetQueryRq': 'Working',
                           'VehicleQueryRq': 'Working',
                           'VehicleMileageQueryRq': 'Working',
                           'VendorQueryRq': 'Working',
                           'VendorCreditQueryRq': 'Working',
                           'VendorTypeQueryRq': 'Working',
                           'WorkersCompCodeQueryRq': 'Working',
                           '': 'DOES NOT WORK',
        }
        self.set_attributes()

    def set_attributes(self):

        # how to proceed once qbxml encounters an error
        self.onError = 'stopOnError' #options = continueOnError

        # returns a count of items to be returned
        self.metaData = 'NoMetaData' #options = MetaDataOnly, MetaDataAndResponseData

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

        # NameFilter search value
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

        # TotalBalanceFilter amount to search for
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

        # You use this tag in the request to limit the data that will be returned in the response. Inside this tag
        # you specify the name of the top-level element or aggregate that is to be returned in the response to the
        # request. You cannot specify fields within an aggregate, for example, you cannot specify a City within an
        # Address: you must specify Address and will get the entire address.
        self.IncludeRetElement = None # options = ?????

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

    def query_request(self):
        if not self.request_ID in self.query_dict or self.query_dict[self.request_ID] == 'DOES NOT WORK':
            raise ValueError('self.request_ID must be set with a proper value. See request.query.__init__.query_dict')
        try:
            # Dynamically call the function to set the attributes for the object (ie search_parameter.set_CustomerQueryRq_attributes())
            getattr(search_parameter, 'set_{}_attributes'.format(self.request_ID))(self)
        except AttributeError:
            warn('set_{}_attributes does not exist'.format(self.request_ID))

        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()
