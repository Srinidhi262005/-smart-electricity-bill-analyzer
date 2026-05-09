"""
Suggestion Service
Provides intelligent energy-saving tips based on consumption brackets and detected anomalies.
"""


def generate_suggestions(units, anomaly_report=None):
    """
    Generates energy-saving recommendations based on usage and patterns.
    
    :param units: Current month unit consumption (float)
    :param anomaly_report: Dict containing results from detect_abnormal_usage (optional)
    :return: List of strings containing actionable advice
    """
    units = float(units)
    suggestions = []

    # Consumption-based recommendations
    if units <= 75:
        suggestions.append('✓ Excellent: Your consumption is very low. Keep maintaining your efficient habits.')
        suggestions.append('Continue monitoring for sudden changes that could indicate appliance faults.')
    elif units <= 150:
        suggestions.append('→ Good: Your consumption is within an efficient range. Small optimizations can help.')
        suggestions.append('Focus on turning off lights in unused rooms and unplugging chargers when not in use.')
    elif units <= 250:
        suggestions.append('⚠ Moderate: Your consumption is average. Consider shifting high-load tasks to off-peak hours.')
        suggestions.append('Run washing machines, dishwashers, and water heaters during late evening or early morning if possible.')
        suggestions.append('Check if your AC unit is set to 24-26°C; every degree higher saves 3-5% energy.')
    elif units <= 350:
        suggestions.append('⚠ High: Your consumption is above average. Immediate action needed for cost savings.')
        suggestions.append('Identify and unplug phantom loads (chargers, standby power, idle devices consuming 5-10W each).')
        suggestions.append('Upgrade to ENERGY STAR refrigerators, washing machines, or AC units to cut usage by 20-40%.')
    else:
        suggestions.append('🔴 Very High: Your consumption is significantly above average. Emergency review recommended.')
        suggestions.append('Audit your AC usage - it likely accounts for 40-60% of your bill. Consider servicing or replacing old units.')
        suggestions.append('Install a smart power strip to eliminate phantom power draw from entertainment systems.')
        suggestions.append('Consider solar panels or a backup generator for off-peak hours if feasible.')

    # Anomaly-specific recommendations
    if anomaly_report:
        if anomaly_report.get('abnormal'):
            patterns = anomaly_report.get('pattern', [])
            
            if any('spike' in p.lower() for p in patterns):
                suggestions.append('→ Spike detected: Check for failing refrigerators, water heater thermostat issues, or AC compressor problems.')
                suggestions.append('Have an electrician inspect high-wattage appliances like water heaters or AC units.')
            
            if any('consecutive increases' in p.lower() for p in patterns):
                suggestions.append('→ Trending up: Usage is increasing month-over-month. Identify the cause before it becomes permanent.')
                suggestions.append('Review recent appliance additions, AC usage increase, or broken weatherstripping around doors/windows.')
            
            if any('significantly above average' in p.lower() for p in patterns):
                suggestions.append('→ Sustained high usage: This is not a spike but a new baseline. Permanent changes may be needed.')
                suggestions.append('Conduct a full home energy audit to identify the source of excess consumption.')

    # Time-based and appliance-specific advice
    if units > 150:
        suggestions.append('💡 Appliance tips: Replace incandescent bulbs with LED (80% less energy), unplug devices when not in use.')
        suggestions.append('→ Thermostat: Program your AC to higher temperatures during peak hours (noon-6 PM) to save 5-15%.')
        suggestions.append('→ Water heater: Lower temperature to 49°C (120°F) and insulate the tank to reduce standby losses.')
    
    if units > 200:
        suggestions.append('→ Heavy appliances: If you have electric cooking, use pressure cookers instead of regular ovens (70% faster).')
        suggestions.append('→ Lighting: Motion sensors in bathrooms and hallways can cut lighting costs by 30%.')
        suggestions.append('→ Ventilation: Use ceiling fans (very low power) instead of AC when possible; feel 3-4°C cooler.')

    # General monitoring advice
    suggestions.append('📊 Track your meter reading weekly to catch spikes early and correlate with weather, events, or new appliance usage.')
    suggestions.append('Compare your bill with neighbors (similar house size) to benchmark if your consumption is typical.')
    
    return suggestions
