docstring = (f"""
📊 AUTOMAÇÃO COMPLETA PARA WHATSAPP DE ANÁLISE E GERAÇÃO DE RELATÓRIO ANALÍTICO DE CLIENTES📊📲

════════════════════════════════════════════
📌 VISÃO GERAL DO PROJETO
════════════════════════════════════════════
\n Esta automação foi desenvolvida com o objetivo de transformar uma base de dados de clientes
em informações estratégicas claras, organizadas e prontas para análise e comunicação.

O fluxo automatizado realiza desde a leitura da base até a geração de relatórios analíticos
estruturados e formatados com destaque visual no terminal, permitindo acompanhamento do
crescimento da empresa, identificação de padrões e suporte direto à tomada de decisões.

Além da análise, o projeto também permite integração com automações de envio de mensagens
e comunicação corporativa.

════════════════════════════════════════════
📚 BIBLIOTECAS UTILIZADAS E FINALIDADES
════════════════════════════════════════════

• os💻
Responsável pela manipulação de diretórios e arquivos do sistema operacional;
Permite localizar bases de dados, acessar pastas do projeto e garantir execução correta
independente do ambiente.

• cores🎨 (arquivo criado pelo próprio projeto)
Centraliza códigos ANSI para estilização do terminal;
Padroniza cores, negrito e resets visuais;
Melhora leitura dos relatórios e apresentação em prints.

• pandas🐼
Principal biblioteca de manipulação e análise de dados;
Responsável pela leitura de arquivos CSV ou Excel;
Criação e tratamento de DataFrames;
Filtragem, cálculos estatísticos e geração de métricas analíticas.

• pyautogui 🧭
Automação de interações com teclado e mouse;
Permite automatizar envio de mensagens e execução de tarefas repetitivas.

• pyperclip 📋
Gerenciamento de área de transferência;
Auxilia na automação copiando textos e mensagens para envio automático.

• openpyxl (uso opcional) 📈
Utilizada quando a base estiver em formato Excel (.xlsx);
Permite leitura e manipulação de planilhas estruturadas.

════════════════════════════════════════════
⚙️ PASSO A PASSO DA AUTOMAÇÃO:
════════════════════════════════════════════

1️⃣ Estruturação do Projeto:
Organização das pastas e arquivos 📂;
Criação do módulo de cores🎨;
Posicionamento da base de dados no diretório correto📊.

2️⃣ Importação das Bibliotecas📚:
Carregamento das ferramentas necessárias para automação,
tratamento de dados, estilização e interação com o sistema.

3️⃣ Carregamento da Base:
Leitura do CSV ou Excel utilizando pandas🐼.

4️⃣ Limpeza e Padronização:
Tratamento de valores nulos;
Conversão de datas;
Padronização de nomes de colunas;
Preparação para análise.

5️⃣ Processamento Analítico:
Identificação de novos clientes;
Cálculo do total da base;
Descoberta do país mais recorrente;
Análise de domínios e sites;
Extração de indicadores estratégicos.

6️⃣ Construção do Relatório:
Montagem de mensagem analítica estruturada;
Inserção dinâmica das métricas calculadas;
Separação por seções informativas.

7️⃣ Estilização Visual:
Aplicação de negrito;
Uso de cores diferentes para métricas;
Melhoria da experiência visual em terminal.

8️⃣ Automação de Comunicação:
Cópia do relatório para área de transferência;
Envio automatizado por ferramentas externas.

9️⃣ Execução Final:
Exibição do relatório no terminal;
Registro das informações analisadas;
Base pronta para dashboards ou integrações futuras.

════════════════════════════════════════════
🎯 IMPORTÂNCIA DO PROJETO:
════════════════════════════════════════════

🎯 Automatiza tarefas repetitivas e reduz esforço manual;
🎯 Diminui falhas humanas durante análises;
🎯 Padroniza geração de relatórios estratégicos;
🎯 Aumenta velocidade de interpretação dos dados;
🎯 Facilita comunicação entre equipes;
🎯 Incentiva decisões orientadas por dados;
🎯 Permite escalabilidade para novos relatórios;
🎯 Cria base sólida para automações empresariais maiores;
🎯 Melhora visualização e apresentação de resultados;
🎯 Integra análise de dados com automação operacional.

════════════════════════════════════════════
🚀 RESULTADO ESPERADO:
════════════════════════════════════════════

Uma automação robusta capaz de:\n
✅ Ler bases de clientes automaticamente;
✅ Gerar métricas estratégicas relevantes;
✅ Construir relatórios claros e visualmente organizados;
✅ Automatizar comunicação de resultados;
✅ Apoiar decisões estratégicas com rapidez e precisão.\n""")

print(docstring.expandtabs(4))