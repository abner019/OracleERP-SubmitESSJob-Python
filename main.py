import requests
from requests.structures import CaseInsensitiveDict
from xml.etree import ElementTree
from requests.auth import HTTPBasicAuth
from suds.sax.element import Element


def call():
    ################# Declaracao de Variaveis
    encodedBase64 = '';
    decodedString = '';

    contador = 3;

    # Enpoint do Webservice SOAP
    url = "https://efei-test.fa.la1.oraclecloud.com:443/ess/esswebservice";
    # Instanciando Header
    headers = CaseInsensitiveDict()


    # Attribuindo content-Type no Header
    headers = {'content-type': 'text/xml'
               }


    # Declarando Request
    payload = """
                  <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://xmlns.oracle.com/scheduler" xmlns:typ="http://xmlns.oracle.com/scheduler/types" xmlns:wsa="http://www.w3.org/2005/08/addressing">
                   <soapenv:Header>
                      <wsa:Action>submitRequest</wsa:Action>
                      <wsa:MessageID>urn:uuid:de3b8096-6576-4fef-a254-797e56ce29a4</wsa:MessageID>
                      <wsa:RelatesTo>urn:uuid:f1d875e4-d718-40ba-9a8e-65733cf0733f</wsa:RelatesTo>
                   </soapenv:Header>
                   <soapenv:Body>
                      <sch:submitRequest>
                         <sch:description>Running Cloud Usage Metrics As Web Service</sch:description>
                         <sch:jobDefinitionId>
                            <typ:name>FinExmSelfCorrectionJob</typ:name>
                            <typ:packageName>/oracle/apps/ess/custom/oracle/apps/ess/financials/expenses/shared/scheduler/</typ:packageName>
                            <typ:type>JOB_DEFINITION</typ:type>
                         </sch:jobDefinitionId>
                         <sch:application>FscmEss</sch:application>
                         <sch:requestedStartTime>2022-05-05T12:30:00</sch:requestedStartTime>
                         <sch:requestParameters>
                            <typ:parameter>
                               <typ:dataType>STRING</typ:dataType>
                               <typ:name>submit.argument1</typ:name>
                               <typ:value>UPD_EXM_CA</typ:value>
                            </typ:parameter>
                            <typ:parameter>
                               <typ:dataType>STRING</typ:dataType>
                               <typ:name>submit.argument2</typ:name>
                               <typ:value/>
                            </typ:parameter>
                            <typ:parameter>
                               <typ:dataType>STRING</typ:dataType>
                               <typ:name>submit.argument3</typ:name>
                               <typ:value>VALIDATE</typ:value>
                            </typ:parameter>
                            <typ:parameter>
                               <typ:dataType>STRING</typ:dataType>
                               <typ:name>submit.argument4</typ:name>
                               <typ:value>[{'cash_advance_id':'300000011474085','status_code':'PAID'}]</typ:value>
                            </typ:parameter>
                         </sch:requestParameters>
                      </sch:submitRequest>
                   </soapenv:Body>
                </soapenv:Envelope>
                """;
    # Enviando Request para o Webservice e guardando a responsta
    resp = requests.post(url, headers=headers, data=payload, auth=HTTPBasicAuth('INT_SUPERBID', 'Intsuperbid2017'))
    print(resp.text);
    # Recuperando o conteudo da resposta e guardando em um dom
    dom = ElementTree.fromstring(resp.content)
    # Declarando as namespaces utilizadas
    namespaces = {
        'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
        'a': 'http://xmlns.oracle.com/scheduler'
    }
    # Recuperando valores por xpath
    resps = dom.findall(
        './soap:Body'
        '/a:submitRequestResponse'
        '/a:requestId',
        namespaces,
    )
    # Recuperand string em base64
    for resp in resps:
        requestId = resp.text;
        print(requestId);





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    call()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/