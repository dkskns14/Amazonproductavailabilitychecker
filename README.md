  Amazon Product Availability Checker – Documentation

1.introduction: The "Amazon Product Availability Checker" is a Python script that allows users to check the availability of a product on Amazon. It utilizes web scraping techniques to extract the availability information from the product's webpage

2.Installation: - Before using the script, ensure that you have Python installed on your system. You can download Python from the official Python websiteThe script utilizes the following libraries, which can be installed using the pip package manager:

requests: pip install requests:- Python requests is a library for making HTTP requests. It provides an easy-to-use interface that makes working with HTTP very simple,

urllib3: pip install urllib3:- urllib3 is a Python library that provides a higher-level interface for making HTTP requests. It is built on top of the standard library's http.client module and provides additional features and functionalities.

BeautifulSoup: pip install beautifulsoup4:- Beautiful Soup (often abbreviated as BS4) is a Python library for parsing HTML and XML documents. It provides a convenient and powerful way to extract data from HTML or XML content by navigating and manipulating the document's elements.

3.How It Works

Importing Libraries:  The script starts by importing the required libraries: requests, urllib3, and Beautiful Soup. These libraries are used to make HTTP requests, disable SSL warnings, and parse HTML content, respectively.

Input for URL: The script prompts the user to provide the URL of the product they want to check. The user enters the URL through the standard input.

Disabling SSL Warnings: To handle SSL certificate verification, the urllib3.disable_warnings() function is called. This disables SSL warnings that might occur during the HTTP request.

Sending HTTP Request: The script uses the requests.get() function to send an HTTP GET request to the provided URL. The verify=False parameter is used to bypass SSL certificate verification.

Parsing HTML Response: The response content from the HTTP request is then parsed using BeautifulSoup. The HTML content is passed to the BeautifulSoup() constructor with the 'html.parser' argument.


Check Availability Element: The script uses the find() method of BeautifulSoup to search for a <span> element with the CSS classes 'a-size-medium' and 'a-color-success'. This element contains the availability information of the product.

Checking Availability: If the availability element is found, the script extracts the availability text using the text attribute of the element. Leading and trailing whitespace is removed using the strip() method. The availability information is then displayed to the user.

Handling Unavailability: If the availability element is not found, the script displays a message indicating that the product is not available.

Calling the Function: Finally, the check_product_Availability() function is called to start the availability check process. The script prompts the user for a URL and performs the necessary operations to check and display the product availability.

4.Usage
  
When prompted, enter the URL of the product on Amazon.
The script will send an HTTP request to the provided URL, scrape the HTML content, and search for the availability element.
If the product is available, the script will display the availability information. Otherwise, it will indicate that the product is not available.

5. Conclusion: The Product Availability Checker script provides a simple way to check the availability of a product on a given website. By leveraging the requests, urllib3, and BeautifulSoup libraries, the script can fetch the HTML content of a web page, parse it, and extract the product availability information






