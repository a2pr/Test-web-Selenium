Dia 8/02/2020

# Meta do curso:
[ementa](\screenshots\ementa.jpg)

# Testes de Aplicaoes Web

## Revisao de tecnicas

### Tecnica particao de equivalencia

Agrupar os casos de sucesso e error em um  teste que atende cada caso.

### Analise de Valor Limite

Provar valores iguais ou pertos ao limite.

### Grafo Causa e Efeito

Usando tabela da verdade e usando os valores de entrada considerar as posibilidades.

### Transicao de Estados

## Desafios de teste para aplicacoes Web

* Base de usurios grande e variada
* Ambiente de negocios
* Usabilidade
*  Localidades
*  Seguranca
*  Desempenho
*  Disponibilidade
*  Conectividade
*  Portabilidade

# Automacao de testes

## Sofware

Execucao de casos de testes reduzindo o tempo de execucao.

1. Como automatizar?
    * Planejamento e escencial. 
    * A automatacao de testes permitem livrar o tempo do testador para se dedicar a outras areas de beneficio ao software.
    * E necesario ter um ambiente separado de desenvolvimiento. 
    * E necesario escolher as ferramentas adequadas para um bom ambiente de automatacao

## Entradas e saidas do processo de automacao de testes

* entrada
  * Requisitos
  * Codigo/fonte executavel
  * Ambiente para teste
  * Dados
* Saidas
  * Resultado de teste
  * Relatorios
  * Bugs

## Elementos da automacao de testes

* Gravador
  
    Gravacao de as ascoes que serao aplicadas
* Executor de testes

    Casos de testes 
* Ponto de verificacao

    Regla de validacao do caso de teste
* Tempo para pensar
  
    Tempo de espera de execucao de uma acao e outra
* Conceitos de programacao 
* Dados de testes utilizados
* Resultados
* Fontes

    Versao do software testada.
* Executaveis
* Controle dos defeitos
  
    Registro dos bugs encontrados
* Documentacao
    * Requisitos, casos de teste relatorio de execucao
* Script de teste
  
    Arquivos gerados pela ferramenta de automacao de testes. 
## Arquitetura
Automatacao precisa estar na arquitetura do software
Fornece um foco de controle para o software

## Vantagens

* Executar a maior quantidades de testes em tempo reduzido
* Relatorios gerados automaticamente
* Testes repetitivos excutados totalmente
* Seguranca na execucao, reusabilidade de teste, manutenbilidade e historico
* Executar mais posibilidades de daados de entrada
* validacao da interface
* Foco nas regras de negocio do cliente

## Boas Praticas

* Ferramentas compativeis com o ambiente
* planejar ambete de automatacao 
* Encare automatacao 
* Integracao Continua / Entraga Continua


# Automatacao de teste de software no ambiente Agil

## Conceito

* Teste funcao para prevenir falhas.
* Testadores precisam ser proativos
* Automacao de teste e considerada a atividade chave para metodos ageis 

## Quadrantes do Teste Agil

##Pirami de Mike Cohn

    Testes de GUI < Testes de Api < Testes unitarios

# Selenium

Ferramenta de testes de sistema para aplicacoes web.
## Selenium IDE 
plugin de chrome de selenium. Interface grava as acoes do usuario. 

### Comandos

* Actions: Manipular o estado do aplicativo
* Accessors: Examinam o estado da aplicacao e armaenam os resultados.
* Assertions: verificam o estado da aplicacao esta em conformidade com o que se espera. 
* Open
* click/clickAndWait
* verifyTitle/assertTitle
* verifyTextPresent
* verifyElementPresent
* verifyText
* verifyTable
* waitforPageToLoad
* waitForElementPresent

### Diferenca entre Selenium IDE e Webdriver

### XPath 

Linguagem de consulta para selecionar nos de um documento

* Sintax
    tag[@attr='valor'] seleccao do tag com essas configuracoes
    tag: input
    @attr: attributo
* Contains()
  * ex: [contains(text(), ""here)]
## configuration for running chrometest
*   Get corresponding [driver](https://chromedriver.chromium.org/downloads) for chrome
*   config for:
       self.driver = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
## test in python
    
    python {fileTestName}
    pytest --html={fileReportName}.html {fileTestName}
    
For getting elements first we should get the id or the xpath
We can get most of the test step via Sellenium IDEm but is need to make some changes to make it work normally. Autocomplete is one example of this.

crobpath to get values for xpath

link with final [script](http://dontpad.com/automacaoweb_fev20)