from django.db import models

ESTADO_CHOICES = (
  ('SP', 'SÃO PAULO'),
  ('PI', 'PIAUÍ'),
  ('BA', 'BAHIA'),
  ('CE', 'CEARÁ'),
  ('MT', 'MATO GROSSO'),
  ('MA', 'MARANHÃO'),
  ('SC', 'SANTA CATARINA'),
  ('RJ', 'RIO DE JANEIRO'),
  ('AM', 'AMAZONAS'),
  ('RN', 'RIO GRANDE DO NORTE'),
)

class Times(models.Model):
  nome = models.CharField(max_length=80, null=False, blank=False)
  estado = models.CharField(choices=ESTADO_CHOICES, max_length=32)
  cores = models.CharField(max_length=40, null=False, blank=False)
  ano_de_fundação = models.PositiveIntegerField(default=1970, verbose_name="Ano de Fundação")
  mundial = models.BooleanField(default=False)

  class Meta:
    verbose_name = 'Time'
    verbose_name_plural = 'Times'

  def __str__(self):
    return f'Time: {self.nome}'