from .utils import save_max_page_number


def main():
    while True:
        try:
            print("Max Page Number of EorzeaDatabase", end=" [int]: ")
            raw = input()
            num = int(raw)
            save_max_page_number(num)
            break
        except Exception:
            pass
