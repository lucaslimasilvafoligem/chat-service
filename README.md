# Bot de Atendimento para WhatsApp

Esse projeto é um bot funcional para WhatsApp, desenvolvido para realizar funções básicas de automação de mensagens, armazenamento de notificações dos clientes e respostas automáticas. Atualmente, ele opera com uma lógica simples, mas tem grande potencial de aprimoramento, como a incorporação de técnicas de IA, PLN e Machine Learning para torná-lo mais poderoso e responsivo.

Com mais refinamento, este bot pode evoluir para um microserviço independente, capaz de interagir com clientes, agendar consultas e oferecer muitas outras possibilidades.

---

## **Estrutura do Projeto**

- **`infos_gerais/`**
  - Contém um arquivo `bot_whats.txt` explicando de forma geral as ferramentas e tecnologias utilizadas no desenvolvimento do chatbot.

- **`build/`**
  - Diretório com arquivos essenciais para instalação de dependências e realização de testes:
    - `bibliotecas.txt`: Lista das dependências necessárias.
    - `download_chromeDrive.py`: Código Python para baixar o WebDriver para distribuições Linux.
    - `teste.py`: Script de teste básico.

- **`bot.py`**
  - Arquivo principal contendo o código funcional do bot. Inclui comentários para facilitar o entendimento. 
  - **Funcionalidades principais**:
    - Simulação de envio de mensagens automáticas.
    - Integração simulada com uma API externa para enviar dados e interagir com mensagens.
    - Configuração específica para Linux e versões do Google Chrome.

- **`mensagem.txt`**
  - Arquivo de texto com mensagens automáticas padrão que o bot pode enviar.

- **`build.sh`**
  - Script para preparar o ambiente, instalar dependências e realizar testes básicos.

---

## **Como Configurar o Ambiente**

1. **Pré-requisitos**
   - Certifique-se de ter o Python instalado na sua máquina.
   - Instale o WebDriver correspondente à sua versão do Google Chrome (veja instruções abaixo).
   - Conceda permissões de execução ao arquivo `build.sh`:
     ```bash
     chmod +x build.sh
     ```

2. **Executar o Script de Configuração**
   - No terminal, rode o comando:
     ```bash
     ./build.sh
     ```
   - O script instalará as dependências listadas em `bibliotecas.txt` e executará o teste inicial.

3. **Instalar o WebDriver (para Linux)**
   - **Automático (Linux)**: Caso utilize Linux, você pode descomentar a chamada no `build.sh` que executa o script `download_chromeDrive.py`.
   - **Manual**: Siga este tutorial para instalar manualmente o WebDriver: [YouTube Tutorial](https://www.youtube.com/watch?v=FT0cWOUkCzI).
   - Certifique-se de que o executável do WebDriver esteja na raiz do projeto.

4. **Configurar a API Gerenciadora de Interações**
   - O bot usa uma API para gerar os caminhos das interações do Selenium. 
   - Faça o cadastro em [EditaCódigo](https://editacodigo.com.br/login.php).
   - Insira o token gerado na parte de configuração do bot (`<Seu_codigo>` no `bot.py`).

---

## **Observações e Possíveis Modificações**

- As sessões do WhatsApp são salvas automaticamente para facilitar o uso. Caso isso não seja desejado, é possível desativar esse comportamento no código.
- O bot, na parte "agente", está configurado para uma versão específica do Google Chrome e pode precisar de ajustes caso sua configuração local seja diferente.
- WhatsApp pode modificar frequentemente a estrutura de CSS/HTML, dificultando o uso de bots. Caso isso aconteça, inspecione a página e atualize os seletores no código do bot.
- A mensagem automática é carregada a partir do arquivo `mensagem.txt`, mas pode ser integrada a uma API para maior flexibilidade.

---

## **Potencial de Expansão**
Com técnicas de IA, PLN e Machine Learning, este chatbot pode ser aprimorado para:
- Reconhecer intenções nas conversas.
- Responder de maneira mais personalizada.
- Interagir com diferentes APIs.
- Atuar como um agente inteligente para microserviços.

---

## **Contribuição**
Contribuições são bem-vindas! Caso encontre algum problema ou tenha sugestões de melhoria, fique à vontade para abrir uma issue ou enviar um pull request.

---

**Autor:** Lucas Silva  
**Contato:** [GitHub](https://github.com/lucaslimasilvafoligem)
