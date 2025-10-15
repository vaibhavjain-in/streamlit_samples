import streamlit as st


st.title('This page is talking about some basic elements of streamlit')
st.header('You will see some examples of basic elements.')
st.subheader('Elements like title, header, subheader, text, markdown etc.')
st.text('This is some text. Text elements are used to display plain text in your Streamlit app. You can use text elements to provide information, instructions, or any other textual content to your users.')
st.divider()

st.write('Hello, world!')


st.markdown("""
# Streamlit Overview

Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.

## Key Features

- **Easy UI Creation**: Build interactive web apps with simple Python scripts.
- **Widgets**: Use sliders, buttons, and input boxes for user interaction.
- **Live Updates**: Automatically update app content as code or data changes.
- **Data Visualization**: Integrate with libraries like Matplotlib, Plotly, and Altair.
- **Media Support**: Display images, audio, and video files.
- **Layout Control**: Organize content with columns, tabs, and expanders.
- **Deployment**: Share apps easily via Streamlit Cloud or other platforms.

### How to Get Started

1. Install Streamlit using pip.
2. Write your Python script with Streamlit components.
3. Run your app with the `streamlit run` command.

#### Example

```python
import streamlit as st
st.write("Hello, Streamlit!")
```

Streamlit is ideal for rapid prototyping and sharing data-driven applications with minimal effort.
""")

st.code('''import streamlit as st
st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")''')
st.caption('This is a caption for the code example above.')
st.divider()
st.latex(r'''
a^2 + b^2 = c^2
''')
