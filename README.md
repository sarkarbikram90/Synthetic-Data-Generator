# 🎲 Synthetic Data Generator

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

**A powerful, user-friendly web application for generating realistic synthetic data**

[🚀 **Live Demo**](https://synthetic-data-generator-for-machine-learning-project.streamlit.app/) • [🐛 Report Bug](https://github.com/sarkarbikram90/Synthetic-Data-Generator/issues) • [✨ Request Feature](https://github.com/sarkarbikram90/Synthetic-Data-Generator/issues)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [✨ Features](#-features)
- [🎯 Use Cases](#-use-cases)
- [📊 Data Types](#-data-types)
- [🚀 Quick Start](#-quick-start)
- [🛠️ Installation](#️-installation)
- [📸 Screenshots](#-screenshots)
- [🔧 Usage](#-usage)
- [⚙️ Configuration](#️-configuration)
- [📈 Performance](#-performance)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---

## Overview

The **Synthetic Data Generator** is a comprehensive web application built with Streamlit that enables users to generate realistic, high-quality synthetic data for testing, development, analytics, and research purposes. With an intuitive interface and powerful generation capabilities, it supports multiple data types and export formats.

### 🎯 Why Synthetic Data?

- **Privacy Protection**: No real customer data at risk
- **Development Speed**: Instant test data generation
- **Compliance**: GDPR/CCPA compliant testing environments
- **Cost Effective**: No need to purchase or license real datasets
- **Scalable**: Generate from upto 10,000 records instantly

---

## ✨ Features

### 🎨 **Intuitive Web Interface**
- Clean, modern UI with responsive design
- Real-time data preview and statistics
- Interactive configuration panels
- Progress indicators and loading states

### 📊 **Multiple Data Types**
  - **Personal/Customer Data**: Names, addresses, contact info
  - **Sales Transactions**: Purchase records, revenue data
  - **Employee Records**: HR data, performance metrics
  - **Time Series**: Temporal data with trends
  - **Text Data**: Reviews, posts, social media content
  - **Application Logs**: System events, user actions, errors
  - **System Data**: OS logs, metrics, security events

### 💾 **Flexible Export Options**
- CSV, JSON, Excel formats
- Individual file downloads
- Bulk ZIP packages
- Configurable data volumes (upto 10,000 records)

### ⚡ **High Performance**
- Optimized data generation algorithms
- Memory-efficient processing
- Instant preview capabilities
- Scalable architecture

### 🔒 **Privacy & Security**
- No real data storage
- Client-side processing
- No personal information collected
- Open-source transparency

---

## 🎯 Use Cases

| Use Case | Description | Benefits |
|----------|-------------|----------|
| **Software Testing** | Generate test datasets for QA and testing | Reliable, consistent test data |
| **Development** | Mock data for development environments | Faster development cycles |
| **Data Science** | Practice datasets for learning and prototyping | Real-world data structures |
| **Demos & Training** | Sample data for presentations and tutorials | Professional, realistic examples |
| **Analytics Testing** | Test dashboards and reporting tools | Comprehensive data coverage |
| **Database Seeding** | Populate development and staging databases | Realistic data relationships |

---

## 📊 Data Types

<details>
<summary><b>👤 Personal/Customer Data</b></summary>

Perfect for CRM systems, user databases, and customer analytics:

- **Identity**: First name, last name, email, phone
- **Demographics**: Age, gender, occupation, salary
- **Location**: Full addresses with city, state, ZIP
- **Metadata**: Creation dates, unique IDs

**Sample Output:**
```csv
id,first_name,last_name,email,phone,city,salary
550e8400-e29b-41d4-a716-446655440000,John,Doe,john.doe@email.com,(555) 123-4567,New York,75000
```
</details>

<details>
<summary><b>💰 Sales Transactions</b></summary>

Ideal for e-commerce platforms, retail analytics, and revenue tracking:

- **Products**: Names, categories, prices, quantities
- **Transactions**: IDs, dates, payment methods, discounts
- **Sales Data**: Revenue, regions, sales representatives
- **Customer Info**: Buyer IDs and preferences

**Sample Output:**
```csv
transaction_id,product_name,category,quantity,unit_price,total_amount,payment_method
TXN-001,Wireless Headphones,Electronics,2,199.99,399.98,Credit Card
```
</details>

<details>
<summary><b>👨‍💼 Employee Records</b></summary>

Essential for HR systems, payroll, and organizational analysis:

- **Personal**: Employee IDs, names, contact information
- **Professional**: Departments, positions, hire dates
- **Performance**: Salaries, ratings, experience levels
- **Organization**: Manager relationships, remote work status

**Sample Output:**
```csv
employee_id,first_name,department,position,salary,hire_date,performance_rating
EMP1001,Alice Johnson,Engineering,Senior Developer,95000,2022-03-15,4.2
```
</details>

<details>
<summary><b>📈 Time Series Data</b></summary>

Perfect for analytics, IoT applications, and financial modeling:

- **Temporal**: Date/time sequences with various intervals
- **Metrics**: Multiple measurement categories
- **Trends**: Realistic growth and seasonal patterns
- **Analytics**: Moving averages, cumulative values

**Sample Output:**
```csv
date,value,category_a,category_b,moving_avg_7d
2024-01-01,142.5,45.2,23.8,140.2
2024-01-02,138.7,52.1,28.3,141.1
```
</details>

<details>
<summary><b>📝 Text Content</b></summary>

Great for content management systems, social media analysis, and NLP:

- **Product Reviews**: Ratings, titles, detailed feedback
- **Blog Posts**: Articles with metadata and engagement metrics
- **Social Media**: Posts with hashtags, likes, and shares
- **Content Marketing**: Realistic text for various platforms

**Sample Output:**
```csv
review_id,product_name,rating,review_title,review_text,helpful_votes
REV00001,Smart Watch Pro,4,"Great battery life","This watch exceeded my expectations...",23
```
</details>

---

## 🚀 Quick Start

### 🌐 **Option 1: Use Online (Recommended)**

Visit the live application: **[Launch App →](https://synthetic-data-generator-for-machine-learning-project.streamlit.app/)**

1. Select your data type from the sidebar
2. Configure the number of records
3. Choose export format
4. Click "Generate Data"
5. Preview and download your dataset

### 💻 **Option 2: Run Locally**


## Clone the repository
```bash
git clone https://github.com/sarkarbikram90/Synthetic-Data-Generator.git
```
```bash
cd Synthetic-Data-Generator
```
## Install dependencies
```bash
pip install -r requirements.txt
```
## Launch the application
```bash
streamlit run app.py
```

Access the app at `http://localhost:8501`

---

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Dependencies

The application uses the following key libraries:

```txt
streamlit>=1.28.0    # Web app framework
pandas>=1.5.0        # Data manipulation
numpy>=1.24.0        # Numerical computing
faker>=19.0.0        # Realistic fake data generation
openpyxl>=3.1.0      # Excel file support
python-dateutil>=2.8.0  # Date/time utilities
```

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sarkarbikram90/Synthetic-Data-Generator.git
   cd Synthetic-Data-Generator
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

---

---

## 🔧 Usage

### Basic Workflow

1. **Configure Data Type**
   ```
   Sidebar → Select Data Type → Choose from 5 options
   ```

2. **Set Parameters**
   ```
   Sidebar → Number of Records → Slide to desired amount (upto 5,000)
   ```

3. **Generate Data**
   ```
   Sidebar → Generate Data Button → Wait for processing
   ```

4. **Preview Results**
   ```
   Main Area → Review generated data → Check statistics
   ```

5. **Export Data**
   ```
   Download Section → Choose format → Click download button
   ```

### Advanced Features

- **Column Information**: Expand the "Column Information" section to see data types, null counts, and unique values
- **Multiple Formats**: Select "All Formats" to download CSV, JSON, and Excel files in one ZIP package
- **Data Validation**: Review the statistics cards to ensure data quality meets your requirements

---

## ⚙️ Configuration

### Customizing Data Generation

The application allows for extensive customization through the sidebar interface:

#### Data Volume
- **Minimum**: 10 records (for quick testing)
- **Maximum**: 5,000 records (for comprehensive datasets)
- **Recommendation**: Start with 100-500 records for initial evaluation

#### Export Formats
- **CSV**: Universal compatibility, best for data analysis
- **JSON**: API integration, NoSQL databases
- **Excel**: Business reporting, spreadsheet analysis
- **ZIP Package**: All formats for comprehensive delivery

#### Text Content Types
When selecting "Text Data", choose from:
- **Reviews**: Product feedback with ratings and sentiment
- **Blog Posts**: Articles with metadata and engagement metrics
- **Social Media**: Posts with hashtags and social signals

---

## 📈 Performance

### Benchmarks

| Records | Generation Time | Memory Usage | File Size (CSV) |
|---------|----------------|--------------|-----------------|
| 100     | < 1 second     | ~2 MB        | ~15 KB          |
| 1,000   | ~2 seconds     | ~5 MB        | ~150 KB         |
| 5,000   | ~8 seconds     | ~20 MB       | ~750 KB         |

### Optimization Tips

- **Batch Processing**: Generate large datasets in chunks if memory is limited
- **Format Selection**: Use CSV for fastest processing and smallest file sizes
- **Preview First**: Always preview smaller samples before generating large datasets

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute

- 🐛 **Report Bugs**: [Open an issue](https://github.com/sarkarbikram90/Synthetic-Data-Generator/issues)
- 💡 **Suggest Features**: [Request new functionality](https://github.com/sarkarbikram90/Synthetic-Data-Generator/issues)
- 📝 **Improve Documentation**: Submit documentation improvements
- 🔧 **Code Contributions**: Submit pull requests with new features or fixes

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Ensure code quality: `pylint app.py`
5. Submit a pull request

---

## 🗺️ Roadmap

### Version 2.0 (Planned)
- [ ] **API Endpoints**: RESTful API for programmatic access
- [ ] **Custom Schemas**: User-defined data structures
- [ ] **Data Relationships**: Foreign keys and referential integrity
- [ ] **Advanced Text**: AI-powered content generation
- [ ] **Real-time Streaming**: Live data generation capabilities

### Version 2.1 (Future)
- [ ] **User Accounts**: Save preferences and generation history
- [ ] **Collaboration**: Team workspaces and shared templates
- [ ] **Enterprise Features**: SSO, audit logs, advanced security
- [ ] **Cloud Integration**: Direct export to cloud storage
- [ ] **Advanced Analytics**: Data profiling and quality metrics

### Long-term Vision
- [ ] **Machine Learning**: Generate data based on existing patterns
- [ ] **Industry Templates**: Pre-built schemas for common use cases
- [ ] **Multi-language Support**: Internationalization
- [ ] **Mobile App**: iOS and Android applications

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Bikram Sarkar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

- **[Streamlit](https://streamlit.io/)** - For the amazing web app framework
- **[Faker](https://faker.readthedocs.io/)** - For realistic fake data generation
- **[Pandas](https://pandas.pydata.org/)** - For powerful data manipulation capabilities
- **[NumPy](https://numpy.org/)** - For numerical computing support

### Special Thanks

- The open-source community for inspiration
---

## 📞 Support

### Get Help

- 📖 **Documentation**: Check this README and inline code comments
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/sarkarbikram90/Synthetic-Data-Generator/issues)
- 💡 **Feature Requests**: [GitHub Issues](https://github.com/sarkarbikram90/Synthetic-Data-Generator/issues)
- 📧 **Contact**: [sarkarbikram90@gmail.com] (for urgent matters)

### Community

- ⭐ **Star this repo** if you find it useful!
- 🍴 **Fork** to create your own version
- 👀 **Watch** for updates and new releases
- 📢 **Share** with your network

---

<div align="center">

**Built with ❤️ by [Bikram Sarkar](https://github.com/sarkarbikram90)**

[![GitHub stars](https://img.shields.io/github/stars/sarkarbikram90/Synthetic-Data-Generator.svg?style=social&label=Star)](https://github.com/sarkarbikram90/Synthetic-Data-Generator)
[![GitHub forks](https://img.shields.io/github/forks/sarkarbikram90/Synthetic-Data-Generator.svg?style=social&label=Fork)](https://github.com/sarkarbikram90/Synthetic-Data-Generator/fork)

</div>
