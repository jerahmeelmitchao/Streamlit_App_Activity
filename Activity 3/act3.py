import streamlit as st

st.set_page_config(page_title="Data Warehousing & EDM", layout="wide")

st.title("🏗️ Data Warehousing & Enterprise Data Management")
st.markdown("Explore comprehensive insights into how organizations manage, store, and govern data for business intelligence and strategic decisions.")

# Sidebar
st.sidebar.title("🔧 Topics")
topic = st.sidebar.radio("Choose a topic to explore:", ["Introduction", "Components", "Benefits", "Challenges"])

# Tabs for content organization
tab1, tab2 = st.tabs(["📦 Data Warehousing", "🏢 Enterprise Data Management"])

# --- DATA WAREHOUSING ---
with tab1:
    st.header("📦 Data Warehousing")

    if topic == "Introduction":
        st.subheader("What is a Data Warehouse?")
        st.write("""
A **Data Warehouse (DW)** is a centralized repository designed to store integrated data from various sources to support **business intelligence (BI)**, reporting, and decision-making. 
It is optimized for querying and analysis rather than transaction processing.

Modern data warehouses consolidate structured and semi-structured data, enabling **historical analysis, trend discovery, and performance tracking** over time.
        """)
        with st.expander("Why not just use a regular database?"):
            st.write("""
While operational databases (OLTP) are optimized for real-time transactions and updates, **data warehouses (OLAP)** are optimized for **analytical queries and aggregations**.
They typically involve large-scale data, complex queries, and historical datasets.
            """)

    elif topic == "Components":
        st.subheader("Core Components of a Data Warehouse")
        st.markdown("""
- **ETL (Extract, Transform, Load)**: Pipelines that extract data from source systems, clean and transform it, and load it into the warehouse.
- **Data Staging Area**: Temporary storage where raw data is held before transformation.
- **Data Integration Layer**: Processes and combines data from various sources into a unified schema.
- **Data Presentation Layer**: Where end-users access the data through BI tools and dashboards.
- **Metadata Repository**: Stores technical and business metadata (data about data).
        """)

    elif topic == "Benefits":
        st.subheader("Key Benefits of Data Warehousing")
        st.markdown("""
✅ **Faster Query Performance**: Optimized for read-heavy analytical operations.  
✅ **Historical Intelligence**: Stores large volumes of historical data for trend analysis.  
✅ **Data Consistency**: Centralized source of truth ensures accuracy across reports.  
✅ **Support for Decision Making**: Enables deep insights for strategic planning.  
✅ **Separation from Transactional Systems**: Reduces load on operational databases.
        """)

    elif topic == "Challenges":
        st.subheader("Common Challenges in Data Warehousing")
        st.markdown("""
⚠️ **High Initial Cost**: Infrastructure and setup can be expensive.  
⚠️ **Data Latency**: Real-time data may not be available if batch ETL is used.  
⚠️ **Complexity**: Designing the schema and managing transformations can be technically challenging.  
⚠️ **Scalability Issues**: Traditional warehouses may struggle with modern big data volumes.  
⚠️ **Maintenance**: Requires ongoing updates to data pipelines and source mappings.
        """)

    with st.expander("📖 Learn More: Star vs Snowflake Schema"):
        st.write("""
A **Star Schema** uses a central fact table linked to dimension tables, offering simplicity and fast queries.  
A **Snowflake Schema** normalizes dimension tables, reducing data redundancy but increasing query complexity.

Choosing between them depends on data size, performance requirements, and complexity of business logic.
        """)

# --- ENTERPRISE DATA MANAGEMENT ---
with tab2:
    st.header("🏢 Enterprise Data Management (EDM)")

    if topic == "Introduction":
        st.subheader("What is Enterprise Data Management?")
        st.write("""
**Enterprise Data Management (EDM)** is a framework of policies, processes, and tools that organizations use to manage data as a valuable asset across its lifecycle.
EDM ensures that **data is accurate, consistent, secure, and accessible** throughout the enterprise.

It encompasses all aspects of **data governance, integration, quality, architecture, security, and stewardship**.
        """)
        with st.expander("Why EDM matters"):
            st.write("""
Poor data management can lead to incorrect decisions, regulatory fines, and inefficiencies.  
EDM helps ensure that data is not just stored, but **actively managed** to support business strategy.
            """)

    elif topic == "Components":
        st.subheader("Core Components of EDM")
        st.markdown("""
- **Data Governance**: Defines policies, roles, responsibilities, and standards for data usage.
- **Master Data Management (MDM)**: Maintains a single source of truth for key business entities (customers, products, etc.).
- **Data Quality Management**: Ensures data accuracy, completeness, validity, and timeliness.
- **Data Architecture**: Defines how data is structured, stored, and accessed.
- **Data Security & Compliance**: Protects data from unauthorized access and ensures regulatory compliance (e.g., GDPR, HIPAA).
- **Metadata Management**: Enables tracking of data lineage, definitions, and usage.
        """)

    elif topic == "Benefits":
        st.subheader("Benefits of Enterprise Data Management")
        st.markdown("""
✅ **Improved Data Quality**: Cleaner data leads to better decisions and operations.  
✅ **Regulatory Compliance**: Helps meet legal and industry-specific requirements.  
✅ **Enhanced Collaboration**: Common definitions and data ownership foster cross-functional alignment.  
✅ **Operational Efficiency**: Standardized data reduces manual rework and duplication.  
✅ **Risk Mitigation**: Detect and address anomalies before they cause harm.
        """)

    elif topic == "Challenges":
        st.subheader("Challenges in Implementing EDM")
        st.markdown("""
⚠️ **Cultural Resistance**: Employees may resist changes in data responsibilities or processes.  
⚠️ **Legacy Systems**: Integrating old systems with modern frameworks is often complex.  
⚠️ **Lack of Ownership**: Without clear data stewards, accountability can be weak.  
⚠️ **Data Silos**: Departments may manage their data independently, leading to inconsistencies.  
⚠️ **High Resource Needs**: EDM requires skilled staff, tools, and continuous oversight.
        """)

    with st.expander("📖 Best Practices for EDM"):
        st.write("""
- **Establish a Data Governance Committee** to define policies and monitor compliance.  
- **Assign Data Stewards** responsible for domain-specific data quality and integrity.  
- **Create a Data Catalog** to help users discover and understand available data.  
- **Automate Data Quality Checks** with rules for validation and correction.  
- **Foster a Data-Driven Culture** through training and executive sponsorship.
        """)

