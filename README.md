### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Pycharm](https://www.sublimetext.com/). 
Além disto é bom ter um editor para trabalhar com o código como [Sublime](https://www.sublimetext.com/). Além 
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

# Instale as dependências
$ npm install

# Execute a aplicação em modo de desenvolvimento
$ npm run dev:server

# O servidor inciará na porta:3333 - acesse http://localhost:3333 

```
<p align="center">
  <a href="https://github.com/tgmarinho/README-ecoleta/blob/master/Insomnia_API_Ecoletajson.json" target="_blank"><img src="https://insomnia.rest/images/run.svg" alt="Run in Insomnia"></a>
</p>
