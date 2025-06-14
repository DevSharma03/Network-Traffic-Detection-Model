# 📡 Network Traffic Detection Model

A smart anomaly detection system built using R for intelligent network traffic analysis and Python Flask for web deployment. This model identifies unusual traffic patterns to flag potential fake or malicious activity.

## 🧠 Features

- Real-time anomaly detection using Isolation Forest  
- Simulated traffic data generation and validation  
- Geolocation mapping with Leaflet in R  
- Interactive ROC and Precision-Recall plots  
- Integrated Flask web server to host the anomaly map  

## 🛠️ Tech Stack

- **Language**: R, Python  
- **ML & Data**: `isotree`, `caret`, `pROC`, `yardstick`  
- **Visualization**: `ggplot2`, `leaflet`, `patchwork`  
- **Web App**: Flask (Python)  
- **Maps**: Leaflet.js via R `leaflet` package  

## 📁 Project Structure

``` bash
Network-Traffic-Detection-Model/
├── leaflet_map.html # Generated interactive map
├── leaflet_map_files/ # Supporting static assets for the map
├── app.py # Flask web server to serve the map
├── NetworkDetection.ipynb # R notebook with full pipeline (data, model, plots)
├── templates/
│ └── index.html # Template HTML file to embed map
└── README.md # Project documentation
```


## 🚀 Getting Started

### 1. Run the R Script

Use RStudio or an R environment to open and execute `NetworkDetection.ipynb`.

This script:
- Simulates network traffic  
- Trains an Isolation Forest model  
- Scores traffic for anomalies  
- Visualizes results with maps and plots  
- Saves `leaflet_map.html` for web use  

### 2. Start the Flask Server

Make sure the R script has generated `leaflet_map.html`.

Then run the Flask app:

```bash
pip install flask
python app.py
```

Visit http://127.0.0.1:5000 to view the interactive map.


## 📊 Sample Results

- Accuracy: ~91.5%
- AUC (ROC): 0.988
- Visualizations include:
- ROC Curve
- Precision-Recall Curve
- Confusion Matrix Heatmap
- Anomaly Score Distribution
- Leaflet-based anomaly map


## 📜 License
This project is licensed under the [MIT License](LICENSE).


## 📬 Contact
For any inquiries, feel free to reach out via work.devashishsharma09@gmail.com or open an issue. 
Let me know if you need any more changes! 🚀😊
