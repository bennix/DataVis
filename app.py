import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="数据可视化应用", layout="wide")

st.title("数据可视化应用")

uploaded_file = st.file_uploader("上传 CSV 或 JSON 文件", type=["csv", "json"])
if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_json(uploaded_file)
    st.subheader("数据预览")
    st.write(df.head())

    all_columns = df.columns.tolist()
    x_column = st.selectbox("选择 X 轴字段", all_columns)
    y_column = st.selectbox("选择 Y 轴字段", all_columns, index=1 if len(all_columns) > 1 else 0)

    chart_type = st.selectbox(
        "选择图表类型",
        ("折线图", "柱状图", "散点图", "直方图", "饼图")
    )

    fig = None
    if chart_type == "折线图":
        fig = px.line(df, x=x_column, y=y_column)
    elif chart_type == "柱状图":
        fig = px.bar(df, x=x_column, y=y_column)
    elif chart_type == "散点图":
        fig = px.scatter(df, x=x_column, y=y_column)
    elif chart_type == "直方图":
        fig = px.histogram(df, x=x_column)
    elif chart_type == "饼图":
        fig = px.pie(df, names=x_column, values=y_column)

    if fig is not None:
        fig.update_layout(font=dict(family="SimHei"))
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("简单统计分析")
    st.write(df.describe(include='all').T)
