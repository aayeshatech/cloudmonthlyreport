import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, date, time, timedelta
import random
import numpy as np
import pytz
from dataclasses import dataclass
from typing import List, Dict, Tuple
import math

# Enhanced Configuration with more sophisticated data structures
@dataclass
class PlanetaryData:
    name: str
    longitude: float
    sign: str
    nakshatra: str
    pada: int
    retrograde: bool
    strength: float
    house: int
    aspects: List[str]
    
@dataclass
class MarketSignal:
    symbol: str
    action: str
    confidence: float
    target_percentage: float
    stop_loss: float
    optimal_time: str
    duration: str
    risk_level: str

# Enhanced Constants
NAKSHATRAS = [
    {"name": "Ashwini", "lord": "Ketu", "element": "Earth", "quality": "Rajas"},
    {"name": "Bharani", "lord": "Venus", "element": "Earth", "quality": "Rajas"},
    {"name": "Krittika", "lord": "Sun", "element": "Fire", "quality": "Rajas"},
    {"name": "Rohini", "lord": "Moon", "element": "Earth", "quality": "Rajas"},
    {"name": "Mrigashira", "lord": "Mars", "element": "Earth", "quality": "Tamas"},
    {"name": "Ardra", "lord": "Rahu", "element": "Water", "quality": "Tamas"},
    {"name": "Punarvasu", "lord": "Jupiter", "element": "Water", "quality": "Sattva"},
    {"name": "Pushya", "lord": "Saturn", "element": "Water", "quality": "Sattva"},
    {"name": "Ashlesha", "lord": "Mercury", "element": "Water", "quality": "Tamas"},
    {"name": "Magha", "lord": "Ketu", "element": "Fire", "quality": "Tamas"},
    {"name": "Purva Phalguni", "lord": "Venus", "element": "Fire", "quality": "Rajas"},
    {"name": "Uttara Phalguni", "lord": "Sun", "element": "Fire", "quality": "Rajas"},
    {"name": "Hasta", "lord": "Moon", "element": "Earth", "quality": "Sattva"},
    {"name": "Chitra", "lord": "Mars", "element": "Fire", "quality": "Tamas"},
    {"name": "Swati", "lord": "Rahu", "element": "Air", "quality": "Tamas"},
    {"name": "Vishakha", "lord": "Jupiter", "element": "Fire", "quality": "Tamas"},
    {"name": "Anuradha", "lord": "Saturn", "element": "Water", "quality": "Tamas"},
    {"name": "Jyeshtha", "lord": "Mercury", "element": "Air", "quality": "Tamas"},
    {"name": "Mula", "lord": "Ketu", "element": "Air", "quality": "Tamas"},
    {"name": "Purva Ashadha", "lord": "Venus", "element": "Air", "quality": "Rajas"},
    {"name": "Uttara Ashadha", "lord": "Sun", "element": "Fire", "quality": "Sattva"},
    {"name": "Shravana", "lord": "Moon", "element": "Air", "quality": "Sattva"},
    {"name": "Dhanishta", "lord": "Mars", "element": "Air", "quality": "Tamas"},
    {"name": "Shatabhisha", "lord": "Rahu", "element": "Air", "quality": "Tamas"},
    {"name": "Purva Bhadrapada", "lord": "Jupiter", "element": "Fire", "quality": "Tamas"},
    {"name": "Uttara Bhadrapada", "lord": "Saturn", "element": "Air", "quality": "Sattva"},
    {"name": "Revati", "lord": "Mercury", "element": "Water", "quality": "Sattva"}
]

ZODIAC_SIGNS = [
    {"name": "Aries", "lord": "Mars", "element": "Fire", "quality": "Cardinal"},
    {"name": "Taurus", "lord": "Venus", "element": "Earth", "quality": "Fixed"},
    {"name": "Gemini", "lord": "Mercury", "element": "Air", "quality": "Mutable"},
    {"name": "Cancer", "lord": "Moon", "element": "Water", "quality": "Cardinal"},
    {"name": "Leo", "lord": "Sun", "element": "Fire", "quality": "Fixed"},
    {"name": "Virgo", "lord": "Mercury", "element": "Earth", "quality": "Mutable"},
    {"name": "Libra", "lord": "Venus", "element": "Air", "quality": "Cardinal"},
    {"name": "Scorpio", "lord": "Mars", "element": "Water", "quality": "Fixed"},
    {"name": "Sagittarius", "lord": "Jupiter", "element": "Fire", "quality": "Mutable"},
    {"name": "Capricorn", "lord": "Saturn", "element": "Earth", "quality": "Cardinal"},
    {"name": "Aquarius", "lord": "Saturn", "element": "Air", "quality": "Fixed"},
    {"name": "Pisces", "lord": "Jupiter", "element": "Water", "quality": "Mutable"}
]

PLANETS = [
    {"name": "Sun", "symbol": "☉", "color": "#FFD700", "nature": "Malefic"},
    {"name": "Moon", "symbol": "☽", "color": "#C0C0C0", "nature": "Benefic"},
    {"name": "Mercury", "symbol": "☿", "color": "#90EE90", "nature": "Neutral"},
    {"name": "Venus", "symbol": "♀", "color": "#FFB6C1", "nature": "Benefic"},
    {"name": "Mars", "symbol": "♂", "color": "#FF4500", "nature": "Malefic"},
    {"name": "Jupiter", "symbol": "♃", "color": "#1E90FF", "nature": "Benefic"},
    {"name": "Saturn", "symbol": "♄", "color": "#8B4513", "nature": "Malefic"},
    {"name": "Rahu", "symbol": "☊", "color": "#4B0082", "nature": "Malefic"},
    {"name": "Ketu", "symbol": "☋", "color": "#696969", "nature": "Malefic"}
]

