import streamlit as st

def show_cards():

    st.markdown(
        """
        <style>

        .card-container{
            display: flex;
            gap: 20px;
            margin-top: 20px;
            margin-bottom: 30px;
        }

        .card{

            flex: 1;

            background: linear-gradient(
                135deg,
                #2563eb,
                #1e40af
            );

            padding: 30px;

            border-radius: 20px;

            color: white;

            text-align: center;

            transition: 0.3s;
        }

        .card:hover{
            transform: scale(1.05);
        }

        .card-title{
            font-size: 22px;
            margin-bottom: 10px;
        }

        .card-value{
            font-size: 40px;
            font-weight: bold;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        </div>
        """,
        unsafe_allow_html=True
    )