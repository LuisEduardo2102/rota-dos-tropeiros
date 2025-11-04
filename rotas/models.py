from django.db import models

# Create your models here.
class Rota(models.Model):
    """
    Define a rota de onibus
    """
    nome = models.Charfield(
    max_lenght=200,
    help_text="Nome ou identificador da rota"
    )

    ativo = models.BooleanField(
        default=True,
        help_text="Inidca se a rota esta na operação"
    )
    
    class Meta:
        verbose_name = "Rota"
        verbose_name_plural = "Rotas"
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Parada(models.Model):
    
    #Define um ponto de parada de ônibs
    
    endereco = models.Charfield(
        max_lenght=255,
        help_text ="Descrição do endereço ou nome da parada"
    )

    latitude_longitude = models.CharField(
        max_lenght=50,
        help_text="Coordenadas no formato 'latitide, longitede' (ex: -24.7900000, -49.0000000)"
    )

    ativo = models.BooleanField(
        default=True,
        help_text="Indica se a parada está atualmente em uso"
    )

    class Meta:
        verbose_name = "Parada"
        verbose_name_plural = "Paradas"
        ordering = ['endereço']

    def __str__(self):
        return self.endereco
    
class RotaParadaHorario(models.Model):

    #Tabela associativa (Through Table) que concecta Rotas e Paradas,
    #especificando o horário e o status de atividade dessa conexão.

    rota = models.ForeignKey(
        Rota,
        on_delete=models.CASCADE,
        related_name="horarios_parada"
    )
    
    parada = models.ForeignKey(
        Parada,
        on_delete=models.CASCADE,
        related_name="horarios_rota"
    )
    
    horarios = models.TimeField(
        help_text="Horário programado para a passagem do ônibus nesta parada"
    )

    ativo = models.BooleanField(
        default=True,
        help_text="Indica se este horário específico nesta parada/rota está ativo "
    )

    class Meta:
        verbose_name = "Horario da Rota na Parada"
        verbose_name_plural = "Horários das Rotas nas Paradas"

        # garante que não haja um horário duplicado para a mesma parada na mesma rota
        unique_togheter = ('rota', 'parada', 'horario')

        # Classifica/Ordena os registros primeiro pela Rota, e depois pelo Horário
        ordering = ['rota', 'horario']

    def __str__(self):
        # verifica o status de todos os objetos relacionados
        rota_nome = self.rota.nome if self.rota else "Rota Idefinida"
        parada_end = self.parada.endereco if self.parada else "Parada Indefinida"
        horario_str = self.horario.strftime('%H:%M') if self.horario else "HH:MM"

        status_horario = "Ativo" if self.ativo else "Inativo"

        return (f"Rota: {rota_nome} | "
                f"Parada: {parada_end} | "
                f"Horário: {horario_str} | ({status_horario})"        
        )

