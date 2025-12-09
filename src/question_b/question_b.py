#write functions here, don't add input('') statements here!

class Stock:
    """Stock class to represent publicly traded stocks"""
    
    def __init__(self, symbol, company_name):
        """Constructor with symbol and company_name parameters"""
        self.__symbol = symbol
        self.__company_name = company_name
    
    def get_symbol(self):
        """Public function to get the stock symbol"""
        return self.__symbol
    
    def get_company_name(self):
        """Public function to get the company name"""
        return self.__company_name