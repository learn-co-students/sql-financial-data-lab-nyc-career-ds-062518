def average_industry_profit_margins():
    return """SELECT DISTINCT industry, AVG(100*ebitda/revenue) OVER (PARTITION BY industry) AS avg_profit_margin
            FROM dow_jones ORDER BY industry;"""

def profit_margin_cte():
    return """WITH CTE AS
            (
            SELECT company, (ebitda/revenue)*100 AS profit_margin FROM dow_jones WHERE ebitda IS NOT NULL
            )
            SELECT * FROM CTE ORDER BY profit_margin DESC;"""

def five_most_levered_capital_structures():
    return """WITH CTE AS
            (
            SELECT company, (100*debt/enterprise_value) AS debt_to_ev FROM dow_jones
            )
            SELECT * FROM CTE ORDER BY debt_to_ev DESC LIMIT 5;"""

def riskier_than_average_cos():
    return """WITH CTE AS
            (
            SELECT symbol,
            (debt/enterprise_value) AS co_debt_to_ev,
            AVG(debt/enterprise_value) OVER (PARTITION BY industry) AS industry_debt_to_ev
            FROM dow_jones
            )
            SELECT symbol FROM CTE WHERE co_debt_to_ev > industry_debt_to_ev;"""

def tech_cos_with_above_average_roi():
    return """WITH CTE AS
            (
            SELECT company,
            (ebitda/enterprise_value)*100 AS company_roi,
            AVG((ebitda/enterprise_value)*100) OVER (PARTITION BY industry) AS industry_roi
            FROM dow_jones WHERE industry = 'Technology'
            )
            SELECT * FROM CTE WHERE company_roi > industry_roi;"""
