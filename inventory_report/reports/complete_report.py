from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        simple_report = super().generate()
        complete_report = "Stocked products by company:\n"
        complete_report += "\n".join(
            [
                f"{company}: {value}"
                for company, value in self.companies_inventories.items()
            ]
        )
        return simple_report + complete_report + "\n"
