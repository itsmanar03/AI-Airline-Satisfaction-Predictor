<h1 align="center">✈️ AI Airline Satisfaction Predictor</h1>

<p align="center">
  <strong>An End-to-End Machine Learning application to predict passenger satisfaction using advanced ensemble methods and interactive analytics.</strong>
</p>

<hr>

<h2>📊 Model Performance & Results</h2>
<p>During the development phase, two powerful ensemble models were evaluated. Based on the final evaluation metrics, both models achieved exceptional performance, with <strong>Random Forest</strong> slightly leading in overall accuracy.</p>

<ul>
  <li><strong>Random Forest Performance:</strong> Accuracy 92.92% | Precision 91.98% | Recall 91.65% | F1-Score 91.81%</li>
  <li><strong>XGBoost Performance:</strong> Accuracy 95.36% | Precision 95.52% | Recall 93.69% | F1-Score 94.60%</li>
</ul>

<blockquote>
  <strong>Note:</strong> Although Random Forest achieved the highest accuracy by a narrow margin, both models demonstrate high reliability for predicting passenger satisfaction.
</blockquote>

<hr>

<h2>🛠️ Key Features</h2>
<ul>
  <li><strong>Predictive Modeling:</strong> High-accuracy classification using fine-tuned ensemble methods.</li>
  <li><strong>Exploratory Data Analysis (EDA):</strong> Deep data insights using correlation heatmaps and distribution plots.</li>
  <li><strong>Interactive Dashboard:</strong> A professional Streamlit UI with Dark/Light mode support.</li>
  <li><strong>Visual Insights:</strong> Real-time prediction confidence tracking using Plotly Gauge charts.</li>
  <li><strong>Efficient Preprocessing:</strong> Automated pipeline for Label Encoding and Feature Scaling.</li>
</ul>

<hr>

<h2>🚀 Technologies Used</h2>
<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-31363C?style=for-the-badge&logo=matplotlib&logoColor=white" />
  <img src="https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" />
</p>

<hr>

<h2>📁 File Structure</h2>
<ul>
  <li><strong>airline_sat.ipynb:</strong> Detailed Jupyter Notebook containing EDA, Feature Engineering, and Model Comparison.</li>
  <li><strong>app.py:</strong> Streamlit application file for real-time predictions.</li>
  <li><strong>xgb_model.pkl:</strong> The trained and saved model file.</li>
  <li><strong>label_encoder.pkl & model_columns.pkl:</strong> Metadata for ensuring input consistency.</li>
</ul>

<hr>

<h2>⚙️ Installation & Usage</h2>

<h3>1. Clone this repository:</h3>
<pre><code>git clone [your-repo-link]</code></pre>

<h3>2. Install the required libraries:</h3>
<pre><code>pip install streamlit pandas xgboost joblib plotly scikit-learn matplotlib seaborn</code></pre>

<h3>3. Launch the dashboard:</h3>
<pre><code>streamlit run app.py</code></pre>
