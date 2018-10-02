# IBM Hack Challenge:  _A Mega Hackathon_

### Problem Statement III:  _Help me with my mood_

#### Help me with my Mood with Social-media Health Analysis and Display Engine (SHADE).

#### About the challenge

With the advances in technology about sentiment analysis and predictive analytics, it has opened many avenues for researchers and enterprises to understand human mental state better. The proposed challenge is to know the emotion/mood of a person, to help in eliminating any negative state of mind that might have adverse effect on his/her daily life.

#### Technologies used

-   Flask
-   Python v3.6.6
-   IBM Watson Tone Analyser API
-   Tweepy: Twitter API, etc.

### Application is deployed on Heroku

Our application is deployed on Heroku. Visit @ https://mood-swinger.herokuapp.com/

### Slides

We have pretty visualized slides which you evaluate for easy understanding of our app
-   Visit @  https://docs.google.com/presentation/d/1yciFYJraSR2lbMLIkZU4witeEAcG-ogADpm3Tl8l-9w/edit?usp=sharing
-   Else, search the repo for "IBMHackChallenge.pdf"

### Documentation

As instructed documentation in similar format is compiled for your ready perusal. We hope you like it.
-   Visit @  https://docs.google.com/document/d/1r0oiZRN78aMfSo070vxci2c2a35lFti7mkbrBPWHG3s/edit?usp=sharing
-   Else, search the repo for "Documentation.pdf"

### Running the app locally

Pre-requisites: [You need tokens for Twiiter and IBM Watson Tone Analyser API]

Example, on bash/zsh add this lines to .bashrc located in :

```
nano ~/.bashrc
```

Add these following lines and the values:

```
export TWITTER_CONSUMER_KEY=
export TWITTER_CONSUMER_SECRET=
export TWITTER_ACCESS_TOKEN=
export TWITTER_ACCESS_TOKEN_SECRET=
export TONE_ANALYSER_USERNAME=
export TONE_ANALYSER_PASSWORD=
```

Now refresh:

```
source ~/.bashrc
```

----------

1.  Clone the repo
2.  Go to root directory of the repo cloned
3.  Setup a virtual environment by executing the command venv:

```
python3 -m venv /path/to/new/virtual/environment 
Example: python3 -m venv env
```

4.  Once a virtual environment has been created, it can be “activated” using a script in the virtual environment’s binary directory. The invocation of the script is platform-specific:

| Platform | Shell | Command to activate virtual environment |
|------- | ------- | ----------------------------- |
| POSIX | bash/zsh | `$ source /bin/activate` |
| POSIX |fish | `$ . /bin/activate.fish` |
| POSIX |csh/tcsh | `$ source /bin/activate.csh` |
| Windows |cmd.exe | `C:> \Scripts\activate.bat` |
| Windows | Powershell | `PS C:> \Scripts\Activate.ps1` |

In my case,  **Platform: Ubuntu (POSIX Compliant)**  and  **Shell: zsh**  So,

```
source env/bin/activate
```

5.  Install all the packages from requirements.txt

```
pip install -r requirements.txt
```

6.  Run run.py

```
python run.py
```

7.  Application will start on  **localhost**  :  **port**

Congratulations, you have successfully fired the application up.