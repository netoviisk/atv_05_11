from django.db import models

class Usuario(models.Model):
    class Admin:
        pass

    def __str__(self):
        return self.email

    nome = models.CharField(maxlength=100)
    email = models.CharField(maxlength=100)
    senha = models.CharField(maxlength=100)


class Colecao(models.Model):
    class Admin:
        pass

    def __str__(self):
        return self.nome

    usuario_id = models.ForeignKey(Usuario)
    nome = models.CharField(maxlength=100)


class Livro(models.Model):
    class Admin:
        list_display = ('colecao_id', 'nome', 'capa', 'genero', 'autor', 'editora')
        list_filter = ['ano_public']
        search_fields = ['nome']

    def __str__(self):
        return self.nome

    colecao_id = models.ForeignKey(Colecao)
    nome = models.CharField(maxlength=100)
    capa = models.CharField(maxlength=100)
    genero = models.CharField(maxlength=100)
    autor = models.CharField(maxlength=100)
    editora = models.CharField(maxlength=100)
    ano_public = models.DateField('Ano de publicacao')


class Comentario(models.Model):
    class Admin:
        pass

    def __str__(self):
        return self.nome

    livro_id = models.ForeignKey(Livro)
    nome = models.CharField(maxlength=100)
    email = models.CharField(maxlength=100)
    site = models.CharField(maxlength=100)
    texto = models.TextField(maxlength=255)