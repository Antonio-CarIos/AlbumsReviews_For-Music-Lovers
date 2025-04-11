from django.db import models

class List(models.Model):
    name_list = models.CharField(max_length=250)
    mini_description = models.CharField(max_length=300)
    user = models.ForeignKey("core.Perfil", on_delete=models.CASCADE, related_name='lists')
    albums = models.ManyToManyField("music.Album", related_name='in_list')

    def __str__(self):
        return f"{self.name_list} - {self.user.nickname}"
    