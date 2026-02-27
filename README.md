---

# Analytical Dashboards with Plotly Dash

This repository contains a collection of interactive analytical dashboards built using Python, Dash and Plotly. The project is currently in an experimental phase, serving as a sandbox to explore data visualization techniques, dashboard layouts, and the implementation of advanced components.

## Features

* **Diverse Visualizations:** Includes Histograms, Pie Charts, Treemaps, Geo-scatter maps, and Bubble charts.
* **Interactive Components:** Real-time data updates using Dash callbacks.
* **Multi-Page Support:** Configured using `dash.register_page` for scalable application structure.
* **Custom Styling:** Integration of `dash-bootstrap-components` and custom CSS classes for card-based layouts and themed UI.

## Project Structure

```text
├── assets/                 # Logo and CSS
├── data/                   # Data source
├── pages/
│   ├── grapConfig/         # Graphs global config
│   ├── graphs/             # Graphs
│   └── dashboard.py        # Main dashboard logic
│   └── sidebar.py          # Sidebar component
│   └── welcome.py          # Welcome page
├── app.py                  # Punto de entrada de la aplicación
└── requirements.txt        # Dependencias del proyecto
```

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/markoechevarria/analytic-dash.git
cd analytic-dash

```


2. **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Run the application:**
```bash
python app.py

```

## To do

* [ ] Connect to a live database instead of local CSV files.
* [ ] Implement more advanced callbacks for filtering across all charts simultaneously.
* [ ] Add Export to CSV/Excel functionality for the AG Grid tables.
* [ ] Improve responsive design for mobile devices.