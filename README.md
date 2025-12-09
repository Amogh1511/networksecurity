### End to end Network security 
to activate the environment use below line
"  .venv\Scripts\activate  "

uvicorn cmd - uvicorn app:app --reload
fastapi link
http://127.0.0.1:8000
docs- http://127.0.0.1:8000/docs
Fastapi Train route - http://127.0.0.1:8000/docs#/default/train_oute_train_get
Fastapi Predict route - http://127.0.0.1:8000/docs#/default/predict_route_predict_get

Summary
- This project builds an end-to-end machine learning pipeline to detect phishing websites. 
- It automates data ingestion, preprocessing, model training, evaluation, and prediction. 
- The system is served through a FastAPI application, allowing users to submit website features and get a phishing/non-phishing prediction. 
- The project follows modular, production-ready architecture with logging, configuration management, exception handling, and artifact tracking.
- This project is an end-to-end machine learning system for phishing website detection. 
- It automates the full workflow — data ingestion, feature engineering, model training, evaluation, and deployment. 
- A FastAPI-based service exposes the trained model for real-time predictions. The project is structured using a modular, production-ready architecture with proper logging, configuration files, custom exceptions, and artifact tracking. 
- It helps identify malicious websites by analyzing key URL and website behavior features, enabling fast and reliable phishing detection.


D:\MyProjects\networksecurity\network_data\phisingData.csv