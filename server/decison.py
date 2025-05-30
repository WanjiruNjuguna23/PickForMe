def get_suggestion(mood, budget, time, activity):
    # Normalize input
    mood = mood.strip().lower()
    budget = budget.strip().lower()
    time = time.strip().lower()
    activity = activity.strip().lower()

    # Sample decision logic (using valid dropdown values)
    if mood == 'tired' and budget == 'low' and time == 'night' and activity == 'watch':
        return "Wind down with a relaxing documentary or nature video."

    if mood == 'romantic' and budget == 'high' and time == 'evening' and activity == 'indoor':
        return "Cook a fancy dinner together and enjoy a cozy movie night."

    if mood == 'curious' and budget == 'low' and time == 'morning' and activity == 'read':
        return "Start your day with a new blog, article, or research topic."

    if mood == 'energized' and budget == 'medium' and time == 'afternoon' and activity == 'outdoor':
        return "Go for a hike or try a new physical activity outdoors."

    if mood == 'bored' and budget == 'low' and time == 'afternoon' and activity == 'do':
        return "Try a quick DIY project or learn something random online."

    if mood == 'lonely' and budget == 'low' and time == 'evening' and activity == 'outdoor':
        return "Call a friend and meet at a park or take a walk together."

    if mood == 'happy' and budget == 'high' and time == 'evening' and activity == 'eat':
        return "Treat yourself to a fine dining experience or new restaurant."

    if mood == 'motivated' and budget == 'medium' and time == 'morning' and activity == 'do':
        return "Enroll in an online course or start a mini productivity sprint."

    if mood == 'sad' and budget == 'low' and time == 'night' and activity == 'watch':
        return "Watch a feel-good show or comedy special to boost your mood."

    if mood == 'hopeful' and budget == 'low' and time == 'morning' and activity == 'outdoor':
        return "Go for a sunrise walk or journal your goals in the fresh air."

    # Fallback if nothing matches
    return "Try doing something intentional and energizing — even a small action can lift your day!"

    
    



