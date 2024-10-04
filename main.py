# import the requests library (1 line)
import requests

# assign the root url (without /status) to the root_url variable for ease of reference (1 line)
root_url = 'https://country-leaders.onrender.com'

# assign the /status endpoint to another variable called status_url (1 line)
status_url = root_url + '/status'

# query the /status endpoint using the get() method and store it in the req variable (1 line)
req = requests.get(status_url)

# check the status_code using a condition and print appropriate messages (4 lines)
if req.status_code == 200:
    print('OK, request accepted')
else:
    print(req.status_code)

#_____________________________________________________________________________

# Set the countries_url variable (1 line)
countries_url = root_url + '/countries'

# query the /countries endpoint using the get() method and store it in the req variable (1 line)
req = requests.get(countries_url) #, params={'country': 'be'})          

# Get the JSON content and store it in the countries variable (1 line)
countries = req.json()         
      
# display the request's status code and the countries variable (1 line)
print("status_code/  ", req.status_code, "\ncountries:  ", countries)

#_____________________________________________________________________________

# Set the cookie_url variable (1 line)
cookie_url = root_url + '/cookie'  

# Query the enpoint, set the cookies variable and display it (2 lines)
cookie = requests.get(cookie_url).cookies
cookie

#_____________________________________________________________________________

# query the /countries endpoint, assign the output to the countries variable (1 line)
countries = requests.get(countries_url, cookies = cookie).json()
# display the countries variable (1 line)
countries

#_____________________________________________________________________________

# Set the leaders_url variable (1 line)
leaders_url = root_url + '/leaders'
# query the /leaders endpoint, assign the output to the leaders variable (1 line)
leaders = requests.get(leaders_url)
# display the leaders variable (1 line)
print(leaders)

#_____________________________________________________________________________

# query the /leaders endpoint using cookies and parameters (take any country in countries)
leaders = requests.get(leaders_url, cookies = cookie, params={"country":"be"})
# assign the output to the leaders variable (1 line)
#leaders = leaders.json()
# display the leaders variable (1 line)
print(leaders.text)

#_____________________________________________________________________________

# 4 lines
leaders_per_country = {}
for i in countries:
    leaders_per_country[i]= requests.get(leaders_url, cookies = cookie, params={"country":i}).json()
leaders_per_country

#_____________________________________________________________________________

# or 1 line
for i in countries: leaders_per_country = {}; leaders_per_country[i]= requests.get(leaders_url, cookies = cookie, params={"country":i}).json()
leaders_per_country

#_____________________________________________________________________________

# < 15 lines
leaders_per_country = {}

def get_leader():
    
    url = 'https://country-leaders.onrender.com'
    cookie = requests.get(url + '/cookie').cookies
    countries = requests.get(url + '/countries', cookies = cookie).json()

    for i in countries:
        leaders_per_country[i]= requests.get(leaders_url, cookies = cookie, params={"country":i}).json()

get_leader()

leaders_per_country

#_____________________________________________________________________________

# 2 lines

get_leader()

leaders_per_country

#_____________________________________________________________________________




