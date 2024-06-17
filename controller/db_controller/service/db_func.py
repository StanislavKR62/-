from .models import Records

def get_records(filter):
    result = []
    records = Records.objects.all().filter(day = filter)
    for rec in records:
        result.append({ 'id' : rec.id, 'title' : rec.title})
    return result

def add_records(day,value):
    new_record = Records.objects.create(title=value,day = day)
    new_record.save()
    return True