# TuniMining

A web-based platform for visualization and tracking of public opinion and e-reputation in Tunisia based on social media analytics :tunisia:!


<p align="center">
  <img src="https://media.giphy.com/media/el134f6EXdGjWtDWqO/giphy.gif" width="600"/> 
</p>

The idea of Social Network Analysis is that by studying people’s interactions, one can
discover and understand people’s opinions about brands, companies, sport, art , public
figures and also determine their popularity; in addition to detecting changes in group
dynamics over time. 

Following the same state of mind, TuniMining has been created to collects data using social media APIs and performs sentiment analysis to get meaningful insight behind the data about relevant subjects in Tunisia. The architecture of the application can be devided into 4 main sub-systems:

:fuelpump: <b> Data Acquisition System </b> 

Extracting comments of Tunisian users with Facebook Graph API and Youtube API.

:bath: <b> Data Cleaning System </b>

The cleaning of the comment text is based on normalizing the data and removing useless terms in order to smooth the matching with the pre-established sentiment dictionary.

:heart: <b> Sentiment Analysis </b> 

Determining the polarity of the comments based on a sentiment dictionary approach. The dictionary was built manually based on the commonly used tunisian dialect expressions (in both latin and arabic characters) and a subjective scoring system.

:bar_chart: <b> Visualization Tool </b> 

The results of the analysis will be displayed in the form of trend diagrams which indicate diﬀerent levels of popularity and polarity.




## Getting Started

### Prerequisites

```
python3
```

### Installation

### Configuration 

### User manual

<p align="center">
  <img src="https://user-images.githubusercontent.com/36090973/66215551-10b84100-e6c4-11e9-9cbb-5aeaef3e761d.png" width="700"/> 
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/36090973/66218764-1e70c500-e6ca-11e9-816b-6616822428d0.png" width="700"/> 
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/36090973/66218784-2df00e00-e6ca-11e9-8fff-c0f3261522a7.png" width="700"/> 
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/36090973/66218850-5415ae00-e6ca-11e9-8df6-0e32b2a6cf1b.png" width="700"/> 
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/36090973/66215412-c20aa700-e6c3-11e9-9ef1-866180bc4429.png" width="700"/> 
</p>





