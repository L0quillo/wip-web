import os
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, KeepTogether, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CORP_DIR = os.path.join(BASE_DIR, "corporativo")
DOCS_DIR = os.path.join(CORP_DIR, "documentos")
LOGOS_DIR = os.path.join(CORP_DIR, "logos")
SKILLS_DIR = os.path.join(CORP_DIR, "ai-skills")

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(LOGOS_DIR, exist_ok=True)
os.makedirs(SKILLS_DIR, exist_ok=True)

# Colors
HEX_RED = "C1303A"      # Main Corporate Red
HEX_BLUE = "244088"     # Industrial Blue
HEX_DARK = "211915"     # Charcoal Dark
HEX_GRAY = "555555"     # Body Gray
HEX_BG_LIGHT = "F4F6F9" # Light Background

RGB_RED = RGBColor(193, 48, 58)
RGB_BLUE = RGBColor(36, 64, 136)
RGB_DARK = RGBColor(33, 25, 21)
RGB_GRAY = RGBColor(85, 85, 85)

COLOR_RED = colors.HexColor("#C1303A")
COLOR_BLUE = colors.HexColor("#244088")
COLOR_DARK = colors.HexColor("#211915")
COLOR_GRAY = colors.HexColor("#555555")
COLOR_BG_LIGHT = colors.HexColor("#F4F6F9")
COLOR_LINE = colors.HexColor("#D0D7DE")

