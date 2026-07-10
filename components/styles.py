import streamlit as st

def load_custom_css():
    """
    Injects custom CSS to style the Streamlit interface, making it feel premium,
    modern, and responsive with smooth transitions and rich visual accents.
    """
    st.markdown(
        """
        <style>
        /* Import Outfit Google Font */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');
        
        /* Apply font and smooth scrolling globally */
        html, body, [class*="css"], .stApp {
            font-family: 'Outfit', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        /* Gradient background for the sidebar */
        [data-testid="stSidebar"] {
            background-image: linear-gradient(180deg, #f0f7f7 0%, #e2eff1 100%);
            border-right: 1px solid rgba(0, 0, 0, 0.05);
        }

        /* Sidebar Title styling */
        .sidebar-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: #0d5c75;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .sidebar-subtitle {
            font-size: 0.9rem;
            color: #557a84;
            margin-bottom: 1.5rem;
            line-height: 1.4;
        }

        /* Styled Card component for results and retrieved chunks */
        .custom-card {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 1.25rem;
            box-shadow: 0 4px 12px rgba(13, 92, 117, 0.05);
            border: 1px solid rgba(13, 92, 117, 0.08);
            margin-bottom: 1rem;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .custom-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(13, 92, 117, 0.08);
            border-color: rgba(13, 92, 117, 0.15);
        }

        /* Main app title styling with a beautiful linear gradient */
        .main-title {
            font-weight: 800;
            background: linear-gradient(135deg, #0d5c75 0%, #1995ad 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            text-align: left;
        }

        /* Quick-start questions styling */
        .stButton > button {
            border-radius: 20px;
            border: 1px solid #1995ad;
            color: #1995ad;
            background-color: transparent;
            font-weight: 500;
            transition: all 0.2s ease;
            width: 100%;
            text-align: left;
            padding: 0.4rem 1rem;
            font-size: 0.9rem;
        }

        .stButton > button:hover {
            background-color: #1995ad;
            color: white;
            border-color: #1995ad;
            transform: scale(1.02);
        }

        /* Answer block accent styling */
        .answer-title {
            color: #0d5c75;
            font-weight: 600;
            margin-bottom: 0.5rem;
            font-size: 1.2rem;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        /* Metric styling */
        .metric-badge {
            background-color: #ecf8f8;
            color: #0d5c75;
            padding: 4px 10px;
            border-radius: 12px;
            font-weight: 600;
            font-size: 0.85rem;
            border: 1px solid rgba(13, 92, 117, 0.1);
            display: inline-block;
        }

        /* Helpful helpline cards */
        .resource-card {
            background-color: rgba(25, 149, 173, 0.05);
            border-left: 4px solid #1995ad;
            border-radius: 4px;
            padding: 8px 12px;
            margin-bottom: 8px;
            font-size: 0.85rem;
        }

        .resource-card a {
            color: #0d5c75;
            font-weight: 600;
            text-decoration: none;
        }
        
        .resource-card a:hover {
            text-decoration: underline;
        }

        /* Dark mode overrides for compatibility */
        @media (prefers-color-scheme: dark) {
            [data-testid="stSidebar"] {
                background-image: linear-gradient(180deg, #121820 0%, #0d1218 100%);
                border-right: 1px solid rgba(255, 255, 255, 0.05);
            }
            .sidebar-title {
                color: #55c4d3;
            }
            .sidebar-subtitle {
                color: #8bb1b8;
            }
            .custom-card {
                background-color: #1a222d;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
                border: 1px solid rgba(255, 255, 255, 0.08);
            }
            .custom-card:hover {
                box-shadow: 0 6px 18px rgba(0, 0, 0, 0.3);
                border-color: rgba(85, 196, 211, 0.3);
            }
            .metric-badge {
                background-color: #182830;
                color: #55c4d3;
                border-color: rgba(85, 196, 211, 0.2);
            }
            .resource-card {
                background-color: rgba(85, 196, 211, 0.05);
                border-left-color: #55c4d3;
            }
            .resource-card a {
                color: #55c4d3;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
