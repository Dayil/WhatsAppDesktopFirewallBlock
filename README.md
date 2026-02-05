# 🛡️ A Muralha do Silêncio: WhatsApp Firewall Control

> *"A verdadeira liberdade digital não é estar sempre conectado, mas escolher quando se desconectar."*

## 📜 Introdução

Seja bem-vindo ao **Santuário do Foco**. Este repositório abriga o `WhatsAppBlock.py`, uma ferramenta tática de defesa contra a interrupção perpétua. Em um mundo onde notificações clamam por atenção a cada segundo, este código devolve a você o controle soberano sobre o seu tempo.

Este projeto não é apenas um bloqueador; é um interruptor de fluxo de dados. Ele permite que você opere em "Deep Work" (Trabalho Profundo) no seu computador, cortando a comunicação do WhatsApp Desktop com a internet, sem a necessidade de fechar o aplicativo ou desligar o Wi-Fi. Você aparecerá offline, mas seu foco estará online.

## ⚙️ Arquitetura, Funcionalidades e O Mecanismo

O sistema foi forjado para ser simples na superfície, mas poderoso nas profundezas do sistema operacional. Suas engrenagens principais incluem:

*   **Interface de Comando Visual (`Tkinter`)**: O script materializa um painel de controle minimalista. Sem configurações complexas, apenas dois caminhos claros: Bloquear (Vermelho) e Liberar (Verde). O status é atualizado em tempo real, servindo como um farol do estado da sua conexão.
*   **O Mensageiro do Sistema (`Subprocess` & `PowerShell`)**: O código Python atua como um general que envia ordens diretas ao núcleo do Windows. Ele manipula as regras de Firewall nativas (`New-NetFirewallRule`), garantindo que o bloqueio seja feito no nível da infraestrutura de rede, e não apenas cosmético.
*   **Mira Laser (`Package Family ID`)**: Diferente de soluções brutas que cortam toda a internet, este script utiliza o identificador genético do aplicativo (`5319275A.WhatsAppDesktop...`). Isso garante uma precisão cirúrgica: apenas o WhatsApp é silenciado; seu navegador, Spotify e e-mails continuam fluindo livremente.
*   **Persistência de Estado**: Ao iniciar, o programa consulta o Windows para saber se as barreiras já estão erguidas, informando imediatamente se o Firewall já está bloqueado ou liberado.

## 💻 Rituais de Execução

Para invocar esta barreira digital e retomar sua produtividade, siga os passos abaixo com atenção.

**⚠️ Aviso Importante:** Como este script manipula o Firewall do Windows, ele exige **Privilégios de Administrador**.

1.  Certifique-se de que o **Python 3.x** esteja instalado em seus domínios.
2.  Este script utiliza apenas as bibliotecas sagradas padrão do Python (`tkinter`, `subprocess`), portanto, nenhuma instalação via `pip` é necessária.
3.  Abra o seu terminal (CMD ou PowerShell) **como Administrador**.
    *   *Clique com botão direito no ícone do terminal > Executar como Administrador.*
4.  Navegue até o diretório onde o script descansa.
5.  Execute o comando de invocação:

    ```bash
    python WhatsAppBlock.py
    ```

6.  A janela de controle surgirá.
    *   Clique em **🔒 Bloquear WhatsApp** para erguer a muralha.
    *   Clique em **🔓 Liberar WhatsApp** para derrubar os portões e permitir o fluxo de mensagens.

## 📋 Requisitos do Sistema

*   **Sistema Operacional**: Windows 10 ou Windows 11 (O script depende do PowerShell e da estrutura de Apps da Microsoft Store).
*   **Alvo**: WhatsApp Desktop (Versão da Microsoft Store).
*   **Permissão**: Acesso de Administrador (Obrigatório para alterar regras de Firewall).
*   **Operador**: Alguém cansado de notificações e pronto para assumir o controle da sua própria atenção.

---

### 🛠️ Solução de Problemas Comuns

*   **"Erro de Permissão/Acesso Negado"**: O Windows protege o Firewall. Se você não rodar o terminal/script como Administrador, o feitiço falhará.
*   **"O WhatsApp continua funcionando"**: O script busca o WhatsApp instalado via Microsoft Store. Se você usa o `.exe` antigo (Win32) baixado do site, o `PackageFamilyName` será diferente.

---

**Autor:** [Daniel "Dayil" Marfim](https://github.com/Dayil/Dayil)
**Data:** 2026
