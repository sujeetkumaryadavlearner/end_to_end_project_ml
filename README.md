🪙 Diamond Price Prediction - End-to-End ML Project
This project involves building an end-to-end Machine Learning pipeline for predicting the price of diamonds based on key features such as carat, cut, color, clarity, and dimensions. The pipeline covers everything from data preprocessing and model training to deployment on AWS.

🔧 Technologies & Tools Used
Python, Pandas, NumPy, Scikit-learn

Regression, SVR, Decision Tree Regressor

Matplotlib, Seaborn (Data Visualization)

Docker, AWS EC2, AWS ECR

GitHub Actions (CI/CD)

Logging, config.yaml, and .env for configuration

OS-independent path handling using os.path.join

🚀 Deployment
Live App: http://54.81.129.195:8080

GitHub Repository: end_to_end_project_ml

📌 Key Features
Trained using multiple algorithms including Linear Regression, Support Vector Regressor, and Decision Tree Regressor

Preprocessing includes scaling, encoding, handling outliers, and null values

CI/CD pipeline using GitHub Actions for automated testing and deployment

Dockerized and deployed on AWS (ECR + EC2)

Proper logging and structured configuration using YAML and .env files

🧠 Key Learnings
Machine Learning is not just about .predict() – A real ML project involves managing configurations, environment setup, deployment, and monitoring.

Configuration Management – Learned to use config.yaml and .env files to manage environment-dependent settings, improving scalability and flexibility.

Importance of Logging – Logs are critical for debugging, especially during model training, deployment, and CI/CD automation.

Cross-platform Path Handling – Faced an issue where a Windows-style path caused errors on a Linux-based AWS EC2 instance. Resolved it by using os.path.join for OS-independent path construction.

DevOps Integration – Understood the importance of integrating DevOps practices (CI/CD) in ML workflows to streamline deployment and collaboration.

⚠️ Challenges Faced
Encountered platform dependency issues due to hardcoded Windows paths when running the code on a Linux-based EC2 instance.

Faced initial difficulties in configuring GitHub Actions for automated deployment but successfully overcame them with iterative testing and YAML debugging.
