# Regression Analysis on Car Auction to find out factor that affect Total revenue 

## Overview

This repository contains the code and results of regression analyses performed on a dataset related to earnings/revenue percentage and employee turnover in a specific context. The analysis aims to understand the impact of various factors on these key business metrics.

## Regression Models

### First Regression: Predicting Earnings/Revenue Percentage

- **Model Summary:**
  - Dependent Variable: Percentage of earnings/revenue
  - Independent Variables: Legacy, Sold, Ftturn, Ptturn, Ohsapercar, Lotdampercar
  - R-squared: 47.3%
  - F-statistic: 10.02 (p-value: 7.04e-08)

- **Findings:**
  - Legacy and Sold are not statistically significant.
  - Ftturn is significant (p-value: 0.001), indicating a negative impact on earnings/revenue.
  - Ohsapercar and Lotdampercar are significant (p-values: 0.031 and 0.000, respectively), with negative impacts.

### Second Regression: Full-Time Employee Turnover Percentage

- **Model Summary:**
  - Dependent Variable: Ftturn (Full-Time Employee Turnover Percentage)
  - Independent Variables: Ei (Employee Incentives), Oc (Occupational Accidents per 1000 Cars)
  - R-squared: 25.7%
  - F-statistic: 12.27 (p-value: 2.66e-05)

- **Findings:**
  - Both Ei and Oc are statistically significant (p-values < 0.05).
  - Ei is associated with a decrease, and Oc is associated with an increase in Ftturn.

### Third Regression: General Model Summary

- **Model 1:**
  - Dependent Variable: Ftturn
  - R-squared: 25.7%
  - Adjusted R-squared: 23.6%
  - F-statistic: 2.66e-05

- **Model 2:**
  - Dependent Variable: Ohsapercar
  - R-squared: 5.6%
  - Adjusted R-squared: 2.9%
  - F-statistic: 0.13

- **Findings:**
  - Model 1 is statistically significant, but Model 2 is not.

### Fourth Regression: Predicting Different Dependent Variables

- **Ftturn Model:**
  - R-squared: 25.7%, Ei and Oc are significant.

- **Ohsapercar Model:**
  - R-squared: 5.6%, Ei and constant are significant.

- **Lotdampercar Model:**
  - R-squared: 25.8%, Ei and Oc are significant.

## Usage

1. Clone the repository.
2. Explore the Jupyter notebooks containing regression code and analyses.
3. Adapt the code for your own dataset or extend the analysis.

## Conclusion

The regression analyses conducted on the provided dataset offer valuable insights into the factors influencing earnings/revenue percentage and employee turnover in the specified context. Here are the key takeaways:

1. **Earnings/Revenue Percentage Prediction:**
   - The model shows a moderate explanatory power (R-squared: 47.3%).
   - Full-time employee turnover (Ftturn) has a significant negative impact on earnings/revenue, emphasizing the importance of employee retention.
   - Factors like OSHA claims per 1000 cars (Ohsapercar) and lot damage per car (Lotdampercar) also significantly influence earnings/revenue, with negative associations.

2. **Employee Turnover Analysis:**
   - The model predicting full-time employee turnover percentage (Ftturn) indicates that both employee incentives (Ei) and occupational accidents per 1000 cars (Oc) significantly affect turnover.
   - Employee incentives are associated with a decrease in turnover, while occupational accidents per 1000 cars are linked to an increase in turnover.

3. **General Observations:**
   - The third regression model suggests that the overall impact of the independent variables may vary based on the dependent variable.
   - Model 1 (Ftturn) is statistically significant, whereas Model 2 (Ohsapercar) lacks significance.
   - It's crucial to consider the context and specific variables when interpreting regression results.

4. **Model Applicability:**
   - The provided Jupyter notebooks and code can serve as a foundation for further analysis on similar datasets.
   - Users are encouraged to adapt the code, explore additional variables, and extend the analysis to gain deeper insights into their specific business context.
