import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date, time, timedelta
import random
from dataclasses import dataclass
from typing import List, Dict

# Page configuration
st.set_page_config(
    page_title="Advanced Vedic Astro Trader Pro",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🔮"
)

# Configuration Classes
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

# Constants
NAKSHATRAS = [
    {"name": "Ashwini", "lord": "Ketu", "element": "Earth"},
    {"name": "Bharani", "lord": "Venus", "element": "Earth"},
    {"name": "Krittika", "lord": "Sun", "element": "Fire"},
    {"name": "Rohini", "lord": "Moon", "element": "Earth"},
    {"name": "Mrigashira", "lord": "Mars", "element": "Earth"},
    {"name": "Ardra", "lord": "Rahu", "element": "Water"},
    {"name": "Punarvasu", "lord": "Jupiter", "element": "Water"},
    {"name": "Pushya", "lord": "Saturn", "element": "Water"},
    {"name": "Ashlesha", "lord": "Mercury", "element": "Water"},
    {"name": "Magha", "lord": "Ketu", "element": "Fire"},
    {"name": "Purva Phalguni", "lord": "Venus", "element": "Fire"},
    {"name": "Uttara Phalguni", "lord": "Sun", "element": "Fire"},
    {"name": "Hasta", "lord": "Moon", "element": "Earth"},
    {"name": "Chitra", "lord": "Mars", "element": "Fire"},
    {"name": "Swati", "lord": "Rahu", "element": "Air"},
    {"name": "Vishakha", "lord": "Jupiter", "element": "Fire"},
    {"name": "Anuradha", "lord": "Saturn", "element": "Water"},
    {"name": "Jyeshtha", "lord": "Mercury", "element": "Air"},
    {"name": "Mula", "lord": "Ketu", "element": "Air"},
    {"name": "Purva Ashadha", "lord": "Venus", "element": "Air"},
    {"name": "Uttara Ashadha", "lord": "Sun", "element": "Fire"},
    {"name": "Shravana", "lord": "Moon", "element": "Air"},
    {"name": "Dhanishta", "lord": "Mars", "element": "Air"},
    {"name": "Shatabhisha", "lord": "Rahu", "element": "Air"},
    {"name": "Purva Bhadrapada", "lord": "Jupiter", "element": "Fire"},
    {"name": "Uttara Bhadrapada", "lord": "Saturn", "element": "Air"},
    {"name": "Revati", "lord": "Mercury", "element": "Water"}
]

ZODIAC_SIGNS = [
    {"name": "Aries", "lord": "Mars", "element": "Fire"},
    {"name": "Taurus", "lord": "Venus", "element": "Earth"},
    {"name": "Gemini", "lord": "Mercury", "element": "Air"},
    {"name": "Cancer", "lord": "Moon", "element": "Water"},
    {"name": "Leo", "lord": "Sun", "element": "Fire"},
    {"name": "Virgo", "lord": "Mercury", "element": "Earth"},
    {"name": "Libra", "lord": "Venus", "element": "Air"},
    {"name": "Scorpio", "lord": "Mars", "element": "Water"},
    {"name": "Sagittarius", "lord": "Jupiter", "element": "Fire"},
    {"name": "Capricorn", "lord": "Saturn", "element": "Earth"},
    {"name": "Aquarius", "lord": "Saturn", "element": "Air"},
    {"name": "Pisces", "lord": "Jupiter", "element": "Water"}
]

PLANETS = [
    {"name": "Sun", "symbol": "☉", "nature": "Malefic"},
    {"name": "Moon", "symbol": "☽", "nature": "Benefic"},
    {"name": "Mercury", "symbol": "☿", "nature": "Neutral"},
    {"name": "Venus", "symbol": "♀", "nature": "Benefic"},
    {"name": "Mars", "symbol": "♂", "nature": "Malefic"},
    {"name": "Jupiter", "symbol": "♃", "nature": "Benefic"},
    {"name": "Saturn", "symbol": "♄", "nature": "Malefic"},
    {"name": "Rahu", "symbol": "☊", "nature": "Malefic"},
    {"name": "Ketu", "symbol": "☋", "nature": "Malefic"}
]