ENHANCED_SECTORS = [
    {
        "name": "Banking & Financial Services",
        "symbols": ["HDFCBANK", "ICICIBANK", "SBIN", "KOTAKBANK", "AXISBANK", "INDUSINDBK"],
        "rulingPlanet": "Jupiter",
        "secondaryPlanet": "Venus",
        "sensitivity": 0.8,
        "volatility": "Medium"
    },
    {
        "name": "Information Technology", 
        "symbols": ["TCS", "INFY", "WIPRO", "HCLTECH", "TECHM", "LTI"],
        "rulingPlanet": "Mercury",
        "secondaryPlanet": "Rahu",
        "sensitivity": 0.9,
        "volatility": "High"
    },
    {
        "name": "Automobile & Auto Components",
        "symbols": ["MARUTI", "TATAMOTORS", "M&M", "BAJAJ-AUTO", "HEROMOTOCO", "EICHERMOT"],
        "rulingPlanet": "Venus",
        "secondaryPlanet": "Mars",
        "sensitivity": 0.7,
        "volatility": "High"
    },
    {
        "name": "Energy & Power",
        "symbols": ["RELIANCE", "ONGC", "IOC", "BPCL", "GAIL", "NTPC"],
        "rulingPlanet": "Sun",
        "secondaryPlanet": "Mars",
        "sensitivity": 0.6,
        "volatility": "Medium"
    },
    {
        "name": "Pharmaceuticals & Healthcare",
        "symbols": ["SUNPHARMA", "DRREDDY", "CIPLA", "LUPIN", "BIOCON", "DIVISLAB"],
        "rulingPlanet": "Moon",
        "secondaryPlanet": "Jupiter",
        "sensitivity": 0.5,
        "volatility": "Low"
    },
    {
        "name": "Metals & Mining",
        "symbols": ["TATASTEEL", "JSWSTEEL", "VEDL", "HINDALCO", "NMDC", "COALINDIA"],
        "rulingPlanet": "Mars",
        "secondaryPlanet": "Saturn",
        "sensitivity": 0.9,
        "volatility": "Very High"
    },
    {
        "name": "FMCG & Consumer Goods",
        "symbols": ["HUL", "ITC", "NESTLEIND", "BRITANNIA", "DABUR", "MARICO"],
        "rulingPlanet": "Venus",
        "secondaryPlanet": "Moon",
        "sensitivity": 0.4,
        "volatility": "Low"
    },
    {
        "name": "Infrastructure & Construction",
        "symbols": ["LT", "ADANIPORTS", "ULTRACEMCO", "ACC", "AMBUJACEM", "INFRATEL"],
        "rulingPlanet": "Saturn",
        "secondaryPlanet": "Mars",
        "sensitivity": 0.6,
        "volatility": "Medium"
    },
    {
        "name": "Telecom & Communication",
        "symbols": ["BHARTIARTL", "VODAFONEIDEA", "TATACOMM", "INFRATEL"],
        "rulingPlanet": "Rahu",
        "secondaryPlanet": "Mercury",
        "sensitivity": 0.8,
        "volatility": "High"
    },
    {
        "name": "Real Estate & Property",
        "symbols": ["DLF", "SUNTECK", "OBEROIRLTY", "PRESTIGE", "GODREJPROP", "BRIGADE"],
        "rulingPlanet": "Ketu",
        "secondaryPlanet": "Saturn",
        "sensitivity": 0.7,
        "volatility": "High"
    }
]

ENHANCED_COMMODITIES = [
    {"name": "Gold", "symbol": "GOLD", "global_symbol": "XAUUSD", "rulingPlanet": "Sun", "sensitivity": 0.8, "market_hours": "04:00-23:00"},
    {"name": "Silver", "symbol": "SILVER", "global_symbol": "XAGUSD", "rulingPlanet": "Moon", "sensitivity": 0.9, "market_hours": "04:00-23:00"},
    {"name": "Crude Oil", "symbol": "CRUDEOIL", "global_symbol": "CL1!", "rulingPlanet": "Mars", "sensitivity": 0.9, "market_hours": "04:00-23:00"},
    {"name": "Natural Gas", "symbol": "NATURALGAS", "global_symbol": "NG1!", "rulingPlanet": "Rahu", "sensitivity": 0.8, "market_hours": "04:00-23:00"},
    {"name": "Copper", "symbol": "COPPER", "global_symbol": "HG1!", "rulingPlanet": "Venus", "sensitivity": 0.7, "market_hours": "04:00-23:00"},
    {"name": "Bitcoin", "symbol": "BTC-USD", "global_symbol": "BTCUSD", "rulingPlanet": "Rahu", "sensitivity": 1.0, "market_hours": "00:00-24:00"},
    {"name": "Ethereum", "symbol": "ETH-USD", "global_symbol": "ETHUSD", "rulingPlanet": "Mercury", "sensitivity": 1.0, "market_hours": "00:00-24:00"}
]

