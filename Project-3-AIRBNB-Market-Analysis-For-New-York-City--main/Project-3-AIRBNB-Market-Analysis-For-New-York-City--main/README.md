# Project-3-AIRBNB-Market-Analysis-For-New-York-City-

## Overview 
New York, the largest city in the United States, has an estimated population of 19.84 million. The dataset used for this project includes AIRBnB accomodation for both local residents as well as tourists who visit the city annually. Being a major tourist attraction, New York receives visitors from various countries like Spain, France, Russia, and more. It is a popular vacation destination for families, and many people also work in the city. However, finding an affordable and suitable living space can be a challenge. With the help of the available dataset from year 2019 and 2023, we aim to analize the current AirBnB Rental Market via data app visualization to offer a cost-effective living option to our clients.

## Website Development  
The steps involved in making the website are as follows:
* Extraction of Data from the following link: http://insideairbnb.com/
* EDA Conducted on the data via Google Collaboratory Notebook
* Data deployed on MongoDB Local Server
* Mongo DB linked to the Flask App, to fetch the data 
* The dataset is jasonified and sent to the html pages for visual calculation and display via HighCharts.js library.

![image](/Images/All_Tech.png)
## Technologies Used 
* Google Collaboratory Notebook
* Python
* Flask
* MONGODB
* HTML
* CSS
* Javascript
* Highcharts.js Library


## Description 

* The first page was created to showcase the conduction of task distribution.
![image](/Images/ImageNo1.png)


* The second page shows comparative analysis via three types of graphs as follows:
1. Graph1: Comparison of the types of room distribution in year 2019 and 2023.

Findings: 

(a) In year 2019, more rooms were available in comparison to year 2023.

(b) Hotel rooms were only availlable in 2023. 

![Image](/Images/Image2.png)

2. Graph2: Comparison of total number of accomodation available in the 5 burroughs of New York City for AirBnB for year 2019 and 2023.

Findings: 

(a) There were more available accomodating listings in Bronx and Queens in year 2023 in comparison to 2019. However, we see the contrary in the case of Brooklyn, Manhattan for year 2019. 

(b) Not a big difference in the number of listings for Staten Island in year 2019 and 2023 i.e 56 more listings in year 2023.

(c) Factors that could influence the number of AirBnb house listings could be the decline of Covid 19, inflation, etc. 


![Image](/Images/Imag3.png)

3. Graph3: Pie-graph to show the top 10 neighbourhoods available for year 2019 and 2023.

Findings:  

(a) The names of the neighbourhood remain the same for both the years 2019 and 2023, with a bit of change in the numerical configuration for the house listings. 

(b) Williamsburg and Bedford-Stuyvesant remain the highest holders of number of AirBnb house listings for 2019 and 2023.

![Image](/Images/Image4.png)
  
5. Graph4: Pie-graph to show the bottom 10 neighbourhoods available for year 2019 and 2023.

Findings:  

(a) There is a slight change of the mentioned neighbourhoods for year 2019 and 2023i.e They werent the same for both the years. Few of the common names of the neighbouhood listings for 2019 and 2023 are as follows : 
      (i) Willowbrook 
      (ii) Fort Wadsworth 
      (iii) Howland Hook 
      (iv) Lighthouse Hill 
      (v) New Drop 

(b) The lowest number of AirBnb house listings in the mentioned neighbourhoods for 2019 and 2023 is around 1-2 houses. There is one exception in year 2023, with 3 AirBnb house listings from Huguenot.

   
![Image](/Images/Image5.png)



* The third graph shows the comparison of mean price distribution over the 5 burroughs in the new york city for year 2019 and 2023. 
![Image](/Images/Image6.png)

Findings : 

(a) Most expensive AirBnb accomodations for both years of 2019 and 2023 were from Manhattan and Staten Island.

(b) AirBnb house listings from Brooklyn, Bronx and Queens were slightly cheaper for both the years 2019 and 2023. 

(c) The house pricing has increased from year 2019 to 2023 comparatively for all the Burroughs in New york City. Since, the time Covid 19 phase got over tourism and traveling was ignited back again. Due to this, the pricing of the accommodation would have been increased in year 2023. As per the current scenario, there is an indication that prices might further increase for the Airbnb house listings in coming times. 

* The fourth graph is bulit using word_cloud alternative with highcharts.js to show all the names of the included neighbourhoods.
![Image](/Images/image7.png)





## Refrences
 - Highcharts Demo Tutorials
 - Youtube videos
 - UofT Bootcamp Tutorials
 - Flask Documentation
 - Mongo Db Documentation 





