class Player(object):
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
    def __str__(self):
        a = self.name + ":\t" + str(self.score)
        return a

def ask_yes_no(q):
    response = None
    while response not in ("yes", "no"):
        response = input(q).lower()
    return response

def ask_number(q, l, h):
    response = None
    while response not in range(l, h):
        response = int(input(q))
    return response

if __name__ == "__main__":
    print("Вы запустили этот модуль на прямую, а не импортировали его")
    print('ПРоверка')