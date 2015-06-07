from quickbooks.parameters import search_parameter

__author__ = 'thecr8tr'

from quickbooks import Quickbooks
from quickbooks.parameters import search_parameter
import xml.etree.ElementTree as ET
from warnings import warn

##########################################
# TODO Need to add requestID as an attribute of request
##########################################

class query(object):

    def __init__(self, file):
        '''There are more of these to map, but I just entered the first few to see how things go'''
        self.qbcom = Quickbooks(qb_file=file)
        self.qbcom.QBXMLMsgsRq = ET.SubElement(self.qbcom.QBXML, 'QBXMLMsgsRq')
        self.request_ID = ''
        search_parameter.set_attributes(self)
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
        self.qbcom.QBXMLMsgsRq = ET.SubElement(self.qbcom.QBXML, 'QBXMLMsgsRq')
        self.request_ID = ''
        search_parameter.set_attributes(self)
        self.add_dict = {'AccountAddRq': 'Working',
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

    def add_request(self):

        if not self.request_ID in self.add_dict:
            raise ValueError('Requested ID : {} not in the list'.format(self.request_ID))
        elif self.add_dict[self.request_ID] != 'Working':
            warn('Requested ID status is: {}'.format(self.add_dict[self.request_ID]))
        getattr(search_parameter, 'set_{}_attributes'.format(self.request_ID))(self)

        self.qbcom.start_session()
        self.response = self.qbcom.request()
        self.qbcom.close_connection()

