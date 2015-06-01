__author__ = 'thecr8tr'

from quickbooks import Quickbooks
import xml.etree.ElementTree as ET

##########################################
# TODO Update all methods like Customer
##########################################

class search_parameter():
    def __init__(self):
        pass

    def set_Customer_request_attributes(self):
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

    def AccountTaxLineInfo(self):
        ''''''
        self.request_ID = 'AccountTaxLineInfoQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def AgingReport(self):
        '''DOES NOT WORK'''
        self.request_ID = 'AgingReportQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ARRefundCreditCard(self):
        ''''''
        self.request_ID = 'ARRefundCreditCardQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def BarCode(self):
        ''''''
        self.request_ID = 'BarCodeQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def BillingRate(self):
        ''''''
        self.request_ID = 'BillingRateQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def BillPaymentCheck(self):
        ''''''
        self.request_ID = 'BillPaymentCheckQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def BillPaymentCreditCard(self):
        ''''''
        self.request_ID = 'BillPaymentCreditCardQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def BillToPay(self):
        '''DOES NOT WORK'''
        self.request_ID = 'BillToPayQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def BudgetSummaryReport(self):
        '''DOES NOT WORK'''
        self.request_ID = 'BudgetSummaryReportQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def BuildAssembly(self):
        ''''''
        self.request_ID = 'BuildAssemblyQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Charge(self):
        ''''''
        self.request_ID = 'ChargeQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Check(self):
        ''''''
        self.request_ID = 'CheckQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Class(self):
        ''''''
        self.request_ID = 'ClassQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Company(self):
        ''''''
        self.request_ID = 'CompanyQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def CompanyActivity(self):
        ''''''
        self.request_ID = 'CompanyActivityQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def CreditCardCharge(self):
        ''''''
        self.request_ID = 'CreditCardChargeQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def CreditCardCredit(self):
        ''''''
        self.request_ID = 'CreditCardCreditQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def CreditMemo(self):
        ''''''
        self.request_ID = 'CreditMemoQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Currency(self):
        ''''''
        self.request_ID = 'CurrencyQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def CustomDetailReport(self):
        '''DOES NOT WORK'''
        self.request_ID = 'CustomDetailReportQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Customer(self):
        ''''''
        self.request_ID = 'CustomerQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def CustomerMsg(self):
        ''''''
        self.request_ID = 'CustomerMsgQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def CustomerType(self):
        ''''''
        self.request_ID = 'CustomerTypeQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def CustomSummaryReport(self):
        '''DOES NOT WORK'''
        self.request_ID = 'CustomSummaryReportQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def DataEventRecoveryInfo(self):
        '''DOES NOT WORK'''
        self.request_ID = 'DataEventRecoveryInfoQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def DataExtDef(self):
        ''''''
        self.request_ID = 'DataExtDefQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def DateDrivenTerms(self):
        ''''''
        self.request_ID = 'DateDrivenTermsQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Deposit(self):
        ''''''
        self.request_ID = 'DepositQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Employee(self):
        ''''''
        self.request_ID = 'EmployeeQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Entity(self):
        ''''''
        self.request_ID = 'EntityQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Estimate(self):
        ''''''
        self.request_ID = 'EstimateQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Form1099CategoryAccountMapping(self):
        ''''''
        self.request_ID = 'Form1099CategoryAccountMappingQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def GeneralDetailReport(self):
        '''DOES NOT WORK'''
        self.request_ID = 'GeneralDetailReportQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Host(self):
        ''''''
        self.request_ID = 'HostQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def InventoryAdjustment(self):
        ''''''
        self.request_ID = 'InventoryAdjustmentQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def InventorySite(self):
        ''''''
        self.request_ID = 'InventorySiteQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Invoice(self):
        ''''''
        self.request_ID = 'InvoiceQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Item(self):
        ''''''
        self.request_ID = 'ItemQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ItemAssembliesCanBuild(self):
        '''DOES NOT WORK'''
        self.request_ID = 'ItemAssembliesCanBuildQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ItemDiscount(self):
        ''''''
        self.request_ID = 'ItemDiscountQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ItemFixedAsset(self):
        ''''''
        self.request_ID = 'ItemFixedAssetQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ItemGroup(self):
        ''''''
        self.request_ID = 'ItemGroupQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ItemInventory(self):
        ''''''
        self.request_ID = 'ItemInventoryQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ItemInventoryAssembly(self):
        ''''''
        self.request_ID = 'ItemInventoryAssemblyQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ItemNonInventory(self):
        ''''''
        self.request_ID = 'ItemNonInventoryQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ItemOtherCharge(self):
        ''''''
        self.request_ID = 'ItemOtherChargeQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ItemPayment(self):
        ''''''
        self.request_ID = 'ItemPaymentQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ItemReceipt(self):
        ''''''
        self.request_ID = 'ItemReceiptQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ItemSalesTax(self):
        ''''''
        self.request_ID = 'ItemSalesTaxQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ItemSalesTaxGroup(self):
        ''''''
        self.request_ID = 'ItemSalesTaxGroupQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ItemService(self):
        ''''''
        self.request_ID = 'ItemServiceQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ItemSites(self):
        ''''''
        self.request_ID = 'ItemSitesQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ItemSubtotal(self):
        ''''''
        self.request_ID = 'ItemSubtotalQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def JobReport(self):
        '''DOES NOT WORK'''
        self.request_ID = 'JobReportQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def JobType(self):
        ''''''
        self.request_ID = 'JobTypeQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def JournalEntry(self):
        ''''''
        self.request_ID = 'JournalEntryQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Lead(self):
        ''''''
        self.request_ID = 'LeadQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ListDeleted(self):
        '''DOES NOT WORK'''
        self.request_ID = 'ListDeletedQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def OtherName(self):
        ''''''
        self.request_ID = 'OtherNameQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def PaymentMethod(self):
        ''''''
        self.request_ID = 'PaymentMethodQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def PayrollDetailReport(self):
        '''DOES NOT WORK'''
        self.request_ID = 'PayrollDetailReportQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def PayrollItemNonWage(self):
        ''''''
        self.request_ID = 'PayrollItemNonWageQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def PayrollItemWage(self):
        ''''''
        self.request_ID = 'PayrollItemWageQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def PayrollSummaryReport(self):
        '''DOES NOT WORK'''
        self.request_ID = 'PayrollSummaryReportQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Preferences(self):
        ''''''
        self.request_ID = 'PreferencesQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def PriceLevel(self):
        ''''''
        self.request_ID = 'PriceLevelQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def PurchaseOrder(self):
        ''''''
        self.request_ID = 'PurchaseOrderQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ReceivePayment(self):
        ''''''
        self.request_ID = 'ReceivePaymentQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ReceivePaymentToDeposit(self):
        ''''''
        self.request_ID = 'ReceivePaymentToDepositQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def SalesOrder(self):
        ''''''
        self.request_ID = 'SalesOrderQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def SalesReceipt(self):
        ''''''
        self.request_ID = 'SalesReceiptQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def SalesRep(self):
        ''''''
        self.request_ID = 'SalesRepQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def SalesTaxCode(self):
        ''''''
        self.request_ID = 'SalesTaxCodeQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def SalesTaxPayable(self):
        ''''''
        self.request_ID = 'SalesTaxPayableQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def SalesTaxPaymentCheck(self):
        ''''''
        self.request_ID = 'SalesTaxPaymentCheckQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ShipMethod(self):
        ''''''
        self.request_ID = 'ShipMethodQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def StandardTerms(self):
        ''''''
        self.request_ID = 'StandardTermsQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Template(self):
        ''''''
        self.request_ID = 'TemplateQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Terms(self):
        ''''''
        self.request_ID = 'TermsQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def TimeReport(self):
        '''DOES NOT WORK'''
        self.request_ID = 'TimeReportQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def TimeTracking(self):
        ''''''
        self.request_ID = 'TimeTrackingQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def ToDo(self):
        ''''''
        self.request_ID = 'ToDoQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Transaction(self):
        ''''''
        self.request_ID = 'TransactionQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Transfer(self):
        ''''''
        self.request_ID = 'TransferQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def TransferInventory(self):
        ''''''
        self.request_ID = 'TransferInventoryQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def TxnDeleted(self):
        '''DOES NOT WORK'''
        self.request_ID = 'TxnDeletedQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def UnitOfMeasureSet(self):
        ''''''
        self.request_ID = 'UnitOfMeasureSetQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Vehicle(self):
        ''''''
        self.request_ID = 'VehicleQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def VehicleMileage(self):
        ''''''
        self.request_ID = 'VehicleMileageQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def Vendor(self):
        ''''''
        self.request_ID = 'VendorQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def VendorCredit(self):
        ''''''
        self.request_ID = 'VendorCreditQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def VendorType(self):
        ''''''
        self.request_ID = 'VendorTypeQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

    def WorkersCompCode(self):
        ''''''
        self.request_ID = 'WorkersCompCodeQueryRq'
        search_parameter.set_Customer_request_attributes(self)
        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()