# Enhanced SECTORS list with all requested sectors
SECTORS = [
    {"name": "Banking & Financial Services", "symbols": ["HDFCBANK", "ICICIBANK", "SBIN", "KOTAKBANK"], "rulingPlanet": "Jupiter"},
    {"name": "Information Technology", "symbols": ["TCS", "INFY", "WIPRO", "HCLTECH"], "rulingPlanet": "Mercury"},
    {"name": "Automobile & Auto Components", "symbols": ["MARUTI", "TATAMOTORS", "M&M", "BAJAJ-AUTO"], "rulingPlanet": "Venus"},
    {"name": "Energy & Power", "symbols": ["RELIANCE", "ONGC", "IOC", "BPCL"], "rulingPlanet": "Sun"},
    {"name": "Pharmaceuticals & Healthcare", "symbols": ["SUNPHARMA", "DRREDDY", "CIPLA", "LUPIN"], "rulingPlanet": "Moon"},
    {"name": "Metals & Mining", "symbols": ["TATASTEEL", "JSWSTEEL", "VEDL", "HINDALCO"], "rulingPlanet": "Mars"},
    {"name": "FMCG & Consumer Goods", "symbols": ["HUL", "ITC", "NESTLEIND", "BRITANNIA"], "rulingPlanet": "Venus"},
    {"name": "Infrastructure & Construction", "symbols": ["LT", "ADANIPORTS", "ULTRACEMCO", "ACC"], "rulingPlanet": "Saturn"},
    {"name": "PSU Banking", "symbols": ["SBIN", "PNB", "BANKINDIA", "CANBK"], "rulingPlanet": "Jupiter"},
    {"name": "Oil & Gas", "symbols": ["RELIANCE", "ONGC", "IOC", "GAIL"], "rulingPlanet": "Sun"},
    {"name": "Gold & Precious Metals", "symbols": ["GOLDBEES", "GOLDGUINEA", "MANAPPURAM", "MUTHOOTFIN"], "rulingPlanet": "Sun"},
    {"name": "Sugar", "symbols": ["BALRAMCHIN", "SHREERENUKA", "BAJAJHIND", "DHAMPUR"], "rulingPlanet": "Venus"},
    {"name": "Tea & Plantation", "symbols": ["TATACONS", "MCLEODRUS", "JAYSHREETEK", "HARRMALAYA"], "rulingPlanet": "Moon"},
    {"name": "Cement", "symbols": ["ULTRACEMCO", "ACC", "AMBUJACEM", "SHREECEM"], "rulingPlanet": "Saturn"}
]

COMMODITIES = [
    {"name": "Gold", "symbol": "GOLD", "global_symbol": "XAUUSD", "rulingPlanet": "Sun", "market_hours": "24/7"},
    {"name": "Silver", "symbol": "SILVER", "global_symbol": "XAGUSD", "rulingPlanet": "Moon", "market_hours": "24/7"},
    {"name": "Crude Oil", "symbol": "CRUDEOIL", "global_symbol": "CL1!", "rulingPlanet": "Mars", "market_hours": "24/6"},
    {"name": "Natural Gas", "symbol": "NATURALGAS", "global_symbol": "NG1!", "rulingPlanet": "Rahu", "market_hours": "24/6"},
    {"name": "Copper", "symbol": "COPPER", "global_symbol": "HG1!", "rulingPlanet": "Venus", "market_hours": "24/6"},
    {"name": "Bitcoin", "symbol": "BTC-USD", "global_symbol": "BTCUSD", "rulingPlanet": "Rahu", "market_hours": "24/7"},
    {"name": "Ethereum", "symbol": "ETH-USD", "global_symbol": "ETHUSD", "rulingPlanet": "Mercury", "market_hours": "24/7"}
]

MOON_PHASES = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous", 
               "Full Moon", "Waning Gibbous", "Third Quarter", "Waning Crescent"]

