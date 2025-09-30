import pandas as pd
from sqlalchemy import text
from src.db.data_base import engine
from dash import html, dcc  
import dash_bootstrap_components as dbc
import plotly.express as px

with engine.begin() as con:
    revenue_df = pd.read_sql(text("""
        SELECT
            d.year, d.month,
            SUM(foi.quantity * (foi.unit_price * (1 - foi.discount_pct/100.0))) AS revenue
        FROM dbo.fact_order fo
        JOIN dbo.dim_date d ON d.date_id = fo.order_date
        JOIN dbo.fact_order_item foi ON foi.order_id = fo.order_id
        WHERE fo.status = 'Completed'
        GROUP BY d.year, d.month
        ORDER BY d.year, d.month
    """), con)

    top_products_df = pd.read_sql(text("""
        SELECT TOP 15 p.product_name,
               SUM(foi.quantity) AS units,
               SUM(foi.quantity * (foi.unit_price * (1 - foi.discount_pct/100.0))) AS revenue
        FROM dbo.fact_order_item foi
        JOIN dbo.fact_order fo ON fo.order_id = foi.order_id AND fo.status = 'Completed'
        JOIN dbo.dim_product p ON p.product_id = foi.product_id
        GROUP BY p.product_name
        ORDER BY revenue DESC
    """), con)

    sales_country_df = pd.read_sql(text("""
        SELECT g.country_iso3, g.country_name,
               SUM(foi.quantity * (foi.unit_price * (1 - foi.discount_pct/100.0))) AS revenue
        FROM dbo.fact_order fo
        JOIN dbo.dim_store s   ON s.store_id = fo.store_id
        JOIN dbo.dim_geography g ON g.country_iso3 = s.country_iso3
        JOIN dbo.fact_order_item foi ON foi.order_id = fo.order_id
        WHERE fo.status = 'Completed'
        GROUP BY g.country_iso3, g.country_name
    """), con)


    def layout():
        revenue_df["year_month"] = revenue_df["year"].astype(str) + "-" + revenue_df["month"].astype(str).str.zfill(2)
        fig1 = px.line(revenue_df, x="year_month", y="revenue", title="Ingresos mensuales")
        fig1.update_layout(xaxis_title="Periodo", yaxis_title="Ingresos")

        return dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H1("Dashboard", className="text-center mt-4"),
                    html.Hr(),
                ], width=12)
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(figure=fig1)
                ], width=12)
            ])
        ])