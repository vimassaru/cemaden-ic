import csv
from pathlib import Path
from django.core.management.base import BaseCommand
from website.models import School


class Command(BaseCommand):
    help = 'Importar dados das escolas do CSV para o banco de dados'

    def __init__(self):
        self.BASE_DIR = Path(__file__).parent.parent.parent.parent
        self.MISC_FOLDER = self.BASE_DIR / 'misc'
        self.CSV_FILE = self.MISC_FOLDER / 'dados_escolas.csv'

    def handle(self, *args, **kwargs):
        with open(self.CSV_FILE, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                School.objects.create(
                    entity_code=row['CO_ENTIDADE'],
                    school_name=row['NO_ENTIDADE'],
                    uf_code=row['CO_UF'],
                    uf=row['UF'],
                    town_code=row['CO_MUNICIPIO'],
                    town_name=row['NO_MUNICIPIO'],
                )
        self.stdout.write(self.style.SUCCESS('Dados importados com sucesso!'))
