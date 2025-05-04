                                        Activity 1: 
![Screenshot 2025-05-04 221609](https://github.com/user-attachments/assets/78fb8510-0785-4453-aae5-b813c3ae23b3)

To create the solution, I started by installing Streamlit and setting up a basic app structure using `st.title`, `st.header`, and `st.write` to display text. 
I added user input fields like `st.text_input` and `st.number_input` to collect data,
then displayed real-time output based on the input to make the app interactive and dynamic.

                                        Activity 2
![Screenshot 2025-05-04 221522](https://github.com/user-attachments/assets/db61e07b-f122-4b51-acb5-392f8c2ae630)

To accomplish this task, I used `st.file_uploader` to allow users to upload a CSV file, then loaded it using Pandas for easy manipulation.
I displayed the data with `st.dataframe`, added a `st.checkbox` to optionally view raw data, and used `st.selectbox` to enable filtering based on a specific column.
This setup provided an interactive and user-friendly way to explore datasets with at least five columns.

                                      Activity 3
![Screenshot 2025-05-04 221341](https://github.com/user-attachments/assets/0f2f80bb-6dbf-48ef-b766-18e4263c6923)
![Screenshot 2025-05-04 221429](https://github.com/user-attachments/assets/72cf2f9d-da12-4368-85b5-f7662e7790a8)
![Screenshot 2025-05-04 221413](https://github.com/user-attachments/assets/10a4d274-6d28-4cde-860f-52bfd47bbb11)
![Screenshot 2025-05-04 221400](https://github.com/user-attachments/assets/823f162d-d3f5-4f13-a04a-2592f7901b22)

To solve this problem, I structured the Streamlit app using `st.sidebar` for filters and user options, which allowed for a cleaner and more interactive layout.
I used `st.columns` and `st.expander` to organize and toggle detailed content about Data Warehousing and Enterprise Data Management, ensuring the information was both well-structured and accessible.
This approach helped present complex topics in a more user-friendly and visually organized way.

                                      Activity 4
![Screenshot 2025-05-04 221232](https://github.com/user-attachments/assets/270ae5dd-3ced-461e-875f-06d5362d4907)
![Screenshot 2025-05-04 221215](https://github.com/user-attachments/assets/5c5df79e-6879-45fc-9c9c-9e29771d3088)
![Screenshot 2025-05-04 221200](https://github.com/user-attachments/assets/805614b9-f7b9-41b6-9533-fb8ff57ea195)
![Screenshot 2025-05-04 221143](https://github.com/user-attachments/assets/1c35da17-1994-4c69-9893-bb1779ad18f0)
![Screenshot 2025-05-04 221128](https://github.com/user-attachments/assets/6418e104-5763-46b6-a2f9-9f59b34d3078)
![Screenshot 2025-05-04 221111](https://github.com/user-attachments/assets/0b93c52d-a4df-4974-bf82-105208c10912)

To solve the problem, I decided to use the Meteo Weather API because it provides accessible and detailed weather data in JSON format. 
I used the requests library to fetch this data and parsed it to extract relevant metrics such as temperature, humidity, and wind speed. 
With Streamlit, I displayed the results using widgets and created five different chart types to visually represent the weather trends and comparisons.

                                      Activity 5
![Screenshot 2025-05-04 220919](https://github.com/user-attachments/assets/602ff16c-75e9-4cc9-a283-faca93fb3642)
![Screenshot 2025-05-04 220900](https://github.com/user-attachments/assets/65239ae3-07ef-40ee-bcd1-03f76ac96e0d)

To accomplish the task, I used SQLAlchemy to establish a connection between Streamlit and the MySQL database, allowing secure and efficient data interaction.
I wrote SQL queries to fetch and filter records, displayed the results using st.dataframe, and used Streamlit forms to insert new rows.
For added functionality, I implemented a basic user authentication system to control access to database operations.

                                    Activity 6
![Screenshot 2025-05-04 222100](https://github.com/user-attachments/assets/3ca2c1f7-cd02-44f7-96f9-ac6396ba57df)

To solve the objective, I utilized OpenCV's cv2.VideoCapture to access the webcam and continuously read video frames in real-time.
I integrated Streamlit sliders to control filter thresholds dynamically (such as GrayScale), and used st.image to display processed frames. 
Additionally, I added a snapshot feature to capture and save the current frame on demand.




