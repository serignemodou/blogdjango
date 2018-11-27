from django.http import Http404

class Article():
    ARTICLE=[
       {'id': 1, 'title': 'article de sport', 'body': 'sadio meilleur joueur'},
       {'id': 2, 'title': 'article politique', 'body': 'abdallah rassure macky'},
       {'id': 3, 'title': 'article social', 'body': 'insecurite dans le pays'},
       {'id': 4, 'title': 'article press', 'body': 'une arme de la demoncratie'},
    ]
    @classmethod
    def all(cls):
        return cls.ARTICLE

    @classmethod
    def findId(cls,id):
        try:
            return cls.ARTICLE[int(id)-1]
        except:
            raise Http404("Désole article {} n'existe pas".format(id))     

          

    