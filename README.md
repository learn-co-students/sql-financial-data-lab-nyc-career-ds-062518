
# Dow Jones Industrials Lab

In this lab we will be calculating financial metrics using data from the constituents of the Dow Jones Industrial Average index!  We will write Window Functions and Common Table Expressions to study the financial well-being of the companies making up the index.  We will study different metrics and assess companies against their industry average metrics.

![dow_logo](https://upload.wikimedia.org/wikipedia/commons/c/c8/DJIA_historical_graph_to_jul11_%28log%29.svg)

## Objectives

1.  Write further queries using Window Functions and Common Table Expressions
2.  Write Window Functions in conjunction with Common Table Expressions to make more powerful queries


## Index Data

The `dow_jones` table contains a variety of information about each company in the DJIA index.  The table include each company name, the exchange where its stock is traded, its ticker symbol, its industry, the date it was added to the index and several financial statistics like enterprise value, debt, revenue, and EBITDA.  All financial metrics are in billions of dollars.

Write your queries inside a "triple quotation mark" string inside the `queries.py` file to get the tests to pass.  A table sample of the first six companies is provided below for your reference.

`dow_jones`:

company         |exchange|symbol|industry|date_added|notes|enterprise_value|debt|revenue|ebitda
----------------|--------|------|--------|----------|-----|----------------|----|-------|-------
3M              |NYSE  |MMM |Conglomerate    |1976-08-09|as Minnesota Mining and Manufacturing|133.31|15.68|32.25|8.09
American Express|NYSE  |AXP |Consumer finance                 |1982-08-30||98.08|38.13|55.82|14.15
Apple           |NASDAQ|AAPL|Consumer electronics             |2015-03-19||954.8|121.84|247.42|76.38
Boeing          |NYSE  |BA  |Aerospace and defense            |1987-03-12||196.37|11.12|93.39|12.12
Caterpillar     |NYSE  |CAT |Construction and mining equipment|1991-05-06||118.42|34.88|45.46|8.45
Chevron         |NYSE  |CVX |Oil & gas             |2008-02-19|also 1930-07-18 to 1999-11-01|264.51|38.76|127.49|21.87


## Queries


#### Average Industry Profit Margins

Our first task is to calculate the average profit margin for each of the ten industries found in the database.  EBITDA, or Earnings Before Interest, Taxes, Depreciation, and Amortization, is the proxy we will use for profits.  We can calculate a company's profit margin by dividing its EBITDA by its revenue and multiplying by 100 to turn the resulting figure into a percentage.

> profit margin = $100*\frac{EBITDA}{revenue}$

The `average_industry_profit_margins` query should contain a Window Function that returns the industries and their respective average profit margins.  The resulting dataset should be ordered alphabetically by industry name.  Use the `DISTINCT` keyword to eliminate the duplicate rows returned by the Window Function.

#### Company Profit Margins

The `profit_margin_cte` should contain a CTE that returns: 1) the company name, and 2) its respective profit margin.  Use the same formula for calculating profit margin.

The resulting dataset should be ordered by profit margin from highest to lowest.

#### Capital Structures

We will study company capital structures in the following query.  In particular, we will determine how much of the value of a company comes from its total debt by dividing each company's debt by its enterprise value.  Again, we will multiple by 100 to turn this result into a percentage.

> debt-to-EV ratio = $100*\frac{debt}{enterprise value}$

The `five_most_levered_capital_structures` query should return 1) the company name, and 2) its respective debt-to-EV ratio.  The query should return the five companies with the most leveraged capital structures, ordered from highest to lowest.

#### Capital Structures vs. the Industry Average

Is it fair to compare company capital structures regardless of their industry?  Probably not.  Companies in certain industries ought to have more debt than companies in others.  After all, it is probably a good thing for a cable company with steady, predictable, and recurring cash flows to have a lot of debt.  A teen retailer, however, has a fickle consumer base and highly variable input prices.  It is probably not a good idea for the teen retailer to have a lot of debt.  Our previous query may be faulty for these reasons.

Let's make an apples to apples comparison by looking at company capital structures as compared to their industry's average.

The `test_riskier_than_average_cos` query should contain a CTE that returns 1) the company's symbol, 2) the company's debt-to EV ratio, and 3) the industry average debt-to-EV ratio (calculate this average value with a Window Function).

From this CTE, the query should the symbol of the companies whose debt-to-EV ratio is above the average ratio for that industry.

#### Return on Investment

In the final query, `tech_cos_with_above_average_roi`, we will study a company's return on investment.  The formula for ROI is as follows:

> return on investment = $100*\frac{EBITDA}{enterprise value}$


The query should contain a CTE that looks at technology companies.  The CTE should 1) select the company's name, 2) calculate the company's ROI, and 3) calculate the tech industry's average ROI.

The overall query should return all rows from the CTE where the company's ROI is greater than the tech industry's ROI.
