from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from django.utils import timezone

class NiveisAcesso(models.Model):
    nome = models.CharField(max_length=20, null=False)

class Usuarios(models.Model):
    matricula = models.CharField(max_length=20, null=False)
    cpf = models.CharField(max_length=11, null=False, unique=True)
    nome = models.CharField(max_length=100, null=False)
    departamento = models.IntegerField(null=False)
    nivel_acesso = models.ForeignKey(NiveisAcesso, on_delete=models.CASCADE, null=False)
    password_hash = models.TextField()

    def set_password(self, password):
        self.password_hash = make_password(password)

    def to_dict(self):
        return {
            "matricula": self.matricula,
            "cpf": self.cpf,
            "nome": self.nome,
            "departamento": self.departamento,
            "nivel_acesso_id": self.nivel_acesso_id,
        }  

class Rotinas(models.Model):
    descricao_rotina = models.CharField(max_length=255, null=False)
    nivel_acesso = models.ForeignKey(NiveisAcesso, on_delete=models.CASCADE, null=False)

class Departamentos(models.Model):
    nome_depart = models.CharField(max_length=255, null=False)

class UsuariosRotina(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    rotina = models.ForeignKey(Rotinas, on_delete=models.CASCADE)
    nivel_acesso = models.ForeignKey(NiveisAcesso, on_delete=models.CASCADE, null=False)
    departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE, null=False)

@receiver(post_save, sender=Usuarios)
@receiver(post_save, sender=Usuarios)
def associar_rotinas_usuarios(sender, instance, created, **kwargs):
    if created:
        rotinas_associadas = set()

        # Associação de rotinas baseada no departamento e nível de acesso
        if instance.nivel_acesso_id == 4:
            rotina_id = 9
        elif instance.departamento == 1:
            rotina_id = 1
        elif instance.departamento == 2:
            rotina_id = 2
        elif instance.departamento == 3:
            rotina_id = 3
        else:
            rotina_id = None

        if rotina_id is not None:
            rotina = Rotinas.objects.get(id=rotina_id)
            UsuariosRotina.objects.create(usuario=instance, rotina=rotina, nivel_acesso=instance.nivel_acesso, departamento_id=instance.departamento)
            rotinas_associadas.add(rotina_id)

        # Associação de rotinas comuns
        for rotina in Rotinas.objects.filter(nivel_acesso=instance.nivel_acesso).exclude(id__in=[1, 2, 3]):
            UsuariosRotina.objects.create(usuario=instance, rotina=rotina, nivel_acesso=instance.nivel_acesso, departamento_id=instance.departamento)

class EtapasAprovacoes(models.Model):
    nome_subtabela = models.CharField(max_length=255, null=False)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True)
    departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE, null=True)
    status_aprovacao = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    departamento_destino = models.IntegerField()
    descricao = models.TextField()
    revisor = models.IntegerField()
    nome_revisor = models.CharField(max_length=255)

class Tabelas(models.Model):
    nome_subtabela = models.CharField(max_length=255, null=False)
    departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    revisor = models.IntegerField()
    nome_revisor = models.CharField(max_length=255)
