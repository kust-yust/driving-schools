from django.db import models

#Model to save school info (id, name, provice, city)
class Schools(models.Model):
    autoescuela_id = models.CharField('Código Autoescuela', max_length=10)
    provincia = models.CharField('Provincia', max_length=50)
    municipio = models.CharField('Municipio', max_length=50)
    nombre = models.CharField('Nombre Autoescuela', max_length=100)

    def __str__(self):
        return self.autoescuela_id

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'

#Used to populate 'Schools' table from .csv file using admin panel
class AddSchool(models.Model):
    data = models.FileField()

    def save(self, *args, **kwargs):
        from csv import reader
        super().save(*args, **kwargs)
        filename = self.data.path
        with open(filename) as f:
            read_file = list(reader(f, dialect='excel'))
            for row in read_file[1:]:
                school = Schools.objects.create(
                    autoescuela_id=str(row[0]),
                    provincia=str(row[1]),
                    municipio=str(row[2]),
                    nombre=str(row[3])
                )

    def __str__(self):
        return self.data.path



class Pruebas(models.Model):
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    seccion = models.IntegerField('Código Sección')
    permiso = models.CharField('Tipo Permiso', max_length = 10)
    examen = models.CharField('Tipo Examen', max_length = 50)
    aptos = models.IntegerField('Número Aptos')
    aptos_1 = models.IntegerField('Número Aptos 1ª convocatoria')
    no_aptos = models.IntegerField('Número Suspendidos')
    total = models.IntegerField('Total Examenados')
    year = models.IntegerField('Año')

    def __str__(self):
        return str(self.school) + ' ' + self.permiso + ' '+self.examen + ' '+ str(self.year)

    class Meta:
        verbose_name = 'Prueba'
        verbose_name_plural = 'Pruebas'

class DataFile(models.Model):
    data = models.FileField()

    def save(self, *args, **kwargs):
        from csv import reader
        super().save(*args, **kwargs)
        filename = self.data.path
        with open(filename) as f:
            read_file = list(reader(f, dialect='excel'))
            for row in read_file[1:]:
                prueba = Pruebas.objects.create(
                    school=Schools.objects.get(autoescuela_id=str(row[2])),
                    seccion=int(float(row[4])),
                    permiso=str(row[5]),
                    examen=str(row[6]),
                    aptos=int(float(row[7])),
                    aptos_1=int(float(row[8])),
                    no_aptos=int(float(row[9])),
                    total=int(float(row[10])),
                    year=int(row[11]),
                )

    def __str__(self):
        return self.data.path

