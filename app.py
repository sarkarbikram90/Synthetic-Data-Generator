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
import logging
import os

# Configure logging
def setup_logging():
    """Configure logging for the application"""
    
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Configure logging format
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            # File handler - saves logs to file
            logging.FileHandler(f'logs/synthdata_{datetime.now().strftime("%Y%m%d")}.log'),
            # Console handler - prints to console (optional for Streamlit)
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger('SyntheticDataGenerator')

# Initialize logger
logger = setup_logging()

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
    
    
      
    .landing-hero p {
        font-size: 1.3rem;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .feature-item {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-top: 4px solid #667eea;
        transition: transform 0.3s ease;
    }
    
    .feature-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.15);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .cta-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 3rem;
        border: none;
        border-radius: 50px;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
  
    
    .stats-showcase {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        margin: 2rem 0;
    }
    
    .stats-row {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 1rem;
    }
    
    .stat-item {
        text-align: center;
        padding: 1rem;
        min-width: 150px;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
        color: #667eea;
    }
    
    .stat-label {
        font-size: 1rem;
        color: #666;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

def show_landing_page():
    
       
    
    # Stats Showcase
    st.markdown("""
    <div class="stats-showcase">
        <h2 style="text-align: center; margin-bottom: 2rem;">Synthetic Data Generator</h2>
        <div class="stats-row">
            <div class="stat-item">
                <div class="stat-number">7</div>
                <div class="stat-label">Data Types</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">10,000</div>
                <div class="stat-label">Records/Seconds</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">3</div>
                <div class="stat-label">Export Formats</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">100%</div>
                <div class="stat-label">Privacy</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Welcome message
    st.markdown("""
        <div class="feature-card">
            <h3>🎯 Quick Start</h3>
            <p>1. Choose your data type from the sidebar</p>
            <p>2. Set the number of records to generate</p>
            <p>3. Select your preferred export format</p>
            <p>4. Click "Generate Synthetic Data"</p>
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
            - **Application Logs**: System events, user actions, errors
            - **System Data**: OS logs, metrics, security events
            - **Correlated VM Data**: VM metrics + logs with matching timestamps
            """)
        
    with col2:
            st.markdown("""
            ### ✨ Key Features
            - **Realistic Data**: Uses Faker library for authentic-looking data
            - **Multiple Formats**: CSV, JSON, Excel export options
            - **Instant Preview**: See your data before downloading
            - **Scalable**: Generate from 50 to 10,000 records
            - **No Setup**: Ready to use immediately
            """)
    
    # Use Cases Section
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎯 **Perfect For**
        
        **Software Development Teams**
        - Unit and integration testing
        - Database seeding and migration testing
        - Load testing and performance validation
        - Demo environments and presentations
        
        **Data Science & Analytics**
        - ML model training and validation
        - Algorithm testing and benchmarking
        - Data pipeline development
        - Statistical analysis and research
        
        **DevOps & Infrastructure**
        - Monitoring system validation
        - Log analysis tool testing
        - Alert rule development
        - Capacity planning and scaling
        """)
    
    with col2:
        st.markdown("""
        ### ✨ **Key Benefits**
        
        **Instant Data Generation**
        - No waiting for data access approvals
        - Generate thousands of records in seconds
        - Consistent and reproducible datasets
        
        **Privacy & Compliance**
        - Zero real customer data exposure
        - GDPR and CCPA compliant by default
        - No data residency concerns
        
              
        **Developer Friendly**
        - Multiple export formats (CSV, JSON, Excel)
        - Open source and customizable
        """)
    
  
    
    # Technology Stack
    st.markdown("""
    ### 🔧 **Built With Modern Technology**
    
    - **Streamlit** - Interactive web application framework
    - **Pandas & NumPy** - High-performance data manipulation
    - **Faker Library** - Realistic fake data generation
    - **Python Ecosystem** - Extensible and maintainable codebase
    - **Cloud Ready** - Deploy anywhere with minimal setup
    """)
    
    # Final CTA
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h3>Ready to Transform Your Data Science and ML Workflow?</h3>
           
        </div>
        """, unsafe_allow_html=True)
        
        
    
# Initialize session state
if 'show_app' not in st.session_state:
    st.session_state.show_app = False

# Route between landing page and main app
if not st.session_state.show_app:
    show_landing_page()
else:
    # Show navigation option to go back to landing
    if st.sidebar.button("🏠 Back to Home", help="Return to landing page"):
        st.session_state.show_app = False
        st.rerun()

class SyntheticDataGenerator:
    """Core class for generating synthetic data with comprehensive logging"""
    
    def __init__(self):
        self.fake = Faker()
        logger.info("SyntheticDataGenerator initialized")
    
    def generate_personal_data(self, num_records: int) -> pd.DataFrame:
        """Generate personal/customer data with logging"""
        
        logger.info(f"Starting personal data generation - Records: {num_records}")
        start_time = datetime.now()
        
        try:
            data = []
            for i in range(num_records):
                # Log progress for large datasets
                if i > 0 and i % 1000 == 0:
                    logger.info(f"Generated {i}/{num_records} personal records")
                first_name = self.fake.first_name()
                last_name = self.fake.last_name()
                record = {
                    'id': self.fake.uuid4(),
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': f"{first_name.lower()}.{last_name.lower()}@example.com",
                    'phone': self.fake.phone_number(),
                    'address': self.fake.address().replace('\n', ', '),
                    'city': self.fake.city(),
                    'state': self.fake.state(),
                    'zip_code': self.fake.zipcode(),
                    'birth_date': self.fake.date_of_birth(minimum_age=18, maximum_age=80),
                    'gender': random.choice(['Male', 'Female', 'Other']),
                    'occupation': self.fake.job(),
                    'salary': random.randint(30000, 150000),
                    'created_at': self.fake.date_time_between(start_date='-12y', end_date='now')
                }
                data.append(record)
            
            df = pd.DataFrame(data)
            generation_time = (datetime.now() - start_time).total_seconds()
            memory_usage = df.memory_usage(deep=True).sum() / 1024 / 1024
            
            logger.info(f"Personal data generation completed - Records: {len(df)}, "
                       f"Time: {generation_time:.2f}s, Memory: {memory_usage:.2f}MB")
            return df
            
        except Exception as e:
            logger.error(f"Personal data generation failed: {str(e)}")
            raise
    
    def generate_sales_data(self, num_records: int) -> pd.DataFrame:
        """Generate sales transaction data with logging"""
        
        logger.info(f"Starting sales data generation - Records: {num_records}")
        start_time = datetime.now()
        
        try:
            products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Webcam', 'Speaker', 'Phone', 'Tablet', 'Charger']
            categories = ['Electronics', 'Accessories', 'Computing', 'Mobile']
            
            data = []
            for i in range(num_records):
                # Log progress for large datasets
                if i > 0 and i % 1000 == 0:
                    logger.info(f"Generated {i}/{num_records} sales records")
                
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
            
            df = pd.DataFrame(data)
            generation_time = (datetime.now() - start_time).total_seconds()
            memory_usage = df.memory_usage(deep=True).sum() / 1024 / 1024
            
            logger.info(f"Sales data generation completed - Records: {len(df)}, "
                       f"Time: {generation_time:.2f}s, Memory: {memory_usage:.2f}MB")
            return df
            
        except Exception as e:
            logger.error(f"Sales data generation failed: {str(e)}")
            raise
    
    def generate_employee_data(self, num_records: int) -> pd.DataFrame:
        """Generate employee data with logging"""
        
        logger.info(f"Starting employee data generation - Records: {num_records}")
        start_time = datetime.now()
        
        try:
            departments = ['Engineering', 'Marketing', 'Sales', 'HR', 'Finance', 'Operations']
            positions = ['Manager', 'Senior', 'Junior', 'Lead', 'Director', 'Analyst']
            
            data = []
            for i in range(num_records):
                # Log progress for large datasets
                if i > 0 and i % 1000 == 0:
                    logger.info(f"Generated {i}/{num_records} employee records")
                
                hire_date = self.fake.date_between(start_date='-10y', end_date='now')
                
                first_name = self.fake.first_name()
                last_name = self.fake.last_name()
                record = {
                    'employee_id': f"EMP{random.randint(1, 100001)}",
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': f"{first_name.lower()}.{last_name.lower()}@{self.fake.company_email().split('@')[1]}",
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
            
            df = pd.DataFrame(data)
            generation_time = (datetime.now() - start_time).total_seconds()
            memory_usage = df.memory_usage(deep=True).sum() / 1024 / 1024
            
            logger.info(f"Employee data generation completed - Records: {len(df)}, "
                       f"Time: {generation_time:.2f}s, Memory: {memory_usage:.2f}MB")
            return df
            
        except Exception as e:
            logger.error(f"Employee data generation failed: {str(e)}")
            raise
    
    def generate_time_series(self, num_points: int, start_date: datetime = None) -> pd.DataFrame:
        """Generate time series data with logging"""
        
        logger.info(f"Starting time series generation - Data points: {num_points}")
        start_time = datetime.now()
        
        try:
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
            
            df = pd.DataFrame(data)
            generation_time = (datetime.now() - start_time).total_seconds()
            memory_usage = df.memory_usage(deep=True).sum() / 1024 / 1024
            
            logger.info(f"Time series generation completed - Points: {len(df)}, "
                       f"Time: {generation_time:.2f}s, Memory: {memory_usage:.2f}MB")
            return df
            
        except Exception as e:
            logger.error(f"Time series generation failed: {str(e)}")
            raise
    
             
            
    def generate_log_data(self, num_records: int, log_type: str) -> pd.DataFrame:
        """Generate realistic application log data with logging"""
        
        logger.info(f"Starting log data generation - Records: {num_records}, Type: {log_type}")
        start_time = datetime.now()
        
        try:
            data = []
            
            # Define realistic data for different log types
            app_names = ['UserService', 'PaymentAPI', 'OrderProcessor', 'AuthService', 'DataPipeline', 
                        'WebApp', 'MobileAPI', 'ReportGenerator', 'EmailService', 'FileUploader']
            
            log_levels = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL']
            
            user_agents = [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X)',
                'PostmanRuntime/7.28.4'
            ]
            
            status_codes = [200, 201, 400, 401, 403, 404, 500, 502, 503]
            methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
            
            for i in range(num_records):
                # Log progress for large datasets
                if i > 0 and i % 1000 == 0:
                    logger.info(f"Generated {i}/{num_records} log records")
                
                base_timestamp = self.fake.date_time_between(start_date='-30d', end_date='now')
                
                if log_type == 'application_lifecycle':
                    events = ['APPLICATION_START', 'APPLICATION_STOP', 'SERVICE_START', 'SERVICE_STOP', 
                             'DEPLOYMENT_START', 'DEPLOYMENT_COMPLETE', 'HEALTH_CHECK', 'SHUTDOWN_INITIATED']
                    
                    event = random.choice(events)
                    level = 'INFO' if event not in ['APPLICATION_STOP', 'SHUTDOWN_INITIATED'] else random.choice(['INFO', 'WARN'])
                    
                    record = {
                        'timestamp': base_timestamp,
                        'log_level': level,
                        'application': random.choice(app_names),
                        'event_type': event,
                        'message': f"{event.replace('_', ' ').title()} - {random.choice(app_names)}",
                        'process_id': random.randint(1000, 9999),
                        'thread_id': random.randint(1, 100),
                        'version': f"{random.randint(1,3)}.{random.randint(0,9)}.{random.randint(0,9)}",
                        'environment': random.choice(['production', 'staging', 'development']),
                        'host': f"server-{random.randint(1,10)}.company.com",
                        'duration_ms': random.randint(100, 5000) if 'START' in event else None
                    }
                
                elif log_type == 'user_interactions':
                    actions = ['LOGIN', 'LOGOUT', 'BUTTON_CLICK', 'PAGE_VIEW', 'FORM_SUBMIT', 
                              'FILE_UPLOAD', 'SEARCH', 'FILTER_APPLIED', 'EXPORT_DATA', 'SETTINGS_CHANGED']
                    
                    action = random.choice(actions)
                    user_id = f"user_{random.randint(1, 123456789)}"
                    session_id = self.fake.uuid4()[:8]
                    
                    record = {
                        'timestamp': base_timestamp,
                        'log_level': 'INFO',
                        'event_type': action,
                        'user_id': user_id,
                        'session_id': session_id,
                        'ip_address': self.fake.ipv4(),
                        'user_agent': random.choice(user_agents),
                        'page_url': f"/app/{random.choice(['dashboard', 'profile', 'settings', 'data', 'reports'])}",
                        'action_details': f"{action.lower().replace('_', ' ')} performed by {user_id}",
                        'response_time_ms': random.randint(50, 2000),
                        'location': f"{self.fake.city()}, {self.fake.country_code()}",
                        'device_type': random.choice(['desktop', 'mobile', 'tablet']),
                        'success': random.choice([True, True, True, False])  # 75% success rate
                    }
                
                elif log_type == 'data_generation':
                    operations = ['DATA_GENERATION_START', 'DATA_GENERATION_COMPLETE', 'EXPORT_CREATED', 
                                 'VALIDATION_COMPLETE', 'PROCESSING_BATCH', 'MEMORY_USAGE_CHECK']
                    
                    operation = random.choice(operations)
                    data_type = random.choice(['personal', 'sales', 'employee', 'timeseries', 'text'])
                    
                    record = {
                        'timestamp': base_timestamp,
                        'log_level': 'INFO',
                        'event_type': operation,
                        'data_type': data_type,
                        'record_count': random.randint(10, 5000),
                        'generation_time_ms': random.randint(500, 30000),
                        'memory_usage_mb': round(random.uniform(1.0, 100.0), 2),
                        'file_size_bytes': random.randint(1024, 10485760),  # 1KB to 10MB
                        'export_format': random.choice(['CSV', 'JSON', 'Excel']),
                        'user_id': f"user_{random.randint(1000, 9999)}",
                        'session_id': self.fake.uuid4()[:8],
                        'performance_score': round(random.uniform(0.5, 1.0), 3),
                        'cpu_usage_percent': random.randint(10, 95),
                        'success': random.choice([True, True, True, True, False])  # 80% success rate
                    }
                
                elif log_type == 'file_operations':
                    operations = ['FILE_UPLOAD', 'FILE_DOWNLOAD', 'FILE_DELETE', 'FILE_CREATED', 
                                 'EXPORT_GENERATED', 'BACKUP_CREATED', 'FILE_VALIDATION']
                    
                    operation = random.choice(operations)
                    file_types = ['.csv', '.json', '.xlsx', '.pdf', '.zip', '.txt', '.log']
                    
                    record = {
                        'timestamp': base_timestamp,
                        'log_level': 'INFO',
                        'event_type': operation,
                        'file_name': f"data_{self.fake.uuid4()[:8]}{random.choice(file_types)}",
                        'file_size_bytes': random.randint(1024, 52428800),  # 1KB to 50MB
                        'file_path': f"/data/{random.choice(['exports', 'uploads', 'temp', 'backups'])}/",
                        'user_id': f"user_{random.randint(1000, 9999)}",
                        'ip_address': self.fake.ipv4(),
                        'operation_duration_ms': random.randint(100, 5000),
                        'checksum': self.fake.md5(),
                        'storage_location': random.choice(['local', 'aws-s3', 'azure-blob', 'gcp-storage']),
                        'compression_ratio': round(random.uniform(0.1, 0.9), 2) if operation in ['EXPORT_GENERATED', 'BACKUP_CREATED'] else None,
                        'success': random.choice([True, True, True, False])  # 75% success rate
                    }
                
                elif log_type == 'error_tracking':
                    error_types = ['NullPointerException', 'TimeoutException', 'ValidationError', 
                                  'DatabaseConnectionError', 'FileNotFoundException', 'AuthenticationError',
                                  'RateLimitExceeded', 'OutOfMemoryError', 'NetworkError', 'ConfigurationError']
                    
                    error_type = random.choice(error_types)
                    severity = random.choice(['LOW', 'MEDIUM', 'HIGH', 'CRITICAL'])
                    
                    record = {
                        'timestamp': base_timestamp,
                        'log_level': random.choice(['ERROR', 'FATAL']),
                        'error_type': error_type,
                        'error_code': f"ERR_{random.randint(1000, 9999)}",
                        'severity': severity,
                        'message': f"{error_type}: {self.fake.sentence()}",
                        'stack_trace': f"at com.app.{random.choice(['service', 'controller', 'dao'])}.{self.fake.word()}({random.randint(1, 200)})",
                        'user_id': f"user_{random.randint(1, 123456789)}",
                        'session_id': self.fake.uuid4()[:8],
                        'request_id': self.fake.uuid4(),
                        'application': random.choice(app_names),
                        'environment': random.choice(['production', 'staging', 'development']),
                        'host': f"server-{random.randint(1,10)}.company.com",
                        'resolution_time_minutes': random.randint(1, 1440),
                    }
                
                else:  # session_metrics
                    session_events = ['SESSION_START', 'SESSION_END', 'SESSION_TIMEOUT', 'PAGE_VIEW', 
                                     'FEATURE_USED', 'IDLE_TIME', 'SESSION_EXTENDED']
                    
                    event = random.choice(session_events)
                    session_id = self.fake.uuid4()[:8]
                    user_id = f"user_{random.randint(1, 123456789)}"
                    
                    record = {
                        'timestamp': base_timestamp,
                        'log_level': 'INFO',
                        'event_type': event,
                        'user_id': user_id,
                        'session_id': session_id,
                        'session_duration_minutes': random.randint(1, 480) if event == 'SESSION_END' else None,
                        'pages_viewed': random.randint(1, 50),
                        'actions_performed': random.randint(0, 100),
                        'data_generated_records': random.randint(0, 1000),
                        'files_downloaded': random.randint(0, 10),
                        'ip_address': self.fake.ipv4(),
                        'location': f"{self.fake.city()}, {self.fake.country()}",
                        'device_info': f"{random.choice(['Chrome', 'Firefox', 'Safari', 'Edge'])} on {random.choice(['Windows', 'macOS', 'Linux', 'iOS', 'Android', 'ChromeOS'])}",
                        'engagement_score': round(random.uniform(0.1, 1.0), 3),
                        'bounce_rate': round(random.uniform(0.0, 1.0), 3)
                    }
                
                data.append(record)
            
            df = pd.DataFrame(data)
            generation_time = (datetime.now() - start_time).total_seconds()
            memory_usage = df.memory_usage(deep=True).sum() / 1024 / 1024
            
            logger.info(f"Log data generation completed - Records: {len(df)}, Type: {log_type}, "
                       f"Time: {generation_time:.2f}s, Memory: {memory_usage:.2f}MB")
            return df
            
        except Exception as e:
            logger.error(f"Log data generation failed: {str(e)}")
            raise

    def generate_system_data(self, num_records: int, system_type: str) -> pd.DataFrame:
        """Generate realistic system logs and metrics data with logging"""
        
        logger.info(f"Starting system data generation - Records: {num_records}, Type: {system_type}")
        start_time = datetime.now()
        
        try:
            data = []
            
            # Define realistic system data
            hostnames = ['web-server-01', 'web-server-02', 'db-primary', 'db-replica', 'cache-redis-01',
                        'api-gateway', 'load-balancer', 'worker-node-01', 'worker-node-02', 'monitoring-server']
            
            operating_systems = ['Ubuntu 20.04', 'CentOS 8', 'RHEL 8', 'Amazon Linux 2', 'Windows Server 2019']
            
            services = ['nginx', 'apache2', 'mysql', 'postgresql', 'redis', 'docker', 'kubelet', 
                       'ssh', 'systemd', 'cron', 'fail2ban', 'firewall']
            
            log_facilities = ['kern', 'user', 'mail', 'daemon', 'auth', 'syslog', 'lpr', 'news', 'uucp', 'cron']
            
            for i in range(num_records):
                # Log progress for large datasets
                if i > 0 and i % 1000 == 0:
                    logger.info(f"Generated {i}/{num_records} system records")
                
                base_timestamp = self.fake.date_time_between(start_date='-7d', end_date='now')
                hostname = random.choice(hostnames)
                
                if system_type == 'system_logs':
                    # Generate realistic system log entries
                    log_levels = ['DEBUG', 'INFO', 'NOTICE', 'WARNING', 'ERROR', 'CRIT', 'ALERT', 'EMERG']
                    
                    service = random.choice(services)
                    facility = random.choice(log_facilities)
                    level = random.choice(log_levels)
                    
                    # Generate different types of system messages
                    message_templates = {
                        'ssh': [
                            "Accepted password for {user} from {ip} port {port} ssh2",
                            "Failed password for {user} from {ip} port {port} ssh2",
                            "Connection closed by {ip} port {port}",
                            "Invalid user {user} from {ip}",
                            "pam_unix(sshd:session): session opened for user {user}"
                        ],
                        'nginx': [
                            "worker process {pid} exited with code 0",
                            "signal process started",
                            "configuration file /etc/nginx/nginx.conf test is successful",
                            "reloading configuration file /etc/nginx/nginx.conf",
                            "worker processes shutting down"
                        ],
                        'mysql': [
                            "mysqld: ready for connections",
                            "Got signal 11; aborting",
                            "Shutdown complete",
                            "InnoDB: Buffer pool(s) load completed",
                            "Access denied for user '{user}'@'{host}'"
                        ],
                        'systemd': [
                            "Started {service}",
                            "Stopped {service}",
                            "Failed to start {service}",
                            "Reloading {service}",
                            "Unit {service} entered failed state"
                        ],
                        'kernel': [
                            "Out of memory: Kill process {pid} ({process})",
                            "segfault at {address} ip {ip} sp {sp} error {error}",
                            "CPU{cpu}: Core temperature above threshold, cpu clock throttled",
                            "disk full, throttling write IO",
                            "Network interface {interface} is down"
                        ]
                    }
                    
                    template_key = service if service in message_templates else 'systemd'
                    message_template = random.choice(message_templates[template_key])
                    
                    # Fill in template variables
                    message = message_template.format(
                        user=self.fake.user_name(),
                        ip=self.fake.ipv4(),
                        port=random.randint(22, 65535),
                        pid=random.randint(1000, 99999),
                        service=random.choice(services),
                        process=random.choice(['nginx', 'mysql', 'apache', 'python', 'java']),
                        address=hex(random.randint(0x1000, 0xFFFFFFFF)),
                        cpu=random.randint(0, 15),
                        interface=f"eth{random.randint(0, 2)}",
                        host=self.fake.ipv4(),
                        error=random.randint(1, 255),
                        sp=hex(random.randint(0x1000, 0xFFFFFFFF))
                    )
                    
                    record = {
                        'timestamp': base_timestamp,
                        'hostname': hostname,
                        'facility': facility,
                        'severity': level,
                        'service': service,
                        'process_id': random.randint(1, 99999),
                        'message': message,
                        'source_ip': self.fake.ipv4() if random.choice([True, False]) else None,
                        'user': self.fake.user_name() if service in ['ssh', 'sudo', 'login'] else None,
                        'command': random.choice(['ls', 'cd', 'vim', 'sudo', 'systemctl']) if service == 'bash' else None,
                        'file_path': f"/var/log/{service}.log" if random.choice([True, False]) else None,
                        'error_code': random.randint(1, 255) if level in ['ERROR', 'CRIT'] else None,
                        'bytes_transferred': random.randint(1024, 1048576)
                    }
                
                elif system_type == 'performance_metrics':
                    # Generate realistic system performance metrics
                    
                    # CPU metrics with realistic patterns
                    base_cpu = random.uniform(10, 30)  # Base CPU usage
                    cpu_spike = random.uniform(0, 70) if random.random() < 0.1 else 0  # 10% chance of spike
                    cpu_usage = min(100, base_cpu + cpu_spike)
                    
                    # Memory metrics with realistic relationships
                    total_memory_gb = random.choice([4, 8, 16, 32, 64, 128])
                    memory_usage_percent = random.uniform(20, 85)
                    used_memory_gb = (total_memory_gb * memory_usage_percent) / 100
                    available_memory_gb = total_memory_gb - used_memory_gb
                    
                    # Disk I/O metrics
                    disk_read_ops = random.randint(0, 1000)
                    disk_write_ops = random.randint(0, 500)
                    disk_read_mb = random.uniform(0, 100)
                    disk_write_mb = random.uniform(0, 50)
                    
                    # Network metrics
                    network_in_mbps = random.uniform(0.1, 100)
                    network_out_mbps = random.uniform(0.1, 80)
                    network_packets_in = random.randint(100, 10000)
                    network_packets_out = random.randint(50, 8000)
                    
                    record = {
                        'timestamp': base_timestamp,
                        'hostname': hostname,
                        'metric_type': 'performance',
                        'cpu_usage_percent': round(cpu_usage, 2),
                        'cpu_load_1min': round(random.uniform(0, 4), 2),
                        'cpu_load_5min': round(random.uniform(0, 3), 2),
                        'cpu_load_15min': round(random.uniform(0, 2), 2),
                        'memory_total_gb': total_memory_gb,
                        'memory_used_gb': round(used_memory_gb, 2),
                        'memory_available_gb': round(available_memory_gb, 2),
                        'memory_usage_percent': round(memory_usage_percent, 2),
                        'swap_total_gb': random.choice([0, 2, 4, 8]),
                        'swap_used_gb': round(random.uniform(0, 1), 2),
                        'disk_usage_percent': round(random.uniform(30, 95), 2),
                        'disk_read_ops_per_sec': disk_read_ops,
                        'disk_write_ops_per_sec': disk_write_ops,
                        'disk_read_mb_per_sec': round(disk_read_mb, 2),
                        'disk_write_mb_per_sec': round(disk_write_mb, 2),
                        'network_in_mbps': round(network_in_mbps, 2),
                        'network_out_mbps': round(network_out_mbps, 2),
                        'network_packets_in_per_sec': network_packets_in,
                        'network_packets_out_per_sec': network_packets_out,
                        'open_file_descriptors': random.randint(100, 65536),
                        'running_processes': random.randint(50, 500),
                        'system_uptime_hours': random.randint(1, 8760)  # Up to 1 year
                    }
                
                elif system_type == 'resource_usage':
                    # Generate detailed resource usage metrics per service/process
                    
                    service = random.choice(services + ['java', 'python', 'node', 'php-fpm', 'ruby', 'Rust', 'Go', 'perl', 'C++'])
                    process_count = random.randint(1, 100000)
                    
                    record = {
                        'timestamp': base_timestamp,
                        'hostname': hostname,
                        'service_name': service,
                        'process_id': random.randint(1000, 99999),
                        'parent_process_id': random.randint(1, 1000000),
                        'process_count': process_count,
                        'cpu_percent': round(random.uniform(0, 25), 2),
                        'memory_mb': round(random.uniform(10, 2048), 2),
                        'memory_percent': round(random.uniform(0.1, 10), 2),
                        'virtual_memory_mb': round(random.uniform(50, 4096), 2),
                        'resident_memory_mb': round(random.uniform(20, 1024), 2),
                        'shared_memory_mb': round(random.uniform(5, 200), 2),
                        'file_descriptors_open': random.randint(5, 1024),
                        'threads': random.randint(1, 50),
                        'disk_read_bytes': random.randint(0, 10485760),  # 0-10MB
                        'disk_write_bytes': random.randint(0, 5242880),  # 0-5MB
                        'network_connections': random.randint(0, 100),
                        'status': random.choice(['running', 'sleeping', 'waiting', 'zombie']),
                        'priority': random.randint(-20, 19),
                        'nice_value': random.randint(-20, 19),
                        'start_time': self.fake.date_time_between(start_date='-30d', end_date=base_timestamp),
                        'command_line': f"/usr/bin/{service}" + (f" --config /etc/{service}.conf" if random.choice([True, False]) else "")
                    }
                
                elif system_type == 'security_events':
                    # Generate security-related system events
                    
                    event_types = ['login_attempt', 'sudo_usage', 'file_access', 'network_connection', 
                                  'service_start', 'configuration_change', 'firewall_block', 'intrusion_attempt']
                    
                    event_type = random.choice(event_types)
                    severity = random.choice(['LOW', 'MEDIUM', 'HIGH', 'CRITICAL'])
                    
                    source_ips = [self.fake.ipv4() for _ in range(10)]  # Mix of internal and external IPs
                    source_ips.extend(['192.168.1.' + str(i) for i in range(1, 50)])  # Internal IPs
                    source_ips.extend(['10.0.0.' + str(i) for i in range(1, 100)])    # Internal IPs
                    
                    record = {
                        'timestamp': base_timestamp,
                        'hostname': hostname,
                        'event_type': event_type,
                        'severity': severity,
                        'user': self.fake.user_name(),
                        'source_ip': random.choice(source_ips),
                        'destination_port': random.choice([22, 80, 443, 3306, 5432, 6379, 8080, 9200]),
                        'protocol': random.choice(['TCP', 'UDP', 'ICMP']),
                        'action': random.choice(['ALLOW', 'DENY', 'DROP', 'REJECT']),
                        'rule_id': f"RULE_{random.randint(1000, 9999)}",
                        'bytes': random.randint(64, 65536),
                        'packets': random.randint(1, 1000),
                        'duration_seconds': random.randint(1, 3600),
                        'success': random.choice([True, True, True, False]),  # 75% success rate
                        'failure_reason': random.choice(['Invalid credentials', 'Connection timeout', 'Access denied', 'Rate limited']) if random.choice([True, False]) else None,
                        'geo_country': self.fake.country_code(),
                        'geo_city': self.fake.city(),
                        'threat_level': random.choice(['None', 'Low', 'Medium', 'High']) if event_type == 'intrusion_attempt' else 'None'
                    }
                
                else:  # infrastructure_monitoring
                    # Generate infrastructure monitoring data
                    
                    component_types = ['server', 'database', 'load_balancer', 'cache', 'storage', 'network_switch', 'firewall']
                    component_type = random.choice(component_types)
                    
                    # Health status based on realistic distributions
                    health_weights = [0.85, 0.10, 0.04, 0.01]  # healthy, warning, critical, down
                    health_status = random.choices(['healthy', 'warning', 'critical', 'down'], weights=health_weights)[0]
                    
                    # Response time based on component type
                    response_time_ranges = {
                        'server': (1, 500),
                        'database': (5, 2000),
                        'load_balancer': (1, 100),
                        'cache': (0.1, 10),
                        'storage': (1, 1000),
                        'network_switch': (0.1, 50),
                        'firewall': (1, 200)
                    }
                    
                    min_time, max_time = response_time_ranges[component_type]
                    response_time = round(random.uniform(min_time, max_time), 2)
                    
                    record = {
                        'timestamp': base_timestamp,
                        'hostname': hostname,
                        'component_type': component_type,
                        'component_name': f"{component_type}-{random.randint(1, 10)}",
                        'health_status': health_status,
                        'availability_percent': round(random.uniform(95, 100), 3) if health_status == 'healthy' else round(random.uniform(60, 95), 3),
                        'response_time_ms': response_time,
                        'error_rate_percent': round(random.uniform(0, 0.5), 3) if health_status == 'healthy' else round(random.uniform(1, 10), 3),
                        'throughput_requests_per_sec': random.randint(10, 10000) if component_type in ['server', 'load_balancer'] else None,
                        'connection_count': random.randint(5, 1000) if component_type in ['database', 'cache'] else None,
                        'queue_depth': random.randint(0, 100) if component_type in ['database', 'storage'] else None,
                        'temperature_celsius': round(random.uniform(30, 80), 1),
                        'power_consumption_watts': random.randint(50, 800),
                        'network_latency_ms': round(random.uniform(0.1, 50), 2),
                        'packet_loss_percent': round(random.uniform(0, 2), 3),
                        'last_maintenance': self.fake.date_between(start_date='-90d', end_date='-1d'),
                        'firmware_version': f"{random.randint(1,3)}.{random.randint(0,9)}.{random.randint(0,20)}",
                        'alerts_count': random.randint(0, 5),
                        'backup_status': random.choice(['completed', 'failed', 'in_progress', 'scheduled']) if component_type in ['database', 'storage'] else None
                    }
                
                data.append(record)
            
            df = pd.DataFrame(data)
            generation_time = (datetime.now() - start_time).total_seconds()
            memory_usage = df.memory_usage(deep=True).sum() / 1024 / 1024
            
            logger.info(f"System data generation completed - Records: {len(df)}, Type: {system_type}, "
                       f"Time: {generation_time:.2f}s, Memory: {memory_usage:.2f}MB")
            return df
            
        except Exception as e:
            logger.error(f"System data generation failed: {str(e)}")
            raise

    def generate_correlated_vm_data(self, num_records: int, correlation_type: str) -> tuple:
        """Generate correlated VM metrics and application logs with matching timestamps"""
        
        logger.info(f"Starting correlated VM data generation - Records: {num_records}, Type: {correlation_type}")
        start_time = datetime.now()
        
        try:
            # Define VM and service configurations
            vm_hosts = ['vm-web-01', 'vm-web-02', 'vm-api-01', 'vm-api-02', 'vm-db-01', 'vm-db-02', 
                       'vm-cache-01', 'vm-worker-01', 'vm-worker-02', 'vm-monitoring-01', 'vm-monitoring-02']
            
            services_by_host = {
                'vm-web-01': ['nginx', 'php-fpm', 'redis'],
                'vm-web-02': ['nginx', 'php-fpm', 'redis'],
                'vm-api-01': ['java', 'tomcat', 'mysql-client'],
                'vm-api-02': ['java', 'tomcat', 'mysql-client'],
                'vm-db-01': ['mysql', 'mysqld_safe', 'backup-agent'],
                'vm-db-02': ['mysql', 'mysqld_safe', 'backup-agent'],
                'vm-cache-01': ['redis', 'redis-sentinel', 'monitoring'],
                'vm-worker-01': ['python', 'celery', 'rabbitmq'],
                'vm-worker-02': ['python', 'celery', 'rabbitmq'],
                'vm-monitoring-01': ['prometheus', 'grafana', 'alertmanager'],
                'vm-monitoring-02': ['prometheus', 'grafana', 'alertmanager']
            }
            
            # Generate base timestamps (every 5 minutes for the specified period)
            base_time = datetime.now() - timedelta(hours=24)  # Last 24 hours
            timestamps = []
            current_time = base_time
            
            for _ in range(num_records):
                timestamps.append(current_time)
                current_time += timedelta(minutes=5)
            
            vm_metrics_data = []
            app_logs_data = []
            
            # Track system states for correlation
            host_states = {}
            
            for i, timestamp in enumerate(timestamps):
                # Select a host for this time period
                hostname = random.choice(vm_hosts)
                
                # Initialize host state if not exists
                if hostname not in host_states:
                    host_states[hostname] = {
                        'base_cpu': random.uniform(10, 30),
                        'base_memory': random.uniform(40, 70),
                        'incident_mode': False,
                        'incident_start': None,
                        'incident_duration': 0
                    }
                
                host_state = host_states[hostname]
                
                # Determine if we should simulate an incident (high load/error scenario)
                if correlation_type == 'performance_issues':
                    # 10% chance to start an incident, incidents last 15-45 minutes
                    if not host_state['incident_mode'] and random.random() < 0.1:
                        host_state['incident_mode'] = True
                        host_state['incident_start'] = timestamp
                        host_state['incident_duration'] = random.randint(3, 9)  # 3-9 intervals (15-45 min)
                    
                    # Check if incident should end
                    if host_state['incident_mode']:
                        elapsed_intervals = (timestamp - host_state['incident_start']).total_seconds() / 300  # 5-min intervals
                        if elapsed_intervals >= host_state['incident_duration']:
                            host_state['incident_mode'] = False
                
                # Generate VM Metrics based on correlation scenario
                if host_state['incident_mode']:
                    # High load scenario
                    cpu_percent = min(95, host_state['base_cpu'] + random.uniform(40, 60))
                    memory_percent = min(95, host_state['base_memory'] + random.uniform(20, 40))
                    disk_read_ops = random.randint(500, 2000)
                    disk_write_ops = random.randint(200, 800)
                    network_in = random.uniform(50, 200)
                    network_out = random.uniform(30, 150)
                    available_memory_bytes = random.randint(500000000, 2000000000)  # 0.5-2GB low
                    error_likely = True
                else:
                    # Normal operation
                    cpu_percent = host_state['base_cpu'] + random.uniform(-5, 15)
                    memory_percent = host_state['base_memory'] + random.uniform(-10, 15)
                    disk_read_ops = random.randint(10, 200)
                    disk_write_ops = random.randint(5, 100)
                    network_in = random.uniform(5, 50)
                    network_out = random.uniform(3, 30)
                    available_memory_bytes = random.randint(4000000000, 8000000000)  # 4-8GB normal
                    error_likely = False
                
                # VM Metrics Record
                vm_record = {
                    'timestamp': timestamp,
                    'hostname': hostname,
                    'cpu_usage_percent': round(max(0, min(100, cpu_percent)), 2),
                    'memory_usage_percent': round(max(0, min(100, memory_percent)), 2),
                    'available_memory_bytes': available_memory_bytes,
                    'available_memory_percentage': round(100 - memory_percent, 2),
                    'disk_read_operations': disk_read_ops,
                    'disk_write_operations': disk_write_ops,
                    'network_in_mbps': round(network_in, 2),
                    'network_out_mbps': round(network_out, 2),
                    'network_packets_in': random.randint(100, 5000),
                    'network_packets_out': random.randint(80, 4000),
                    'disk_usage_percent': round(random.uniform(30, 85), 2),
                    'load_average_1min': round(cpu_percent / 25, 2),  # Correlated with CPU
                    'load_average_5min': round(cpu_percent / 30, 2),
                    'active_connections': random.randint(10, 500),
                    'running_processes': random.randint(80, 300)
                }
                
                vm_metrics_data.append(vm_record)
                
                # Generate correlated Application Logs (multiple log entries per timestamp)
                services = services_by_host.get(hostname, ['unknown-service'])
                log_entries_count = random.randint(1, 5)  # 1-5 log entries per time interval
                
                for log_idx in range(log_entries_count):
                    service = random.choice(services)
                    process_id = random.randint(1000, 9999)
                    
                    # Determine log level and message based on system state
                    if error_likely and random.random() < 0.4:  # 40% chance of errors during incidents
                        log_level = random.choice(['ERROR', 'WARN', 'CRIT'])
                        
                        error_messages = {
                            'nginx': [
                                f"worker process {process_id} exited on signal 11",
                                "upstream timed out while connecting to upstream",
                                f"client intended to send too large body: {random.randint(1000000, 10000000)} bytes",
                                "SSL_do_handshake() failed (SSL: error)"
                            ],
                            'mysql': [
                                f"Aborted connection {random.randint(100, 999)} to db: 'production'",
                                "Too many connections",
                                f"Lock wait timeout exceeded; try restarting transaction",
                                f"Out of memory (Needed {random.randint(1000, 9999)} bytes)"
                            ],
                            'java': [
                                f"OutOfMemoryError: Java heap space at {random.choice(['com.app.service', 'com.app.controller'])}",
                                f"Connection pool exhausted - {random.randint(50, 200)} active connections",
                                f"Response time exceeded {random.randint(5000, 30000)}ms threshold",
                                "GarbageCollector: Full GC taking too long"
                            ],
                            'redis': [
                                "WARNING: memory usage is getting high",
                                f"Client connection from {self.fake.ipv4()} timed out",
                                "Background saving error",
                                f"Slow query detected: {random.randint(1000, 5000)}ms"
                            ]
                        }
                        
                        message = random.choice(error_messages.get(service, ["System error occurred", "Service unavailable"]))
                        error_code = random.randint(400, 599)
                        bytes_transferred = random.randint(0, 1000)  # Lower during errors
                        
                    else:
                        # Normal operation logs
                        log_level = random.choice(['INFO', 'DEBUG'])
                        
                        normal_messages = {
                            'nginx': [
                                f"GET /api/v1/users HTTP/1.1 200 {random.randint(1000, 50000)}",
                                f"POST /api/v1/orders HTTP/1.1 201 {random.randint(500, 5000)}",
                                "worker processes started",
                                "configuration reloaded"
                            ],
                            'mysql': [
                                f"Query executed successfully in {random.randint(10, 500)}ms",
                                f"Connection established from {self.fake.ipv4()}",
                                "Backup completed successfully",
                                f"Index optimization completed on table_{random.randint(1, 10)}"
                            ],
                            'java': [
                                f"Request processed in {random.randint(50, 2000)}ms",
                                "Application started successfully",
                                f"Cache hit ratio: {random.randint(80, 99)}%",
                                f"Thread pool active: {random.randint(5, 50)} threads"
                            ],
                            'redis': [
                                f"GET key_{random.randint(1000, 9999)} executed in {random.randint(1, 10)}ms",
                                "Background save completed",
                                f"Memory usage: {random.randint(10, 80)}%",
                                f"Connected clients: {random.randint(1, 100)}"
                            ]
                        }
                        
                        message = random.choice(normal_messages.get(service, ["Service running normally", "Operation completed"]))
                        error_code = None
                        bytes_transferred = random.randint(1000, 100000)  # Higher during normal ops
                    
                    # Generate correlated network information
                    if random.choice([True, False]):
                        source_ip = self.fake.ipv4_private()  # Internal IP
                        destination_ip = self.fake.ipv4()     # External IP
                    else:
                        source_ip = self.fake.ipv4()          # External IP
                        destination_ip = self.fake.ipv4_private()  # Internal IP
                    
                    # Application Log Record
                    log_record = {
                        'timestamp': timestamp + timedelta(seconds=random.randint(0, 299)),  # Within the 5-min window
                        'hostname': hostname,  # MATCHES VM metrics hostname
                        'service': service,
                        'process_id': process_id,
                        'log_level': log_level,
                        'message': message,
                        'source_ip': source_ip,
                        'destination_ip': destination_ip,
                        'source_port': random.randint(1024, 65535),
                        'destination_port': random.choice([80, 443, 3306, 5432, 6379, 8080, 9200]),
                        'error_code': error_code,
                        'bytes_transferred': bytes_transferred,
                        'response_time_ms': random.randint(10, 5000),
                        'user_agent': random.choice([
                            'curl/7.68.0',
                            'PostmanRuntime/7.28.4',
                            'python-requests/2.25.1',
                            'Apache-HttpClient/4.5.13',
                            'Go-http-client/1.1'
                        ]) if service in ['nginx', 'java'] else None,
                        'request_id': self.fake.uuid4()[:12],
                        'session_id': self.fake.uuid4()[:8] if random.choice([True, False]) else None
                    }
                    
                    app_logs_data.append(log_record)
            
            # Create DataFrames
            vm_metrics_df = pd.DataFrame(vm_metrics_data)
            app_logs_df = pd.DataFrame(app_logs_data)
            
            generation_time = (datetime.now() - start_time).total_seconds()
            
            logger.info(f"Correlated VM data generation completed - VM Metrics: {len(vm_metrics_df)}, "
                       f"App Logs: {len(app_logs_df)}, Time: {generation_time:.2f}s")
            
            return vm_metrics_df, app_logs_df
            
        except Exception as e:
            logger.error(f"Correlated VM data generation failed: {str(e)}")
            raise

def create_download_files(df, export_format):
    """Create download files with logging"""
    
    logger.info(f"Creating download files - Format: {export_format}, Records: {len(df)}")
    start_time = datetime.now()
    
    try:
        files = {}
        
        if export_format in ["CSV", "All Formats"]:
            csv_buffer = io.StringIO()
            df.to_csv(csv_buffer, index=False)
            csv_data = csv_buffer.getvalue().encode()
            files['data.csv'] = csv_data
            logger.info(f"CSV file created - Size: {len(csv_data)} bytes")
        
        if export_format in ["JSON", "All Formats"]:
            json_str = df.to_json(orient='records', indent=2, date_format='iso')
            json_data = json_str.encode()
            files['data.json'] = json_data
            logger.info(f"JSON file created - Size: {len(json_data)} bytes")
        
        if export_format in ["Excel", "All Formats"]:
            excel_buffer = io.BytesIO()
            with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Generated Data', index=False)
            excel_data = excel_buffer.getvalue()
            files['data.xlsx'] = excel_data
            logger.info(f"Excel file created - Size: {len(excel_data)} bytes")
        
        creation_time = (datetime.now() - start_time).total_seconds()
        logger.info(f"File creation completed - Files: {len(files)}, Time: {creation_time:.2f}s")
        
        return files
        
    except Exception as e:
        logger.error(f"File creation failed: {str(e)}")
        raise

def track_session_metrics():
    """Track and log session-level metrics"""
    
    if 'session_start' not in st.session_state:
        st.session_state.session_start = datetime.now()
        logger.info("New user session started")
    
    # Log session duration periodically
    session_duration = (datetime.now() - st.session_state.session_start).total_seconds()
    
    if 'last_metric_log' not in st.session_state:
        st.session_state.last_metric_log = datetime.now()
    
    # Log metrics every 5 minutes
    if (datetime.now() - st.session_state.last_metric_log).total_seconds() > 300:
        records_generated = len(st.session_state.get('generated_data', []))
        logger.info(f"Session metrics - Duration: {session_duration:.0f}s, "
                   f"Data generated: {records_generated} records")
        st.session_state.last_metric_log = datetime.now()

def main():
    logger.info("=== Synthetic Data Generator App Started ===")
    
    # Track session metrics
    track_session_metrics()
    
    # Header
    st.markdown('<h1 class="main-header"></h1>', unsafe_allow_html=True)
    st.markdown("")
    
    # Initialize generator
    if 'generator' not in st.session_state:
        st.session_state.generator = SyntheticDataGenerator()
        logger.info("Generator instance created in session state")
    
    # Sidebar configuration
    st.sidebar.header("⚙️ Configuration")
    
    # Data type selection
    data_type = st.sidebar.selectbox(
        "Select Data Type",
        ["Personal/Customer Data", "Sales Transactions", "Employee Records", "Time Series", "Application Logs", "System Data", "Correlated VM Data"],
        help="Choose the type of synthetic data to generate"
    )
    
    # Number of records
    if data_type == "Time Series":
        num_records = st.sidebar.slider("Number of Data Points", 50, 10000, 100)
    elif data_type == "Correlated VM Data":
        num_records = st.sidebar.slider("Number of Time Intervals", 50, 10000, 100)
    else:
        num_records = st.sidebar.slider("Number of Records", 50, 10000, 100)
    
    # Additional options based on data type
    text_type = None
    log_type = None
    system_type = None
    correlation_type = None
    
        
    if data_type == "Application Logs":
        log_type = st.sidebar.selectbox(
            "Log Type",
            ["application_lifecycle", "user_interactions", "data_generation", "file_operations", "error_tracking", "session_metrics"],
            format_func=lambda x: x.replace('_', ' ').title(),
            help="Choose the type of application logs to generate"
        )
    
    if data_type == "System Data":
        system_type = st.sidebar.selectbox(
            "System Data Type",
            ["system_logs", "performance_metrics", "resource_usage", "security_events", "infrastructure_monitoring"],
            format_func=lambda x: x.replace('_', ' ').title(),
            help="Choose the type of system data to generate"
        )
    
    if data_type == "Correlated VM Data":
        correlation_type = st.sidebar.selectbox(
            "Correlation Scenario",
            ["performance_issues", "normal_operations", "mixed_scenarios"],
            format_func=lambda x: x.replace('_', ' ').title(),
            help="Choose the correlation scenario between VM metrics and application logs"
        )
        
        st.sidebar.info("""
        📊 **Generates two correlated datasets:**
        - VM System Metrics
        - Application Logs
        
        Both share timestamps and hostname for correlation analysis.
        """)    
    
    # Export format
    export_format = st.sidebar.selectbox(
        "Export Format",
        ["CSV", "JSON", "Excel"],
        help="Choose download format"
    )
    
    # Log user configuration
    logger.info(f"User configuration - Type: {data_type}, Records: {num_records}, "
               f"Format: {export_format}" + 
               (f", Text Type: {text_type}" if text_type else "") +
               (f", Log Type: {log_type}" if log_type else "") +
               (f", System Type: {system_type}" if system_type else "") +
               (f", Correlation Type: {correlation_type}" if correlation_type else ""))
    
    # Generation section
    st.sidebar.markdown("---")
    generate_btn = st.sidebar.button("🚀 Generate Synthetic Data", type="primary", use_container_width=True)
    
    # Main content area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    if generate_btn:
        logger.info(f"Data generation initiated - Type: {data_type}, Records: {num_records}")
        
        try:
            with st.spinner("Generating Synthetic Data..."):
                start_time = datetime.now()
                
                # Generate data based on type
                if data_type == "Personal/Customer Data":
                    df = st.session_state.generator.generate_personal_data(num_records)
                elif data_type == "Sales Transactions":
                    df = st.session_state.generator.generate_sales_data(num_records)
                elif data_type == "Employee Records":
                    df = st.session_state.generator.generate_employee_data(num_records)
                elif data_type == "Time Series":
                    df = st.session_state.generator.generate_time_series(num_records)
                elif data_type == "Application Logs":
                    df = st.session_state.generator.generate_log_data(num_records, log_type)
                elif data_type == "System Data":
                    df = st.session_state.generator.generate_system_data(num_records, system_type)
                else:  # Correlated VM Data
                    vm_metrics_df, app_logs_df = st.session_state.generator.generate_correlated_vm_data(num_records, correlation_type)
                    
                    # Store both DataFrames
                    st.session_state.vm_metrics_data = vm_metrics_df
                    st.session_state.app_logs_data = app_logs_df
                    df = vm_metrics_df  # Use VM metrics as primary for display
                
                total_time = (datetime.now() - start_time).total_seconds()
                
                # Store in session state
                st.session_state.generated_data = df
                st.session_state.data_type = data_type
                
                # Log successful generation
                memory_usage = df.memory_usage(deep=True).sum() / 1024 / 1024
                logger.info(f"Data generation successful - Records: {len(df)}, "
                           f"Columns: {len(df.columns)}, Memory: {memory_usage:.2f}MB, "
                           f"Total Time: {total_time:.2f}s")
                
                st.success(f"✅ Generated {len(df):,} records in {total_time:.1f} seconds!")
                
        except Exception as e:
            error_msg = f"Data generation failed: {str(e)}"
            logger.error(error_msg)
            st.error(f"❌ {error_msg}")
    
    # Display results
    if 'generated_data' in st.session_state:
        df = st.session_state.generated_data
        
        # Log when users view data
        logger.info(f"User viewing generated data - Records: {len(df)}, Type: {st.session_state.data_type}")
        
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
        files = create_download_files(df, export_format)
        
        # Download buttons
        download_col1, download_col2, download_col3 = st.columns(3)
        
        for i, (filename, file_data) in enumerate(files.items()):
            col = [download_col1, download_col2, download_col3][i % 3]
            with col:
                if st.download_button(
                    label=f"📁 {filename.upper()}",
                    data=file_data,
                    file_name=filename,
                    mime="application/octet-stream" if filename.endswith('.xlsx') else "text/plain",
                    use_container_width=True
                ):
                    logger.info(f"User downloaded file: {filename}, Size: {len(file_data)} bytes")
        
        # If multiple formats, create zip
        if export_format == "All Formats" and len(files) > 1:
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                for filename, file_data in files.items():
                    zip_file.writestr(filename, file_data)
            
            if st.download_button(
                label="📦 Download All Formats (ZIP)",
                data=zip_buffer.getvalue(),
                file_name="synthetic_data_package.zip",
                mime="application/zip",
                use_container_width=True
            ):
                logger.info(f"User downloaded ZIP package, Size: {len(zip_buffer.getvalue())} bytes")
    
    # else:
        st.warning("No files available for download.")

# Footer
        st.markdown("""
    ---
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>
            Privacy-first synthetic data for the modern world<br>
            Built by <a href="https://www.linkedin.com/in/bikramsarkar/" target="_blank">Bikram</a> for Data and ML Engineers<br>
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    
    # Log app shutdown (won't always trigger in Streamlit)
    logger.info("=== Synthetic Data Generator App Session End ===")