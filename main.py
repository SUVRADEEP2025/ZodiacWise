def get_zodiac_sign(month, day):
    """
    Calculate zodiac sign based on birth month and day.
    
    Args:
        month (int): Month as number (1-12)
        day (int): Day of the month (1-31)
        
    Returns:
        str: Zodiac sign name
    """
    # Validate input
    if not 1 <= month <= 12:
        return "Invalid month. Please enter a number between 1 and 12."
    if not 1 <= day <= 31:
        return "Invalid day. Please enter a number between 1 and 31."
    
    # Check for months with fewer days
    if month == 2 and day > 29:
        return "Invalid date for February."
    if month in [4, 6, 9, 11] and day > 30:
        return "Invalid date for this month."
    
    # Define zodiac sign date ranges
    if (month == 1 and 1 <= day <= 19) or (month == 12 and 22 <= day <= 31):
        return "Capricorn"
    elif (month == 1 and 20 <= day <= 31) or (month == 2 and 1 <= day <= 18):
        return "Aquarius"
    elif (month == 2 and 19 <= day <= 29) or (month == 3 and 1 <= day <= 20):
        return "Pisces"
    elif (month == 3 and 21 <= day <= 31) or (month == 4 and 1 <= day <= 19):
        return "Aries"
    elif (month == 4 and 20 <= day <= 30) or (month == 5 and 1 <= day <= 20):
        return "Taurus"
    elif (month == 5 and 21 <= day <= 31) or (month == 6 and 1 <= day <= 20):
        return "Gemini"
    elif (month == 6 and 21 <= day <= 30) or (month == 7 and 1 <= day <= 22):
        return "Cancer"
    elif (month == 7 and 23 <= day <= 31) or (month == 8 and 1 <= day <= 22):
        return "Leo"
    elif (month == 8 and 23 <= day <= 31) or (month == 9 and 1 <= day <= 22):
        return "Virgo"
    elif (month == 9 and 23 <= day <= 30) or (month == 10 and 1 <= day <= 22):
        return "Libra"
    elif (month == 10 and 23 <= day <= 31) or (month == 11 and 1 <= day <= 21):
        return "Scorpio"
    elif (month == 11 and 22 <= day <= 30) or (month == 12 and 1 <= day <= 21):
        return "Sagittarius"
    else:
        return "Invalid date combination."

def get_zodiac_sign_from_string(date_str):
    """
    Calculate zodiac sign from a date string in format MM/DD or Month Day
    
    Args:
        date_str (str): Date string (e.g., "1/15", "January 15", "15 January")
        
    Returns:
        str: Zodiac sign name
    """
    import re
    
    # Try to parse MM/DD format
    if re.match(r'^\d{1,2}/\d{1,2}$', date_str):
        month, day = map(int, date_str.split('/'))
        return get_zodiac_sign(month, day)
    
    # Try to parse Month Day format
    month_names = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
        'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
    }
    
    # Convert to lowercase and split
    parts = date_str.lower().split()
    
    # Format: "January 15" or "15 January"
    if len(parts) == 2:
        if parts[0].isdigit():
            # Format: "15 January"
            day = int(parts[0])
            month_name = parts[1]
            month = month_names.get(month_name, 0)
        else:
            # Format: "January 15"
            month_name = parts[0]
            day = int(parts[1])
            month = month_names.get(month_name, 0)
        
        if month == 0:
            return "Invalid month name. Please use full month name (e.g., January, February)."
        
        return get_zodiac_sign(month, day)
    
    return "Invalid date format. Please use MM/DD or 'Month Day' format (e.g., '1/15' or 'January 15')."

def main():
    """Main function to interact with user"""
    print("Zodiac Sign Calculator")
    print("=====================")
    print("Enter your birth date in one of these formats:")
    print("- MM/DD (e.g., 1/15 for January 15th)")
    print("- Month Day (e.g., January 15)")
    print("- Day Month (e.g., 15 January)")
    print()
    
    while True:
        user_input = input("Enter your birth date (or 'quit' to exit): ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        result = get_zodiac_sign_from_string(user_input)
        
        if "Invalid" in result:
            print(f"❌ {result}")
        else:
            print(f"✨ Your zodiac sign is: {result}")
            print(f"   Based on date: {user_input}")
        
        print()  # Empty line for readability

# Run with example inputs if executed directly
if __name__ == "__main__":
    # Example usage
    test_dates = [
        (1, 15),    # Capricorn
        (1, 25),    # Aquarius
        (2, 20),    # Pisces
        (3, 22),    # Aries
        (4, 21),    # Taurus
        (5, 25),    # Gemini
        (6, 25),    # Cancer
        (7, 25),    # Leo
        (8, 25),    # Virgo
        (9, 25),    # Libra
        (10, 25),   # Scorpio
        (11, 25),   # Sagittarius
        (12, 25),   # Capricorn
    ]
    
    print("=== Example Results ===")
    for month, day in test_dates:
        sign = get_zodiac_sign(month, day)
        month_names = ["January", "February", "March", "April", "May", "June", 
                      "July", "August", "September", "October", "November", "December"]
        print(f"{month_names[month-1]} {day}: {sign}")
    
    print("\n" + "="*50)
    print("Now try your own birthday!")
    print("="*50 + "\n")
    
    # Start interactive mode
    main()
