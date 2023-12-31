import csv
from datetime import datetime as dt
from typing import Any, Dict

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider: Any) -> None:
        self.status_count: Dict[str, int] = {}
        self.total_peps: int = 0

    def process_item(
        self, item: Dict[str, Any], spider: Any
    ) -> Dict[str, Any]:
        status = item["status"]

        if status:
            self.status_count[status] = self.status_count.get(status, 0) + 1

        self.total_peps += 1

        return item

    def close_spider(self, spider: Any) -> None:
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
