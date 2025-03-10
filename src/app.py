import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime
import pandas as pd
import time
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Intersections Interface", page_icon=":traffic_light:", layout="wide", initial_sidebar_state="expanded")


with st.sidebar:
    st.title("SMART INDIA HACKATHON 2024")
    selected = option_menu(
        "Main Menu", 
        ["RT Camera Feed", "Simulated Model Demo","Featured Models","Model Statistics","Traffic Analytics", "Database"], 
        icons=["camera-video", "robot", "star", "bar-chart", "gear", "database"], 
        menu_icon="cast", 
        default_index=0,
    )
    st.subheader("A project by Team SLASH 6")
    st.subheader("Students of Easwari Engineering College")
    
    st.image(r"E:\SIH-2024\src\assets\logo.png")
    
if selected == "RT Camera Feed":
    st.title("SMART INTERSECTIONS")
    st.subheader("Real-Time Traffic Flow Optimization with AI-Driven Adaptive Signal Systems")
    st.header("Real-Time Camera Feed Streaming")
    location = st.selectbox("Select the Junction / Intersection", 
                            ("Anna Nagar Metro Junction",
                             "Vadapalani Junction", 
                             "Ashok Pillar Junction",
                             "Madipakkam Lake Junction",
                             "Kottur Intersection",),)

    st.success("Location Description: " + location)
    st.success("Location ID: TN-CHN-W11-JN15")

    col1, col2 = st.columns(2)
    
    with col1:
        st.write("---------------------------------------------------")
        st.write("Signal ID: W11-JN15-SGNL1")
        st.video(r"https://youtu.be/Beu5OdUDCDo",autoplay=True)

        st.write("---------------------------------------------------")
        st.write("Signal ID: W11-JN15-SGNL2")
        st.video(r"https://youtu.be/GTr5BjpFW5I",autoplay=True)
    
    with col2:
        st.write("---------------------------------------------------")
        st.write("Signal ID: W11-JN15-SGNL3")
        st.video(r"https://youtu.be/8SNx3F_Gk34",autoplay=True)
        
        st.write("---------------------------------------------------")
        st.write("Signal ID: W11-JN15-SGNL4")
        st.video(r"https://youtu.be/sy31Cubcnn8",autoplay=True)

elif selected == "Simulated Model Demo":
    st.title("Simulated Demo Environment")
    st.subheader("Our solution also incorporates a master control - fail safe mechanism.")
    st.image(r"E:\SIH-2024\src\assets\simulated_demo.png")
    st.text("NOTE: This is just a simulated demo of the interface in which the working of the model will be demonstrated.")
    st.text("Features such as traffic signals, signal timing counter are will be added for the final demonstration.")
    st.video("https://youtu.be/MugHld4YzsA",autoplay=True)


elif selected == "Featured Models":
    st.title("EXCLUSIVE MODEL FEATURES")
    
    st.header("Emergency Vehicle Detection")
    col1,col2 = st.columns(2)
    with col1:
        st.image(r"E:\SIH-2024\src\assets\emergency_vehicle_detection_1.png")
    with col2:
        st.image(r"E:\SIH-2024\src\assets\emergency_vehicle_detection_2.png")
    st.header("Accident Detection")
    col1,col2 = st.columns(2)
    with col1:
        st.image(r"E:\SIH-2024\src\assets\accident_detection_1.png")
    with col2:
        st.image(r"E:\SIH-2024\src\assets\accident_detection_2.jpeg")
    st.header("Stop Line Crossing Violation Detection")
    col1,col2 = st.columns(2)
    with col1:
        st.image(r"E:\SIH-2024\src\assets\stop_line_crossing_1.png")
    with col2:
        st.image(r"E:\SIH-2024\src\assets\stop_line_crossing_2.png")


elif selected == "Model Statistics":
    st.title("Model Performace Analysis")
    st.subheader("Emergency Vehicle Detection Model")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Training Performance Analysis")
        st.image(r"E:\SIH-2024\src\assets\EVD model\train_loss.png")
    with col2:
        st.write("Model Validation Analysis")
        st.image(r"E:\SIH-2024\src\assets\EVD model\val_loss.png")
    
    st.subheader("Traffic Flow Intensity Model")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Training Performance Analysis")
        st.image(r"E:\SIH-2024\src\assets\TFIM model\train_loss.png")
    with col2:
        st.write("Model Validation Analysis")
        st.image(r"E:\SIH-2024\src\assets\TFIM model\val_loss.png")        
    

# Page 3: Analytics
elif selected == "Traffic Analytics":
    st.title("Traffic Data Analytics")
    st.subheader("Real-Time Traffic Analysis and Model Insights")
    
    # Create placeholders for key metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Total Vehicles Detected", value="1,250", delta="+50")
    with col2:
        st.metric(label="Average Speed (km/h)", value="45", delta="0 km/h")
    with col3:
        st.metric(label="Current Traffic Density", value="Medium", delta="Low")
    
    # Display a line chart showing vehicle counts over time
    st.subheader("Vehicle Counts Over Time")
    time_series_data = {
        "Timestamp": pd.date_range(start="2024-08-27 08:00:00", periods=10, freq="5T"),
        "Vehicle Count": [100, 120, 150, 200, 180, 170, 160, 190, 210, 220]
    }
    df_time_series = pd.DataFrame(time_series_data)
    
    st.line_chart(df_time_series.set_index("Timestamp"))
    
    # Display a bar chart for vehicle type distribution
    st.subheader("Vehicle Type Distribution")
    vehicle_distribution = {
        "Vehicle Type": ["Car", "Bus", "Two-Wheeler", "Heavy-Vehicle", "Auto-Rickshaw"],
        "Counts": [600, 50, 300, 70, 280]
    }
    df_distribution = pd.DataFrame(vehicle_distribution)
    
    fig, ax = plt.subplots()
    ax.bar(df_distribution["Vehicle Type"], df_distribution["Counts"], color="skyblue")
    ax.set_ylabel("Counts")
    ax.set_title("Vehicle Type Distribution")
    
    st.pyplot(fig)
    
    # Placeholder for future model insights
    st.subheader("Model Insights")
    st.write("Insights derived from these analytics can be used to understand patterns in traffic with respect to vehicle counts, timing of congestion etc.")
    st.write("These insights can then be verified and then added to heuristic data for improved model performance.")

