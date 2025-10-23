# Voicestack Call Analytics Dashboard

A **Streamlit dashboard** for analyzing dental practice front desk calls. The dashboard provides insights into call volume, status, categories, and sentiment analysis to help optimize operations and improve patient experience.

---

## Features

### Quantitative Metrics
- **Total Calls** – Number of calls in the selected date range.
- **Answered vs Missed Calls** – Monitor front desk efficiency.
- **Average Call Duration** – Identify potential bottlenecks.
- **Booking Rate** – Percentage of calls resulting in bookings.
- **Cancellations** – Track patient cancellations.
- **Call Volume Over Time** – See peak hours and trends.
- **Call Direction** – Split between incoming and outgoing calls.
- **Call Status Distribution** – Visualize answered vs missed vs other statuses.

### Qualitative Metrics
- **Call Categorization** – Categorize calls into:
  - Booking
  - Cancellation
  - Billing
  - Insurance
  - Clinical
  - Other
- **Call Sentiment** – Analyze positivity or negativity of call transcripts.
- **Sentiment by Category** – Understand sentiment trends across different call types.

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/blackmamba-ops/voicestack_dashboard.git
cd Carestack_Assignment
````

2. **Create a virtual environment and activate it**

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Ensure your dataset** `Assignment Dataset.xlsx` is in the project root.

---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open your browser and visit:

* Local: `http://localhost:8501`

---

## Dashboard Interactivity

* **Filters**: Adjust date range, call direction, and call status using the sidebar.
* **KPIs**: Key metrics are displayed at the top.
* **Charts**:

  * Call volume over time
  * Call direction pie chart
  * Call status bar chart
  * Call category bar chart
  * Sentiment distribution histogram
  * Sentiment by category box plot

---

## Data Requirements

The Excel dataset must contain the following columns:

* `Call Time` – DateTime of the call.
* `Call Direction` – Incoming/Outgoing.
* `Call Status` – Answered, Missed, etc.
* `Conversation Duration` – Duration in seconds.
* `transcript` – Text transcript of the call (optional for sentiment and categorization).

---

## Notes

* The current **call categorization** is keyword-based as a placeholder. We can integrate an NLP model (e.g., OpenAI GPT) for more accurate classification or Ollama for local deployment. Currently, I am not using any LLMs because my APIs are exhausted and I do not have a dedicated GPU on my system for running models locally via ollama.
---

## Requirements

* Python >= 3.10
* Streamlit
* pandas
* numpy
* plotly
* textblob
* openpyxl

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## License

This project is for educational purposes and assignment submission.
