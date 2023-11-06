import PyPDF2

# Abra o arquivo PDF

adicoes = {}
lineIsBugged = False

with open('di.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Obtenha o número de páginas no PDF
    num_pages = len(pdf_reader.pages)
    print(f"O PDF tem {num_pages} páginas.")

    # Percorra cada página do PDF
    pegando_texto = False
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]

        # Extraia o texto da página atual
        page_text = page.extract_text()
        lines = page_text.split('\n')

        text_acumulado = []  # Para acumular o texto entre as ocorrências de 'ADICAO.............:'
        
        for line in lines:
            if 'Adição: ' in line: # Assim que terminar as adições resumidas e começar as adições detalhadas não pegar mais textos
                pegando_texto = False

            if 'ADICAO.............:' in line:
                if pegando_texto:
                    texto_completo = '\n'.join(text_acumulado)
                    print()
                    print(f"Texto entre 'ADICAO.............:' na página {page_num + 1}:\n{texto_completo}")
                    text_acumulado = []
                    pegando_texto = False
                pegando_texto = True

                textos = line.split()
                num_adicao = textos[1]
                ncm = textos[3]

                adicoes[num_adicao] = {}
                adicoes[num_adicao]['NCM'] = ncm

            elif pegando_texto:
                
                if 'Valor Aduaneiro....: ' in line:
                    texto = line.split('Valor Aduaneiro....: ')
                    valor_arduaneiro = float(texto[1].replace('.', '').replace(',', '.'))
                    adicoes[num_adicao]['Valor_Arduaneiro'] = valor_arduaneiro
                    #text_acumulado.append(line)
                if 'II.................: ' in line:
                    texto = line.split()
                    aliquota_II = float(texto[1].replace('.','').replace(',','.'))
                    valor_II = float(texto[5].replace('.','').replace(',','.'))
                    adicoes[num_adicao]['II'] = {}
                    adicoes[num_adicao]['II']['aliquota_II'] = aliquota_II  
                    adicoes[num_adicao]['II']['valor_II'] = valor_II
                if 'IPI................: ' in line:
                    texto = line.split()
                    aliquota_IPI = float(texto[1].replace('.','').replace(',','.'))
                    valor_IPI = float(texto[5].replace('.','').replace(',','.'))
                    adicoes[num_adicao]['IPI'] = {}
                    adicoes[num_adicao]['IPI']['aliquota_IPI'] = aliquota_IPI  
                    adicoes[num_adicao]['IPI']['valor_IPI'] = valor_IPI
                if 'Taxa Siscomex......: ' in line:
                    texto = line.split('Taxa Siscomex......: ')
                    taxa_siscomex = float(texto[1].replace('.','').replace(',','.'))
                    adicoes[num_adicao]['taxa_siscomex'] = taxa_siscomex
                if 'Base Calculo PIS...: ' in line:
                    texto = line.split('Base Calculo PIS...: ')
                    base_IPI = float(texto[1].replace('.','').replace(',','.'))
                    adicoes[num_adicao]['base_IPI'] = base_IPI
                if line == 'PIS..............':
                    lineIsBugged = True
                    continue
                if lineIsBugged:
                    texto = line.split()
                    aliquota_PIS = float(texto[1].replace('.','').replace(',','.'))
                    valor_PIS = float(texto[5].replace('.','').replace(',','.'))
                    adicoes[num_adicao]['PIS'] = {}
                    adicoes[num_adicao]['PIS']['aliquota_PIS'] = aliquota_PIS
                    adicoes[num_adicao]['PIS']['valor_PIS'] = valor_PIS
                    lineIsBugged = False
                print(adicoes)

        # Certifique-se de lidar com o último bloco de texto acumulado, se houver
        if pegando_texto and text_acumulado:
            texto_completo = '\n'.join(text_acumulado)
            print()
            print(f"Texto entre 'ADICAO.............:' na página {page_num + 1}:\n{texto_completo}")