from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import util

def gerar_pdf_nota_fatura(nf_data, caminho_arquivo):
    try:
        doc = SimpleDocTemplate(caminho_arquivo, pagesize=A4, rightMargin=20*mm,leftMargin=20*mm, topMargin=20*mm, bottomMargin=20*mm)
        styles = getSampleStyleSheet()
        style_titulo = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=16,textColor=colors.HexColor('#003366'), spaceAfter=12, alignment=TA_CENTER)
        style_normal = ParagraphStyle('CustomNormal', parent=styles['Normal'], fontSize=9,leading=12)
        style_bold = ParagraphStyle('CustomBold', parent=styles['Normal'], fontSize=9,fontName='Helvetica-Bold', leading=12)
        elementos = []
        elementos.extend(criar_cabecalho(nf_data, style_titulo, style_bold, style_normal))
        elementos.append(Spacer(1, 10*mm))
        elementos.extend(criar_secao_destinatario(nf_data, style_bold, style_normal))
        elementos.append(Spacer(1, 5*mm))
        elementos.extend(criar_secao_fatura(nf_data, style_bold, style_normal))
        elementos.append(Spacer(1, 5*mm))
        elementos.append(criar_tabela_produtos(nf_data))
        elementos.append(Spacer(1, 5*mm))
        elementos.append(criar_secao_totais(nf_data))
        elementos.append(Spacer(1, 5*mm))
        elementos.extend(criar_secao_observacoes(nf_data, style_bold, style_normal))
        elementos.append(Spacer(1, 5*mm))
        elementos.extend(criar_rodape(nf_data, style_bold, style_normal))
        doc.build(elementos)
        # print(nf_data)
        return True
    except Exception as e:
        # import traceback
        # traceback.print_exc()
        print(f"Erro ao gerar PDF: {e}")
        return False

def criar_cabecalho(nf_data, style_titulo, style_normal, style_bold):
    elementos = []
    elementos.append(Paragraph("FEDERAL ANDAIMES", style_titulo))
    elementos.append(Spacer(1, 3*mm))
    contrato = nf_data.get('contrato', '') or ''
    dados_cabecalho = [
        [
            Paragraph("Nome Empresarial: 60.067.070 - Sonia Maria Leobons da Silva<br/>"
                     "Endereço: Avenida Tomas Alves de Figuereido, 150, C2<br/>"
                     "Vila Hepacaré - Lorena - SP - CEP 12608-356<br/>"
                     "Cel.: (12) 99776-4144<br/>"
                     "CNPJ: 60.067.070/0001-99", style_normal),
            Paragraph(f"<b>NOTA FATURA</b><br/>"
                     f"<b>Nº {nf_data['numero_nf']}</b><br/>"
                     f"<b>Contrato: {contrato}</b><br/>"
                     f"Data de Emissão<br/>"
                     f"{formatar_data(nf_data['data_emissao'])}", 
                     ParagraphStyle('center', alignment=TA_CENTER, fontSize=10))
        ]
    ]
    tabela = Table(dados_cabecalho, colWidths=[120*mm, 50*mm])
    tabela.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elementos.append(tabela)
    return elementos

def criar_secao_destinatario(nf_data, style_bold, style_normal):
    elementos = []
    elementos.append(Paragraph("<b>DESTINATÁRIO</b>", style_bold))
    dados_cliente = [
        [
            Paragraph("<b>NOME / RAZÃO SOCIAL</b>", style_bold),
            Paragraph("<b>CPF/CNPJ</b>", style_bold)
            
        ],
        [
            Paragraph(nf_data['cliente_nome'], style_normal), 
            Paragraph(nf_data['cliente_cpf_cnpj'] or '', style_normal)
        ],
        [
            Paragraph("<b>CEP</b>", style_bold),
            Paragraph("<b>ENDEREÇO</b>", style_bold)
        ],
        [
            Paragraph(nf_data['cliente_cep'] or '', style_normal),
            Paragraph(nf_data['cliente_rua'] or '', style_normal)
        ],
        [
            Paragraph("<b>NÚMERO</b>", style_bold),
            Paragraph("<b>COMPLEMENTO</b>", style_bold)
        ],
        [
            Paragraph(nf_data['cliente_numero'] or '', style_normal),
            Paragraph(nf_data['cliente_complemento'] or '', style_normal)
        ],
        [
            Paragraph("<b>BAIRRO</b>", style_bold),
            Paragraph("<b>CIDADE</b>", style_bold)
        ],
        [
            Paragraph(nf_data['cliente_bairro'] or '', style_normal),
            Paragraph(nf_data['cliente_cidade'] or '', style_normal)
        ],
        [
            Paragraph("<b>UF</b>", style_bold),
            Paragraph("<b>TELEFONE</b>", style_bold)
        ],
        [
            Paragraph(nf_data['cliente_uf'] or '', style_normal),
            Paragraph(nf_data['cliente_telefone'] or '', style_normal)
        ]
    ]
    tabela = Table(dados_cliente, colWidths=[85*mm, 85*mm])
    tabela.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('BACKGROUND', (0, 2), (-1, 2), colors.lightgrey),
        ('BACKGROUND', (0, 4), (-1, 4), colors.lightgrey),
        ('BACKGROUND', (0, 6), (-1, 6), colors.lightgrey),
        ('BACKGROUND', (0, 8), (-1, 8), colors.lightgrey),
    ]))
    elementos.append(tabela)
    return elementos

