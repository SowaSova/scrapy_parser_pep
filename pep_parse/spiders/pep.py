import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        table = response.css("section#numerical-index")
        for res in table.css("tbody > tr"):
            url = res.css("td:nth-child(2) a::attr(href)").get()
            meta_data = {
                "number": res.css("td:nth-child(2) a::text").get(),
                "name": res.css("td:nth-child(3) a::text").get(),
            }
            yield response.follow(url, callback=self.parse_pep, meta=meta_data)

    def parse_pep(self, response):
        status = (
            response.css("dl.rfc2822.field-list.simple")
            .xpath("dt[contains(., 'Status:')]/following::*/text()")
            .get()
        )
        data = {
            "number": response.meta["number"],
            "name": response.meta["name"],
            "status": status,
        }
        yield PepParseItem(data)
