from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(
    disease,
    confidence,
    specialist,
    symptoms
):

    file_path = "reports/medical_report.pdf"

    doc = SimpleDocTemplate(
        file_path,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "<b>AI Health Consultant Report</b>",
        styles['Title']
    )

    elements.append(title)
    elements.append(Spacer(1, 20))

    disease_text = Paragraph(
        f"<b>Predicted Disease:</b> {disease}",
        styles['BodyText']
    )

    elements.append(disease_text)
    elements.append(Spacer(1, 12))

    confidence_text = Paragraph(
        f"<b>Confidence:</b> {confidence:.2f}%",
        styles['BodyText']
    )

    elements.append(confidence_text)
    elements.append(Spacer(1, 12))

    specialist_text = Paragraph(
        f"<b>Recommended Specialist:</b> {specialist}",
        styles['BodyText']
    )

    elements.append(specialist_text)
    elements.append(Spacer(1, 12))

    symptoms_text = Paragraph(
        f"<b>Symptoms:</b> {symptoms}",
        styles['BodyText']
    )

    elements.append(symptoms_text)
    elements.append(Spacer(1, 20))

    note = Paragraph(
        "This report is generated for educational purposes only.",
        styles['Italic']
    )

    elements.append(note)

    doc.build(elements)

    return file_path