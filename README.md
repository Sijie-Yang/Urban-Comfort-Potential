# <div align="center">Computational Urban Comfort Indexing and Annealed Optimisation for Latent Potentials</div>

<div align="center">

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

<br>

<div align="center">

<img src="./Img/social_media_post_mapping.png" alt="Social Media Post Mapping" width="600"/>

</div>

## News

- **2025-09-22**: Release of first version of project data and code.

## Todo

- [x] Update the first version of data and code for this project.
- [ ] Update a second version of data and code with more details.

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

## Data Structure

```
Data/
├── Data_UCI_pUCI.gpkg          # Main UCI and pUCI dataset (58+ spatial features)
└── Optimisation_Result/        # 675 optimization result files
    ├── ising_optimisation_UCP_*.gpkg (630 files)    # Spatial optimization results
    ├── UCP_ising_energy_evolution_*.csv (45 files) # Energy evolution tracking
```

## Getting Started

### Prerequisites

- Python 3.8+
- Required packages:
  - `geopandas` - Geospatial data processing
  - `matplotlib` - Data visualization
  - `pandas` - Data analysis
  - `numpy` - Numerical computing
  - `tqdm` - Progress bars for data loading

### Installation

```bash
git clone https://github.com/Sijie-Yang/Urban-Comfort-Potential.git
cd Urban-Comfort-Potential
pip install geopandas matplotlib pandas numpy tqdm
```

## Usage

### Quick Start
Run the main analysis notebook:
```bash
jupyter notebook RunMe.ipynb
```

**Note**: Each main section (marked with ## headers) in the notebook can be run independently. You can execute any section without needing to run the previous sections first.

### Analysis Workflow

The notebook is organized into two main analytical components:

#### 🏙️ **UCI Assessment Result Analytics**
1. **Import UCI Data**: Load comprehensive urban comfort index dataset with 58+ spatial features
2. **Visualize UCI Patterns**: Generate 5-level classification maps for each social activity:
   - Eating & Drinking
   - Nature Exploration  
   - Community Gathering
   - Walking & Exercising
   - Urban Sightseeing

#### 🎯 **UCP Optimisation Result Analytics**
1. **Create UCP Geodataframe**: Initialize spatial framework for optimization analysis
2. **Load Feature-Policy Pairs**: Import 45 optimization result files (5 policies × 9 features)
3. **Policy-specific UCP Analysis**: Examine UCP patterns for each policy scenario:
   - UCP_1: Balanced Development
   - UCP_2: Eco-Livable City Initiative
   - UCP_3: Community Cohesion Drive
   - UCP_4: Active Walkability Focus
   - UCP_5: Tourism Strategy Development
4. **Delta-UCP Analysis**: Calculate specialized UCP differences between policies
5. **Administrative District Analysis**: Aggregate UCP outcomes at district level
6. **PCA Analysis**: Perform principal component analysis of Delta-UCP patterns
7. **District Classification**: Categorize districts based on UCP characteristics

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
