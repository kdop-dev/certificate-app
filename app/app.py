from flask import send_file, send_from_directory, safe_join, abort, request
from fpdf import FPDF
from flask import Flask
app = Flask(__name__)

pdf_w=210
pdf_h=297

STORAGE_PDF="certs"

class PDF(FPDF):
    def lines(self):
        self.set_fill_color(255, 255, 255) # color for outer rectangle
        self.rect(5.0, 5.0, 200.0,287.0,'DF')
        self.set_fill_color(255, 255, 255) # color for inner rectangle
        self.rect(8.0, 8.0, 194.0,282.0,'FD')
        #self.dashed_line(x1=0+45, y1=120, x2=pdf_w-45, y2=120, dash_length = 1, space_length = 1)

    def titles(self):
            self.set_xy(0.0, 10.0)
            self.set_font('Balista', 'R', 18)
            self.set_text_color(220, 50, 50)
            self.cell(w=210.0, h=40.0, align='C', txt="Certificado de Participação", border=0)
            self.set_xy(0.0, 40.0)
            self.set_text_color(100, 100, 100)
            self.set_font('Balista', 'R', 14)
            self.cell(w=210.0, h=40.0, align='C', txt="Pílula de inovação - Workshop interativo K8s", border=0)

    def texts(self, name):
            with open(name,'rb') as xy:
                txt=xy.read().decode('UTF-8')
            self.set_xy(10.0, 150.0)
            self.set_text_color(0, 0, 0)
            self.set_font('Balista', 'R', 12)
            self.multi_cell(w=0, h=10, txt=txt, align='C')

    def participant_name(self, name):
            self.set_xy(10.0, 100.0)
            self.set_text_color(0, 0, 0)
            self.set_font('Balista', 'R', 16)
            self.multi_cell(w=0, h=10, txt=name, align='C')

    def congratulations(self):
            self.set_xy(0.0, 200.0)
            self.set_font('Balista', 'R', 22)
            self.set_text_color(220, 50, 50)
            self.cell(w=210.0, h=40.0, align='C', txt="Parabéns", border=0) 

    def imagex(self):
            self.image('static/lion.png', 10, 10, 33) # sup left
            self.image('static/lion-i.png', pdf_w-42, 10, 33) # sup right
            self.image('static/lion.png', 10, pdf_h-50, 33) # low left
            self.image('static/lion-i.png', pdf_w-42, pdf_h-50, 33) # low right


def create_cert(name):
    # full syntax
    #PDF(orientation={'P'(def.) or 'L'}, measure{'mm'(def.),'cm','pt','in'}, format{'A4'(def.),'A3','A5','Letter','Legal')
    #default
    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.add_font('Balista', 'R', 'static/balista.ttf', uni=True)
    pdf.add_page()
    pdf.lines()
    pdf.texts("static/cert.txt")
    pdf.titles()
    pdf.imagex()
    pdf.participant_name(name)
    pdf.congratulations()
    pdf.set_author('Anderson Santos')
    filename = f'{STORAGE_PDF}/{name}-cert.pdf'
    pdf.output(filename,'F')
    return filename

@app.route("/")
@app.route("/health")
def health():
    return "Cert-app Ok!"

@app.route("/get-cert")
def get_pdf():

    participant = request.args.get('p')

    filename = create_cert(participant)

    try:
        return send_file(filename, as_attachment=True)
        # return send_from_directory(app.config["CLIENT_PDF"], filename=filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)

# run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)