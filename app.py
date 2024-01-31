import os
import random
from typing import Sequence

import datasets
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from setfit import SetFitModel

st.set_page_config(
    page_title="mtg-coloridentity-multilabel-classification",
    page_icon="🧙",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None,
)


default_hf_home = os.path.join(os.path.expanduser("~"), ".cache", "huggingface")
HF_HOME = os.environ.get("HF_HOME", default_hf_home)

coloridentity_model = "joshuasundance/mtg-coloridentity-multilabel-classification"

colors = ["B", "G", "R", "U", "W"]
labels = ["black", "green", "red", "blue", "white"]

sns.set()

col1, col2 = st.columns(2)


@st.cache_resource
def get_model(
    model_id: str = coloridentity_model,
    cache_dir: str = HF_HOME,
    **kwargs,
) -> SetFitModel:
    return SetFitModel.from_pretrained(model_id, cache_dir=cache_dir, **kwargs)


@st.cache_data
def get_data(
    repo_id: str = coloridentity_model,
    cache_dir: str = HF_HOME,
    **kwargs,
) -> datasets.Dataset:
    dataset_dict = datasets.load_dataset(repo_id, cache_dir=cache_dir, **kwargs)
    return datasets.concatenate_datasets(
        list(dataset_dict.values()),
    )


def get_random_text() -> str:
    return dataset.select([random.randint(0, len(dataset))])[0]["text"]  # nosec


@st.cache_data
def get_preds(input_text: str) -> Sequence[float]:
    return model.predict_proba(input_text)


def prob_bars(preds: Sequence[float]) -> None:
    _preds = (float(p) for p in preds)
    df = pd.DataFrame(
        zip(labels, _preds),
        columns=["Color", "Probability"],
    )
    plt.figure(figsize=(8, 6))
    ax = sns.barplot(x="Color", y="Probability", data=df, palette=labels)

    # Add data labels on each bar
    for p in ax.patches:
        ax.annotate(
            format(p.get_height(), ".4f"),
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, 9),
            textcoords="offset points",
        )

    plt.title("Prediction Probabilities")
    plt.xlabel("Color")
    plt.ylabel("Probability")
    st.pyplot(plt.gcf())


model = get_model()
dataset = get_data()
default_text = get_random_text()

if "input_text" not in st.session_state:
    st.session_state.input_text = default_text

with col1:
    if st.button("🎲 Roll the Dice"):
        st.session_state.input_text = get_random_text()
    input_text = st.text_area(
        "Card name and text",
        st.session_state.input_text,
        height=400,
    )

preds = get_preds(input_text)

with col2:
    prob_bars(preds)
