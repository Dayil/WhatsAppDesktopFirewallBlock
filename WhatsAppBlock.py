# WhatsApp Firewall Control
# Autor: [Daniel "Dayil" Marfim]

# Esse script permite bloquear ou liberar o WhatsApp Desktop usando regras de firewall do Windows.
# Cansou de ser interrompido por notificações ou quer garantir que o WhatsApp só funcione quando você quiser?
# Este programa é para você! Você vai aparecer como se não estivesse receber mensagens.
# Ele cria regras específicas para o aplicativo, garantindo que apenas o WhatsApp seja afetado.

# Importando as ferramentas que vamos usar (como se fosse pegar martelo e pregos na caixa de ferramentas)
import tkinter as tk
import subprocess  # Ferramenta para mandar comandos para o "cérebro" do Windows
from tkinter import messagebox

# =========================
# CONFIGURAÇÕES
# =========================
# Este código longo é o "RG" do WhatsApp no Windows. É um identificador único.
# O Windows precisa dele para saber exatamente qual aplicativo bloquear, sem confundir com outros.
PACKAGE_FAMILY = "5319275A.WhatsAppDesktop_cv1g1gvanyjgm"
# Nome que daremos para a regra de SAÍDA (dados saindo do seu computador para a internet).
RULE_OUT = "WhatsApp"
# Nome que daremos para a regra de ENTRADA (dados vindo da internet para o seu computador).
RULE_IN = "WhatsApp_IN"


# =========================
# FUNÇÕES DE SISTEMA
# =========================
def run_ps(command):
    # Esta função é o mensageiro. Ela pega o nosso pedido e entrega para o Windows (PowerShell) executar.
    # O "creationflags" serve para não ficar abrindo aquelas janelas pretas chatas na tela.
    subprocess.run(
        ["powershell", "-Command", command],
        check=True,
        creationflags=subprocess.CREATE_NO_WINDOW
    )


def regra_existe(nome):
    # Aqui o programa pergunta para o Windows: "Ei, você já tem uma regra com esse nome anotada aí?"
    cmd = f'Get-NetFirewallRule -DisplayName "{nome}" -ErrorAction SilentlyContinue'
    result = subprocess.run(
        ["powershell", "-Command", cmd],
        capture_output=True,
        text=True,
        creationflags=subprocess.CREATE_NO_WINDOW
    )
    return result.stdout.strip() != ""


def criar_regras_se_necessario():
    # Se o Windows disser "Não conheço essa regra", esta função cria ela.
    try:
        # Verifica e cria a regra de SAÍDA (Outbound) - O que sai do seu PC para a internet
        if not regra_existe(RULE_OUT):
            run_ps(
                f'New-NetFirewallRule '
                f'-DisplayName "{RULE_OUT}" '
                f'-Direction Outbound '
                f'-Action Allow '
                f'-PackageFamilyName "{PACKAGE_FAMILY}"'
            )

        # Verifica e cria a regra de ENTRADA (Inbound) - O que vem da internet para o seu PC
        if not regra_existe(RULE_IN):
            run_ps(
                f'New-NetFirewallRule '
                f'-DisplayName "{RULE_IN}" '
                f'-Direction Inbound '
                f'-Action Allow '
                f'-PackageFamilyName "{PACKAGE_FAMILY}"'
            )
    except Exception as e:
        messagebox.showerror("Erro ao criar regras", str(e))


# =========================
# AÇÕES (O que os botões fazem)
# =========================
def bloquear():
    # Quando clicamos em "Bloquear", ele garante que as regras existem e muda elas para "Block" (Bloquear).
    try:
        criar_regras_se_necessario()
        run_ps(f'Set-NetFirewallRule -DisplayName "{RULE_OUT}" -Action Block')
        run_ps(f'Set-NetFirewallRule -DisplayName "{RULE_IN}"  -Action Block')
        status.config(text="🔒 WhatsApp BLOQUEADO (IN + OUT)", fg="red")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def liberar():
    # Quando clicamos em "Liberar", ele muda as regras para "Allow" (Permitir).
    try:
        criar_regras_se_necessario()
        run_ps(f'Set-NetFirewallRule -DisplayName "{RULE_OUT}" -Action Allow')
        run_ps(f'Set-NetFirewallRule -DisplayName "{RULE_IN}"  -Action Allow')
        status.config(text="🔓 WhatsApp LIBERADO (IN + OUT)", fg="green")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


# =========================
# VERIFICAÇÃO DE STATUS
# =========================
def verificar_status_inicial():
    # Verifica o estado atual da regra de firewall ao iniciar o programa.
    try:
        # Garante que as regras existam antes de verificar. Se não existirem,
        # serão criadas com a ação padrão "Allow" (Liberado).
        criar_regras_se_necessario()

        # Comando para pegar a ação (Allow/Block) da regra de saída.
        cmd = f'(Get-NetFirewallRule -DisplayName "{RULE_OUT}").Action'
        result = subprocess.run(
            ["powershell", "-Command", cmd],
            capture_output=True,
            text=True,
            check=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        
        action = result.stdout.strip()

        # Atualiza a interface com base na ação encontrada.
        # Verifica se a palavra "Block" (Bloquear) está na resposta do Windows.
        # Usamos "in" porque às vezes o Windows devolve o texto com espaços ou múltiplas linhas.
        if "Block" in action:
            status.config(text="🔒 WhatsApp BLOQUEADO (IN + OUT)", fg="red")
        else:
            status.config(text="🔓 WhatsApp LIBERADO (IN + OUT)", fg="green")

    except Exception as e:
        # Se ocorrer um erro (ex: falta de permissão de administrador), informa o usuário.
        status.config(text="⚠️ Status desconhecido", fg="orange")
        messagebox.showwarning("Falha na Verificação", f"Não foi possível verificar o status inicial. Tente executar como administrador.\n\nDetalhes: {e}")


# =========================
# INTERFACE (O desenho da janela)
# =========================
# Cria a janela principal
root = tk.Tk()
root.title("WhatsApp Firewall Control")
root.geometry("400x260")
root.resizable(False, False) # Impede de esticar a janela

titulo = tk.Label(
    root,
    text="Controle de Firewall do WhatsApp",
    font=("Segoe UI", 15, "bold")
)
titulo.pack(pady=15)

status = tk.Label(
    root,
    text="Estado desconhecido",
    font=("Segoe UI", 12)
)
status.pack(pady=10)

# Botão Vermelho (Bloquear)
btn_block = tk.Button(
    root,
    text="🔒 Bloquear WhatsApp",
    font=("Segoe UI", 11),
    width=30,
    height=2,
    command=bloquear
)
btn_block.pack(pady=6)

# Botão Verde (Liberar)
btn_allow = tk.Button(
    root,
    text="🔓 Liberar WhatsApp",
    font=("Segoe UI", 11),
    width=30,
    height=2,
    command=liberar
)
btn_allow.pack(pady=6)

# Roda a verificação de status assim que a janela é criada
verificar_status_inicial()

# Mantém a janela aberta esperando você clicar em algo
root.mainloop()