def criar_secao_fatura(nf_data, style_bold, style_normal):
    elementos = []
    elementos.append(Paragraph("<b>FATURA</b>", style_bold))
    vencimento_dias = nf_data.get('vencimento', '01/01/1970')
    vencimento = f"{vencimento_dias}" if vencimento_dias else ''
    valor_locacao = nf_data.get('valor_locacao', 0)
    valor_formatado = util.formatar_moeda(valor_locacao)
    #valor = util.formatar_moeda(nf_data['valor'])
    dados_fatura = [
        [Paragraph("<b>VENCIMENTO</b>", style_bold), 
         Paragraph("<b>VALOR</b>", style_bold), 
         Paragraph("<b>VALOR POR EXTENSO</b>", style_bold)],
        [Paragraph(vencimento, style_normal), 
         Paragraph(valor_formatado, style_normal), 
         Paragraph(nf_data.get('valor_por_extenso', ''), style_normal)]
    ]
    tabela = Table(dados_fatura, colWidths=[30*mm, 30*mm, 110*mm])
    tabela.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('BOX', (0, 0), (-1, -1), 1, colors.black), ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.grey), ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey)]))
    elementos.append(tabela)
    return elementos

def criar_tabela_produtos(nf_data):
    dados = [
        [Paragraph("<b>CÓD</b>", ParagraphStyle('center', alignment=TA_CENTER, fontSize=8)),
         Paragraph("<b>DESCRIÇÃO</b>", ParagraphStyle('center', alignment=TA_CENTER, fontSize=8)),
         Paragraph("<b>UNID</b>", ParagraphStyle('center', alignment=TA_CENTER, fontSize=8)),
         Paragraph("<b>QUANT</b>", ParagraphStyle('center', alignment=TA_CENTER, fontSize=8)),
         Paragraph("<b>VALOR UNIT</b>", ParagraphStyle('center', alignment=TA_CENTER, fontSize=8)),
         Paragraph("<b>VALOR TOTAL</b>", ParagraphStyle('center', alignment=TA_CENTER, fontSize=8))]
    ]
    style_item = ParagraphStyle('item', fontSize=8)
    for item in nf_data['itens']:
        dados.append([
            Paragraph(item['codigo_produto'], style_item),
            Paragraph(item['descricao'], style_item),
            Paragraph(item['unidade'], ParagraphStyle('center', alignment=TA_CENTER, fontSize=8)),
            Paragraph(f"{item['quantidade']:.2f}", ParagraphStyle('center', alignment=TA_CENTER, fontSize=8)),
            Paragraph(util.formatar_moeda(item['valor_unitario']), 
                     ParagraphStyle('right', alignment=TA_RIGHT, fontSize=8)),
            Paragraph(util.formatar_moeda(item['valor_total']),
                     ParagraphStyle('right', alignment=TA_RIGHT, fontSize=8))
        ])
    while len(dados) < 6:
        dados.append(['', '', '', '', '', '']) 
    tabela = Table(dados, colWidths=[20*mm, 70*mm, 15*mm, 20*mm, 25*mm, 25*mm])
    tabela.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4472C4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ]))
    return tabela

def criar_secao_totais(nf_data):
    dados = [
        [
            Paragraph("* EMPRESA NÃO OBRIGADA A EMISSÃO DE NOTA FISCAL PARA LOCAÇÃO DE BENS MÓVEIS,\n"
                     "CONFORME DETERMINA LEI COMPLEMENTAR Nº 116/2003", 
                     ParagraphStyle('legal', fontSize=7, leading=9)),
            Paragraph("<b>VALOR DA LOCAÇÃO</b>", ParagraphStyle('center', alignment=TA_CENTER, fontSize=10)), util.formatar_moeda(nf_data['valor_locacao'])
        ],
        [
            "",
            "VALOR TOTAL",
            util.formatar_moeda(nf_data['valor_total_nota'])
        ]
    ]
    tabela = Table(dados, colWidths=[85*mm, 42.5*mm, 42.5*mm])
    tabela.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (1, 0), (-1, -1), 10),
        ('FONTNAME', (2, 0), (2, 0), 'Helvetica-Bold'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('SPAN', (0, 0), (0, 1))
    ]))
    return tabela

def criar_secao_observacoes(nf_data, style_bold, style_normal):
    elementos = []
    elementos.append(Paragraph("<b>DADOS ADICIONAIS</b>", style_bold))
    elementos.append(Paragraph("<b>OBSERVAÇÕES:</b>", style_bold))
    elementos.append(Paragraph(nf_data['observacoes'], style_normal))
    return elementos

def criar_rodape(nf_data, style_bold, style_normal):
    elementos = []
    elementos.append(Paragraph("<b>-----------------------------------------------------------------------------------------------------------------------------------------------------------</b>", style_bold))
    elementos.append(Paragraph(f"<b>RECEBEMOS DE 60.067.070 - Sonia Maria Leobons da Silva OS PRODUTOS CONSTANTES DESSA NOTA FATURA nº {str(nf_data['numero_nf'])}</b>", style_bold))
    elementos.append(Paragraph("<b></b>", style_bold))
    elementos.append(Paragraph("<b>DATA DO RECEBIMENTO</b>", style_bold))
    elementos.append(Paragraph("<b></b>", style_bold))
    elementos.append(Paragraph("<b>IDENTIFICAÇÃO E ASSINATURA DO RECEBEDOR</b>", style_bold))
    #elementos.append(Paragraph(str(nf_data['numero_nf']), style_normal))
    return elementos

def formatar_data(data_str):
    if not data_str:
        return ''
    try:
        from datetime import datetime
        dt = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
        return dt.strftime("%d/%m/%Y")
    except:
        return data_str