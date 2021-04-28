from fpdf import FPDF


class Bill:
    """
    Data of a bill such as amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Flatmate that share the bill base on the period of living in the flat.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate):
        weight = self.days_in_house / (self.days_in_house + flatmate.days_in_house)
        to_pay = weight * bill.amount
        return to_pay


class PdfReport:
    """
    Create a PDF file containing data about the flatmates with their names, amount due, and period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = "$" + str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = "$" + str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=40, h=40)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmate Bill', border=0, align='C', ln=1)

        # Insert Period and value
        pdf.set_font(family='Times', style='I', size=20)
        pdf.cell(w=100, h=40, txt="Period: ", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font(family='Times', style='B', size=18)
        pdf.cell(w=100, h=40, txt="Name ", border=0)
        pdf.cell(w=150, h=40, txt="Amount to Pay", border=0, ln=1)

        # Insert name and payment of first flatmate
        pdf.set_font(family='Times', size=16)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and payment of second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)


bill = Bill(120, "Dec 2020")
john = Flatmate("John", 20)
marry = Flatmate("Marry", 25)
print(john.pays(bill, marry))
print(marry.pays(bill, john))
pdf_report = PdfReport("Report1.pdf")
pdf_report.generate(john, marry, bill)