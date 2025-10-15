from pathlib import Path
import streamlit as st

dir_path = Path(__file__).parent / "pages"

st.set_page_config(
    page_title='Streamlit Samples',
    layout='wide',
    initial_sidebar_state='expanded',
)

def run() -> None:
    page = st.navigation(
        {
            "Pages": [
                st.Page(
                    dir_path / "basic_elements.py",
                    title="Basic Elements",
                    icon=":material/waving_hand:"
                ),
                st.Page(
                    dir_path / "data_elements.py",
                    title="Data Elements",
                    icon=":material/table:",
                ),
                st.Page(
                    dir_path / "status_elements.py",
                    title="Status Elements",
                    icon=":material/warning:",
                ),
                st.Page(
                    dir_path / "media_elements.py",
                    title="Media Elements",
                    icon=":material/stock_media:",
                ),
                st.Page(
                    dir_path / "layouts.py",
                    title="Layouts",
                    icon=":material/mobile_layout:",
                ),
                st.Page(
                    dir_path / "input_elements.py",
                    title="Input Elements",
                    icon=":material/input:",
                ),
                st.Page(
                    dir_path / "form.py",
                    title="Sample Form",
                    icon=":material/dynamic_form:",
                ),
                st.Page(
                    dir_path / "data_viz.py",
                    title="Data Visualization",
                    icon=":material/area_chart:",
                ),
                st.Page(
                    dir_path / "data_viz_integrations.py",
                    title="Data Visualization Integrations",
                    icon=":material/bubble_chart:",
                ),
                st.Page(
                    dir_path / "chat_elements.py",
                    title="Chat Elements",
                    icon=":material/chat:",
                ),
            ]
        }
    )
    page.run()


if __name__ == "__main__":
    run()