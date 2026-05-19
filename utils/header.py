import streamlit as st

def show_header():

    st.markdown(
        """
        <style>

        .hero-container{
            background: linear-gradient(
                135deg,
                #0f172a,
                #1e3a8a
            );

            padding: 50px;

            border-radius: 20px;

            color: white;

            margin-bottom: 30px;
        }

        .hero-title{
            font-size: 50px;
            font-weight: bold;
            margin-bottom: 15px;
        }

        .hero-subtitle{
            font-size: 22px;
            margin-bottom: 30px;
            opacity: 0.9;
        }

        .hero-box{
            background: rgba(255,255,255,0.1);

            padding: 25px;

            border-radius: 15px;

            font-size: 20px;

            line-height: 2;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-container">

        </div>
        """,
        unsafe_allow_html=True
    )