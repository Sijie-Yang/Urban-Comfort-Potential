<div align="center">

# Computational Urban Comfort Indexing and Annealed Optimisation for Latent Potentials

**[Sijie Yang](https://sijie-yang.com)**<sup>a,b</sup>, **[Zdravko Trivic]()**<sup>a</sup>, **[Yihan Zhu]()**<sup>a</sup>, **[Mahmoud Abdelrahman]()**<sup>a</sup>, **[Filip Biljecki](https://filipbiljecki.com)**<sup>a,c,*</sup>

<sup>a</sup> Department of Architecture, National University of Singapore  
<sup>b</sup> School of Engineering and Applied Science, University of Pennsylvania  
<sup>c</sup> Department of Real Estate, National University of Singapore  
<sup>*</sup> Corresponding author: filip@nus.edu.sg

</div>

<div align="center">

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

</div>

<br>

<div align="center">
<div style="display: flex; justify-content: center; align-items: center; gap: 20px; margin-bottom: 30px;">
<img src="./Img/DoA Logo.jpg" alt="DoA Logo" width="150"/>
<img src="./Img/UAL Logo.jpg" alt="UAL Logo" width="150"/>
<img src="./Img/Penn Logo.png" alt="Penn Logo" width="150"/>

</div>
<a href="https://ual.sg">Urban Analytics Lab</a>
</div>



[Urban Analytics Lab](https://ual.sg)



<br>

<div align="center">

<img src="./Img/social_media_post_mapping.png" alt="Social Media Post Mapping" width="600"/>

</div>

## News

- **2025-09-22**: Release of first version of project data and code.
- **2026-03-16**: Added full details of project implementation.

## Todo

- [X] Update the first version of data and code for this project.
- [X] Update a full-detail version of data and code with more details.
- [] Continue to refine and adjust the framework.
- [] Extend this framework to 10 global cities.

## Abstract

Urban comfort shapes how people inhabit cities and can be assessed through modelling of environmental and social conditions. Beyond these observable states lies urban comfort potential—the latent scope for improving comfort across activities and places—which remains largely invisible without systematic analysis.

We examine Singapore as a global city, analysing **44,228 geotagged image–text posts** to classify five activity types and link them to spatial features using surveys and causal inference. A hybrid urban comfort index achieves strong validation (**R² > 0.8** across all activity categories) and, combined with **Ising Monte Carlo optimisation**, enables targeted simulations of improvement strategies.

**Keywords:** human-centred GeoAI, urban optimisation, urban planning, social media, geospatial modelling

## Key Features

### 🏙️ Urban Comfort Index (UCI) Analysis

- **Multi-activity Assessment**: Evaluation across 5 social activities:
  - Eating & Drinking
  - Nature Exploration
  - Community Gathering
  - Walking & Exercising
  - Urban Sightseeing

### 📊 Comprehensive Data Integration

- **Streetscape Perception (SP)**: Environmental comfort factors including greenery, shading, imageability, and human scale
- **Functional Convenience (FC)**: Point-of-interest ratings, density analysis, and user reviews
- **Accessibility (AC)**: Transportation connectivity and transit access metrics
- **Context Density (CD)**: Population, building, and leisure space density analysis

### 🎯 Policy-weighted Urban Comfort Index (pUCI)

- **5 Strategic Planning Scenarios**:
  - pUCI_1: Balanced Development
  - pUCI_2: Eco-Livable City Initiative
  - pUCI_3: Community Cohesion Drive
  - pUCI_4: Active Walkability Focus
  - pUCI_5: Tourism Strategy Development

### 🔧 Advanced Optimization Framework

- **Ising Monte Carlo Optimization**: Systematic spatial optimization with simulated annealing
- **Causal Inference**: Identifying activity-specific spatial drivers using causal forest models
- **Socio-spatial Variation Analysis**: Understanding policy-sensitive vs location-sensitive features
- **Geospatial Modelling**: HGWR-based UCI construction with hybrid weighting approach

## Repository Structure

| Notebook | Description | Main inputs | Main outputs |
|----------|-------------|-------------|--------------|
| **code_1** | Social Activity Data | Raw social media / activity data | Activity counts, Moran's I, LISA maps |
| **code_2** | Geospatial Data | — | `data_geospatial.gpkg` (SP, FC, AC, CD features) |
| **code_3** | Social Activity Field (UCI Part 1) | `data_social_activity.gpkg`, `data_geospatial.gpkg` | `data_uci_modelling.gpkg` (features + field targets) |
| **code_4** | Causal Forest Analytics (UCI Part 2) | `data_uci_modelling.gpkg` | `data_uci_dimension_causal_importance.json` |
| **code_5** | Resident & Expert Survey (UCI Part 3) | `data_resident_survey_results.csv` | Hybrid weights (used in code_6) |
| **code_6** | UCI Modelling (UCI Part 4) | `data_uci_modelling.gpkg`, `data_uci_hybrid_weighting.json` | `data_uci_modelling_with_preds_uci.gpkg`, model tables |
| **code_7** | UCI Optimisation / pUCI (UCI Part 5) | `data_uci_modelling_with_preds_uci.gpkg` | pUCI scores, `optimisation_result*/` (Ising results) |
| **code_8** | Result Analytics | `data_uci_puci.gpkg`, `data/optimisation_result/` | UCI/pUCI visualisation, delta-UCP, socio-spatial variation, PCA, district classification |

## Data Structure

```
data/
├── data_administrative_districts.geojson   # Administrative boundaries (code_8)
├── data_geospatial.gpkg                    # Geospatial features SP/FC/AC/CD (code_2 → code_3)
├── data_social_activity.gpkg               # Social activity counts (code_1 → code_3)
├── data_resident_survey_results.csv        # Resident survey (code_5)
├── data_uci_modelling.gpkg                 # Features + activity field targets (code_3 → code_4, code_6)
├── data_uci_modelling_with_preds_uci.gpkg  # UCI predictions (code_6 → code_7)
├── data_uci_puci.gpkg                      # UCI + pUCI scores (code_7 → code_8)
├── data_uci_social_activity_field.gpkg     # Activity field (code_3)
├── data_uci_dimension_causal_importance.json  # Causal importance (code_4)
├── data_uci_hybrid_weighting.json         # Hybrid weights (code_5 → code_6)
├── table_model_comparison.csv              # Model comparison (code_6)
├── table_model_mean.csv                    # Model metrics (code_6)
├── optimisation_result/                    # Ising optimisation results (code_7 output; used by code_8)
└── optimisation_result_user/               # Optional user output folder (code_7)
```

## Getting Started

### Prerequisites

- Python 3.8+
- Jupyter (for running notebooks)

Key packages (install as needed per notebook):

- `geopandas`, `pandas`, `numpy` — data and geospatial
- `matplotlib` — visualisation
- `scikit-learn` — models, scaling, metrics
- `statsmodels` — HGWR, VIF (code_6)
- `econml` — Causal Forest (code_4)
- `libpysal`, `esda` — spatial weights and Moran’s I (code_1)
- `tqdm` — progress bars

### Installation

```bash
git clone https://github.com/Sijie-Yang/Urban-Comfort-Potential.git
cd Urban-Comfort-Potential
pip install geopandas pandas numpy matplotlib scikit-learn statsmodels econml libpysal esda tqdm
```

## Usage

### Pipeline order

Notebooks can be run in sequence to reproduce the full pipeline, or run individually if the required data files already exist:

1. **code_1** — Social activity data and spatial autocorrelation  
2. **code_2** — Geospatial feature preparation → `data/data_geospatial.gpkg`  
3. **code_3** — Social activity field + merge → `data/data_uci_modelling.gpkg`  
4. **code_4** — Causal forest analytics → `data/data_uci_dimension_causal_importance.json`  
5. **code_5** — Resident & expert survey → hybrid weights for code_6  
6. **code_6** — UCI modelling (HGWR, hybrid weighting) → `data/data_uci_modelling_with_preds_uci.gpkg`  
7. **code_7** — pUCI and Ising optimisation → `data/data_uci_puci.gpkg`, `data/optimisation_result/` (or `optimisation_result_user/`)  
8. **code_8** — Result analytics (UCI/pUCI maps, optimisation summaries, socio-spatial variation, delta-UCP, PCA, district classification)

```bash
jupyter notebook code_1_social_activity_data.ipynb   # start from data
# or
jupyter notebook code_8_result_analytics.ipynb        # run analytics if data already exist
```

**Note:** Each notebook (and each main section marked with `##`) can be run independently where inputs are available.

### What each notebook does

- **code_1–code_3**: Build activity and geospatial inputs and the unified modelling dataset (`data_uci_modelling.gpkg`).
- **code_4**: Causal forest on activity-field targets; output used with code_5 for hybrid weights.
- **code_5**: Survey processing and expert weights; combined with causal weights in code_6.
- **code_6**: Model comparison and final UCI modelling; produces UCI predictions and `data_uci_modelling_with_preds_uci.gpkg`.
- **code_7**: Computes pUCI, runs Ising Monte Carlo optimisation per pUCI × feature, writes optimisation result GeoPackages and CSVs.
- **code_8**: Loads UCI/pUCI and optimisation results; produces visualisations, delta-UCP, socio-spatial variation, PCA, and district-level classification.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

You are free to:

- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:

- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

[![CC BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

## Contact

- Author: Sijie Yang
- GitHub: [@Sijie-Yang](https://github.com/Sijie-Yang)
