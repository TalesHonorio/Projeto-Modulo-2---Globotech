import csv
from analise.sistema import SistemaAnaliseEngajamento

def formatar_tempo(segundos):
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
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Métricas de Conteúdos")
        print("2 - Informações de Usuários")
        print("3 - Informações de Conteúdos")
        print("4 - Informações de Plataformas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo...")
            break

        elif opcao == "1":
            menu_metricas(sistema)

        elif opcao == "2":
            sistema.gerar_relatorio_atividade_usuarios(top_n=5)

        elif opcao == "3":
            print("\nTotal de conteúdos:", len(sistema._SistemaAnaliseEngajamento__conteudos_registrados))
            for c in list(sistema._SistemaAnaliseEngajamento__conteudos_registrados.values())[:5]:
                print(f"- {c.nome_conteudo} (ID: {c.id_conteudo})")

        elif opcao == "4":
            print("\nTotal de plataformas:", len(sistema._SistemaAnaliseEngajamento__plataformas_registradas))
            for p in sistema.listar_plataformas():
                print(f"- {p.nome_plataforma}")

        else:
            print("Opção inválida. Tente novamente.")

def menu_metricas(sistema):
    while True:
        print("\n=== MENU DE MÉTRICAS ===")
        print("1 - Total de interações por conteúdo")
        print("2 - Contagem por tipo de interação para cada conteúdo")
        print("3 - Tempo total de visualização por conteúdo")
        print("4 - Média de tempo de visualização por conteúdo")
        print("5 - Listar comentários por conteúdo")
        print("6 - Top-5 conteúdos com mais visualizações")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma métrica: ")

        if opcao == "0":
            break

        elif opcao == "1":
            sistema.gerar_relatorio_engajamento_conteudos()

        elif opcao == "2":
            for c in sistema._SistemaAnaliseEngajamento__conteudos_registrados.values():
                print(f"\n{c.nome_conteudo}:")
                contagem = c.contar_tipos_interacao()
                for tipo, qtd in contagem.items():
                    print(f"  {tipo}: {qtd}")

        elif opcao == "3":
            for c in sistema._SistemaAnaliseEngajamento__conteudos_registrados.values():
                tempo = c.calcular_tempo_total_consumo()
                print(f"{c.nome_conteudo}: {formatar_tempo(tempo)}")

        elif opcao == "4":
            for c in sistema._SistemaAnaliseEngajamento__conteudos_registrados.values():
                media = c.calcular_media_tempo_consumo()
                print(f"{c.nome_conteudo}: {formatar_tempo(media)}")

        elif opcao == "5":
            for c in sistema._SistemaAnaliseEngajamento__conteudos_registrados.values():
                comentarios = c.listar_comentarios()
                if comentarios:
                    print(f"\nComentários em {c.nome_conteudo}:")
                    for texto in comentarios:
                        print(f"  - {texto}")

        elif opcao == "6":
            sistema.identificar_top_conteudos(metrica="visualizacoes", n=5)

        else:
            print("Opção inválida. Tente novamente.")

def main():
    sistema = SistemaAnaliseEngajamento()
    sistema.processar_interacoes_do_csv("interacoes_globo.csv")
    menu(sistema)

if __name__ == "__main__":
    main()
