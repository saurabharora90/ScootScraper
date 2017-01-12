# ScootScraper
A python tool to allow you to quickly check the prices of any destination on flyscoot.com

##Requirements
You can use the pip tool to install the dependencies needed for this project. Simply run 

`pip install requirements-txt`

##Usage
After you have installed the dependencies, you can run the scraper and get the prices to any destination:

`scrapy crawl price -a t=JAI`

Supported arguments:

 - **t**: The destination Airport Code. *Compulsory*
 - **f**: The departure Airport Code. *Optional*. Defaults to SIN

`scrapy crawl price -a t=SIN -a f=JAI`