# ==========================================
# 1. GENERATE DOCX
# ==========================================
def generate_docx():
    doc = docx.Document()
    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)

    def set_cell_background(cell, fill_hex):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        tcPr.append(shd)

    def add_h(text, level):
        p = doc.add_heading(level=level)
        p.paragraph_format.space_before = Pt(14 if level==1 else 10)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        if level == 1:
            run.font.color.rgb = RGB_RED
            run.font.size = Pt(16)
            run.bold = True
        elif level == 2:
            run.font.color.rgb = RGB_BLUE
            run.font.size = Pt(13)
            run.bold = True
        elif level == 3:
            run.font.color.rgb = RGB_DARK
            run.font.size = Pt(11)
            run.bold = True
        return p

    def add_p(text, bold_prefix="", italic=False):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_b = p.add_run(bold_prefix)
            r_b.bold = True
            r_b.font.color.rgb = RGB_DARK
            r_b.font.size = Pt(10)
        r = p.add_run(text)
        r.font.color.rgb = RGB_GRAY
        r.font.size = Pt(10)
        if italic:
            r.italic = True
        return p

    def add_bullet(bold_title, desc):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        r_b = p.add_run(bold_title + ": ")
        r_b.bold = True
        r_b.font.color.rgb = RGB_DARK
        r_b.font.size = Pt(9.5)
        r_t = p.add_run(desc)
        r_t.font.color.rgb = RGB_GRAY
        r_t.font.size = Pt(9.5)
        return p

    # Logo if exists
    logo_path = os.path.join(BASE_DIR, "LOGO WIP-01.png")
    if os.path.exists(logo_path):
        doc.add_picture(logo_path, width=Inches(2.5))
        last_p = doc.paragraphs[-1]
        last_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(6)
    title_p.paragraph_format.space_after = Pt(2)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t = title_p.add_run("MANUAL DE IDENTIDAD CORPORATIVA & ESTRATEGIA COMERCIAL")
    r_t.font.size = Pt(18)
    r_t.bold = True
    r_t.font.color.rgb = RGB_RED

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_after = Pt(12)
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_s = sub_p.add_run("WIP | Soluciones Integrales en Tratamiento de Aguas, Filtración y Montajes Industriales")
    r_s.font.size = Pt(11)
    r_s.bold = True
    r_s.font.color.rgb = RGB_BLUE

    # Meta callout
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = tbl.cell(0, 0)
    set_cell_background(c, HEX_BG_LIGHT)
    p_c = c.paragraphs[0]
    p_c.paragraph_format.space_before = Pt(6)
    p_c.paragraph_format.space_after = Pt(6)
    r_c = p_c.add_run("Propósito del Documento: Establecer las directrices visuales, técnicas y comerciales de WIP para la generación consistente de contenido publicitario, catálogos técnicos, videos, propuestas B2B y el desarrollo de la nueva página web corporativa.")
    r_c.font.size = Pt(9.5)
    r_c.italic = True
    r_c.font.color.rgb = RGB_DARK

    doc.add_paragraph()

    # SECTION 1
    add_h("1. IDENTIDAD CORPORATIVA Y ELEMENTOS VISUALES", level=1)
    add_p("La identidad corporativa de WIP refleja solidez industrial, precisión de ingeniería y compromiso con la sustentabilidad y el cumplimiento normativo estricto en el sector hídrico e industrial.")

    add_h("1.1 Paleta de Colores Corporativos", level=2)
    
    # Table Colors
    t_col = doc.add_table(rows=5, cols=4)
    t_col.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Color / Elemento", "HEX", "RGB", "Uso Principal"]
    for i, h in enumerate(headers):
        cell = t_col.cell(0, i)
        set_cell_background(cell, HEX_RED)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

    color_rows = [
        ("Rojo WIP Primario", "#C1303A", "RGB(193, 48, 58)", "Logotipo, botones principales de acción (CTA), títulos destacados."),
        ("Azul Industrial Secundario", "#244088", "RGB(36, 64, 136)", "Subtítulos, íconos de ingeniería, tarjetas de servicio y acentos."),
        ("Gris Oscuro Carbón", "#211915", "RGB(33, 25, 21)", "Tipografía principal, encabezados oscuros, fondos de contraste."),
        ("Gris Técnico / Neutro", "#99989D / #F4F6F9", "RGB(153, 152, 157)", "Fondos de secciones, bordes técnicos, tablas y cajas de datos.")
    ]
    for row_idx, data in enumerate(color_rows, start=1):
        for col_idx, text in enumerate(data):
            cell = t_col.cell(row_idx, col_idx)
            set_cell_background(cell, HEX_BG_LIGHT if row_idx % 2 == 0 else "FFFFFF")
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            r = p.add_run(text)
            r.font.size = Pt(9)
            r.font.color.rgb = RGB_DARK if col_idx == 0 else RGB_GRAY
            if col_idx == 0:
                r.bold = True

    doc.add_paragraph()
    add_h("1.2 Tipografía Corporativa", level=2)
    add_bullet("Titulares y Encabezados", "Inter, Montserrat o Roboto Bold. Líneas limpias, modernas y legibles.")
    add_bullet("Cuerpo de Texto y Fichas Técnicas", "Roboto Regular o Inter Regular (tamaño 9.5pt a 11pt, interlineado 1.15x - 1.3x).")
    add_bullet("Datos Técnicos y Tablas", "JetBrains Mono o Roboto Mono para caudales, micrajes, presiones y códigos de partes.")

    # SECTION 2
    add_h("2. POSICIONAMIENTO Y PROPUESTA DE VALOR COMERCIAL", level=1)
    add_bullet("Propuesta de Valor Central", "Ingeniería confiable y soluciones integrales de filtración, potabilización y montajes industriales de alto rendimiento, garantizando cumplimiento de normativas nacionales e internacionales.")
    add_bullet("Marco Normativo y Certificaciones", "Norma Boliviana NB 512 (Agua Potable), Ley de Medio Ambiente 1333 (Efluentes y PTAR), FDA/NSF (Materiales grado alimenticio), ASME/AWS (Calificación de procedimientos de soldadura TIG/MIG/MAG/SMAW).")
    add_bullet("Público Objetivo (B2B)", "Industrias de alimentos y bebidas, farmacéuticas, minería, hidrocarburos, embotelladoras, constructoras, hospitales, hoteles y municipios.")

    # SECTION 3
    add_h("3. MATRIZ INTEGRAL DE LÍNEAS DE NEGOCIO Y SERVICIOS", level=1)

    add_h("3.1 Línea de Tratamiento de Aguas (Potable, Industrial y Residual)", level=2)
    add_bullet("Plantas Potabilizadoras de Agua (PPA)", "Sistemas modulares montados en estructura metálica transportable, diseñados bajo NB 512 con etapas de floculación, sedimentación, filtración multimedia y desinfección.")
    add_bullet("Plantas de Tratamiento de Residuos Industriales (PDA-I)", "Sistemas fisicoquímicos, biológicos, flotación DAF, desbaste y separación de hidrocarburos con alto valor añadido.")
    add_bullet("Plantas de Tratamiento de Aguas Residuales (PTAR)", "Depuración biológica y fisicoquímica para descarga segura bajo Ley 1333 (Series C comerciales y D domésticas).")
    add_bullet("Sistemas de Ósmosis Inversa (RO)", "Purificación y desmineralización por membranas para procesos farmacéuticos, alimentos y calderos.")
    add_bullet("Ablandadores de Agua de Intercambio Iónico", "Eliminación de dureza (calcio y magnesio) con resinas catiónicas y tanques de salmuera para protección de calderas y circuitos de enfriamiento.")
    add_bullet("Desmineralizadores de Agua (Modelo SDA)", "Columnas catiónicas y aniónicas para agua de ultra pureza desionizada.")
    add_bullet("Filtros Multimedia y de Arena", "Retención de sólidos suspendidos y turbidez hasta 20 micras.")
    add_bullet("Filtros de Carbón Activado", "Eliminación de cloro libre, olores, sabores y compuestos orgánicos (incluyendo cartuchos Pentair Pentek SCBC-10).")
    add_bullet("Desinfección Ultravioleta (UV) y Ozonizadores", "Eliminación microbiológica instantánea sin químicos residuales (Ozono 3000x más rápido que el cloro).")
    add_bullet("Bombas Dosificadoras de Químicos y Carcasas", "Dosificación precisa para polímeros, coagulantes y biocidas. Carcasas NSF/FDA de 10” a 20” estándar y Big Blue.")

    add_h("3.2 Línea de Filtración Industrial y Filtros Metálicos", level=2)
    add_bullet("Filtros Metálicos para Aceites (Serie P)", "Carcasas de acero de alta resistencia dimensionadas hasta 15 bar a 100°C con bridas PN16 de 2” y 3”.")
    add_bullet("Filtros para Combustibles (GN, GLP y Líquidos)", "Sistemas con manómetro de glicerina, válvulas de seguridad, pintura epóxica y sistema eléctrico Explosion Proof para tanques aéreos y enterrados.")
    add_bullet("Filtros Metálicos para Polvo y Gases", "Purificadores de aire industrial con carbón activado granulado y mangas metálicas para control de emisiones y solventes.")
    add_bullet("Consumibles de Filtración", "Filtros de polipropileno extruido, filtros bolsa de alto caudal, filtros plisados lavables y cartuchos recargables.")

    add_h("3.3 Línea de Servicios de Ingeniería y Montajes Industriales", level=2)
    add_bullet("Líneas de Vapor y Condensado", "Instalación de cabezales distribuidores, estaciones reguladoras de presión, bolsillos separadores de gotas y trampas de vapor.")
    add_bullet("Líneas de Combustibles (GN, GLP, Líquidos)", "Tendido y prueba hidrostática/neumática de redes industriales bajo normativa.")
    add_bullet("Soldaduras Especiales Certificadas", "Procedimientos TIG, MIG, MAG y SMAW en aceros al carbono, inoxidables y aleaciones especiales.")
    add_bullet("Protección Refractaria y Aislamiento", "Moldeado de piezas especiales refractarias y revestimiento térmico para calderos y hornos.")
    add_bullet("Instalaciones Eléctricas Industriales y Obras Civiles", "Tableros de control automatizado, acometidas y fundaciones para maquinaria pesada.")

    # SECTION 4
    add_h("4. GUÍA DE CREACIÓN DE CONTENIDOS COMERCIALES", level=1)
    add_bullet("Tono de Comunicación", "Técnico-consultivo, profesional, resolutivo y enfocado en la eficiencia operativa, ahorro de costos y cumplimiento legal.")
    add_bullet("Estructura de Folletos y Fichas Comerciales", "1. Título Impactante -> 2. Problema Industrial -> 3. Solución Técnica WIP -> 4. Tabla de Especificaciones -> 5. Cumplimiento Normativo -> 6. Llamado a la Acción (WhatsApp / Cotización Inmediata).")
    add_bullet("Estructura de Guiones Audiovisuales (Reels / YouTube)", "Gancho (0-3s): ¿Parada de planta por sarro o agua dura? -> Desarrollo (4-20s): Demostración del equipo/servicio WIP -> Prueba (21-35s): Datos de rendimiento/norma -> Cierre (36-45s): Contacta al equipo de ingeniería de WIP.")

    doc.save(os.path.join(DOCS_DIR, "MANUAL_IDENTIDAD_Y_ESTRATEGIA_COMERCIAL_WIP.docx"))
    print("DOCX generated successfully.")

