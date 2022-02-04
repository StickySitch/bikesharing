# bikesharing
## Overview
In order to decide whether or not Des Moines, Iowa is an viable location for a bike sharing service for our investors; We have analyzed [Citibike's August 2019 bike sharing data](https://s3.amazonaws.com/tripdata/index.html) of Manhattan, New York.

As you will see below, we have used ```Tableau``` to create visualizations of many different aspects of data. Although our data is coming from the best performing month of one of the best performing cities, we can still take these new insights, use a little **critical thinking**, and successfully launch a bike sharing service in Des Moines, Iowa!

## Tableau Dashboard
**`Tableau URL:`** [Dashboard](https://public.tableau.com/app/profile/jack.jones6748/viz/BikeSharingAnalysis-ManhattanNewYork/BikeShareAnalysis?publish=yes)

## Visualizations & Results
Alright, let's dive in! To start, lets take a look at our first slide "Active Locations".
### Active Locations:
![Active Locations](https://github.com/StickySitch/bikesharing/blob/main/resources/Active%20Locations.png)

Above you can see our top starting and ending locations for rides. The markers of a larger size and darker color represent areas of higher use. Based on both of our maps above, our most active locations are those of business (commuters) and tourism. Areas such as Midtown Manhattan. 

### Checkout Times for Users
![Checkout Times for Users](https://github.com/StickySitch/bikesharing/blob/main/resources/Checkout%20Times%20for%20Users.png)
The line chart above is displaying the checkout times of users. When looking at the data, we discovered that 49% of all rentals were returned within 10 minutes of riding. These numbers would support our theory of a large amount of our users being commuters.
Another important point is that 99% of ALL rentals were returned within 60 minutes.  As you can see on the chart, after 5 minutes of riding, the number of bikes starts to decline rapidly. Again supporting the theory that the majority of our users are commuters. Much fewer users are using this service to explore the city.

### Checkout Times by Gender
![Checkout Times by Gender](https://github.com/StickySitch/bikesharing/blob/main/resources/Checkout%20Times%20by%20Gender.png)
Breaking down our checkout times into gender shows us a few things:
- The majority of users are male (65% of all users).
- Checkout times for male and females are similar.
- Unknown users have a steadier amount of users checking out for longer periods of time.
	- This would lead us to believe that a larger amount of our unknown users are likely to be tourists.
### Trips by Weekday Per Hour
![Trips by Weekday Per Hour](https://github.com/StickySitch/bikesharing/blob/main/resources/Trips%20by%20Weekday%20per%20Hour.png)
With the visualization above we can determine our most active times for each day. The darker the color, the higher the concentration of users on that day.
- ##### Weekdays (Monday-Friday)
	-	With weekdays being work days for the majority of our 9-5 workers, our most active times are 7am-9am and 5pm-8pm when people are commuting to work.
- ##### Weekends (Saturday-Sunday)
	-	With the weekends being much more relaxed, people get their days started later and stay our and about much longer. Our most active hours range for weekends is 10am-5pm.
### Trips by Weekday Per Hour by Gender
![Trips by Weekday Per Hour by Gender](https://github.com/StickySitch/bikesharing/blob/main/resources/Trips%20by%20Gender%20%28Weekday%20per%20Hour%29.png)
Right off the bat we can see that both **males and females** have **similar checkout times** again. The **Unknown** users aren't as active in the commuting hours but they do have an increase in use during our **weekend peak hours of 10am-5pm.**
#### Gender ratio:
- ```Females:``` **25%** of all users
- ```Males:``` **65%** of all users
- ```Unknown:``` **10%** of all users

### User Trips by Gender by Weekday and Type
![User Trips by Gender by Weekday and Type](https://github.com/StickySitch/bikesharing/blob/main/resources/tripsbygenderbyweekday.png)
Above we can see our rides broken down by user type (Customer or Subscriber), gender and by each day of the week. This visualization shows us that **81%** of all users are **subscribers**! This along with our subscribers most active days being during weekend; We can deduce once again that our commuting theory is correct!

### Peak Rental Times
![enter image description here](https://github.com/StickySitch/bikesharing/blob/main/resources/Peak%20Hours.png)
Lastly, let's take a look at our overall peak rental hours. Going along with our commuter theory, our peak rental times overall are those that would be used to get to and from work. 
- **Peak Rentals**
	- 8am-10am
	- 5pm-7pm

## Summary
With all of this data there are a few key pieces of information to make note of:
- Areas of high business concentration have the most active bike rental stalls. Areas such as Midtown.
- 49% of all users return their bikes by the 10 minutes mark
- 81% of all users are subscribers

In summary, Des Moines, Iowa could very well be a viable location for a bike sharing service IF a few changes are made. With Manhattan, New York being over 4x smaller in size and having a population 8x bigger than Des Moines, the whole city is practically filled and bike sharing is very practical. So what does this mean for Des Moines? Well it means that in order to make this work, we would need to concentrate our bike sharing stalls in high business areas of Des Moines.

#### Additional Insights
In order to decide whether Des Moines is truly a viable option, a few more visualizations could be created:
- A visualization showing not only the starting and ending locations but also the riders routes and the distances traveled would be useful in determining if they use the bike for the whole commute or are they possibly catching a train before or after renting.
- Add a visualization of bike rental activity by age group. With this data we can determine the ages that rent the most and use this information to target that demographic.
