class ValuationConfidenceCalculator:

    def __init__(self, announced, verified, turnover, stake, employees):
        self.announced = announced
        self.verified = verified
        self.turnover = turnover
        self.stake = stake
        self.employees = employees

        self.score = 50
        self.reasons = []
        self.warnings = []


    def calculate(self):

        # Announced vs Verified valuation

        difference = 100 - (
            min(self.announced, self.verified) /
            max(self.announced, self.verified)
            * 100
        )


        if difference <= 15:
            self.score += 15
            self.reasons.append(
                "Verified and announced valuations are close."
            )

        elif difference > 50:
            self.score -= 20
            self.warnings.append(
                "Verified and announced valuation amounts differ significantly."
            )


        # Turnover check

        if self.verified > self.turnover:
            self.score += 5
            self.reasons.append(
                "Valuation is higher than turnover."
            )


        elif self.verified < self.turnover * 0.2:
            self.score -= 15
            self.warnings.append(
                "Valuation appears inconsistent with turnover."
            )


        # Stake check

        if self.stake >= 0.5:
            self.score += 5
            self.reasons.append(
                "Fundraising stake is reliable."
            )

        else:
            self.score -= 15
            self.warnings.append(
                "Stake taken is below 0.5%, reducing reliability."
            )


        # Employee check

        if self.employees >= 500:
            self.score += 15
            self.reasons.append(
                "Company has 500+ employees."
            )

        elif self.employees >= 50:
            self.score += 7
            self.reasons.append(
                "Company has medium employee count."
            )


        self.score = max(0, min(100, self.score))


        if self.score >= 75:
            rating = "High 🥇"

        elif self.score >= 50:
            rating = "Medium 🥈"

        elif self.score >= 25:
            rating = "Low 🥉"

        else:
            rating = "Hidden ⚫"


        return {
            "rating": rating,
            "score": self.score,
            "reasons": self.reasons,
            "warnings": self.warnings
        }
