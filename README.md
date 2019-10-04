# TuniMining

A web-based platform for visualization and tracking of public opinion and e-reputation in Tunisia based on social media analytics :tunisia:!


<p align="center">
  <img src="https://media.giphy.com/media/el134f6EXdGjWtDWqO/giphy.gif" width="600"/> 
</p>

TuniMining collects data using social media APIs and performs sentiment analysis to get meaningful insight behind the data about relevant subjects in Tunisia. 

The application is devided into 4 main sub-systems:

:fuelpump: <b> Data Acquisition System :</b> 

Extracting comments of Tunisian users with Facebook Graph API and Youtube API.

:bath: <b> Data Cleaning System :</b>

The cleaning of the comment text is based on normalizing the data and removing useless terms in order to smooth the matching with the pre-established sentiment dictionary.

:heart: <b> Sentiment Analysis :</b> 

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


