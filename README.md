[![LinkedIn][linkedin-shield]][linkedin-url]
</br>

# Directory Hunt

<!-- TABLE OF CONTENTS -->
<details open="open">
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
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A GET REST API that takes in a path given by the user. We run the "ls -la" 
OS command on the path and translate the output into JSON format. This
application is Dockerized with unit tests.

### Built With

* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/downloads/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Pytest](https://docs.pytest.org/en/stable/)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Docker
  ```sh
  brew cask install docker
  ```

### Installation

1. Run in terminal of your choice:
   ```sh
   ./getpath.sh
   ```
NOTE: Some paths you may need give Docker permission to access!

2. Open in browser of your choice this link:
   ```
   http://0.0.0.0:80
   ```

### Testing
* Run Pytest
   ```sh
   pytest
   ```

### Docs

See swagger.yaml file in the repository for Swagger style documentation

<!-- CONTACT -->
## Contact

Rebecca Hsieh - rebecca.hsieh07@gmail.com - therealslimhsiehdy.com


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/therealslimhsiehdy