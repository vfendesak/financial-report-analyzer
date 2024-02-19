from datetime import date

import requests
from bs4 import BeautifulSoup


class SECScraper:
    def __init__(self, YEARS_BACK=15):
        self.current_year = date.today().year
        self.YEARS_BACK = YEARS_BACK

    def request_archive(self, ticker):
        base_url = "https://www.sec.gov/cgi-bin/browse-edgar"

        querystring = {
            "action": "getcompany",
            "CIK": ticker,
            "type": "10-k",
            "dateb": "",
            "owner": "exclude",
            "count": "40",
        }

        payload = ""
        headers = {
            "cookie": "ak_bmsc=3F5BFA3D8E552152BD2E67FCE10096DC~000000000000000000000000000000~YAAQx2ZWuPGOaFmNAQAAjp5vWxYmY%2BQzQhGEA4LdPvlk%2FKhQJGvIpoJ7c1qejPPfkG2poXtV5pxvxMDleQ99lavTu2Ic4xtioLn9RNQTTeekmo3qrSSNHNN2tncMBNnQOiJgNc9C4pjVcMkSgM%2F0T1rwSpfExoFy3%2BK3QJD47Lg1IPGzeSyo9h%2F%2BMklPX7t5n%2FtN9YUJgzw%2F9lyQSnu3akaaX0T7zEOLowD%2Bysti7Y46giUIP0ekuZ4oU%2B3Ck%2BYMgXD%2FiaERUudhYh0Ix%2B4scR5M0%2BPDGxb%2BbduEBYxdKq6p%2BR%2F7NNWocRQRah7XUC5eeBQOQaHX8FskSVY9YgLE1Nguxow9JpXo2Y%2FrN2xTVm5%2Flnp55entnuHPUozJ26P032IWtCwyDl%2BODkijsuSpPPfO5gH7PVw6Vgo%2B0B1ZxrrNVOsre0ZJrMrRJVa0%2B4It",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "max-age=0",
            "Cookie": "ak_bmsc=3F5BFA3D8E552152BD2E67FCE10096DC~000000000000000000000000000000~YAAQBFgDF1l3BzqNAQAAsylmWxY3NmHWL7CNijcxPunbjZqtio8FdHvQRDxOufmYtfoLhzIVAtPu8I5mXDZBynhUH4XLCr34T8vnJfr7WP+zN4ewSSLZvA2OqWi7xui1z/gW/4q2N7Wb1JjOlXYAdUdt6HHwM+ayuNUv5nw8XvjzzTjm3A7dmFqOGRWdUk7SloEozLRAThyho2i2FkQz/olX+pg3dnozT8Hf0KIRIB5CBxk5ujeFaMWu924K9EpBgptEQ3SkQzITJ/RX+JFcIvDWed7fubLT7cqIdpGMkGboDLrMkJB0Sn+eTSZLolUjysrqtCka7KbPIjUOB4Ps45rbw8joDmfW2k87cE3pQauIrcXTRXrJpwxZ3rZ3Zfix04ULaYUllw==; bm_mi=ED08638E1BD445BFF11BE79BB1DFA4AB~YAAQBFgDF7TNBzqNAQAAgYdtWxbyg9yNZ4FwK6GcLTLosLPB6G+qVK00PIRMsBo3jM0G8TbLAPo6OiFA6HTDdEqD3Ue6OIpMPPBiz+5SQoBFHCN6DtnZVnK4cEpP6qZM9rh3I/wENUqoNs6SNYu0XHiORLwxWxYfq7jUrFZyS+MkE9WPX+wfZdTHSaKCu+xbqf5QoSW1XosxPdYyDZI0SJafesQnz/89NHFelL+KZYXCRbKX1+xJg6pyCO3gj6H/F6FenGR1jGPZg81quf1+hAWUNEVapyIZCsXrZOc0SCC/tnpErpVOwY4bCTeEBMHhFGCS9Sui5ABMUftidodk~1; bm_sv=6E383066D99B4042B27BC05EFB9E214C~YAAQBFgDF7XNBzqNAQAAgYdtWxbZ34/QlgV23NeESN8YlMo1bTxIL6kiC2ZoKd1nypGTSXU0jCG1bX1upvIoz9RbMQNJr8SGK70G9TeWoaSu65EfNYKTUuKMR5c0Wz8O+Aaf2s9di+Rmta4WDh/ID40Rc4JHxKAWZyY7Eu5azfYrv57bgorrFj8yw2ZkQ7WoJuR5DAuo7oIaoNt/nn972prbW/gUxfKWdiSIHl+FjXYRFOh9VHPLPWVdwFob~1",
            "Sec-Ch-Ua": '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Sec-Gpc": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        }
        return requests.request("GET", base_url, data=payload, headers=headers, params=querystring)

    def request_filings(self, filings_url):
        payload = ""
        headers = {
            "cookie": "ak_bmsc=3F5BFA3D8E552152BD2E67FCE10096DC~000000000000000000000000000000~YAAQx2ZWuPGOaFmNAQAAjp5vWxYmY%2BQzQhGEA4LdPvlk%2FKhQJGvIpoJ7c1qejPPfkG2poXtV5pxvxMDleQ99lavTu2Ic4xtioLn9RNQTTeekmo3qrSSNHNN2tncMBNnQOiJgNc9C4pjVcMkSgM%2F0T1rwSpfExoFy3%2BK3QJD47Lg1IPGzeSyo9h%2F%2BMklPX7t5n%2FtN9YUJgzw%2F9lyQSnu3akaaX0T7zEOLowD%2Bysti7Y46giUIP0ekuZ4oU%2B3Ck%2BYMgXD%2FiaERUudhYh0Ix%2B4scR5M0%2BPDGxb%2BbduEBYxdKq6p%2BR%2F7NNWocRQRah7XUC5eeBQOQaHX8FskSVY9YgLE1Nguxow9JpXo2Y%2FrN2xTVm5%2Flnp55entnuHPUozJ26P032IWtCwyDl%2BODkijsuSpPPfO5gH7PVw6Vgo%2B0B1ZxrrNVOsre0ZJrMrRJVa0%2B4It",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "max-age=0",
            "Cookie": "bm_mi=ED08638E1BD445BFF11BE79BB1DFA4AB~YAAQBFgDF7TNBzqNAQAAgYdtWxbyg9yNZ4FwK6GcLTLosLPB6G+qVK00PIRMsBo3jM0G8TbLAPo6OiFA6HTDdEqD3Ue6OIpMPPBiz+5SQoBFHCN6DtnZVnK4cEpP6qZM9rh3I/wENUqoNs6SNYu0XHiORLwxWxYfq7jUrFZyS+MkE9WPX+wfZdTHSaKCu+xbqf5QoSW1XosxPdYyDZI0SJafesQnz/89NHFelL+KZYXCRbKX1+xJg6pyCO3gj6H/F6FenGR1jGPZg81quf1+hAWUNEVapyIZCsXrZOc0SCC/tnpErpVOwY4bCTeEBMHhFGCS9Sui5ABMUftidodk~1; bm_sv=6E383066D99B4042B27BC05EFB9E214C~YAAQBFgDF2PRBzqNAQAA7bdtWxZ/PMnzQtqKxlp6rHlliSc5lEgp7+zUu8TI4Xu/xyLMumWqeu2jg37RxlLPK8b7Rs8LoDuJiCygPT7GzSCi8aM+MB/28XvQXjd80mfWfTz+zar1aNSd68bGYmag18CEmulDaFVaZe49jir81rM+tQChQg8onMmTTMpMZ0ILDPGk8R8lJhnEudXBQMx0B3BlbWAMOH3EGZiBn8dWEmg/sEl0IcksFZdu37+H~1; ak_bmsc=3F5BFA3D8E552152BD2E67FCE10096DC~000000000000000000000000000000~YAAQBFgDF984CDqNAQAAKF1zWxZxJmUcvth1s3WIXMiM6eK4zNe8VG7F8kxxmQEyJeW1bwoOCGnYBZLY72j6ad2WrL3I+M38IRnAcdPguId43ntcRpKnZMpTj75jxBvmrDhU2wlRUP9a3nZXP9CI1UioVxGQYCrHWYOjQhlKlTYXwfu4vK38tdb6sFApHj/bKdeQJyIHWE27dfMjHNtDQpo0QED5BTIIVRFwruczxT/qgvigl2s8kiOZIX1a3QqC02Rwmt9OvwFmZScwu30UpEUHvUr17ED0eCWdkcy7dk6duR33kpx9F1b6bWqd6Ae2IzAtpDEOl+6V+yOqyFqejNJeKWhLcxbfEX18qyy8aqIQ73qF3vybKWDFzipNKT4y8WkT6E3+YfyEBgxG319NwPPQdVZ14ZkKv1UpFPFV9lkhUUoBx2CGVfnPbiJVGAPL",
            "If-Modified-Since": "Thu, 02 Nov 2023 22 08:27 GMT",
            "Sec-Ch-Ua": '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Sec-Gpc": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        }
        return requests.request("GET", filings_url, data=payload, headers=headers)

    def fetch_filing_urls(self, archive):
        archive_urls = {}

        soup = BeautifulSoup(archive.text, "html.parser")
        table = soup.find("table", class_="tableFile2")
        rows = table.find_all("tr")

        for row in rows[1:]:  # Skip the header row
            cols = row.find_all("td")
            if len(cols) > 3:
                filing_date = cols[3].text.strip()
                year = int(filing_date.split("-")[0])

                if year >= (self.current_year - self.YEARS_BACK):
                    filing_href = cols[1].find("a")["href"]
                    filing_page_url = f"https://www.sec.gov{filing_href}"

                    archive_urls[year] = {"filings_url": filing_page_url}

        return archive_urls

    def fetch_10k_urls(self, archive_urls):
        filings = {}
        for year, value in archive_urls.items():
            filings_url = value["filings_url"]

            filings_response = self.request_filings(filings_url)
            filing_page_soup = BeautifulSoup(filings_response.text, "html.parser")
            for doc_link in filing_page_soup.find_all("a"):
                if doc_link.text.startswith(self.ticker):
                    doc_href = doc_link["href"]
                    download_url = f"https://www.sec.gov{doc_href}"
                    filings[year] = "".join(download_url.split(".xml")).replace("_htm", ".htm")
        return filings

    def get_doc_href(self, archive_soup):
        rows = archive_soup.find_all("tr")

        ten_k_url = ""

        for row in rows:
            cols = row.find_all("td")
            if len(cols) > 3:
                doc_type = cols[3].text.strip()
                if "10-K" in doc_type:
                    ten_k_url = cols[2].find("a")["href"]
        return ten_k_url

    def fetch_filings(self, archive_urls):
        filings = {}
        for year, value in archive_urls.items():
            filings_url = value["filings_url"]

            filings_response = self.request_filings(filings_url)
            archive_soup = BeautifulSoup(filings_response.text, "html.parser")

            doc_href = self.get_doc_href(archive_soup)
            download_url = f"https://www.sec.gov{doc_href}"
            filings[year] = (
                "".join(download_url.split(".xml")).replace("_htm", ".htm").replace("ix?doc=/", "")
            )
        return filings

    def get_10k_filings(self, ticker):
        archive = self.request_archive(ticker)
        archive_urls = self.fetch_filing_urls(archive)
        return self.fetch_filings(archive_urls)

    def fetch_report(self, report_url: str):
        payload = ""
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "max-age=0",
            "Cookie": "bm_mi=2F5AC7DBEC90CA72B7048BFB724142E4~YAAQVCR+aDfBglWNAQAAXdbhXxZRJ4RnkkNmfKWUeKc1QmGH7v3TlPngbOdNdESvidaNFbsxYRDuqNOeHf7o1570sBMa6264ltivVUhPKdRHSGYpVZ2XMWAD/nsmFsSdGcaKYGWMYw5uwfMf/PBPBlZjEQFik5jnd6rWMARaXnpOcYh9njmeVVV519UStSmkmZI5vOvjdoluWej0Z2CxX3Tvw6lNgc1tGVpPsmufVg31H7mrJXYEd2r8dgK/8ByPdjyyHV9vmHGVXWgtIYQEPdFuSZTZcKKd+BnNxBwJMemL5bYVUglFp1bWgOrjeN1N3ix8AELEMXzUgBOh3O3bOm20cMppfRlldfsle3K8Ih4OPhQV7X2gCBWcP/IF9xpVVVUCvbQc36+ZPkQeYwCpp1ZbDy4=~1; bm_sv=6FE42A06849FED4835CF97262309E48E~YAAQVCR+aELBglWNAQAA9N3hXxbgrPGTXP4dLr20mIrEPGqqt/fAg73yGCttn0ty9QTvryHyxJIj5/Xk9bdr1pg+N8DKmsja3McwAOPL66B3PbRpOXDni0I/7hj2onuFL1tySgSQdD5H2wbu2hHzLereVi/obIf/64d3G6DMRmi21FiZaZXw0bKx8Dcbey35f4/a0B3//5sv5dyHH022pza3IR0waWQFv9Up4U5Z1kAbE6dcCBfgw81JPrQ0CA==~1; ak_bmsc=A56127CD072C24354C54D9D888F73150~000000000000000000000000000000~YAAQVCR+aB3CglWNAQAAPE7iXxZxAH8EfBgLMoBK20p82jHscZyuohv2ZDf4igBKSFrl/lk2WxTlHBCZjxlNf0g7+4qhiHtb+iiwCO6dsttHAG4aLtjhcRUqGypjDKB5LdHa2gdTTYL6d+zDand7hgzuYEMTmjSlIXjsdiIpL5cRkkkc62gsj4VYGbKiS7sXf8ZJrpwcTVflEsete1zfSn9uR5h8ydDbzbLPj/YOTNBCNU2lE61l66SPhy3c3LkvFWNB33V1iZVX/r7AqomFCHZQrZiEejEOczLuLEfLyEE/ol0OlL5UgHM/KIfQtfG7xhej2JoGiKzIBRyzQT7iChekHOjlzZgF0IvCURxPvw4bLD14OlSOsh9QYMBkH6MEs8csRoOCbuBdYFKkXESQ+dC0QkyTlDgDbzv61UZ6u/Tzsp3AlkDvWHW2FLNVdZE8G47QP0auueW3sMi84Y3n4reVALhIZUHywXQ6w4F4K3P3fQwcU+F/qOFevEsQU60mNxbPeEc=",
            "If-Modified-Since": "Fri, 22 Feb 2019 21 17:19 GMT",
            "Sec-Ch-Ua": '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Sec-Gpc": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        }

        return requests.request("GET", report_url, data=payload, headers=headers)
