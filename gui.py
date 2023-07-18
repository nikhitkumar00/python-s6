from breezypythongui import EasyFrame


class TaxCodeDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Tax Calculator")

        self.addLabel(text="Income", row=0, column=0)
        self.incomeField = self.addFloatField(value=0.0, row=0, column=1)

        self.addLabel(text="Dependents", row=1, column=0)
        self.depField = self.addIntegerField(value=0, row=1, column=1)

        self.addLabel(text="Exemption amount", row=2, column=0)
        self.exeField = self.addFloatField(value=0.0, row=2, column=1)

        self.addButton(
            text="Compute", row=3, column=0, columnspan=2, command=self.computeTax
        )

        self.addLabel(text="Total tax", row=4, column=0)
        self.taxField = self.addFloatField(value=0.0, row=4, column=1, precision=2)

    def computeTax(self):
        income = self.incomeField.getNumber()
        numDependents = self.depField.getNumber()
        exemptionAmount = self.exeField.getNumber()

        tax = (income - numDependents * exemptionAmount) * 0.15

        self.taxField.setNumber(tax)


TaxCodeDemo().mainloop()
