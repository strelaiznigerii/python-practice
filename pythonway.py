### скрипт для записи успеха в python

class Comment():

    def __init__(self) -> None:
        self.info = self.input_info()    

    def input_info(self) -> str:
        self.info = input('Опишите то, что сделано')


def main():
    c = Comment()
    print(c.info)    

if __name__ == '__main__':
    main()
