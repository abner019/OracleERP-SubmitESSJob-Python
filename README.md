### Como Submeter um Scheduled Processes (ESSJOB) por Web Services utilizando Python
Os ESSJobs são programas baseados em PL/SQL, Relatórios BIP, Host, SQL Loader e outras tecnologias para executar lógica de negócios. Existem muitos  ESS padrão/semeados disponíveis no Oracle Fusion e muitas vezes é preciso disparar um processo através de um script ou integração.

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Pycharm](https://www.sublimetext.com/). Além 
de tambem ter acesso a um ambiente Oracle ERP Cloud 

#### Submetendo um ESSJob no Oracle

```bash

# Dentro do Oracle Erp Cloud:
 -> Localize o ESSJOB 
 -> Submeta

# Recupere as informações de definição do Job com a query abaixo:

select DEFINITION, APPLICATION 
  from FUSION.ESS_REQUEST_HISTORY 
  where requestid=4082803

# Recupere as informações de parametros/valores
select NAME,DATATYPE,VALUE
  from FUSION.ESS_REQUEST_PROPERTY
  where requestid=4082803
    and name like 'submit%'

# Com as informacoes em mãos, preencha o seu payload:
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
  

# Adicione as Informacoes das informações no script:
 -> url: enpoint do serviço
 -> userName: usuario
 -> pwd: senha

# Execute o script, e aguarde um resposta identica a essa:

<env:Envelope xmlns:env="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing">
   <env:Header>
      <wsa:Action>submitRequest</wsa:Action>
      <wsa:MessageID>urn:uuid:de3b8096-6576-4fef-a254-797e56ce29a4</wsa:MessageID>
      <wsa:RelatesTo>urn:uuid:f1d875e4-d718-40ba-9a8e-65733cf0733f</wsa:RelatesTo>
   </env:Header>
   <env:Body>
      <ns0:submitRequestResponse xmlns:ns0="http://xmlns.oracle.com/scheduler">
         <requestId xsi:type="xsd:long" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">4082803</requestId>
      </ns0:submitRequestResponse>
   </env:Body>
</env:Envelope>



