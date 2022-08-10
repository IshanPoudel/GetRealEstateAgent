# GetRealEstateAgent

Using Selenium and BeautifulSoup , this program given a url link , gets the link of all the listed properties. 

<b><h2>For each of the listed properties , it grabs the following data. </b></h2>
<b>
House Link

Property address 

Name of the agent

Name of the real estate agency if applicable

Address of the real estate agency 

Texas real_estate id number of the agent

The agency's public business address as listed in the Texas Real Estate Comission Website (www.trec.texas.gov).

The agency's business email.

</b>

Stores the data in mysql table titled final_agent.


<b><h1> How to run the program</b></h1>

<b>
In the config.py file , change the variables user and password to the username and  password to the local mysql file.

Run Initialize_Database.py

Run Main.py

</b>