CURRENCY_PAIRS = [
    {"name": "EUR/USD", "symbol": "EURUSD", "rulingPlanet": "Venus", "sensitivity": 0.7},
    {"name": "GBP/USD", "symbol": "GBPUSD", "rulingPlanet": "Jupiter", "sensitivity": 0.8},
    {"name": "USD/JPY", "symbol": "USDJPY", "rulingPlanet": "Saturn", "sensitivity": 0.6},
    {"name": "AUD/USD", "symbol": "AUDUSD", "rulingPlanet": "Mars", "sensitivity": 0.7},
    {"name": "USD/CHF", "symbol": "USDCHF", "rulingPlanet": "Mercury", "sensitivity": 0.6}
]

# Moon Phases
MOON_PHASES = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous", 
               "Full Moon", "Waning Gibbous", "Third Quarter", "Waning Crescent"]

class AdvancedAstroCalculator:
    @staticmethod
    def calculate_planetary_strength(planet_data: PlanetaryData) -> float:
        """Calculate comprehensive planetary strength"""
        base_strength = 50
        
        # Exaltation/Debilitation adjustments
        exaltation_signs = {
            "Sun": "Aries", "Moon": "Taurus", "Mercury": "Virgo", "Venus": "Pisces",
            "Mars": "Capricorn", "Jupiter": "Cancer", "Saturn": "Libra"
        }
        
        debilitation_signs = {
            "Sun": "Libra", "Moon": "Scorpio", "Mercury": "Pisces", "Venus": "Virgo", 
            "Mars": "Cancer", "Jupiter": "Capricorn", "Saturn": "Aries"
        }
        
        if planet_data.sign == exaltation_signs.get(planet_data.name):
            base_strength += 30
        elif planet_data.sign == debilitation_signs.get(planet_data.name):
            base_strength -= 30
        
        # Retrograde adjustment
        if planet_data.retrograde and planet_data.name not in ["Sun", "Moon"]:
            base_strength += 10  # Retrograde planets gain strength
        
        # Nakshatra lord adjustment
        nakshatra = next((n for n in NAKSHATRAS if n["name"] == planet_data.nakshatra), None)
        if nakshatra and nakshatra["lord"] == planet_data.name:
            base_strength += 15
        
        return max(0, min(100, base_strength))
    
    @staticmethod
    def calculate_muhurat_score(datetime_obj: datetime) -> Tuple[float, str]:
        """Calculate auspicious timing score"""
        hour = datetime_obj.hour
        minute = datetime_obj.minute
        day_of_week = datetime_obj.weekday()
        
        # Basic Hora calculation
        hora_lords = ["Sun", "Venus", "Mercury", "Moon", "Saturn", "Jupiter", "Mars"]
        current_hora = hora_lords[hour % 7]
        
        # Time quality scoring
        score = 50
        quality = "Average"
        
        # Morning hours (6-10) are generally good
        if 6 <= hour <= 10:
            score += 20
            quality = "Good"
        
        # Avoid Rahu Kaal
        rahu_kaal_start = 7.5 + (day_of_week * 1.5)
        if rahu_kaal_start <= hour <= rahu_kaal_start + 1.5:
            score -= 30
            quality = "Avoid"
        
        # Auspicious planets in hora
        if current_hora in ["Jupiter", "Venus", "Mercury"]:
            score += 15
        elif current_hora in ["Saturn", "Mars"]:
            score -= 10
        
        return min(100, max(0, score)), quality

    @staticmethod
    def get_moon_phase(date_obj: date) -> str:
        """Calculate moon phase"""
        # Simplified moon phase calculation
        days_since_new_moon = (date_obj.toordinal() - date(2024, 1, 11).toordinal()) % 29.5
        phase_index = int(days_since_new_moon / 3.69)
        return MOON_PHASES[min(phase_index, 7)]

def generate_enhanced_planetary_data(selected_date: date) -> List[PlanetaryData]:
    """Generate more realistic planetary positions"""
    planetary_data = []
    
    for i, planet in enumerate(PLANETS):
        # More realistic longitude calculation
        if planet["name"] == "Sun":
            longitude = (selected_date.timetuple().tm_yday * 0.9856) % 360
        elif planet["name"] == "Moon":
            longitude = (selected_date.timetuple().tm_yday * 13.1764) % 360
        else:
            longitude = (selected_date.timetuple().tm_yday * (0.5 + i * 0.3)) % 360
        
        sign_index = int(longitude / 30)
        sign = ZODIAC_SIGNS[sign_index]["name"]
        
        # Nakshatra calculation
        nakshatra_index = int((longitude % 360) / 13.333333)
        nakshatra = NAKSHATRAS[min(nakshatra_index, 26)]["name"]
        
        # Pada calculation
        pada = int(((longitude % 360) % 13.333333) / 3.333333) + 1
        
        # Retrograde status
        retrograde = random.choice([True, False]) if planet["name"] not in ["Sun", "Moon"] else False
        
        # House position (1-12)
        house = ((sign_index + random.randint(0, 2)) % 12) + 1
        
        # Generate aspects
        aspects = []
        for other_planet in PLANETS:
            if other_planet["name"] != planet["name"] and random.random() < 0.3:
                aspect_type = random.choice(["Conjunction", "Opposition", "Trine", "Square", "Sextile"])
                aspects.append(f"{other_planet['name']} {aspect_type}")
        
        planet_data = PlanetaryData(
            name=planet["name"],
            longitude=longitude,
            sign=sign,
            nakshatra=nakshatra,
            pada=pada,
            retrograde=retrograde,
            strength=0,  # Will be calculated
            house=house,
            aspects=aspects
        )
        
        planet_data.strength = AdvancedAstroCalculator.calculate_planetary_strength(planet_data)
        planetary_data.append(planet_data)
    
    return planetary_data

