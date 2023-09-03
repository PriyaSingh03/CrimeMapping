# MAPPING OF CRIMES IN INDIA 


![Crime Mapping Logo](https://github.com/PriyaSingh03/CrimeMapping/assets/107784525/74d9689f-0f6c-482d-b5c9-0dc830103dc5)


# Abstract

The Crime Mapping Project is a comprehensive analysis and visualization initiative aimed at understanding crime patterns, trends, and hotspots across various regions in India. This documentation provides detailed insights into data collection, preprocessing, and the use of advanced visualization techniques to gain actionable insights from crime data.

# Introduction

Crime mapping is crucial for law enforcement agencies and policymakers to allocate resources effectively and develop targeted crime prevention strategies. This documentation outlines the methodologies, tools, and insights gained from the Crime Mapping Project.

# Data Collection

### Data Sources
- Collection of criminal data or FIR data is challenging as these are sensitive and confidential data.
- Data collection and manipulation of data required most brainstorming and time during our project as there is no predefined dataset on the Internet for this problem statement So we had to create and collect a dataset of our own.
- We somehow through our research managed to get some raw and unfiltered data which was mostly imbalance and filled with null values
- We used some datasets from `data.world` and `Harvard's dataverse`

### Data Preprocessing
- We performed some data preprocessing steps, such as cleaning, handling missing values, and standardization.
- As we collected datasets from various sources, we had to concat as well as discard many unnecessary data which was not needed
- We converted data to our required data types and shaped it according to our needs.
- Then, we performed EDA of all the collected datasets to brainstorm how can we find relations between these datasets and these vast data points

### Feature Engineering
- The data that we collected, analyzed and manipulated was not enough for a criminal mapping website.
- We had to extract data-time from other datasets and feature-scaled the data-time data to fulfil all the data point values
- We also need to find the location with the exact longitude and latitude for plotting our data on the map. As there is no such data on the Internet, we Geocoded our own dataset to find the locations along with their exact longitude and latitude

# Visualization and Analysis

### Plotting First Information Report(FIR) Details on the Map
- We used `Streamlit`, `Mapbox` and `Folium` to visualize the data on the map. Then we converted the data into two types of markers: `Normal` and `DateTime`
- The Normal marker shows all the Fir locations with respect to their Police Station addresses.
- Provide a step-by-step guide to plotting FIR details on interactive maps.
* Significance of different color markers helps use to **visualize crime patterns** in different DateTime :
  - ### Green Marker &#x1F7E2;
    <span style="color: green;">Green Marker for depicting crimes committed in Morning or Noon</span>

  - ### Blue Marker &#x1F535;
    <span style="color: blue;">Blue Marker for depicting crimes committed in Evening or Night</span>

    ![Map marker example](https://github.com/PriyaSingh03/CrimeMapping/assets/107784525/ac66c238-c98f-4a83-b4d5-753acbcc3b25)



- We only made the dataset for Uttar Pradesh as we had a shortage of time collecting and making new data for all FIR's in India is a lengthy process
  


# Visualizing Crime Data All Over India

* Normal Map with Red Markers: Initially, a standard map is displayed, showcasing numerous crime incidents all over India. Each crime is marked with a red marker to provide a comprehensive view of the distribution of crimes across the country.
* Crime Rate by State and Crime Type: A plot is generated to display the crime rate in each state, along with the types of crimes committed. This helps in identifying regions with higher crime rates and understanding the distribution of different crime types within each state.
* Crime Rate for All States with Respective Crime Types: Another visualization illustrates the crime rate for all states in India, highlighting the specific types of crimes prevalent in each state. This information can be valuable for law enforcement agencies to allocate resources effectively.
  

 <img src="https://github.com/PriyaSingh03/CrimeMapping/assets/107784525/66adb212-9720-49dd-ab07-54527ec17935" alt="drawing" style="width:600px"/>


# Genetrating hotspots for particular types of crime(under IPC section)

* In this feature, we map the crimes on the basis of their `IPC section`. With the help of this analysis, we are able to clearly see the regions in which a particular pattern of crimes(under the IPC section) is more prevalent. This can help us to visualise the behavioural patterns of criminals. 
* Also we can slightly predict the financial condition of the region by filtering the regions that have more cases of robbery, fraud(IPC 420) and dacoity, depicting the people of the region are more wealthier and thus accused of this type of crimes.

![image](https://github.com/PriyaSingh03/CrimeMapping/assets/107784525/09e2060f-de48-4201-a638-91cbfa210ee9)


# Conclusion

In conclusion, the Crime Mapping Project has provided valuable insights into crime patterns and hotspots based on IPC sections. Data-driven decision-making is crucial in crime prevention and law enforcement. Future directions include expanding the project and incorporating additional data sources for more effective crime reduction strategies

## Acknowledgments
We would like to express our sincere gratitude and appreciation to everyone who contributed to the success of this Crime Mapping project. Without their support, expertise, and dedication, this project would not have been possible.

## References
- https://data.world/
- https://dataverse.harvard.edu/
- https://ncrb.gov.in/en/crime-and-criminal-tracking-network-systems-cctns
- https://justicehub.in/

---
