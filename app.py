import streamlit as st
import pandas as pd
import numpy as np
from faker import Faker
import random
import string
from datetime import datetime, timedelta
import io
import json
from typing import Dict, List, Any
import zipfile

# Initialize Faker
fake = Faker()

# Page configuration
st.set_page_config(
    page_title="Synthetic Data Generator",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .feature-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .stats-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

class SyntheticDataGenerator:
    """Core class for generating synthetic data"""
    
    def __init__(self):
        self.fake = Faker()
    
    def generate_personal_data(self, num_records: int) -> pd.DataFrame:
        """Generate personal/customer data"""
        data = []
        for _ in range(num_records):
            record = {
                'id': self.fake.uuid4(),
                'first_name': self.fake.first_name(),
                'last_name': self.fake.last_name(),
                'email': self.fake.email(),
                'phone': self.fake.phone_number(),
                'address': self.fake.address().replace('\n', ', '),
                'city': self.fake.city(),
                'state': self.fake.state(),
                'zip_code': self.fake.zipcode(),
                'birth_date': self.fake.date_of_birth(minimum_age=18, maximum_age=80),
                'gender': random.choice(['Male', 'Female', 'Other']),
                'occupation': self.fake.job(),
                'salary': random.randint(30000, 150000),
                'created_at': self.fake.date_time_between(start_date='-2y', end_date='now')
            }
            data.append(record)
        return pd.DataFrame(data)
    
    def generate_sales_data(self, num_records: int) -> pd.DataFrame:
        """Generate sales transaction data"""
        products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Webcam', 'Speaker', 'Phone', 'Tablet', 'Charger']
        categories = ['Electronics', 'Accessories', 'Computing', 'Mobile']
        
        data = []
        for _ in range(num_records):
            product = random.choice(products)
            quantity = random.randint(1, 5)
            unit_price = round(random.uniform(10, 2000), 2)
            
            record = {
                'transaction_id': self.fake.uuid4(),
                'customer_id': self.fake.uuid4(),
                'product_name': product,
                'category': random.choice(categories),
                'quantity': quantity,
                'unit_price': unit_price,
                'total_amount': round(quantity * unit_price, 2),
                'discount_percent': random.choice([0, 5, 10, 15, 20]),
                'payment_method': random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Cash']),
                'transaction_date': self.fake.date_time_between(start_date='-1y', end_date='now'),
                'sales_rep': self.fake.name(),
                'region': random.choice(['North', 'South', 'East', 'West', 'Central'])
            }
            data.append(record)
        return pd.DataFrame(data)
    
    def generate_employee_data(self, num_records: int) -> pd.DataFrame:
        """Generate employee data"""
        departments = ['Engineering', 'Marketing', 'Sales', 'HR', 'Finance', 'Operations']
        positions = ['Manager', 'Senior', 'Junior', 'Lead', 'Director', 'Analyst']
        
        data = []
        for _ in range(num_records):
            hire_date = self.fake.date_between(start_date='-5y', end_date='now')
            
            record = {
                'employee_id': f"EMP{random.randint(1000, 9999)}",
                'first_name': self.fake.first_name(),
                'last_name': self.fake.last_name(),
                'email': self.fake.company_email(),
                'department': random.choice(departments),
                'position': f"{random.choice(positions)} {random.choice(departments).replace('s', '')}",
                'hire_date': hire_date,
                'salary': random.randint(40000, 200000),
                'manager_id': f"EMP{random.randint(1000, 9999)}",
                'performance_rating': round(random.uniform(2.5, 5.0), 1),
                'years_experience': random.randint(1, 20),
                'remote_work': random.choice([True, False]),
                'bonus_eligible': random.choice([True, False])
            }
            data.append(record)
        return pd.DataFrame(data)
    
    def generate_time_series(self, num_points: int, start_date: datetime = None) -> pd.DataFrame:
        """Generate time series data"""
        if start_date is None:
            start_date = datetime.now() - timedelta(days=num_points)
        
        dates = [start_date + timedelta(days=i) for i in range(num_points)]
        
        # Generate synthetic metrics with trends and seasonality
        base_value = 100
        trend = np.linspace(0, 50, num_points)
        seasonality = 10 * np.sin(2 * np.pi * np.arange(num_points) / 30)  # 30-day cycle
        noise = np.random.normal(0, 5, num_points)
        
        values = base_value + trend + seasonality + noise
        
        data = {
            'date': dates,
            'value': values,
            'category_a': np.random.uniform(20, 80, num_points),
            'category_b': np.random.uniform(10, 60, num_points),
            'cumulative': np.cumsum(values),
            'moving_avg_7d': pd.Series(values).rolling(window=7, min_periods=1).mean()
        }
        
        return pd.DataFrame(data)
    
    def generate_text_data(self, num_records: int, text_type: str) -> pd.DataFrame:
        """Generate text data"""
        data = []
        
        for i in range(num_records):
            if text_type == 'reviews':
                record = {
                    'review_id': f"REV{i+1:05d}",
                    'product_name': self.fake.catch_phrase(),
                    'reviewer_name': self.fake.name(),
                    'rating': random.randint(1, 5),
                    'review_title': self.fake.sentence(nb_words=6)[:-1],
                    'review_text': self.fake.text(max_nb_chars=300),
                    'helpful_votes': random.randint(0, 100),
                    'review_date': self.fake.date_between(start_date='-1y', end_date='now')
                }
            elif text_type == 'blog_posts':
                record = {
                    'post_id': f"POST{i+1:05d}",
                    'title': self.fake.sentence(nb_words=8)[:-1],
                    'author': self.fake.name(),
                    'content': self.fake.text(max_nb_chars=500),
                    'tags': ', '.join(self.fake.words(nb=3)),
                    'views': random.randint(100, 10000),
                    'likes': random.randint(5, 500),
                    'publish_date': self.fake.date_between(start_date='-6m', end_date='now')
                }
            else:  # social_media
                record = {
                    'post_id': f"SM{i+1:06d}",
                    'username': self.fake.user_name(),
                    'platform': random.choice(['Twitter', 'Facebook', 'Instagram', 'LinkedIn']),
                    'post_text': self.fake.text(max_nb_chars=150),
                    'hashtags': ' '.join([f"#{word}" for word in self.fake.words(nb=2)]),
                    'likes': random.randint(0, 1000),
                    'shares': random.randint(0, 100),
                    'comments': random.randint(0, 50),
                    'post_datetime': self.fake.date_time_between(start_date='-30d', end_date='now')
                }
            
            data.append(record)
        
        return pd.DataFrame(data)

def main():
    # Header
    st.markdown('<h1 class="main-header">🎲 Synthetic Data Generator</h1>', unsafe_allow_html=True)
    st.markdown("**Generate realistic synthetic data for testing, development, and analysis**")
    
    # Initialize generator
    if 'generator' not in st.session_state:
        st.session_state.generator = SyntheticDataGenerator()
    
    # Sidebar configuration
    st.sidebar.header("⚙️ Configuration")
    
    # Data type selection
    data_type = st.sidebar.selectbox(
        "Select Data Type",
        ["Personal/Customer Data", "Sales Transactions", "Employee Records", "Time Series", "Text Data"],
        help="Choose the type of synthetic data to generate"
    )
    
    # Number of records
    if data_type == "Time Series":
        num_records = st.sidebar.slider("Number of Data Points", 50, 1000, 365)
    else:
        num_records = st.sidebar.slider("Number of Records", 10, 5000, 100)
    
    # Additional options based on data type
    if data_type == "Text Data":
        text_type = st.sidebar.selectbox(
            "Text Type",
            ["reviews", "blog_posts", "social_media"],
            format_func=lambda x: x.replace('_', ' ').title()
        )
    
    # Export format
    export_format = st.sidebar.selectbox(
        "Export Format",
        ["CSV", "JSON", "Excel", "All Formats"],
        help="Choose download format"
    )
    
    # Generation section
    st.sidebar.markdown("---")
    generate_btn = st.sidebar.button("🚀 Generate Data", type="primary", use_container_width=True)
    
    # Main content area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    if generate_btn:
        with st.spinner("Generating synthetic data..."):
            # Generate data based on type
            if data_type == "Personal/Customer Data":
                df = st.session_state.generator.generate_personal_data(num_records)
            elif data_type == "Sales Transactions":
                df = st.session_state.generator.generate_sales_data(num_records)
            elif data_type == "Employee Records":
                df = st.session_state.generator.generate_employee_data(num_records)
            elif data_type == "Time Series":
                df = st.session_state.generator.generate_time_series(num_records)
            else:  # Text Data
                df = st.session_state.generator.generate_text_data(num_records, text_type)
            
            # Store in session state
            st.session_state.generated_data = df
            st.session_state.data_type = data_type
    
    # Display results
    if 'generated_data' in st.session_state:
        df = st.session_state.generated_data
        
        # Stats row
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="stats-card">
                <h3>{len(df):,}</h3>
                <p>Records Generated</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="stats-card">
                <h3>{len(df.columns)}</h3>
                <p>Columns</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            memory_usage = df.memory_usage(deep=True).sum() / 1024 / 1024
            st.markdown(f"""
            <div class="stats-card">
                <h3>{memory_usage:.1f} MB</h3>
                <p>Memory Usage</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="stats-card">
                <h3>{export_format}</h3>
                <p>Export Format</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Data preview
        st.subheader("📊 Data Preview")
        
        # Show column info
        with st.expander("Column Information", expanded=False):
            col_info = pd.DataFrame({
                'Column': df.columns,
                'Type': df.dtypes.astype(str),
                'Non-Null Count': df.count(),
                'Null Count': df.isnull().sum(),
                'Unique Values': df.nunique()
            })
            st.dataframe(col_info, use_container_width=True)
        
        # Main data display
        st.dataframe(df.head(20), use_container_width=True)
        
        if len(df) > 20:
            st.info(f"Showing first 20 rows out of {len(df):,} total records.")
        
        # Download section
        st.subheader("💾 Download Generated Data")
        
        # Prepare download files
        def create_download_files(df, export_format):
            files = {}
            
            if export_format in ["CSV", "All Formats"]:
                csv_buffer = io.StringIO()
                df.to_csv(csv_buffer, index=False)
                files['data.csv'] = csv_buffer.getvalue().encode()
            
            if export_format in ["JSON", "All Formats"]:
                json_str = df.to_json(orient='records', indent=2, date_format='iso')
                files['data.json'] = json_str.encode()
            
            if export_format in ["Excel", "All Formats"]:
                excel_buffer = io.BytesIO()
                with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                    df.to_excel(writer, sheet_name='Generated Data', index=False)
                files['data.xlsx'] = excel_buffer.getvalue()
            
            return files
        
        files = create_download_files(df, export_format)
        
        # Download buttons
        download_col1, download_col2, download_col3 = st.columns(3)
        
        for i, (filename, file_data) in enumerate(files.items()):
            col = [download_col1, download_col2, download_col3][i % 3]
            with col:
                st.download_button(
                    label=f"📁 {filename.upper()}",
                    data=file_data,
                    file_name=filename,
                    mime="application/octet-stream" if filename.endswith('.xlsx') else "text/plain",
                    use_container_width=True
                )
        
        # If multiple formats, create zip
        if export_format == "All Formats" and len(files) > 1:
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                for filename, file_data in files.items():
                    zip_file.writestr(filename, file_data)
            
            st.download_button(
                label="📦 Download All Formats (ZIP)",
                data=zip_buffer.getvalue(),
                file_name="synthetic_data_package.zip",
                mime="application/zip",
                use_container_width=True
            )
    
    else:
        # Welcome message
        st.markdown("""
        <div class="feature-card">
            <h3>🎯 Quick Start</h3>
            <p>1. Choose your data type from the sidebar</p>
            <p>2. Set the number of records to generate</p>
            <p>3. Select your preferred export format</p>
            <p>4. Click "Generate Data" to create synthetic data</p>
            <p>5. Preview and download your generated dataset</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Feature overview
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 📋 Available Data Types
            - **Personal/Customer Data**: Names, addresses, contact info
            - **Sales Transactions**: Purchase records, revenue data
            - **Employee Records**: HR data, performance metrics
            - **Time Series**: Temporal data with trends
            - **Text Data**: Reviews, posts, social media content
            """)
        
        with col2:
            st.markdown("""
            ### ✨ Key Features
            - **Realistic Data**: Uses Faker library for authentic-looking data
            - **Multiple Formats**: CSV, JSON, Excel export options
            - **Instant Preview**: See your data before downloading
            - **Scalable**: Generate from 10 to 5,000+ records
            - **No Setup**: Ready to use immediately
            """)

if __name__ == "__main__":
    main()