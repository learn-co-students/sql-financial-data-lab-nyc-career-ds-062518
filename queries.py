def average_industry_profit_margins():
    return """SELECT DISTINCT industry, AVG(ebitda/revenue*100)
                OVER(PARTITION BY industry)
                FROM dow_jones
                ORDER BY industry;"""

def profit_margin_cte():
    return """WITH profit_margin_cte AS
                (SELECT company, revenue, ebitda from dow_jones WHERE ebitda != 0)
                SELECT company, ebitda/revenue*100 AS profit_margin from profit_margin_cte
                ORDER BY profit_margin DESC, company;"""

def five_most_levered_capital_structures():
    return """WITH cap_struct AS
                (SELECT company, debt, enterprise_value from dow_jones)
                SELECT company, debt/enterprise_value*100 AS debt_EV from cap_struct
                ORDER BY debt_EV DESC, company
                LIMIT 5;"""

def riskier_than_average_cos():
    return """WITH CTE AS
                (SELECT symbol, debt/enterprise_value*100 AS debt_EV, avg(debt/enterprise_value*100)
                OVER(PARTITION BY industry) AS ind_avg from dow_jones)
                SELECT symbol FROM CTE
                WHERE debt_EV > ind_avg;"""

def pharma_cos_with_above_average_roi():
    return """WITH CTE AS
                (SELECT company, ebitda/enterprise_value*100 AS comp_roi, avg(ebitda/enterprise_value*100)
                OVER(PARTITION BY industry) AS ind_roi from dow_jones WHERE industry = 'Pharmaceuticals')
                SELECT * FROM CTE
                WHERE comp_roi > ind_roi;"""
