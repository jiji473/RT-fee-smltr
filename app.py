import streamlit as st
import matplotlib.pyplot as plt

st.title("Retail Fee Simulator")

brand_investment = st.slider("Brand Investment (€)", 100000, 1000000, 245000, step=10000)
retailer_audience_fee = st.slider("Retailer Audience Fee (%)", 0.0, 0.5, 0.25, step=0.01)
dsp_fee = st.slider("DSP Fee (%)", 0.0, 0.5, 0.13, step=0.01)
criteo_retailer_fee = st.slider("Criteo Retailer Fee (%)", 0.0, 0.5, 0.15, step=0.01)

tac = brand_investment / (1 + retailer_audience_fee + dsp_fee)
audience_fee = tac * retailer_audience_fee
criteo_retailer_revenue_on_fee = audience_fee * criteo_retailer_fee
criteo_retailer_revenue_on_dsp_fee = dsp_fee * tac
retailer_take = audience_fee - criteo_retailer_revenue_on_fee
criteo_margin = criteo_retailer_revenue_on_fee + criteo_retailer_revenue_on_dsp_fee
share = tac / brand_investment * 100

st.markdown(f"**TAC**: {tac:,.0f} €")
st.markdown(f"**Audience Fee**: {audience_fee:,.0f} €")
st.markdown(f"**Criteo Revenue (Audience Fee)**: {criteo_retailer_revenue_on_fee:,.0f} €")
st.markdown(f"**Criteo Revenue (DSP Fee)**: {criteo_retailer_revenue_on_dsp_fee:,.0f} €")
st.markdown(f"**Retailer Take**: {retailer_take:,.0f} €")
st.markdown(f"**Criteo Margin**: {criteo_margin:,.0f} €")
st.markdown(f"**Share of media over spend**: {share:.0f}%")

# Bar Chart
labels = ['TAC', 'Audience Fee', 'Criteo Revenue (Fee)', 'Criteo Revenue (DSP)', 'Retailer Take', 'Criteo Margin']
values = [tac, audience_fee, criteo_retailer_revenue_on_fee, criteo_retailer_revenue_on_dsp_fee, retailer_take, criteo_margin]

fig, ax = plt.subplots()
ax.bar(labels, values)
ax.set_ylabel('€')
ax.set_title('Répartition des revenus')
st.pyplot(fig)
