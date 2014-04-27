
import twitteroauth



class TwitterSearch(self):
    "Class for searching the Twittersphere using the API"
    """
    geocode format  geocode='37.781157,-122.398720,1mi'  lat,lon,radius
    
     GetSearch(self, term=None, geocode=None, since_id=None, max_id=None, 
                 until=None, count=15, lang=None, locale=None, result_type='mixed', include_entities=None)
    """
    
    def __init__(self, twitterApi):
        self.api = twitteroauth.getAuthenticatedApi()
        self.lang = "en"
        self.resultType = "mixed"
        self.geocode = None
    
    def checkApi(self, self.api):
        
    def setLanguage(self, lang):
        self.language = lang

    def setGeocode(self, lat, lon, radius):
        self.geocode = lat + "," + lon + "," + radius + "mi"
        
        #can be mixed, recent, popular
    def setResultType(self, resultType="mixed"):
        self.resultType = resultType
        
    def searchForText(self, text):
        self.api.GetSearch("CTA", lang="en")
        
    def search(self, text):
        results =  self.api.GetSearch(text, lang=self.lang, result_type=self.resultType,  )
