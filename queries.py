def average_industry_profit_margins():
    return """SELECT DISTINCT industry, AVG(ebitda / revenue * 100) OVER(PARTITION BY industry)
    as margin from dow_jones ORDER BY industry ASC;"""

def profit_margin_cte():
    return """WITH profit_margin_cte AS (SELECT company, ebitda / revenue * 100 as margin from dow_jones ORDER BY margin DESC)
    SELECT * from profit_margin_cte WHERE margin > 0;"""

def five_most_levered_capital_structures():
    return """SELECT company, ((debt/enterprise_value)*100) AS debt_ev_ratio FROM dow_jones
    ORDER BY debt_ev_ratio DESC LIMIT 5;"""

def riskier_than_average_cos():
    return """WITH test_riskier_than_average AS(SELECT symbol, ((debt/enterprise_value)*100)
    AS debt_ev_ratio, AVG((debt/enterprise_value)*100) OVER(PARTITION BY industry) AS avg_debt_ev_ratio FROM dow_jones ORDER BY debt_ev_ratio DESC)
    SELECT symbol FROM test_riskier_than_average WHERE debt_ev_ratio > avg_debt_ev_ratio;"""

def pharma_cos_with_above_average_roi():
    return """WITH tech_cos_with_above_average_roi
    AS(SELECT company,((ebitda/enterprise_value)*100)
    AS roi,AVG((ebitda/enterprise_value)*100)
    OVER(PARTITION BY industry) AS avg_roi FROM dow_jones WHERE industry LIKE 'Pharmaceuticals')
    SELECT * FROM tech_cos_with_above_average_roi WHERE roi > avg_roi;"""
