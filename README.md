# AtomTinyDB
An simple TinyDB atomic API call's

## Setup the venv
```bash
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
pip3 list
deactivate
```

## Install global
```bash
python3 -m setup.py install
```

## Install venv
```bash
source ./venv/bin/activate
./setup.py install
```

### Test simple call's
Just using call's of tinydb method
```bash
./test/simple.py
```

### Test thread call's
Using thread call's to test the atomic isues
```bash
./test/thread.py
```

### Python code
Example 1
```python

import from AtomTinyDb import AtomTinyDbConn, AtomTinyDbLock

if __name__ == "__main__":

    # Create file .json 
    # obs: you cam use the TinyDB parameter's
    aDb = AtomTinyDbConn('./data/db_threads.json', sort_keys=True, indent=4, separators=(',', ': '))

    # Lock TinyDB until de end
    with AtomTinyDbLock(aDB.table('table01')) as db:

        # insert dado
        val1 = db.insert({'id_data': str(ObjectId()),
                        'idade':10,
                        'status':0,
                        'nome':'Eduardo Pagotto',
                        'sexo':True,
                        'last':datetime.timestamp(datetime.now())})

    aDb.close()
```

### Several commnad
[examples](docs/examples.md): Insert; Update; Remove; Query