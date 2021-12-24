<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="">
    <img src="https://key0.cc/images/preview/27177_e37c477ada017fd7cc4ecc3ac315a21a.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">K8S App</h3>
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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project is intended to be built for learning porpuses following DevOps ideals

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Docker](https://www.docker.com/)
* [Minikube](https://kubernetes.io/es/docs/tutorials/hello-minikube/)
* [Python3.9](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Flask-Restx](https://flask-restx.readthedocs.io/en/latest/)
* [Javascript](https://www.javascript.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

In order to make the project work you need minikube and docker installed and start minikube with Docker as driver: **minikube start --driver=docker**.


### Installation

_This project has been build in a Debian 11 image running in VirtualBox_

1. Clone the repo 
   ```sh
   git clone https://github.com/walterbaidal/k8s-app.git
   ```
   
2. Run the minikube environment
   ```sh 
    eval $(minikube docker-env)
   ```
3. Build backend-image and run manifests
   ```sh
   cd /k8s-app/backend/
   docker build -t k8s-backend .
   kubectl apply -f k8s-backend.yaml
   ```
   
4. Build frontend-image and run manifests
   ```sh
   cd /k8s-app/frontend/
   docker build -t k8s-frontend .
   kubectl apply -f k8s-frontend.yaml
   ```
   
5. Run service from minikube
   ```sh
   minikube service frontend-k8s-app
   ```  


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Work in progress 

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Walter Baidal - [@NatsukashiiNee](https://twitter.com/NatsukashiiNee) - walterbaidal96@gmail.com

Project Link: [https://github.com/walterbaidal/k8s-app](https://github.com/walterbaidal/k8s-app)

<p align="right">(<a href="#top">back to top</a>)</p>