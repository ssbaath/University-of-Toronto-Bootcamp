# AIRBnB_UofT_Project-1_DA2023 #

New York is the largest city in the United States, with an estimated 2022 population of 8.948 million. This data set comprises of the people who locally live there as well as the tourists which visit the city annually. It is a major tourist attraction with many people visiting the city from various countries like Spain, France, Russia, etc. It is a favourite vacation spot for many families. With many people also working in the city, it is always a challenge to find a suitable living space which is affordable and in suitable locality. Therefore with the available dataset and contributing analysis of the data, we will try providing a cost effective locations to the clients.

### Goals of success ###
1. Creating a suitable price range as per the size and cost of the living space.
2. Allocate the locations as per accurate client ratings.
3. Provide details regarding the climate zone as per longitudinal and latitudinal data and other essential places around the prospective location.
4. Ensuring accuracy of the data and not wasting the client’s time and space.
5. Establishing a good long term Owner-Client relationship.

2. Validity and reliability of the model is checked through the preparation of the data. The data is prepared by cleaning, integrating, reducing and feature selecting the data. The source quality is measured through the accuracy , completeness, consistency, timeliness, believability, value added, interpretability and accessibility.

### Results ###

1. There are 16 identified types of Attributes:

    id : Discrete - Numeric Attribute
    name : Nominal Attribute
    host_id : Discrete-Numeric Attribute
    host_name : Nominal Attribute
    neighbourhood_group : Nominal Attribute
    neighbourhood : Nominal Attribute
    latitude : Interval-Scaled Numeric Attribute
    longitude : Interval-Scaled Numeric Attribute
    room_type : Nominal Attribute
    price : Discrete-Numeric Attribute
    minimum_nights : Discrete-Numeric Attribute
    number_of_reviews : Discrete-Numeric Attribute
    last_review : Date-Time Attribute
    reviews_per_month : Discrete-Numeric Attribute
    calculated_host_listings_count : Discrete-Numeric Attribute
    availability_365 : Discrete-Numeric Attribute
    
2. There are three types of rooms available in the data set :-

    Entire home/apt: Highest Availability 
    Private Room : Second Highest Availability 
    Shared room : Lowest Availability 
    
    


![Reference Image](main/Images/graph1.png)


    

3. Univariate Analysis

(a)

#The attribute 'minimum-nights' range from 1-1250 nights. Which means that the lowest value for minimum night to stay is mentioned as one(1) and the maximum value is 1250 nights(3 years approx).


#Number of values missing per attribute:

    Name(name): There are in total 16 missing values.
    Host Name(host_name): There are 21 missing values.
    Last Review(last_review): There are 10052 missing-review dates.
    Review Per Month(reviews_per_month) : There are 10052 missing values.

#The hosts with maximum house listings are:

    ID.219517861 with 327 house listings.( 1rst Highest Rank)
    ID.107434423 with 232 house listings.( 2nd Highest Rank)
    ID.30283594 with 121 house listings.( 3rd Highest Rank)

There are other id's with house listings comparatively low in number than the ones listed above.


Normalization

#The house listings are from the five Boroughs of New York:

    Brooklyn
    Manhattan
    Queens
    Staten Island
    Bronx



#Calculating top 10 neighbourhoods with maximum number of house listings.
Williamsburg          3920
Bedford-Stuyvesant    3714
Harlem                2658
Bushwick              2465
Upper West Side       1971
Hell's Kitchen        1958
East Village          1853
Upper East Side       1798
Crown Heights         1564
Midtown               1545




