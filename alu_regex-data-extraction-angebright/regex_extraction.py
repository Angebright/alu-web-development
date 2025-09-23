import re

# Sample API Response (Hotel Example)
api_response = """
Hotel1 - Luxury, Hotel2 - Budget, Hotel3 - Boutique
Reservation email: reservations@hotelparadiso.example.co.uk
Visit: https://www.hotelparadiso.example.com/booking?ref=homepage
Check rooms at: https://sub.hotelparadiso.example.org/rooms/suite
Contact: 123-456-7890 or 123.456.7890
Credit cards: 1234 5678 9012 3456, 1234-5678-9012-3456
Event Time: 14:30 or 2:30 PM
HTML: <div class="room"> <img src="room.jpg" alt="suite"> </div>
Hashtags: #HotelLife #RelaxAndUnwind
Prices: $19.99, $1,234.56, $100
"""

# Regex patterns
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
url_pattern = r'https?://[^\s]+'
phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
credit_pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
time_pattern = r'((?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?)'
html_pattern = r'<[^>]+>'
hashtag_pattern = r'#\w+'
currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

# Extract data
emails = re.findall(email_pattern, api_response)
urls = re.findall(url_pattern, api_response)
phones = re.findall(phone_pattern, api_response)
credit_cards = re.findall(credit_pattern, api_response)
times = re.findall(time_pattern, api_response)
html_tags = re.findall(html_pattern, api_response)
hashtags = re.findall(hashtag_pattern, api_response)
currencies = re.findall(currency_pattern, api_response)

# Print results
print("Emails:", emails)
print("URLs:", urls)
print("Phones:", phones)
print("Credit Cards:", credit_cards)
print("Times:", times)
print("HTML Tags:", html_tags)
print("Hashtags:", hashtags)
print("Currencies:", currencies)

