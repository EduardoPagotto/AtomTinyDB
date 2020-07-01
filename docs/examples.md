
### Objeto de query
dados = Query()

### Lista Todos os Documentos do DB
lista = db.all()

### Insercao de Documento no DB
indice = db.insert(record_file)

### Update usando Objeto de Query
db.update({'status': 1}, dados.seq == item_mod['seq'])
db.update({'branco': True, 'threshold': 0}, dados.seq == item_mod['seq'])
db.update({'branco': False, 'threshold': 1000}, dados.seq == item_mod['seq'])
db.update({'seq':serial_file}, (dados.seq == ultimo['seq']) & (dados.date == ultimo['date']))
db.update(novo, (dados.seq == destino['seq']) & (dados.date == destino['date']))
db.update({'last': datetime.timestamp(datetime.now())}, dados.summary.id == item['summary']['id'])

### Update usando sentenca where
db.update(valDB, where('summary')['id'] == summary['id'])
db.update(increment('ok'), where('summary')['id'] == summary['id'])
db.update({'done_nva':True, 'last': datetime.timestamp(datetime.now())}, where('summary')['id'] == summary['id'])
db.update(val, where('summary')['id'] == summary['id'])
db.update(increment('erro'), where('summary')['id'] == summary['id'])
db.update(val, where('summary')['id'] == summary['id'])

### Update usando chave (uniq key )do Documento
db.update(modificados, doc_ids=[indice])

### Consuldade um unico documento usando Objeto Query
item = db.get(dados.seq == item_mod['seq'])
origem = db.get((dados.seq == destino['seq']) & (dados.date != destino['date']))
master = db.get(Query().summary.id == summary['id'])

### Consulta de unico Documento usando Where
dados = db.get(where('type') == type_image)

### Consulta de unico Documento usando chave (uniq key )do Documento
dados = db.get(doc_id=indice)

### Consulta multiplos Documentos usando Objeto Query
itens = db.search(dados.seq >= serial_file)
itens = db.search((dados.last < to_pronto) & (dados.done_fluxion == True))

### Remocao de documento(s) usando Uniq key (lista)
db.remove(doc_ids=[origem.doc_id])

### Remocao de Documento usando Objeto Query
db.remove(dados.summary.id == item['summary']['id'])