# Supervised ML Algorithms End-to-End Machine Learning Project

An end-to-end machine learning project demonstrating the complete workflow from data preprocessing and model development to deployment and monitoring.

## Overview

This project showcases the full lifecycle of a machine learning application, including data preprocessing, feature engineering, model training, evaluation, and deployment. The application is designed to be modular and scalable, adhering to best practices in MLOps. The project is aimed at predicting student marks by considering various features.

## Technologies Used

- **Programming Languages**: Python
- **Machine Learning Frameworks**: Scikit-learn
- **Machine Learning Models Implemented**:
  
  ```
        "Linear Regression": LinearRegression(),
        "Gradient Boosting": GradientBoostingRegressor(),
        "K-Neighbours Regressor": KNeighborsRegressor(),
        "Decision Tree": DecisionTreeRegressor(),
        "Random Forest": RandomForestRegressor(),
        "Cat Boost Regressor": CatBoostRegressor(),
        "Ada Boost Regressor": AdaBoostRegressor()
  ```
  
- **Web Framework**: Flask
- **Containerization**: Docker
- **Deployment**: AWS EC2, AWS ECR, Docker, AWS Elastic Beanstalk
- **Version Control**: Git
- **Continuous Integration/Continuous Deployment (CI/CD)**: GitHub Actions

## Project Structure

The project is organized as follows:

```

ML-end-to-end/
├── .ebextensions/         # Elastic Beanstalk configuration files
├── .github/workflows/     # GitHub Actions workflows
├── artifacts/             # Model artifacts and outputs
├── notebook/              # Jupyter notebooks for exploration and prototyping
├── src/                   # Source code for data processing and modeling
│   ├── __init__.py
│   ├── data_processing.py
│   └── model.py
├── templates/             # HTML templates for Flask application
├── .gitignore             # Git ignore file
├── Dockerfile             # Docker configuration
├── README.md              # Project documentation
├── application.py         # Flask application
├── requirements.txt       # Python dependencies
└── setup.py               # Package setup
```



## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SayamKhatri/ML-end-to-end.git
   ```


2. **Navigate to the project directory**:
   ```bash
   cd ML-end-to-end
   ```


3. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```


4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```


## Usage

1. **Run the application**:
   ```bash
   python application.py
   ```

   Access the application at `http://127.0.0.1:5000/`.

## Deployment

The application is containerized using Docker for consistent deployment across environments.

1. **Build the Docker image**:
   ```bash
   docker build -t ml-end-to-end .
   ```


2. **Run the Docker container**:
   ```bash
   docker run -p 5000:5000 ml-end-to-end
   ```

   The application will be accessible at `http://localhost:5000/`.

For cloud deployment, AWS Elastic Beanstalk configurations are provided in the `.ebextensions` directory.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
