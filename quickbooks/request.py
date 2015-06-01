__author__ = 'thecr8tr'

from quickbooks import Quickbooks


class query(object):
    def __init__(self, file):
        self.qbcom = Quickbooks(qb_file=file)

    def AccountTaxLineInfo(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('AccountTaxLineInfo', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def AgingReport(self):
        '''DOES NOT WORK'''
        Request_Tag = self.qbcom.create_xml_tag_name('AgingReport', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ARRefundCreditCard(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ARRefundCreditCard', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def BarCode(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('BarCode', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def BillingRate(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('BillingRate', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def BillPaymentCheck(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('BillPaymentCheck', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def BillPaymentCreditCard(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('BillPaymentCreditCard', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def BillToPay(self):
        '''DOES NOT WORK'''
        Request_Tag = self.qbcom.create_xml_tag_name('BillToPay', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def BudgetSummaryReport(self):
        '''DOES NOT WORK'''
        Request_Tag = self.qbcom.create_xml_tag_name('BudgetSummaryReport', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def BuildAssembly(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('BuildAssembly', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Charge(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Charge', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Check(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Check', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Class(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Class', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Company(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Company', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def CompanyActivity(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('CompanyActivity', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def CreditCardCharge(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('CreditCardCharge', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def CreditCardCredit(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('CreditCardCredit', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def CreditMemo(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('CreditMemo', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Currency(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Currency', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def CustomDetailReport(self):
        '''DOES NOT WORK'''
        Request_Tag = self.qbcom.create_xml_tag_name('CustomDetailReport', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Customer(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Customer', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def CustomerMsg(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('CustomerMsg', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def CustomerType(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('CustomerType', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def CustomSummaryReport(self):
        '''DOES NOT WORK'''
        Request_Tag = self.qbcom.create_xml_tag_name('CustomSummaryReport', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def DataEventRecoveryInfo(self):
        '''DOES NOT WORK'''
        Request_Tag = self.qbcom.create_xml_tag_name('DataEventRecoveryInfo', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def DataExtDef(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('DataExtDef', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def DateDrivenTerms(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('DateDrivenTerms', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Deposit(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Deposit', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Employee(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Employee', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Entity(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Entity', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Estimate(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Estimate', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Form1099CategoryAccountMapping(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Form1099CategoryAccountMapping', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def GeneralDetailReport(self):
        '''DOES NOT WORK'''
        Request_Tag = self.qbcom.create_xml_tag_name('GeneralDetailReport', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Host(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Host', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def InventoryAdjustment(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('InventoryAdjustment', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def InventorySite(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('InventorySite', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Invoice(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Invoice', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Item(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Item', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ItemAssembliesCanBuild(self):
        '''DOES NOT WORK'''
        Request_Tag = self.qbcom.create_xml_tag_name('ItemAssembliesCanBuild', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ItemDiscount(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ItemDiscount', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ItemFixedAsset(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ItemFixedAsset', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ItemGroup(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ItemGroup', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ItemInventory(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ItemInventory', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ItemInventoryAssembly(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ItemInventoryAssembly', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ItemNonInventory(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ItemNonInventory', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ItemOtherCharge(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ItemOtherCharge', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ItemPayment(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ItemPayment', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ItemReceipt(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ItemReceipt', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ItemSalesTax(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ItemSalesTax', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ItemSalesTaxGroup(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ItemSalesTaxGroup', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ItemService(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ItemService', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ItemSites(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ItemSites', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ItemSubtotal(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ItemSubtotal', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def JobReport(self):
        '''DOES NOT WORK'''
        Request_Tag = self.qbcom.create_xml_tag_name('JobReport', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def JobType(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('JobType', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def JournalEntry(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('JournalEntry', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Lead(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Lead', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ListDeleted(self):
        '''DOES NOT WORK'''
        Request_Tag = self.qbcom.create_xml_tag_name('ListDeleted', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def OtherName(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('OtherName', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def PaymentMethod(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('PaymentMethod', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def PayrollDetailReport(self):
        '''DOES NOT WORK'''
        Request_Tag = self.qbcom.create_xml_tag_name('PayrollDetailReport', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def PayrollItemNonWage(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('PayrollItemNonWage', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def PayrollItemWage(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('PayrollItemWage', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def PayrollSummaryReport(self):
        '''DOES NOT WORK'''
        Request_Tag = self.qbcom.create_xml_tag_name('PayrollSummaryReport', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Preferences(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Preferences', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def PriceLevel(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('PriceLevel', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def PurchaseOrder(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('PurchaseOrder', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ReceivePayment(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ReceivePayment', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ReceivePaymentToDeposit(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ReceivePaymentToDeposit', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def SalesOrder(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('SalesOrder', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def SalesReceipt(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('SalesReceipt', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def SalesRep(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('SalesRep', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def SalesTaxCode(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('SalesTaxCode', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def SalesTaxPayable(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('SalesTaxPayable', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def SalesTaxPaymentCheck(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('SalesTaxPaymentCheck', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ShipMethod(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ShipMethod', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def StandardTerms(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('StandardTerms', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Template(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Template', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Terms(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Terms', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def TimeReport(self):
        '''DOES NOT WORK'''
        Request_Tag = self.qbcom.create_xml_tag_name('TimeReport', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def TimeTracking(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('TimeTracking', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def ToDo(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('ToDo', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Transaction(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Transaction', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Transfer(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Transfer', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def TransferInventory(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('TransferInventory', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def TxnDeleted(self):
        '''DOES NOT WORK'''
        Request_Tag = self.qbcom.create_xml_tag_name('TxnDeleted', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def UnitOfMeasureSet(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('UnitOfMeasureSet', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Vehicle(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Vehicle', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def VehicleMileage(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('VehicleMileage', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def Vendor(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('Vendor', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def VendorCredit(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('VendorCredit', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def VendorType(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('VendorType', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()

    def WorkersCompCode(self):
        ''''''
        Request_Tag = self.qbcom.create_xml_tag_name('WorkersCompCode', 'query', 'rq')
        self.qbcom.qbxml_query = self.qbcom.qbxml_query.format(Request_Tag, Request_Tag)
        self.qbcom.start_session()
        self.response = self.qbcom.request(self.qbcom.qbxml_query)
        self.qbcom.close_connection()