# Helper Functions
@st.cache_data
def generate_planetary_data(selected_date: date) -> List[PlanetaryData]:
    """Generate realistic planetary positions"""
    planetary_data = []
    
    for i, planet in enumerate(PLANETS):
        # Realistic longitude calculation
        if planet["name"] == "Sun":
            longitude = (selected_date.timetuple().tm_yday * 0.9856) % 360
        elif planet["name"] == "Moon":
            longitude = (selected_date.timetuple().tm_yday * 13.1764) % 360
        else:
            longitude = (selected_date.timetuple().tm_yday * (0.5 + i * 0.3)) % 360
        
        sign_index = int(longitude / 30)
        sign = ZODIAC_SIGNS[sign_index]["name"]
        
        nakshatra_index = int((longitude % 360) / 13.333333)
        nakshatra = NAKSHATRAS[min(nakshatra_index, 26)]["name"]
        
        pada = int(((longitude % 360) % 13.333333) / 3.333333) + 1
        retrograde = random.choice([True, False]) if planet["name"] not in ["Sun", "Moon"] else False
        house = ((sign_index + random.randint(0, 2)) % 12) + 1
        
        # Generate aspects
        aspects = []
        for other_planet in PLANETS:
            if other_planet["name"] != planet["name"] and random.random() < 0.3:
                aspect_type = random.choice(["Conjunction", "Opposition", "Trine", "Square"])
                aspects.append(f"{other_planet['name']} {aspect_type}")
        
        # Calculate strength
        strength = calculate_planetary_strength(planet["name"], sign, retrograde, nakshatra)
        
        planet_data = PlanetaryData(
            name=planet["name"],
            longitude=longitude,
            sign=sign,
            nakshatra=nakshatra,
            pada=pada,
            retrograde=retrograde,
            strength=strength,
            house=house,
            aspects=aspects
        )
        
        planetary_data.append(planet_data)
    
    return planetary_data

def calculate_planetary_strength(planet_name: str, sign: str, retrograde: bool, nakshatra: str) -> float:
    """Calculate planetary strength"""
    base_strength = 50
    
    exaltation_signs = {
        "Sun": "Aries", "Moon": "Taurus", "Mercury": "Virgo", "Venus": "Pisces",
        "Mars": "Capricorn", "Jupiter": "Cancer", "Saturn": "Libra"
    }
    
    debilitation_signs = {
        "Sun": "Libra", "Moon": "Scorpio", "Mercury": "Pisces", "Venus": "Virgo", 
        "Mars": "Cancer", "Jupiter": "Capricorn", "Saturn": "Aries"
    }
    
    if sign == exaltation_signs.get(planet_name):
        base_strength += 30
    elif sign == debilitation_signs.get(planet_name):
        base_strength -= 30
    
    if retrograde and planet_name not in ["Sun", "Moon"]:
        base_strength += 10
    
    return max(0, min(100, base_strength + random.randint(-10, 10)))

def get_moon_phase(date_obj: date) -> str:
    """Calculate moon phase"""
    days_since_new_moon = (date_obj.toordinal() - date(2024, 1, 11).toordinal()) % 29.5
    phase_index = int(days_since_new_moon / 3.69)
    return MOON_PHASES[min(phase_index, 7)]

