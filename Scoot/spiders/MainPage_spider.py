import scrapy
from scrapy import FormRequest

class MainPage(scrapy.Spider):
    name = "price"
    allowed_domains = ["flyscoot.com"]
    start_urls = [
            'http://www.flyscoot.com/en/',
        ]

    def __init__(self, t, f = 'SIN', *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        self.departure = f
        self.destination = t

    def parse(self, response):
        formdata = {'revAvailabilitySearch.SearchInfo.AdultCount' : '1',
        'revAvailabilitySearch.SearchInfo.ChildrenCount' : '0',
        'revAvailabilitySearch.SearchInfo.InfantCount' : '0',
        'revAvailabilitySearch.SearchInfo.Direction' : 'Return',
        'revAvailabilitySearch.SearchInfo.PromoCode' : '',
        'revAvailabilitySearch.SearchInfo.SalesCode' : '',
        'revAvailabilitySearch.SearchInfo.SearchStations[0].DepartureStationCode' : self.departure,
        'revAvailabilitySearch.SearchInfo.SearchStations[0].ArrivalStationCode' : self.destination,
        'revAvailabilitySearch.SearchInfo.SearchStations[0].DepartureDate':	'04/13/2017',
        'revAvailabilitySearch.SearchInfo.SearchStations[1].DepartureStationCode' : self.destination,
        'revAvailabilitySearch.SearchInfo.SearchStations[1].ArrivalStationCode' : self.departure,
        'revAvailabilitySearch.SearchInfo.SearchStations[1].DepartureDate' : '04/16/2017'}
        yield FormRequest.from_response(response,
                                formxpath='//*[@id="searhflightform_return"]',
                                formdata=formdata,
                                clickdata={'class': 'btn btn-default btn--full btn--booking'},
                                callback=self.bookingPage)

    def bookingPage(Self, response):
        pathForDepartFlights = '/html/body/div[1]/main/form[1]/section[1]/div[3]/div[1]/div'
        timingForDepartFlight = '/html/body/div[1]/main/form[1]/section[1]/div[3]/div[3]/div[1]/div[1]/ul/li/text()'

        pathForReturnFlights = '/html/body/div[1]/main/form[1]/section[2]/div[3]/div[1]/div'
        timingForReturnFlight = '/html/body/div[1]/main/form[1]/section[2]/div[3]/div[3]/div[1]/div[1]/ul/li/text()'

        currentFlightDepart = response.xpath(pathForDepartFlights).xpath('div[@class="tab active"]')
        departDay = currentFlightDepart.xpath('a/span/text()').extract()[0].strip()
        departCost = currentFlightDepart.xpath('a/span/strong/text()').extract()[0].strip()
        print "Flight {2} on {0} at {3} is {1} ".format(departDay, departCost, response.xpath('/html/body/div[1]/main/form[1]/section[1]/div[1]/div/div[1]/h2/text()').extract()[0].strip(), response.xpath(timingForDepartFlight).extract()[0].strip())

        currentFlightReturn = response.xpath(pathForReturnFlights).xpath('div[@class="tab active"]')
        returnDay = currentFlightReturn.xpath('a/span/text()').extract()[0].strip()
        returnCost = currentFlightReturn.xpath('a/span/strong/text()').extract()[0].strip()
        print "Flight {2} on {0} at {3} is {1} ".format(returnDay, returnCost, response.xpath('/html/body/div[1]/main/form[1]/section[2]/div[1]/div/div[1]/h2/text()').extract()[0].strip(), response.xpath(timingForReturnFlight).extract()[0].strip())
        #scrapy.utils.response.open_in_browser(response)
