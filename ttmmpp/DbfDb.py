from dbfread import DBF
from main.models import Street

for item in DBF('C:\data\otsaldk.DBF', encoding='cp866'):
    obj, created = Street.objects.get_or_create(name=str(item['Street']))
    print(item['Street']+" -- "+created)
    #print(item['FIO'])
