from core.assistant import ask_stilgar


def main():
    print("[Stilgar]: Saudações! Pergunte algo ou digite 'sair' para encerrar.\n")

    while True:
        try:
            user_input = input("[Você] > ").strip()
            if user_input.lower() in ["sair", "exit"]:
                print("Encerrando conversa com Stilgar.")
                break

            response = ask_stilgar(user_input)
            print(f"[Stilgar] > {response}\n")

        except KeyboardInterrupt:
            print("\nEncerrando conversa com Stilgar.")
            break
        except Exception as e:
            print(f"[Erro] > {str(e)}")


if __name__ == "__main__":
    main()
