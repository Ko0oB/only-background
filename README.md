# Photo Motion Remover
---

<a name="readme-top"></a>
<!-- TABLE OF CONTENTS -->

## 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
- [🧩 Project Structure](#project-structure)
- [💻 Getting Started](#getting-started)
  - [Setup](#setup)
  - [Install](#install)
- [🚀 Demo](#demo)
- [👥 Author](#author)
- [🔭 Future Features](#future-features)
- [🤝 Contributing](#contributing)
- [⭐️ Show your support](#support)
- [📝 License](#license)
<!-- - [🙏 Acknowledgements](#acknowledgements)-->

<!-- PROJECT DESCRIPTION -->
## 📖 About the Project <a name="about-project"></a>

Simple Flask web application to remove moving objects from a series of photos.  


## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details>
  <summary>Backend</summary>
  <ul>
    <li><a href="https://www.python.org/">Phyton</a></li>
    <li><a href="https://palletsprojects.com/projects/flask">Flask</a></li>
    <li><a href="https://numpy.org/">NumPy</a></li>
    <li><a href="https://docs.opencv.org/4.x/index.html">OpenCV</a></li>
  </ul>
</details>
<details>
  <summary>Frontend</summary>
  <ul>
    <li><a href="https://www.w3.org/TR/html52/">HTML5</a></li>
    <li><a href="https://www.w3.org/Style/CSS/Overview.en.html">CSS3</a></li>
    <li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript">JavaScript</a></li>
    <li><a href="https://getbootstrap.com/docs/5.3/">Bootstrap 5</a></li>
  </ul>
</details>


<!-- Features -->

### Key Features <a name="key-features"></a>

Features:

- Upload multiple photos at once (minimum 2)  
- Automatic resizing and alignment to the first image  
- Moving object removal based on pixel variance analysis  
- Displays processing time information  
- Before and after preview in the UI  
- Download processed image

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- PROJECT STRUCTURE -->

## 🧩 Project Structure <a name="project-structure"></a>

```sh
only-background/
│
├── app.py
│
├── static/
│   ├── script.js          # Handles file upload, sends images to the backend, shows progress...
│   └── style.css          # Custom CSS styles
├── templates/
│   └── index.html         # HTML template with Bootstrap
├── uploads/               # folder created at runtime to store uploaded images
├── results/               # folder with output picture
│
├── images/
│   └── screenshot.png     # Screenshot from web application
├── requirements.txt
└── README.md
```

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>

To get a local copy up and running, follow these steps.

### Setup
Clone this repository to your desired folder:

```sh
  git clone https://github.com/Ko0oB/only-background.git
```
or 
```sh
  git clone git@github.com:Ko0oB/only-background.git
```
Create and activate virtual environment
```sh
  python -m venv venv

    # Windows
  venv\Scripts\activate

    # Linux / macOS
  source venv/bin/activate
```

### Install
Install dependencies:
```sh
  pip install -r requirements.txt
```

### Usage
Run the Flask app:
```sh
  python app.py
```
Open your browser at http://127.0.0.1:5000 or http://localhost:5000/ 

Submit as many of the same size photos as possible.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- DEMO -->

## 🚀 Demo <a name="demo"></a>

![Demo](images/screenshot.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- AUTHORS -->

## 👥 Authors <a name="author"></a>

👤 **Konrad "KoB"**

- GitHub: [@Ko0oB](https://github.com/Ko0oB)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE FEATURES -->

## 🔭 Future Features <a name="future-features"></a>

- **Improve moving object removal algorithm/method**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/Ko0oB/Sudoku/issues)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

Give a ⭐️ if you like this project!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->
<!-- 
## 🙏 Acknowledgments <a name="acknowledgements"></a>

N/A

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->
<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
