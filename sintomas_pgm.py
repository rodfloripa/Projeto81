
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# 1. ESTRUTURA DO GRAFO: Doença causa Sintomas
#   Gripe    Resfriado  Covid
#      \          |       /
#       Febre,  Tosse, Cansaco

modelo = BayesianModel([
    ('Gripe', 'Febre'), ('Resfriado', 'Febre'), ('Covid', 'Febre'),
    ('Gripe', 'Tosse'), ('Resfriado', 'Tosse'), ('Covid', 'Tosse'),
    ('Gripe', 'Cansaco'), ('Covid', 'Cansaco')
])

# 2. FATORES / CPDs = Tabelas de Probabilidade

# Probabilidade Prior: chance de ter a doença sem saber nada
cpd_gripe = TabularCPD(variable='Gripe', variable_card=2, values=[[0.95], [0.05]])  # 5% chance
cpd_resfriado = TabularCPD(variable='Resfriado', variable_card=2, values=[[0.90], [0.10]])  # 10% chance
cpd_covid = TabularCPD(variable='Covid', variable_card=2, values=[[0.98], [0.02]])  # 2% chance

# P(Febre | Gripe, Resfriado, Covid)
# [P(Febre=Não), P(Febre=Sim)] para cada combinação de doenças
cpd_febre = TabularCPD(
    variable='Febre',
    variable_card=2,
    values=[
        [0.99, 0.7, 0.8, 0.4, 0.6, 0.2, 0.3, 0.05],  # Não ter febre
        [0.01, 0.3, 0.2, 0.6, 0.4, 0.8, 0.7, 0.95]   # Ter febre
    ],
    evidence=['Gripe', 'Resfriado', 'Covid'],
    evidence_card=[2, 2, 2]
)

# P(Tosse | Gripe, Resfriado, Covid)
cpd_tosse = TabularCPD(
    variable='Tosse',
    variable_card=2,
    values=[
        [0.95, 0.6, 0.7, 0.3, 0.5, 0.2, 0.25, 0.1],
        [0.05, 0.4, 0.3, 0.7, 0.5, 0.8, 0.75, 0.9]
    ],
    evidence=['Gripe', 'Resfriado', 'Covid'],
    evidence_card=[2, 2, 2]
)

# P(Cansaco | Gripe, Covid)
cpd_cansaco = TabularCPD(
    variable='Cansaco',
    variable_card=2,
    values=[
        [0.9, 0.4, 0.3, 0.1],
        [0.1, 0.6, 0.7, 0.9]
    ],
    evidence=['Gripe', 'Covid'],
    evidence_card=[2, 2]
)

# 3. JUNTAR TUDO NO MODELO
modelo.add_cpds(
    cpd_gripe,
    cpd_resfriado,
    cpd_covid,
    cpd_febre,
    cpd_tosse,
    cpd_cansaco
)

modelo.check_model()  # Verifica se está consistente

# 4. INFERÊNCIA: Fazer pergunta pro modelo
inferencia = VariableElimination(modelo)

# CASO 1: Paciente com Febre=Sim e Tosse=Sim
resultado = inferencia.query(
    variables=['Gripe', 'Resfriado', 'Covid'],
    evidence={
        'Febre': 1,
        'Tosse': 1
    }  # 1=Sim, 0=Não
)

print("Paciente com Febre + Tosse:")
print(resultado)

# CASO 2: Paciente com Febre=Sim, Tosse=Sim, Cansaco=Sim
resultado2 = inferencia.query(
    variables=['Gripe', 'Resfriado', 'Covid'],
    evidence={
        'Febre': 1,
        'Tosse': 1,
        'Cansaco': 1
    }
)

print("\nPaciente com Febre + Tosse + Cansaco:")
print(resultado2)

