IP Location Tracker
This Python script allows users to retrieve the approximate geographical location of an IP address using IP-based geolocation. It is designed for educational purposes, particularly for Computer Science and Engineering (CSE) students, to demonstrate how to work with geolocation data in Python.
Features

Retrieve location data (city, state/region, country, and coordinates) for a given IP address.
Use 'me' to get the location based on your current IP address.
Includes sample IP addresses for testing.
Simple command-line interface with a loop for multiple queries.
Error handling for invalid IP addresses and network issues.

Prerequisites

Python 3.x installed on your system.
The geocoder library. Install it using:pip install geocoder


An active internet connection to query the geolocation service.

Installation

Download the location_tracker.py script from this repository.
Ensure you have Python 3.x installed.
Install the geocoder library:pip install geocoder



Usage

Open a terminal or command prompt.
Navigate to the directory containing location_tracker.py.
Run the script:python location_tracker.py


Follow the on-screen prompts:
Enter an IP address to get its location.
Enter 'me' to get your current IP's location.
Enter 'q' to quit.



Examples

To get the location of Google's DNS server:
Enter IP address: 8.8.8.8
City: Mountain View
State/Region: California
Country: United States
Latitude, Longitude: [37.386, -122.0838]


To get your own location:
Enter IP address: me
City: Your City
State/Region: Your State
Country: Your Country
Latitude, Longitude: [Your Lat, Your Long]



How It Works
This script uses the geocoder library, which queries an online geolocation service (like GeoIP) to retrieve location data based on the provided IP address. When 'me' is entered, it uses your current public IP address to fetch the location.
Limitations

The accuracy of the location data can vary. It may not pinpoint exact addresses, especially for dynamic IP addresses or when using VPNs.
Requires an internet connection to function.
Depends on the availability and accuracy of the geolocation service used by the geocoder library.

Contributing
This is an educational project, but contributions are welcome! If you have suggestions for improvements or additional features, feel free to fork the repository and submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

