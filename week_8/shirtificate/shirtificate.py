from fpdf import FPDF

class Shirtificate:
    def __init__(self, name):
        self.name = name

        # create pdf
        self.pdf = FPDF(orientation="portrait", format="A4")
        self.pdf.add_page()
        #header
        self.pdf.set_font('Arial', 'B', 32)
        self.pdf.cell(0, 10, 'CS50 Shirtificate', align='C', ln=1)
        # image
        self.pdf.image("shirtificate.png", x=20, y=50, w=170)
        # shirt's name
        self.pdf.set_font('Arial', 'B', 20)
        self.pdf.set_text_color(255, 255, 255)  # White
        self.pdf.cell(0, 130, self.name, align='C', ln=1, fill=False)
        # print pdf
        self.pdf.output("shirtificate.pdf")

def main():
    name = get_shirtificate(input("Name: "))


def get_shirtificate(nm):
    shirtificate = Shirtificate(nm)


if __name__ == "__main__":
    main()