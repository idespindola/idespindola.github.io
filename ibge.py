import requests
import json

lista_estados = [
    {
        "id": 1,
        "nome": "Acre",
        "sigla": "AC"
    },
    {
        "id": 2,
        "nome": "Alagoas",
        "sigla": "AL"
    },
    {
        "id": 3,
        "nome": "Amapá",
        "sigla": "AP"
    },
    {
        "id": 4,
        "nome": "Amazonas",
        "sigla": "AM"
    },
    {
        "id": 5,
        "nome": "Bahia",
        "sigla": "BA"
    },
    {
        "id": 6,
        "nome": "Ceará",
        "sigla": "CE"
    },
    {
        "id": 7,
        "nome": "Distrito Federal",
        "sigla": "DF"
    },
    {
        "id": 8,
        "nome": "Espírito Santo",
        "sigla": "ES"
    },
    {
        "id": 9,
        "nome": "Goiás",
        "sigla": "GO"
    },
    {
        "id": 10,
        "nome": "Maranhão",
        "sigla": "MA"
    },
    {
        "id": 11,
        "nome": "Mato Grosso",
        "sigla": "MT"
    },
    {
        "id": 12,
        "nome": "Mato Grosso do Sul",
        "sigla": "MS"
    },
    {
        "id": 13,
        "nome": "Minas Gerais",
        "sigla": "MG"
    },
    {
        "id": 14,
        "nome": "Pará ",
        "sigla": "PA"
    },
    {
        "id": 15,
        "nome": "Paraíba",
        "sigla": "PB"
    },
    {
        "id": 16,
        "nome": "Paraná",
        "sigla": "PR"
    },
    {
        "id": 17,
        "nome": "Pernambuco",
        "sigla": "PE"
    },
    {
        "id": 18,
        "nome": "Piauí",
        "sigla": "PI"
    },
    {
        "id": 19,
        "nome": "Rio de Janeiro",
        "sigla": "RJ"
    },
    {
        "id": 20,
        "nome": "Rio Grande do Norte",
        "sigla": "RN"
    },
    {
        "id": 21,
        "nome": "Rio Grande do Sul",
        "sigla": "RS"
    },
    {
        "id": 22,
        "nome": "Rondônia",
        "sigla": "RO"
    },
    {
        "id": 23,
        "nome": "Roraima",
        "sigla": "RR"
    },
    {
        "id": 24,
        "nome": "Santa Catarina",
        "sigla": "SC"
    },
    {
        "id": 25,
        "nome": "São Paulo",
        "sigla": "SP"
    },
    {
        "id": 26,
        "nome": "Sergipe",
        "sigla": "SE"
    },
    {
        "id": 27,
        "nome": "Tocantins",
        "sigla": "TO"
    }

]

lista_sigla = []
lista_id = []
for item in lista_estados:
	lista_sigla.append(item['sigla'])
	lista_id.append(item['id'])
dicionario_estados = dict(zip(lista_sigla, lista_id))

lista_municipios = {}
todos = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios?orderBy=nome'
rio_minas = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/31|33/municipios'
requisicao = requests.get(todos).json()
for item in requisicao:
    nome = '%s - %s' %(item['nome'], item['microrregiao']['mesorregiao']['UF']['sigla'])
    ibge = item ['id']
    id_uf = item['microrregiao']['mesorregiao']['UF']['id']
    id_uf_nota = dicionario_estados[item['microrregiao']['mesorregiao']['UF']['sigla']]
    lista_municipios[nome] = { 
            "ibge": ibge,
            "id_uf": id_uf,
            "id_uf_nota": id_uf_nota,
            }
lista_municipios = [lista_municipios]
with open('municipios.json', 'w') as outfile:
    json.dump(lista_municipios, outfile, indent=4)

###############################################################################################################
empenho_local = 'Dentro de Miracema' 
municipio = 'Santo Antônio de Pádua - RJ'

id_uf_nota = requests.get('https://idespindola.github.io/municipios_.json').json()[0][municipio]['id_uf_nota']
print(id_uf_nota)
ibge = requests.get('https://idespindola.github.io/municipios_.json').json()[0][municipio]['ibge']
print(ibge)
