## Domain Links Scraper
This script will start in the defined page/pages and scrape all URLs
inside a defined domain until no links to that domain are left.

It will go through all the links found for that specific domain,
find the urls in those pages, and follow from there, without repeating pages.

It extracts all URLs into a CSV file. Only URLs of the same domain.

This script was used to [generate a page rank](https://github.com/georgerappel/page-rank) for a university assignment,
It can also be used to generate a adjacency matrix, graphs, and
many other data structures that require links between pages in a domain.

### Running the script

Install scrapy using pip:

`sudo pip install scrapy`

Run the bash file to start scraping:

`bash start_scraper.sh`

If you `CTRL + C` during the process, some URLs will be saved anyway
in the output file.