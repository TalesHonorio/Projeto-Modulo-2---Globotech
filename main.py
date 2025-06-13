import csv
from analise.sistema import SistemaAnaliseEngajamento

def formatar_tempo(segundos):
    """
    Converte um valor em segundos para uma string legível no formato:
    'Xh Ymin Zs', 'Ymin Zs' ou 'Zs', dependendo do valor.
    """
    segundos = int(segundos)
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    seg = segundos % 60

    if horas > 0:
        return f"{horas}h {minutos}min {seg}s"
    elif minutos > 0:
        return f"{minutos}min {seg}s"
    else:
        return f"{seg}s"

def menu(sistema):
    """
    Menu principal com opções de relatórios formatados.
    """
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Métricas de Conteúdos")
        print("2 - Informações de Usuários")
        print("3 - Informações de Conteúdos")
        print("4 - Informações de Plataformas")
        print("5 - Listar Podcasts")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo...")
            break

        elif opcao == "1":
            menu_metricas(sistema)

        elif opcao == "2":
            # Mostra só os 5 usuários com mais interações
            print("\n=== TOP-5 USUÁRIOS ===")
            usuarios = sorted(
                sistema.listar_usuarios(),
                key=lambda u: len(u.interacoes_realizadas),
                reverse=True
            )[:5]
            for u in usuarios:
                total = len(u.interacoes_realizadas)
                print(f"ID: {u.id_usuario} | Interacoes: {total}")

        elif opcao == "3":
            # Mostra todos os conteúdos
            print("\n=== CONTEÚDOS ===")
            for c in sistema.listar_conteudos():
                print(f"ID: {c.id_conteudo} | Conteudo: {c.nome_conteudo}")

        elif opcao == "4":
            # Mostra todas as plataformas
            print("\n=== PLATAFORMAS ===")
            for p in sistema.listar_plataformas():
                print(f"ID: {p.id_plataforma} | Plataforma: {p.nome_plataforma}")

        elif opcao == "5":
            # Nova opção: listar podcasts com tipos de interação
            print("\n=== PODCASTS & INTERAÇÕES ===")
            podcasts = sistema.listar_conteudos_por_tipo("podcast")
            if not podcasts:
                print("Nenhum podcast encontrado.")
            for p in podcasts:
                print(f"\nPodcast: {p.nome_conteudo}")
                contagem = p.calcular_contagem_por_tipo_interacao()
                for tipo, qtd in contagem.items():
                    print(f"  {tipo.capitalize()}: {qtd}")

        else:
            print("Opção inválida. Tente novamente.")


def menu_metricas(sistema):
    """
    Submenu específico para métricas de engajamento de conteúdo,
    permitindo ao usuário escolher diferentes relatórios e visualizações.
    """
    while True:
        print("\n=== MENU DE MÉTRICAS ===")
        print("1 - Total de interações por conteúdo")
        print("2 - Contagem por tipo de interação para cada conteúdo")
        print("3 - Tempo total de visualização por conteúdo")
        print("4 - Média de tempo de visualização por conteúdo")
        print("5 - Listar comentários por conteúdo")
        print("6 - Top-5 conteúdos por total de interações")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma métrica: ")

        if opcao == "0":
            break

        # 1) Total de interações por conteúdo
        elif opcao == "1":
            print("\n=== TOTAL DE INTERAÇÕES POR CONTEÚDO ===")
            for c in sistema.listar_conteudos():
                total = c.calcular_total_interacoes_engajamento()
                print(f"{c.nome_conteudo} | Interações: {total}")

        # 2) Contagem por tipo
        elif opcao == "2":
            print("\n=== CONTAGEM POR TIPO DE INTERAÇÃO ===")
            for c in sistema.listar_conteudos():
                contagem = c.calcular_contagem_por_tipo_interacao()
                print(f"\n{c.nome_conteudo}:")
                for tipo, qtd in contagem.items():
                    print(f"  {tipo.capitalize()}: {qtd}")

        # 3) Tempo total de visualização
        elif opcao == "3":
            print("\n=== TEMPO TOTAL DE VISUALIZAÇÃO POR CONTEÚDO ===")
            for c in sistema.listar_conteudos():
                tempo = c.calcular_tempo_total_consumo()
                print(f"{c.nome_conteudo} | Tempo Total: {formatar_tempo(tempo)}")

        # 4) Média de tempo de visualização
        elif opcao == "4":
            print("\n=== MÉDIA DE TEMPO DE VISUALIZAÇÃO POR CONTEÚDO ===")
            for c in sistema.listar_conteudos():
                media = c.calcular_media_tempo_consumo()
                print(f"{c.nome_conteudo} | Tempo Médio: {formatar_tempo(media)}")

        # 5) Listar comentários
        elif opcao == "5":
            print("\n=== COMENTÁRIOS POR CONTEÚDO ===")
            for c in sistema.listar_conteudos():
                comentarios = c.listar_comentarios()
                if comentarios:
                    print(f"\n{c.nome_conteudo}:")
                    for texto in comentarios:
                        print(f"  - {texto}")

        # 6) Top-5 conteúdos
        elif opcao == "6":
            print("\n=== TOP-5 CONTEÚDOS POR INTERAÇÕES ===")
            top5 = sorted(
                sistema.listar_conteudos(),
                key=lambda c: c.calcular_total_interacoes_engajamento(),
                reverse=True
            )[:5]
            for c in top5:
                total = c.calcular_total_interacoes_engajamento()
                print(f"{c.nome_conteudo} | Interações: {total}")

        else:
            print("Opção inválida. Tente novamente.")

def main():
    """
    Ponto de entrada do script:
    - Instancia o sistema de análise
    - Processa o CSV de interações
    - Inicia o menu de interação com o usuário
    """
    sistema = SistemaAnaliseEngajamento()
    sistema.processar_interacoes_do_csv("interacoes_globo.csv")
    menu(sistema)

if __name__ == "__main__":
    main()
