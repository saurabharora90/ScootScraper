import scrapy
from scrapy import FormRequest

class MainPage(scrapy.Spider):
    name = "landingPage"
    allowed_domains = ["flyscoot.com"]
    start_urls = [
            'http://www.flyscoot.com/en/',
        ]

    def __init__(self, to, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        self.destination = to

    def parse(self, response):
        formdata = {'revAvailabilitySearch.SearchInfo.AdultCount' : '1',
        'revAvailabilitySearch.SearchInfo.ChildrenCount' : '0',
        'revAvailabilitySearch.SearchInfo.InfantCount' : '0',
        'revAvailabilitySearch.SearchInfo.Direction' : 'Return',
        'revAvailabilitySearch.SearchInfo.PromoCode' : '',
        'revAvailabilitySearch.SearchInfo.SalesCode' : '',
        'revAvailabilitySearch.SearchInfo.SearchStations[0].DepartureStationCode' : 'SIN',
        'revAvailabilitySearch.SearchInfo.SearchStations[0].ArrivalStationCode' : self.destination,
        'revAvailabilitySearch.SearchInfo.SearchStations[0].DepartureDate':	'01/27/2017',
        'revAvailabilitySearch.SearchInfo.SearchStations[1].DepartureStationCode' : self.destination,
        'revAvailabilitySearch.SearchInfo.SearchStations[1].ArrivalStationCode' : 'SIN',
        'revAvailabilitySearch.SearchInfo.SearchStations[1].DepartureDate' : '01/31/2017'}
        yield FormRequest.from_response(response,
                                formxpath='//*[@id="searhflightform_return"]',
                                formdata=formdata,
                                clickdata={'class': 'btn btn-default btn--full btn--booking'},
                                callback=self.bookingPage)

    def bookingPage(Self, response):
        pathForDepartFlights = '/html/body/div[1]/main/form[1]/section[1]/div[3]/div[1]/div'
        pathForReturnFlights = '/html/body/div[1]/main/form[1]/section[2]/div[3]/div[1]/div'

        currentFlightDepart = response.xpath(pathForDepartFlights).xpath('div[@class="tab active"]')
        departDay = currentFlightDepart.xpath('a/span/text()').extract()[0].strip()
        departCost = currentFlightDepart.xpath('a/span/strong/text()').extract()[0].strip()
        print "Flight {2} on {0} is {1} ".format(departDay, departCost, response.xpath('/html/body/div[1]/main/form[1]/section[1]/div[1]/div/div[1]/h2/text()').extract()[0].strip())

        currentFlightReturn = response.xpath(pathForReturnFlights).xpath('div[@class="tab active"]')
        returnDay = currentFlightReturn.xpath('a/span/text()').extract()[0].strip()
        returnCost = currentFlightReturn.xpath('a/span/strong/text()').extract()[0].strip()
        print "Flight {2} on {0} is {1} ".format(returnDay, returnCost, response.xpath('/html/body/div[1]/main/form[1]/section[2]/div[1]/div/div[1]/h2/text()').extract()[0].strip())
        #scrapy.utils.response.open_in_browser(response)
