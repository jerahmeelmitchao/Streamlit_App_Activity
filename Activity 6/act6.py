import cv2
import numpy as np
import streamlit as st

# Function to apply grayscale filter
def apply_filter(frame, intensity):
    # Convert to grayscale and apply intensity
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)  # Convert back to BGR for display

# Snapshot functionality
def save_snapshot(frame):
    snapshot_filename = "snapshot.png"
    cv2.imwrite(snapshot_filename, frame)
    return snapshot_filename

# Set up the Streamlit app
st.title("Real-Time Webcam Video Capture")

# Set up webcam capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    st.error("Unable to access the webcam.")
else:
    # Sliders for filter control
    intensity_slider = st.slider("Filter Intensity", 0, 100, 50)

    # Display an image for snapshots
    snapshot = None

    # Start video stream
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture frame.")
            break
        
        # Apply filter
        frame = apply_filter(frame, intensity_slider)

        # Convert frame for Streamlit
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Show the current frame in Streamlit
        st.image(frame_rgb, channels="RGB", use_column_width=True)

        # Snapshot button
        if st.button("Take Snapshot"):
            snapshot_filename = save_snapshot(frame)
            snapshot = cv2.imread(snapshot_filename)
            st.image(snapshot, caption="Snapshot", channels="RGB", use_column_width=True)

        # Optionally, break out of the loop after some time (for demonstration)
        if st.button("Stop Video"):
            break

    # Release the capture object and close windows
    cap.release()

