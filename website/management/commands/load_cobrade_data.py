import csv
from pathlib import Path
from django.core.management.base import BaseCommand
from website.models import Cobrade
import logging


class Command(BaseCommand):
    help = 'Importar dados das escolas do CSV para o banco de dados'

    def __init__(self):
        self.BASE_DIR = Path(__file__).parent.parent.parent.parent
        self.MISC_FOLDER = self.BASE_DIR / 'misc'
        self.CSV_FILE = self.MISC_FOLDER / 'dados_cobrade.csv'

    def handle(self, *args, **kwargs):
        try:
            with open(self.CSV_FILE, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    Cobrade.objects.create(
                        cobrade_id=row['COBRADE'],
                        description=row['DESCRIÇÃO'],
                    )

            print('Dados importados com sucesso!')
        except Exception as e:
            print(f'Ocorre o seguinte erro: \n {logging.exception(e)}')
