import xml.etree.ElementTree as ET
import win32com.client

class Quickbooks:
    def __init__(self, qb_file=None, stop_on_error=True):
        '''
        qb_file must be the Absolute path to your quickbooks
        stop_on_error is a QBXML variable (not currently used)
        '''
        self.qb_file = qb_file
        self.app_name = "Quickbooks Python"
        self.ticket = None
        self.qbxml_query = """
        <?qbxml version="13.0"?>
        <QBXML>
            <QBXMLMsgsRq onError="stopOnError">
                <{}></{}>
            </QBXMLMsgsRq>
        </QBXML>
        """

    def version_suported(self):
        """
        Return The highest version of QBXML supported by the QB File
        iter over the SupportedQBXMLVersion and return the last value.
        """
        for ver in ET.fromstring(self.get('Host')).iter("SupportedQBXMLVersion"):
          version = ver.text

        return  version

    def create_xml_tag_name(self, object_name, operation, method):
        '''
        According to chapter 3 page # 32:
        Naming are sliced in 3 parts object, operation + Rq
        '''
        return "%s%s%s" %(object_name, operation.title(), method.title())

    def start_session(self, mode=2):
        """
        It creates and returns a Session Object.
        """
        self.session = win32com.client.Dispatch("QBXMLRP2.RequestProcessor")
        self.session.OpenConnection('', self.app_name)
        self.ticket = self.session.BeginSession(self.qb_file, mode)

    def close_connection(self):
        self.session.EndSession(self.ticket)
        self.session.CloseConnection()

    def request(self, qbxml_query, query='CustomerQuery'):

        self.resp = None
        try:
            return self.session.ProcessRequest(self.ticket, qbxml_query)
        except Exception as e:
            print(e)

    def get(self, query):
        q = self.create_xml_tag_name(query, operation='query', method='rq')
        return self.request(q)