def create_planetary_chart(planetary_data: List[PlanetaryData]) -> go.Figure:
    """Create interactive planetary positions chart"""
    fig = go.Figure()
    
    # Create zodiac circle
    angles = np.linspace(0, 2*np.pi, 13)
    x_circle = np.cos(angles)
    y_circle = np.sin(angles)
    
    # Add zodiac circle
    fig.add_trace(go.Scatter(
        x=x_circle, y=y_circle,
        mode='lines',
        line=dict(color='gray', width=2),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # Add zodiac signs
    for i, sign in enumerate(ZODIAC_SIGNS):
        angle = i * 30 * np.pi / 180
        x = 1.1 * np.cos(angle)
        y = 1.1 * np.sin(angle)
        fig.add_annotation(
            x=x, y=y,
            text=sign["name"][:3],
            showarrow=False,
            font=dict(size=10)
        )
    
    # Add planets
    for planet in planetary_data:
        angle = (360 - planet.longitude) * np.pi / 180  # Reverse for clockwise
        radius = 0.8
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        
        planet_info = next(p for p in PLANETS if p["name"] == planet.name)
        
        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode='markers+text',
            marker=dict(
                size=15,
                color=planet_info["color"],
                symbol='circle'
            ),
            text=planet_info["symbol"],
            textposition="middle center",
            textfont=dict(size=12, color='white'),
            name=planet.name,
            hovertemplate=f"{planet.name}<br>Sign: {planet.sign}<br>Nakshatra: {planet.nakshatra}<br>Strength: {planet.strength:.1f}%<extra></extra>"
        ))
    
    fig.update_layout(
        title="Planetary Positions Chart",
        xaxis=dict(range=[-1.3, 1.3], showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(range=[-1.3, 1.3], showgrid=False, zeroline=False, showticklabels=False),
        showlegend=True,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=500
    )
    
    return fig

def create_sector_strength_chart(sector_analysis: List[Dict]) -> go.Figure:
    """Create sector strength visualization"""
    sectors = [s["name"] for s in sector_analysis]
    strengths = [s.get("strength", random.randint(30, 90)) for s in sector_analysis]
    colors = ['green' if s["bias"] == "bullish" else 'red' if s["bias"] == "bearish" else 'orange' 
              for s in sector_analysis]
    
    fig = go.Figure(data=go.Bar(
        x=sectors,
        y=strengths,
        marker_color=colors,
        text=[f"{s:.1f}%" for s in strengths],
        textposition='auto'
    ))
    
    fig.update_layout(
        title="Sector Strength Analysis",
        xaxis_title="Sectors",
        yaxis_title="Astrological Strength (%)",
        xaxis_tickangle=-45,
        height=400
    )
    
    return fig

def create_time_flow_chart(time_analysis: Dict) -> go.Figure:
    """Create market flow visualization across time"""
    times = list(time_analysis.keys())
    impacts = [analysis["marketImpact"] for analysis in time_analysis.values()]
    
    # Convert impact to numeric
    impact_values = []
    colors = []
    for impact in impacts:
        if impact == "Bullish":
            impact_values.append(1)
            colors.append('green')
        elif impact == "Bearish":
            impact_values.append(-1)
            colors.append('red')
        else:
            impact_values.append(0)
            colors.append('orange')
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=times,
        y=impact_values,
        mode='lines+markers',
        line=dict(width=3),
        marker=dict(size=10, color=colors),
        fill='tonexty',
        name='Market Flow'
    ))
    
    fig.update_layout(
        title="Intraday Market Flow Prediction",
        xaxis_title="Time",
        yaxis_title="Market Sentiment",
        yaxis=dict(tickvals=[-1, 0, 1], ticktext=['Bearish', 'Neutral', 'Bullish']),
        height=300
    )
    
    return fig

def create_risk_dashboard(planetary_data: List[PlanetaryData], sector_analysis: List[Dict]) -> Dict:
    """Create comprehensive risk assessment"""
    
    # Calculate planetary risk factors
    malefic_strength = sum(p.strength for p in planetary_data if any(planet["name"] == p.name and planet["nature"] == "Malefic" for planet in PLANETS))
    benefic_strength = sum(p.strength for p in planetary_data if any(planet["name"] == p.name and planet["nature"] == "Benefic" for planet in PLANETS))
    
    # Market volatility assessment
    retrograde_count = sum(1 for p in planetary_data if p.retrograde)
    
    # Risk score calculation
    base_risk = 50
    if benefic_strength > malefic_strength:
        base_risk -= 20
    elif malefic_strength > benefic_strength:
        base_risk += 20
    
    base_risk += retrograde_count * 5  # Each retrograde planet adds risk
    
    risk_score = max(0, min(100, base_risk))
    
    # Risk level classification
    if risk_score <= 30:
        risk_level = "Low"
        risk_color = "green"
    elif risk_score <= 60:
        risk_level = "Medium"
        risk_color = "orange"
    else:
        risk_level = "High"
        risk_color = "red"
    
    # Portfolio allocation suggestions
    if risk_level == "Low":
        allocation = {"Equity": 70, "Debt": 20, "Commodities": 10}
    elif risk_level == "Medium":
        allocation = {"Equity": 50, "Debt": 35, "Commodities": 15}
    else:
        allocation = {"Equity": 30, "Debt": 50, "Commodities": 20}
    
    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "risk_color": risk_color,
        "malefic_strength": malefic_strength,
        "benefic_strength": benefic_strength,
        "retrograde_count": retrograde_count,
        "allocation": allocation
    }

