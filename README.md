# AtomTinyDB
An simple TinyDB atomic API call's 

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
```python
# imports
from AtomTinyDb import AtomTinyDbConn, AtomTinyDbLock

if __name__ == "__main__":

    # Create file .json 
    # obs: you cam use the TinyDB parameter's
    aDb = AtomTinyDbConn('./data/db_threads.json')

    # Lock TinyDB until de end
    with AtomTinyDbLock(aDB.table('table01')) as db:

        # insert dado
        val1 = db.insert({'id_data': str(ObjectId()),
                        'idade':10,
                        'status':0,
                        'nome':'Eduardo Pagotto',
                        'sexo':True,
                        'last':datetime.timestamp(datetime.now())})


```