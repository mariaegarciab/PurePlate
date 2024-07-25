PurePlate: AI-Driven Quality Control for Food Manufacturing

Overview

PurePlate is an AI-driven solution designed to predict defects in food products during the manufacturing process. Utilizing machine learning, image recognition, and statistical process control, PurePlate aims to enhance product consistency, reduce defects, and improve customer satisfaction.

Repository Contents

	•	Capstone.ipynb: Jupyter Notebook containing the data preparation, training, and evaluation code.
	•	app.py: Flask application for real-time defect detection.
	•	PurePlateApp.html: Front-end interface for real-time object detection.
	•	PurePlate_Report.pdf: Comprehensive report on the project, including objectives, methodology, development, and conclusions.

Installation

	1.	Clone the repository:
 bash
 '''
git clone https://github.com/yourusername/PurePlate.git
cd PurePlate
'''

	2.	Create a virtual environment and install dependencies:
 bash
 '''
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
'''

Usage

	1.	Run the Flask application:
 '''
python3 app.py
 '''

 2.	Open PurePlateApp.html in your browser to access the real-time detection interface.

Data

The dataset used for training the model is available on RoboFlow: Food Ingredients Image Detection.

Model

The YOLOv8 model is used for defect detection. Training and evaluation code is provided in the Capstone.ipynb notebook.

Contributing

Feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

License

This project is licensed under the MIT License.
