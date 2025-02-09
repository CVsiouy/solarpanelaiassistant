import streamlit as st
import plotly.graph_objs as go

st.title("Solar Insights 😎")
    
# 1. Cost & ROI Analysis
st.subheader("Cost & ROI Analysis 👌")
investment = st.number_input("Enter total investment cost ($)", value=10000)
annual_savings = st.number_input("Enter annual savings from solar ($)", value=1500)
years = st.number_input("Years of operation", value=10)

if st.button("Calculate ROI"):
    total_savings = annual_savings * years
    roi = ((total_savings - investment) / investment) * 100
    st.write(f"**Total Savings over {years} years:** ${total_savings}")
    st.write(f"**ROI:** {roi:.2f}%")

st.markdown("---")

# 2. Market Trends
st.subheader("Market Trends 📈")
st.write("\n- Solar panel costs have decreased by 70% in the last decade.")
st.write("\n- Adoption of solar energy is growing at 20% annually.")
st.write("\n- New technologies are focusing on higher efficiency and storage solutions.")

if 'show_graph' not in st.session_state:
    st.session_state.show_graph = False

# Function to toggle the graph display
def toggle_graph():
    st.session_state.show_graph = not st.session_state.show_graph

market_data = {
"year": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
"cost": [100, 90, 80, 70, 60, 50, 40, 35, 30, 25, 20],
"adoption": [5, 10, 15, 25, 35, 50, 65, 75, 85, 90, 95]
}


# Toggle button
if st.button("Close Graph" if st.session_state.show_graph else "Show Market Trends Graph", on_click=toggle_graph):
    pass  # Button click handled by toggle_graph

# Display graph if toggle is True
if st.session_state.show_graph:
    fig = go.Figure()

    # Cost Line
    fig.add_trace(go.Scatter(
        x=market_data["year"],
        y=market_data["cost"],
        mode='lines+markers',
        name='Cost ($/Watt)',
        line=dict(color='purple')
    ))

    # Adoption Line
    fig.add_trace(go.Scatter(
        x=market_data["year"],
        y=market_data["adoption"],
        mode='lines+markers',
        name='Adoption (%)',
        line=dict(color='green')
    ))

    fig.update_layout(
        title="Cost Reduction and Adoption Growth Over the Years",
        xaxis_title="Year",
        yaxis_title="Value",
        legend_title="Metrics",
        width=700,
        height=400
    )

    st.plotly_chart(fig)

st.markdown("---") # horizantal divider for sections

# 3. Industry Regulations & Maintenance
st.subheader("Regulations & Maintenance 🚧")
st.write("**Industry Regulations:**")
st.write("\n- Follow local building codes and obtain necessary permits.")
st.write("\n- Compliance with renewable energy incentives and subsidies.")

st.write("\n**Maintenance Requirements:**")
st.write("\n- Clean panels every 6 months.")
st.write("\n- Check inverter performance regularly.")
st.write("\n- Inspect for shading issues and wiring damages.")

