def average_industry_profit_margins():
    return """SELECT DISTINCT industry, AVG(100*EBITDA/revenue) OVER (PARTITION BY industry)
                AS  avg_profit_margin FROM dow_jones
                ORDER BY industry;"""

def profit_margin_cte():
    return """WITH profit_margin AS
                (SELECT company, (100*EBITDA/revenue) AS
                comp_profit_margin FROM dow_jones WHERE ebitda > 0)
                SELECT * FROM profit_margin
                ORDER BY comp_profit_margin DESC;"""

def five_most_levered_capital_structures():
    return """SELECT company, (100*debt/enterprise_value) AS
                debt_to_ev FROM dow_jones
                ORDER BY debt_to_ev DESC LIMIT 5;"""

def riskier_than_average_cos():
    return """WITH riskier_than_avg AS
            (SELECT symbol, (100*debt/enterprise_value) AS
            debt_to_ev, AVG(100*debt/enterprise_value) OVER (PARTITION BY industry) AS
            avg_debt_to_ev FROM dow_jones)
            SELECT symbol FROM riskier_than_avg WHERE debt_to_ev > avg_debt_to_ev;"""

def pharma_cos_with_above_average_roi():
    return """WITH pharma_cos_above_avg AS
            (SELECT company, (100*EBITDA/enterprise_value) AS roi,
            AVG(100*EBITDA/enterprise_value) OVER (PARTITION BY industry) AS avg_pharma_roi
            FROM dow_jones WHERE industry = 'Pharmaceuticals')
            SELECT * FROM pharma_cos_above_avg WHERE roi > avg_pharma_roi;"""
