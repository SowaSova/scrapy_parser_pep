import csv
from datetime import datetime as dt

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_count = {}
        self.total_peps = 0

    def process_item(self, item, spider):
        status = item["status"]

        if status:
            self.status_count[status] = self.status_count.get(status, 0) + 1

        self.total_peps += 1

        return item

    def close_spider(self, spider):
        now = dt.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_dir = BASE_DIR / "results"
        file_dir.mkdir(exist_ok=True)
        filename = f"status_summary_{now}.csv"

        with open(file_dir / filename, "w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Статус", "Количество"])
            for status, count in self.status_count.items():
                writer.writerow([status, count])
            writer.writerow(["TOTAL", self.total_peps])
