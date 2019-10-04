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
### Configuration 

#### Set up your Pyhton environment
Run this command under the root directory of this repository:

```shell
$ pipenv install
```

To create a virtual environment you just execute the `$ pipenv shell` command.


#### Update your tokens 
Update the `DataAcquisition/secrets.py` file by adding your API tokens: 

```
FACEBOOK_TOKEN="your-user-access-token"
YOUTUBE_DEVELOPER_KEY="your-youtube-developer-key"
```

You can follow these two guides to quickly get your [Facebook](https://elfsight.com/blog/2017/10/how-to-get-facebook-access-token/) and [Youtube](https://www.slickremix.com/docs/get-api-key-for-youtube/) tokens.

#### Update your Mongo Database by adding the existing collections (optional, but can save you some time to quickly test the application on existing data input :timer_clock:) 

You can run these commands to synchronize your database with the data we provide: 
```
$ mongoimport --db database --collection rawComments --file ../Databases/rawComments.json
$ mongoimport --db database --collection postsData --file ../Databases/postsData.json
$ mongoimport --db database --collection cleanComments --file ../Databases/cleanComments.json
```


### User manual

#### Data Acquisition (can be skipped)

To run the data acquisition script and update your database with the latest data retrieved from social media, you can run this script: 

```
$ python DataAcquisition/GeneralDataAcquisition.py
```

NB: You can upload the existing databases following the steps in the Configuration part to skip this step. :boom:

#### Data Cleaning (can be skipped)

To clean the rawComments, you can run this script: 
```
$ python Cleaning\ \&\ Scoring\ Comments/cleaningSystem.py
```

NB: You can upload the existing databases following the steps in the Configuration part to skip this step. :boom:


#### TuniMining's Web Application 

To discover our web application and start using sentiment analizer, you can run this command: 
```
$ python TuniMining\ Web\ Application/manage.py runserver
```
These steps will follow: 

1 - Welcome to TuniMining ! :wave:
<p align="center">
  <img src="https://user-images.githubusercontent.com/36090973/66215551-10b84100-e6c4-11e9-9cbb-5aeaef3e761d.png" width="700"/> 
</p>


2 - Choose the category of the entity you want to test ! (Your biggest dilemma :open_mouth:) 
<p align="center">
  <img src="https://user-images.githubusercontent.com/36090973/66218764-1e70c500-e6ca-11e9-816b-6616822428d0.png" width="700"/> 
</p>

3 - Choose the sub-category of the entity you want to test ! (Your second biggest dilemma :astonished:)
<p align="center">
  <img src="https://user-images.githubusercontent.com/36090973/66218784-2df00e00-e6ca-11e9-8fff-c0f3261522a7.png" width="700"/> 
</p>

4 - Choose your entity ! (We're almost done :raised_hands:) 

<p align="center">
  <img src="https://user-images.githubusercontent.com/36090973/66218850-5415ae00-e6ca-11e9-8df6-0e32b2a6cf1b.png" width="700"/> 
</p>

5 - Wait a few seconds (Don't give up! :crossed_fingers:) 

<p align="center">
  <img src="https://user-images.githubusercontent.com/28828162/66238275-1a0ad300-e6ef-11e9-9756-74d48d3330f0.png" width="700"/> 
</p>


6 - Enjoy getting insights on your entity's popularity (Tadaaaa :tada:)

<p align="center">
  <img src="https://user-images.githubusercontent.com/36090973/66215412-c20aa700-e6c3-11e9-9ef1-866180bc4429.png" width="700"/> 
</p>

Hint: You can hover on the charts to get even more insights! 
