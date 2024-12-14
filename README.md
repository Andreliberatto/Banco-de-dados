E aí, pessoal! Aqui está a explicação do sistema de registro de ponto que eu, André Amorim Liberatto, desenvolvi para um treinamento python. Esse projeto foi criado em Python, com a interface gráfica feita no tkinter e utilizando o banco de dados SQLite para armazenar tudo. Ele serve para gerenciar as entradas e saídas dos funcionários de forma simples e eficiente, com a possibilidade de exportar os logs para CSV e até adicionar departamentos na hora!

### Funcionalidades Principais
- **Registrar Ponto**: O usuário só precisa inserir o nome e escolher o departamento. O sistema registra automaticamente a data e hora. Se o funcionário já tiver registrado entrada no dia, ele só atualiza a saída; caso contrário, é registrado o horário de entrada.
  
- **Visualizar Logs**: Uma tabela interativa mostra todos os registros de entrada e saída, atualizados em tempo real.

- **Exportar Logs**: Os registros podem ser exportados para um arquivo CSV, facilitando o acompanhamento e análise em planilhas.

- **Adicionar Departamentos**: Novos departamentos podem ser adicionados ao sistema sem necessidade de reiniciar o programa.

### Estrutura do Código
- **Banco de Dados**: Utilizei o SQLite, que é bem prático e não exige servidor dedicado. Ele armazena os registros na tabela `logs`, com informações como id, nome do funcionário, departamento, data, hora de entrada e hora de saída.
  
- **Interface Gráfica**: A interface foi desenvolvida no tkinter, com componentes como campos para nome, seleção de departamento e botões para registrar ponto e exportar os logs. A tabela de logs é exibida diretamente na tela.
  
- **Estilo e Organização**: A classe `ttk.Style` foi usada para melhorar a estética da aplicação, e a estrutura do código é bem modular, com funções específicas para cada tarefa, como `registrar_ponto`, `atualizar_logs` e `exportar_csv`.

### Fluxo do Sistema
1. O usuário insere o nome e escolhe o departamento.
2. Clica em "Registrar Ponto" e, dependendo da situação, o sistema registra a entrada ou a saída.
3. Os dados são armazenados no banco de dados e exibidos na tabela.
4. Os logs podem ser exportados para CSV para facilitar consultas posteriores.

### Tecnologias Utilizadas
- **Python**: Linguagem principal.
- **tkinter**: Para a interface gráfica.
- **sqlite3**: Para o banco de dados.
- **csv**: Para exportação de dados.
- **datetime**: Para manipulação de data e hora.

### Possíveis Melhorias
- **Autenticação**: Uma camada extra de segurança para o registro de ponto.
- **Filtros de Logs**: Permitir filtrar por data ou funcionário.
- **Relatórios**: Gerar relatórios mais detalhados, como gráficos ou PDFs.
- **Interface Responsiva**: Usar bibliotecas como CustomTkinter para tornar a interface ainda mais moderna e responsiva.

Este é um projeto em constante evolução, e logo ele terá mais funcionalidades (ou não)!