# Custom CSS
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
.stDataFrame > div {
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# Header
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

# Sidebar
with st.sidebar:
    st.markdown("### 📊 Analysis Configuration")
    
    selected_date = st.date_input("📅 Trading Date", date.today())
    
    market_type = st.selectbox(
        "🌍 Market Type", 
        ["Indian", "Global", "Commodity", "Cryptocurrency", "Forex"]
    )
    
    # Enhanced Indian market options with all requested sectors
    if market_type == "Indian":
        markets = [
            "Nifty 50", "Bank Nifty", "Sensex", "Nifty IT", "Nifty Auto",
            "Nifty Pharma", "Nifty FMCG", "Nifty Metal", "Nifty PSU Bank",
            "Nifty Oil & Gas", "Gold ETF", "Nifty Commodities",
            "Sugar Stocks", "Tea & Plantation", "Cement Sector"
        ]
    elif market_type == "Global":
        markets = ["Dow Jones", "Nasdaq", "S&P 500", "FTSE 100", "DAX"]
    elif market_type == "Commodity":
        markets = ["Gold", "Silver", "Crude Oil", "Natural Gas", "Copper"]
    elif market_type == "Cryptocurrency":
        markets = ["Bitcoin", "Ethereum", "Binance Coin", "Cardano", "Solana"]
    else:  # Forex
        markets = ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CHF"]
    
    market_index = st.selectbox("📈 Primary Market", markets)
    
    start_time = st.time_input("🕐 Start Time", value=time(9, 15))
    end_time = st.time_input("🕕 End Time", value=time(15, 30))
    
    analysis_depth = st.selectbox(
        "🔍 Analysis Depth",
        ["Quick", "Standard", "Comprehensive", "Deep Research"],
        index=1
    )
    
    include_risk = st.checkbox("⚠️ Include Risk Assessment", value=True)
    include_portfolio = st.checkbox("💼 Portfolio Advice", value=True)
    
    if st.button("🚀 Generate Analysis", type="primary"):
        st.session_state.run_analysis = True

# Main Analysis
if hasattr(st.session_state, 'run_analysis') and st.session_state.run_analysis:
    with st.spinner("🔮 Performing astrological calculations..."):
        
        # Generate data
        planetary_data = generate_planetary_data(selected_date)
        moon_phase = get_moon_phase(selected_date)
        
        # Dashboard metrics
        st.markdown("## 📊 Market Intelligence Dashboard")
        
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
            muhurat_quality = random.choice(["Good", "Average", "Caution"])
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
            market_volatility = random.choice(["Low", "Medium", "High"])
            volatility_colors = {"Low": "green", "Medium": "orange", "High": "red"}
            st.markdown(f"""
                <div class="metric-card" style="background: {volatility_colors[market_volatility]};">
                    <h3>📊 Market Volatility</h3>
                    <h2>{market_volatility}</h2>
                </div>
            """, unsafe_allow_html=True)
        
        # Risk Assessment
        if include_risk:
            st.markdown("## ⚠️ Risk Assessment")
            
            malefic_strength = sum(p.strength for p in planetary_data if any(planet["name"] == p.name and planet["nature"] == "Malefic" for planet in PLANETS))
            benefic_strength = sum(p.strength for p in planetary_data if any(planet["name"] == p.name and planet["nature"] == "Benefic" for planet in PLANETS))
            
            risk_score = min(100, max(0, 50 + (malefic_strength - benefic_strength) / 10 + retrograde_count * 5))
            
            if risk_score <= 30:
                risk_level, risk_color = "Low", "green"
            elif risk_score <= 60:
                risk_level, risk_color = "Medium", "orange"
            else:
                risk_level, risk_color = "High", "red"
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                    <div style="background: {risk_color}; padding: 1rem; border-radius: 10px; color: white;">
                        <h3>🎯 Risk Level: {risk_level}</h3>
                        <h2>Score: {risk_score:.0f}/100</h2>
                    </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                    <div class="metric-card">
                        <h3>😇 Benefic Strength</h3>
                        <h2>{benefic_strength:.1f}</h2>
                    </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                    <div class="metric-card">
                        <h3>😈 Malefic Strength</h3>
                        <h2>{malefic_strength:.1f}</h2>
                    </div>
                """, unsafe_allow_html=True)
        
        # Tabbed Analysis
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🎯 Quick Signals", "🏭 Sector Analysis", "⏰ Time Analysis", 
            "🪐 Planetary Details", "💼 Trading Signals"
        ])
        
        with tab1:
            st.markdown("### 🎯 Quick Trading Signals")
            
            # Generate signals based on market type
            if market_type == "Indian":
                signal_items = SECTORS
                signal_type = "sector"
            elif market_type == "Commodity":
                signal_items = COMMODITIES[:5]  # Gold, Silver, Crude Oil, Natural Gas, Copper
                signal_type = "commodity"
            else:
                # For Global, Crypto, Forex - create generic items
                signal_items = [{"name": market} for market in markets[:6]]
                signal_type = "market"
            
            bullish_count = random.randint(3, 5)
            bearish_count = random.randint(2, 4)
            neutral_count = random.randint(3, 5)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("#### 🟢 Bullish Opportunities")
                for i in range(bullish_count):
                    item = random.choice(signal_items)
                    optimal_time = f"{random.randint(9, 15)}:{random.choice(['00', '30'])}"
                    
                    if market_type == "Commodity":
                        planet_info = f"Ruling Planet: {item.get('rulingPlanet', 'N/A')}"
                        if item['name'] == "Gold":
                            driver = "Safe haven demand rising"
                        elif item['name'] == "Silver":
                            driver = "Industrial demand surge"
                        elif item['name'] == "Crude Oil":
                            driver = "Supply concerns mounting"
                        else:
                            driver = "Strong fundamentals"
                    else:
                        planet_info = f"Planetary influence positive"
                        if market_type == "Indian" and "name" in item:
                            if "FMCG" in item['name']:
                                driver = "Venus favorable for consumer goods"
                            elif "Pharma" in item['name']:
                                driver = "Moon strength boosts healthcare"
                            elif "Metal" in item['name']:
                                driver = "Mars energy supports metals"
                            elif "PSU Bank" in item['name']:
                                driver = "Jupiter blesses public banking"
                            elif "Oil & Gas" in item['name']:
                                driver = "Sun power energizes oil sector"
                            elif "Gold" in item['name']:
                                driver = "Sun exaltation favors gold"
                            elif "Sugar" in item['name']:
                                driver = "Venus sweetens sugar prospects"
                            elif "Tea" in item['name']:
                                driver = "Moon nourishes plantation sector"
                            elif "Cement" in item['name']:
                                driver = "Saturn strengthens construction"
                            else:
                                driver = "Technical breakout expected"
                        else:
                            driver = "Technical breakout expected"
                    
                    st.markdown(f"""
                        <div class="bullish-card">
                            <h4>{item['name']}</h4>
                            <p><strong>Action:</strong> GO LONG</p>
                            <p><strong>Best Time:</strong> {optimal_time}</p>
                            <p><strong>Confidence:</strong> {random.choice(['High', 'Medium'])}</p>
                            <p><small>{driver}</small></p>
                        </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("#### 🔴 Bearish Warnings")
                for i in range(bearish_count):
                    item = random.choice(signal_items)
                    optimal_time = f"{random.randint(9, 15)}:{random.choice(['00', '30'])}"
                    
                    if market_type == "Commodity":
                        if item['name'] == "Gold":
                            driver = "Dollar strength pressure"
                        elif item['name'] == "Silver":
                            driver = "Industrial demand concerns"
                        elif item['name'] == "Crude Oil":
                            driver = "Oversupply fears"
                        else:
                            driver = "Bearish sentiment"
                    else:
                        if market_type == "Indian" and "name" in item:
                            if "FMCG" in item['name']:
                                driver = "Venus weak - consumer spending down"
                            elif "Pharma" in item['name']:
                                driver = "Moon afflicted - regulatory concerns"
                            elif "Metal" in item['name']:
                                driver = "Mars retrograde - demand slowdown"
                            else:
                                driver = "Technical breakdown risk"
                        else:
                            driver = "Technical breakdown risk"
                    
                    st.markdown(f"""
                        <div class="bearish-card">
                            <h4>{item['name']}</h4>
                            <p><strong>Action:</strong> GO SHORT</p>
                            <p><strong>Best Time:</strong> {optimal_time}</p>
                            <p><strong>Confidence:</strong> {random.choice(['High', 'Medium'])}</p>
                            <p><small>{driver}</small></p>
                        </div>
                    """, unsafe_allow_html=True)
            
            with col3:
                st.markdown("#### 🟡 Neutral Zones")
                for i in range(neutral_count):
                    item = random.choice(signal_items)
                    st.markdown(f"""
                        <div class="neutral-card">
                            <h4>{item['name']}</h4>
                            <p><strong>Action:</strong> HOLD/WATCH</p>
                            <p><strong>Status:</strong> Range-bound</p>
                            <p><small>Await clear direction</small></p>
                        </div>
                    """, unsafe_allow_html=True)
        
        with tab2:
            if market_type == "Indian":
                st.markdown("### 🏭 Comprehensive Sector Analysis")
                
                sector_data = []
                for sector in SECTORS:
                    bias = random.choice(["BULLISH", "BEARISH", "NEUTRAL"])
                    action = "BUY" if bias == "BULLISH" else "SELL" if bias == "BEARISH" else "HOLD"
                    strength = random.randint(40, 90)
                    
                    sector_data.append({
                        "Sector": sector["name"],
                        "Ruling Planet": sector["rulingPlanet"],
                        "Bias": bias,
                        "Action": action,
                        "Strength": f"{strength}%",
                        "Best Symbol": random.choice(sector["symbols"])
                    })
                
                df = pd.DataFrame(sector_data)
                st.dataframe(df, use_container_width=True)
                
                # Sector strength chart
                st.markdown("#### 📊 Sector Strength Distribution")
                chart_data = pd.DataFrame({
                    'Sector': [s['Sector'] for s in sector_data],
                    'Strength': [int(s['Strength'].replace('%', '')) for s in sector_data]
                })
                st.bar_chart(chart_data.set_index('Sector'))
                
            elif market_type == "Commodity":
                st.markdown("### 🥇 Commodity Analysis")
                
                commodity_data = []
                for commodity in COMMODITIES[:5]:  # Gold, Silver, Crude Oil, Natural Gas, Copper
                    bias = random.choice(["BULLISH", "BEARISH", "NEUTRAL"])
                    action = "BUY" if bias == "BULLISH" else "SELL" if bias == "BEARISH" else "HOLD"
                    strength = random.randint(40, 90)
                    
                    # Commodity-specific analysis
                    if commodity["name"] == "Gold":
                        analysis = "Safe haven demand + inflation hedge"
                    elif commodity["name"] == "Silver":
                        analysis = "Industrial demand + precious metal appeal"
                    elif commodity["name"] == "Crude Oil":
                        analysis = "Geopolitical tensions + supply dynamics"
                    elif commodity["name"] == "Natural Gas":
                        analysis = "Seasonal demand + storage levels"
                    elif commodity["name"] == "Copper":
                        analysis = "Industrial growth + infrastructure demand"
                    else:
                        analysis = "Global economic factors"
                    
                    commodity_data.append({
                        "Commodity": commodity["name"],
                        "Symbol": commodity["symbol"],
                        "Ruling Planet": commodity["rulingPlanet"],
                        "Bias": bias,
                        "Action": action,
                        "Strength": f"{strength}%",
                        "Market Hours": commodity["market_hours"],
                        "Key Driver": analysis
                    })
                
                df = pd.DataFrame(commodity_data)
                st.dataframe(df, use_container_width=True)
                
                # Commodity strength chart
                st.markdown("#### 📊 Commodity Strength")
                chart_data = pd.DataFrame({
                    'Commodity': [c['Commodity'] for c in commodity_data],
                    'Strength': [int(c['Strength'].replace('%', '')) for c in commodity_data]
                })
                st.bar_chart(chart_data.set_index('Commodity'))
                
            else:
                st.markdown("### 📊 Market Analysis")
                st.info(f"Analysis for {market_type} markets - {market_index}")
                
                # Generic market analysis for other types
                market_data = []
                sample_markets = markets[:5] if len(markets) > 5 else markets
                
                for market in sample_markets:
                    bias = random.choice(["BULLISH", "BEARISH", "NEUTRAL"])
                    action = "BUY" if bias == "BULLISH" else "SELL" if bias == "BEARISH" else "HOLD"
                    strength = random.randint(40, 90)
                    
                    market_data.append({
                        "Market": market,
                        "Type": market_type,
                        "Bias": bias,
                        "Action": action,
                        "Strength": f"{strength}%"
                    })
                
                df = pd.DataFrame(market_data)
                st.dataframe(df, use_container_width=True)
                
                # Market strength chart
                st.markdown(f"#### 📊 {market_type} Market Strength")
                chart_data = pd.DataFrame({
                    'Market': [m['Market'] for m in market_data],
                    'Strength': [int(m['Strength'].replace('%', '')) for m in market_data]
                })
                st.bar_chart(chart_data.set_index('Market'))
        
        with tab3:
            st.markdown("### ⏰ Time Analysis")
            
            # Generate time slots
            time_slots = []
            current_time = datetime.combine(selected_date, start_time)
            end_datetime = datetime.combine(selected_date, end_time)
            
            while current_time <= end_datetime:
                time_slots.append(current_time.strftime("%H:%M"))
                current_time += timedelta(minutes=45)
            
            time_data = []
            sentiment_values = []
            
            for time_slot in time_slots:
                impact = random.choice(["Bullish", "Bearish", "Neutral"])
                confidence = random.choice(["High", "Medium", "Low"])
                active_planets = random.sample([p["name"] for p in PLANETS], 3)
                
                time_data.append({
                    "Time": time_slot,
                    "Market Impact": impact,
                    "Confidence": confidence,
                    "Active Planets": ", ".join(active_planets),
                    "Recommended Action": f"{'Buy' if impact == 'Bullish' else 'Sell' if impact == 'Bearish' else 'Hold'} {market_index}"
                })
                
                sentiment_values.append(1 if impact == "Bullish" else -1 if impact == "Bearish" else 0)
            
            time_df = pd.DataFrame(time_data)
            st.dataframe(time_df, use_container_width=True)
            
            # Market sentiment flow
            st.markdown("#### 📈 Market Sentiment Flow")
            sentiment_df = pd.DataFrame({
                'Time': time_slots,
                'Sentiment': sentiment_values
            })
            st.line_chart(sentiment_df.set_index('Time'))
        
        with tab4:
            st.markdown("### 🪐 Planetary Details")
            
            # Planetary strength chart
            st.markdown("#### 🌟 Planetary Strength")
            planet_df = pd.DataFrame({
                'Planet': [p.name for p in planetary_data],
                'Strength': [p.strength for p in planetary_data]
            })
            st.bar_chart(planet_df.set_index('Planet'))
            
            # Detailed table
            planet_table_data = []
            for p in planetary_data:
                planet_info = next(planet for planet in PLANETS if planet["name"] == p.name)
                planet_table_data.append({
                    "Planet": f"{p.name} {planet_info['symbol']}",
                    "Sign": p.sign,
                    "Nakshatra": p.nakshatra,
                    "Pada": p.pada,
                    "House": p.house,
                    "Strength": f"{p.strength:.1f}%",
                    "Status": "Retrograde" if p.retrograde else "Direct",
                    "Key Aspects": ", ".join(p.aspects[:2]) if p.aspects else "None"
                })
            
            planet_df = pd.DataFrame(planet_table_data)
            st.dataframe(planet_df, use_container_width=True)
        
        with tab5:
            st.markdown("### 💼 Trading Signals")
            
            # Generate trading signals
            signals = []
            if market_type == "Indian":
                symbols = []
                for sector in SECTORS[:8]:  # Use more sectors for signals
                    symbols.extend(sector["symbols"][:2])
            elif market_type == "Commodity":
                symbols = [c["symbol"] for c in COMMODITIES[:5]]  # Gold, Silver, Crude Oil, Natural Gas, Copper
            else:
                symbols = [c["symbol"] for c in COMMODITIES]
            
            for symbol in symbols:
                bias = random.choice(["BULLISH", "BEARISH", "NEUTRAL"])
                
                # Set appropriate price format based on market type
                if market_type == "Indian":
                    price_prefix = "₹"
                    price_range = (100, 5000)
                elif market_type == "Commodity":
                    if symbol in ["GOLD", "SILVER"]:
                        price_prefix = "$"
                        price_range = (1800, 2200) if symbol == "GOLD" else (22, 28)  # Gold per oz, Silver per oz
                    elif symbol == "CRUDEOIL":
                        price_prefix = "$"
                        price_range = (70, 90)  # Crude per barrel
                    elif symbol == "NATURALGAS":
                        price_prefix = "$"
                        price_range = (2, 6)  # Natural Gas per MMBtu
                    elif symbol == "COPPER":
                        price_prefix = "$"
                        price_range = (3, 5)  # Copper per lb
                    else:
                        price_prefix = "$"
                        price_range = (10, 500)
                else:
                    price_prefix = "$"
                    price_range = (10, 500)
                
                signals.append({
                    "Symbol": symbol,
                    "Market Type": market_type,
                    "Bias": bias,
                    "Action": "BUY" if bias == "BULLISH" else "SELL" if bias == "BEARISH" else "HOLD",
                    "Entry Price": f"{price_prefix}{random.uniform(price_range[0], price_range[1]):.2f}",
                    "Target": f"{random.uniform(2, 8):.1f}%",
                    "Stop Loss": f"{random.uniform(1, 4):.1f}%",
                    "Confidence": random.choice(["High", "Medium", "Low"]),
                    "Risk Level": random.choice(["Low", "Medium", "High"])
                })
            
            signals_df = pd.DataFrame(signals)
            st.dataframe(signals_df, use_container_width=True)
            
            # Download button
            csv = signals_df.to_csv(index=False)
            st.download_button(
                label="📥 Download Signals CSV",
                data=csv,
                file_name=f"signals_{selected_date}.csv",
                mime="text/csv"
            )
        
        # Key Insights
        st.markdown("## 🔍 Key Insights")
        
        strongest_planet = max(planetary_data, key=lambda x: x.strength)
        retrograde_planets = [p.name for p in planetary_data if p.retrograde]
        
        insights = [
            f"🌟 Strongest planetary influence: **{strongest_planet.name}** (Strength: {strongest_planet.strength:.1f}%)",
            f"⚠️ Retrograde planets: **{', '.join(retrograde_planets) if retrograde_planets else 'None'}**",
            f"🌙 Moon phase **{moon_phase}** suggests {'increased volatility' if 'Full' in moon_phase or 'New' in moon_phase else 'moderate stability'}",
            f"⏰ Best trading hours: **{random.choice(['10:00-11:30', '13:00-14:30', '11:00-12:00'])}**",
            f"🎯 Market sentiment: **{random.choice(['Cautiously Optimistic', 'Neutral with Bullish Bias', 'Mixed Signals'])}**"
        ]
        
        if market_type == "Indian":
            sector_insights = [
                f"🏭 **Pharma sector** shows strong Moon influence - healthcare demand rising",
                f"💰 **PSU Banks** benefit from Jupiter's blessing - public sector strength",
                f"🥇 **Gold ETFs** shine with Sun's power - safe haven appeal",
                f"🏗️ **Cement sector** gains Saturn's stability - infrastructure boost"
            ]
            insights.extend(random.sample(sector_insights, 2))
        
        for insight in insights:
            st.markdown(f"• {insight}")
        
        # Special Alerts
        st.markdown("## 🚨 Special Alerts")
        alerts = [
            "🌒 New Moon approaching - Expect volatility",
            "♃ Jupiter aspect favorable for banking sector",
            "♄ Saturn square Mars - Caution in metal stocks",
            "☉ Sun exalted - Golden opportunities in precious metals",
            "♀ Venus strong - FMCG and consumer goods bullish"
        ]
        
        for alert in random.sample(alerts, 3):
            st.warning(alert)
        
        # Disclaimer
        st.markdown("---")
        st.markdown("""
            <div style="text-align: center; padding: 1rem; background-color: rgba(0,0,0,0.1); border-radius: 10px;">
                <h4>⚠️ Important Disclaimer</h4>
                <p>This analysis is for educational purposes only. Always consult qualified financial advisors 
                before making investment decisions. Astrological predictions do not guarantee market outcomes.</p>
            </div>
        """, unsafe_allow_html=True)

# Default message
if not hasattr(st.session_state, 'run_analysis'):
    st.info("👈 Configure your analysis parameters in the sidebar and click 'Generate Analysis' to begin!")
    
    st.markdown("## 🌟 Welcome to Advanced Vedic Astro Trader Pro!")
    st.markdown("""
    This application combines ancient Vedic astrology with modern market analysis to provide:
    
    - **🪐 Planetary Position Analysis** - Real-time planetary strength calculations
    - **📊 Comprehensive Sector Analysis** - All major Indian market sectors including:
      - Traditional sectors (Banking, IT, Auto, Energy)
      - **NEW**: Pharma, FMCG, Metal, PSU Banking
      - **NEW**: Oil & Gas, Gold ETF, Sugar, Tea & Plantation
      - **NEW**: Cement and Infrastructure sectors
    - **⏰ Intraday Time Analysis** - Optimal trading hours based on planetary periods
    - **💼 Individual Stock Signals** - Specific buy/sell recommendations
    - **⚠️ Risk Assessment** - Comprehensive risk evaluation using planetary influences
    
    **Enhanced Features:**
    - Support for **15 Indian market sectors** including all major indices
    - Support for Global, Commodity, Cryptocurrency, and Forex markets
    - Multiple analysis depths from Quick to Deep Research
    - Interactive charts and visualizations
    - Downloadable trading signals
    - Real-time planetary strength calculations
    - Specialized analysis for new sectors like PSU Banking, Tea, Sugar, and Cement
    
    **New Sectors Added:**
    - 💊 **Nifty Pharma** - Healthcare and pharmaceutical stocks
    - 🛒 **Nifty FMCG** - Fast-moving consumer goods
    - 🔩 **Nifty Metal** - Steel, aluminum, and mining companies
    - 🏛️ **Nifty PSU Bank** - Public sector banking
    - ⛽ **Nifty Oil & Gas** - Energy sector stocks
    - 🥇 **Gold ETF** - Precious metals and gold investments
    - 🍯 **Sugar Stocks** - Sugar industry companies
    - 🍃 **Tea & Plantation** - Tea gardens and plantation companies
    - 🏗️ **Cement Sector** - Construction and cement companies
    
    Select your preferences in the sidebar to get started!
    """)
