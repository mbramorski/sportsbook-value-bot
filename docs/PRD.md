Sportsbook Value Bot - Product Requirements Document



1\. Product Summary

An ML-augmented AI chatbot that identifies value bets by comparing sportsbook odds to model predictions. Users can ask natural-language questions about today's games and receive actionable feedback.



2\. Features

\- Scrape or fetch live odds

\- Predict match outcomes (win prob, over/under, etc.)

\- Calculate implied probability vs model prediction

\- Identify value bets

\- Query via chatbot interface



3\. Example User Questions

\- “Which bets today have the best value?”

\- “What’s your prediction for Arsenal vs Chelsea?”

\- “Do you think the Lakers will cover the spread?”

\- “Which games have sharp line movement?”

\- “What’s the model’s win % for Bayern Munich?”

\- “What’s the difference between model and book on tonight’s MLB games?”

\- “Give me over/under picks with value”

\- “What’s your confidence in Real Madrid?”

\- “Any betting trends for tonight?”

\- “Explain why this bet is +EV”



4\. Data Sources

\- \[TheOddsAPI](https://theoddsapi.com/) – live odds

\- \[football-data.co.uk](https://football-data.co.uk/) – historical match results

\- \[FBref](https://fbref.com/en/) – player/team stats

\- \[Flashscore/Sofascore] – lineups, late news (optional for future)



5\. MVP Scope

\- Odds scraper or API feed

\- Simple logistic regression or tree model for W/L prediction

\- CLI or chatbot interface to query best bets





