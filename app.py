import streamlit as st

st.set_page_config(
    page_title="Geomathematics & Geostatistics – core class",
    layout="wide",
)

# --- HEADER / LOGOS ---------------------------------------------------------

col1, col2, col3 = st.columns([1.2, 2, 1.2])

with col1:
    st.image(
        "https://u-szeged.hu/site/design3/img/szte_logo_en.jpg",
        caption="University of Szeged",
        width=140,
    )

with col3:
    st.image(
        "https://geosci.u-szeged.hu/site/upload/2024/10/logo_v2_2_64x55.png",
        caption="Geosciences",
        width=80,
    )

with col2:
    st.markdown(
        """
        <div style="text-align: center; padding-top: 0.5rem;">
            <h1>Geomathematics &amp; Geostatistics</h1>
            <h3 style="margin-top: 0.25rem;">
                Department of Atmospheric and Geospatial Data Science
            </h3>
            <p style="font-style: italic; margin-top: 0.5rem;">
                app.py – Geomathematics &amp; Geostatistics core class<br>
                by <strong>Hawkar Ali Abdulhaq</strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# --- MAIN CONTENT -----------------------------------------------------------

st.subheader("Core Python class")

st.markdown(
    """
```python
class GeomathematicsGeostatistics:
    pass
```
"""
)
