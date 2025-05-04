import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.title("🌤️ Weather Dashboard with Open-Meteo API")
st.write("Get forecast for any city around the world.")

# Location input
city = st.text_input("Enter city name (e.g., Tokyo, New York, Manila):", "Manila")

# Map city to coordinates (for demo simplicity, we hardcode a few cities)
city_coords = {
    "Manila": (14.5995, 120.9842),
    "Tokyo": (35.6895, 139.6917),
    "New York": (40.7128, -74.0060),
    "London": (51.5074, -0.1278),
    "Paris": (48.8566, 2.3522)
}

if city not in city_coords:
    st.warning("City not recognized in this demo. Try Manila, Tokyo, New York, London, or Paris.")
else:
    lat, lon = city_coords[city]
    api_url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
        "&hourly=temperature_2m,precipitation,weathercode,windspeed_10m"
        "&daily=temperature_2m_max,temperature_2m_min"
        "&timezone=auto"
    )

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Parse hourly data
        hourly_df = pd.DataFrame(data['hourly'])
        hourly_df['time'] = pd.to_datetime(hourly_df['time'])

        # Show raw data
        with st.expander("Show Raw Forecast Data"):
            st.dataframe(hourly_df.head(24))

        st.header("📈 Temperature (Next 24 Hours)")
        st.line_chart(hourly_df.set_index('time')['temperature_2m'].head(24))

        st.header("🌧️ Precipitation Forecast (Bar Chart)")
        st.bar_chart(hourly_df.set_index('time')['precipitation'].head(24))

        st.header("💨 Wind Speed Forecast (Area Chart)")
        st.area_chart(hourly_df.set_index('time')['windspeed_10m'].head(24))

        # Weather condition frequency (weathercode)
        weather_counts = hourly_df['weathercode'].head(24).value_counts()
        st.header("☁️ Weather Condition Frequency (Pie Chart)")
        fig, ax = plt.subplots()
        ax.pie(weather_counts, labels=weather_counts.index, autopct='%1.1f%%')
        ax.axis('equal')
        st.pyplot(fig)

        st.header("📋 Full Forecast Table (Next 24 Hours)")
        st.dataframe(hourly_df.head(24))

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
