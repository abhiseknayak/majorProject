# majorProject

Title of the project: Fuzzy rule based time series analysis.

Intution: ARIMA, LSTM are some known tools. But here we try to predict sequetial values based on fuzzy logic.

Approach: First we divide our data into overlapping classes. Genrate rules. For new values through that rules determine news values. 

What's New: 
1. The method isn't used for oil-prices and various commodities. 
2. Tested with different partition method, different fuzzy and defuzzy approaches.
3. Generated rules for each feature and combined as master feature rule. 
   Say, rules generated for feature A as rule r(A) and feature B as r(B) associated together as r(AB). 

Reference: https://pypi.org/project/pyFTS/

Android App:

Current Android App is prototype showing predicted graph for oil price of a certain region based on mobile location.

Plan to apply the same for multiple entities that can provide rough estimates of the expenses near you.

Objective: Helpful for tourists, re-location.
