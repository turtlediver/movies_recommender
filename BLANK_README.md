<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
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




<!-- PROJECT LOGO -->
<br />
<div align="center">


<h3 align="center">REEL RECS</h3>

  <p align="center">
    A movie recommendation app to find your next watch.
    
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This application recommends a selection of 10 movies based on a movie title provided by the user. Recommendations are chosen based on Collaborative Filtering. We use a movie ratings dataset to look at all other movies liked by users who watched and liked (i.e. rated at least 5/10) the provided movie title. These users are Similar Users. Then, sort the movies based on how many users from Similar Users liked each movie. Finally, take the top 10 movies from the sorted set of movies.

Recommendations are further personalized with the help of Cohere AI Chat bot. On the recommended movies page, mousing over each movie's icon will reveal a short text explaining why the user will enjoy the recommendation, based on their inputted movie.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Flask
* Bootstrap
* Sci-kit Learn
* Pandas
* JavaScript


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps:

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python installations:
  ```
  pip install Flask
  pip install python-dotenv
  pip install pandas
  pip install numpy
  pip install -U scikit-learn
  
  ```
* TMDB API Key
  - create an account on https://developer.themoviedb.org/docs/getting-started
* Cohere API Key 
 - create an account on https://docs.cohere.com/docs/chat-api

### Installation

1. Clone this repo to your local system.
2. Download user ratings ml-25m dataset to root directory of this project:
   https://grouplens.org/datasets/movielens/25m/
3. Create a new file ```.env``` in root directory.
   - file contents should be as follows:
     ```
     TMDB_API_KEY="<Your TMDB API key>"
     COHERE_API_KEY="<Your Cohere API key>"
     ```
4. Run ```flask run``` in the root directory and open the 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Under Construction

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Future improvements
Under Construction

<p align="right">(<a href="#readme-top">back to top</a>)</p>



