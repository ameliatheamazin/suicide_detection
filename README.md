<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ameliatheamazin/suicide_detection">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Suicide Ideation Detection System for Tweets</h3>

  <p align="center">
    <br />
    <a href="https://github.com/ameliatheamazin/suicide_detection"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ameliatheamazin/suicide_detection">View Demo</a>
    &middot;
    <a href="https://github.com/ameliatheamazin/suicide_detection/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/ameliatheamazin/suicide_detection/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>




<!-- ABOUT THE PROJECT -->
## About The Project



A final-year project aimed at building a real-time web application that integrates Random Forest model to enable real-time classification of tweets fetched through Twitter API into its associated level of suicide risk (`low`, `medium`, `high`) and to trigger an appropriate crisis response.


### Built With

* [![Flask][flask]][flask-url]
* [![Jinja Template][jinja-template]][jinja-template-url]
* [![Node][node]][node-url]
* [![Socket.io][socket.io]][socket-url]
* [![Twitter API][twitter-api]][twitter-api-url]


  
### 📄 Research Publications

**Towards A Machine Learning Framework for Suicide Ideation Detection in Twitter**  
🔗 [Read the full article](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=bmnt0JcAAAAJ&authuser=1&citation_for_view=bmnt0JcAAAAJ:u5HHmVD_uO8C)

**Characteristics of Multi-Class Suicide Risks Tweets Through Feature Extraction and Machine Learning Techniques**  
🔗 [Read the full article](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=bmnt0JcAAAAJ&authuser=1&citation_for_view=bmnt0JcAAAAJ:u-x6o8ySG0sC)
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- OVERVIEW -->
## Overview

The system classifies tweets into multiple suicide risk levels and can respond automatically or flag for moderation. It incorporates natural language processing (NLP), feature extraction techniques, machine learning, and real-time monitoring.

### Features

* Tweet scraping using Twitter API to build training set

* Preprocessing: tokenization, stopword removal, POS tagging

* Classification into suicide risk levels

* Automated responses for high-risk posts

* Flask web app for demonstration

### Tech Stack

1. Training data: Twitter API
   
3. Python: scikit-learn, NLTK (VADER), Pandas, Pickle

3. Frontend: Jinja2, Bootstrap, Chart.js

4. Backend: Flask, Node



## ▶️ How to Access this Repo?

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ameliatheamazin/suicide_detection.git
   ```
2. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. Run `python app.py`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Usage

1. Launch the web app

2. Input tweets manually or stream real-time tweets

3. See classification results and system responses

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## 📊 Dataset
- Recommended to use datasets related to mental health on textual social media posts
- _For training datasets, please contact author_
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🧠 Model Training
1. Preprocessing: Removal of redundant words (whitespace, symbols) ,lemmatization and tokenization

2. Feature extraction: PoS tagging, VADER (Sentiment analysis), TF-IDF (vector representation of tweets), 

3. Model training: Random Forest, evaluated across accuracy, precision and recall

4. Model integration: Serialized model with Pickle
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🌐 Web App Features
1. Built with Flask, equipped with Bootstrap and Jinja2 template for basic UI and chart.js for real-time tweet analysis chart

3. Crisis resource linking and alert mechanism

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# 🔑 Key Findings

## 1. Linguistic and Sentiment Patterns as Risk Indicators
- The model effectively captures linguistic features — such as sentiment scores, TF‑IDF weighted terms, and part-of-speech patterns — that correspond to different **levels of suicide ideation**.
- It learned to detect subtle differences in word choice, syntax, and emotional tone that signal increasing risk.

## 2. Importance of Contextual Features
- The **context** surrounding words — not just isolated terms — plays a critical role in model performance.
- Correct interpretation requires context to form accurate sentiment and TF‑IDF understanding, which enhances classification capabilities.

## 3. Generalizability and Real-Time Effectiveness
- When tested on random sample data flows, the system maintained performance, indicating good **generalization to unseen tweets**.
- This supports the model’s **practical viability** for real-time monitoring in a deployed (Flask‑based) environment.

## 4. Integrated Real-Time Response Mechanism
- Medium and high risk tweets trigger **automated care messages** and links to mental health resources.
- **High-risk** cases are **flagged for moderator review**, demonstrating a functional and validated integration of detection and crisis response in real time.


## ⚖️ Ethical Considerations

* No real-time deployment without human oversight

* Data anonymized and used for academic research

* Must comply with platform and privacy policies

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Amelia Lim - amelialimyq@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## 🙏 Acknowledgments

* Dr. Loo Yim Ling, my advisor, for her invaluable guidance, continuous support, and insightful feedback throughout the project.
* My family, who has always encouraged, supported and inspired me to achieve my full potential.
* The online research/ tech community for providing the necessary resources to conduct the study.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ameliatheamazin/suicide_detection.svg?style=for-the-badge
[contributors-url]: https://github.com/ameliatheamazin/suicide_detection/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ameliatheamazin/suicide_detection.svg?style=for-the-badge
[forks-url]: https://github.com/ameliatheamazin/suicide_detection/network/members
[stars-shield]: https://img.shields.io/github/stars/ameliatheamazin/suicide_detection.svg?style=for-the-badge
[stars-url]: https://github.com/ameliatheamazin/suicide_detection/stargazers
[issues-shield]: https://img.shields.io/github/issues/ameliatheamazin/suicide_detection.svg?style=for-the-badge
[issues-url]: https://github.com/ameliatheamazin/suicide_detection/issues
[license-shield]: https://img.shields.io/github/license/ameliatheamazin/suicide_detection.svg?style=for-the-badge
[license-url]: https://github.com/ameliatheamazin/suicide_detection/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/amelialimyq
[flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[flask-url]: https://flask.palletsprojects.com/
[twitter-api]: https://img.shields.io/badge/Twitter%20API-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white
[twitter-api-url]: https://developer.twitter.com/en/docs/twitter-api
[socket.io]: https://img.shields.io/badge/Socket.io-010101?style=for-the-badge&logo=socket.io&logoColor=white
[socket-url]: https://socket.io/
[node]: https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white
[node-url]: https://nodejs.org/
[jinja-template]: https://img.shields.io/badge/Jinja-FFC107?style=for-the-badge&logo=jinja&logoColor=black
[jinja-template-url]: https://jinja.palletsprojects.com/