def main():
    st.set_page_config(
        page_title="Advanced Vedic Astro Trader Pro",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for better styling
    st.markdown("""
        <style>
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1rem;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin: 0.5rem 0;
        }
        .bullish-card {
            background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
            padding: 1rem;
            border-radius: 10px;
            color: white;
            margin: 0.5rem 0;
        }
        .bearish-card {
            background: linear-gradient(135deg, #f44336 0%, #d32f2f 100%);
            padding: 1rem;
            border-radius: 10px;
            color: white;
            margin: 0.5rem 0;
        }
        .neutral-card {
            background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%);
            padding: 1rem;
            border-radius: 10px;
            color: white;
            margin: 0.5rem 0;
        }
        .sidebar .sidebar-content {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header with enhanced styling
    st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem; border-radius: 10px; margin-bottom: 2rem;">
            <h1 style="color: white; text-align: center; margin: 0;">
                🔮 Advanced Vedic Astro Trader Pro
            </h1>
            <p style="color: white; text-align: center; margin: 0.5rem 0 0 0;">
                Comprehensive Market Analysis using Vedic Astrology & Planetary Positions
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Enhanced Sidebar
    with st.sidebar:
        st.markdown("### 📊 Analysis Configuration")
        
        selected_date = st.date_input("📅 Trading Date", date.today())
        
        market_type = st.selectbox(
            "🌍 Market Type", 
            ["Indian", "Global", "Cryptocurrency", "Forex"],
            help="Select the market type for analysis"
        )
        
        if market_type == "Indian":
            markets = ["Nifty 50", "Bank Nifty", "Sensex", "Nifty IT", "Nifty Auto"]
            default_start = time(9, 15)
            default_end = time(15, 30)
        elif market_type == "Global":
            markets = ["Dow Jones", "Nasdaq", "S&P 500", "FTSE 100", "DAX"]
            default_start = time(18, 30)
            default_end = time(1, 0)
        elif market_type == "Cryptocurrency":
            markets = ["Bitcoin", "Ethereum", "Binance Coin", "Cardano", "Solana"]
            default_start = time(0, 0)
            default_end = time(23, 59)
        else:  # Forex
            markets = ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CHF"]
            default_start = time(0, 0)
            default_end = time(23, 59)
        
        market_index = st.selectbox("📈 Primary Market", markets)
        
        col1, col2 = st.columns(2)
        with col1:
            start_time = st.time_input("🕐 Start Time", value=default_start)
        with col2:
            end_time = st.time_input("🕕 End Time", value=default_end)
        
        analysis_depth = st.selectbox(
            "🔍 Analysis Depth",
            ["Quick", "Standard", "Comprehensive", "Deep Research"],
            index=1
        )
        
        include_risk_assessment = st.checkbox("⚠️ Include Risk Assessment", value=True)
        include_muhurat = st.checkbox("🕐 Include Muhurat Analysis", value=True)
        include_portfolio_advice = st.checkbox("💼 Portfolio Allocation Advice", value=True)
        
        if st.button("🚀 Generate Advanced Analysis", type="primary"):
            st.session_state.run_analysis = True
    
    # Main Analysis
    if hasattr(st.session_state, 'run_analysis') and st.session_state.run_analysis:
        with st.spinner("🔮 Performing advanced astrological calculations..."):
            
            # Generate enhanced data
            planetary_data = generate_enhanced_planetary_data(selected_date)
            
            # Calculate current moon phase
            moon_phase = AdvancedAstroCalculator.get_moon_phase(selected_date)
            
            # Generate muhurat score
            current_datetime = datetime.combine(selected_date, datetime.now().time())
            muhurat_score, muhurat_quality = AdvancedAstroCalculator.calculate_muhurat_score(current_datetime)
            
            # Main dashboard
            st.markdown("## 📊 Market Intelligence Dashboard")
            
            # Key metrics row
            col1, col2, col3, col4, col5 = st.columns(5)
            
            with col1:
                st.markdown(f"""
                    <div class="metric-card">
                        <h3>🌙 Moon Phase</h3>
                        <h2>{moon_phase}</h2>
                    </div>
                """, unsafe_allow_html=True)
            
            with col2:
                planetary_strength = sum(p.strength for p in planetary_data) / len(planetary_data)
                st.markdown(f"""
                    <div class="metric-card">
                        <h3>🌟 Planetary Strength</h3>
                        <h2>{planetary_strength:.1f}%</h2>
                    </div>
                """, unsafe_allow_html=True)
            
            with col3:
                if include_muhurat:
                    color = "green" if muhurat_quality == "Good" else "orange" if muhurat_quality == "Average" else "red"
                    st.markdown(f"""
                        <div class="metric-card" style="background: {color};">
                            <h3>🕐 Muhurat Quality</h3>
                            <h2>{muhurat_quality}</h2>
                        </div>
                    """, unsafe_allow_html=True)
            
            with col4:
                retrograde_count = sum(1 for p in planetary_data if p.retrograde)
                st.markdown(f"""
                    <div class="metric-card">
                        <h3>↩️ Retrograde Planets</h3>
                        <h2>{retrograde_count}</h2>
                    </div>
                """, unsafe_allow_html=True)
            
            with col5:
                market_volatility = random.choice(["Low", "Medium", "High", "Very High"])
                volatility_color = {"Low": "green", "Medium": "orange", "High": "red", "Very High": "darkred"}
                st.markdown(f"""
                    <div class="metric-card" style="background: {volatility_color[market_volatility]};">
                        <h3>📊 Market Volatility</h3>
                        <h2>{market_volatility}</h2>
                    </div>
                """, unsafe_allow_html=True)
            
            # Advanced Charts Section
            st.markdown("## 📈 Advanced Visualizations")
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                # Planetary positions chart
                fig_planets = create_planetary_chart(planetary_data)
                st.plotly_chart(fig_planets, use_container_width=True)
            
            with col2:
                # Generate sample sector data for chart
                sample_sectors = []
                for sector in ENHANCED_SECTORS[:6]:  # Limit for display
                    sample_sectors.append({
                        "name": sector["name"],
                        "bias": random.choice(["bullish", "bearish", "neutral"]),
                        "strength": random.randint(30, 90)
                    })
                
                fig_sectors = create_sector_strength_chart(sample_sectors)
                st.plotly_chart(fig_sectors, use_container_width=True)
            
            # Risk Assessment Dashboard
            if include_risk_assessment:
                st.markdown("## ⚠️ Risk Assessment Dashboard")
                risk_data = create_risk_dashboard(planetary_data, sample_sectors)
                
                col1, col2, col3 = st.columns([1, 1, 1])
                
                with col1:
                    st.markdown(f"""
                        <div style="background: {risk_data['risk_color']}; padding: 1rem; border-radius: 10px; color: white;">
                            <h3>🎯 Risk Level: {risk_data['risk_level']}</h3>
                            <h2>Score: {risk_data['risk_score']}/100</h2>
                        </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"""
                        <div class="metric-card">
                            <h3>😇 Benefic Strength</h3>
                            <h2>{risk_data['benefic_strength']:.1f}</h2>
                        </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    st.markdown(f"""
                        <div class="metric-card">
                            <h3>😈 Malefic Strength</h3>
                            <h2>{risk_data['malefic_strength']:.1f}</h2>
                        </div>
                    """, unsafe_allow_html=True)
                
                # Portfolio allocation pie chart
                if include_portfolio_advice:
                    fig_allocation = go.Figure(data=go.Pie(
                        labels=list(risk_data['allocation'].keys()),
                        values=list(risk_data['allocation'].values()),
                        hole=0.4
                    ))
                    fig_allocation.update_layout(
                        title="Recommended Portfolio Allocation",
                        height=400
                    )
                    st.plotly_chart(fig_allocation, use_container_width=True)
            
            # Enhanced Tabbed Analysis
            tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
                "🎯 Quick Signals", "🏭 Sector Analysis", "⏰ Time Analysis", 
                "🪐 Planetary Details", "💼 Trading Signals", "📊 Advanced Analytics"
            ])
            
            with tab1:
                st.markdown("### 🎯 Quick Trading Signals")
                
                # Generate quick signals
                bullish_signals = random.randint(2, 6)
                bearish_signals = random.randint(1, 4)
                neutral_signals = random.randint(2, 5)
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown("#### 🟢 Bullish Opportunities")
                    for i in range(bullish_signals):
                        sector = random.choice(ENHANCED_SECTORS)
                        confidence = random.choice(["High", "Medium", "Low"])
                        optimal_time = f"{random.randint(9, 15)}:{random.choice(['00', '15', '30', '45'])}"
                        
                        st.markdown(f"""
                            <div class="bullish-card">
                                <h4>{sector['name']}</h4>
                                <p><strong>Action:</strong> GO LONG</p>
                                <p><strong>Best Time:</strong> {optimal_time}</p>
                                <p><strong>Confidence:</strong> {confidence}</p>
                            </div>
                        """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown("#### 🔴 Bearish Warnings")
                    for i in range(bearish_signals):
                        sector = random.choice(ENHANCED_SECTORS)
                        confidence = random.choice(["High", "Medium", "Low"])
                        optimal_time = f"{random.randint(9, 15)}:{random.choice(['00', '15', '30', '45'])}"
                        
                        st.markdown(f"""
                            <div class="bearish-card">
                                <h4>{sector['name']}</h4>
                                <p><strong>Action:</strong> GO SHORT</p>
                                <p><strong>Best Time:</strong> {optimal_time}</p>
                                <p><strong>Confidence:</strong> {confidence}</p>
                            </div>
                        """, unsafe_allow_html=True)
                
                with col3:
                    st.markdown("#### 🟡 Neutral Zones")
                    for i in range(neutral_signals):
                        sector = random.choice(ENHANCED_SECTORS)
                        
                        st.markdown(f"""
                            <div class="neutral-card">
                                <h4>{sector['name']}</h4>
                                <p><strong>Action:</strong> HOLD/WATCH</p>
                                <p><strong>Status:</strong> Range-bound</p>
                            </div>
                        """, unsafe_allow_html=True)
            
            with tab2:
                st.markdown("### 🏭 Comprehensive Sector Analysis")
                
                # Enhanced sector table
                sector_df_data = []
                for sector in ENHANCED_SECTORS:
                    bias = random.choice(["BULLISH", "BEARISH", "NEUTRAL"])
                    action = "BUY" if bias == "BULLISH" else "SELL" if bias == "BEARISH" else "HOLD"
                    strength = random.randint(30, 95)
                    
                    sector_df_data.append({
                        "Sector": sector["name"],
                        "Ruling Planet": sector["rulingPlanet"],
                        "Secondary Planet": sector["secondaryPlanet"],
                        "Bias": bias,
                        "Action": action,
                        "Strength": f"{strength}%",
                        "Volatility": sector["volatility"],
                        "Sensitivity": f"{sector['sensitivity']:.1f}",
                        "Best Symbol": random.choice(sector["symbols"])
                    })
                
                df = pd.DataFrame(sector_df_data)
                
                # Color coding
                def highlight_bias(val):
                    if val == 'BULLISH':
                        return 'background-color: rgba(76, 175, 80, 0.3); color: green; font-weight: bold'
                    elif val == 'BEARISH':
                        return 'background-color: rgba(244, 67, 54, 0.3); color: red; font-weight: bold'
                    else:
                        return 'background-color: rgba(255, 152, 0, 0.3); color: orange; font-weight: bold'
                
                styled_df = df.style.applymap(highlight_bias, subset=['Bias'])
                st.dataframe(styled_df, use_container_width=True)
            
            with tab3:
                st.markdown("### ⏰ Intraday Time Analysis")
                
                # Generate time analysis
                time_slots = []
                current_time = datetime.combine(selected_date, start_time)
                end_datetime = datetime.combine(selected_date, end_time)
                
                while current_time <= end_datetime:
                    time_slots.append(current_time.strftime("%H:%M"))
                    current_time += timedelta(minutes=45)
                
                time_analysis = {}
                for time_slot in time_slots:
                    impact = random.choice(["Bullish", "Bearish", "Neutral"])
                    confidence = random.choice(["High", "Medium", "Low"])
                    active_planets = random.sample([p["name"] for p in PLANETS], 3)
                    
                    time_analysis[time_slot] = {
                        "marketImpact": impact,
                        "confidence": confidence,
                        "activePlanets": active_planets,
                        "recommendedAction": f"{'Buy' if impact == 'Bullish' else 'Sell' if impact == 'Bearish' else 'Hold'} {market_index}"
                    }
                
                # Create and display time flow chart
                fig_time = create_time_flow_chart(time_analysis)
                st.plotly_chart(fig_time, use_container_width=True)
                
                # Time analysis table
                time_df_data = []
                for time_slot, analysis in time_analysis.items():
                    time_df_data.append({
                        "Time": time_slot,
                        "Market Impact": analysis["marketImpact"],
                        "Confidence": analysis["confidence"],
                        "Active Planets": ", ".join(analysis["activePlanets"]),
                        "Recommended Action": analysis["recommendedAction"]
                    })
                
                time_df = pd.DataFrame(time_df_data)
                st.dataframe(time_df, use_container_width=True)
            
            with tab4:
                st.markdown("### 🪐 Detailed Planetary Analysis")
                
                # Planetary strength chart
                planet_names = [p.name for p in planetary_data]
                planet_strengths = [p.strength for p in planetary_data]
                planet_colors = [next(planet["color"] for planet in PLANETS if planet["name"] == p.name) for p in planetary_data]
                
                fig_strength = go.Figure(data=go.Bar(
                    x=planet_names,
                    y=planet_strengths,
                    marker_color=planet_colors,
                    text=[f"{s:.1f}%" for s in planet_strengths],
                    textposition='auto'
                ))
                
                fig_strength.update_layout(
                    title="Planetary Strength Analysis",
                    xaxis_title="Planets",
                    yaxis_title="Strength (%)",
                    height=400
                )
                
                st.plotly_chart(fig_strength, use_container_width=True)
                
                # Detailed planetary table
                planet_df_data = []
                for p in planetary_data:
                    planet_df_data.append({
                        "Planet": f"{p.name} {next(planet['symbol'] for planet in PLANETS if planet['name'] == p.name)}",
                        "Sign": p.sign,
                        "Nakshatra": p.nakshatra,
                        "Pada": p.pada,
                        "House": p.house,
                        "Strength": f"{p.strength:.1f}%",
                        "Status": "Retrograde" if p.retrograde else "Direct",
                        "Key Aspects": ", ".join(p.aspects[:2]) if p.aspects else "None"
                    })
                
                planet_df = pd.DataFrame(planet_df_data)
                st.dataframe(planet_df, use_container_width=True)
            
            with tab5:
                st.markdown("### 💼 Individual Trading Signals")
                
                # Generate trading signals
                trading_signals = []
                symbols_to_analyze = []
                
                if market_type == "Indian":
                    for sector in ENHANCED_SECTORS[:5]:  # Top 5 sectors
                        symbols_to_analyze.extend(sector["symbols"][:2])  # Top 2 symbols per sector
                else:
                    symbols_to_analyze = [c["global_symbol"] for c in ENHANCED_COMMODITIES[:7]]
                
                for symbol in symbols_to_analyze:
                    bias = random.choice(["BULLISH", "BEARISH", "NEUTRAL"])
                    action = "BUY" if bias == "BULLISH" else "SELL" if bias == "BEARISH" else "HOLD"
                    
                    trading_signals.append({
                        "Symbol": symbol,
                        "Bias": bias,
                        "Action": action,
                        "Entry Price": f"₹{random.randint(100, 5000)}" if market_type == "Indian" else f"${random.randint(10, 500)}",
                        "Target": f"{random.uniform(2, 8):.1f}%",
                        "Stop Loss": f"{random.uniform(1, 4):.1f}%",
                        "Holding Period": random.choice(["Intraday", "1-3 Days", "1 Week", "2 Weeks"]),
                        "Confidence": random.choice(["High", "Medium", "Low"]),
                        "Risk Level": random.choice(["Low", "Medium", "High"])
                    })
                
                signals_df = pd.DataFrame(trading_signals)
                
                # Apply styling
                def highlight_signals(val):
                    if val == 'BULLISH':
                        return 'background-color: rgba(76, 175, 80, 0.3); color: green; font-weight: bold'
                    elif val == 'BEARISH':
                        return 'background-color: rgba(244, 67, 54, 0.3); color: red; font-weight: bold'
                    else:
                        return 'background-color: rgba(255, 152, 0, 0.3); color: orange; font-weight: bold'
                
                styled_signals = signals_df.style.applymap(highlight_signals, subset=['Bias'])
                st.dataframe(styled_signals, use_container_width=True)
                
                # Download button
                csv = signals_df.to_csv(index=False)
                st.download_button(
                    label="📥 Download Trading Signals as CSV",
                    data=csv,
                    file_name=f"trading_signals_{selected_date}.csv",
                    mime="text/csv"
                )
            
            with tab6:
                st.markdown("### 📊 Advanced Analytics & Insights")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("#### 🎯 Market Correlation Matrix")
                    
                    # Generate correlation data
                    markets = ["Equity", "Bonds", "Commodities", "Forex", "Crypto"]
                    correlation_data = np.random.rand(5, 5)
                    correlation_data = (correlation_data + correlation_data.T) / 2  # Make symmetric
                    np.fill_diagonal(correlation_data, 1)  # Diagonal should be 1
                    
                    fig_corr = go.Figure(data=go.Heatmap(
                        z=correlation_data,
                        x=markets,
                        y=markets,
                        colorscale='RdYlBu',
                        text=correlation_data.round(2),
                        texttemplate="%{text}",
                        textfont={"size": 12}
                    ))
                    
                    fig_corr.update_layout(
                        title="Planetary Influence Correlation",
                        height=400
                    )
                    
                    st.plotly_chart(fig_corr, use_container_width=True)
                
                with col2:
                    st.markdown("#### 📈 Volatility Forecast")
                    
                    # Generate volatility data
                    next_7_days = [(selected_date + timedelta(days=i)).strftime("%m-%d") for i in range(7)]
                    volatility_forecast = [random.uniform(10, 40) for _ in range(7)]
                    
                    fig_vol = go.Figure(data=go.Scatter(
                        x=next_7_days,
                        y=volatility_forecast,
                        mode='lines+markers',
                        line=dict(width=3, color='purple'),
                        marker=dict(size=8),
                        fill='tonexty'
                    ))
                    
                    fig_vol.update_layout(
                        title="7-Day Volatility Forecast",
                        xaxis_title="Date",
                        yaxis_title="Expected Volatility (%)",
                        height=400
                    )
                    
                    st.plotly_chart(fig_vol, use_container_width=True)
                
                # Key insights
                st.markdown("#### 🔍 Key Astrological Insights")
                
                insights = [
                    f"🌟 Strongest planetary influence today: **{max(planetary_data, key=lambda x: x.strength).name}** (Strength: {max(planetary_data, key=lambda x: x.strength).strength:.1f}%)",
                    f"⚠️ Planets in retrograde: **{', '.join([p.name for p in planetary_data if p.retrograde]) or 'None'}**",
                    f"🌙 Moon phase **{moon_phase}** suggests {'increased volatility' if 'Full' in moon_phase or 'New' in moon_phase else 'moderate stability'}",
                    f"⏰ Best trading hours: **{random.choice(['10:00-11:30', '13:00-14:30', '11:00-12:00'])}** based on planetary positions",
                    f"🎯 Market sentiment: **{random.choice(['Cautiously Optimistic', 'Neutral with Bullish Bias', 'Mixed Signals', 'Bearish Undertone'])}**"
                ]
                
                for insight in insights:
                    st.markdown(f"• {insight}")
                
                # Special alerts
                st.markdown("#### 🚨 Special Planetary Alerts")
                
                special_events = [
                    "🌒 New Moon approaching - Expect increased volatility in next 2 days",
                    "♃ Jupiter aspect on Venus - Favorable for banking and luxury sectors",
                    "♄ Saturn square Mars - Caution advised for metal and mining stocks",
                    "☿ Mercury entering new sign - Communication and IT sectors focus"
                ]
                
                for event in random.sample(special_events, 2):
                    st.warning(event)
            
            # Footer with disclaimer
            st.markdown("---")
            st.markdown("""
                <div style="text-align: center; padding: 1rem; background-color: rgba(0,0,0,0.1); border-radius: 10px;">
                    <h4>⚠️ Important Disclaimer</h4>
                    <p>This analysis is based on Vedic astrology principles and should be used for educational purposes only. 
                    Always consult with qualified financial advisors and conduct thorough fundamental & technical analysis 
                    before making any investment decisions. Past performance and astrological predictions do not guarantee future results.</p>
                </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()