elif selected == "Database":
    st.title("Traffic Analytics Database")
    junction = st.selectbox("Select the Junction / Intersection", 
                                ("Anna Nagar Metro Junction",
                                 "Vadapalani Junction", 
                                 "Ashok Pillar Junction",
                                 "Madipakkam Lake Junction",
                                 "Kottur Intersection",),)
    st.header("Database for " + junction)
    traffic_density_data = {
    "Timestamp": [
        "2024-08-28 08:10:45", 
        "2024-08-28 08:10:50", 
        "2024-08-28 08:10:55",
        "2024-08-28 08:11:00",
        "2024-08-28 08:11:05",
        "2024-08-28 08:11:10",
        "2024-08-28 08:11:15",
        "2024-08-28 08:11:20",
        "2024-08-28 08:11:25",
        "2024-08-28 08:11:30"
    ],
    "Signal_ID": [
        "W11-JN15-SGNL3",
        "W11-JN15-SGNL1",
        "W11-JN15-SGNL3",
        "W11-JN15-SGNL4",
        "W11-JN15-SGNL2",
        "W11-JN15-SGNL1",
        "W11-JN15-SGNL3",
        "W11-JN15-SGNL2",
        "W11-JN15-SGNL1",
        "W11-JN15-SGNL2"
    ],
    "Detection Counts (car|two-wheeler|bus|heavy-vehicle|auto-rickshaw)": [
        "12|28|2|1|3", 
        "6|54|4|2|7", 
        "4|14|1|0|4",
        "12|28|2|1|11",
        "2|28|2|0|2",
        "26|28|2|1|8",
        "8|37|2|1|12",
        "12|21|1|0|9",
        "12|34|4|1|3",
        "12|17|2|3|4",
        ] 
    }
    signal_data_1 = {
    "Camera_ID": [1, 2, 3, 4, 5, 6, 7],
    "Timestamp": [
        "2024-08-27 08:05:00", 
        "2024-08-27 08:20:00", 
        "2024-08-27 08:35:00", 
        "2024-08-27 08:50:00", 
        "2024-08-27 09:05:00", 
        "2024-08-27 09:20:00", 
        "2024-08-27 09:35:00"
    ],
    "Signal_Status": [
        "Green", 
        "Red", 
        "Yellow", 
        "Green", 
        "Red", 
        "Green", 
        "Red"
        ],
    "Duration": [45, 60, 10, 50, 55, 40, 60]
    }

    signal_data_2 = {
        "Signal_ID": [8, 9, 10, 11, 12, 13, 14],
        "Camera_ID": [8, 9, 10, 11, 12, 13, 14],
        "Timestamp": [
            "2024-08-27 08:10:00", 
            "2024-08-27 08:25:00", 
            "2024-08-27 08:40:00", 
            "2024-08-27 08:55:00", 
            "2024-08-27 09:10:00", 
            "2024-08-27 09:25:00", 
            "2024-08-27 09:40:00"
        ],
        "Signal_Status": [
            "Yellow", 
            "Green", 
            "Red", 
            "Yellow", 
            "Green", 
            "Red", 
            "Green"
        ],
        "Duration": [30, 55, 15, 25, 50, 35, 45]
    }

    camera_data = {
    "Camera_ID": [1, 2, 3, 4],
    "Location": [
        "East End to Metro Road", 
        "South to Santhome Church Road", 
        "Bangalore Highway ", 
        "Towards Besant Nagar Housing", 
    ],
    "Lane_Count": [3,2, 3, 3],
    "Installation_Date": [
        "2024-07-15", 
        "2024-06-20", 
        "2024-08-01", 
        "2024-07-30", 
        ],
    "Status": ["Active", "Active", "Inactive", "Active"]
    }

    if junction == "Vadapalani Junction":
        st.subheader("Camera Status and Details")
        st.table(camera_data)
        
        st.subheader("Signal Response Data")
        col1,col2 = st.columns(2)
        with col1:
            st.text("Signal ID: W11-JN15-SGNL1")
            st.table(signal_data_1)
        with col2:
            st.text("Signal ID: W11-JN15-SGNL2")
            st.table(signal_data_2)
            
        col1,col2 = st.columns(2)
        with col1:
            st.text("Signal ID: W11-JN15-SGNL3")
            st.table(signal_data_1)
        with col2:
            st.text("Signal ID: W11-JN15-SGNL4")
            st.table(signal_data_2)

        st.subheader("Real Time Model Detection Logging")
        st.table(traffic_density_data)

        
    
        