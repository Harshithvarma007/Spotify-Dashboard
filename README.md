# Spotify Dashboard: Advanced Power BI Project

Welcome to the Spotify Dashboard project, an advanced Power BI application showcasing the most streamed Spotify songs of 2023 with visualizations and analytics.

## Blog Link

Read more about the development of this Spotify Dashboard on my Medium blog:
[Spotify Dashboard - Advanced Power BI Project](https://medium.com/@harshith007varma007/spotify-dashboard-advanced-power-bi-project-5844d4877893)

## Deployed Project

Access the deployed Spotify Dashboard application:
[Spotify Dashboard](https://spotify-dashboard-007.streamlit.app/)


## Table of Contents

1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [Dataset](#dataset)
4. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Setup Spotify Developer API](#setup-spotify-developer-api)
5. [Usage](#usage)
6. [Dashboard Features](#dashboard-features)
   - [Charts and Visualizations](#charts-and-visualizations)
   - [Adding Background Image](#adding-background-image)
   - [Creating Measures](#creating-measures)
   - [Advanced Visualizations](#advanced-visualizations)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

This repository contains the resources and instructions to create an advanced Spotify Dashboard using Power BI. The dashboard visualizes data on the most streamed Spotify songs of 2023, including charts, measures, and interactive features.

## Project Overview

The project leverages Power BI's capabilities to create an engaging dashboard that displays insights such as top songs, artist popularity, and trends over time. It utilizes the Spotify Developer API to enrich song data with album cover images, enhancing the visual appeal of the dashboard.

## Dataset

The dataset (`spotify-2023.csv`) used in this project includes information on the most streamed songs from Spotify in 2023. It contains attributes such as track name, artist(s) name, streams, and release date. Additional data, such as album cover URLs, is fetched dynamically using the Spotify Developer API.

## Getting Started

To get started with the Spotify Dashboard project, follow these steps:

### Prerequisites

- Power BI Desktop installed on your machine.
- Python (for fetching album cover URLs using the Spotify Developer API).
- Spotify Developer account to obtain API credentials.

### Installation

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/Harshithvarma007/Spotify-Dashboard.git
   ```

2. Open the Power BI Desktop application and load the `dashboard.pbix` file.

### Setup Spotify Developer API

To fetch album cover URLs from the Spotify Developer API:

1. Create a Spotify Developer account and register a new application.
2. Obtain your Client ID and Client Secret.
3. Update the `url.py` script with your API credentials (`client_id` and `client_secret`).
4. Run the script to fetch album cover URLs and update the dataset (`spotify-2023-urls.csv`).

## Usage

Once the setup is complete, open `dashboard.pbix` in Power BI Desktop. Refresh the data to load the updated dataset with album cover URLs. Explore different visualizations, slicers, and data cards to interact with the dashboard.

## Dashboard Features

### Charts and Visualizations

- **Top Songs by Streams**: Visualize the top songs based on streaming counts.
- **Artist Popularity**: Analyze artist popularity trends.
- **Trend Analysis**: Track streaming trends over time using date-based slicers.

### Adding Background Image

To add the custom background image:

1. Copy the provided background image to your Power BI canvas.
2. Set the image properties to match the specified dimensions and alignment.

### Creating Measures

Measures are used for dynamic calculations in Power BI:

- **_max streams**: Calculates the maximum number of streams for a song.
- **_Top Song streams**: Compares individual song streams against the maximum streams.
- **_Average Stream per year**: Computes the average streams per year.
- **_Top song vs AVG**: Measures the deviation of top song streams from the average streams.

### Advanced Visualizations

- **HTML Content**: Embed HTML content for custom visualizations or images.
- **Unit Chart**: Display energy percentage using Vega visualization.
- **HeatMap**: Use Vega-Lite to visualize streaming data across months and days of the week.

## Contributing

Contributions to improve this project are welcome! Fork the repository, make your changes, and submit a pull request. Please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize the sections and details based on your specific implementation and requirements. This README.md provides a structured overview that helps users understand, set up, and utilize your Spotify Dashboard project effectively.
