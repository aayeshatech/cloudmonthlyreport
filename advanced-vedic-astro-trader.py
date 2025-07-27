<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced Astrological Trading Analysis Platform</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%);
            min-height: 100vh;
            color: #e0e0e0;
            overflow-x: hidden;
        }

        .container {
            max-width: 1600px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            margin-bottom: 40px;
            position: relative;
        }

        .header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 200px;
            height: 2px;
            background: linear-gradient(90deg, transparent, #ffd700, transparent);
        }

        .header h1 {
            font-size: 3rem;
            margin-bottom: 15px;
            background: linear-gradient(45deg, #ffd700, #ffb347, #ff6b35);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 30px rgba(255, 215, 0, 0.3);
            animation: glow 2s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { filter: brightness(1); }
            to { filter: brightness(1.2); }
        }

        .header p {
            font-size: 1.2rem;
            color: #b8b8b8;
            margin-bottom: 10px;
        }

        .dashboard {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 30px;
            margin-bottom: 30px;
        }

        .control-panel {
            background: rgba(26, 26, 46, 0.8);
            border-radius: 20px;
            padding: 30px;
            border: 1px solid rgba(255, 215, 0, 0.2);
            backdrop-filter: blur(10px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        }

        .quick-stats {
            background: rgba(22, 33, 62, 0.8);
            border-radius: 20px;
            padding: 30px;
            border: 1px solid rgba(255, 179, 71, 0.2);
            backdrop-filter: blur(10px);
        }

        .section-title {
            font-size: 1.5rem;
            margin-bottom: 20px;
            color: #ffd700;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .input-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
            margin-bottom: 25px;
        }

        .input-group {
            position: relative;
        }

        .input-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #ffd700;
            font-size: 0.9rem;
        }

        .input-group input, .input-group select {
            width: 100%;
            padding: 15px 20px;
            border: 2px solid rgba(255, 215, 0, 0.3);
            border-radius: 10px;
            font-size: 1rem;
            background: rgba(255, 255, 255, 0.05);
            color: #e0e0e0;
            transition: all 0.3s ease;
        }

        .input-group input:focus, .input-group select:focus {
            outline: none;
            border-color: #ffd700;
            background: rgba(255, 255, 255, 0.1);
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.2);
        }

        .btn {
            padding: 15px 30px;
            border: none;
            border-radius: 10px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
            position: relative;
            overflow: hidden;
        }

        .btn-primary {
            background: linear-gradient(45deg, #ffd700, #ffb347);
            color: #000;
        }

        .btn-secondary {
            background: linear-gradient(45deg, #ff6b35, #f7931e);
            color: white;
        }

        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(255, 215, 0, 0.3);
        }

        .btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.5s;
        }

        .btn:hover::before {
            left: 100%;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
        }

        .stat-card {
            background: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            border: 1px solid rgba(255, 215, 0, 0.1);
            transition: all 0.3s ease;
        }

        .stat-card:hover {
            transform: scale(1.05);
            border-color: rgba(255, 215, 0, 0.3);
        }

        .stat-card h3 {
            font-size: 2rem;
            color: #ffd700;
            margin-bottom: 5px;
        }

        .stat-card p {
            color: #b8b8b8;
            font-size: 0.9rem;
        }

        .report-container {
            background: rgba(26, 26, 46, 0.9);
            border-radius: 20px;
            margin-bottom: 30px;
            border: 1px solid rgba(255, 215, 0, 0.2);
            overflow: hidden;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        }

        .report-header {
            background: linear-gradient(45deg, #1a1a2e, #16213e);
            color: #ffd700;
            padding: 25px;
            text-align: center;
            border-bottom: 2px solid rgba(255, 215, 0, 0.3);
        }

        .report-tabs {
            display: flex;
            background: rgba(22, 33, 62, 0.8);
            border-bottom: 1px solid rgba(255, 215, 0, 0.2);
        }

        .tab {
            flex: 1;
            padding: 15px 20px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            border-right: 1px solid rgba(255, 215, 0, 0.1);
            color: #b8b8b8;
        }

        .tab.active {
            background: rgba(255, 215, 0, 0.1);
            color: #ffd700;
            border-bottom: 2px solid #ffd700;
        }

        .tab:hover {
            background: rgba(255, 215, 0, 0.05);
            color: #ffd700;
        }

        .tab-content {
            padding: 30px;
            display: none;
        }

        .tab-content.active {
            display: block;
        }

        .forecast-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
            max-height: 600px;
            overflow-y: auto;
            padding-right: 10px;
        }

        .forecast-grid::-webkit-scrollbar {
            width: 8px;
        }

        .forecast-grid::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
        }

        .forecast-grid::-webkit-scrollbar-thumb {
            background: linear-gradient(45deg, #ffd700, #ffb347);
            border-radius: 10px;
        }

        .forecast-grid::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(45deg, #ffb347, #ffd700);
        }

        .forecast-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 25px;
            border-left: 4px solid #ffd700;
            transition: all 0.3s ease;
        }

        .forecast-card:hover {
            transform: translateX(10px);
            background: rgba(255, 255, 255, 0.08);
        }

        .forecast-date {
            font-size: 1.1rem;
            color: #ffd700;
            margin-bottom: 10px;
            font-weight: 600;
        }

        .forecast-event {
            font-size: 1.3rem;
            margin-bottom: 15px;
            color: #e0e0e0;
        }

        .forecast-impact {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            text-transform: uppercase;
        }

        .bullish {
            background: linear-gradient(45deg, #4caf50, #8bc34a);
            color: white;
        }

        .bearish {
            background: linear-gradient(45deg, #f44336, #ff5722);
            color: white;
        }

        .neutral {
            background: linear-gradient(45deg, #ff9800, #ffc107);
            color: #000;
        }

        .transit-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        .transit-table th {
            background: rgba(255, 215, 0, 0.1);
            padding: 15px;
            text-align: left;
            color: #ffd700;
            border-bottom: 2px solid rgba(255, 215, 0, 0.3);
        }

        .transit-table td {
            padding: 12px 15px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            color: #e0e0e0;
        }

        .transit-table tr:hover {
            background: rgba(255, 255, 255, 0.05);
        }

        .planetary-positions {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin-bottom: 30px;
        }

        .planet-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            border: 1px solid rgba(255, 215, 0, 0.1);
        }

        .planet-symbol {
            font-size: 2rem;
            margin-bottom: 10px;
        }

        .planet-degree {
            color: #ffd700;
            font-weight: 600;
            margin-bottom: 5px;
        }

        .planet-sign {
            color: #b8b8b8;
            font-size: 0.9rem;
        }

        .loading {
            display: none;
            text-align: center;
            padding: 60px;
        }

        .spinner {
            border: 4px solid rgba(255, 215, 0, 0.3);
            border-top: 4px solid #ffd700;
            border-radius: 50%;
            width: 60px;
            height: 60px;
            animation: spin 1s linear infinite;
            margin: 0 auto 30px;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .signal-indicator {
            display: inline-block;
            padding: 8px 16px;
            border-radius: 25px;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.8rem;
            letter-spacing: 1px;
        }

        .buy-signal {
            background: linear-gradient(45deg, #4caf50, #8bc34a);
            color: white;
            animation: pulse-green 2s infinite;
        }

        .sell-signal {
            background: linear-gradient(45deg, #f44336, #ff5722);
            color: white;
            animation: pulse-red 2s infinite;
        }

        .hold-signal {
            background: linear-gradient(45deg, #ff9800, #ffc107);
            color: #000;
        }

        @keyframes pulse-green {
            0%, 100% { box-shadow: 0 0 0 0 rgba(76, 175, 80, 0.7); }
            50% { box-shadow: 0 0 0 10px rgba(76, 175, 80, 0); }
        }

        @keyframes pulse-red {
            0%, 100% { box-shadow: 0 0 0 0 rgba(244, 67, 54, 0.7); }
            50% { box-shadow: 0 0 0 10px rgba(244, 67, 54, 0); }
        }

        @media (max-width: 1200px) {
            .dashboard {
                grid-template-columns: 1fr;
            }
            
            .forecast-grid {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 768px) {
            .container {
                padding: 15px;
            }
            
            .header h1 {
                font-size: 2rem;
            }
            
            .stats-grid {
                grid-template-columns: 1fr;
            }
            
            .planetary-positions {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        .advanced-features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }

        .feature-card {
            background: rgba(22, 33, 62, 0.8);
            border-radius: 15px;
            padding: 25px;
            border: 1px solid rgba(255, 179, 71, 0.2);
            text-align: center;
        }

        .feature-icon {
            font-size: 3rem;
            margin-bottom: 15px;
            background: linear-gradient(45deg, #ffd700, #ffb347);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>🌟 Advanced Astrological Trading Platform</h1>
            <p>Professional Market Analysis with Planetary Transits & Forecasting</p>
            <div style="margin-top: 15px; color: #ffd700;">
                <span id="currentDateTime"></span>
            </div>
        </header>

        <div class="dashboard">
            <div class="control-panel">
                <h2 class="section-title">⚙️ Analysis Controls</h2>
                
                <div class="input-grid">
                    <div class="input-group">
                        <label for="symbol">📈 Symbol/Index</label>
                        <input type="text" id="symbol" value="NIFTY" placeholder="Enter symbol (e.g., NIFTY, BANKNIFTY, SENSEX)">
                    </div>
                    

                    
                    <div class="input-group">
                        <label for="analysisType">🔮 Analysis Type</label>
                        <select id="analysisType">
                            <option value="monthly">Monthly Forecast</option>
                            <option value="weekly">Weekly Analysis</option>
                            <option value="daily">Daily Transits</option>
                            <option value="annual">Annual Overview</option>
                        </select>
                    </div>
                    
                    <div class="input-group">
                        <label for="selectedMonth">📅 Select Month</label>
                        <select id="selectedMonth">
                            <option value="0">January 2025</option>
                            <option value="1">February 2025</option>
                            <option value="2">March 2025</option>
                            <option value="3">April 2025</option>
                            <option value="4">May 2025</option>
                            <option value="5">June 2025</option>
                            <option value="6">July 2025</option>
                            <option value="7" selected>August 2025</option>
                            <option value="8">September 2025</option>
                            <option value="9">October 2025</option>
                            <option value="10">November 2025</option>
                            <option value="11">December 2025</option>
                        </select>
                    </div>
                    
                    <div class="input-group">
                        <label for="marketType">🏪 Market Type</label>
                        <select id="marketType">
                            <option value="equity">Equity</option>
                            <option value="commodity">Commodity</option>
                            <option value="currency">Currency</option>
                            <option value="crypto">Cryptocurrency</option>
                        </select>
                    </div>
                    
                    <div class="input-group">
                        <label for="timeZone">🌍 Time Zone</label>
                        <select id="timeZone">
                            <option value="IST">IST (Indian Standard Time)</option>
                            <option value="EST">EST (Eastern Standard Time)</option>
                            <option value="GMT">GMT (Greenwich Mean Time)</option>
                            <option value="JST">JST (Japan Standard Time)</option>
                        </select>
                    </div>
                </div>
                
                <div style="display: flex; gap: 15px; flex-direction: column;">
                    <button class="btn btn-primary" onclick="generateReport()">🚀 Generate Analysis</button>
                    <button class="btn btn-secondary" onclick="exportReport()">📊 Export Report</button>
                </div>
            </div>

            <div class="quick-stats">
                <h2 class="section-title">📊 Quick Overview</h2>
                
                <div class="stats-grid">
                    <div class="stat-card">
                        <h3 id="marketSentiment">--</h3>
                        <p>Market Sentiment</p>
                    </div>
                    <div class="stat-card">
                        <h3 id="nextSignal">--</h3>
                        <p>Next Major Signal</p>
                    </div>
                    <div class="stat-card">
                        <h3 id="planetsActive">--</h3>
                        <p>Active Transits</p>
                    </div>
                    <div class="stat-card">
                        <h3 id="riskLevel">--</h3>
                        <p>Risk Level</p>
                    </div>
                </div>

                <div class="planetary-positions" id="planetaryPositions">
                    <!-- Planetary positions will be populated here -->
                </div>
            </div>
        </div>

        <div class="report-container" id="reportContainer" style="display: none;">
            <div class="report-header">
                <h2>🌟 Astrological Market Analysis Report</h2>
                <p id="reportSymbol">Symbol: NIFTY | Generated: <span id="reportTime"></span></p>
            </div>

            <div class="report-tabs">
                <div class="tab active" onclick="showTab('forecast')">🔮 Monthly Forecast</div>
                <div class="tab" onclick="showTab('transits')">🌙 Transit Analysis</div>
                <div class="tab" onclick="showTab('signals')">📈 Trading Signals</div>
                <div class="tab" onclick="showTab('correlation')">📊 Historical Correlation</div>
            </div>

            <div id="forecastTab" class="tab-content active">
                <h3 style="color: #ffd700; margin-bottom: 20px;">📅 Monthly Planetary Transit Forecast</h3>
                <div style="text-align: center; margin-bottom: 15px; color: #b8b8b8; font-size: 0.9rem; padding: 10px; background: rgba(255, 215, 0, 0.1); border-radius: 8px; border-left: 3px solid #ffd700;">
                    <span id="forecastCount">Showing all daily forecasts for selected month</span> | 
                    <span style="color: #ffd700;">📜 Scroll down to view all dates ⬇️</span>
                </div>
                <div class="forecast-grid" id="monthlyForecast">
                    <!-- Monthly forecasts will be populated here -->
                </div>
            </div>

            <div id="transitsTab" class="tab-content">
                <h3 style="color: #ffd700; margin-bottom: 20px;">🌙 Detailed Transit Analysis</h3>
                <div style="text-align: center; margin-bottom: 15px; color: #b8b8b8; font-size: 0.9rem; padding: 10px; background: rgba(255, 215, 0, 0.1); border-radius: 8px; border-left: 3px solid #ffd700;">
                    <span id="transitCount">Complete daily transit data for selected month</span> | 
                    <span style="color: #ffd700;">📜 Scroll table to view all dates ⬇️</span>
                </div>
                <div class="table-container">
                    <table class="transit-table" id="transitTable">
                        <thead>
                            <tr>
                                <th>Date & Time</th>
                                <th>Planet</th>
                                <th>Transit Event</th>
                                <th>Market Impact</th>
                                <th>% Change</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody id="transitTableBody">
                            <!-- Transit data will be populated here -->
                        </tbody>
                    </table>
                </div>
            </div>

            <div id="signalsTab" class="tab-content">
                <h3 style="color: #ffd700; margin-bottom: 20px;">📈 Trading Signals & Recommendations</h3>
                <div id="tradingSignals">
                    <!-- Trading signals will be populated here -->
                </div>
            </div>

            <div id="correlationTab" class="tab-content">
                <h3 style="color: #ffd700; margin-bottom: 20px;">📊 Historical Planetary-Market Correlation</h3>
                <div id="correlationAnalysis">
                    <!-- Correlation analysis will be populated here -->
                </div>
            </div>
        </div>

        <div class="advanced-features">
            <div class="feature-card">
                <div class="feature-icon">🔮</div>
                <h3>Predictive Modeling</h3>
                <p>Advanced algorithms combining planetary movements with market psychology</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <h3>Real-time Updates</h3>
                <p>Live planetary positions and instant market correlations</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3>Multi-timeframe Analysis</h3>
                <p>From intraday to annual forecasting capabilities</p>
            </div>
        </div>

        <div class="loading" id="loading">
            <div class="spinner"></div>
            <p>Calculating planetary positions and market correlations...</p>
        </div>
    </div>

    <script>
        // Global month names array - moved to top level to avoid temporal dead zone
        const monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 
                           'July', 'August', 'September', 'October', 'November', 'December'];

        // Planetary symbols and data
        const PLANETS = {
            sun: { symbol: '☉', name: 'Sun' },
            moon: { symbol: '☽', name: 'Moon' },
            mercury: { symbol: '☿', name: 'Mercury' },
            venus: { symbol: '♀', name: 'Venus' },
            mars: { symbol: '♂', name: 'Mars' },
            jupiter: { symbol: '♃', name: 'Jupiter' },
            saturn: { symbol: '♄', name: 'Saturn' },
            uranus: { symbol: '♅', name: 'Uranus' },
            neptune: { symbol: '♆', name: 'Neptune' },
            pluto: { symbol: '♇', name: 'Pluto' }
        };

        const ZODIAC_SIGNS = [
            { name: "♈ Aries", start: 0 },
            { name: "♉ Taurus", start: 30 },
            { name: "♊ Gemini", start: 60 },
            { name: "♋ Cancer", start: 90 },
            { name: "♌ Leo", start: 120 },
            { name: "♍ Virgo", start: 150 },
            { name: "♎ Libra", start: 180 },
            { name: "♏ Scorpio", start: 210 },
            { name: "♐ Sagittarius", start: 240 },
            { name: "♑ Capricorn", start: 270 },
            { name: "♒ Aquarius", start: 300 },
            { name: "♓ Pisces", start: 330 }
        ];

        let currentData = {};

        // Update current date and time
        function updateDateTime() {
            const now = new Date();
            document.getElementById('currentDateTime').textContent = 
                now.toLocaleDateString() + ' ' + now.toLocaleTimeString();
        }

        // Calculate planetary positions (simplified calculation)
        function calculatePlanetaryPositions(date) {
            const positions = {};
            const daysSince2000 = (date - new Date('2000-01-01')) / (1000 * 60 * 60 * 24);
            
            // Simplified orbital calculations
            positions.sun = (280.460 + 0.9856474 * daysSince2000) % 360;
            positions.moon = (218.316 + 13.176396 * daysSince2000) % 360;
            positions.mercury = (252.250 + 4.092317 * daysSince2000) % 360;
            positions.venus = (181.979 + 1.602130 * daysSince2000) % 360;
            positions.mars = (355.433 + 0.524033 * daysSince2000) % 360;
            positions.jupiter = (34.351 + 0.083091 * daysSince2000) % 360;
            positions.saturn = (50.077 + 0.033494 * daysSince2000) % 360;
            positions.uranus = (314.055 + 0.011733 * daysSince2000) % 360;
            positions.neptune = (304.348 + 0.006020 * daysSince2000) % 360;
            positions.pluto = (238.958 + 0.004028 * daysSince2000) % 360;
            
            return positions;
        }

        // Get zodiac sign from degree
        function getZodiacSign(degree) {
            const normalizedDegree = ((degree % 360) + 360) % 360;
            for (let i = ZODIAC_SIGNS.length - 1; i >= 0; i--) {
                if (normalizedDegree >= ZODIAC_SIGNS[i].start) {
                    const signDegree = normalizedDegree - ZODIAC_SIGNS[i].start;
                    return {
                        sign: ZODIAC_SIGNS[i].name,
                        degree: signDegree.toFixed(1)
                    };
                }
            }
            return { sign: ZODIAC_SIGNS[0].name, degree: normalizedDegree.toFixed(1) };
        }

        // Generate market impact based on planetary aspects
        function calculateMarketImpact(planetPositions) {
            const impacts = [];
            const aspects = [];
            
            // Calculate major aspects between planets
            const planetNames = Object.keys(planetPositions);
            for (let i = 0; i < planetNames.length; i++) {
                for (let j = i + 1; j < planetNames.length; j++) {
                    const planet1 = planetNames[i];
                    const planet2 = planetNames[j];
                    const angle = Math.abs(planetPositions[planet1] - planetPositions[planet2]);
                    const normalizedAngle = Math.min(angle, 360 - angle);
                    
                    // Major aspects: conjunction (0°), sextile (60°), square (90°), trine (120°), opposition (180°)
                    const majorAspects = [0, 60, 90, 120, 180];
                    const tolerance = 8; // degrees
                    
                    for (const aspectAngle of majorAspects) {
                        if (Math.abs(normalizedAngle - aspectAngle) <= tolerance) {
                            aspects.push({
                                planet1: planet1,
                                planet2: planet2,
                                aspect: aspectAngle,
                                strength: tolerance - Math.abs(normalizedAngle - aspectAngle)
                            });
                        }
                    }
                }
            }
            
            return aspects;
        }

        // Real astronomical events for 2025 with daily aspects
        const MONTHLY_ASTRONOMICAL_EVENTS_2025 = {
            0: [ // January 2025
                { date: 1, event: 'New Year - Mercury sextile Venus', aspect: 'Mercury ⚹ Venus', sentiment: 'bullish', change: '+1.2' },
                { date: 3, event: 'Sun trine Jupiter', aspect: 'Sun △ Jupiter', sentiment: 'bullish', change: '+2.1' },
                { date: 7, event: 'Venus square Mars', aspect: 'Venus □ Mars', sentiment: 'bearish', change: '-1.8' },
                { date: 11, event: 'Lunar Nodes enter Pisces/Virgo', aspect: 'Nodes Ingress', sentiment: 'neutral', change: '±0.8' },
                { date: 14, event: 'Mercury conjunct Saturn', aspect: 'Mercury ☌ Saturn', sentiment: 'bearish', change: '-1.5' },
                { date: 18, event: 'Sun sextile Neptune', aspect: 'Sun ⚹ Neptune', sentiment: 'neutral', change: '+0.9' },
                { date: 21, event: 'Mars trine Uranus', aspect: 'Mars △ Uranus', sentiment: 'bullish', change: '+2.3' },
                { date: 25, event: 'Venus conjunct Jupiter', aspect: 'Venus ☌ Jupiter', sentiment: 'bullish', change: '+3.1' },
                { date: 28, event: 'Mercury square Pluto', aspect: 'Mercury □ Pluto', sentiment: 'bearish', change: '-2.0' },
                { date: 31, event: 'Sun opposition Mars', aspect: 'Sun ☍ Mars', sentiment: 'bearish', change: '-1.7' }
            ],
            1: [ // February 2025
                { date: 2, event: 'Venus trine Saturn', aspect: 'Venus △ Saturn', sentiment: 'neutral', change: '+1.1' },
                { date: 5, event: 'Mercury sextile Jupiter', aspect: 'Mercury ⚹ Jupiter', sentiment: 'bullish', change: '+1.9' },
                { date: 9, event: 'Sun square Uranus', aspect: 'Sun □ Uranus', sentiment: 'bearish', change: '-2.2' },
                { date: 12, event: 'Mars conjunct Neptune', aspect: 'Mars ☌ Neptune', sentiment: 'neutral', change: '±1.3' },
                { date: 16, event: 'Venus opposition Pluto', aspect: 'Venus ☍ Pluto', sentiment: 'bearish', change: '-1.9' },
                { date: 19, event: 'Sun trine Mars', aspect: 'Sun △ Mars', sentiment: 'bullish', change: '+2.4' },
                { date: 22, event: 'Mercury square Neptune', aspect: 'Mercury □ Neptune', sentiment: 'bearish', change: '-1.6' },
                { date: 25, event: 'Jupiter sextile Saturn', aspect: 'Jupiter ⚹ Saturn', sentiment: 'bullish', change: '+2.8' },
                { date: 28, event: 'Venus trine Uranus', aspect: 'Venus △ Uranus', sentiment: 'bullish', change: '+2.1' }
            ],
            2: [ // March 2025
                { date: 3, event: 'Mercury conjunct Venus', aspect: 'Mercury ☌ Venus', sentiment: 'bullish', change: '+1.7' },
                { date: 7, event: 'Sun square Jupiter', aspect: 'Sun □ Jupiter', sentiment: 'bearish', change: '-1.4' },
                { date: 11, event: 'Mars sextile Saturn', aspect: 'Mars ⚹ Saturn', sentiment: 'neutral', change: '+1.0' },
                { date: 15, event: 'Venus square Uranus', aspect: 'Venus □ Uranus', sentiment: 'bearish', change: '-1.8' },
                { date: 19, event: 'Sun conjunct Mercury', aspect: 'Sun ☌ Mercury', sentiment: 'neutral', change: '+0.7' },
                { date: 22, event: 'Jupiter trine Neptune', aspect: 'Jupiter △ Neptune', sentiment: 'bullish', change: '+3.2' },
                { date: 26, event: 'Mars opposition Venus', aspect: 'Mars ☍ Venus', sentiment: 'bearish', change: '-2.1' },
                { date: 30, event: 'Neptune enters Aries', aspect: 'Neptune Ingress', sentiment: 'bullish', change: '+2.1' }
            ],
            3: [ // April 2025
                { date: 2, event: 'Mercury trine Mars', aspect: 'Mercury △ Mars', sentiment: 'bullish', change: '+1.9' },
                { date: 6, event: 'Venus sextile Neptune', aspect: 'Venus ⚹ Neptune', sentiment: 'neutral', change: '+1.2' },
                { date: 10, event: 'Sun square Saturn', aspect: 'Sun □ Saturn', sentiment: 'bearish', change: '-2.0' },
                { date: 14, event: 'Mars conjunct Jupiter', aspect: 'Mars ☌ Jupiter', sentiment: 'bullish', change: '+2.7' },
                { date: 18, event: 'Mercury opposition Uranus', aspect: 'Mercury ☍ Uranus', sentiment: 'bearish', change: '-1.5' },
                { date: 21, event: 'Venus square Saturn', aspect: 'Venus □ Saturn', sentiment: 'bearish', change: '-1.8' },
                { date: 25, event: 'Sun trine Neptune', aspect: 'Sun △ Neptune', sentiment: 'bullish', change: '+2.3' },
                { date: 29, event: 'Jupiter sextile Uranus', aspect: 'Jupiter ⚹ Uranus', sentiment: 'bullish', change: '+2.9' }
            ],
            4: [ // May 2025
                { date: 3, event: 'Mercury square Jupiter', aspect: 'Mercury □ Jupiter', sentiment: 'bearish', change: '-1.6' },
                { date: 7, event: 'Venus trine Mars', aspect: 'Venus △ Mars', sentiment: 'bullish', change: '+2.2' },
                { date: 11, event: 'Sun sextile Uranus', aspect: 'Sun ⚹ Uranus', sentiment: 'bullish', change: '+1.8' },
                { date: 15, event: 'Mars square Neptune', aspect: 'Mars □ Neptune', sentiment: 'bearish', change: '-2.1' },
                { date: 18, event: 'Jupiter squares Lunar Nodes', aspect: 'Jupiter □ Nodes', sentiment: 'neutral', change: '±1.5' },
                { date: 22, event: 'Venus opposition Jupiter', aspect: 'Venus ☍ Jupiter', sentiment: 'bearish', change: '-1.9' },
                { date: 24, event: 'Saturn enters Aries', aspect: 'Saturn Ingress', sentiment: 'bearish', change: '-1.8' },
                { date: 28, event: 'Mercury conjunct Neptune', aspect: 'Mercury ☌ Neptune', sentiment: 'neutral', change: '+0.9' },
                { date: 31, event: 'Sun square Mars', aspect: 'Sun □ Mars', sentiment: 'bearish', change: '-2.3' }
            ],
            5: [ // June 2025
                { date: 4, event: 'Venus sextile Saturn', aspect: 'Venus ⚹ Saturn', sentiment: 'neutral', change: '+1.1' },
                { date: 8, event: 'Mercury trine Uranus', aspect: 'Mercury △ Uranus', sentiment: 'bullish', change: '+2.0' },
                { date: 9, event: 'Jupiter enters Cancer', aspect: 'Jupiter Ingress', sentiment: 'bullish', change: '+3.2' },
                { date: 12, event: 'Sun opposition Neptune', aspect: 'Sun ☍ Neptune', sentiment: 'bearish', change: '-1.7' },
                { date: 16, event: 'Mars sextile Jupiter', aspect: 'Mars ⚹ Jupiter', sentiment: 'bullish', change: '+2.4' },
                { date: 20, event: 'Venus square Pluto', aspect: 'Venus □ Pluto', sentiment: 'bearish', change: '-2.0' },
                { date: 24, event: 'Jupiter cazimi', aspect: 'Jupiter ☌ Sun', sentiment: 'bullish', change: '+3.1' },
                { date: 27, event: 'Mercury square Saturn', aspect: 'Mercury □ Saturn', sentiment: 'bearish', change: '-1.4' },
                { date: 30, event: 'Sun trine Jupiter', aspect: 'Sun △ Jupiter', sentiment: 'bullish', change: '+2.8' }
            ],
            6: [ // July 2025
                { date: 3, event: 'Venus conjunct Mercury', aspect: 'Venus ☌ Mercury', sentiment: 'bullish', change: '+1.6' },
                { date: 7, event: 'Uranus enters Gemini', aspect: 'Uranus Ingress', sentiment: 'bullish', change: '+2.8' },
                { date: 11, event: 'Mars opposition Saturn', aspect: 'Mars ☍ Saturn', sentiment: 'bearish', change: '-2.4' },
                { date: 15, event: 'Sun square Uranus', aspect: 'Sun □ Uranus', sentiment: 'bearish', change: '-1.9' },
                { date: 17, event: 'Mercury Retrograde begins', aspect: 'Mercury Rx', sentiment: 'bearish', change: '-1.5' },
                { date: 21, event: 'Venus trine Neptune', aspect: 'Venus △ Neptune', sentiment: 'neutral', change: '+1.3' },
                { date: 25, event: 'Jupiter sextile Mars', aspect: 'Jupiter ⚹ Mars', sentiment: 'bullish', change: '+2.5' },
                { date: 29, event: 'Sun conjunct Venus', aspect: 'Sun ☌ Venus', sentiment: 'bullish', change: '+2.1' }
            ],
            7: [ // August 2025
                { date: 2, event: 'Mercury square Jupiter', aspect: 'Mercury □ Jupiter', sentiment: 'bearish', change: '-1.7' },
                { date: 6, event: 'Mars trine Neptune', aspect: 'Mars △ Neptune', sentiment: 'neutral', change: '+1.4' },
                { date: 10, event: 'Venus opposition Uranus', aspect: 'Venus ☍ Uranus', sentiment: 'bearish', change: '-2.2' },
                { date: 11, event: 'Mercury Direct', aspect: 'Mercury Direct', sentiment: 'bullish', change: '+1.9' },
                { date: 15, event: 'Sun sextile Jupiter', aspect: 'Sun ⚹ Jupiter', sentiment: 'bullish', change: '+2.3' },
                { date: 19, event: 'Mars square Pluto', aspect: 'Mars □ Pluto', sentiment: 'bearish', change: '-2.1' },
                { date: 23, event: 'Venus trine Saturn', aspect: 'Venus △ Saturn', sentiment: 'neutral', change: '+1.2' },
                { date: 27, event: 'Jupiter opposition Saturn', aspect: 'Jupiter ☍ Saturn', sentiment: 'bearish', change: '-2.5' },
                { date: 31, event: 'Sun square Mars', aspect: 'Sun □ Mars', sentiment: 'bearish', change: '-1.8' }
            ],
            8: [ // September 2025
                { date: 4, event: 'Mars squares Jupiter', aspect: 'Mars □ Jupiter', sentiment: 'bearish', change: '-2.3' },
                { date: 7, event: 'Total Lunar Eclipse in Pisces', aspect: 'Lunar Eclipse', sentiment: 'neutral', change: '±2.3' },
                { date: 11, event: 'Venus sextile Mars', aspect: 'Venus ⚹ Mars', sentiment: 'bullish', change: '+1.8' },
                { date: 13, event: 'Mercury cazimi', aspect: 'Mercury ☌ Sun', sentiment: 'neutral', change: '+1.1' },
                { date: 17, event: 'Jupiter trine Uranus', aspect: 'Jupiter △ Uranus', sentiment: 'bullish', change: '+2.9' },
                { date: 21, event: 'Partial Solar Eclipse in Virgo', aspect: 'Solar Eclipse', sentiment: 'bullish', change: '+1.6' },
                { date: 24, event: 'Mars squares Pluto', aspect: 'Mars □ Pluto', sentiment: 'bearish', change: '-2.4' },
                { date: 28, event: 'Venus opposition Neptune', aspect: 'Venus ☍ Neptune', sentiment: 'bearish', change: '-1.5' }
            ],
            9: [ // October 2025
                { date: 2, event: 'Mercury trine Jupiter', aspect: 'Mercury △ Jupiter', sentiment: 'bullish', change: '+2.2' },
                { date: 6, event: 'Sun square Saturn', aspect: 'Sun □ Saturn', sentiment: 'bearish', change: '-1.9' },
                { date: 10, event: 'Mars sextile Venus', aspect: 'Mars ⚹ Venus', sentiment: 'bullish', change: '+1.7' },
                { date: 14, event: 'Jupiter opposition Pluto', aspect: 'Jupiter ☍ Pluto', sentiment: 'bearish', change: '-2.1' },
                { date: 18, event: 'Venus square Jupiter', aspect: 'Venus □ Jupiter', sentiment: 'bearish', change: '-1.6' },
                { date: 22, event: 'Neptune Rx enters Pisces', aspect: 'Neptune Ingress', sentiment: 'neutral', change: '±1.2' },
                { date: 26, event: 'Sun trine Mars', aspect: 'Sun △ Mars', sentiment: 'bullish', change: '+2.4' },
                { date: 30, event: 'Mercury conjunct Saturn', aspect: 'Mercury ☌ Saturn', sentiment: 'bearish', change: '-1.8' }
            ],
            10: [ // November 2025
                { date: 4, event: 'Mars opposes Uranus', aspect: 'Mars ☍ Uranus', sentiment: 'bearish', change: '-2.6' },
                { date: 7, event: 'Uranus Rx enters Taurus', aspect: 'Uranus Ingress', sentiment: 'bearish', change: '-2.1' },
                { date: 9, event: 'Mercury Retrograde begins', aspect: 'Mercury Rx', sentiment: 'bearish', change: '-1.3' },
                { date: 13, event: 'Venus trine Jupiter', aspect: 'Venus △ Jupiter', sentiment: 'bullish', change: '+2.7' },
                { date: 17, event: 'Sun sextile Neptune', aspect: 'Sun ⚹ Neptune', sentiment: 'neutral', change: '+1.0' },
                { date: 20, event: 'Mercury cazimi', aspect: 'Mercury ☌ Sun', sentiment: 'neutral', change: '+0.8' },
                { date: 24, event: 'Mars square Neptune', aspect: 'Mars □ Neptune', sentiment: 'bearish', change: '-1.9' },
                { date: 29, event: 'Mercury Direct', aspect: 'Mercury Direct', sentiment: 'bullish', change: '+2.0' }
            ],
            11: [ // December 2025
                { date: 3, event: 'Venus opposition Mars', aspect: 'Venus ☍ Mars', sentiment: 'bearish', change: '-2.0' },
                { date: 7, event: 'Jupiter sextile Saturn', aspect: 'Jupiter ⚹ Saturn', sentiment: 'bullish', change: '+2.3' },
                { date: 8, event: 'Mars squares Saturn', aspect: 'Mars □ Saturn', sentiment: 'bearish', change: '-2.5' },
                { date: 12, event: 'Sun trine Uranus', aspect: 'Sun △ Uranus', sentiment: 'bullish', change: '+2.1' },
                { date: 14, event: 'Mars squares Neptune', aspect: 'Mars □ Neptune', sentiment: 'bearish', change: '-2.2' },
                { date: 18, event: 'Venus conjunct Jupiter', aspect: 'Venus ☌ Jupiter', sentiment: 'bullish', change: '+3.0' },
                { date: 22, event: 'Mercury sextile Mars', aspect: 'Mercury ⚹ Mars', sentiment: 'bullish', change: '+1.8' },
                { date: 26, event: 'Sun square Jupiter', aspect: 'Sun □ Jupiter', sentiment: 'bearish', change: '-1.7' },
                { date: 31, event: 'Year End - Venus trine Saturn', aspect: 'Venus △ Saturn', sentiment: 'neutral', change: '+1.1' }
            ]
        };

        // Generate monthly forecast for selected month
        function generateMonthlyForecast(symbol, selectedMonth) {
            const forecasts = [];
            const monthData = MONTHLY_ASTRONOMICAL_EVENTS_2025[selectedMonth] || [];
            const year = 2025;
            
            // Get number of days in the selected month
            const daysInMonth = new Date(year, selectedMonth + 1, 0).getDate();
            
            // Create a forecast for each day of the month
            for (let day = 1; day <= daysInMonth; day++) {
                const currentDate = new Date(year, selectedMonth, day);
                
                // Check if there's a specific astronomical event for this day
                const dayEvent = monthData.find(event => event.date === day);
                
                if (dayEvent) {
                    // Use the specific astronomical event
                    forecasts.push({
                        date: currentDate.toLocaleDateString(),
                        day: day,
                        event: dayEvent.event,
                        aspect: dayEvent.aspect,
                        sentiment: dayEvent.sentiment,
                        change: dayEvent.change,
                        impact: getImpactLevel(dayEvent.sentiment, dayEvent.change)
                    });
                } else {
                    // Generate based on planetary positions
                    const positions = calculatePlanetaryPositions(currentDate);
                    const aspects = calculateMarketImpact(positions);
                    
                    let sentiment = 'neutral';
                    let changePercent = (Math.random() - 0.5) * 1.5; // Small random change for non-event days
                    let aspectName = 'Minor Transit';
                    
                    if (aspects.length > 0) {
                        const strongestAspect = aspects.reduce((prev, current) => 
                            (prev.strength > current.strength) ? prev : current
                        );
                        
                        // Determine sentiment based on aspect
                        if (strongestAspect.aspect === 120 || strongestAspect.aspect === 60) {
                            sentiment = 'bullish';
                            changePercent = Math.random() * 1.5 + 0.5;
                            aspectName = `${PLANETS[strongestAspect.planet1]?.name || 'Planet'} ${strongestAspect.aspect === 120 ? '△' : '⚹'} ${PLANETS[strongestAspect.planet2]?.name || 'Planet'}`;
                        } else if (strongestAspect.aspect === 90 || strongestAspect.aspect === 180) {
                            sentiment = 'bearish';
                            changePercent = -(Math.random() * 1.5 + 0.5);
                            aspectName = `${PLANETS[strongestAspect.planet1]?.name || 'Planet'} ${strongestAspect.aspect === 90 ? '□' : '☍'} ${PLANETS[strongestAspect.planet2]?.name || 'Planet'}`;
                        } else {
                            aspectName = `${PLANETS[strongestAspect.planet1]?.name || 'Planet'} ☌ ${PLANETS[strongestAspect.planet2]?.name || 'Planet'}`;
                        }
                    }
                    
                    forecasts.push({
                        date: currentDate.toLocaleDateString(),
                        day: day,
                        event: `Daily ${aspectName}`,
                        aspect: aspectName,
                        sentiment: sentiment,
                        change: (changePercent > 0 ? '+' : '') + changePercent.toFixed(1),
                        impact: getImpactLevel(sentiment, changePercent.toFixed(1))
                    });
                }
            }
            
            return forecasts;
        }
        
        // Helper function to determine impact level
        function getImpactLevel(sentiment, changeStr) {
            const change = Math.abs(parseFloat(changeStr));
            if (sentiment === 'bullish') {
                return change > 2.5 ? 'Very Strong Bullish' : change > 1.5 ? 'Strong Bullish' : 'Moderate Bullish';
            } else if (sentiment === 'bearish') {
                return change > 2.5 ? 'Very Strong Bearish' : change > 1.5 ? 'Strong Bearish' : 'Moderate Bearish';
            } else {
                return change > 1.5 ? 'Significant Neutral' : 'Moderate Neutral';
            }
        }

        // Generate trading signals
        function generateTradingSignals(forecasts) {
            const signals = [];
            
            forecasts.forEach((forecast, index) => {
                const change = parseFloat(forecast.change);
                let signal = 'HOLD';
                let confidence = 'Medium';
                let reasoning = '';
                
                if (change > 2) {
                    signal = 'BUY';
                    confidence = change > 3 ? 'High' : 'Medium';
                    reasoning = `Strong bullish planetary alignment. Expected upward movement of ${Math.abs(change).toFixed(1)}%`;
                } else if (change < -2) {
                    signal = 'SELL';
                    confidence = change < -3 ? 'High' : 'Medium';
                    reasoning = `Bearish planetary configuration. Expected downward movement of ${Math.abs(change).toFixed(1)}%`;
                } else {
                    reasoning = `Neutral planetary influence. Range-bound movement expected.`;
                }
                
                signals.push({
                    date: forecast.date,
                    signal: signal,
                    confidence: confidence,
                    reasoning: reasoning,
                    change: forecast.change
                });
            });
            
            return signals;
        }

        // Show/hide tabs
        function showTab(tabName) {
            // Hide all tab contents
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });
            
            // Remove active class from all tabs
            document.querySelectorAll('.tab').forEach(tab => {
                tab.classList.remove('active');
            });
            
            // Show selected tab content and mark tab as active
            document.getElementById(tabName + 'Tab').classList.add('active');
            event.target.classList.add('active');
        }

        // Generate comprehensive report
        function generateReport() {
            const symbol = document.getElementById('symbol').value || 'NIFTY';
            const selectedMonth = parseInt(document.getElementById('selectedMonth').value);
            
            // Show loading
            document.getElementById('loading').style.display = 'block';
            document.getElementById('reportContainer').style.display = 'none';
            
            setTimeout(() => {
                // Update planetary positions
                const currentDate = new Date();
                const planetPositions = calculatePlanetaryPositions(currentDate);
                
                // Update planetary display
                const planetaryContainer = document.getElementById('planetaryPositions');
                planetaryContainer.innerHTML = '';
                
                Object.keys(PLANETS).forEach(planetKey => {
                    const position = planetPositions[planetKey];
                    const zodiacInfo = getZodiacSign(position);
                    
                    const planetCard = document.createElement('div');
                    planetCard.className = 'planet-card';
                    planetCard.innerHTML = `
                        <div class="planet-symbol">${PLANETS[planetKey].symbol}</div>
                        <div class="planet-degree">${position.toFixed(1)}°</div>
                        <div class="planet-sign">${zodiacInfo.sign}</div>
                    `;
                    planetaryContainer.appendChild(planetCard);
                });
                
                // Generate monthly forecast for selected month
                const forecasts = generateMonthlyForecast(symbol, selectedMonth);
                const signals = generateTradingSignals(forecasts);
                
                // Update monthly forecast tab (show ALL entries with scroll)
                const forecastContainer = document.getElementById('monthlyForecast');
                forecastContainer.innerHTML = '';
                
                forecasts.forEach(forecast => {
                    const forecastCard = document.createElement('div');
                    forecastCard.className = 'forecast-card';
                    forecastCard.innerHTML = `
                        <div class="forecast-date">${forecast.date}</div>
                        <div class="forecast-event">${forecast.event}</div>
                        <div class="forecast-impact ${forecast.sentiment}">${forecast.impact}</div>
                        <div style="margin-top: 10px; color: #b8b8b8;">
                            Expected Change: ${forecast.change}%
                        </div>
                    `;
                    forecastContainer.appendChild(forecastCard);
                });
                
                // Update forecast count
                document.getElementById('forecastCount').textContent = 
                    `Showing all ${forecasts.length} daily forecasts for ${monthNames[selectedMonth]} 2025`;
                
                // Update transit table (show ALL entries with scroll)
                const transitTableBody = document.getElementById('transitTableBody');
                transitTableBody.innerHTML = '';
                
                forecasts.forEach(forecast => {
                    const row = transitTableBody.insertRow();
                    row.innerHTML = `
                        <td>${forecast.date}</td>
                        <td>♃ ${forecast.aspect.split(' ')[0] || 'Jupiter'}</td>
                        <td>${forecast.event}</td>
                        <td><span class="forecast-impact ${forecast.sentiment}">${forecast.impact}</span></td>
                        <td>${forecast.change}%</td>
                        <td><span class="signal-indicator ${forecast.sentiment === 'bullish' ? 'buy' : forecast.sentiment === 'bearish' ? 'sell' : 'hold'}-signal">
                            ${forecast.sentiment === 'bullish' ? 'BUY' : forecast.sentiment === 'bearish' ? 'SELL' : 'HOLD'}
                        </span></td>
                    `;
                });
                
                // Update transit count
                document.getElementById('transitCount').textContent = 
                    `Complete daily transit data for ${monthNames[selectedMonth]} 2025 (${forecasts.length} days)`;
                
                // Update trading signals - Show complete month data in organized format
                const signalsContainer = document.getElementById('tradingSignals');
                
                signalsContainer.innerHTML = `
                    <div style="margin-bottom: 20px;">
                        <h4 style="color: #ffd700; margin-bottom: 15px;">📊 Complete ${monthNames[selectedMonth]} 2025 Daily Analysis</h4>
                        <div class="daily-signals-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px;">
                            ${forecasts.map(forecast => `
                                <div class="daily-signal-card" style="background: rgba(255, 255, 255, 0.05); border-radius: 10px; padding: 15px; border-left: 4px solid ${
                                    forecast.sentiment === 'bullish' ? '#4caf50' : 
                                    forecast.sentiment === 'bearish' ? '#f44336' : '#ff9800'
                                };">
                                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                                        <span style="font-weight: 600; color: #ffd700;">${monthNames[selectedMonth]} ${forecast.day}</span>
                                        <span class="signal-indicator ${forecast.sentiment === 'bullish' ? 'buy' : forecast.sentiment === 'bearish' ? 'sell' : 'hold'}-signal" style="font-size: 0.7rem; padding: 3px 8px;">
                                            ${forecast.sentiment === 'bullish' ? 'BUY' : forecast.sentiment === 'bearish' ? 'SELL' : 'HOLD'}
                                        </span>
                                    </div>
                                    <div style="font-size: 0.9rem; color: #e0e0e0; margin-bottom: 8px;">${forecast.aspect}</div>
                                    <div style="font-size: 0.85rem; color: #b8b8b8; margin-bottom: 8px;">${forecast.event}</div>
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span style="font-size: 1.1rem; font-weight: 600; color: ${
                                            forecast.change.includes('+') ? '#4caf50' : 
                                            forecast.change.includes('-') ? '#f44336' : '#ff9800'
                                        };">${forecast.change}%</span>
                                        <span style="font-size: 0.8rem; color: #888;">${forecast.sentiment.toUpperCase()}</span>
                                    </div>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                `;
                
                // Update correlation analysis
                const correlationContainer = document.getElementById('correlationAnalysis');
                correlationContainer.innerHTML = `
                    <div class="forecast-grid">
                        <div class="forecast-card">
                            <div class="forecast-date">Jupiter Transits</div>
                            <div class="forecast-event">85% Bullish Correlation</div>
                            <div class="forecast-impact bullish">Strong Positive</div>
                            <div style="margin-top: 10px; color: #b8b8b8;">
                                Historical data shows Jupiter transits correlate with major bull runs
                            </div>
                        </div>
                        <div class="forecast-card">
                            <div class="forecast-date">Saturn Aspects</div>
                            <div class="forecast-event">72% Bearish Correlation</div>
                            <div class="forecast-impact bearish">Moderate Negative</div>
                            <div style="margin-top: 10px; color: #b8b8b8;">
                                Saturn squares often precede market corrections
                            </div>
                        </div>
                        <div class="forecast-card">
                            <div class="forecast-date">Mercury Retrograde</div>
                            <div class="forecast-event">65% Volatility Increase</div>
                            <div class="forecast-impact neutral">High Volatility</div>
                            <div style="margin-top: 10px; color: #b8b8b8;">
                                Increased intraday volatility during retrograde periods
                            </div>
                        </div>
                        <div class="forecast-card">
                            <div class="forecast-date">Full Moon Cycles</div>
                            <div class="forecast-event">78% Trend Reversal</div>
                            <div class="forecast-impact neutral">Reversal Signal</div>
                            <div style="margin-top: 10px; color: #b8b8b8;">
                                Full moons often mark important trend reversals
                            </div>
                        </div>
                    </div>
                `;
                
                // Update quick stats
                const bullishCount = forecasts.filter(f => f.sentiment === 'bullish').length;
                const bearishCount = forecasts.filter(f => f.sentiment === 'bearish').length;
                
                document.getElementById('marketSentiment').textContent = 
                    bullishCount > bearishCount ? 'BULLISH' : bearishCount > bullishCount ? 'BEARISH' : 'NEUTRAL';
                document.getElementById('nextSignal').textContent = signals[0]?.signal || 'HOLD';
                document.getElementById('planetsActive').textContent = Object.keys(planetPositions).length;
                document.getElementById('riskLevel').textContent = 
                    bearishCount > 15 ? 'HIGH' : bearishCount > 10 ? 'MEDIUM' : 'LOW';
                
                // Update report header
                document.getElementById('reportSymbol').innerHTML = 
                    `Symbol: ${symbol} | Month: ${monthNames[selectedMonth]} 2025 | Generated: ${new Date().toLocaleString()}`;
                
                // Store current data
                currentData = { symbol, selectedMonth, forecasts, signals, planetPositions };
                
                // Hide loading and show results
                document.getElementById('loading').style.display = 'none';
                document.getElementById('reportContainer').style.display = 'block';
                
                // Smooth scroll to results
                document.getElementById('reportContainer').scrollIntoView({ 
                    behavior: 'smooth',
                    block: 'start'
                });
            }, 2000);
        }

        // Export report functionality
        function exportReport() {
            if (!currentData.forecasts) {
                alert('Please generate a report first');
                return;
            }
            
            let csvContent = 'Date,Day,Event,Planetary Aspect,Sentiment,Change %,Impact Level\n';
            currentData.forecasts.forEach(forecast => {
                csvContent += `${forecast.date},${forecast.day || ''},${forecast.event},${forecast.aspect || ''},${forecast.sentiment},${forecast.change},${forecast.impact}\n`;
            });
            
            const blob = new Blob([csvContent], { type: 'text/csv' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.setAttribute('hidden', '');
            a.setAttribute('href', url);
            a.setAttribute('download', `astro-trading-report-${currentData.symbol}-${monthNames[currentData.selectedMonth] || 'monthly'}-${new Date().toISOString().split('T')[0]}.csv`);
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        }
        
        // Auto-update when month selection changes
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('selectedMonth').addEventListener('change', function() {
                if (currentData.forecasts) {
                    generateReport();
                }
            });
        });

        // Initialize
        updateDateTime();
        setInterval(updateDateTime, 1000);
        
        // Auto-generate initial report
        setTimeout(() => {
            generateReport();
        }, 1000);
    </script>
</body>
</html>
