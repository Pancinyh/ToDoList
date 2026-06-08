from datetime import date
from dateutil.relativedelta import relativedelta

class BancoTarefas:
    def __init__(self):
        self.lista = []

    def adicionar_tarefa(self, nome, motivo, data_criacao=None, data_termino=None):
        self.lista.append(Tarefa(nome=nome, motivo=motivo,
                                 data_criacao=data_criacao, data_termino=data_termino))
        
    def buscar_tarefa(self, nome):
        for tarefa in self.lista:
            if tarefa.nome == nome:
                return tarefa
        return None
        
    def to_dict(self):
        return [
                {
                    'nome': item.nome,
                    'motivo': item.motivo,
                    'criacao': item.criacao.strftime('%d/%m/%Y'),
                    'termino': item.termino.strftime('%d/%m/%Y')

                }
                for item in self.lista
            ]
    
class Tarefa:
    def __init__(self, nome, motivo, data_criacao, data_termino):
        self.nome = nome
        self.motivo = motivo
        self.criacao = data_criacao if data_criacao is not None else date.today()
        self.termino = data_termino

    def tempo_restante(self):
        diferenca = relativedelta(self.termino, self.criacao)
        if diferenca.months <= 0 and diferenca.years <= 0:
            return "A tarefa já passou de seu prazo."
        return f"{diferenca.months} mêses e {diferenca.days} dias."
        