# ==========================================
# 2. GENERATE PDF
# ==========================================
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        # Top bar
        self.setFillColor(COLOR_RED)
        self.rect(0, 782, 612, 10, fill=1, stroke=0)
        
        # Header text
        self.setFont("Helvetica", 8)
        self.setFillColor(COLOR_GRAY)
        self.drawString(54, 768, "WIP | Manual de Identidad Corporativa y Estrategia Comercial")
        
        # Footer line
        self.setStrokeColor(COLOR_LINE)
        self.setLineWidth(0.5)
        self.line(54, 45, 558, 45)
        
        # Footer text
        self.setFont("Helvetica", 8)
        self.setFillColor(COLOR_GRAY)
        self.drawString(54, 32, "Confidencial - Uso Comercial e Ingeniería WIP")
        self.drawRightString(558, 32, f"Página {self._pageNumber} de {page_count}")
        self.restoreState()

def generate_pdf():
    pdf_path = os.path.join(DOCS_DIR, "MANUAL_IDENTIDAD_Y_ESTRATEGIA_COMERCIAL_WIP.pdf")
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    style_title = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=COLOR_RED,
        alignment=1, # Center
        spaceAfter=4
    )

    style_subtitle = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=COLOR_BLUE,
        alignment=1,
        spaceAfter=12
    )

    style_h1 = ParagraphStyle(
        'CustomH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=COLOR_RED,
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    style_h2 = ParagraphStyle(
        'CustomH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=COLOR_BLUE,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    style_body = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=COLOR_DARK,
        spaceAfter=5
    )

    style_bullet = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=COLOR_DARK,
        leftIndent=12,
        firstLineIndent=-12,
        spaceAfter=3
    )

    story = []

    # Logo
    logo_path = os.path.join(BASE_DIR, "LOGO WIP-01.png")
    if os.path.exists(logo_path):
        story.append(RLImage(logo_path, width=150, height=55))
        story.append(Spacer(1, 8))

    story.append(Paragraph("MANUAL DE IDENTIDAD CORPORATIVA & ESTRATEGIA COMERCIAL", style_title))
    story.append(Paragraph("WIP | Tratamiento de Aguas, Filtración y Montajes Industriales", style_subtitle))
    
    # Meta Box Table
    meta_p = Paragraph("<b>Documento Maestro Corporativo</b> &bull; Directrices para generación de contenidos con Inteligencia Artificial (ChatGPT, Claude/Hermes, Gemini), catálogos técnicos, material publicitario y desarrollo de la nueva web.", style_body)
    meta_table = Table([[meta_p]], colWidths=[504])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_BG_LIGHT),
        ('BOX', (0,0), (-1,-1), 0.5, COLOR_LINE),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 10))

    # 1. Identidad Visual
    story.append(Paragraph("1. IDENTIDAD VISUAL Y PALETA CROMÁTICA", style_h1))
    story.append(Paragraph("La identidad visual de WIP proyecta confianza técnica, precisión ingenieril y sostenibilidad ambiental. La combinación del <b>Rojo Corporativo</b> y el <b>Azul Industrial</b> equilibra dinamismo energético y rigurosidad hídrica.", style_body))
    
    # Table Colors
    t_data = [
        [Paragraph("<b>Color</b>", style_body), Paragraph("<b>Código HEX / RGB</b>", style_body), Paragraph("<b>Aplicación en Piezas Comerciales</b>", style_body)],
        [Paragraph("<b>Rojo WIP Primario</b>", style_body), Paragraph("#C1303A<br/>RGB(193, 48, 58)", style_body), Paragraph("Logotipo, botones de acción (CTA), títulos de alto impacto.", style_body)],
        [Paragraph("<b>Azul Industrial</b>", style_body), Paragraph("#244088<br/>RGB(36, 64, 136)", style_body), Paragraph("Subtítulos, íconos de agua/procesos, tarjetas técnicas.", style_body)],
        [Paragraph("<b>Gris Carbón</b>", style_body), Paragraph("#211915<br/>RGB(33, 25, 21)", style_body), Paragraph("Textos de lectura principal, encabezados oscuros.", style_body)],
        [Paragraph("<b>Gris Claro Técnico</b>", style_body), Paragraph("#F4F6F9<br/>RGB(244, 246, 249)", style_body), Paragraph("Fondos de tablas, cajas destacadas y fondos web.", style_body)],
    ]
    col_t = Table(t_data, colWidths=[120, 114, 270])
    col_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_BG_LIGHT),
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_LINE),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(col_t)
    story.append(Spacer(1, 8))

    # 2. Posicionamiento
    story.append(Paragraph("2. POSICIONAMIENTO Y PROPUESTA DE VALOR B2B", style_h1))
    story.append(Paragraph("&bull; <b>Propuesta de Valor:</b> Soluciones integrales de ingeniería llave en mano para tratamiento de agua, filtración crítica y montajes industriales con máxima durabilidad y cero paradas no programadas.", style_bullet))
    story.append(Paragraph("&bull; <b>Cumplimiento Normativo Obligatorio:</b> Cumplimiento estricto de la <b>Norma Boliviana NB 512</b> (Agua Potable), <b>Ley 1333 de Medio Ambiente</b> (Efluentes Industriales PTAR), estándares <b>FDA/NSF</b> y códigos de soldadura <b>ASME / AWS</b>.", style_bullet))
    story.append(Paragraph("&bull; <b>Sectores Clave:</b> Alimentos y bebidas, farmacéuticas, minería, hidrocarburos, embotelladoras, manufactura, calderas industriales, hoteles y hospitales.", style_bullet))

    # 3. Portafolio
    story.append(Paragraph("3. PORTAFOLIO TÉCNICO Y COMERCIAL", style_h1))
    
    story.append(Paragraph("3.1 Línea de Tratamiento de Aguas", style_h2))
    story.append(Paragraph("&bull; <b>Plantas Potabilizadoras de Agua (PPA):</b> Plantas modulares transportables en estructura de acero bajo Norma NB 512.", style_bullet))
    story.append(Paragraph("&bull; <b>Plantas de Residuos Industriales (PDA-I) & PTAR:</b> Depuración biológica y fisicoquímica de efluentes bajo Ley 1333.", style_bullet))
    story.append(Paragraph("&bull; <b>Ósmosis Inversa (RO):</b> Desmineralización por membranas para alimentos, farmacéutica y agua de caldero.", style_bullet))
    story.append(Paragraph("&bull; <b>Ablandadores de Agua & Desmineralizadores (SDA):</b> Intercambio iónico catiónico y aniónico de alta regeneración.", style_bullet))
    story.append(Paragraph("&bull; <b>Filtración Especializada:</b> Filtros de arena multimedia, carbón activado Pentek SCBC-10, sistemas UV y Ozonizadores industriales.", style_bullet))

    story.append(Paragraph("3.2 Línea de Filtración Industrial & Filtros Metálicos", style_h2))
    story.append(Paragraph("&bull; <b>Filtros para Aceite (Serie P):</b> Diseñados para presiones de hasta 15 bar y 100°C con bridas PN16 de 2” y 3”.", style_bullet))
    story.append(Paragraph("&bull; <b>Filtros de Combustibles:</b> Equipos Explosion-Proof para tanques de combustible con manómetro de glicerina y doble capa epóxica.", style_bullet))
    story.append(Paragraph("&bull; <b>Filtros de Polvo & Gases:</b> Adsorción con carbón activado granular para control ambiental y olores.", style_bullet))

    story.append(Paragraph("3.3 Línea de Montajes e Ingeniería", style_h2))
    story.append(Paragraph("&bull; <b>Vapor y Condensado:</b> Colectores, estaciones reguladoras de presión y separadores de gotas.", style_bullet))
    story.append(Paragraph("&bull; <b>Redes de Combustibles (GN / GLP):</b> Tendido industrial de gas y líneas de fluidos.", style_bullet))
    story.append(Paragraph("&bull; <b>Soldaduras Especiales Certificadas:</b> Homologación en procedimientos TIG, MIG, MAG y SMAW.", style_bullet))
    story.append(Paragraph("&bull; <b>Refractarios & Obras Civiles:</b> Aislamiento térmico para calderos y bases de concreto para maquinaria pesada.", style_bullet))

    # 4. Estrategia de IA
    story.append(Paragraph("4. PROTOCOLO DE GENERACIÓN DE CONTENIDOS CON IA", style_h1))
    story.append(Paragraph("Para garantizar consistencia de marca, toda pieza generada por ChatGPT, Hermes o Gemini debe incluir: (1) Datos técnicos verificables (bar, GPM, micras, normas NB512/Ley 1333), (2) Tono B2B enfocado en confiabilidad y retorno de inversión, y (3) Llamado claro a contacto técnico comercial.", style_body))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("PDF generated successfully.")

