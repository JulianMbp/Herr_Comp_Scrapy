from scrapy_selenium import SeleniumRequest
import scrapy

class CountryPopulationSeleniumSpider(scrapy.Spider):
    name = "country_population_selenium_spider"
    start_urls = [
        "https://www.worldometers.info/world-population/"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        rows = response.xpath('//table[contains(@class, "table") or contains(@id, "example2")]//tr[td]')
        for row in rows:
            yield {
                "Country": row.xpath('td[2]//text()').get(),
                "Population 2025": row.xpath('td[3]//text()').get(),
                "Yearly Change": row.xpath('td[4]//text()').get(),
                "Net Change": row.xpath('td[5]//text()').get(),
                "Density (P/Km²)": row.xpath('td[6]//text()').get(),
                "Land Area (Km²)": row.xpath('td[7]//text()').get(),
                "Migrants (net)": row.xpath('td[8]//text()').get(),
                "Fert. Rate": row.xpath('td[9]//text()').get(),
                "Median Age": row.xpath('td[10]//text()').get(),
                "Urban Pop %": row.xpath('td[11]//text()').get(),
                "World Share": row.xpath('td[12]//text()').get()
            }