from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(
    disease,
    confidence,
    specialist,
    symptoms
):

    filename = "reports/medical_report.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    # TITLE

    title = Paragraph(
        "AI Health Consultant Report",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    # DISEASE

    disease_text = Paragraph(
        f"<b>Predicted Disease:</b> {disease}",
        styles['BodyText']
    )

    elements.append(disease_text)

    elements.append(Spacer(1, 12))

    # CONFIDENCE

    confidence_text = Paragraph(
        f"<b>Confidence Score:</b> {confidence:.2f}%",
        styles['BodyText']
    )

    elements.append(confidence_text)

    elements.append(Spacer(1, 12))

    # SPECIALIST

    specialist_text = Paragraph(
        f"<b>Recommended Specialist:</b> {specialist}",
        styles['BodyText']
    )

    elements.append(specialist_text)

    elements.append(Spacer(1, 12))

    # SYMPTOMS

    symptoms_text = Paragraph(
        f"<b>Symptoms:</b> {symptoms}",
        styles['BodyText']
    )

    elements.append(symptoms_text)

    elements.append(Spacer(1, 20))

    # DISCLAIMER

    disclaimer = Paragraph(
        "This report is generated for educational purposes only.",
        styles['Italic']
    )

    elements.append(disclaimer)

    # BUILD PDF

    doc.build(elements)

    return filename