# ==========================================
# 3. GENERATE MARKDOWN VERSION
# ==========================================
def generate_markdown():
    md_content = """# MANUAL DE IDENTIDAD CORPORATIVA Y ESTRATEGIA COMERCIAL
**Empresa:** WIP | Soluciones Integrales en Tratamiento de Aguas, Filtración y Montajes Industriales  
**Versión:** 2.0  
**Uso:** Guía maestra de marca, creación de contenidos comerciales y desarrollo web.

---

## 1. Identidad Visual y Cromática

### 1.1 Paleta de Colores
| Nombre del Color | Código HEX | Código RGB | Aplicación Principal |
| :--- | :--- | :--- | :--- |
| **Rojo WIP Primario** | `#C1303A` / `#FE0000` | `RGB(193, 48, 58)` | Logotipo, botones de acción (CTA), títulos principales. |
| **Azul Industrial** | `#244088` | `RGB(36, 64, 136)` | Subtítulos, iconografía hídrica, tarjetas técnicas. |
| **Gris Oscuro Carbón** | `#211915` | `RGB(33, 25, 21)` | Texto de lectura, encabezados de alto contraste. |
| **Gris Técnico / Neutro** | `#99989D` / `#F4F6F9` | `RGB(153, 152, 157)` | Fondos de tablas, fichas técnicas y bordes. |

### 1.2 Tipografías Recomendadas
- **Títulos y Encabezados:** Inter Bold, Montserrat Bold, Roboto Bold.
- **Cuerpo de Texto:** Roboto Regular, Inter Regular (Interlineado 1.25x - 1.4x).
- **Especificaciones Técnicas y Códigos:** JetBrains Mono o Roboto Mono.

---

## 2. Propuesta de Valor y Posicionamiento B2B

### 2.1 Propuesta de Valor
> *"Ingeniería de vanguardia y soluciones integrales llave en mano para tratamiento de agua, filtración industrial crítica y montajes mecánicos de alta exigencia, asegurando estricto cumplimiento normativo y máxima continuidad operativa."*

### 2.2 Normativas y Homologaciones Clave
- **NB 512 (Norma Boliviana de Agua Potable):** Parámetros fisicoquímicos y microbiológicos para consumo humano.
- **Ley de Medio Ambiente 1333 (Bolivia):** Límites permisibles para descargas de efluentes industriales y aguas residuales (PTAR/PDA-I).
- **Estándares NSF / FDA:** Materiales y polipropileno grado alimenticio para carcasas y cartuchos filtrantes.
- **Códigos de Soldadura ASME / AWS:** Procedimientos homologados de soldadura TIG, MIG, MAG y SMAW.

### 2.3 Audiencia y Sectores Clave
1. **Industria de Alimentos y Bebidas:** Embotelladoras, lácteos, cervecerías, agroindustria (agua ultra pura, filtración sanitaria).
2. **Industria Farmacéutica y Cosmética:** Ósmosis inversa, desmineralización por intercambio iónico, desinfección UV/Ozono.
3. **Sector Minero y Petrolero:** Separación de hidrocarburos, filtración de combustibles explosion-proof, tratamiento de efluentes complejos.
4. **Plantas Industriales y Manufactureras:** Calderas de vapor, torres de enfriamiento, ablandamiento de agua, redes de gas y montajes.
5. **Sector Institucional y Hospitalario:** Potabilización autónoma, depuración sanitaria y climatización.

---

## 3. Matriz Completa de Productos y Servicios

### 3.1 Tratamiento de Aguas
- **Plantas Potabilizadoras de Agua (PPA):** Estructura metálica skid transportable, clarificación, filtración y cloración NB 512.
- **Plantas de Residuos Industriales (PDA-I):** Desbaste, DAF, fisicoquímico y separación de aceites.
- **Plantas de Aguas Residuales (PTAR):** Series C (comercial) y D (doméstica) bajo Ley 1333.
- **Sistemas de Ósmosis Inversa (RO):** Membranas semipermeables de alta retención de sales y contaminantes.
- **Ablandadores de Agua:** Intercambio catiónico para eliminación de dureza cálcica y magnésica en calderos.
- **Desmineralizadores (Modelo SDA):** Columnas catiónicas y aniónicas en serie para agua de alta resistividad.
- **Filtros de Arena Multimedia & Carbón Activado:** Retención de sólidos (20 micras), remoción de cloro y olores.
- **Desinfección Ultravioleta (UV) & Ozonizadores:** Esterilización instantánea sin subproductos químicos.
- **Bombas Dosificadoras de Químicos:** Dosificación de precisión para coagulantes, floculantes y neutralizantes.
- **Carcasas y Cartuchos:** Carcasas NSF/FDA de 10" y 20" (Slim y Big Blue), filtros plisados, filtros bolsa y polipropileno.

### 3.2 Filtración Industrial & Metálica
- **Filtros Metálicos para Aceite (Serie P):** Presión de trabajo 7 a 10 bar (diseño hasta 15 bar a 100°C), bridas PN16.
- **Filtros de Combustible (GN / GLP / Diésel):** Diseño Explosion Proof con manómetro de glicerina y visor de nivel.
- **Filtros Metálicos para Polvo y Vapores:** Purificación de aire con carbón activado granular para solventes y humos.

### 3.3 Servicios de Ingeniería y Montajes
- **Redes de Vapor y Condensado:** Manifolds de distribución, estaciones reductoras de presión (PRV) y separadores de gotas.
- **Instalación de Combustibles:** Redes certificadas de GN, GLP y combustibles líquidos.
- **Soldaduras Industriales Especiales:** Procedimientos calificados TIG, MIG, MAG y SMAW.
- **Protección Refractaria:** Moldeo de piezas refractarias y revestimiento térmico para hornos y calderos.
- **Instalaciones Eléctricas Industriales & Obras Civiles:** Cuadros eléctricos de automatización y fundaciones de equipos.

---

## 4. Guía de Redacción Comercial y Formatos para Redes / Medios

### 4.1 Fórmula de Copywriting B2B
1. **Gancho de Impacto:** Enfoque en costo de inactividad, fallas en calderas, incrustaciones o sanciones ambientales.
2. **Propuesta de Solución WIP:** Tecnología precisa, dimensionamiento a medida y soporte de ingeniería local.
3. **Validación Técnica:** Micraje, caudal (GPM / m³/h), presión de trabajo y normativa aplicable (NB 512, Ley 1333).
4. **Llamado a la Acción (CTA):** *“Solicita una evaluación técnica sin costo con nuestros ingenieros especializados.”*
"""
    with open(os.path.join(DOCS_DIR, "MANUAL_IDENTIDAD_Y_ESTRATEGIA_COMERCIAL_WIP.md"), "w", encoding="utf-8") as f:
        f.write(md_content)
    print("Markdown generated successfully.")

if __name__ == "__main__":
    generate_docx()
    generate_pdf()
    generate_markdown()
