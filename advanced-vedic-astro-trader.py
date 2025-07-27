#!/usr/bin/env python3
"""
Advanced Astrological Trading Analysis Platform
Professional Market Analysis with Planetary Transits & Forecasting
"""

import datetime
import csv
import json
import math
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class Sentiment(Enum):
    BULLISH = "bullish"
    BEARISH = "bearish"
    NEUTRAL = "neutral"


class Signal(Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"


@dataclass
class Planet:
    symbol: str
    name: str


@dataclass
class ZodiacSign:
    name: str
    start: float


@dataclass
class AstronomicalEvent:
    date: int
    event: str
    aspect: str
    sentiment: Sentiment
    change: str


@dataclass
class Forecast:
    date: str
    day: int
    event: str
    aspect: str
    sentiment: Sentiment
    change: str
    impact: str


@dataclass
class TradingSignal:
    date: str
    signal: Signal
    confidence: str
    reasoning: str
    change: str


@dataclass
class PlanetaryPosition:
    planet: str
    degree: float
    zodiac_sign: str
    sign_degree: float


class AstrologicalTradingPlatform:
    """Main class for astrological trading analysis"""
    
    def __init__(self):
        self.planets = {
            'sun': Planet('☉', 'Sun'),
            'moon': Planet('☽', 'Moon'),
            'mercury': Planet('☿', 'Mercury'),
            'venus': Planet('♀', 'Venus'),
            'mars': Planet('♂', 'Mars'),
            'jupiter': Planet('♃', 'Jupiter'),
            'saturn': Planet('♄', 'Saturn'),
            'uranus': Planet('♅', 'Uranus'),
            'neptune': Planet('♆', 'Neptune'),
            'pluto': Planet('♇', 'Pluto')
        }
        
        self.zodiac_signs = [
            ZodiacSign("♈ Aries", 0),
            ZodiacSign("♉ Taurus", 30),
            ZodiacSign("♊ Gemini", 60),
            ZodiacSign("♋ Cancer", 90),
            ZodiacSign("♌ Leo", 120),
            ZodiacSign("♍ Virgo", 150),
            ZodiacSign("♎ Libra", 180),
            ZodiacSign("♏ Scorpio", 210),
            ZodiacSign("♐ Sagittarius", 240),
            ZodiacSign("♑ Capricorn", 270),
            ZodiacSign("♒ Aquarius", 300),
            ZodiacSign("♓ Pisces", 330)
        ]
        
        self.month_names = [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ]
        
        # Astronomical events for 2025 (converted from JavaScript)
        self.monthly_events_2025 = {
            0: [  # January 2025
                AstronomicalEvent(1, 'New Year - Mercury sextile Venus', 'Mercury ⚹ Venus', Sentiment.BULLISH, '+1.2'),
                AstronomicalEvent(3, 'Sun trine Jupiter', 'Sun △ Jupiter', Sentiment.BULLISH, '+2.1'),
                AstronomicalEvent(7, 'Venus square Mars', 'Venus □ Mars', Sentiment.BEARISH, '-1.8'),
                AstronomicalEvent(11, 'Lunar Nodes enter Pisces/Virgo', 'Nodes Ingress', Sentiment.NEUTRAL, '±0.8'),
                AstronomicalEvent(14, 'Mercury conjunct Saturn', 'Mercury ☌ Saturn', Sentiment.BEARISH, '-1.5'),
                AstronomicalEvent(18, 'Sun sextile Neptune', 'Sun ⚹ Neptune', Sentiment.NEUTRAL, '+0.9'),
                AstronomicalEvent(21, 'Mars trine Uranus', 'Mars △ Uranus', Sentiment.BULLISH, '+2.3'),
                AstronomicalEvent(25, 'Venus conjunct Jupiter', 'Venus ☌ Jupiter', Sentiment.BULLISH, '+3.1'),
                AstronomicalEvent(28, 'Mercury square Pluto', 'Mercury □ Pluto', Sentiment.BEARISH, '-2.0'),
                AstronomicalEvent(31, 'Sun opposition Mars', 'Sun ☍ Mars', Sentiment.BEARISH, '-1.7')
            ],
            1: [  # February 2025
                AstronomicalEvent(2, 'Venus trine Saturn', 'Venus △ Saturn', Sentiment.NEUTRAL, '+1.1'),
                AstronomicalEvent(5, 'Mercury sextile Jupiter', 'Mercury ⚹ Jupiter', Sentiment.BULLISH, '+1.9'),
                AstronomicalEvent(9, 'Sun square Uranus', 'Sun □ Uranus', Sentiment.BEARISH, '-2.2'),
                AstronomicalEvent(12, 'Mars conjunct Neptune', 'Mars ☌ Neptune', Sentiment.NEUTRAL, '±1.3'),
                AstronomicalEvent(16, 'Venus opposition Pluto', 'Venus ☍ Pluto', Sentiment.BEARISH, '-1.9'),
                AstronomicalEvent(19, 'Sun trine Mars', 'Sun △ Mars', Sentiment.BULLISH, '+2.4'),
                AstronomicalEvent(22, 'Mercury square Neptune', 'Mercury □ Neptune', Sentiment.BEARISH, '-1.6'),
                AstronomicalEvent(25, 'Jupiter sextile Saturn', 'Jupiter ⚹ Saturn', Sentiment.BULLISH, '+2.8'),
                AstronomicalEvent(28, 'Venus trine Uranus', 'Venus △ Uranus', Sentiment.BULLISH, '+2.1')
            ],
            2: [  # March 2025
                AstronomicalEvent(3, 'Mercury conjunct Venus', 'Mercury ☌ Venus', Sentiment.BULLISH, '+1.7'),
                AstronomicalEvent(7, 'Sun square Jupiter', 'Sun □ Jupiter', Sentiment.BEARISH, '-1.4'),
                AstronomicalEvent(11, 'Mars sextile Saturn', 'Mars ⚹ Saturn', Sentiment.NEUTRAL, '+1.0'),
                AstronomicalEvent(15, 'Venus square Uranus', 'Venus □ Uranus', Sentiment.BEARISH, '-1.8'),
                AstronomicalEvent(19, 'Sun conjunct Mercury', 'Sun ☌ Mercury', Sentiment.NEUTRAL, '+0.7'),
                AstronomicalEvent(22, 'Jupiter trine Neptune', 'Jupiter △ Neptune', Sentiment.BULLISH, '+3.2'),
                AstronomicalEvent(26, 'Mars opposition Venus', 'Mars ☍ Venus', Sentiment.BEARISH, '-2.1'),
                AstronomicalEvent(30, 'Neptune enters Aries', 'Neptune Ingress', Sentiment.BULLISH, '+2.1')
            ],
            # Adding more months for completeness
            7: [  # August 2025
                AstronomicalEvent(2, 'Mercury square Jupiter', 'Mercury □ Jupiter', Sentiment.BEARISH, '-1.7'),
                AstronomicalEvent(6, 'Mars trine Neptune', 'Mars △ Neptune', Sentiment.NEUTRAL, '+1.4'),
                AstronomicalEvent(10, 'Venus opposition Uranus', 'Venus ☍ Uranus', Sentiment.BEARISH, '-2.2'),
                AstronomicalEvent(11, 'Mercury Direct', 'Mercury Direct', Sentiment.BULLISH, '+1.9'),
                AstronomicalEvent(15, 'Sun sextile Jupiter', 'Sun ⚹ Jupiter', Sentiment.BULLISH, '+2.3'),
                AstronomicalEvent(19, 'Mars square Pluto', 'Mars □ Pluto', Sentiment.BEARISH, '-2.1'),
                AstronomicalEvent(23, 'Venus trine Saturn', 'Venus △ Saturn', Sentiment.NEUTRAL, '+1.2'),
                AstronomicalEvent(27, 'Jupiter opposition Saturn', 'Jupiter ☍ Saturn', Sentiment.BEARISH, '-2.5'),
                AstronomicalEvent(31, 'Sun square Mars', 'Sun □ Mars', Sentiment.BEARISH, '-1.8')
            ]
        }

    def calculate_planetary_positions(self, date: datetime.date) -> Dict[str, float]:
        """Calculate simplified planetary positions for given date"""
        # Calculate days since J2000.0 (January 1, 2000)
        j2000 = datetime.date(2000, 1, 1)
        days_since_j2000 = (date - j2000).days
        
        # Simplified orbital calculations (in degrees)
        positions = {
            'sun': (280.460 + 0.9856474 * days_since_j2000) % 360,
            'moon': (218.316 + 13.176396 * days_since_j2000) % 360,
            'mercury': (252.250 + 4.092317 * days_since_j2000) % 360,
            'venus': (181.979 + 1.602130 * days_since_j2000) % 360,
            'mars': (355.433 + 0.524033 * days_since_j2000) % 360,
            'jupiter': (34.351 + 0.083091 * days_since_j2000) % 360,
            'saturn': (50.077 + 0.033494 * days_since_j2000) % 360,
            'uranus': (314.055 + 0.011733 * days_since_j2000) % 360,
            'neptune': (304.348 + 0.006020 * days_since_j2000) % 360,
            'pluto': (238.958 + 0.004028 * days_since_j2000) % 360
        }
        
        return positions

    def get_zodiac_sign(self, degree: float) -> Tuple[str, float]:
        """Get zodiac sign and degree within sign for given celestial longitude"""
        normalized_degree = ((degree % 360) + 360) % 360
        
        for i in range(len(self.zodiac_signs) - 1, -1, -1):
            if normalized_degree >= self.zodiac_signs[i].start:
                sign_degree = normalized_degree - self.zodiac_signs[i].start
                return self.zodiac_signs[i].name, sign_degree
        
        # Default to Aries if no match found
        return self.zodiac_signs[0].name, normalized_degree

    def calculate_market_impact(self, planet_positions: Dict[str, float]) -> List[Dict]:
        """Calculate market impact based on planetary aspects"""
        aspects = []
        planet_names = list(planet_positions.keys())
        
        # Calculate major aspects between planets
        for i in range(len(planet_names)):
            for j in range(i + 1, len(planet_names)):
                planet1 = planet_names[i]
                planet2 = planet_names[j]
                angle = abs(planet_positions[planet1] - planet_positions[planet2])
                normalized_angle = min(angle, 360 - angle)
                
                # Major aspects: conjunction (0°), sextile (60°), square (90°), trine (120°), opposition (180°)
                major_aspects = [0, 60, 90, 120, 180]
                tolerance = 8  # degrees
                
                for aspect_angle in major_aspects:
                    if abs(normalized_angle - aspect_angle) <= tolerance:
                        strength = tolerance - abs(normalized_angle - aspect_angle)
                        aspects.append({
                            'planet1': planet1,
                            'planet2': planet2,
                            'aspect': aspect_angle,
                            'strength': strength
                        })
        
        return aspects

    def get_impact_level(self, sentiment: Sentiment, change_str: str) -> str:
        """Determine impact level based on sentiment and change percentage"""
        try:
            change = abs(float(change_str.replace('+', '').replace('±', '')))
        except (ValueError, AttributeError):
            change = 1.0
            
        if sentiment == Sentiment.BULLISH:
            if change > 2.5:
                return 'Very Strong Bullish'
            elif change > 1.5:
                return 'Strong Bullish'
            else:
                return 'Moderate Bullish'
        elif sentiment == Sentiment.BEARISH:
            if change > 2.5:
                return 'Very Strong Bearish'
            elif change > 1.5:
                return 'Strong Bearish'
            else:
                return 'Moderate Bearish'
        else:
            if change > 1.5:
                return 'Significant Neutral'
            else:
                return 'Moderate Neutral'

    def generate_monthly_forecast(self, symbol: str, year: int, month: int) -> List[Forecast]:
        """Generate monthly forecast for specified symbol and month"""
        forecasts = []
        month_data = self.monthly_events_2025.get(month, [])
        
        # Get number of days in the month
        if month == 12:
            next_month = datetime.date(year + 1, 1, 1)
        else:
            next_month = datetime.date(year, month + 2, 1)
        
        current_month = datetime.date(year, month + 1, 1)
        days_in_month = (next_month - current_month).days
        
        # Create forecast for each day
        for day in range(1, days_in_month + 1):
            current_date = datetime.date(year, month + 1, day)
            
            # Check for specific astronomical event
            day_event = next((event for event in month_data if event.date == day), None)
            
            if day_event:
                forecasts.append(Forecast(
                    date=current_date.strftime('%Y-%m-%d'),
                    day=day,
                    event=day_event.event,
                    aspect=day_event.aspect,
                    sentiment=day_event.sentiment,
                    change=day_event.change,
                    impact=self.get_impact_level(day_event.sentiment, day_event.change)
                ))
            else:
                # Generate based on planetary positions
                positions = self.calculate_planetary_positions(current_date)
                aspects = self.calculate_market_impact(positions)
                
                sentiment = Sentiment.NEUTRAL
                change_percent = (hash(str(current_date)) % 1000 - 500) / 1000 * 1.5  # Pseudo-random
                aspect_name = 'Minor Transit'
                
                if aspects:
                    strongest_aspect = max(aspects, key=lambda x: x['strength'])
                    
                    # Determine sentiment based on aspect
                    if strongest_aspect['aspect'] in [120, 60]:  # Trine or sextile
                        sentiment = Sentiment.BULLISH
                        change_percent = abs(change_percent) + 0.5
                        symbol_map = {120: '△', 60: '⚹'}
                        aspect_name = f"{self.planets[strongest_aspect['planet1']].name} {symbol_map[strongest_aspect['aspect']]} {self.planets[strongest_aspect['planet2']].name}"
                    elif strongest_aspect['aspect'] in [90, 180]:  # Square or opposition
                        sentiment = Sentiment.BEARISH
                        change_percent = -(abs(change_percent) + 0.5)
                        symbol_map = {90: '□', 180: '☍'}
                        aspect_name = f"{self.planets[strongest_aspect['planet1']].name} {symbol_map[strongest_aspect['aspect']]} {self.planets[strongest_aspect['planet2']].name}"
                    else:  # Conjunction
                        aspect_name = f"{self.planets[strongest_aspect['planet1']].name} ☌ {self.planets[strongest_aspect['planet2']].name}"
                
                change_str = f"{'+' if change_percent > 0 else ''}{change_percent:.1f}"
                
                forecasts.append(Forecast(
                    date=current_date.strftime('%Y-%m-%d'),
                    day=day,
                    event=f"Daily {aspect_name}",
                    aspect=aspect_name,
                    sentiment=sentiment,
                    change=change_str,
                    impact=self.get_impact_level(sentiment, change_str)
                ))
        
        return forecasts

    def generate_trading_signals(self, forecasts: List[Forecast]) -> List[TradingSignal]:
        """Generate trading signals based on forecasts"""
        signals = []
        
        for forecast in forecasts:
            try:
                change = float(forecast.change.replace('+', '').replace('±', ''))
            except (ValueError, AttributeError):
                change = 0
                
            signal = Signal.HOLD
            confidence = 'Medium'
            reasoning = ''
            
            if change > 2:
                signal = Signal.BUY
                confidence = 'High' if change > 3 else 'Medium'
                reasoning = f"Strong bullish planetary alignment. Expected upward movement of {abs(change):.1f}%"
            elif change < -2:
                signal = Signal.SELL
                confidence = 'High' if change < -3 else 'Medium'
                reasoning = f"Bearish planetary configuration. Expected downward movement of {abs(change):.1f}%"
            else:
                reasoning = "Neutral planetary influence. Range-bound movement expected."
            
            signals.append(TradingSignal(
                date=forecast.date,
                signal=signal,
                confidence=confidence,
                reasoning=reasoning,
                change=forecast.change
            ))
        
        return signals

    def get_planetary_positions_display(self, date: datetime.date) -> List[PlanetaryPosition]:
        """Get current planetary positions for display"""
        positions = self.calculate_planetary_positions(date)
        display_positions = []
        
        for planet_key, degree in positions.items():
            zodiac_sign, sign_degree = self.get_zodiac_sign(degree)
            display_positions.append(PlanetaryPosition(
                planet=self.planets[planet_key].name,
                degree=degree,
                zodiac_sign=zodiac_sign,
                sign_degree=sign_degree
            ))
        
        return display_positions

    def generate_report(self, symbol: str = 'NIFTY', year: int = 2025, month: int = 7) -> Dict:
        """Generate comprehensive astrological trading report"""
        current_date = datetime.date.today()
        
        # Generate forecasts and signals
        forecasts = self.generate_monthly_forecast(symbol, year, month)
        signals = self.generate_trading_signals(forecasts)
        
        # Get planetary positions
        planetary_positions = self.get_planetary_positions_display(current_date)
        
        # Calculate statistics
        bullish_count = sum(1 for f in forecasts if f.sentiment == Sentiment.BULLISH)
        bearish_count = sum(1 for f in forecasts if f.sentiment == Sentiment.BEARISH)
        
        market_sentiment = 'BULLISH' if bullish_count > bearish_count else 'BEARISH' if bearish_count > bullish_count else 'NEUTRAL'
        risk_level = 'HIGH' if bearish_count > 15 else 'MEDIUM' if bearish_count > 10 else 'LOW'
        
        report = {
            'symbol': symbol,
            'month': self.month_names[month],
            'year': year,
            'generated_date': current_date.isoformat(),
            'market_sentiment': market_sentiment,
            'risk_level': risk_level,
            'active_transits': len(planetary_positions),
            'forecasts': forecasts,
            'signals': signals,
            'planetary_positions': planetary_positions,
            'statistics': {
                'total_days': len(forecasts),
                'bullish_days': bullish_count,
                'bearish_days': bearish_count,
                'neutral_days': len(forecasts) - bullish_count - bearish_count
            }
        }
        
        return report

    def export_to_csv(self, report: Dict, filename: Optional[str] = None) -> str:
        """Export report to CSV file"""
        if filename is None:
            filename = f"astro_trading_report_{report['symbol']}_{report['month']}_{report['year']}.csv"
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Date', 'Day', 'Event', 'Planetary_Aspect', 'Sentiment', 'Change_%', 'Impact_Level']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for forecast in report['forecasts']:
                writer.writerow({
                    'Date': forecast.date,
                    'Day': forecast.day,
                    'Event': forecast.event,
                    'Planetary_Aspect': forecast.aspect,
                    'Sentiment': forecast.sentiment.value,
                    'Change_%': forecast.change,
                    'Impact_Level': forecast.impact
                })
        
        return filename

    def print_report(self, report: Dict):
        """Print formatted report to console"""
        print("=" * 80)
        print(f"🌟 ADVANCED ASTROLOGICAL TRADING ANALYSIS REPORT")
        print("=" * 80)
        print(f"Symbol: {report['symbol']}")
        print(f"Period: {report['month']} {report['year']}")
        print(f"Generated: {report['generated_date']}")
        print(f"Market Sentiment: {report['market_sentiment']}")
        print(f"Risk Level: {report['risk_level']}")
        print(f"Active Transits: {report['active_transits']}")
        print()
        
        print("📊 MONTHLY STATISTICS")
        print("-" * 40)
        stats = report['statistics']
        print(f"Total Days: {stats['total_days']}")
        print(f"Bullish Days: {stats['bullish_days']}")
        print(f"Bearish Days: {stats['bearish_days']}")
        print(f"Neutral Days: {stats['neutral_days']}")
        print()
        
        print("🌙 CURRENT PLANETARY POSITIONS")
        print("-" * 40)
        for pos in report['planetary_positions'][:5]:  # Show first 5
            print(f"{pos.planet}: {pos.degree:.1f}° in {pos.zodiac_sign}")
        print()
        
        print("🔮 MONTHLY FORECAST HIGHLIGHTS")
        print("-" * 40)
        # Show significant events
        significant_forecasts = [f for f in report['forecasts'] 
                               if abs(float(f.change.replace('+', '').replace('±', '').replace('-', ''))) > 2.0]
        
        for forecast in significant_forecasts[:10]:  # Show top 10
            sentiment_symbol = "📈" if forecast.sentiment == Sentiment.BULLISH else "📉" if forecast.sentiment == Sentiment.BEARISH else "➡️"
            print(f"{sentiment_symbol} {forecast.date}: {forecast.event} ({forecast.change}%)")
        
        print("\n" + "=" * 80)


def main():
    """Main function to demonstrate the platform"""
    platform = AstrologicalTradingPlatform()
    
    print("🌟 Welcome to the Advanced Astrological Trading Analysis Platform")
    print()
    
    # Interactive menu
    while True:
        print("\nChoose an option:")
        print("1. Generate Monthly Report")
        print("2. View Current Planetary Positions")
        print("3. Export Report to CSV")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            symbol = input("Enter symbol (default: NIFTY): ").strip() or 'NIFTY'
            year = int(input("Enter year (default: 2025): ").strip() or '2025')
            month = int(input("Enter month (0-11, default: 7 for August): ").strip() or '7')
            
            print("\n📊 Generating report...")
            report = platform.generate_report(symbol, year, month)
            platform.print_report(report)
            
        elif choice == '2':
            current_date = datetime.date.today()
            positions = platform.get_planetary_positions_display(current_date)
            
            print(f"\n🌙 Current Planetary Positions ({current_date})")
            print("-" * 50)
            for pos in positions:
                print(f"{pos.planet}: {pos.degree:.1f}° in {pos.zodiac_sign} ({pos.sign_degree:.1f}°)")
            
        elif choice == '3':
            symbol = input("Enter symbol (default: NIFTY): ").strip() or 'NIFTY'
            year = int(input("Enter year (default: 2025): ").strip() or '2025')
            month = int(input("Enter month (0-11, default: 7 for August): ").strip() or '7')
            
            report = platform.generate_report(symbol, year, month)
            filename = platform.export_to_csv(report)
            print(f"\n✅ Report exported to: {filename}")
            
        elif choice == '4':
            print("\n🌟 Thank you for using the Astrological Trading Platform!")
            break
        
        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
