class FilePile:
    __contenu = []
    def __init__(self, le_contenu=None):
        if le_contenu is None:
            le_contenu = []
        self.__contenu = le_contenu

    def accesTete(self):
        if len(self.__contenu) == 0:
            return None
        return self.__contenu[0]
    def accesSommet(self):
        if len(self.__contenu) == 0:
            return None
        return self.__contenu[-1]

    def defiler(self):
        if len(self.__contenu) == 0:
            return None
        self.__contenu = self.__contenu[1:]

    def depiler(self):
        if len(self.__contenu) == 0:
            return None
        self.__contenu = self.__contenu[:-1]

    def rempiler(self, unElement):
        self.__contenu.append(unElement)

    def __len__(self):
        return len(self.__contenu)
    def __repr__(self):
        return "Cette pile contient : " + ", ".join([str(e) for e in self.__contenu])

