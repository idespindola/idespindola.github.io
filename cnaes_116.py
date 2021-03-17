import requests
import json

lista_cnaes = [
    {
        "CodigoServicoMunicipal": "1011205",
        "DescricaoServicoMunicipal": "Matadouro - abate de reses sob contrato, exceto abate de suínos",
        "CodigoServicoFederal": "17.05",
        "DescricaoServicoFederal": "Fornecimento de mão-de-obra, mesmo em caráter temporário, inclusive de empregados ou trabalhadores, avulsos ou temporários, contratados pelo prestador de serviço."
    },
    {
        "CodigoServicoMunicipal": "1012104",
        "DescricaoServicoMunicipal": "Matadouro - abate de suínos sob contrato",
        "CodigoServicoFederal": "17.05",
        "DescricaoServicoFederal": "Fornecimento de mão-de-obra, mesmo em caráter temporário, inclusive de empregados ou trabalhadores, avulsos ou temporários, contratados pelo prestador de serviço."
    },
    {
        "CodigoServicoMunicipal": "1340501",
        "DescricaoServicoMunicipal": "Estamparia e texturização em fios, tecidos, artefatos têxteis e peças ",
        "CodigoServicoFederal": "14.05",
        "DescricaoServicoFederal": "Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "1340502",
        "DescricaoServicoMunicipal": "Alvejamento, tingimento e torção em fios, tecidos, artefatos têxteis e",
        "CodigoServicoFederal": "14.10",
        "DescricaoServicoFederal": "Tinturaria e lavanderia."
    },
    {
        "CodigoServicoMunicipal": "1340599",
        "DescricaoServicoMunicipal": "Outros serviços de acabamento em fios, tecidos, artefatos têxteis e pe",
        "CodigoServicoFederal": "14.09",
        "DescricaoServicoFederal": "Alfaiataria e costura, quando o material for fornecido pelo usuário final, exceto aviamento."
    },
    {
        "CodigoServicoMunicipal": "1340599",
        "DescricaoServicoMunicipal": "Outros serviços de acabamento em fios, tecidos, artefatos têxteis e pe",
        "CodigoServicoFederal": "14.10",
        "DescricaoServicoFederal": "Tinturaria e lavanderia."
    },
    {
        "CodigoServicoMunicipal": "1412602",
        "DescricaoServicoMunicipal": "Confecção, sob medida, de peças do vestuário, exceto roupas íntimas",
        "CodigoServicoFederal": "14.09",
        "DescricaoServicoFederal": "Alfaiataria e costura, quando o material for fornecido pelo usuário final, exceto aviamento."
    },
    {
        "CodigoServicoMunicipal": "1413402",
        "DescricaoServicoMunicipal": "Confecção, sob medida, de roupas profissionais",
        "CodigoServicoFederal": "14.09",
        "DescricaoServicoFederal": "Alfaiataria e costura, quando o material for fornecido pelo usuário final, exceto aviamento."
    },
    {
        "CodigoServicoMunicipal": "1531902",
        "DescricaoServicoMunicipal": "Acabamento de calçados de couro sob contrato",
        "CodigoServicoFederal": "14.09",
        "DescricaoServicoFederal": "Alfaiataria e costura, quando o material for fornecido pelo usuário final, exceto aviamento."
    },
    {
        "CodigoServicoMunicipal": "161002",
        "DescricaoServicoMunicipal": "Serviço de poda de árvores para lavouras",
        "CodigoServicoFederal": "07.16",
        "DescricaoServicoFederal": "Florestamento, reflorestamento, semeadura, adubação, reparação de solo, plantio, silagem, colheita, corte e descascamento de árvores, silvicultura, exploração florestal e dos serviços congêneres indissociáveis da formação, manutenção e colheita de florestas, para quaisquer fins e por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "161003",
        "DescricaoServicoMunicipal": "Serviço de preparação de terreno, cultivo e colheita",
        "CodigoServicoFederal": "07.16",
        "DescricaoServicoFederal": "Florestamento, reflorestamento, semeadura, adubação, reparação de solo, plantio, silagem, colheita, corte e descascamento de árvores, silvicultura, exploração florestal e dos serviços congêneres indissociáveis da formação, manutenção e colheita de florestas, para quaisquer fins e por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "1622699",
        "DescricaoServicoMunicipal": "Fabricação de outros artigos de carpintaria para construção",
        "CodigoServicoFederal": "14.13",
        "DescricaoServicoFederal": "Carpintaria e serralheria."
    },
    {
        "CodigoServicoMunicipal": "162801",
        "DescricaoServicoMunicipal": "Serviço de inseminação artificial em animais",
        "CodigoServicoFederal": "05.04",
        "DescricaoServicoFederal": "Inseminação artificial, fertilização in vitro e congêneres."
    },
    {
        "CodigoServicoMunicipal": "162802",
        "DescricaoServicoMunicipal": "Serviço de tosquiamento de ovinos",
        "CodigoServicoFederal": "05.08",
        "DescricaoServicoFederal": "Guarda, tratamento, amestramento, embelezamento, alojamento e congêneres."
    },
    {
        "CodigoServicoMunicipal": "162803",
        "DescricaoServicoMunicipal": "Serviço de manejo de animais",
        "CodigoServicoFederal": "05.08",
        "DescricaoServicoFederal": "Guarda, tratamento, amestramento, embelezamento, alojamento e congêneres."
    },
    {
        "CodigoServicoMunicipal": "162899",
        "DescricaoServicoMunicipal": "Atividades de apoio à pecuária não especificadas anteriormente",
        "CodigoServicoFederal": "05.08",
        "DescricaoServicoFederal": "Guarda, tratamento, amestramento, embelezamento, alojamento e congêneres."
    },
    {
        "CodigoServicoMunicipal": "162899",
        "DescricaoServicoMunicipal": "Atividades de apoio à pecuária não especificadas anteriormente",
        "CodigoServicoFederal": "17.01",
        "DescricaoServicoFederal": "Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista; análise, exame, pesquisa, coleta, compilação e fornecimento de dados e informações de qualquer natureza, inclusive cadastro e similares."
    },
    {
        "CodigoServicoMunicipal": "1811301",
        "DescricaoServicoMunicipal": "Impressão de jornais",
        "CodigoServicoFederal": "13.05",
        "DescricaoServicoFederal": "Composição gráfica, inclusive confecção de impressos gráficos, fotocomposição, clicheria, zincografia, litografia e fotolitografia, exceto se destinados a posterior operação de comercialização ou industrialização, ainda que incorporados, de qualquer forma, a outra mercadoria que deva ser objeto de posterior circulação, tais como bulas, rótulos, etiquetas, caixas, cartuchos, embalagens e manuais técnicos e de instrução, quando ficarão sujeitos ao ICMS."
    },
    {
        "CodigoServicoMunicipal": "1811302",
        "DescricaoServicoMunicipal": "Impressão de livros, revistas e outras publicações periódicas",
        "CodigoServicoFederal": "13.05",
        "DescricaoServicoFederal": "Composição gráfica, inclusive confecção de impressos gráficos, fotocomposição, clicheria, zincografia, litografia e fotolitografia, exceto se destinados a posterior operação de comercialização ou industrialização, ainda que incorporados, de qualquer forma, a outra mercadoria que deva ser objeto de posterior circulação, tais como bulas, rótulos, etiquetas, caixas, cartuchos, embalagens e manuais técnicos e de instrução, quando ficarão sujeitos ao ICMS."
    },
    {
        "CodigoServicoMunicipal": "1812100",
        "DescricaoServicoMunicipal": "Impressão de material de segurança",
        "CodigoServicoFederal": "13.05",
        "DescricaoServicoFederal": "Composição gráfica, inclusive confecção de impressos gráficos, fotocomposição, clicheria, zincografia, litografia e fotolitografia, exceto se destinados a posterior operação de comercialização ou industrialização, ainda que incorporados, de qualquer forma, a outra mercadoria que deva ser objeto de posterior circulação, tais como bulas, rótulos, etiquetas, caixas, cartuchos, embalagens e manuais técnicos e de instrução, quando ficarão sujeitos ao ICMS."
    },
    {
        "CodigoServicoMunicipal": "1813001",
        "DescricaoServicoMunicipal": "Impressão de material para uso publicitário",
        "CodigoServicoFederal": "13.05",
        "DescricaoServicoFederal": "Composição gráfica, inclusive confecção de impressos gráficos, fotocomposição, clicheria, zincografia, litografia e fotolitografia, exceto se destinados a posterior operação de comercialização ou industrialização, ainda que incorporados, de qualquer forma, a outra mercadoria que deva ser objeto de posterior circulação, tais como bulas, rótulos, etiquetas, caixas, cartuchos, embalagens e manuais técnicos e de instrução, quando ficarão sujeitos ao ICMS."
    },
    {
        "CodigoServicoMunicipal": "1813099",
        "DescricaoServicoMunicipal": "Impressão de material para outros usos",
        "CodigoServicoFederal": "13.05",
        "DescricaoServicoFederal": "Composição gráfica, inclusive confecção de impressos gráficos, fotocomposição, clicheria, zincografia, litografia e fotolitografia, exceto se destinados a posterior operação de comercialização ou industrialização, ainda que incorporados, de qualquer forma, a outra mercadoria que deva ser objeto de posterior circulação, tais como bulas, rótulos, etiquetas, caixas, cartuchos, embalagens e manuais técnicos e de instrução, quando ficarão sujeitos ao ICMS."
    },
    {
        "CodigoServicoMunicipal": "1821100",
        "DescricaoServicoMunicipal": "Serviços de pré-impressão",
        "CodigoServicoFederal": "13.05",
        "DescricaoServicoFederal": "Composição gráfica, inclusive confecção de impressos gráficos, fotocomposição, clicheria, zincografia, litografia e fotolitografia, exceto se destinados a posterior operação de comercialização ou industrialização, ainda que incorporados, de qualquer forma, a outra mercadoria que deva ser objeto de posterior circulação, tais como bulas, rótulos, etiquetas, caixas, cartuchos, embalagens e manuais técnicos e de instrução, quando ficarão sujeitos ao ICMS."
    },
    {
        "CodigoServicoMunicipal": "1822901",
        "DescricaoServicoMunicipal": "Serviços de encadernação e plastificação",
        "CodigoServicoFederal": "13.05",
        "DescricaoServicoFederal": "Composição gráfica, inclusive confecção de impressos gráficos, fotocomposição, clicheria, zincografia, litografia e fotolitografia, exceto se destinados a posterior operação de comercialização ou industrialização, ainda que incorporados, de qualquer forma, a outra mercadoria que deva ser objeto de posterior circulação, tais como bulas, rótulos, etiquetas, caixas, cartuchos, embalagens e manuais técnicos e de instrução, quando ficarão sujeitos ao ICMS."
    },
    {
        "CodigoServicoMunicipal": "1822999",
        "DescricaoServicoMunicipal": "Serviços de acabamentos gráficos, exceto encadernação e plastificação",
        "CodigoServicoFederal": "14.08",
        "DescricaoServicoFederal": "Encadernação, gravação e douração de livros, revistas e congêneres."
    },
    {
        "CodigoServicoMunicipal": "1830001",
        "DescricaoServicoMunicipal": "Reprodução de som em qualquer suporte",
        "CodigoServicoFederal": "13.02",
        "DescricaoServicoFederal": "Fonografia ou gravação de sons, inclusive trucagem, dublagem, mixagem e congêneres."
    },
    {
        "CodigoServicoMunicipal": "1830002",
        "DescricaoServicoMunicipal": "Reprodução de vídeo em qualquer suporte",
        "CodigoServicoFederal": "13.03",
        "DescricaoServicoFederal": "Fotografia e cinematografia, inclusive revelação, ampliação, cópia, reprodução, trucagem e congêneres."
    },
    {
        "CodigoServicoMunicipal": "1830003",
        "DescricaoServicoMunicipal": "Reprodução de software em qualquer suporte",
        "CodigoServicoFederal": "01.03",
        "DescricaoServicoFederal": "Processamento, armazenamento ou hospedagem de dados, textos, imagens, vídeos, páginas eletrônicas, aplicativos e sistemas de informação, entre outros formatos, e congêneres."
    },
    {
        "CodigoServicoMunicipal": "2212900",
        "DescricaoServicoMunicipal": "Reforma de pneumáticos usados",
        "CodigoServicoFederal": "14.04",
        "DescricaoServicoFederal": "Recauchutagem ou regeneração de pneus."
    },
    {
        "CodigoServicoMunicipal": "2330305",
        "DescricaoServicoMunicipal": "Preparação de massa de concreto e argamassa para construção",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "2391501",
        "DescricaoServicoMunicipal": "Britamento de pedras, exceto associado à extração",
        "CodigoServicoFederal": "07.01",
        "DescricaoServicoFederal": "Engenharia, agronomia, agrimensura, arquitetura, geologia, urbanismo, paisagismo e congêneres."
    },
    {
        "CodigoServicoMunicipal": "2391501",
        "DescricaoServicoMunicipal": "Britamento de pedras, exceto associado à extração",
        "CodigoServicoFederal": "14.05",
        "DescricaoServicoFederal": "Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "2391502",
        "DescricaoServicoMunicipal": "Aparelhamento de pedras para construção, exceto associado à extração",
        "CodigoServicoFederal": "14.05",
        "DescricaoServicoFederal": "Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "2391503",
        "DescricaoServicoMunicipal": "Aparelhamento de placas e execução de trabalhos em mármore, granito, a",
        "CodigoServicoFederal": "14.05",
        "DescricaoServicoFederal": "Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "2399101",
        "DescricaoServicoMunicipal": "Decoração, lapidação, gravação, vitrificação e outros trabalhos em cer",
        "CodigoServicoFederal": "14.13",
        "DescricaoServicoFederal": "Carpintaria e serralheria."
    },
    {
        "CodigoServicoMunicipal": "2512800",
        "DescricaoServicoMunicipal": "Fabricação de esquadrias de metal",
        "CodigoServicoFederal": "14.13",
        "DescricaoServicoFederal": "Carpintaria e serralheria."
    },
    {
        "CodigoServicoMunicipal": "2539001",
        "DescricaoServicoMunicipal": "Serviços de usinagem, tornearia e solda",
        "CodigoServicoFederal": "14.05",
        "DescricaoServicoFederal": "Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "2539002",
        "DescricaoServicoMunicipal": "Serviços de tratamento e revestimento em metais",
        "CodigoServicoFederal": "14.05",
        "DescricaoServicoFederal": "Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "2542000",
        "DescricaoServicoMunicipal": "Fabricação de artigos de serralheria, exceto esquadrias",
        "CodigoServicoFederal": "14.13",
        "DescricaoServicoFederal": "Carpintaria e serralheria."
    },
    {
        "CodigoServicoMunicipal": "2599302",
        "DescricaoServicoMunicipal": "Serviço de corte e dobra de metais",
        "CodigoServicoFederal": "14.05",
        "DescricaoServicoFederal": "Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "2722802",
        "DescricaoServicoMunicipal": "Recondicionamento de baterias e acumuladores para veículos automotores",
        "CodigoServicoFederal": "14.05",
        "DescricaoServicoFederal": "Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "2950600",
        "DescricaoServicoMunicipal": "Recondicionamento e recuperação de motores para veículos automotores",
        "CodigoServicoFederal": "14.03",
        "DescricaoServicoFederal": "Recondicionamento de motores (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "311604",
        "DescricaoServicoMunicipal": "Atividades de apoio à pesca em água salgada",
        "CodigoServicoFederal": "17.01",
        "DescricaoServicoFederal": "Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista; análise, exame, pesquisa, coleta, compilação e fornecimento de dados e informações de qualquer natureza, inclusive cadastro e similares."
    },
    {
        "CodigoServicoMunicipal": "311604",
        "DescricaoServicoMunicipal": "Atividades de apoio à pesca em água salgada",
        "CodigoServicoFederal": "20.01",
        "DescricaoServicoFederal": "Serviços portuários, ferroportuários, utilização de porto, movimentação de passageiros, reboque de embarcações, rebocador escoteiro, atracação, desatracação, serviços de praticagem, capatazia, armazenagem de qualquer natureza, serviços acessórios, movimentação de mercadorias, serviços de apoio marítimo, de movimentação ao largo, serviços de armadores, estiva, conferência, logística e congêneres."
    },
    {
        "CodigoServicoMunicipal": "312404",
        "DescricaoServicoMunicipal": "Atividades de apoio à pesca em água doce",
        "CodigoServicoFederal": "17.01",
        "DescricaoServicoFederal": "Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista; análise, exame, pesquisa, coleta, compilação e fornecimento de dados e informações de qualquer natureza, inclusive cadastro e similares."
    },
    {
        "CodigoServicoMunicipal": "312404",
        "DescricaoServicoMunicipal": "Atividades de apoio à pesca em água doce",
        "CodigoServicoFederal": "20.01",
        "DescricaoServicoFederal": "Serviços portuários, ferroportuários, utilização de porto, movimentação de passageiros, reboque de embarcações, rebocador escoteiro, atracação, desatracação, serviços de praticagem, capatazia, armazenagem de qualquer natureza, serviços acessórios, movimentação de mercadorias, serviços de apoio marítimo, de movimentação ao largo, serviços de armadores, estiva, conferência, logística e congêneres."
    },
    {
        "CodigoServicoMunicipal": "3211601",
        "DescricaoServicoMunicipal": "Lapidação de gemas",
        "CodigoServicoFederal": "39.01",
        "DescricaoServicoFederal": "Serviços de ourivesaria e lapidação (quando o material for fornecido pelo tomador do serviço)."
    },
    {
        "CodigoServicoMunicipal": "321305",
        "DescricaoServicoMunicipal": "Atividades de apoio à aqüicultura em água salgada e salobra",
        "CodigoServicoFederal": "17.01",
        "DescricaoServicoFederal": "Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista; análise, exame, pesquisa, coleta, compilação e fornecimento de dados e informações de qualquer natureza, inclusive cadastro e similares."
    },
    {
        "CodigoServicoMunicipal": "321305",
        "DescricaoServicoMunicipal": "Atividades de apoio à aqüicultura em água salgada e salobra",
        "CodigoServicoFederal": "20.01",
        "DescricaoServicoFederal": "Serviços portuários, ferroportuários, utilização de porto, movimentação de passageiros, reboque de embarcações, rebocador escoteiro, atracação, desatracação, serviços de praticagem, capatazia, armazenagem de qualquer natureza, serviços acessórios, movimentação de mercadorias, serviços de apoio marítimo, de movimentação ao largo, serviços de armadores, estiva, conferência, logística e congêneres."
    },
    {
        "CodigoServicoMunicipal": "3250703",
        "DescricaoServicoMunicipal": "Fabricação de aparelhos e utensílios para correção de defeitos físicos",
        "CodigoServicoFederal": "04.14",
        "DescricaoServicoFederal": "Próteses sob encomenda."
    },
    {
        "CodigoServicoMunicipal": "3250706",
        "DescricaoServicoMunicipal": "Serviços de prótese dentária",
        "CodigoServicoFederal": "04.14",
        "DescricaoServicoFederal": "Próteses sob encomenda."
    },
    {
        "CodigoServicoMunicipal": "3250709",
        "DescricaoServicoMunicipal": "Serviço de laboratório óptico",
        "CodigoServicoFederal": "14.05",
        "DescricaoServicoFederal": "Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "3311200",
        "DescricaoServicoMunicipal": "Manutenção e reparação de tanques, reservatórios metálicos e caldeiras",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3312102",
        "DescricaoServicoMunicipal": "Manutenção e reparação de aparelhos e instrumentos de medida, teste e ",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3312103",
        "DescricaoServicoMunicipal": "Manutenção e reparação de aparelhos eletromédicos e eletroterapêuticos",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3312104",
        "DescricaoServicoMunicipal": "Manutenção e reparação de equipamentos e instrumentos ópticos",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3313901",
        "DescricaoServicoMunicipal": "Manutenção e reparação de geradores, transformadores e motores elétric",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3313902",
        "DescricaoServicoMunicipal": "Manutenção e reparação de baterias e acumuladores elétricos, exceto pa",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3313999",
        "DescricaoServicoMunicipal": "Manutenção e reparação de máquinas, aparelhos e materiais elétricos nã",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314701",
        "DescricaoServicoMunicipal": "Manutenção e reparação de máquinas motrizes não-elétricas",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314702",
        "DescricaoServicoMunicipal": "Manutenção e reparação de equipamentos hidráulicos e pneumáticos, exce",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314703",
        "DescricaoServicoMunicipal": "Manutenção e reparação de válvulas industriais",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314704",
        "DescricaoServicoMunicipal": "Manutenção e reparação de compressores",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314705",
        "DescricaoServicoMunicipal": "Manutenção e reparação de equipamentos de transmissão para fins indust",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314706",
        "DescricaoServicoMunicipal": "Manutenção e reparação de máquinas, aparelhos e equipamentos para inst",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314707",
        "DescricaoServicoMunicipal": "Manutenção e reparação de máquinas e aparelhos de refrigeração e venti",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314708",
        "DescricaoServicoMunicipal": "Manutenção e reparação de máquinas, equipamentos e aparelhos para tran",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314709",
        "DescricaoServicoMunicipal": "Manutenção e reparação de máquinas de escrever, calcular e de outros e",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314710",
        "DescricaoServicoMunicipal": "Manutenção e reparação de máquinas e equipamentos para uso geral não e",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314711",
        "DescricaoServicoMunicipal": "Manutenção e reparação de máquinas e equipamentos para agricultura e p",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314712",
        "DescricaoServicoMunicipal": "Manutenção e reparação de tratores agrícolas",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314713",
        "DescricaoServicoMunicipal": "Manutenção e reparação de máquinas-ferramenta",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314714",
        "DescricaoServicoMunicipal": "Manutenção e reparação de máquinas e equipamentos para a prospecção e ",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314715",
        "DescricaoServicoMunicipal": "Manutenção e reparação de máquinas e equipamentos para uso na extração",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314716",
        "DescricaoServicoMunicipal": "Manutenção e reparação de tratores, exceto agrícolas",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314717",
        "DescricaoServicoMunicipal": "Manutenção e reparação de máquinas e equipamentos de terraplenagem, pa",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314718",
        "DescricaoServicoMunicipal": "Manutenção e reparação de máquinas para a indústria metalúrgica, excet",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314719",
        "DescricaoServicoMunicipal": "Manutenção e reparação de máquinas e equipamentos para as indústrias d",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314720",
        "DescricaoServicoMunicipal": "Manutenção e reparação de máquinas e equipamentos para a indústria têx",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314721",
        "DescricaoServicoMunicipal": "Manutenção e reparação de máquinas e aparelhos para a indústria de cel",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314722",
        "DescricaoServicoMunicipal": "Manutenção e reparação de máquinas e aparelhos para a indústria do plá",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3314799",
        "DescricaoServicoMunicipal": "Manutenção e reparação de outras máquinas e equipamentos para usos ind",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3315500",
        "DescricaoServicoMunicipal": "Manutenção e reparação de veículos ferroviários",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3316301",
        "DescricaoServicoMunicipal": "Manutenção e reparação de aeronaves, exceto a manutenção na pista",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3316302",
        "DescricaoServicoMunicipal": "Manutenção de aeronaves na pista",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3317101",
        "DescricaoServicoMunicipal": "Manutenção e reparação de embarcações e estruturas flutuantes",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3317102",
        "DescricaoServicoMunicipal": "Manutenção e reparação de embarcações para esporte e lazer",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3319800",
        "DescricaoServicoMunicipal": "Manutenção e reparação de equipamentos e produtos não especificados an",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "3321000",
        "DescricaoServicoMunicipal": "Instalação de máquinas e equipamentos industriais",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "3329501",
        "DescricaoServicoMunicipal": "Serviços de montagem de móveis de qualquer material",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "3329501",
        "DescricaoServicoMunicipal": "Serviços de montagem de móveis de qualquer material",
        "CodigoServicoFederal": "14.13",
        "DescricaoServicoFederal": "Carpintaria e serralheria."
    },
    {
        "CodigoServicoMunicipal": "3514000",
        "DescricaoServicoMunicipal": "Distribuição de energia elétrica",
        "CodigoServicoFederal": "03.04",
        "DescricaoServicoFederal": "Locação, sublocação, arrendamento, direito de passagem ou permissão de uso, compartilhado ou não, de ferrovia, rodovia, postes, cabos, dutos e condutos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "3520402",
        "DescricaoServicoMunicipal": "Distribuição de combustíveis gasosos por redes urbanas",
        "CodigoServicoFederal": "03.04",
        "DescricaoServicoFederal": "Locação, sublocação, arrendamento, direito de passagem ou permissão de uso, compartilhado ou não, de ferrovia, rodovia, postes, cabos, dutos e condutos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "3702900",
        "DescricaoServicoMunicipal": "Atividades relacionadas a esgoto, exceto a gestão de redes",
        "CodigoServicoFederal": "07.10",
        "DescricaoServicoFederal": "Limpeza, manutenção e conservação de vias e logradouros públicos, imóveis, chaminés, piscinas, parques, jardins e congêneres."
    },
    {
        "CodigoServicoMunicipal": "3811400",
        "DescricaoServicoMunicipal": "Coleta de resíduos não-perigosos",
        "CodigoServicoFederal": "07.09",
        "DescricaoServicoFederal": "Varrição, coleta, remoção, incineração, tratamento, reciclagem, separação e destinação final de lixo, rejeitos e outros resíduos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "3811400",
        "DescricaoServicoMunicipal": "Coleta de resíduos não-perigosos",
        "CodigoServicoFederal": "11.04",
        "DescricaoServicoFederal": "Armazenamento, depósito, carga, descarga, arrumação e guarda de bens de qualquer espécie."
    },
    {
        "CodigoServicoMunicipal": "3812200",
        "DescricaoServicoMunicipal": "Coleta de resíduos perigosos",
        "CodigoServicoFederal": "07.09",
        "DescricaoServicoFederal": "Varrição, coleta, remoção, incineração, tratamento, reciclagem, separação e destinação final de lixo, rejeitos e outros resíduos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "3812200",
        "DescricaoServicoMunicipal": "Coleta de resíduos perigosos",
        "CodigoServicoFederal": "11.04",
        "DescricaoServicoFederal": "Armazenamento, depósito, carga, descarga, arrumação e guarda de bens de qualquer espécie."
    },
    {
        "CodigoServicoMunicipal": "3821100",
        "DescricaoServicoMunicipal": "Tratamento e disposição de resíduos não-perigosos",
        "CodigoServicoFederal": "07.09",
        "DescricaoServicoFederal": "Varrição, coleta, remoção, incineração, tratamento, reciclagem, separação e destinação final de lixo, rejeitos e outros resíduos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "3822000",
        "DescricaoServicoMunicipal": "Tratamento e disposição de resíduos perigosos",
        "CodigoServicoFederal": "07.09",
        "DescricaoServicoFederal": "Varrição, coleta, remoção, incineração, tratamento, reciclagem, separação e destinação final de lixo, rejeitos e outros resíduos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "3822000",
        "DescricaoServicoMunicipal": "Tratamento e disposição de resíduos perigosos",
        "CodigoServicoFederal": "07.12",
        "DescricaoServicoFederal": "Controle e tratamento de efluentes de qualquer natureza e de agentes físicos, químicos e biológicos."
    },
    {
        "CodigoServicoMunicipal": "3831901",
        "DescricaoServicoMunicipal": "Recuperação de sucatas de alumínio",
        "CodigoServicoFederal": "07.09",
        "DescricaoServicoFederal": "Varrição, coleta, remoção, incineração, tratamento, reciclagem, separação e destinação final de lixo, rejeitos e outros resíduos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "3831999",
        "DescricaoServicoMunicipal": "Recuperação de materiais metálicos, exceto alumínio",
        "CodigoServicoFederal": "07.09",
        "DescricaoServicoFederal": "Varrição, coleta, remoção, incineração, tratamento, reciclagem, separação e destinação final de lixo, rejeitos e outros resíduos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "3832700",
        "DescricaoServicoMunicipal": "Recuperação de materiais plásticos",
        "CodigoServicoFederal": "07.09",
        "DescricaoServicoFederal": "Varrição, coleta, remoção, incineração, tratamento, reciclagem, separação e destinação final de lixo, rejeitos e outros resíduos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "3839401",
        "DescricaoServicoMunicipal": "Usinas de compostagem",
        "CodigoServicoFederal": "07.09",
        "DescricaoServicoFederal": "Varrição, coleta, remoção, incineração, tratamento, reciclagem, separação e destinação final de lixo, rejeitos e outros resíduos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "3839401",
        "DescricaoServicoMunicipal": "Usinas de compostagem",
        "CodigoServicoFederal": "07.16",
        "DescricaoServicoFederal": "Florestamento, reflorestamento, semeadura, adubação, reparação de solo, plantio, silagem, colheita, corte e descascamento de árvores, silvicultura, exploração florestal e dos serviços congêneres indissociáveis da formação, manutenção e colheita de florestas, para quaisquer fins e por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "3839499",
        "DescricaoServicoMunicipal": "Recuperação de materiais não especificados anteriormente",
        "CodigoServicoFederal": "07.09",
        "DescricaoServicoFederal": "Varrição, coleta, remoção, incineração, tratamento, reciclagem, separação e destinação final de lixo, rejeitos e outros resíduos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "3900500",
        "DescricaoServicoMunicipal": "Descontaminação e outros serviços de gestão de resíduos",
        "CodigoServicoFederal": "07.12",
        "DescricaoServicoFederal": "Controle e tratamento de efluentes de qualquer natureza e de agentes físicos, químicos e biológicos."
    },
    {
        "CodigoServicoMunicipal": "4120400",
        "DescricaoServicoMunicipal": "Construção de edifícios",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4120400",
        "DescricaoServicoMunicipal": "Construção de edifícios",
        "CodigoServicoFederal": "07.05",
        "DescricaoServicoFederal": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4211101",
        "DescricaoServicoMunicipal": "Construção de rodovias e ferrovias",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4211101",
        "DescricaoServicoMunicipal": "Construção de rodovias e ferrovias",
        "CodigoServicoFederal": "07.05",
        "DescricaoServicoFederal": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4211102",
        "DescricaoServicoMunicipal": "Pintura para sinalização em pistas rodoviárias e aeroportos",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4211102",
        "DescricaoServicoMunicipal": "Pintura para sinalização em pistas rodoviárias e aeroportos",
        "CodigoServicoFederal": "07.05",
        "DescricaoServicoFederal": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4212000",
        "DescricaoServicoMunicipal": "Construção de obras-de-arte especiais",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4212000",
        "DescricaoServicoMunicipal": "Construção de obras-de-arte especiais",
        "CodigoServicoFederal": "07.05",
        "DescricaoServicoFederal": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4213800",
        "DescricaoServicoMunicipal": "Obras de urbanização - ruas, praças e calçadas",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4213800",
        "DescricaoServicoMunicipal": "Obras de urbanização - ruas, praças e calçadas",
        "CodigoServicoFederal": "07.10",
        "DescricaoServicoFederal": "Limpeza, manutenção e conservação de vias e logradouros públicos, imóveis, chaminés, piscinas, parques, jardins e congêneres."
    },
    {
        "CodigoServicoMunicipal": "4221901",
        "DescricaoServicoMunicipal": "Construção de barragens e represas para geração de energia elétrica",
        "CodigoServicoFederal": "07.17",
        "DescricaoServicoFederal": "Escoramento, contenção de encostas e serviços congêneres."
    },
    {
        "CodigoServicoMunicipal": "4221901",
        "DescricaoServicoMunicipal": "Construção de barragens e represas para geração de energia elétrica",
        "CodigoServicoFederal": "07.18",
        "DescricaoServicoFederal": "Limpeza e dragagem de rios, portos, canais, baías, lagos, lagoas, represas, açudes e congêneres."
    },
    {
        "CodigoServicoMunicipal": "4221902",
        "DescricaoServicoMunicipal": "Construção de estações e redes de distribuição de energia elétrica",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4221902",
        "DescricaoServicoMunicipal": "Construção de estações e redes de distribuição de energia elétrica",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "4221903",
        "DescricaoServicoMunicipal": "Manutenção de redes de distribuição de energia elétrica",
        "CodigoServicoFederal": "07.05",
        "DescricaoServicoFederal": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4221904",
        "DescricaoServicoMunicipal": "Construção de estações e redes de telecomunicações",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4221905",
        "DescricaoServicoMunicipal": "Manutenção de estações e redes de telecomunicações",
        "CodigoServicoFederal": "07.05",
        "DescricaoServicoFederal": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4222701",
        "DescricaoServicoMunicipal": "Construção de redes de abastecimento de água, coleta de esgoto e const",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4222702",
        "DescricaoServicoMunicipal": "Obras de irrigação",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4223500",
        "DescricaoServicoMunicipal": "Construção de redes de transportes por dutos, exceto para água e esgot",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4291000",
        "DescricaoServicoMunicipal": "Obras portuárias, marítimas e fluviais",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4291000",
        "DescricaoServicoMunicipal": "Obras portuárias, marítimas e fluviais",
        "CodigoServicoFederal": "07.05",
        "DescricaoServicoFederal": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4292801",
        "DescricaoServicoMunicipal": "Montagem de estruturas metálicas",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4292801",
        "DescricaoServicoMunicipal": "Montagem de estruturas metálicas",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "4292802",
        "DescricaoServicoMunicipal": "Obras de montagem industrial",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4299501",
        "DescricaoServicoMunicipal": "Construção de instalações esportivas e recreativas",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4299501",
        "DescricaoServicoMunicipal": "Construção de instalações esportivas e recreativas",
        "CodigoServicoFederal": "07.05",
        "DescricaoServicoFederal": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4299599",
        "DescricaoServicoMunicipal": "Outras obras de engenharia civil não especificadas anteriormente",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4311801",
        "DescricaoServicoMunicipal": "Demolição de edifícios e outras estruturas",
        "CodigoServicoFederal": "07.04",
        "DescricaoServicoFederal": "Demolição."
    },
    {
        "CodigoServicoMunicipal": "4311802",
        "DescricaoServicoMunicipal": "Preparação de canteiro e limpeza de terreno",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4312600",
        "DescricaoServicoMunicipal": "Perfurações e sondagens",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4313400",
        "DescricaoServicoMunicipal": "Obras de terraplenagem",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4319300",
        "DescricaoServicoMunicipal": "Serviços de preparação do terreno não especificados anteriormente",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4321500",
        "DescricaoServicoMunicipal": "Serviço de instalações elétricas, inclusive antenas",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4321500",
        "DescricaoServicoMunicipal": "Serviço de instalações elétricas, inclusive antenas",
        "CodigoServicoFederal": "07.05",
        "DescricaoServicoFederal": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4321500",
        "DescricaoServicoMunicipal": "Serviço de instalações elétricas, inclusive antenas",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "4322301",
        "DescricaoServicoMunicipal": "Instalações hidráulicas, sanitárias e de gás",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4322301",
        "DescricaoServicoMunicipal": "Instalações hidráulicas, sanitárias e de gás",
        "CodigoServicoFederal": "07.05",
        "DescricaoServicoFederal": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4322301",
        "DescricaoServicoMunicipal": "Instalações hidráulicas, sanitárias e de gás",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "4322302",
        "DescricaoServicoMunicipal": "Instalação e manutenção de sistemas centrais de ar condicionado, de ve",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4322302",
        "DescricaoServicoMunicipal": "Instalação e manutenção de sistemas centrais de ar condicionado, de ve",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4322302",
        "DescricaoServicoMunicipal": "Instalação e manutenção de sistemas centrais de ar condicionado, de ve",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "4322303",
        "DescricaoServicoMunicipal": "Instalações de sistema de prevenção contra incêndio",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4322303",
        "DescricaoServicoMunicipal": "Instalações de sistema de prevenção contra incêndio",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4322303",
        "DescricaoServicoMunicipal": "Instalações de sistema de prevenção contra incêndio",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "4329101",
        "DescricaoServicoMunicipal": "Instalação de painéis publicitários",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "4329101",
        "DescricaoServicoMunicipal": "Instalação de painéis publicitários",
        "CodigoServicoFederal": "24.01",
        "DescricaoServicoFederal": "Serviços de chaveiros, confecção de carimbos, placas, sinalização visual, banners, adesivos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "4329102",
        "DescricaoServicoMunicipal": "Instalação de equipamentos para orientação à navegação marítima, fluvi",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "4329103",
        "DescricaoServicoMunicipal": "Intalação, manutenção e reparação de elevadores, escadas e esteiras ro",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4329103",
        "DescricaoServicoMunicipal": "Intalação, manutenção e reparação de elevadores, escadas e esteiras ro",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4329103",
        "DescricaoServicoMunicipal": "Intalação, manutenção e reparação de elevadores, escadas e esteiras ro",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "4329104",
        "DescricaoServicoMunicipal": "Montagem e instalação de sistemas e equipamentos de iluminação e sinal",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4329104",
        "DescricaoServicoMunicipal": "Montagem e instalação de sistemas e equipamentos de iluminação e sinal",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "4329105",
        "DescricaoServicoMunicipal": "Tratamentos térmicos, acústicos ou de vibração",
        "CodigoServicoFederal": "07.08",
        "DescricaoServicoFederal": "Calafetação."
    },
    {
        "CodigoServicoMunicipal": "4329105",
        "DescricaoServicoMunicipal": "Tratamentos térmicos, acústicos ou de vibração",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4329199",
        "DescricaoServicoMunicipal": "Outras obras de instalações em construções não especificadas anteriorm",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4330401",
        "DescricaoServicoMunicipal": "Impermeabilização em obras de engenharia civil",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4330402",
        "DescricaoServicoMunicipal": "Instalação de portas, janelas, tetos, divisórias e armários embutidos ",
        "CodigoServicoFederal": "07.06",
        "DescricaoServicoFederal": "Colocação e instalação de tapetes, carpetes, assoalhos, cortinas, revestimentos de parede, vidros, divisórias, placas de gesso e congêneres, com material fornecido pelo tomador do serviço."
    },
    {
        "CodigoServicoMunicipal": "4330402",
        "DescricaoServicoMunicipal": "Instalação de portas, janelas, tetos, divisórias e armários embutidos ",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "4330402",
        "DescricaoServicoMunicipal": "Instalação de portas, janelas, tetos, divisórias e armários embutidos ",
        "CodigoServicoFederal": "14.13",
        "DescricaoServicoFederal": "Carpintaria e serralheria."
    },
    {
        "CodigoServicoMunicipal": "4330403",
        "DescricaoServicoMunicipal": "Obras de acabamento em gesso e estuque",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4330403",
        "DescricaoServicoMunicipal": "Obras de acabamento em gesso e estuque",
        "CodigoServicoFederal": "07.05",
        "DescricaoServicoFederal": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4330403",
        "DescricaoServicoMunicipal": "Obras de acabamento em gesso e estuque",
        "CodigoServicoFederal": "07.06",
        "DescricaoServicoFederal": "Colocação e instalação de tapetes, carpetes, assoalhos, cortinas, revestimentos de parede, vidros, divisórias, placas de gesso e congêneres, com material fornecido pelo tomador do serviço."
    },
    {
        "CodigoServicoMunicipal": "4330403",
        "DescricaoServicoMunicipal": "Obras de acabamento em gesso e estuque",
        "CodigoServicoFederal": "14.07",
        "DescricaoServicoFederal": "Colocação de molduras e congêneres."
    },
    {
        "CodigoServicoMunicipal": "4330404",
        "DescricaoServicoMunicipal": "Serviços de pintura de edifícios em geral",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4330404",
        "DescricaoServicoMunicipal": "Serviços de pintura de edifícios em geral",
        "CodigoServicoFederal": "07.05",
        "DescricaoServicoFederal": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4330405",
        "DescricaoServicoMunicipal": "Aplicação de revestimentos e de resinas em interiores e exteriores",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4330405",
        "DescricaoServicoMunicipal": "Aplicação de revestimentos e de resinas em interiores e exteriores",
        "CodigoServicoFederal": "07.05",
        "DescricaoServicoFederal": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4330405",
        "DescricaoServicoMunicipal": "Aplicação de revestimentos e de resinas em interiores e exteriores",
        "CodigoServicoFederal": "07.06",
        "DescricaoServicoFederal": "Colocação e instalação de tapetes, carpetes, assoalhos, cortinas, revestimentos de parede, vidros, divisórias, placas de gesso e congêneres, com material fornecido pelo tomador do serviço."
    },
    {
        "CodigoServicoMunicipal": "4330405",
        "DescricaoServicoMunicipal": "Aplicação de revestimentos e de resinas em interiores e exteriores",
        "CodigoServicoFederal": "07.07",
        "DescricaoServicoFederal": "Recuperação, raspagem, polimento e lustração de pisos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "4330405",
        "DescricaoServicoMunicipal": "Aplicação de revestimentos e de resinas em interiores e exteriores",
        "CodigoServicoFederal": "07.08",
        "DescricaoServicoFederal": "Calafetação."
    },
    {
        "CodigoServicoMunicipal": "4330499",
        "DescricaoServicoMunicipal": "Outras obras de acabamento da construção",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4330499",
        "DescricaoServicoMunicipal": "Outras obras de acabamento da construção",
        "CodigoServicoFederal": "07.05",
        "DescricaoServicoFederal": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4330499",
        "DescricaoServicoMunicipal": "Outras obras de acabamento da construção",
        "CodigoServicoFederal": "07.06",
        "DescricaoServicoFederal": "Colocação e instalação de tapetes, carpetes, assoalhos, cortinas, revestimentos de parede, vidros, divisórias, placas de gesso e congêneres, com material fornecido pelo tomador do serviço."
    },
    {
        "CodigoServicoMunicipal": "4391600",
        "DescricaoServicoMunicipal": "Obras de fundações",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4399101",
        "DescricaoServicoMunicipal": "Administração de obras",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4399101",
        "DescricaoServicoMunicipal": "Administração de obras",
        "CodigoServicoFederal": "07.19",
        "DescricaoServicoFederal": "Acompanhamento e fiscalização da execução de obras de engenharia, arquitetura e urbanismo."
    },
    {
        "CodigoServicoMunicipal": "4399102",
        "DescricaoServicoMunicipal": "Montagem e desmontagem de andaimes e outras estruturas temporárias",
        "CodigoServicoFederal": "03.05",
        "DescricaoServicoFederal": "Cessão de andaimes, palcos, coberturas e outras estruturas de uso temporário."
    },
    {
        "CodigoServicoMunicipal": "4399102",
        "DescricaoServicoMunicipal": "Montagem e desmontagem de andaimes e outras estruturas temporárias",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "4399103",
        "DescricaoServicoMunicipal": "Obras de alvenaria",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4399103",
        "DescricaoServicoMunicipal": "Obras de alvenaria",
        "CodigoServicoFederal": "07.05",
        "DescricaoServicoFederal": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4399104",
        "DescricaoServicoMunicipal": "Serviços de operação e fornecimento de equipamentos para transporte e ",
        "CodigoServicoFederal": "14.14",
        "DescricaoServicoFederal": "Guincho intramunicipal, guindaste e içamento."
    },
    {
        "CodigoServicoMunicipal": "4399105",
        "DescricaoServicoMunicipal": "Perfuração e construção de poços de água",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4399199",
        "DescricaoServicoMunicipal": "Serviços especializados para construção não especificados anteriorment",
        "CodigoServicoFederal": "07.02",
        "DescricaoServicoFederal": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4399199",
        "DescricaoServicoMunicipal": "Serviços especializados para construção não especificados anteriorment",
        "CodigoServicoFederal": "07.05",
        "DescricaoServicoFederal": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4399199",
        "DescricaoServicoMunicipal": "Serviços especializados para construção não especificados anteriorment",
        "CodigoServicoFederal": "07.17",
        "DescricaoServicoFederal": "Escoramento, contenção de encostas e serviços congêneres."
    },
    {
        "CodigoServicoMunicipal": "4512901",
        "DescricaoServicoMunicipal": "Representantes comerciais e agentes do comércio de veículos automotore",
        "CodigoServicoFederal": "10.09",
        "DescricaoServicoFederal": "Representação de qualquer natureza, inclusive comercial."
    },
    {
        "CodigoServicoMunicipal": "4512902",
        "DescricaoServicoMunicipal": "Comércio sob consignação de veículos automotores",
        "CodigoServicoFederal": "10.02",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "4512902",
        "DescricaoServicoMunicipal": "Comércio sob consignação de veículos automotores",
        "CodigoServicoFederal": "10.05",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de bens móveis ou imóveis, não abrangidos em outros itens ou subitens, inclusive aqueles realizados no âmbito de Bolsas de Mercadorias e Futuros, por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "4520001",
        "DescricaoServicoMunicipal": "Serviços de manutenção e reparação mecânica de veículos automotores",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4520001",
        "DescricaoServicoMunicipal": "Serviços de manutenção e reparação mecânica de veículos automotores",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "4520002",
        "DescricaoServicoMunicipal": "Serviços de lanternagem ou funilaria e pintura de veículos automotores",
        "CodigoServicoFederal": "14.05",
        "DescricaoServicoFederal": "Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "4520002",
        "DescricaoServicoMunicipal": "Serviços de lanternagem ou funilaria e pintura de veículos automotores",
        "CodigoServicoFederal": "14.12",
        "DescricaoServicoFederal": "Funilaria e lanternagem."
    },
    {
        "CodigoServicoMunicipal": "4520003",
        "DescricaoServicoMunicipal": "Serviços de manutenção e reparação elétrica de veículos automotores",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4520003",
        "DescricaoServicoMunicipal": "Serviços de manutenção e reparação elétrica de veículos automotores",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "4520004",
        "DescricaoServicoMunicipal": "Serviços de alinhamento e balanceamento de veículos automotores",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4520005",
        "DescricaoServicoMunicipal": "Serviços de lavagem, lubrificação e polimento de veículos automotores",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4520005",
        "DescricaoServicoMunicipal": "Serviços de lavagem, lubrificação e polimento de veículos automotores",
        "CodigoServicoFederal": "14.05",
        "DescricaoServicoFederal": "Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "4520006",
        "DescricaoServicoMunicipal": "Serviços de borracharia para veículos automotores",
        "CodigoServicoFederal": "14.04",
        "DescricaoServicoFederal": "Recauchutagem ou regeneração de pneus."
    },
    {
        "CodigoServicoMunicipal": "4520006",
        "DescricaoServicoMunicipal": "Serviços de borracharia para veículos automotores",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "4520007",
        "DescricaoServicoMunicipal": "Serviços de instalação, manutenção e reparação de acessórios para veíc",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4520007",
        "DescricaoServicoMunicipal": "Serviços de instalação, manutenção e reparação de acessórios para veíc",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "4520008",
        "DescricaoServicoMunicipal": "Serviços de capotaria",
        "CodigoServicoFederal": "14.11",
        "DescricaoServicoFederal": "Tapeçaria e reforma de estofamentos em geral."
    },
    {
        "CodigoServicoMunicipal": "4542101",
        "DescricaoServicoMunicipal": "Representantes comerciais e agentes do comércio de motocicletas e moto",
        "CodigoServicoFederal": "10.09",
        "DescricaoServicoFederal": "Representação de qualquer natureza, inclusive comercial."
    },
    {
        "CodigoServicoMunicipal": "4542102",
        "DescricaoServicoMunicipal": "Comércio sob consignação de motocicletas e motonetas",
        "CodigoServicoFederal": "10.02",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "4542102",
        "DescricaoServicoMunicipal": "Comércio sob consignação de motocicletas e motonetas",
        "CodigoServicoFederal": "10.05",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de bens móveis ou imóveis, não abrangidos em outros itens ou subitens, inclusive aqueles realizados no âmbito de Bolsas de Mercadorias e Futuros, por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "4543900",
        "DescricaoServicoMunicipal": "Manutenção e reparação de motocicletas e motonetas",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4611700",
        "DescricaoServicoMunicipal": "Representantes comerciais e agentes do comércio de matérias-primas agr",
        "CodigoServicoFederal": "10.09",
        "DescricaoServicoFederal": "Representação de qualquer natureza, inclusive comercial."
    },
    {
        "CodigoServicoMunicipal": "4612500",
        "DescricaoServicoMunicipal": "Representantes comerciais e agentes do comércio de combustíveis, miner",
        "CodigoServicoFederal": "10.09",
        "DescricaoServicoFederal": "Representação de qualquer natureza, inclusive comercial."
    },
    {
        "CodigoServicoMunicipal": "4613300",
        "DescricaoServicoMunicipal": "Representantes comerciais e agentes do comércio de madeira, material d",
        "CodigoServicoFederal": "10.09",
        "DescricaoServicoFederal": "Representação de qualquer natureza, inclusive comercial."
    },
    {
        "CodigoServicoMunicipal": "4614100",
        "DescricaoServicoMunicipal": "Representantes comerciais e agentes do comércio de máquinas, equipamen",
        "CodigoServicoFederal": "10.09",
        "DescricaoServicoFederal": "Representação de qualquer natureza, inclusive comercial."
    },
    {
        "CodigoServicoMunicipal": "4615000",
        "DescricaoServicoMunicipal": "Representantes comerciais e agentes do comércio de eletrodomésticos, m",
        "CodigoServicoFederal": "10.09",
        "DescricaoServicoFederal": "Representação de qualquer natureza, inclusive comercial."
    },
    {
        "CodigoServicoMunicipal": "4616800",
        "DescricaoServicoMunicipal": "Representantes comerciais e agentes do comércio de têxteis, vestuário,",
        "CodigoServicoFederal": "10.09",
        "DescricaoServicoFederal": "Representação de qualquer natureza, inclusive comercial."
    },
    {
        "CodigoServicoMunicipal": "4617600",
        "DescricaoServicoMunicipal": "Representantes comerciais e agentes do comércio de produtos alimentíci",
        "CodigoServicoFederal": "10.09",
        "DescricaoServicoFederal": "Representação de qualquer natureza, inclusive comercial."
    },
    {
        "CodigoServicoMunicipal": "4618401",
        "DescricaoServicoMunicipal": "Representantes comerciais e agentes do comércio de medicamentos, cosmé",
        "CodigoServicoFederal": "10.09",
        "DescricaoServicoFederal": "Representação de qualquer natureza, inclusive comercial."
    },
    {
        "CodigoServicoMunicipal": "4618402",
        "DescricaoServicoMunicipal": "Representantes comerciais e agentes do comércio de instrumentos e mate",
        "CodigoServicoFederal": "10.09",
        "DescricaoServicoFederal": "Representação de qualquer natureza, inclusive comercial."
    },
    {
        "CodigoServicoMunicipal": "4618403",
        "DescricaoServicoMunicipal": "Representantes comerciais e agentes do comércio de jornais, revistas e",
        "CodigoServicoFederal": "10.09",
        "DescricaoServicoFederal": "Representação de qualquer natureza, inclusive comercial."
    },
    {
        "CodigoServicoMunicipal": "4618499",
        "DescricaoServicoMunicipal": "Outros representantes comerciais e agentes do comércio especializado e",
        "CodigoServicoFederal": "10.09",
        "DescricaoServicoFederal": "Representação de qualquer natureza, inclusive comercial."
    },
    {
        "CodigoServicoMunicipal": "4619200",
        "DescricaoServicoMunicipal": "Representantes comerciais e agentes do comércio de mercadorias em gera",
        "CodigoServicoFederal": "10.09",
        "DescricaoServicoFederal": "Representação de qualquer natureza, inclusive comercial."
    },
    {
        "CodigoServicoMunicipal": "4751202",
        "DescricaoServicoMunicipal": "Recarga de cartuchos para equipamentos de informática",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "4771702",
        "DescricaoServicoMunicipal": "Comércio varejista de produtos farmacêuticos, com manipulação de fórmu",
        "CodigoServicoFederal": "04.07",
        "DescricaoServicoFederal": "Serviços farmacêuticos."
    },
    {
        "CodigoServicoMunicipal": "4771703",
        "DescricaoServicoMunicipal": "Comércio varejista de produtos farmacêuticos homeopáticos",
        "CodigoServicoFederal": "04.07",
        "DescricaoServicoFederal": "Serviços farmacêuticos."
    },
    {
        "CodigoServicoMunicipal": "4911600",
        "DescricaoServicoMunicipal": "Transporte ferroviário de carga",
        "CodigoServicoFederal": "03.04",
        "DescricaoServicoFederal": "Locação, sublocação, arrendamento, direito de passagem ou permissão de uso, compartilhado ou não, de ferrovia, rodovia, postes, cabos, dutos e condutos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "4912402",
        "DescricaoServicoMunicipal": "Transporte ferroviário de passageiros municipal e em região metropolit",
        "CodigoServicoFederal": "16.01",
        "DescricaoServicoFederal": "Serviços de transporte coletivo municipal rodoviário, metroviário, ferroviário e aquaviário de passageiros."
    },
    {
        "CodigoServicoMunicipal": "4912403",
        "DescricaoServicoMunicipal": "Transporte metroviário",
        "CodigoServicoFederal": "16.01",
        "DescricaoServicoFederal": "Serviços de transporte coletivo municipal rodoviário, metroviário, ferroviário e aquaviário de passageiros."
    },
    {
        "CodigoServicoMunicipal": "4921301",
        "DescricaoServicoMunicipal": "Transporte rodoviário coletivo de passageiros, com itinerário fixo, mu",
        "CodigoServicoFederal": "16.01",
        "DescricaoServicoFederal": "Serviços de transporte coletivo municipal rodoviário, metroviário, ferroviário e aquaviário de passageiros."
    },
    {
        "CodigoServicoMunicipal": "4921302",
        "DescricaoServicoMunicipal": "Transporte rodoviário coletivo de passageiros, com itinerário fixo, in",
        "CodigoServicoFederal": "16.01",
        "DescricaoServicoFederal": "Serviços de transporte coletivo municipal rodoviário, metroviário, ferroviário e aquaviário de passageiros."
    },
    {
        "CodigoServicoMunicipal": "4922102",
        "DescricaoServicoMunicipal": "Transporte rodoviário coletivo de passageiros, com itinerário fixo, in",
        "CodigoServicoFederal": "16.02",
        "DescricaoServicoFederal": "Outros serviços de transporte de natureza municipal."
    },
    {
        "CodigoServicoMunicipal": "4923001",
        "DescricaoServicoMunicipal": "Serviço de táxi",
        "CodigoServicoFederal": "16.01",
        "DescricaoServicoFederal": "Serviços de transporte coletivo municipal rodoviário, metroviário, ferroviário e aquaviário de passageiros."
    },
    {
        "CodigoServicoMunicipal": "4923002",
        "DescricaoServicoMunicipal": "Serviço de transporte de passageiros - locação de automóveis com motor",
        "CodigoServicoFederal": "16.01",
        "DescricaoServicoFederal": "Serviços de transporte coletivo municipal rodoviário, metroviário, ferroviário e aquaviário de passageiros."
    },
    {
        "CodigoServicoMunicipal": "4924800",
        "DescricaoServicoMunicipal": "Transporte escolar",
        "CodigoServicoFederal": "16.01",
        "DescricaoServicoFederal": "Serviços de transporte coletivo municipal rodoviário, metroviário, ferroviário e aquaviário de passageiros."
    },
    {
        "CodigoServicoMunicipal": "4929901",
        "DescricaoServicoMunicipal": "Transporte rodoviário coletivo de passageiros, sob regime de fretament",
        "CodigoServicoFederal": "16.01",
        "DescricaoServicoFederal": "Serviços de transporte coletivo municipal rodoviário, metroviário, ferroviário e aquaviário de passageiros."
    },
    {
        "CodigoServicoMunicipal": "4929903",
        "DescricaoServicoMunicipal": "Organização de excursões em veículos rodoviários próprios, municipal",
        "CodigoServicoFederal": "09.03",
        "DescricaoServicoFederal": "Guias de turismo."
    },
    {
        "CodigoServicoMunicipal": "4929904",
        "DescricaoServicoMunicipal": "Organização de excursões em veículos rodoviários próprios, intermunici",
        "CodigoServicoFederal": "09.03",
        "DescricaoServicoFederal": "Guias de turismo."
    },
    {
        "CodigoServicoMunicipal": "4929999",
        "DescricaoServicoMunicipal": "Outros transportes rodoviários de passageiros não especificados anteri",
        "CodigoServicoFederal": "16.02",
        "DescricaoServicoFederal": "Outros serviços de transporte de natureza municipal."
    },
    {
        "CodigoServicoMunicipal": "4930201",
        "DescricaoServicoMunicipal": "Transporte rodoviário de carga, exceto produtos perigosos e mudanças, ",
        "CodigoServicoFederal": "16.02",
        "DescricaoServicoFederal": "Outros serviços de transporte de natureza municipal."
    },
    {
        "CodigoServicoMunicipal": "4930203",
        "DescricaoServicoMunicipal": "Transporte rodoviário de produtos perigosos",
        "CodigoServicoFederal": "16.02",
        "DescricaoServicoFederal": "Outros serviços de transporte de natureza municipal."
    },
    {
        "CodigoServicoMunicipal": "4930204",
        "DescricaoServicoMunicipal": "Transporte rodoviário de mudanças",
        "CodigoServicoFederal": "16.02",
        "DescricaoServicoFederal": "Outros serviços de transporte de natureza municipal."
    },
    {
        "CodigoServicoMunicipal": "4940000",
        "DescricaoServicoMunicipal": "Transporte dutoviário",
        "CodigoServicoFederal": "16.02",
        "DescricaoServicoFederal": "Outros serviços de transporte de natureza municipal."
    },
    {
        "CodigoServicoMunicipal": "4950700",
        "DescricaoServicoMunicipal": "Trens turísticos, teleféricos e similares",
        "CodigoServicoFederal": "09.02",
        "DescricaoServicoFederal": "Agenciamento, organização, promoção, intermediação e execução de programas de turismo, passeios, viagens, excursões, hospedagens e congêneres."
    },
    {
        "CodigoServicoMunicipal": "4950700",
        "DescricaoServicoMunicipal": "Trens turísticos, teleféricos e similares",
        "CodigoServicoFederal": "16.01",
        "DescricaoServicoFederal": "Serviços de transporte coletivo municipal rodoviário, metroviário, ferroviário e aquaviário de passageiros."
    },
    {
        "CodigoServicoMunicipal": "5021101",
        "DescricaoServicoMunicipal": "Transporte por navegação interior de carga, municipal, exceto travessi",
        "CodigoServicoFederal": "16.02",
        "DescricaoServicoFederal": "Outros serviços de transporte de natureza municipal."
    },
    {
        "CodigoServicoMunicipal": "5022001",
        "DescricaoServicoMunicipal": "Transporte por navegação interior de passageiros em linhas regulares, ",
        "CodigoServicoFederal": "16.01",
        "DescricaoServicoFederal": "Serviços de transporte coletivo municipal rodoviário, metroviário, ferroviário e aquaviário de passageiros."
    },
    {
        "CodigoServicoMunicipal": "5030102",
        "DescricaoServicoMunicipal": "Navegação de apoio portuário",
        "CodigoServicoFederal": "20.01",
        "DescricaoServicoFederal": "Serviços portuários, ferroportuários, utilização de porto, movimentação de passageiros, reboque de embarcações, rebocador escoteiro, atracação, desatracação, serviços de praticagem, capatazia, armazenagem de qualquer natureza, serviços acessórios, movimentação de mercadorias, serviços de apoio marítimo, de movimentação ao largo, serviços de armadores, estiva, conferência, logística e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5091201",
        "DescricaoServicoMunicipal": "Transporte por navegação de travessia, municipal",
        "CodigoServicoFederal": "16.01",
        "DescricaoServicoFederal": "Serviços de transporte coletivo municipal rodoviário, metroviário, ferroviário e aquaviário de passageiros."
    },
    {
        "CodigoServicoMunicipal": "5091201",
        "DescricaoServicoMunicipal": "Transporte por navegação de travessia, municipal",
        "CodigoServicoFederal": "16.02",
        "DescricaoServicoFederal": "Outros serviços de transporte de natureza municipal."
    },
    {
        "CodigoServicoMunicipal": "5099801",
        "DescricaoServicoMunicipal": "Transporte aquaviário para passeios turísticos",
        "CodigoServicoFederal": "16.01",
        "DescricaoServicoFederal": "Serviços de transporte coletivo municipal rodoviário, metroviário, ferroviário e aquaviário de passageiros."
    },
    {
        "CodigoServicoMunicipal": "5112999",
        "DescricaoServicoMunicipal": "Outros serviços de transporte aéreo de passageiros não-regular",
        "CodigoServicoFederal": "16.01",
        "DescricaoServicoFederal": "Serviços de transporte coletivo municipal rodoviário, metroviário, ferroviário e aquaviário de passageiros."
    },
    {
        "CodigoServicoMunicipal": "5211701",
        "DescricaoServicoMunicipal": "Armazéns gerais - emissão de warrant",
        "CodigoServicoFederal": "11.04",
        "DescricaoServicoFederal": "Armazenamento, depósito, carga, descarga, arrumação e guarda de bens de qualquer espécie."
    },
    {
        "CodigoServicoMunicipal": "5211701",
        "DescricaoServicoMunicipal": "Armazéns gerais - emissão de warrant",
        "CodigoServicoFederal": "20.01",
        "DescricaoServicoFederal": "Serviços portuários, ferroportuários, utilização de porto, movimentação de passageiros, reboque de embarcações, rebocador escoteiro, atracação, desatracação, serviços de praticagem, capatazia, armazenagem de qualquer natureza, serviços acessórios, movimentação de mercadorias, serviços de apoio marítimo, de movimentação ao largo, serviços de armadores, estiva, conferência, logística e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5211702",
        "DescricaoServicoMunicipal": "Guarda-móveis",
        "CodigoServicoFederal": "11.04",
        "DescricaoServicoFederal": "Armazenamento, depósito, carga, descarga, arrumação e guarda de bens de qualquer espécie."
    },
    {
        "CodigoServicoMunicipal": "5211799",
        "DescricaoServicoMunicipal": "Depósitos de mercadorias para terceiros, exceto armazéns gerais e guar",
        "CodigoServicoFederal": "11.04",
        "DescricaoServicoFederal": "Armazenamento, depósito, carga, descarga, arrumação e guarda de bens de qualquer espécie."
    },
    {
        "CodigoServicoMunicipal": "5211799",
        "DescricaoServicoMunicipal": "Depósitos de mercadorias para terceiros, exceto armazéns gerais e guar",
        "CodigoServicoFederal": "20.01",
        "DescricaoServicoFederal": "Serviços portuários, ferroportuários, utilização de porto, movimentação de passageiros, reboque de embarcações, rebocador escoteiro, atracação, desatracação, serviços de praticagem, capatazia, armazenagem de qualquer natureza, serviços acessórios, movimentação de mercadorias, serviços de apoio marítimo, de movimentação ao largo, serviços de armadores, estiva, conferência, logística e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5212500",
        "DescricaoServicoMunicipal": "Carga e descarga",
        "CodigoServicoFederal": "11.04",
        "DescricaoServicoFederal": "Armazenamento, depósito, carga, descarga, arrumação e guarda de bens de qualquer espécie."
    },
    {
        "CodigoServicoMunicipal": "5212500",
        "DescricaoServicoMunicipal": "Carga e descarga",
        "CodigoServicoFederal": "20.01",
        "DescricaoServicoFederal": "Serviços portuários, ferroportuários, utilização de porto, movimentação de passageiros, reboque de embarcações, rebocador escoteiro, atracação, desatracação, serviços de praticagem, capatazia, armazenagem de qualquer natureza, serviços acessórios, movimentação de mercadorias, serviços de apoio marítimo, de movimentação ao largo, serviços de armadores, estiva, conferência, logística e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5221400",
        "DescricaoServicoMunicipal": "Concessionárias de rodovias, pontes, túneis e serviços relacionados",
        "CodigoServicoFederal": "03.04",
        "DescricaoServicoFederal": "Locação, sublocação, arrendamento, direito de passagem ou permissão de uso, compartilhado ou não, de ferrovia, rodovia, postes, cabos, dutos e condutos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "5221400",
        "DescricaoServicoMunicipal": "Concessionárias de rodovias, pontes, túneis e serviços relacionados",
        "CodigoServicoFederal": "22.01",
        "DescricaoServicoFederal": "Serviços de exploração de rodovia mediante cobrança de preço ou pedágio dos usuários, envolvendo execução de serviços de conservação, manutenção, melhoramentos para adequação de capacidade e segurança de trânsito, operação, monitoração, assistência aos usuários e outros serviços definidos em contratos, atos de concessão ou de permissão ou em normas oficiais."
    },
    {
        "CodigoServicoMunicipal": "5222200",
        "DescricaoServicoMunicipal": "Terminais rodoviários e ferroviários",
        "CodigoServicoFederal": "20.03",
        "DescricaoServicoFederal": " Serviços de terminais rodoviários, ferroviários, metroviários, movimentação de passageiros, mercadorias, inclusive suas operações, logística e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5223100",
        "DescricaoServicoMunicipal": "Estacionamento de veículos",
        "CodigoServicoFederal": "11.01",
        "DescricaoServicoFederal": "Guarda e estacionamento de veículos terrestres automotores, de aeronaves e de embarcações."
    },
    {
        "CodigoServicoMunicipal": "5229001",
        "DescricaoServicoMunicipal": "Serviços de apoio ao transporte por táxi, inclusive centrais de chamad",
        "CodigoServicoFederal": "10.02",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "5229001",
        "DescricaoServicoMunicipal": "Serviços de apoio ao transporte por táxi, inclusive centrais de chamad",
        "CodigoServicoFederal": "17.02",
        "DescricaoServicoFederal": "Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra-estrutura administrativa e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5229002",
        "DescricaoServicoMunicipal": "Serviços de reboque de veículos",
        "CodigoServicoFederal": "14.14",
        "DescricaoServicoFederal": "Guincho intramunicipal, guindaste e içamento."
    },
    {
        "CodigoServicoMunicipal": "5229099",
        "DescricaoServicoMunicipal": "Outras atividades auxiliares dos transportes terrestres não especifica",
        "CodigoServicoFederal": "11.03",
        "DescricaoServicoFederal": "Escolta, inclusive de veículos e cargas."
    },
    {
        "CodigoServicoMunicipal": "5231101",
        "DescricaoServicoMunicipal": "Administração da infra-estrutura portuária",
        "CodigoServicoFederal": "20.01",
        "DescricaoServicoFederal": "Serviços portuários, ferroportuários, utilização de porto, movimentação de passageiros, reboque de embarcações, rebocador escoteiro, atracação, desatracação, serviços de praticagem, capatazia, armazenagem de qualquer natureza, serviços acessórios, movimentação de mercadorias, serviços de apoio marítimo, de movimentação ao largo, serviços de armadores, estiva, conferência, logística e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5231102",
        "DescricaoServicoMunicipal": "Operações de terminais",
        "CodigoServicoFederal": "20.01",
        "DescricaoServicoFederal": "Serviços portuários, ferroportuários, utilização de porto, movimentação de passageiros, reboque de embarcações, rebocador escoteiro, atracação, desatracação, serviços de praticagem, capatazia, armazenagem de qualquer natureza, serviços acessórios, movimentação de mercadorias, serviços de apoio marítimo, de movimentação ao largo, serviços de armadores, estiva, conferência, logística e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5232000",
        "DescricaoServicoMunicipal": "Atividades de agenciamento marítimo",
        "CodigoServicoFederal": "10.06",
        "DescricaoServicoFederal": "Agenciamento marítimo."
    },
    {
        "CodigoServicoMunicipal": "5239700",
        "DescricaoServicoMunicipal": "Atividades auxiliares dos transportes aquaviários não especificadas an",
        "CodigoServicoFederal": "20.01",
        "DescricaoServicoFederal": "Serviços portuários, ferroportuários, utilização de porto, movimentação de passageiros, reboque de embarcações, rebocador escoteiro, atracação, desatracação, serviços de praticagem, capatazia, armazenagem de qualquer natureza, serviços acessórios, movimentação de mercadorias, serviços de apoio marítimo, de movimentação ao largo, serviços de armadores, estiva, conferência, logística e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5240199",
        "DescricaoServicoMunicipal": "Atividades auxiliares dos transportes aéreos, exceto operação dos aero",
        "CodigoServicoFederal": "20.02",
        "DescricaoServicoFederal": "Serviços aeroportuários, utilização de aeroporto, movimentação de passageiros, armazenagem de qualquer natureza, capatazia, movimentação de aeronaves, serviços de apoio aeroportuários, serviços acessórios, movimentação de mercadorias, logística e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5250801",
        "DescricaoServicoMunicipal": "Comissaria de despachos",
        "CodigoServicoFederal": "33.01",
        "DescricaoServicoFederal": "Serviços de desembaraço aduaneiro, comissários, despachantes e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5250802",
        "DescricaoServicoMunicipal": "Atividades de despachantes aduaneiros",
        "CodigoServicoFederal": "33.01",
        "DescricaoServicoFederal": "Serviços de desembaraço aduaneiro, comissários, despachantes e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5250803",
        "DescricaoServicoMunicipal": "Agenciamento de cargas, exceto para o transporte marítimo",
        "CodigoServicoFederal": "10.05",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de bens móveis ou imóveis, não abrangidos em outros itens ou subitens, inclusive aqueles realizados no âmbito de Bolsas de Mercadorias e Futuros, por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "5250803",
        "DescricaoServicoMunicipal": "Agenciamento de cargas, exceto para o transporte marítimo",
        "CodigoServicoFederal": "10.06",
        "DescricaoServicoFederal": "Agenciamento marítimo."
    },
    {
        "CodigoServicoMunicipal": "5250804",
        "DescricaoServicoMunicipal": "Organização logística do transporte de carga",
        "CodigoServicoFederal": "11.04",
        "DescricaoServicoFederal": "Armazenamento, depósito, carga, descarga, arrumação e guarda de bens de qualquer espécie."
    },
    {
        "CodigoServicoMunicipal": "5250805",
        "DescricaoServicoMunicipal": "Operador de transporte multimodal - OTM",
        "CodigoServicoFederal": "20.01",
        "DescricaoServicoFederal": "Serviços portuários, ferroportuários, utilização de porto, movimentação de passageiros, reboque de embarcações, rebocador escoteiro, atracação, desatracação, serviços de praticagem, capatazia, armazenagem de qualquer natureza, serviços acessórios, movimentação de mercadorias, serviços de apoio marítimo, de movimentação ao largo, serviços de armadores, estiva, conferência, logística e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5250805",
        "DescricaoServicoMunicipal": "Operador de transporte multimodal - OTM",
        "CodigoServicoFederal": "20.02",
        "DescricaoServicoFederal": "Serviços aeroportuários, utilização de aeroporto, movimentação de passageiros, armazenagem de qualquer natureza, capatazia, movimentação de aeronaves, serviços de apoio aeroportuários, serviços acessórios, movimentação de mercadorias, logística e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5250805",
        "DescricaoServicoMunicipal": "Operador de transporte multimodal - OTM",
        "CodigoServicoFederal": "20.03",
        "DescricaoServicoFederal": " Serviços de terminais rodoviários, ferroviários, metroviários, movimentação de passageiros, mercadorias, inclusive suas operações, logística e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5310501",
        "DescricaoServicoMunicipal": "Atividades do Correio Nacional",
        "CodigoServicoFederal": "26.01",
        "DescricaoServicoFederal": "Serviços de coleta, remessa ou entrega de correspondências, documentos, objetos, bens ou valores, inclusive pelos correios e suas agências franqueadas; courrier e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5310502",
        "DescricaoServicoMunicipal": "Atividades de franqueadas e permissionárias do Correio Nacional",
        "CodigoServicoFederal": "17.08",
        "DescricaoServicoFederal": "Franquia (franchising)."
    },
    {
        "CodigoServicoMunicipal": "5310502",
        "DescricaoServicoMunicipal": "Atividades de franqueadas e permissionárias do Correio Nacional",
        "CodigoServicoFederal": "26.01",
        "DescricaoServicoFederal": "Serviços de coleta, remessa ou entrega de correspondências, documentos, objetos, bens ou valores, inclusive pelos correios e suas agências franqueadas; courrier e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5320201",
        "DescricaoServicoMunicipal": "Serviços de malote não realizados pelo Correio Nacional",
        "CodigoServicoFederal": "26.01",
        "DescricaoServicoFederal": "Serviços de coleta, remessa ou entrega de correspondências, documentos, objetos, bens ou valores, inclusive pelos correios e suas agências franqueadas; courrier e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5320202",
        "DescricaoServicoMunicipal": "Serviços de entrega rápida",
        "CodigoServicoFederal": "26.01",
        "DescricaoServicoFederal": "Serviços de coleta, remessa ou entrega de correspondências, documentos, objetos, bens ou valores, inclusive pelos correios e suas agências franqueadas; courrier e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5510801",
        "DescricaoServicoMunicipal": "Hotéis",
        "CodigoServicoFederal": "09.01",
        "DescricaoServicoFederal": "Hospedagem de qualquer natureza em hotéis, apart-service condominiais, flat, apart-hotéis, hotéis residência, residence-service, suite service, hotelaria marítima, motéis, pensões e congêneres; ocupação por temporada com fornecimento de serviço (o valor da alimentação e gorjeta, quando incluído no preço da diária, fica sujeito ao Imposto Sobre Serviços)."
    },
    {
        "CodigoServicoMunicipal": "5510801",
        "DescricaoServicoMunicipal": "Hotéis",
        "CodigoServicoFederal": "09.02",
        "DescricaoServicoFederal": "Agenciamento, organização, promoção, intermediação e execução de programas de turismo, passeios, viagens, excursões, hospedagens e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5510801",
        "DescricaoServicoMunicipal": "Hotéis",
        "CodigoServicoFederal": "09.03",
        "DescricaoServicoFederal": "Guias de turismo."
    },
    {
        "CodigoServicoMunicipal": "5510802",
        "DescricaoServicoMunicipal": "Apart-hotéis",
        "CodigoServicoFederal": "09.01",
        "DescricaoServicoFederal": "Hospedagem de qualquer natureza em hotéis, apart-service condominiais, flat, apart-hotéis, hotéis residência, residence-service, suite service, hotelaria marítima, motéis, pensões e congêneres; ocupação por temporada com fornecimento de serviço (o valor da alimentação e gorjeta, quando incluído no preço da diária, fica sujeito ao Imposto Sobre Serviços)."
    },
    {
        "CodigoServicoMunicipal": "5510802",
        "DescricaoServicoMunicipal": "Apart-hotéis",
        "CodigoServicoFederal": "09.02",
        "DescricaoServicoFederal": "Agenciamento, organização, promoção, intermediação e execução de programas de turismo, passeios, viagens, excursões, hospedagens e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5510803",
        "DescricaoServicoMunicipal": "Motéis",
        "CodigoServicoFederal": "09.01",
        "DescricaoServicoFederal": "Hospedagem de qualquer natureza em hotéis, apart-service condominiais, flat, apart-hotéis, hotéis residência, residence-service, suite service, hotelaria marítima, motéis, pensões e congêneres; ocupação por temporada com fornecimento de serviço (o valor da alimentação e gorjeta, quando incluído no preço da diária, fica sujeito ao Imposto Sobre Serviços)."
    },
    {
        "CodigoServicoMunicipal": "5590601",
        "DescricaoServicoMunicipal": "Albergues, exceto assistenciais",
        "CodigoServicoFederal": "09.01",
        "DescricaoServicoFederal": "Hospedagem de qualquer natureza em hotéis, apart-service condominiais, flat, apart-hotéis, hotéis residência, residence-service, suite service, hotelaria marítima, motéis, pensões e congêneres; ocupação por temporada com fornecimento de serviço (o valor da alimentação e gorjeta, quando incluído no preço da diária, fica sujeito ao Imposto Sobre Serviços)."
    },
    {
        "CodigoServicoMunicipal": "5590602",
        "DescricaoServicoMunicipal": "Campings",
        "CodigoServicoFederal": "09.01",
        "DescricaoServicoFederal": "Hospedagem de qualquer natureza em hotéis, apart-service condominiais, flat, apart-hotéis, hotéis residência, residence-service, suite service, hotelaria marítima, motéis, pensões e congêneres; ocupação por temporada com fornecimento de serviço (o valor da alimentação e gorjeta, quando incluído no preço da diária, fica sujeito ao Imposto Sobre Serviços)."
    },
    {
        "CodigoServicoMunicipal": "5590603",
        "DescricaoServicoMunicipal": "Pensões",
        "CodigoServicoFederal": "09.01",
        "DescricaoServicoFederal": "Hospedagem de qualquer natureza em hotéis, apart-service condominiais, flat, apart-hotéis, hotéis residência, residence-service, suite service, hotelaria marítima, motéis, pensões e congêneres; ocupação por temporada com fornecimento de serviço (o valor da alimentação e gorjeta, quando incluído no preço da diária, fica sujeito ao Imposto Sobre Serviços)."
    },
    {
        "CodigoServicoMunicipal": "5590699",
        "DescricaoServicoMunicipal": "Outros alojamentos não especificados anteriormente",
        "CodigoServicoFederal": "09.01",
        "DescricaoServicoFederal": "Hospedagem de qualquer natureza em hotéis, apart-service condominiais, flat, apart-hotéis, hotéis residência, residence-service, suite service, hotelaria marítima, motéis, pensões e congêneres; ocupação por temporada com fornecimento de serviço (o valor da alimentação e gorjeta, quando incluído no preço da diária, fica sujeito ao Imposto Sobre Serviços)."
    },
    {
        "CodigoServicoMunicipal": "5590699",
        "DescricaoServicoMunicipal": "Outros alojamentos não especificados anteriormente",
        "CodigoServicoFederal": "09.02",
        "DescricaoServicoFederal": "Agenciamento, organização, promoção, intermediação e execução de programas de turismo, passeios, viagens, excursões, hospedagens e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5620102",
        "DescricaoServicoMunicipal": "Serviços de alimentação para eventos e recepções - bufê",
        "CodigoServicoFederal": "17.11",
        "DescricaoServicoFederal": "Organização de festas e recepções; bufê (exceto o fornecimento de alimentação e bebidas, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "5811500",
        "DescricaoServicoMunicipal": "Edição de livros",
        "CodigoServicoFederal": "17.02",
        "DescricaoServicoFederal": "Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra-estrutura administrativa e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5812300",
        "DescricaoServicoMunicipal": "Edição de jornais",
        "CodigoServicoFederal": "17.02",
        "DescricaoServicoFederal": "Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra-estrutura administrativa e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5813100",
        "DescricaoServicoMunicipal": "Edição de revistas",
        "CodigoServicoFederal": "17.02",
        "DescricaoServicoFederal": "Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra-estrutura administrativa e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5819100",
        "DescricaoServicoMunicipal": "Edição de cadastros, listas e outros produtos gráficos",
        "CodigoServicoFederal": "17.02",
        "DescricaoServicoFederal": "Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra-estrutura administrativa e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5821200",
        "DescricaoServicoMunicipal": "Edição integrada à impressão de livros",
        "CodigoServicoFederal": "17.02",
        "DescricaoServicoFederal": "Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra-estrutura administrativa e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5822100",
        "DescricaoServicoMunicipal": "Edição integrada à impressão de jornais",
        "CodigoServicoFederal": "17.02",
        "DescricaoServicoFederal": "Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra-estrutura administrativa e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5823900",
        "DescricaoServicoMunicipal": "Edição integrada à impressão de revistas",
        "CodigoServicoFederal": "17.02",
        "DescricaoServicoFederal": "Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra-estrutura administrativa e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5829800",
        "DescricaoServicoMunicipal": "Edição integrada à impressão de cadastros, listas e outros produtos gr",
        "CodigoServicoFederal": "17.02",
        "DescricaoServicoFederal": "Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra-estrutura administrativa e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5911102",
        "DescricaoServicoMunicipal": "Produção de filmes para publicidade",
        "CodigoServicoFederal": "17.06",
        "DescricaoServicoFederal": "Propaganda e publicidade, inclusive promoção de vendas, planejamento de campanhas ou sistemas de publicidade, elaboração de desenhos, textos e demais materiais publicitários."
    },
    {
        "CodigoServicoMunicipal": "5911199",
        "DescricaoServicoMunicipal": "Atividades de produção cinematográfica, de vídeos e de programas de te",
        "CodigoServicoFederal": "12.13",
        "DescricaoServicoFederal": "Produção, mediante ou sem encomenda prévia, de eventos, espetáculos, entrevistas, shows, ballet, danças, desfiles, bailes, teatros, óperas, concertos, recitais, festivais e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5911199",
        "DescricaoServicoMunicipal": "Atividades de produção cinematográfica, de vídeos e de programas de te",
        "CodigoServicoFederal": "13.03",
        "DescricaoServicoFederal": "Fotografia e cinematografia, inclusive revelação, ampliação, cópia, reprodução, trucagem e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5912001",
        "DescricaoServicoMunicipal": "Serviços de dublagem",
        "CodigoServicoFederal": "13.02",
        "DescricaoServicoFederal": "Fonografia ou gravação de sons, inclusive trucagem, dublagem, mixagem e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5912002",
        "DescricaoServicoMunicipal": "Serviços de mixagem sonora em produção audiovisual",
        "CodigoServicoFederal": "13.02",
        "DescricaoServicoFederal": "Fonografia ou gravação de sons, inclusive trucagem, dublagem, mixagem e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5912099",
        "DescricaoServicoMunicipal": "Atividades de pós-produção cinematográfica, de vídeos e de programas d",
        "CodigoServicoFederal": "13.03",
        "DescricaoServicoFederal": "Fotografia e cinematografia, inclusive revelação, ampliação, cópia, reprodução, trucagem e congêneres."
    },
    {
        "CodigoServicoMunicipal": "5914600",
        "DescricaoServicoMunicipal": "Atividades de exibição cinematográfica",
        "CodigoServicoFederal": "12.02",
        "DescricaoServicoFederal": "Exibições cinematográficas."
    },
    {
        "CodigoServicoMunicipal": "5914600",
        "DescricaoServicoMunicipal": "Atividades de exibição cinematográfica",
        "CodigoServicoFederal": "12.16",
        "DescricaoServicoFederal": "Exibição de filmes, entrevistas, musicais, espetáculos, shows, concertos, desfiles, óperas, competições esportivas, de destreza intelectual ou congêneres."
    },
    {
        "CodigoServicoMunicipal": "5920100",
        "DescricaoServicoMunicipal": "Atividades de gravação de som e de edição de música",
        "CodigoServicoFederal": "13.02",
        "DescricaoServicoFederal": "Fonografia ou gravação de sons, inclusive trucagem, dublagem, mixagem e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6021700",
        "DescricaoServicoMunicipal": "Atividades de televisão aberta",
        "CodigoServicoFederal": "12.13",
        "DescricaoServicoFederal": "Produção, mediante ou sem encomenda prévia, de eventos, espetáculos, entrevistas, shows, ballet, danças, desfiles, bailes, teatros, óperas, concertos, recitais, festivais e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6110801",
        "DescricaoServicoMunicipal": "Serviços de telefonia fixa comutada - STFC",
        "CodigoServicoFederal": "15.07",
        "DescricaoServicoFederal": "Acesso, movimentação, atendimento e consulta a contas em geral, por qualquer meio ou processo, inclusive por telefone, fac-símile, internet e telex, acesso a terminais de atendimento, inclusive vinte e quatro horas; acesso a outro banco e a rede compartilhada; fornecimento de saldo, extrato e demais informações relativas a contas em geral, por qualquer meio ou processo."
    },
    {
        "CodigoServicoMunicipal": "6110899",
        "DescricaoServicoMunicipal": "Serviços de telecomunicações por fio não especificados anteriormente",
        "CodigoServicoFederal": "09.01",
        "DescricaoServicoFederal": "Hospedagem de qualquer natureza em hotéis, apart-service condominiais, flat, apart-hotéis, hotéis residência, residence-service, suite service, hotelaria marítima, motéis, pensões e congêneres; ocupação por temporada com fornecimento de serviço (o valor da alimentação e gorjeta, quando incluído no preço da diária, fica sujeito ao Imposto Sobre Serviços)."
    },
    {
        "CodigoServicoMunicipal": "6141800",
        "DescricaoServicoMunicipal": "Instalação e assistência técnica em televisão por assinatura, inclusiv",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "6142600",
        "DescricaoServicoMunicipal": "Operadoras de televisão por assinatura por microondas",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "6143400",
        "DescricaoServicoMunicipal": "Operadoras de televisão por assinatura por satélite",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "6190601",
        "DescricaoServicoMunicipal": "Provedores de acesso às redes de comunicações",
        "CodigoServicoFederal": "01.03",
        "DescricaoServicoFederal": "Processamento, armazenamento ou hospedagem de dados, textos, imagens, vídeos, páginas eletrônicas, aplicativos e sistemas de informação, entre outros formatos, e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6190602",
        "DescricaoServicoMunicipal": "Provedores de voz sobre protocolo internet - VOIP",
        "CodigoServicoFederal": "01.03",
        "DescricaoServicoFederal": "Processamento, armazenamento ou hospedagem de dados, textos, imagens, vídeos, páginas eletrônicas, aplicativos e sistemas de informação, entre outros formatos, e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6190602",
        "DescricaoServicoMunicipal": "Provedores de voz sobre protocolo internet - VOIP",
        "CodigoServicoFederal": "10.09",
        "DescricaoServicoFederal": "Representação de qualquer natureza, inclusive comercial."
    },
    {
        "CodigoServicoMunicipal": "6190699",
        "DescricaoServicoMunicipal": "Serviço de conexão a redes de telecomunicações",
        "CodigoServicoFederal": "10.02",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "6190699",
        "DescricaoServicoMunicipal": "Serviço de conexão a redes de telecomunicações",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "6190699",
        "DescricaoServicoMunicipal": "Serviço de conexão a redes de telecomunicações",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "6201500",
        "DescricaoServicoMunicipal": "Desenvolvimento de programas de computador sob encomenda",
        "CodigoServicoFederal": "01.01",
        "DescricaoServicoFederal": "Análise e desenvolvimento de sistemas."
    },
    {
        "CodigoServicoMunicipal": "6201500",
        "DescricaoServicoMunicipal": "Desenvolvimento de programas de computador sob encomenda",
        "CodigoServicoFederal": "01.02",
        "DescricaoServicoFederal": "Programação."
    },
    {
        "CodigoServicoMunicipal": "6201500",
        "DescricaoServicoMunicipal": "Desenvolvimento de programas de computador sob encomenda",
        "CodigoServicoFederal": "01.04",
        "DescricaoServicoFederal": "Elaboração de programas de computadores, inclusive de jogos eletrônicos, independentemente da arquitetura construtiva da máquina em que o programa será executado, incluindo tablets, smartphones e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6201500",
        "DescricaoServicoMunicipal": "Desenvolvimento de programas de computador sob encomenda",
        "CodigoServicoFederal": "01.08",
        "DescricaoServicoFederal": "Planejamento, confecção, manutenção e atualização de páginas eletrônicas."
    },
    {
        "CodigoServicoMunicipal": "6202300",
        "DescricaoServicoMunicipal": "Desenvolvimento e licenciamento de programas de computador customizáve",
        "CodigoServicoFederal": "01.04",
        "DescricaoServicoFederal": "Elaboração de programas de computadores, inclusive de jogos eletrônicos, independentemente da arquitetura construtiva da máquina em que o programa será executado, incluindo tablets, smartphones e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6202300",
        "DescricaoServicoMunicipal": "Desenvolvimento e licenciamento de programas de computador customizáve",
        "CodigoServicoFederal": "01.05",
        "DescricaoServicoFederal": "Licenciamento ou cessão de direito de uso de programas de computação."
    },
    {
        "CodigoServicoMunicipal": "6203100",
        "DescricaoServicoMunicipal": "Desenvolvimento e licenciamento de programas de computador não-customi",
        "CodigoServicoFederal": "01.04",
        "DescricaoServicoFederal": "Elaboração de programas de computadores, inclusive de jogos eletrônicos, independentemente da arquitetura construtiva da máquina em que o programa será executado, incluindo tablets, smartphones e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6204000",
        "DescricaoServicoMunicipal": "Consultoria em tecnologia da informação",
        "CodigoServicoFederal": "01.06",
        "DescricaoServicoFederal": "Assessoria e consultoria em informática."
    },
    {
        "CodigoServicoMunicipal": "6209100",
        "DescricaoServicoMunicipal": "Suporte técnico, manutenção e outros serviços em tecnologia da informa",
        "CodigoServicoFederal": "01.07",
        "DescricaoServicoFederal": "Suporte técnico em informática, inclusive instalação, configuração e manutenção de programas de computação e bancos de dados."
    },
    {
        "CodigoServicoMunicipal": "6311900",
        "DescricaoServicoMunicipal": "Tratamento de dados, provedores de serviços de aplicação e serviços de",
        "CodigoServicoFederal": "01.03",
        "DescricaoServicoFederal": "Processamento, armazenamento ou hospedagem de dados, textos, imagens, vídeos, páginas eletrônicas, aplicativos e sistemas de informação, entre outros formatos, e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6319400",
        "DescricaoServicoMunicipal": "Portais, provedores de conteúdo e outros serviços de informação na int",
        "CodigoServicoFederal": "01.08",
        "DescricaoServicoFederal": "Planejamento, confecção, manutenção e atualização de páginas eletrônicas."
    },
    {
        "CodigoServicoMunicipal": "6391700",
        "DescricaoServicoMunicipal": "Agências de notícias",
        "CodigoServicoFederal": "10.07",
        "DescricaoServicoFederal": "Agenciamento de notícias."
    },
    {
        "CodigoServicoMunicipal": "6399200",
        "DescricaoServicoMunicipal": "Outras atividades de prestação de serviços de informação não especific",
        "CodigoServicoFederal": "10.01",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de câmbio, de seguros, de cartões de crédito, de planos de saúde e de planos de previdência privada."
    },
    {
        "CodigoServicoMunicipal": "6399200",
        "DescricaoServicoMunicipal": "Outras atividades de prestação de serviços de informação não especific",
        "CodigoServicoFederal": "17.01",
        "DescricaoServicoFederal": "Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista; análise, exame, pesquisa, coleta, compilação e fornecimento de dados e informações de qualquer natureza, inclusive cadastro e similares."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.02",
        "DescricaoServicoFederal": "Abertura de contas em geral, inclusive conta-corrente, conta de investimentos e aplicação e caderneta de poupança, no País e no exterior, bem como a manutenção das referidas contas ativas e inativas."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.03",
        "DescricaoServicoFederal": "Locação e manutenção de cofres particulares, de terminais eletrônicos, de terminais de atendimento e de bens e equipamentos em geral."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.04",
        "DescricaoServicoFederal": "Fornecimento ou emissão de atestados em geral, inclusive atestado de idoneidade, atestado de capacidade financeira e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.05",
        "DescricaoServicoFederal": "Cadastro, elaboração de ficha cadastral, renovação cadastral e congêneres, inclusão ou exclusão no Cadastro de Emitentes de Cheques sem Fundos – CCF ou em quaisquer outros bancos cadastrais."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.06",
        "DescricaoServicoFederal": "Emissão, reemissão e fornecimento de avisos, comprovantes e documentos em geral; abono de firmas; coleta e entrega de documentos, bens e valores; comunicação com outra agência ou com a administração central; licenciamento eletrônico de veículos; transferência de veículos; agenciamento fiduciário ou depositário; devolução de bens em custódia."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.07",
        "DescricaoServicoFederal": "Acesso, movimentação, atendimento e consulta a contas em geral, por qualquer meio ou processo, inclusive por telefone, fac-símile, internet e telex, acesso a terminais de atendimento, inclusive vinte e quatro horas; acesso a outro banco e a rede compartilhada; fornecimento de saldo, extrato e demais informações relativas a contas em geral, por qualquer meio ou processo."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.08",
        "DescricaoServicoFederal": "Emissão, reemissão, alteração, cessão, substituição, cancelamento e registro de contrato de crédito; estudo, análise e avaliação de operações de crédito; emissão, concessão, alteração ou contratação de aval, fiança, anuência e congêneres; serviços relativos a abertura de crédito, para quaisquer fins."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.09",
        "DescricaoServicoFederal": "Arrendamento mercantil (leasing) de quaisquer bens, inclusive cessão de direitos e obrigações, substituição de garantia, alteração, cancelamento e registro de contrato, e demais serviços relacionados ao arrendamento mercantil (leasing)."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.10",
        "DescricaoServicoFederal": "Serviços relacionados a cobranças, recebimentos ou pagamentos em geral, de títulos quaisquer, de contas ou carnês, de câmbio, de tributos e por conta de terceiros, inclusive os efetuados por meio eletrônico, automático ou por máquinas de atendimento; fornecimento de posição de cobrança, recebimento ou pagamento; emissão de carnês, fichas de compensação, impressos e documentos em geral."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.11",
        "DescricaoServicoFederal": "Devolução de títulos, protesto de títulos, sustação de protesto, manutenção de títulos, reapresentação de títulos, e demais serviços a eles relacionados."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.12",
        "DescricaoServicoFederal": "Custódia em geral, inclusive de títulos e valores mobiliários."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.13",
        "DescricaoServicoFederal": "Serviços relacionados a operações de câmbio em geral, edição, alteração, prorrogação, cancelamento e baixa de contrato de câmbio; emissão de registro de exportação ou de crédito; cobrança ou depósito no exterior; emissão, fornecimento e cancelamento de cheques de viagem; fornecimento, transferência, cancelamento e demais serviços relativos a carta de crédito de importação, exportação e garantias recebidas; envio e recebimento de mensagens em geral relacionadas a operações de câmbio."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.14",
        "DescricaoServicoFederal": "Fornecimento, emissão, reemissão, renovação e manutenção de cartão magnético, cartão de crédito, cartão de débito, cartão salário e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.15",
        "DescricaoServicoFederal": "Compensação de cheques e títulos quaisquer; serviços relacionados a depósito, inclusive depósito identificado, a saque de contas quaisquer, por qualquer meio ou processo, inclusive em terminais eletrônicos e de atendimento."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.16",
        "DescricaoServicoFederal": "Emissão, reemissão, liquidação, alteração, cancelamento e baixa de ordens de pagamento, ordens de crédito e similares, por qualquer meio ou processo; serviços relacionados à transferência de valores, dados, fundos, pagamentos e similares, inclusive entre contas em geral."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.17",
        "DescricaoServicoFederal": "Emissão, fornecimento, devolução, sustação, cancelamento e oposição de cheques quaisquer, avulso ou por talão."
    },
    {
        "CodigoServicoMunicipal": "6421200",
        "DescricaoServicoMunicipal": "Bancos comerciais",
        "CodigoServicoFederal": "15.18",
        "DescricaoServicoFederal": "Serviços relacionados a crédito imobiliário, avaliação e vistoria de imóvel ou obra, análise técnica e jurídica, emissão, reemissão, alteração, transferência e renegociação de contrato, emissão e reemissão do termo de quitação e demais serviços relacionados a crédito imobiliário."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.02",
        "DescricaoServicoFederal": "Abertura de contas em geral, inclusive conta-corrente, conta de investimentos e aplicação e caderneta de poupança, no País e no exterior, bem como a manutenção das referidas contas ativas e inativas."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.03",
        "DescricaoServicoFederal": "Locação e manutenção de cofres particulares, de terminais eletrônicos, de terminais de atendimento e de bens e equipamentos em geral."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.04",
        "DescricaoServicoFederal": "Fornecimento ou emissão de atestados em geral, inclusive atestado de idoneidade, atestado de capacidade financeira e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.05",
        "DescricaoServicoFederal": "Cadastro, elaboração de ficha cadastral, renovação cadastral e congêneres, inclusão ou exclusão no Cadastro de Emitentes de Cheques sem Fundos – CCF ou em quaisquer outros bancos cadastrais."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.06",
        "DescricaoServicoFederal": "Emissão, reemissão e fornecimento de avisos, comprovantes e documentos em geral; abono de firmas; coleta e entrega de documentos, bens e valores; comunicação com outra agência ou com a administração central; licenciamento eletrônico de veículos; transferência de veículos; agenciamento fiduciário ou depositário; devolução de bens em custódia."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.07",
        "DescricaoServicoFederal": "Acesso, movimentação, atendimento e consulta a contas em geral, por qualquer meio ou processo, inclusive por telefone, fac-símile, internet e telex, acesso a terminais de atendimento, inclusive vinte e quatro horas; acesso a outro banco e a rede compartilhada; fornecimento de saldo, extrato e demais informações relativas a contas em geral, por qualquer meio ou processo."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.08",
        "DescricaoServicoFederal": "Emissão, reemissão, alteração, cessão, substituição, cancelamento e registro de contrato de crédito; estudo, análise e avaliação de operações de crédito; emissão, concessão, alteração ou contratação de aval, fiança, anuência e congêneres; serviços relativos a abertura de crédito, para quaisquer fins."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.09",
        "DescricaoServicoFederal": "Arrendamento mercantil (leasing) de quaisquer bens, inclusive cessão de direitos e obrigações, substituição de garantia, alteração, cancelamento e registro de contrato, e demais serviços relacionados ao arrendamento mercantil (leasing)."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.10",
        "DescricaoServicoFederal": "Serviços relacionados a cobranças, recebimentos ou pagamentos em geral, de títulos quaisquer, de contas ou carnês, de câmbio, de tributos e por conta de terceiros, inclusive os efetuados por meio eletrônico, automático ou por máquinas de atendimento; fornecimento de posição de cobrança, recebimento ou pagamento; emissão de carnês, fichas de compensação, impressos e documentos em geral."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.11",
        "DescricaoServicoFederal": "Devolução de títulos, protesto de títulos, sustação de protesto, manutenção de títulos, reapresentação de títulos, e demais serviços a eles relacionados."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.12",
        "DescricaoServicoFederal": "Custódia em geral, inclusive de títulos e valores mobiliários."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.13",
        "DescricaoServicoFederal": "Serviços relacionados a operações de câmbio em geral, edição, alteração, prorrogação, cancelamento e baixa de contrato de câmbio; emissão de registro de exportação ou de crédito; cobrança ou depósito no exterior; emissão, fornecimento e cancelamento de cheques de viagem; fornecimento, transferência, cancelamento e demais serviços relativos a carta de crédito de importação, exportação e garantias recebidas; envio e recebimento de mensagens em geral relacionadas a operações de câmbio."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.14",
        "DescricaoServicoFederal": "Fornecimento, emissão, reemissão, renovação e manutenção de cartão magnético, cartão de crédito, cartão de débito, cartão salário e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.15",
        "DescricaoServicoFederal": "Compensação de cheques e títulos quaisquer; serviços relacionados a depósito, inclusive depósito identificado, a saque de contas quaisquer, por qualquer meio ou processo, inclusive em terminais eletrônicos e de atendimento."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.16",
        "DescricaoServicoFederal": "Emissão, reemissão, liquidação, alteração, cancelamento e baixa de ordens de pagamento, ordens de crédito e similares, por qualquer meio ou processo; serviços relacionados à transferência de valores, dados, fundos, pagamentos e similares, inclusive entre contas em geral."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.17",
        "DescricaoServicoFederal": "Emissão, fornecimento, devolução, sustação, cancelamento e oposição de cheques quaisquer, avulso ou por talão."
    },
    {
        "CodigoServicoMunicipal": "6422100",
        "DescricaoServicoMunicipal": "Bancos múltiplos, com carteira comercial",
        "CodigoServicoFederal": "15.18",
        "DescricaoServicoFederal": "Serviços relacionados a crédito imobiliário, avaliação e vistoria de imóvel ou obra, análise técnica e jurídica, emissão, reemissão, alteração, transferência e renegociação de contrato, emissão e reemissão do termo de quitação e demais serviços relacionados a crédito imobiliário."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.02",
        "DescricaoServicoFederal": "Abertura de contas em geral, inclusive conta-corrente, conta de investimentos e aplicação e caderneta de poupança, no País e no exterior, bem como a manutenção das referidas contas ativas e inativas."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.03",
        "DescricaoServicoFederal": "Locação e manutenção de cofres particulares, de terminais eletrônicos, de terminais de atendimento e de bens e equipamentos em geral."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.04",
        "DescricaoServicoFederal": "Fornecimento ou emissão de atestados em geral, inclusive atestado de idoneidade, atestado de capacidade financeira e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.05",
        "DescricaoServicoFederal": "Cadastro, elaboração de ficha cadastral, renovação cadastral e congêneres, inclusão ou exclusão no Cadastro de Emitentes de Cheques sem Fundos – CCF ou em quaisquer outros bancos cadastrais."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.06",
        "DescricaoServicoFederal": "Emissão, reemissão e fornecimento de avisos, comprovantes e documentos em geral; abono de firmas; coleta e entrega de documentos, bens e valores; comunicação com outra agência ou com a administração central; licenciamento eletrônico de veículos; transferência de veículos; agenciamento fiduciário ou depositário; devolução de bens em custódia."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.07",
        "DescricaoServicoFederal": "Acesso, movimentação, atendimento e consulta a contas em geral, por qualquer meio ou processo, inclusive por telefone, fac-símile, internet e telex, acesso a terminais de atendimento, inclusive vinte e quatro horas; acesso a outro banco e a rede compartilhada; fornecimento de saldo, extrato e demais informações relativas a contas em geral, por qualquer meio ou processo."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.08",
        "DescricaoServicoFederal": "Emissão, reemissão, alteração, cessão, substituição, cancelamento e registro de contrato de crédito; estudo, análise e avaliação de operações de crédito; emissão, concessão, alteração ou contratação de aval, fiança, anuência e congêneres; serviços relativos a abertura de crédito, para quaisquer fins."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.09",
        "DescricaoServicoFederal": "Arrendamento mercantil (leasing) de quaisquer bens, inclusive cessão de direitos e obrigações, substituição de garantia, alteração, cancelamento e registro de contrato, e demais serviços relacionados ao arrendamento mercantil (leasing)."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.10",
        "DescricaoServicoFederal": "Serviços relacionados a cobranças, recebimentos ou pagamentos em geral, de títulos quaisquer, de contas ou carnês, de câmbio, de tributos e por conta de terceiros, inclusive os efetuados por meio eletrônico, automático ou por máquinas de atendimento; fornecimento de posição de cobrança, recebimento ou pagamento; emissão de carnês, fichas de compensação, impressos e documentos em geral."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.11",
        "DescricaoServicoFederal": "Devolução de títulos, protesto de títulos, sustação de protesto, manutenção de títulos, reapresentação de títulos, e demais serviços a eles relacionados."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.12",
        "DescricaoServicoFederal": "Custódia em geral, inclusive de títulos e valores mobiliários."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.13",
        "DescricaoServicoFederal": "Serviços relacionados a operações de câmbio em geral, edição, alteração, prorrogação, cancelamento e baixa de contrato de câmbio; emissão de registro de exportação ou de crédito; cobrança ou depósito no exterior; emissão, fornecimento e cancelamento de cheques de viagem; fornecimento, transferência, cancelamento e demais serviços relativos a carta de crédito de importação, exportação e garantias recebidas; envio e recebimento de mensagens em geral relacionadas a operações de câmbio."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.14",
        "DescricaoServicoFederal": "Fornecimento, emissão, reemissão, renovação e manutenção de cartão magnético, cartão de crédito, cartão de débito, cartão salário e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.15",
        "DescricaoServicoFederal": "Compensação de cheques e títulos quaisquer; serviços relacionados a depósito, inclusive depósito identificado, a saque de contas quaisquer, por qualquer meio ou processo, inclusive em terminais eletrônicos e de atendimento."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.16",
        "DescricaoServicoFederal": "Emissão, reemissão, liquidação, alteração, cancelamento e baixa de ordens de pagamento, ordens de crédito e similares, por qualquer meio ou processo; serviços relacionados à transferência de valores, dados, fundos, pagamentos e similares, inclusive entre contas em geral."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.17",
        "DescricaoServicoFederal": "Emissão, fornecimento, devolução, sustação, cancelamento e oposição de cheques quaisquer, avulso ou por talão."
    },
    {
        "CodigoServicoMunicipal": "6423900",
        "DescricaoServicoMunicipal": "Caixas econômicas",
        "CodigoServicoFederal": "15.18",
        "DescricaoServicoFederal": "Serviços relacionados a crédito imobiliário, avaliação e vistoria de imóvel ou obra, análise técnica e jurídica, emissão, reemissão, alteração, transferência e renegociação de contrato, emissão e reemissão do termo de quitação e demais serviços relacionados a crédito imobiliário."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.02",
        "DescricaoServicoFederal": "Abertura de contas em geral, inclusive conta-corrente, conta de investimentos e aplicação e caderneta de poupança, no País e no exterior, bem como a manutenção das referidas contas ativas e inativas."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.03",
        "DescricaoServicoFederal": "Locação e manutenção de cofres particulares, de terminais eletrônicos, de terminais de atendimento e de bens e equipamentos em geral."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.04",
        "DescricaoServicoFederal": "Fornecimento ou emissão de atestados em geral, inclusive atestado de idoneidade, atestado de capacidade financeira e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.05",
        "DescricaoServicoFederal": "Cadastro, elaboração de ficha cadastral, renovação cadastral e congêneres, inclusão ou exclusão no Cadastro de Emitentes de Cheques sem Fundos – CCF ou em quaisquer outros bancos cadastrais."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.06",
        "DescricaoServicoFederal": "Emissão, reemissão e fornecimento de avisos, comprovantes e documentos em geral; abono de firmas; coleta e entrega de documentos, bens e valores; comunicação com outra agência ou com a administração central; licenciamento eletrônico de veículos; transferência de veículos; agenciamento fiduciário ou depositário; devolução de bens em custódia."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.07",
        "DescricaoServicoFederal": "Acesso, movimentação, atendimento e consulta a contas em geral, por qualquer meio ou processo, inclusive por telefone, fac-símile, internet e telex, acesso a terminais de atendimento, inclusive vinte e quatro horas; acesso a outro banco e a rede compartilhada; fornecimento de saldo, extrato e demais informações relativas a contas em geral, por qualquer meio ou processo."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.08",
        "DescricaoServicoFederal": "Emissão, reemissão, alteração, cessão, substituição, cancelamento e registro de contrato de crédito; estudo, análise e avaliação de operações de crédito; emissão, concessão, alteração ou contratação de aval, fiança, anuência e congêneres; serviços relativos a abertura de crédito, para quaisquer fins."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.09",
        "DescricaoServicoFederal": "Arrendamento mercantil (leasing) de quaisquer bens, inclusive cessão de direitos e obrigações, substituição de garantia, alteração, cancelamento e registro de contrato, e demais serviços relacionados ao arrendamento mercantil (leasing)."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.10",
        "DescricaoServicoFederal": "Serviços relacionados a cobranças, recebimentos ou pagamentos em geral, de títulos quaisquer, de contas ou carnês, de câmbio, de tributos e por conta de terceiros, inclusive os efetuados por meio eletrônico, automático ou por máquinas de atendimento; fornecimento de posição de cobrança, recebimento ou pagamento; emissão de carnês, fichas de compensação, impressos e documentos em geral."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.11",
        "DescricaoServicoFederal": "Devolução de títulos, protesto de títulos, sustação de protesto, manutenção de títulos, reapresentação de títulos, e demais serviços a eles relacionados."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.12",
        "DescricaoServicoFederal": "Custódia em geral, inclusive de títulos e valores mobiliários."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.13",
        "DescricaoServicoFederal": "Serviços relacionados a operações de câmbio em geral, edição, alteração, prorrogação, cancelamento e baixa de contrato de câmbio; emissão de registro de exportação ou de crédito; cobrança ou depósito no exterior; emissão, fornecimento e cancelamento de cheques de viagem; fornecimento, transferência, cancelamento e demais serviços relativos a carta de crédito de importação, exportação e garantias recebidas; envio e recebimento de mensagens em geral relacionadas a operações de câmbio."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.14",
        "DescricaoServicoFederal": "Fornecimento, emissão, reemissão, renovação e manutenção de cartão magnético, cartão de crédito, cartão de débito, cartão salário e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.15",
        "DescricaoServicoFederal": "Compensação de cheques e títulos quaisquer; serviços relacionados a depósito, inclusive depósito identificado, a saque de contas quaisquer, por qualquer meio ou processo, inclusive em terminais eletrônicos e de atendimento."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.16",
        "DescricaoServicoFederal": "Emissão, reemissão, liquidação, alteração, cancelamento e baixa de ordens de pagamento, ordens de crédito e similares, por qualquer meio ou processo; serviços relacionados à transferência de valores, dados, fundos, pagamentos e similares, inclusive entre contas em geral."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.17",
        "DescricaoServicoFederal": "Emissão, fornecimento, devolução, sustação, cancelamento e oposição de cheques quaisquer, avulso ou por talão."
    },
    {
        "CodigoServicoMunicipal": "6424701",
        "DescricaoServicoMunicipal": "Bancos cooperativos",
        "CodigoServicoFederal": "15.18",
        "DescricaoServicoFederal": "Serviços relacionados a crédito imobiliário, avaliação e vistoria de imóvel ou obra, análise técnica e jurídica, emissão, reemissão, alteração, transferência e renegociação de contrato, emissão e reemissão do termo de quitação e demais serviços relacionados a crédito imobiliário."
    },
    {
        "CodigoServicoMunicipal": "6424702",
        "DescricaoServicoMunicipal": "Cooperativas centrais de crédito",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.02",
        "DescricaoServicoFederal": "Abertura de contas em geral, inclusive conta-corrente, conta de investimentos e aplicação e caderneta de poupança, no País e no exterior, bem como a manutenção das referidas contas ativas e inativas."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.03",
        "DescricaoServicoFederal": "Locação e manutenção de cofres particulares, de terminais eletrônicos, de terminais de atendimento e de bens e equipamentos em geral."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.04",
        "DescricaoServicoFederal": "Fornecimento ou emissão de atestados em geral, inclusive atestado de idoneidade, atestado de capacidade financeira e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.05",
        "DescricaoServicoFederal": "Cadastro, elaboração de ficha cadastral, renovação cadastral e congêneres, inclusão ou exclusão no Cadastro de Emitentes de Cheques sem Fundos – CCF ou em quaisquer outros bancos cadastrais."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.06",
        "DescricaoServicoFederal": "Emissão, reemissão e fornecimento de avisos, comprovantes e documentos em geral; abono de firmas; coleta e entrega de documentos, bens e valores; comunicação com outra agência ou com a administração central; licenciamento eletrônico de veículos; transferência de veículos; agenciamento fiduciário ou depositário; devolução de bens em custódia."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.07",
        "DescricaoServicoFederal": "Acesso, movimentação, atendimento e consulta a contas em geral, por qualquer meio ou processo, inclusive por telefone, fac-símile, internet e telex, acesso a terminais de atendimento, inclusive vinte e quatro horas; acesso a outro banco e a rede compartilhada; fornecimento de saldo, extrato e demais informações relativas a contas em geral, por qualquer meio ou processo."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.08",
        "DescricaoServicoFederal": "Emissão, reemissão, alteração, cessão, substituição, cancelamento e registro de contrato de crédito; estudo, análise e avaliação de operações de crédito; emissão, concessão, alteração ou contratação de aval, fiança, anuência e congêneres; serviços relativos a abertura de crédito, para quaisquer fins."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.09",
        "DescricaoServicoFederal": "Arrendamento mercantil (leasing) de quaisquer bens, inclusive cessão de direitos e obrigações, substituição de garantia, alteração, cancelamento e registro de contrato, e demais serviços relacionados ao arrendamento mercantil (leasing)."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.10",
        "DescricaoServicoFederal": "Serviços relacionados a cobranças, recebimentos ou pagamentos em geral, de títulos quaisquer, de contas ou carnês, de câmbio, de tributos e por conta de terceiros, inclusive os efetuados por meio eletrônico, automático ou por máquinas de atendimento; fornecimento de posição de cobrança, recebimento ou pagamento; emissão de carnês, fichas de compensação, impressos e documentos em geral."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.11",
        "DescricaoServicoFederal": "Devolução de títulos, protesto de títulos, sustação de protesto, manutenção de títulos, reapresentação de títulos, e demais serviços a eles relacionados."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.12",
        "DescricaoServicoFederal": "Custódia em geral, inclusive de títulos e valores mobiliários."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.13",
        "DescricaoServicoFederal": "Serviços relacionados a operações de câmbio em geral, edição, alteração, prorrogação, cancelamento e baixa de contrato de câmbio; emissão de registro de exportação ou de crédito; cobrança ou depósito no exterior; emissão, fornecimento e cancelamento de cheques de viagem; fornecimento, transferência, cancelamento e demais serviços relativos a carta de crédito de importação, exportação e garantias recebidas; envio e recebimento de mensagens em geral relacionadas a operações de câmbio."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.14",
        "DescricaoServicoFederal": "Fornecimento, emissão, reemissão, renovação e manutenção de cartão magnético, cartão de crédito, cartão de débito, cartão salário e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.15",
        "DescricaoServicoFederal": "Compensação de cheques e títulos quaisquer; serviços relacionados a depósito, inclusive depósito identificado, a saque de contas quaisquer, por qualquer meio ou processo, inclusive em terminais eletrônicos e de atendimento."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.16",
        "DescricaoServicoFederal": "Emissão, reemissão, liquidação, alteração, cancelamento e baixa de ordens de pagamento, ordens de crédito e similares, por qualquer meio ou processo; serviços relacionados à transferência de valores, dados, fundos, pagamentos e similares, inclusive entre contas em geral."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.17",
        "DescricaoServicoFederal": "Emissão, fornecimento, devolução, sustação, cancelamento e oposição de cheques quaisquer, avulso ou por talão."
    },
    {
        "CodigoServicoMunicipal": "6424703",
        "DescricaoServicoMunicipal": "Cooperativas de crédito mútuo",
        "CodigoServicoFederal": "15.18",
        "DescricaoServicoFederal": "Serviços relacionados a crédito imobiliário, avaliação e vistoria de imóvel ou obra, análise técnica e jurídica, emissão, reemissão, alteração, transferência e renegociação de contrato, emissão e reemissão do termo de quitação e demais serviços relacionados a crédito imobiliário."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.02",
        "DescricaoServicoFederal": "Abertura de contas em geral, inclusive conta-corrente, conta de investimentos e aplicação e caderneta de poupança, no País e no exterior, bem como a manutenção das referidas contas ativas e inativas."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.03",
        "DescricaoServicoFederal": "Locação e manutenção de cofres particulares, de terminais eletrônicos, de terminais de atendimento e de bens e equipamentos em geral."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.04",
        "DescricaoServicoFederal": "Fornecimento ou emissão de atestados em geral, inclusive atestado de idoneidade, atestado de capacidade financeira e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.05",
        "DescricaoServicoFederal": "Cadastro, elaboração de ficha cadastral, renovação cadastral e congêneres, inclusão ou exclusão no Cadastro de Emitentes de Cheques sem Fundos – CCF ou em quaisquer outros bancos cadastrais."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.06",
        "DescricaoServicoFederal": "Emissão, reemissão e fornecimento de avisos, comprovantes e documentos em geral; abono de firmas; coleta e entrega de documentos, bens e valores; comunicação com outra agência ou com a administração central; licenciamento eletrônico de veículos; transferência de veículos; agenciamento fiduciário ou depositário; devolução de bens em custódia."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.07",
        "DescricaoServicoFederal": "Acesso, movimentação, atendimento e consulta a contas em geral, por qualquer meio ou processo, inclusive por telefone, fac-símile, internet e telex, acesso a terminais de atendimento, inclusive vinte e quatro horas; acesso a outro banco e a rede compartilhada; fornecimento de saldo, extrato e demais informações relativas a contas em geral, por qualquer meio ou processo."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.08",
        "DescricaoServicoFederal": "Emissão, reemissão, alteração, cessão, substituição, cancelamento e registro de contrato de crédito; estudo, análise e avaliação de operações de crédito; emissão, concessão, alteração ou contratação de aval, fiança, anuência e congêneres; serviços relativos a abertura de crédito, para quaisquer fins."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.09",
        "DescricaoServicoFederal": "Arrendamento mercantil (leasing) de quaisquer bens, inclusive cessão de direitos e obrigações, substituição de garantia, alteração, cancelamento e registro de contrato, e demais serviços relacionados ao arrendamento mercantil (leasing)."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.10",
        "DescricaoServicoFederal": "Serviços relacionados a cobranças, recebimentos ou pagamentos em geral, de títulos quaisquer, de contas ou carnês, de câmbio, de tributos e por conta de terceiros, inclusive os efetuados por meio eletrônico, automático ou por máquinas de atendimento; fornecimento de posição de cobrança, recebimento ou pagamento; emissão de carnês, fichas de compensação, impressos e documentos em geral."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.11",
        "DescricaoServicoFederal": "Devolução de títulos, protesto de títulos, sustação de protesto, manutenção de títulos, reapresentação de títulos, e demais serviços a eles relacionados."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.12",
        "DescricaoServicoFederal": "Custódia em geral, inclusive de títulos e valores mobiliários."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.13",
        "DescricaoServicoFederal": "Serviços relacionados a operações de câmbio em geral, edição, alteração, prorrogação, cancelamento e baixa de contrato de câmbio; emissão de registro de exportação ou de crédito; cobrança ou depósito no exterior; emissão, fornecimento e cancelamento de cheques de viagem; fornecimento, transferência, cancelamento e demais serviços relativos a carta de crédito de importação, exportação e garantias recebidas; envio e recebimento de mensagens em geral relacionadas a operações de câmbio."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.14",
        "DescricaoServicoFederal": "Fornecimento, emissão, reemissão, renovação e manutenção de cartão magnético, cartão de crédito, cartão de débito, cartão salário e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.15",
        "DescricaoServicoFederal": "Compensação de cheques e títulos quaisquer; serviços relacionados a depósito, inclusive depósito identificado, a saque de contas quaisquer, por qualquer meio ou processo, inclusive em terminais eletrônicos e de atendimento."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.16",
        "DescricaoServicoFederal": "Emissão, reemissão, liquidação, alteração, cancelamento e baixa de ordens de pagamento, ordens de crédito e similares, por qualquer meio ou processo; serviços relacionados à transferência de valores, dados, fundos, pagamentos e similares, inclusive entre contas em geral."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.17",
        "DescricaoServicoFederal": "Emissão, fornecimento, devolução, sustação, cancelamento e oposição de cheques quaisquer, avulso ou por talão."
    },
    {
        "CodigoServicoMunicipal": "6424704",
        "DescricaoServicoMunicipal": "Cooperativas de crédito rural",
        "CodigoServicoFederal": "15.18",
        "DescricaoServicoFederal": "Serviços relacionados a crédito imobiliário, avaliação e vistoria de imóvel ou obra, análise técnica e jurídica, emissão, reemissão, alteração, transferência e renegociação de contrato, emissão e reemissão do termo de quitação e demais serviços relacionados a crédito imobiliário."
    },
    {
        "CodigoServicoMunicipal": "6431000",
        "DescricaoServicoMunicipal": "Bancos múltiplos, sem carteira comercial",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6431000",
        "DescricaoServicoMunicipal": "Bancos múltiplos, sem carteira comercial",
        "CodigoServicoFederal": "15.06",
        "DescricaoServicoFederal": "Emissão, reemissão e fornecimento de avisos, comprovantes e documentos em geral; abono de firmas; coleta e entrega de documentos, bens e valores; comunicação com outra agência ou com a administração central; licenciamento eletrônico de veículos; transferência de veículos; agenciamento fiduciário ou depositário; devolução de bens em custódia."
    },
    {
        "CodigoServicoMunicipal": "6431000",
        "DescricaoServicoMunicipal": "Bancos múltiplos, sem carteira comercial",
        "CodigoServicoFederal": "15.08",
        "DescricaoServicoFederal": "Emissão, reemissão, alteração, cessão, substituição, cancelamento e registro de contrato de crédito; estudo, análise e avaliação de operações de crédito; emissão, concessão, alteração ou contratação de aval, fiança, anuência e congêneres; serviços relativos a abertura de crédito, para quaisquer fins."
    },
    {
        "CodigoServicoMunicipal": "6431000",
        "DescricaoServicoMunicipal": "Bancos múltiplos, sem carteira comercial",
        "CodigoServicoFederal": "15.09",
        "DescricaoServicoFederal": "Arrendamento mercantil (leasing) de quaisquer bens, inclusive cessão de direitos e obrigações, substituição de garantia, alteração, cancelamento e registro de contrato, e demais serviços relacionados ao arrendamento mercantil (leasing)."
    },
    {
        "CodigoServicoMunicipal": "6431000",
        "DescricaoServicoMunicipal": "Bancos múltiplos, sem carteira comercial",
        "CodigoServicoFederal": "15.12",
        "DescricaoServicoFederal": "Custódia em geral, inclusive de títulos e valores mobiliários."
    },
    {
        "CodigoServicoMunicipal": "6431000",
        "DescricaoServicoMunicipal": "Bancos múltiplos, sem carteira comercial",
        "CodigoServicoFederal": "15.18",
        "DescricaoServicoFederal": "Serviços relacionados a crédito imobiliário, avaliação e vistoria de imóvel ou obra, análise técnica e jurídica, emissão, reemissão, alteração, transferência e renegociação de contrato, emissão e reemissão do termo de quitação e demais serviços relacionados a crédito imobiliário."
    },
    {
        "CodigoServicoMunicipal": "6432800",
        "DescricaoServicoMunicipal": "Bancos de investimento",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6432800",
        "DescricaoServicoMunicipal": "Bancos de investimento",
        "CodigoServicoFederal": "15.07",
        "DescricaoServicoFederal": "Acesso, movimentação, atendimento e consulta a contas em geral, por qualquer meio ou processo, inclusive por telefone, fac-símile, internet e telex, acesso a terminais de atendimento, inclusive vinte e quatro horas; acesso a outro banco e a rede compartilhada; fornecimento de saldo, extrato e demais informações relativas a contas em geral, por qualquer meio ou processo."
    },
    {
        "CodigoServicoMunicipal": "6432800",
        "DescricaoServicoMunicipal": "Bancos de investimento",
        "CodigoServicoFederal": "15.08",
        "DescricaoServicoFederal": "Emissão, reemissão, alteração, cessão, substituição, cancelamento e registro de contrato de crédito; estudo, análise e avaliação de operações de crédito; emissão, concessão, alteração ou contratação de aval, fiança, anuência e congêneres; serviços relativos a abertura de crédito, para quaisquer fins."
    },
    {
        "CodigoServicoMunicipal": "6432800",
        "DescricaoServicoMunicipal": "Bancos de investimento",
        "CodigoServicoFederal": "15.16",
        "DescricaoServicoFederal": "Emissão, reemissão, liquidação, alteração, cancelamento e baixa de ordens de pagamento, ordens de crédito e similares, por qualquer meio ou processo; serviços relacionados à transferência de valores, dados, fundos, pagamentos e similares, inclusive entre contas em geral."
    },
    {
        "CodigoServicoMunicipal": "6433600",
        "DescricaoServicoMunicipal": "Bancos de desenvolvimento",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6433600",
        "DescricaoServicoMunicipal": "Bancos de desenvolvimento",
        "CodigoServicoFederal": "15.02",
        "DescricaoServicoFederal": "Abertura de contas em geral, inclusive conta-corrente, conta de investimentos e aplicação e caderneta de poupança, no País e no exterior, bem como a manutenção das referidas contas ativas e inativas."
    },
    {
        "CodigoServicoMunicipal": "6433600",
        "DescricaoServicoMunicipal": "Bancos de desenvolvimento",
        "CodigoServicoFederal": "15.07",
        "DescricaoServicoFederal": "Acesso, movimentação, atendimento e consulta a contas em geral, por qualquer meio ou processo, inclusive por telefone, fac-símile, internet e telex, acesso a terminais de atendimento, inclusive vinte e quatro horas; acesso a outro banco e a rede compartilhada; fornecimento de saldo, extrato e demais informações relativas a contas em geral, por qualquer meio ou processo."
    },
    {
        "CodigoServicoMunicipal": "6433600",
        "DescricaoServicoMunicipal": "Bancos de desenvolvimento",
        "CodigoServicoFederal": "15.08",
        "DescricaoServicoFederal": "Emissão, reemissão, alteração, cessão, substituição, cancelamento e registro de contrato de crédito; estudo, análise e avaliação de operações de crédito; emissão, concessão, alteração ou contratação de aval, fiança, anuência e congêneres; serviços relativos a abertura de crédito, para quaisquer fins."
    },
    {
        "CodigoServicoMunicipal": "6433600",
        "DescricaoServicoMunicipal": "Bancos de desenvolvimento",
        "CodigoServicoFederal": "15.16",
        "DescricaoServicoFederal": "Emissão, reemissão, liquidação, alteração, cancelamento e baixa de ordens de pagamento, ordens de crédito e similares, por qualquer meio ou processo; serviços relacionados à transferência de valores, dados, fundos, pagamentos e similares, inclusive entre contas em geral."
    },
    {
        "CodigoServicoMunicipal": "6434400",
        "DescricaoServicoMunicipal": "Agências de fomento",
        "CodigoServicoFederal": "10.04",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de contratos de arrendamento mercantil (leasing), de franquia (franchising) e de faturização (factoring)."
    },
    {
        "CodigoServicoMunicipal": "6434400",
        "DescricaoServicoMunicipal": "Agências de fomento",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6435201",
        "DescricaoServicoMunicipal": "Sociedades de crédito imobiliário",
        "CodigoServicoFederal": "15.18",
        "DescricaoServicoFederal": "Serviços relacionados a crédito imobiliário, avaliação e vistoria de imóvel ou obra, análise técnica e jurídica, emissão, reemissão, alteração, transferência e renegociação de contrato, emissão e reemissão do termo de quitação e demais serviços relacionados a crédito imobiliário."
    },
    {
        "CodigoServicoMunicipal": "6435202",
        "DescricaoServicoMunicipal": "Associações de poupança e empréstimo",
        "CodigoServicoFederal": "15.02",
        "DescricaoServicoFederal": "Abertura de contas em geral, inclusive conta-corrente, conta de investimentos e aplicação e caderneta de poupança, no País e no exterior, bem como a manutenção das referidas contas ativas e inativas."
    },
    {
        "CodigoServicoMunicipal": "6435202",
        "DescricaoServicoMunicipal": "Associações de poupança e empréstimo",
        "CodigoServicoFederal": "15.08",
        "DescricaoServicoFederal": "Emissão, reemissão, alteração, cessão, substituição, cancelamento e registro de contrato de crédito; estudo, análise e avaliação de operações de crédito; emissão, concessão, alteração ou contratação de aval, fiança, anuência e congêneres; serviços relativos a abertura de crédito, para quaisquer fins."
    },
    {
        "CodigoServicoMunicipal": "6435202",
        "DescricaoServicoMunicipal": "Associações de poupança e empréstimo",
        "CodigoServicoFederal": "15.18",
        "DescricaoServicoFederal": "Serviços relacionados a crédito imobiliário, avaliação e vistoria de imóvel ou obra, análise técnica e jurídica, emissão, reemissão, alteração, transferência e renegociação de contrato, emissão e reemissão do termo de quitação e demais serviços relacionados a crédito imobiliário."
    },
    {
        "CodigoServicoMunicipal": "6435203",
        "DescricaoServicoMunicipal": "Companhias hipotecárias",
        "CodigoServicoFederal": "10.05",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de bens móveis ou imóveis, não abrangidos em outros itens ou subitens, inclusive aqueles realizados no âmbito de Bolsas de Mercadorias e Futuros, por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "6435203",
        "DescricaoServicoMunicipal": "Companhias hipotecárias",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6435203",
        "DescricaoServicoMunicipal": "Companhias hipotecárias",
        "CodigoServicoFederal": "15.07",
        "DescricaoServicoFederal": "Acesso, movimentação, atendimento e consulta a contas em geral, por qualquer meio ou processo, inclusive por telefone, fac-símile, internet e telex, acesso a terminais de atendimento, inclusive vinte e quatro horas; acesso a outro banco e a rede compartilhada; fornecimento de saldo, extrato e demais informações relativas a contas em geral, por qualquer meio ou processo."
    },
    {
        "CodigoServicoMunicipal": "6435203",
        "DescricaoServicoMunicipal": "Companhias hipotecárias",
        "CodigoServicoFederal": "15.08",
        "DescricaoServicoFederal": "Emissão, reemissão, alteração, cessão, substituição, cancelamento e registro de contrato de crédito; estudo, análise e avaliação de operações de crédito; emissão, concessão, alteração ou contratação de aval, fiança, anuência e congêneres; serviços relativos a abertura de crédito, para quaisquer fins."
    },
    {
        "CodigoServicoMunicipal": "6435203",
        "DescricaoServicoMunicipal": "Companhias hipotecárias",
        "CodigoServicoFederal": "15.18",
        "DescricaoServicoFederal": "Serviços relacionados a crédito imobiliário, avaliação e vistoria de imóvel ou obra, análise técnica e jurídica, emissão, reemissão, alteração, transferência e renegociação de contrato, emissão e reemissão do termo de quitação e demais serviços relacionados a crédito imobiliário."
    },
    {
        "CodigoServicoMunicipal": "6436100",
        "DescricaoServicoMunicipal": "Sociedades de crédito, financiamento e investimento - financeiras",
        "CodigoServicoFederal": "15.08",
        "DescricaoServicoFederal": "Emissão, reemissão, alteração, cessão, substituição, cancelamento e registro de contrato de crédito; estudo, análise e avaliação de operações de crédito; emissão, concessão, alteração ou contratação de aval, fiança, anuência e congêneres; serviços relativos a abertura de crédito, para quaisquer fins."
    },
    {
        "CodigoServicoMunicipal": "6437900",
        "DescricaoServicoMunicipal": "Sociedades de crédito ao microempreendedor",
        "CodigoServicoFederal": "15.08",
        "DescricaoServicoFederal": "Emissão, reemissão, alteração, cessão, substituição, cancelamento e registro de contrato de crédito; estudo, análise e avaliação de operações de crédito; emissão, concessão, alteração ou contratação de aval, fiança, anuência e congêneres; serviços relativos a abertura de crédito, para quaisquer fins."
    },
    {
        "CodigoServicoMunicipal": "6438701",
        "DescricaoServicoMunicipal": "Bancos de câmbio",
        "CodigoServicoFederal": "15.13",
        "DescricaoServicoFederal": "Serviços relacionados a operações de câmbio em geral, edição, alteração, prorrogação, cancelamento e baixa de contrato de câmbio; emissão de registro de exportação ou de crédito; cobrança ou depósito no exterior; emissão, fornecimento e cancelamento de cheques de viagem; fornecimento, transferência, cancelamento e demais serviços relativos a carta de crédito de importação, exportação e garantias recebidas; envio e recebimento de mensagens em geral relacionadas a operações de câmbio."
    },
    {
        "CodigoServicoMunicipal": "6438799",
        "DescricaoServicoMunicipal": "Outras instituições de intermediação não-monetária não especificadas a",
        "CodigoServicoFederal": "15.13",
        "DescricaoServicoFederal": "Serviços relacionados a operações de câmbio em geral, edição, alteração, prorrogação, cancelamento e baixa de contrato de câmbio; emissão de registro de exportação ou de crédito; cobrança ou depósito no exterior; emissão, fornecimento e cancelamento de cheques de viagem; fornecimento, transferência, cancelamento e demais serviços relativos a carta de crédito de importação, exportação e garantias recebidas; envio e recebimento de mensagens em geral relacionadas a operações de câmbio."
    },
    {
        "CodigoServicoMunicipal": "6440900",
        "DescricaoServicoMunicipal": "Arrendamento mercantil",
        "CodigoServicoFederal": "15.09",
        "DescricaoServicoFederal": "Arrendamento mercantil (leasing) de quaisquer bens, inclusive cessão de direitos e obrigações, substituição de garantia, alteração, cancelamento e registro de contrato, e demais serviços relacionados ao arrendamento mercantil (leasing)."
    },
    {
        "CodigoServicoMunicipal": "6450600",
        "DescricaoServicoMunicipal": "Sociedades de capitalização",
        "CodigoServicoFederal": "15.02",
        "DescricaoServicoFederal": "Abertura de contas em geral, inclusive conta-corrente, conta de investimentos e aplicação e caderneta de poupança, no País e no exterior, bem como a manutenção das referidas contas ativas e inativas."
    },
    {
        "CodigoServicoMunicipal": "6450600",
        "DescricaoServicoMunicipal": "Sociedades de capitalização",
        "CodigoServicoFederal": "15.07",
        "DescricaoServicoFederal": "Acesso, movimentação, atendimento e consulta a contas em geral, por qualquer meio ou processo, inclusive por telefone, fac-símile, internet e telex, acesso a terminais de atendimento, inclusive vinte e quatro horas; acesso a outro banco e a rede compartilhada; fornecimento de saldo, extrato e demais informações relativas a contas em geral, por qualquer meio ou processo."
    },
    {
        "CodigoServicoMunicipal": "6470101",
        "DescricaoServicoMunicipal": "Fundos de investimento, exceto previdenciários e imobiliários",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6470102",
        "DescricaoServicoMunicipal": "Fundos de investimento previdenciários",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6470103",
        "DescricaoServicoMunicipal": "Fundos de investimento imobiliários",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6491300",
        "DescricaoServicoMunicipal": "Sociedades de fomento mercantil - factoring",
        "CodigoServicoFederal": "10.04",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de contratos de arrendamento mercantil (leasing), de franquia (franchising) e de faturização (factoring)."
    },
    {
        "CodigoServicoMunicipal": "6491300",
        "DescricaoServicoMunicipal": "Sociedades de fomento mercantil - factoring",
        "CodigoServicoFederal": "17.23",
        "DescricaoServicoFederal": "Assessoria, análise, avaliação, atendimento, consulta, cadastro, seleção, gerenciamento de informações, administração de contas a receber ou a pagar e em geral, relacionados a operações de faturização (factoring)."
    },
    {
        "CodigoServicoMunicipal": "6493000",
        "DescricaoServicoMunicipal": "Administração de consórcios para aquisição de bens e direitos",
        "CodigoServicoFederal": "17.12",
        "DescricaoServicoFederal": "Administração em geral, inclusive de bens e negócios de terceiros."
    },
    {
        "CodigoServicoMunicipal": "6499901",
        "DescricaoServicoMunicipal": "Clubes de investimento",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6499902",
        "DescricaoServicoMunicipal": "Sociedades de investimento",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6499904",
        "DescricaoServicoMunicipal": "Caixas de financiamento de corporações",
        "CodigoServicoFederal": "15.18",
        "DescricaoServicoFederal": "Serviços relacionados a crédito imobiliário, avaliação e vistoria de imóvel ou obra, análise técnica e jurídica, emissão, reemissão, alteração, transferência e renegociação de contrato, emissão e reemissão do termo de quitação e demais serviços relacionados a crédito imobiliário."
    },
    {
        "CodigoServicoMunicipal": "6499999",
        "DescricaoServicoMunicipal": "Outras atividades de serviços financeiros não especificadas anteriorme",
        "CodigoServicoFederal": "10.01",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de câmbio, de seguros, de cartões de crédito, de planos de saúde e de planos de previdência privada."
    },
    {
        "CodigoServicoMunicipal": "6499999",
        "DescricaoServicoMunicipal": "Outras atividades de serviços financeiros não especificadas anteriorme",
        "CodigoServicoFederal": "10.02",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "6499999",
        "DescricaoServicoMunicipal": "Outras atividades de serviços financeiros não especificadas anteriorme",
        "CodigoServicoFederal": "10.03",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de direitos de propriedade industrial, artística ou literária."
    },
    {
        "CodigoServicoMunicipal": "6499999",
        "DescricaoServicoMunicipal": "Outras atividades de serviços financeiros não especificadas anteriorme",
        "CodigoServicoFederal": "10.04",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de contratos de arrendamento mercantil (leasing), de franquia (franchising) e de faturização (factoring)."
    },
    {
        "CodigoServicoMunicipal": "6499999",
        "DescricaoServicoMunicipal": "Outras atividades de serviços financeiros não especificadas anteriorme",
        "CodigoServicoFederal": "10.05",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de bens móveis ou imóveis, não abrangidos em outros itens ou subitens, inclusive aqueles realizados no âmbito de Bolsas de Mercadorias e Futuros, por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "6499999",
        "DescricaoServicoMunicipal": "Outras atividades de serviços financeiros não especificadas anteriorme",
        "CodigoServicoFederal": "15.12",
        "DescricaoServicoFederal": "Custódia em geral, inclusive de títulos e valores mobiliários."
    },
    {
        "CodigoServicoMunicipal": "6511101",
        "DescricaoServicoMunicipal": "Seguros de vida",
        "CodigoServicoFederal": "10.01",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de câmbio, de seguros, de cartões de crédito, de planos de saúde e de planos de previdência privada."
    },
    {
        "CodigoServicoMunicipal": "6511102",
        "DescricaoServicoMunicipal": "Planos de auxílio-funeral",
        "CodigoServicoFederal": "25.03",
        "DescricaoServicoFederal": "Planos ou convênio funerários."
    },
    {
        "CodigoServicoMunicipal": "6550200",
        "DescricaoServicoMunicipal": "Planos de saúde",
        "CodigoServicoFederal": "04.22",
        "DescricaoServicoFederal": "Planos de medicina de grupo ou individual e convênios para prestação de assistência médica, hospitalar, odontológica e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6550200",
        "DescricaoServicoMunicipal": "Planos de saúde",
        "CodigoServicoFederal": "04.23",
        "DescricaoServicoFederal": "Outros planos de saúde que se cumpram através de serviços de terceiros contratados, credenciados, cooperados ou apenas pagos pelo operador do plano mediante indicação do beneficiário."
    },
    {
        "CodigoServicoMunicipal": "6550200",
        "DescricaoServicoMunicipal": "Planos de saúde",
        "CodigoServicoFederal": "05.09",
        "DescricaoServicoFederal": "Planos de atendimento e assistência médico-veterinária."
    },
    {
        "CodigoServicoMunicipal": "6611801",
        "DescricaoServicoMunicipal": "Bolsa de valores",
        "CodigoServicoFederal": "10.02",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "6611801",
        "DescricaoServicoMunicipal": "Bolsa de valores",
        "CodigoServicoFederal": "10.04",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de contratos de arrendamento mercantil (leasing), de franquia (franchising) e de faturização (factoring)."
    },
    {
        "CodigoServicoMunicipal": "6611801",
        "DescricaoServicoMunicipal": "Bolsa de valores",
        "CodigoServicoFederal": "17.12",
        "DescricaoServicoFederal": "Administração em geral, inclusive de bens e negócios de terceiros."
    },
    {
        "CodigoServicoMunicipal": "6611802",
        "DescricaoServicoMunicipal": "Bolsa de mercadorias",
        "CodigoServicoFederal": "17.12",
        "DescricaoServicoFederal": "Administração em geral, inclusive de bens e negócios de terceiros."
    },
    {
        "CodigoServicoMunicipal": "6611803",
        "DescricaoServicoMunicipal": "Bolsa de mercadorias e futuros",
        "CodigoServicoFederal": "17.12",
        "DescricaoServicoFederal": "Administração em geral, inclusive de bens e negócios de terceiros."
    },
    {
        "CodigoServicoMunicipal": "6611804",
        "DescricaoServicoMunicipal": "Administração de mercados de balcão organizados",
        "CodigoServicoFederal": "17.12",
        "DescricaoServicoFederal": "Administração em geral, inclusive de bens e negócios de terceiros."
    },
    {
        "CodigoServicoMunicipal": "6612601",
        "DescricaoServicoMunicipal": "Corretoras de títulos e valores mobiliários",
        "CodigoServicoFederal": "10.02",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "6612601",
        "DescricaoServicoMunicipal": "Corretoras de títulos e valores mobiliários",
        "CodigoServicoFederal": "10.03",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de direitos de propriedade industrial, artística ou literária."
    },
    {
        "CodigoServicoMunicipal": "6612602",
        "DescricaoServicoMunicipal": "Distribuidoras de títulos e valores mobiliários",
        "CodigoServicoFederal": "10.02",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "6612602",
        "DescricaoServicoMunicipal": "Distribuidoras de títulos e valores mobiliários",
        "CodigoServicoFederal": "10.10",
        "DescricaoServicoFederal": "Distribuição de bens de terceiros."
    },
    {
        "CodigoServicoMunicipal": "6612603",
        "DescricaoServicoMunicipal": "Corretoras de câmbio",
        "CodigoServicoFederal": "10.01",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de câmbio, de seguros, de cartões de crédito, de planos de saúde e de planos de previdência privada."
    },
    {
        "CodigoServicoMunicipal": "6612603",
        "DescricaoServicoMunicipal": "Corretoras de câmbio",
        "CodigoServicoFederal": "15.13",
        "DescricaoServicoFederal": "Serviços relacionados a operações de câmbio em geral, edição, alteração, prorrogação, cancelamento e baixa de contrato de câmbio; emissão de registro de exportação ou de crédito; cobrança ou depósito no exterior; emissão, fornecimento e cancelamento de cheques de viagem; fornecimento, transferência, cancelamento e demais serviços relativos a carta de crédito de importação, exportação e garantias recebidas; envio e recebimento de mensagens em geral relacionadas a operações de câmbio."
    },
    {
        "CodigoServicoMunicipal": "6612604",
        "DescricaoServicoMunicipal": "Corretoras de contratos de mercadorias",
        "CodigoServicoFederal": "10.02",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "6612604",
        "DescricaoServicoMunicipal": "Corretoras de contratos de mercadorias",
        "CodigoServicoFederal": "10.04",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de contratos de arrendamento mercantil (leasing), de franquia (franchising) e de faturização (factoring)."
    },
    {
        "CodigoServicoMunicipal": "6612605",
        "DescricaoServicoMunicipal": "Agentes de investimentos em aplicações financeiras",
        "CodigoServicoFederal": "10.05",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de bens móveis ou imóveis, não abrangidos em outros itens ou subitens, inclusive aqueles realizados no âmbito de Bolsas de Mercadorias e Futuros, por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "6612605",
        "DescricaoServicoMunicipal": "Agentes de investimentos em aplicações financeiras",
        "CodigoServicoFederal": "17.20",
        "DescricaoServicoFederal": "Consultoria e assessoria econômica ou financeira."
    },
    {
        "CodigoServicoMunicipal": "6613400",
        "DescricaoServicoMunicipal": "Administração de cartões de crédito",
        "CodigoServicoFederal": "10.03",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de direitos de propriedade industrial, artística ou literária."
    },
    {
        "CodigoServicoMunicipal": "6613400",
        "DescricaoServicoMunicipal": "Administração de cartões de crédito",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6619301",
        "DescricaoServicoMunicipal": "Serviços de liquidação e custódia",
        "CodigoServicoFederal": "15.10",
        "DescricaoServicoFederal": "Serviços relacionados a cobranças, recebimentos ou pagamentos em geral, de títulos quaisquer, de contas ou carnês, de câmbio, de tributos e por conta de terceiros, inclusive os efetuados por meio eletrônico, automático ou por máquinas de atendimento; fornecimento de posição de cobrança, recebimento ou pagamento; emissão de carnês, fichas de compensação, impressos e documentos em geral."
    },
    {
        "CodigoServicoMunicipal": "6619301",
        "DescricaoServicoMunicipal": "Serviços de liquidação e custódia",
        "CodigoServicoFederal": "15.12",
        "DescricaoServicoFederal": "Custódia em geral, inclusive de títulos e valores mobiliários."
    },
    {
        "CodigoServicoMunicipal": "6619302",
        "DescricaoServicoMunicipal": "Correspondentes de instituições financeiras",
        "CodigoServicoFederal": "10.04",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de contratos de arrendamento mercantil (leasing), de franquia (franchising) e de faturização (factoring)."
    },
    {
        "CodigoServicoMunicipal": "6619302",
        "DescricaoServicoMunicipal": "Correspondentes de instituições financeiras",
        "CodigoServicoFederal": "15.10",
        "DescricaoServicoFederal": "Serviços relacionados a cobranças, recebimentos ou pagamentos em geral, de títulos quaisquer, de contas ou carnês, de câmbio, de tributos e por conta de terceiros, inclusive os efetuados por meio eletrônico, automático ou por máquinas de atendimento; fornecimento de posição de cobrança, recebimento ou pagamento; emissão de carnês, fichas de compensação, impressos e documentos em geral."
    },
    {
        "CodigoServicoMunicipal": "6619304",
        "DescricaoServicoMunicipal": "Caixas eletrônicos",
        "CodigoServicoFederal": "15.07",
        "DescricaoServicoFederal": "Acesso, movimentação, atendimento e consulta a contas em geral, por qualquer meio ou processo, inclusive por telefone, fac-símile, internet e telex, acesso a terminais de atendimento, inclusive vinte e quatro horas; acesso a outro banco e a rede compartilhada; fornecimento de saldo, extrato e demais informações relativas a contas em geral, por qualquer meio ou processo."
    },
    {
        "CodigoServicoMunicipal": "6619305",
        "DescricaoServicoMunicipal": "Operadoras de cartões de débito",
        "CodigoServicoFederal": "15.01",
        "DescricaoServicoFederal": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6619399",
        "DescricaoServicoMunicipal": "Outras atividades auxiliares dos serviços financeiros não especificada",
        "CodigoServicoFederal": "10.01",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de câmbio, de seguros, de cartões de crédito, de planos de saúde e de planos de previdência privada."
    },
    {
        "CodigoServicoMunicipal": "6619399",
        "DescricaoServicoMunicipal": "Outras atividades auxiliares dos serviços financeiros não especificada",
        "CodigoServicoFederal": "10.02",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "6619399",
        "DescricaoServicoMunicipal": "Outras atividades auxiliares dos serviços financeiros não especificada",
        "CodigoServicoFederal": "10.05",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de bens móveis ou imóveis, não abrangidos em outros itens ou subitens, inclusive aqueles realizados no âmbito de Bolsas de Mercadorias e Futuros, por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "6621501",
        "DescricaoServicoMunicipal": "Peritos e avaliadores de seguros",
        "CodigoServicoFederal": "17.09",
        "DescricaoServicoFederal": "Perícias, laudos, exames técnicos e análises técnicas."
    },
    {
        "CodigoServicoMunicipal": "6621501",
        "DescricaoServicoMunicipal": "Peritos e avaliadores de seguros",
        "CodigoServicoFederal": "17.16",
        "DescricaoServicoFederal": "Auditoria"
    },
    {
        "CodigoServicoMunicipal": "6621501",
        "DescricaoServicoMunicipal": "Peritos e avaliadores de seguros",
        "CodigoServicoFederal": "18.01",
        "DescricaoServicoFederal": "Serviços de regulação de sinistros vinculados a contratos de seguros; inspeção e avaliação de riscos para cobertura de contratos de seguros; prevenção e gerência de riscos seguráveis e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6621501",
        "DescricaoServicoMunicipal": "Peritos e avaliadores de seguros",
        "CodigoServicoFederal": "28.01",
        "DescricaoServicoFederal": "Serviços de avaliação de bens e serviços de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "6621502",
        "DescricaoServicoMunicipal": "Auditoria e consultoria atuarial",
        "CodigoServicoFederal": "17.16",
        "DescricaoServicoFederal": "Auditoria"
    },
    {
        "CodigoServicoMunicipal": "6621502",
        "DescricaoServicoMunicipal": "Auditoria e consultoria atuarial",
        "CodigoServicoFederal": "17.18",
        "DescricaoServicoFederal": "Atuária e cálculos técnicos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "6621502",
        "DescricaoServicoMunicipal": "Auditoria e consultoria atuarial",
        "CodigoServicoFederal": "17.20",
        "DescricaoServicoFederal": "Consultoria e assessoria econômica ou financeira."
    },
    {
        "CodigoServicoMunicipal": "6622300",
        "DescricaoServicoMunicipal": "Corretores e agentes de seguros, de planos de previdência complementar",
        "CodigoServicoFederal": "10.01",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de câmbio, de seguros, de cartões de crédito, de planos de saúde e de planos de previdência privada."
    },
    {
        "CodigoServicoMunicipal": "6622300",
        "DescricaoServicoMunicipal": "Corretores e agentes de seguros, de planos de previdência complementar",
        "CodigoServicoFederal": "10.02",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "6629100",
        "DescricaoServicoMunicipal": "Atividades auxiliares dos seguros, da previdência complementar e dos p",
        "CodigoServicoFederal": "18.01",
        "DescricaoServicoFederal": "Serviços de regulação de sinistros vinculados a contratos de seguros; inspeção e avaliação de riscos para cobertura de contratos de seguros; prevenção e gerência de riscos seguráveis e congêneres."
    },
    {
        "CodigoServicoMunicipal": "6630400",
        "DescricaoServicoMunicipal": "Atividades de administração de fundos por contrato ou comissão",
        "CodigoServicoFederal": "17.12",
        "DescricaoServicoFederal": "Administração em geral, inclusive de bens e negócios de terceiros."
    },
    {
        "CodigoServicoMunicipal": "6821801",
        "DescricaoServicoMunicipal": "Corretagem na compra e venda e avaliação de imóveis",
        "CodigoServicoFederal": "10.02",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "6821801",
        "DescricaoServicoMunicipal": "Corretagem na compra e venda e avaliação de imóveis",
        "CodigoServicoFederal": "10.05",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de bens móveis ou imóveis, não abrangidos em outros itens ou subitens, inclusive aqueles realizados no âmbito de Bolsas de Mercadorias e Futuros, por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "6821801",
        "DescricaoServicoMunicipal": "Corretagem na compra e venda e avaliação de imóveis",
        "CodigoServicoFederal": "28.01",
        "DescricaoServicoFederal": "Serviços de avaliação de bens e serviços de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "6821802",
        "DescricaoServicoMunicipal": "Corretagem no aluguel de imóveis",
        "CodigoServicoFederal": "10.02",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "6821802",
        "DescricaoServicoMunicipal": "Corretagem no aluguel de imóveis",
        "CodigoServicoFederal": "10.05",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de bens móveis ou imóveis, não abrangidos em outros itens ou subitens, inclusive aqueles realizados no âmbito de Bolsas de Mercadorias e Futuros, por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "6822600",
        "DescricaoServicoMunicipal": "Gestão e administração da propriedade imobiliária",
        "CodigoServicoFederal": "10.02",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "6822600",
        "DescricaoServicoMunicipal": "Gestão e administração da propriedade imobiliária",
        "CodigoServicoFederal": "10.05",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de bens móveis ou imóveis, não abrangidos em outros itens ou subitens, inclusive aqueles realizados no âmbito de Bolsas de Mercadorias e Futuros, por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "6822600",
        "DescricaoServicoMunicipal": "Gestão e administração da propriedade imobiliária",
        "CodigoServicoFederal": "17.12",
        "DescricaoServicoFederal": "Administração em geral, inclusive de bens e negócios de terceiros."
    },
    {
        "CodigoServicoMunicipal": "6911701",
        "DescricaoServicoMunicipal": "Serviços advocatícios",
        "CodigoServicoFederal": "17.14",
        "DescricaoServicoFederal": "Advocacia."
    },
    {
        "CodigoServicoMunicipal": "6911702",
        "DescricaoServicoMunicipal": "Atividades auxiliares da justiça",
        "CodigoServicoFederal": "17.09",
        "DescricaoServicoFederal": "Perícias, laudos, exames técnicos e análises técnicas."
    },
    {
        "CodigoServicoMunicipal": "6911702",
        "DescricaoServicoMunicipal": "Atividades auxiliares da justiça",
        "CodigoServicoFederal": "17.15",
        "DescricaoServicoFederal": "Arbitragem de qualquer espécie, inclusive jurídica."
    },
    {
        "CodigoServicoMunicipal": "6911703",
        "DescricaoServicoMunicipal": "Agente de propriedade industrial",
        "CodigoServicoFederal": "10.03",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de direitos de propriedade industrial, artística ou literária."
    },
    {
        "CodigoServicoMunicipal": "6912500",
        "DescricaoServicoMunicipal": "Cartórios",
        "CodigoServicoFederal": "21.01",
        "DescricaoServicoFederal": "Serviços de registros públicos, cartorários e notariais."
    },
    {
        "CodigoServicoMunicipal": "6920601",
        "DescricaoServicoMunicipal": "Atividades de contabilidade",
        "CodigoServicoFederal": "17.19",
        "DescricaoServicoFederal": "Contabilidade, inclusive serviços técnicos e auxiliares."
    },
    {
        "CodigoServicoMunicipal": "6920602",
        "DescricaoServicoMunicipal": "Atividades de consultoria e auditoria contábil e tributária",
        "CodigoServicoFederal": "17.01",
        "DescricaoServicoFederal": "Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista; análise, exame, pesquisa, coleta, compilação e fornecimento de dados e informações de qualquer natureza, inclusive cadastro e similares."
    },
    {
        "CodigoServicoMunicipal": "6920602",
        "DescricaoServicoMunicipal": "Atividades de consultoria e auditoria contábil e tributária",
        "CodigoServicoFederal": "17.09",
        "DescricaoServicoFederal": "Perícias, laudos, exames técnicos e análises técnicas."
    },
    {
        "CodigoServicoMunicipal": "6920602",
        "DescricaoServicoMunicipal": "Atividades de consultoria e auditoria contábil e tributária",
        "CodigoServicoFederal": "17.16",
        "DescricaoServicoFederal": "Auditoria"
    },
    {
        "CodigoServicoMunicipal": "7020400",
        "DescricaoServicoMunicipal": "Assessoria, consultoria, orientação e assistência em gestão, negócios,",
        "CodigoServicoFederal": "17.01",
        "DescricaoServicoFederal": "Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista; análise, exame, pesquisa, coleta, compilação e fornecimento de dados e informações de qualquer natureza, inclusive cadastro e similares."
    },
    {
        "CodigoServicoMunicipal": "7020400",
        "DescricaoServicoMunicipal": "Assessoria, consultoria, orientação e assistência em gestão, negócios,",
        "CodigoServicoFederal": "17.03",
        "DescricaoServicoFederal": "Planejamento, coordenação, programação ou organização técnica, financeira ou administrativa."
    },
    {
        "CodigoServicoMunicipal": "7020400",
        "DescricaoServicoMunicipal": "Assessoria, consultoria, orientação e assistência em gestão, negócios,",
        "CodigoServicoFederal": "17.17",
        "DescricaoServicoFederal": "Análise de Organização e Métodos."
    },
    {
        "CodigoServicoMunicipal": "7020400",
        "DescricaoServicoMunicipal": "Assessoria, consultoria, orientação e assistência em gestão, negócios,",
        "CodigoServicoFederal": "17.20",
        "DescricaoServicoFederal": "Consultoria e assessoria econômica ou financeira."
    },
    {
        "CodigoServicoMunicipal": "7020400",
        "DescricaoServicoMunicipal": "Assessoria, consultoria, orientação e assistência em gestão, negócios,",
        "CodigoServicoFederal": "35.01",
        "DescricaoServicoFederal": "Serviços de reportagem, assessoria de imprensa, jornalismo e relações públicas."
    },
    {
        "CodigoServicoMunicipal": "7111100",
        "DescricaoServicoMunicipal": "Serviços de arquitetura",
        "CodigoServicoFederal": "07.01",
        "DescricaoServicoFederal": "Engenharia, agronomia, agrimensura, arquitetura, geologia, urbanismo, paisagismo e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7112000",
        "DescricaoServicoMunicipal": "Serviços de engenharia",
        "CodigoServicoFederal": "07.01",
        "DescricaoServicoFederal": "Engenharia, agronomia, agrimensura, arquitetura, geologia, urbanismo, paisagismo e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7112000",
        "DescricaoServicoMunicipal": "Serviços de engenharia",
        "CodigoServicoFederal": "07.03",
        "DescricaoServicoFederal": "Elaboração de planos diretores, estudos de viabilidade, estudos organizacionais e outros, relacionados com obras e serviços de engenharia; elaboração de anteprojetos, projetos básicos e projetos executivos para trabalhos de engenharia."
    },
    {
        "CodigoServicoMunicipal": "7112000",
        "DescricaoServicoMunicipal": "Serviços de engenharia",
        "CodigoServicoFederal": "07.19",
        "DescricaoServicoFederal": "Acompanhamento e fiscalização da execução de obras de engenharia, arquitetura e urbanismo."
    },
    {
        "CodigoServicoMunicipal": "7112000",
        "DescricaoServicoMunicipal": "Serviços de engenharia",
        "CodigoServicoFederal": "17.09",
        "DescricaoServicoFederal": "Perícias, laudos, exames técnicos e análises técnicas."
    },
    {
        "CodigoServicoMunicipal": "7112000",
        "DescricaoServicoMunicipal": "Serviços de engenharia",
        "CodigoServicoFederal": "28.01",
        "DescricaoServicoFederal": "Serviços de avaliação de bens e serviços de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "7119701",
        "DescricaoServicoMunicipal": "Serviços de cartografia, topografia e geodésia",
        "CodigoServicoFederal": "07.01",
        "DescricaoServicoFederal": "Engenharia, agronomia, agrimensura, arquitetura, geologia, urbanismo, paisagismo e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7119701",
        "DescricaoServicoMunicipal": "Serviços de cartografia, topografia e geodésia",
        "CodigoServicoFederal": "07.20",
        "DescricaoServicoFederal": "Aerofotogrametria (inclusive interpretação), cartografia, mapeamento, levantamentos topográficos, batimétricos, geográficos, geodésicos, geológicos, geofísicos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7119702",
        "DescricaoServicoMunicipal": "Atividades de estudos geológicos",
        "CodigoServicoFederal": "07.01",
        "DescricaoServicoFederal": "Engenharia, agronomia, agrimensura, arquitetura, geologia, urbanismo, paisagismo e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7119702",
        "DescricaoServicoMunicipal": "Atividades de estudos geológicos",
        "CodigoServicoFederal": "07.20",
        "DescricaoServicoFederal": "Aerofotogrametria (inclusive interpretação), cartografia, mapeamento, levantamentos topográficos, batimétricos, geográficos, geodésicos, geológicos, geofísicos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7119703",
        "DescricaoServicoMunicipal": "Serviços de desenho técnico relacionados à arquitetura e engenharia",
        "CodigoServicoFederal": "32.01",
        "DescricaoServicoFederal": "Serviços de desenhos técnicos."
    },
    {
        "CodigoServicoMunicipal": "7119704",
        "DescricaoServicoMunicipal": "Serviços de perícia técnica relacionados à segurança do trabalho",
        "CodigoServicoFederal": "17.09",
        "DescricaoServicoFederal": "Perícias, laudos, exames técnicos e análises técnicas."
    },
    {
        "CodigoServicoMunicipal": "7119799",
        "DescricaoServicoMunicipal": "Atividades técnicas relacionadas à engenharia e arquitetura não especi",
        "CodigoServicoFederal": "07.20",
        "DescricaoServicoFederal": "Aerofotogrametria (inclusive interpretação), cartografia, mapeamento, levantamentos topográficos, batimétricos, geográficos, geodésicos, geológicos, geofísicos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7119799",
        "DescricaoServicoMunicipal": "Atividades técnicas relacionadas à engenharia e arquitetura não especi",
        "CodigoServicoFederal": "31.01",
        "DescricaoServicoFederal": "Serviços técnicos em edificações, eletrônica, eletrotécnica, mecânica, telecomunicações e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7120100",
        "DescricaoServicoMunicipal": "Testes e análises técnicas",
        "CodigoServicoFederal": "17.09",
        "DescricaoServicoFederal": "Perícias, laudos, exames técnicos e análises técnicas."
    },
    {
        "CodigoServicoMunicipal": "7210000",
        "DescricaoServicoMunicipal": "Pesquisa e desenvolvimento experimental em ciências físicas e naturais",
        "CodigoServicoFederal": "02.01",
        "DescricaoServicoFederal": "Serviços de pesquisas e desenvolvimento de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "7210000",
        "DescricaoServicoMunicipal": "Pesquisa e desenvolvimento experimental em ciências físicas e naturais",
        "CodigoServicoFederal": "30.01",
        "DescricaoServicoFederal": "Serviços de biologia, biotecnologia e química."
    },
    {
        "CodigoServicoMunicipal": "7220700",
        "DescricaoServicoMunicipal": "Pesquisa e desenvolvimento experimental em ciências sociais e humanas",
        "CodigoServicoFederal": "02.01",
        "DescricaoServicoFederal": "Serviços de pesquisas e desenvolvimento de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "7311400",
        "DescricaoServicoMunicipal": "Propaganda e publicidade, planejamento e elaboração de campanhas publi",
        "CodigoServicoFederal": "10.08",
        "DescricaoServicoFederal": "Agenciamento de publicidade e propaganda, inclusive o agenciamento de veiculação por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "7311400",
        "DescricaoServicoMunicipal": "Propaganda e publicidade, planejamento e elaboração de campanhas publi",
        "CodigoServicoFederal": "17.06",
        "DescricaoServicoFederal": "Propaganda e publicidade, inclusive promoção de vendas, planejamento de campanhas ou sistemas de publicidade, elaboração de desenhos, textos e demais materiais publicitários."
    },
    {
        "CodigoServicoMunicipal": "7312200",
        "DescricaoServicoMunicipal": "Agenciamento de espaços para publicidade, exceto em veículos de comuni",
        "CodigoServicoFederal": "10.08",
        "DescricaoServicoFederal": "Agenciamento de publicidade e propaganda, inclusive o agenciamento de veiculação por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "7319001",
        "DescricaoServicoMunicipal": "Criação de estandes para feiras e exposições",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "7319001",
        "DescricaoServicoMunicipal": "Criação de estandes para feiras e exposições",
        "CodigoServicoFederal": "17.06",
        "DescricaoServicoFederal": "Propaganda e publicidade, inclusive promoção de vendas, planejamento de campanhas ou sistemas de publicidade, elaboração de desenhos, textos e demais materiais publicitários."
    },
    {
        "CodigoServicoMunicipal": "7319002",
        "DescricaoServicoMunicipal": "Promoção de vendas",
        "CodigoServicoFederal": "17.06",
        "DescricaoServicoFederal": "Propaganda e publicidade, inclusive promoção de vendas, planejamento de campanhas ou sistemas de publicidade, elaboração de desenhos, textos e demais materiais publicitários."
    },
    {
        "CodigoServicoMunicipal": "7319003",
        "DescricaoServicoMunicipal": "Marketing direto",
        "CodigoServicoFederal": "17.06",
        "DescricaoServicoFederal": "Propaganda e publicidade, inclusive promoção de vendas, planejamento de campanhas ou sistemas de publicidade, elaboração de desenhos, textos e demais materiais publicitários."
    },
    {
        "CodigoServicoMunicipal": "7319004",
        "DescricaoServicoMunicipal": "Consultoria em publicidade",
        "CodigoServicoFederal": "17.01",
        "DescricaoServicoFederal": "Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista; análise, exame, pesquisa, coleta, compilação e fornecimento de dados e informações de qualquer natureza, inclusive cadastro e similares."
    },
    {
        "CodigoServicoMunicipal": "7319099",
        "DescricaoServicoMunicipal": "Outras atividades de publicidade não especificadas anteriormente",
        "CodigoServicoFederal": "17.06",
        "DescricaoServicoFederal": "Propaganda e publicidade, inclusive promoção de vendas, planejamento de campanhas ou sistemas de publicidade, elaboração de desenhos, textos e demais materiais publicitários."
    },
    {
        "CodigoServicoMunicipal": "7320300",
        "DescricaoServicoMunicipal": "Pesquisas de mercado e de opinião pública",
        "CodigoServicoFederal": "17.01",
        "DescricaoServicoFederal": "Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista; análise, exame, pesquisa, coleta, compilação e fornecimento de dados e informações de qualquer natureza, inclusive cadastro e similares."
    },
    {
        "CodigoServicoMunicipal": "7320300",
        "DescricaoServicoMunicipal": "Pesquisas de mercado e de opinião pública",
        "CodigoServicoFederal": "17.21",
        "DescricaoServicoFederal": "Estatística"
    },
    {
        "CodigoServicoMunicipal": "7410201",
        "DescricaoServicoMunicipal": "Design",
        "CodigoServicoFederal": "07.11",
        "DescricaoServicoFederal": "Decoração e jardinagem, inclusive corte e poda de árvores."
    },
    {
        "CodigoServicoMunicipal": "7410201",
        "DescricaoServicoMunicipal": "Design",
        "CodigoServicoFederal": "23.01",
        "DescricaoServicoFederal": "Serviços de programação e comunicação visual, desenho industrial e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7410201",
        "DescricaoServicoMunicipal": "Design",
        "CodigoServicoFederal": "39.01",
        "DescricaoServicoFederal": "Serviços de ourivesaria e lapidação (quando o material for fornecido pelo tomador do serviço)."
    },
    {
        "CodigoServicoMunicipal": "7410202",
        "DescricaoServicoMunicipal": "Decoração de interiores",
        "CodigoServicoFederal": "07.11",
        "DescricaoServicoFederal": "Decoração e jardinagem, inclusive corte e poda de árvores."
    },
    {
        "CodigoServicoMunicipal": "7420001",
        "DescricaoServicoMunicipal": "Atividades de produção de fotografias, exceto aérea e submarina",
        "CodigoServicoFederal": "13.03",
        "DescricaoServicoFederal": "Fotografia e cinematografia, inclusive revelação, ampliação, cópia, reprodução, trucagem e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7420002",
        "DescricaoServicoMunicipal": "Atividades de produção de fotografias aéreas e submarinas",
        "CodigoServicoFederal": "13.03",
        "DescricaoServicoFederal": "Fotografia e cinematografia, inclusive revelação, ampliação, cópia, reprodução, trucagem e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7420003",
        "DescricaoServicoMunicipal": "Laboratórios fotográficos",
        "CodigoServicoFederal": "13.03",
        "DescricaoServicoFederal": "Fotografia e cinematografia, inclusive revelação, ampliação, cópia, reprodução, trucagem e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7420004",
        "DescricaoServicoMunicipal": "Filmagem de festas e eventos",
        "CodigoServicoFederal": "13.03",
        "DescricaoServicoFederal": "Fotografia e cinematografia, inclusive revelação, ampliação, cópia, reprodução, trucagem e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7420005",
        "DescricaoServicoMunicipal": "Serviços de microfilmagem",
        "CodigoServicoFederal": "13.04",
        "DescricaoServicoFederal": "Reprografia, microfilmagem e digitalização."
    },
    {
        "CodigoServicoMunicipal": "7490101",
        "DescricaoServicoMunicipal": "Serviços de tradução, interpretação e similares",
        "CodigoServicoFederal": "17.02",
        "DescricaoServicoFederal": "Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra-estrutura administrativa e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7490102",
        "DescricaoServicoMunicipal": "Escafandria e mergulho",
        "CodigoServicoFederal": "07.21",
        "DescricaoServicoFederal": "Pesquisa, perfuração, cimentação, mergulho, perfilagem, concretação, testemunhagem, pescaria, estimulação e outros serviços relacionados com a exploração e explotação de petróleo, gás natural e de outros recursos minerais."
    },
    {
        "CodigoServicoMunicipal": "7490102",
        "DescricaoServicoMunicipal": "Escafandria e mergulho",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "7490103",
        "DescricaoServicoMunicipal": "Serviços de agronomia e de consultoria às atividades agrícolas e pecuá",
        "CodigoServicoFederal": "05.01",
        "DescricaoServicoFederal": "Medicina veterinária e zootecnia."
    },
    {
        "CodigoServicoMunicipal": "7490103",
        "DescricaoServicoMunicipal": "Serviços de agronomia e de consultoria às atividades agrícolas e pecuá",
        "CodigoServicoFederal": "17.01",
        "DescricaoServicoFederal": "Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista; análise, exame, pesquisa, coleta, compilação e fornecimento de dados e informações de qualquer natureza, inclusive cadastro e similares."
    },
    {
        "CodigoServicoMunicipal": "7490104",
        "DescricaoServicoMunicipal": "Atividades de intermediação e agenciamento de serviços e negócios em g",
        "CodigoServicoFederal": "10.01",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de câmbio, de seguros, de cartões de crédito, de planos de saúde e de planos de previdência privada."
    },
    {
        "CodigoServicoMunicipal": "7490104",
        "DescricaoServicoMunicipal": "Atividades de intermediação e agenciamento de serviços e negócios em g",
        "CodigoServicoFederal": "10.02",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "7490104",
        "DescricaoServicoMunicipal": "Atividades de intermediação e agenciamento de serviços e negócios em g",
        "CodigoServicoFederal": "10.03",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de direitos de propriedade industrial, artística ou literária."
    },
    {
        "CodigoServicoMunicipal": "7490104",
        "DescricaoServicoMunicipal": "Atividades de intermediação e agenciamento de serviços e negócios em g",
        "CodigoServicoFederal": "10.04",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de contratos de arrendamento mercantil (leasing), de franquia (franchising) e de faturização (factoring)."
    },
    {
        "CodigoServicoMunicipal": "7490104",
        "DescricaoServicoMunicipal": "Atividades de intermediação e agenciamento de serviços e negócios em g",
        "CodigoServicoFederal": "10.05",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de bens móveis ou imóveis, não abrangidos em outros itens ou subitens, inclusive aqueles realizados no âmbito de Bolsas de Mercadorias e Futuros, por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "7490104",
        "DescricaoServicoMunicipal": "Atividades de intermediação e agenciamento de serviços e negócios em g",
        "CodigoServicoFederal": "10.08",
        "DescricaoServicoFederal": "Agenciamento de publicidade e propaganda, inclusive o agenciamento de veiculação por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "7490105",
        "DescricaoServicoMunicipal": "Agenciamento de profissionais para atividades esportivas, culturais e ",
        "CodigoServicoFederal": "10.02",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "7490105",
        "DescricaoServicoMunicipal": "Agenciamento de profissionais para atividades esportivas, culturais e ",
        "CodigoServicoFederal": "37.01",
        "DescricaoServicoFederal": "Serviços de artistas, atletas, modelos e manequins."
    },
    {
        "CodigoServicoMunicipal": "7490199",
        "DescricaoServicoMunicipal": "Serviço de avaliação de conhecimentos de qualquer natureza",
        "CodigoServicoFederal": "07.12",
        "DescricaoServicoFederal": "Controle e tratamento de efluentes de qualquer natureza e de agentes físicos, químicos e biológicos."
    },
    {
        "CodigoServicoMunicipal": "7490199",
        "DescricaoServicoMunicipal": "Serviço de avaliação de conhecimentos de qualquer natureza",
        "CodigoServicoFederal": "07.18",
        "DescricaoServicoFederal": "Limpeza e dragagem de rios, portos, canais, baías, lagos, lagoas, represas, açudes e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7490199",
        "DescricaoServicoMunicipal": "Serviço de avaliação de conhecimentos de qualquer natureza",
        "CodigoServicoFederal": "07.21",
        "DescricaoServicoFederal": "Pesquisa, perfuração, cimentação, mergulho, perfilagem, concretação, testemunhagem, pescaria, estimulação e outros serviços relacionados com a exploração e explotação de petróleo, gás natural e de outros recursos minerais."
    },
    {
        "CodigoServicoMunicipal": "7490199",
        "DescricaoServicoMunicipal": "Serviço de avaliação de conhecimentos de qualquer natureza",
        "CodigoServicoFederal": "07.22",
        "DescricaoServicoFederal": "Nucleação e bombardeamento de nuvens e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7490199",
        "DescricaoServicoMunicipal": "Serviço de avaliação de conhecimentos de qualquer natureza",
        "CodigoServicoFederal": "17.01",
        "DescricaoServicoFederal": "Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista; análise, exame, pesquisa, coleta, compilação e fornecimento de dados e informações de qualquer natureza, inclusive cadastro e similares."
    },
    {
        "CodigoServicoMunicipal": "7490199",
        "DescricaoServicoMunicipal": "Serviço de avaliação de conhecimentos de qualquer natureza",
        "CodigoServicoFederal": "17.02",
        "DescricaoServicoFederal": "Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra-estrutura administrativa e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7490199",
        "DescricaoServicoMunicipal": "Serviço de avaliação de conhecimentos de qualquer natureza",
        "CodigoServicoFederal": "17.21",
        "DescricaoServicoFederal": "Estatística"
    },
    {
        "CodigoServicoMunicipal": "7490199",
        "DescricaoServicoMunicipal": "Serviço de avaliação de conhecimentos de qualquer natureza",
        "CodigoServicoFederal": "23.01",
        "DescricaoServicoFederal": "Serviços de programação e comunicação visual, desenho industrial e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7490199",
        "DescricaoServicoMunicipal": "Serviço de avaliação de conhecimentos de qualquer natureza",
        "CodigoServicoFederal": "28.01",
        "DescricaoServicoFederal": "Serviços de avaliação de bens e serviços de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "7490199",
        "DescricaoServicoMunicipal": "Serviço de avaliação de conhecimentos de qualquer natureza",
        "CodigoServicoFederal": "36.01",
        "DescricaoServicoFederal": "Serviços de meteorologia."
    },
    {
        "CodigoServicoMunicipal": "7500100",
        "DescricaoServicoMunicipal": "Atividades veterinárias",
        "CodigoServicoFederal": "05.01",
        "DescricaoServicoFederal": "Medicina veterinária e zootecnia."
    },
    {
        "CodigoServicoMunicipal": "7500100",
        "DescricaoServicoMunicipal": "Atividades veterinárias",
        "CodigoServicoFederal": "05.02",
        "DescricaoServicoFederal": "Hospitais, clínicas, ambulatórios, prontos-socorros e congêneres, na área veterinária."
    },
    {
        "CodigoServicoMunicipal": "7500100",
        "DescricaoServicoMunicipal": "Atividades veterinárias",
        "CodigoServicoFederal": "05.03",
        "DescricaoServicoFederal": "Laboratórios de análise na área veterinária."
    },
    {
        "CodigoServicoMunicipal": "7500100",
        "DescricaoServicoMunicipal": "Atividades veterinárias",
        "CodigoServicoFederal": "05.05",
        "DescricaoServicoFederal": "Bancos de sangue e de órgãos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7500100",
        "DescricaoServicoMunicipal": "Atividades veterinárias",
        "CodigoServicoFederal": "05.06",
        "DescricaoServicoFederal": "Coleta de sangue, leite, tecidos, sêmen, órgãos e materiais biológicos de qualquer espécie."
    },
    {
        "CodigoServicoMunicipal": "7500100",
        "DescricaoServicoMunicipal": "Atividades veterinárias",
        "CodigoServicoFederal": "05.07",
        "DescricaoServicoFederal": "Unidade de atendimento, assistência ou tratamento móvel e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7732202",
        "DescricaoServicoMunicipal": "Aluguel de andaimes",
        "CodigoServicoFederal": "03.05",
        "DescricaoServicoFederal": "Cessão de andaimes, palcos, coberturas e outras estruturas de uso temporário."
    },
    {
        "CodigoServicoMunicipal": "7739003",
        "DescricaoServicoMunicipal": "Aluguel de palcos, coberturas e outras estruturas de uso temporário, e",
        "CodigoServicoFederal": "03.05",
        "DescricaoServicoFederal": "Cessão de andaimes, palcos, coberturas e outras estruturas de uso temporário."
    },
    {
        "CodigoServicoMunicipal": "7740300",
        "DescricaoServicoMunicipal": "Gestão de ativos intangíveis não-financeiros",
        "CodigoServicoFederal": "03.02",
        "DescricaoServicoFederal": "Cessão de direito de uso de marcas e de sinais de propaganda."
    },
    {
        "CodigoServicoMunicipal": "7740300",
        "DescricaoServicoMunicipal": "Gestão de ativos intangíveis não-financeiros",
        "CodigoServicoFederal": "10.02",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "7740300",
        "DescricaoServicoMunicipal": "Gestão de ativos intangíveis não-financeiros",
        "CodigoServicoFederal": "17.08",
        "DescricaoServicoFederal": "Franquia (franchising)."
    },
    {
        "CodigoServicoMunicipal": "7740300",
        "DescricaoServicoMunicipal": "Gestão de ativos intangíveis não-financeiros",
        "CodigoServicoFederal": "17.12",
        "DescricaoServicoFederal": "Administração em geral, inclusive de bens e negócios de terceiros."
    },
    {
        "CodigoServicoMunicipal": "7810800",
        "DescricaoServicoMunicipal": "Seleção e agenciamento de mão-de-obra",
        "CodigoServicoFederal": "17.04",
        "DescricaoServicoFederal": "Recrutamento, agenciamento, seleção e colocação de mão-de-obra."
    },
    {
        "CodigoServicoMunicipal": "7820500",
        "DescricaoServicoMunicipal": "Locação de mão-de-obra temporária",
        "CodigoServicoFederal": "17.05",
        "DescricaoServicoFederal": "Fornecimento de mão-de-obra, mesmo em caráter temporário, inclusive de empregados ou trabalhadores, avulsos ou temporários, contratados pelo prestador de serviço."
    },
    {
        "CodigoServicoMunicipal": "7830200",
        "DescricaoServicoMunicipal": "Fornecimento e gestão de recursos humanos para terceiros",
        "CodigoServicoFederal": "17.05",
        "DescricaoServicoFederal": "Fornecimento de mão-de-obra, mesmo em caráter temporário, inclusive de empregados ou trabalhadores, avulsos ou temporários, contratados pelo prestador de serviço."
    },
    {
        "CodigoServicoMunicipal": "7911200",
        "DescricaoServicoMunicipal": "Agências de viagens",
        "CodigoServicoFederal": "09.02",
        "DescricaoServicoFederal": "Agenciamento, organização, promoção, intermediação e execução de programas de turismo, passeios, viagens, excursões, hospedagens e congêneres."
    },
    {
        "CodigoServicoMunicipal": "7911200",
        "DescricaoServicoMunicipal": "Agências de viagens",
        "CodigoServicoFederal": "09.03",
        "DescricaoServicoFederal": "Guias de turismo."
    },
    {
        "CodigoServicoMunicipal": "7912100",
        "DescricaoServicoMunicipal": "Operadores turísticos",
        "CodigoServicoFederal": "09.03",
        "DescricaoServicoFederal": "Guias de turismo."
    },
    {
        "CodigoServicoMunicipal": "7990200",
        "DescricaoServicoMunicipal": "Serviços de reservas e outros serviços de turismo não especificados an",
        "CodigoServicoFederal": "09.02",
        "DescricaoServicoFederal": "Agenciamento, organização, promoção, intermediação e execução de programas de turismo, passeios, viagens, excursões, hospedagens e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8011101",
        "DescricaoServicoMunicipal": "Atividades de vigilância e segurança privada",
        "CodigoServicoFederal": "11.02",
        "DescricaoServicoFederal": "Vigilância, segurança ou monitoramento de bens, pessoas e semoventes."
    },
    {
        "CodigoServicoMunicipal": "8011101",
        "DescricaoServicoMunicipal": "Atividades de vigilância e segurança privada",
        "CodigoServicoFederal": "11.03",
        "DescricaoServicoFederal": "Escolta, inclusive de veículos e cargas."
    },
    {
        "CodigoServicoMunicipal": "8011102",
        "DescricaoServicoMunicipal": "Serviços de adestramento de cães de guarda",
        "CodigoServicoFederal": "05.08",
        "DescricaoServicoFederal": "Guarda, tratamento, amestramento, embelezamento, alojamento e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8011102",
        "DescricaoServicoMunicipal": "Serviços de adestramento de cães de guarda",
        "CodigoServicoFederal": "11.04",
        "DescricaoServicoFederal": "Armazenamento, depósito, carga, descarga, arrumação e guarda de bens de qualquer espécie."
    },
    {
        "CodigoServicoMunicipal": "8012900",
        "DescricaoServicoMunicipal": "Atividades de transporte de valores",
        "CodigoServicoFederal": "11.02",
        "DescricaoServicoFederal": "Vigilância, segurança ou monitoramento de bens, pessoas e semoventes."
    },
    {
        "CodigoServicoMunicipal": "8012900",
        "DescricaoServicoMunicipal": "Atividades de transporte de valores",
        "CodigoServicoFederal": "11.03",
        "DescricaoServicoFederal": "Escolta, inclusive de veículos e cargas."
    },
    {
        "CodigoServicoMunicipal": "8012900",
        "DescricaoServicoMunicipal": "Atividades de transporte de valores",
        "CodigoServicoFederal": "11.04",
        "DescricaoServicoFederal": "Armazenamento, depósito, carga, descarga, arrumação e guarda de bens de qualquer espécie."
    },
    {
        "CodigoServicoMunicipal": "8012900",
        "DescricaoServicoMunicipal": "Atividades de transporte de valores",
        "CodigoServicoFederal": "26.01",
        "DescricaoServicoFederal": "Serviços de coleta, remessa ou entrega de correspondências, documentos, objetos, bens ou valores, inclusive pelos correios e suas agências franqueadas; courrier e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8020000",
        "DescricaoServicoMunicipal": "Atividades de monitoramento de sistemas de segurança",
        "CodigoServicoFederal": "11.02",
        "DescricaoServicoFederal": "Vigilância, segurança ou monitoramento de bens, pessoas e semoventes."
    },
    {
        "CodigoServicoMunicipal": "8020000",
        "DescricaoServicoMunicipal": "Atividades de monitoramento de sistemas de segurança",
        "CodigoServicoFederal": "11.04",
        "DescricaoServicoFederal": "Armazenamento, depósito, carga, descarga, arrumação e guarda de bens de qualquer espécie."
    },
    {
        "CodigoServicoMunicipal": "8020000",
        "DescricaoServicoMunicipal": "Atividades de monitoramento de sistemas de segurança",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "8020001",
        "DescricaoServicoMunicipal": "Atividades de monitoramento de sistemas de segurança eletrônico",
        "CodigoServicoFederal": "11.02",
        "DescricaoServicoFederal": "Vigilância, segurança ou monitoramento de bens, pessoas e semoventes."
    },
    {
        "CodigoServicoMunicipal": "8020002",
        "DescricaoServicoMunicipal": "Outras atividades de serviço de segurança",
        "CodigoServicoFederal": "11.02",
        "DescricaoServicoFederal": "Vigilância, segurança ou monitoramento de bens, pessoas e semoventes."
    },
    {
        "CodigoServicoMunicipal": "8030700",
        "DescricaoServicoMunicipal": "Atividades de investigação particular",
        "CodigoServicoFederal": "34.01",
        "DescricaoServicoFederal": "Serviços de investigações particulares, detetives e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8111700",
        "DescricaoServicoMunicipal": "Serviços combinados para apoio a edifícios, exceto condomínios prediai",
        "CodigoServicoFederal": "07.10",
        "DescricaoServicoFederal": "Limpeza, manutenção e conservação de vias e logradouros públicos, imóveis, chaminés, piscinas, parques, jardins e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8111700",
        "DescricaoServicoMunicipal": "Serviços combinados para apoio a edifícios, exceto condomínios prediai",
        "CodigoServicoFederal": "07.11",
        "DescricaoServicoFederal": "Decoração e jardinagem, inclusive corte e poda de árvores."
    },
    {
        "CodigoServicoMunicipal": "8111700",
        "DescricaoServicoMunicipal": "Serviços combinados para apoio a edifícios, exceto condomínios prediai",
        "CodigoServicoFederal": "17.05",
        "DescricaoServicoFederal": "Fornecimento de mão-de-obra, mesmo em caráter temporário, inclusive de empregados ou trabalhadores, avulsos ou temporários, contratados pelo prestador de serviço."
    },
    {
        "CodigoServicoMunicipal": "8121400",
        "DescricaoServicoMunicipal": "Limpeza em prédios e em domicílios",
        "CodigoServicoFederal": "07.10",
        "DescricaoServicoFederal": "Limpeza, manutenção e conservação de vias e logradouros públicos, imóveis, chaminés, piscinas, parques, jardins e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8121400",
        "DescricaoServicoMunicipal": "Limpeza em prédios e em domicílios",
        "CodigoServicoFederal": "07.11",
        "DescricaoServicoFederal": "Decoração e jardinagem, inclusive corte e poda de árvores."
    },
    {
        "CodigoServicoMunicipal": "8121400",
        "DescricaoServicoMunicipal": "Limpeza em prédios e em domicílios",
        "CodigoServicoFederal": "07.12",
        "DescricaoServicoFederal": "Controle e tratamento de efluentes de qualquer natureza e de agentes físicos, químicos e biológicos."
    },
    {
        "CodigoServicoMunicipal": "8121400",
        "DescricaoServicoMunicipal": "Limpeza em prédios e em domicílios",
        "CodigoServicoFederal": "07.13",
        "DescricaoServicoFederal": "Dedetização, desinfecção, desinsetização, imunização, higienização, desratização, pulverização e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8122200",
        "DescricaoServicoMunicipal": "Imunização e controle de pragas urbanas",
        "CodigoServicoFederal": "07.13",
        "DescricaoServicoFederal": "Dedetização, desinfecção, desinsetização, imunização, higienização, desratização, pulverização e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8129000",
        "DescricaoServicoMunicipal": "Serviço de esterilização",
        "CodigoServicoFederal": "07.09",
        "DescricaoServicoFederal": "Varrição, coleta, remoção, incineração, tratamento, reciclagem, separação e destinação final de lixo, rejeitos e outros resíduos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "8129000",
        "DescricaoServicoMunicipal": "Serviço de esterilização",
        "CodigoServicoFederal": "07.10",
        "DescricaoServicoFederal": "Limpeza, manutenção e conservação de vias e logradouros públicos, imóveis, chaminés, piscinas, parques, jardins e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8129000",
        "DescricaoServicoMunicipal": "Serviço de esterilização",
        "CodigoServicoFederal": "07.11",
        "DescricaoServicoFederal": "Decoração e jardinagem, inclusive corte e poda de árvores."
    },
    {
        "CodigoServicoMunicipal": "8129000",
        "DescricaoServicoMunicipal": "Serviço de esterilização",
        "CodigoServicoFederal": "07.12",
        "DescricaoServicoFederal": "Controle e tratamento de efluentes de qualquer natureza e de agentes físicos, químicos e biológicos."
    },
    {
        "CodigoServicoMunicipal": "8129000",
        "DescricaoServicoMunicipal": "Serviço de esterilização",
        "CodigoServicoFederal": "07.13",
        "DescricaoServicoFederal": "Dedetização, desinfecção, desinsetização, imunização, higienização, desratização, pulverização e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8130300",
        "DescricaoServicoMunicipal": "Atividades paisagísticas",
        "CodigoServicoFederal": "07.10",
        "DescricaoServicoFederal": "Limpeza, manutenção e conservação de vias e logradouros públicos, imóveis, chaminés, piscinas, parques, jardins e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8130300",
        "DescricaoServicoMunicipal": "Atividades paisagísticas",
        "CodigoServicoFederal": "07.11",
        "DescricaoServicoFederal": "Decoração e jardinagem, inclusive corte e poda de árvores."
    },
    {
        "CodigoServicoMunicipal": "8130300",
        "DescricaoServicoMunicipal": "Atividades paisagísticas",
        "CodigoServicoFederal": "07.12",
        "DescricaoServicoFederal": "Controle e tratamento de efluentes de qualquer natureza e de agentes físicos, químicos e biológicos."
    },
    {
        "CodigoServicoMunicipal": "8130300",
        "DescricaoServicoMunicipal": "Atividades paisagísticas",
        "CodigoServicoFederal": "07.13",
        "DescricaoServicoFederal": "Dedetização, desinfecção, desinsetização, imunização, higienização, desratização, pulverização e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8211300",
        "DescricaoServicoMunicipal": "Serviços combinados de escritório e apoio administrativo",
        "CodigoServicoFederal": "03.03",
        "DescricaoServicoFederal": "Exploração de salões de festas, centro de convenções, escritórios virtuais, stands, quadras esportivas, estádios, ginásios, auditórios, casas de espetáculos, parques de diversões, canchas e congêneres, para realização de eventos ou negócios de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "8211300",
        "DescricaoServicoMunicipal": "Serviços combinados de escritório e apoio administrativo",
        "CodigoServicoFederal": "17.02",
        "DescricaoServicoFederal": "Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra-estrutura administrativa e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8211300",
        "DescricaoServicoMunicipal": "Serviços combinados de escritório e apoio administrativo",
        "CodigoServicoFederal": "17.03",
        "DescricaoServicoFederal": "Planejamento, coordenação, programação ou organização técnica, financeira ou administrativa."
    },
    {
        "CodigoServicoMunicipal": "8219901",
        "DescricaoServicoMunicipal": "Fotocópias",
        "CodigoServicoFederal": "13.04",
        "DescricaoServicoFederal": "Reprografia, microfilmagem e digitalização."
    },
    {
        "CodigoServicoMunicipal": "8219999",
        "DescricaoServicoMunicipal": "Preparação de documentos e serviços especializados de apoio administra",
        "CodigoServicoFederal": "17.02",
        "DescricaoServicoFederal": "Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra-estrutura administrativa e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8220200",
        "DescricaoServicoMunicipal": "Atividades de teleatendimento",
        "CodigoServicoFederal": "10.09",
        "DescricaoServicoFederal": "Representação de qualquer natureza, inclusive comercial."
    },
    {
        "CodigoServicoMunicipal": "8220200",
        "DescricaoServicoMunicipal": "Atividades de teleatendimento",
        "CodigoServicoFederal": "17.02",
        "DescricaoServicoFederal": "Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra-estrutura administrativa e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8230001",
        "DescricaoServicoMunicipal": "Serviços de organização de feiras, congressos, exposições e festas",
        "CodigoServicoFederal": "12.08",
        "DescricaoServicoFederal": "Feiras, exposições, congressos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8230001",
        "DescricaoServicoMunicipal": "Serviços de organização de feiras, congressos, exposições e festas",
        "CodigoServicoFederal": "17.10",
        "DescricaoServicoFederal": "Planejamento, organização e administração de feiras, exposições, congressos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8230002",
        "DescricaoServicoMunicipal": "Casas de festas e eventos",
        "CodigoServicoFederal": "03.03",
        "DescricaoServicoFederal": "Exploração de salões de festas, centro de convenções, escritórios virtuais, stands, quadras esportivas, estádios, ginásios, auditórios, casas de espetáculos, parques de diversões, canchas e congêneres, para realização de eventos ou negócios de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "8291100",
        "DescricaoServicoMunicipal": "Atividades de cobrança e informações cadastrais",
        "CodigoServicoFederal": "17.22",
        "DescricaoServicoFederal": "Cobrança em geral."
    },
    {
        "CodigoServicoMunicipal": "8292000",
        "DescricaoServicoMunicipal": "Envasamento e empacotamento sob contrato",
        "CodigoServicoFederal": "14.05",
        "DescricaoServicoFederal": "Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "8299701",
        "DescricaoServicoMunicipal": "Medição de consumo de energia elétrica, gás e água",
        "CodigoServicoFederal": "17.01",
        "DescricaoServicoFederal": "Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista; análise, exame, pesquisa, coleta, compilação e fornecimento de dados e informações de qualquer natureza, inclusive cadastro e similares."
    },
    {
        "CodigoServicoMunicipal": "8299703",
        "DescricaoServicoMunicipal": "Serviços de gravação de carimbos, exceto confecção",
        "CodigoServicoFederal": "24.01",
        "DescricaoServicoFederal": "Serviços de chaveiros, confecção de carimbos, placas, sinalização visual, banners, adesivos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8299704",
        "DescricaoServicoMunicipal": "Leiloeiros independentes",
        "CodigoServicoFederal": "17.13",
        "DescricaoServicoFederal": "Leilão e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8299706",
        "DescricaoServicoMunicipal": "Casas lotéricas",
        "CodigoServicoFederal": "19.01",
        "DescricaoServicoFederal": "Serviços de distribuição e venda de bilhetes e demais produtos de loteria, bingos, cartões, pules ou cupons de apostas, sorteios, prêmios, inclusive os decorrentes de títulos de capitalização e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8299799",
        "DescricaoServicoMunicipal": "Serviços de avaliação e despachos em geral",
        "CodigoServicoFederal": "10.10",
        "DescricaoServicoFederal": "Distribuição de bens de terceiros."
    },
    {
        "CodigoServicoMunicipal": "8299799",
        "DescricaoServicoMunicipal": "Serviços de avaliação e despachos em geral",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "8299799",
        "DescricaoServicoMunicipal": "Serviços de avaliação e despachos em geral",
        "CodigoServicoFederal": "17.02",
        "DescricaoServicoFederal": "Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra-estrutura administrativa e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8411600",
        "DescricaoServicoMunicipal": "Administração pública em geral",
        "CodigoServicoFederal": "17.12",
        "DescricaoServicoFederal": "Administração em geral, inclusive de bens e negócios de terceiros."
    },
    {
        "CodigoServicoMunicipal": "8511200",
        "DescricaoServicoMunicipal": "Educação infantil - creche",
        "CodigoServicoFederal": "08.01",
        "DescricaoServicoFederal": "Ensino regular pré-escolar, fundamental, médio e superior."
    },
    {
        "CodigoServicoMunicipal": "8512100",
        "DescricaoServicoMunicipal": "Educação infantil - pré-escola",
        "CodigoServicoFederal": "08.01",
        "DescricaoServicoFederal": "Ensino regular pré-escolar, fundamental, médio e superior."
    },
    {
        "CodigoServicoMunicipal": "8513900",
        "DescricaoServicoMunicipal": "Ensino fundamental",
        "CodigoServicoFederal": "08.01",
        "DescricaoServicoFederal": "Ensino regular pré-escolar, fundamental, médio e superior."
    },
    {
        "CodigoServicoMunicipal": "8520100",
        "DescricaoServicoMunicipal": "Ensino médio",
        "CodigoServicoFederal": "08.01",
        "DescricaoServicoFederal": "Ensino regular pré-escolar, fundamental, médio e superior."
    },
    {
        "CodigoServicoMunicipal": "8531700",
        "DescricaoServicoMunicipal": "Educação superior - graduação",
        "CodigoServicoFederal": "08.01",
        "DescricaoServicoFederal": "Ensino regular pré-escolar, fundamental, médio e superior."
    },
    {
        "CodigoServicoMunicipal": "8532500",
        "DescricaoServicoMunicipal": "Educação superior - graduação e pós-graduação",
        "CodigoServicoFederal": "08.01",
        "DescricaoServicoFederal": "Ensino regular pré-escolar, fundamental, médio e superior."
    },
    {
        "CodigoServicoMunicipal": "8533300",
        "DescricaoServicoMunicipal": "Educação superior - pós-graduação e extensão",
        "CodigoServicoFederal": "08.01",
        "DescricaoServicoFederal": "Ensino regular pré-escolar, fundamental, médio e superior."
    },
    {
        "CodigoServicoMunicipal": "8541400",
        "DescricaoServicoMunicipal": "Educação profissional de nível técnico",
        "CodigoServicoFederal": "08.01",
        "DescricaoServicoFederal": "Ensino regular pré-escolar, fundamental, médio e superior."
    },
    {
        "CodigoServicoMunicipal": "8542200",
        "DescricaoServicoMunicipal": "Educação profissional de nível tecnológico",
        "CodigoServicoFederal": "08.01",
        "DescricaoServicoFederal": "Ensino regular pré-escolar, fundamental, médio e superior."
    },
    {
        "CodigoServicoMunicipal": "8550302",
        "DescricaoServicoMunicipal": "Atividades de apoio à educação, exceto caixas escolares",
        "CodigoServicoFederal": "08.02",
        "DescricaoServicoFederal": "Instrução, treinamento, orientação pedagógica e educacional, avaliação de conhecimentos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "8550302",
        "DescricaoServicoMunicipal": "Atividades de apoio à educação, exceto caixas escolares",
        "CodigoServicoFederal": "10.03",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de direitos de propriedade industrial, artística ou literária."
    },
    {
        "CodigoServicoMunicipal": "8591100",
        "DescricaoServicoMunicipal": "Ensino de esportes",
        "CodigoServicoFederal": "06.04",
        "DescricaoServicoFederal": "Ginástica, dança, esportes, natação, artes marciais e demais atividades físicas."
    },
    {
        "CodigoServicoMunicipal": "8591100",
        "DescricaoServicoMunicipal": "Ensino de esportes",
        "CodigoServicoFederal": "09.02",
        "DescricaoServicoFederal": "Agenciamento, organização, promoção, intermediação e execução de programas de turismo, passeios, viagens, excursões, hospedagens e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8592901",
        "DescricaoServicoMunicipal": "Ensino de dança",
        "CodigoServicoFederal": "06.04",
        "DescricaoServicoFederal": "Ginástica, dança, esportes, natação, artes marciais e demais atividades físicas."
    },
    {
        "CodigoServicoMunicipal": "8592902",
        "DescricaoServicoMunicipal": "Ensino de artes cênicas, exceto dança",
        "CodigoServicoFederal": "08.02",
        "DescricaoServicoFederal": "Instrução, treinamento, orientação pedagógica e educacional, avaliação de conhecimentos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "8592903",
        "DescricaoServicoMunicipal": "Ensino de música",
        "CodigoServicoFederal": "08.02",
        "DescricaoServicoFederal": "Instrução, treinamento, orientação pedagógica e educacional, avaliação de conhecimentos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "8592999",
        "DescricaoServicoMunicipal": "Ensino de arte e cultura não especificado anteriormente",
        "CodigoServicoFederal": "08.02",
        "DescricaoServicoFederal": "Instrução, treinamento, orientação pedagógica e educacional, avaliação de conhecimentos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "8593700",
        "DescricaoServicoMunicipal": "Ensino de idiomas",
        "CodigoServicoFederal": "08.02",
        "DescricaoServicoFederal": "Instrução, treinamento, orientação pedagógica e educacional, avaliação de conhecimentos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "8599601",
        "DescricaoServicoMunicipal": "Centro de formação de condutores com ou sem pista de treinamento",
        "CodigoServicoFederal": "08.02",
        "DescricaoServicoFederal": "Instrução, treinamento, orientação pedagógica e educacional, avaliação de conhecimentos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "8599602",
        "DescricaoServicoMunicipal": "Cursos de pilotagem",
        "CodigoServicoFederal": "08.02",
        "DescricaoServicoFederal": "Instrução, treinamento, orientação pedagógica e educacional, avaliação de conhecimentos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "8599603",
        "DescricaoServicoMunicipal": "Treinamento em informática",
        "CodigoServicoFederal": "08.02",
        "DescricaoServicoFederal": "Instrução, treinamento, orientação pedagógica e educacional, avaliação de conhecimentos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "8599604",
        "DescricaoServicoMunicipal": "Treinamento em desenvolvimento profissional e gerencial",
        "CodigoServicoFederal": "08.02",
        "DescricaoServicoFederal": "Instrução, treinamento, orientação pedagógica e educacional, avaliação de conhecimentos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "8599605",
        "DescricaoServicoMunicipal": "Cursos preparatórios para concursos",
        "CodigoServicoFederal": "08.02",
        "DescricaoServicoFederal": "Instrução, treinamento, orientação pedagógica e educacional, avaliação de conhecimentos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "8599699",
        "DescricaoServicoMunicipal": "Outras atividades de ensino não especificadas anteriormente",
        "CodigoServicoFederal": "08.02",
        "DescricaoServicoFederal": "Instrução, treinamento, orientação pedagógica e educacional, avaliação de conhecimentos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "8599699",
        "DescricaoServicoMunicipal": "Outras atividades de ensino não especificadas anteriormente",
        "CodigoServicoFederal": "17.24",
        "DescricaoServicoFederal": "Apresentação de palestras, conferências, seminários e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8610101",
        "DescricaoServicoMunicipal": "Atividades de atendimento hospitalar, exceto pronto-socorro e unidades",
        "CodigoServicoFederal": "04.03",
        "DescricaoServicoFederal": "Hospitais, clínicas, laboratórios, sanatórios, manicômios, casas de saúde, prontos-socorros, ambulatórios e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8610102",
        "DescricaoServicoMunicipal": "Atividades de atendimento em pronto-socorro e unidades hospitalares pa",
        "CodigoServicoFederal": "04.03",
        "DescricaoServicoFederal": "Hospitais, clínicas, laboratórios, sanatórios, manicômios, casas de saúde, prontos-socorros, ambulatórios e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8621601",
        "DescricaoServicoMunicipal": "UTI móvel",
        "CodigoServicoFederal": "04.21",
        "DescricaoServicoFederal": "Unidade de atendimento, assistência ou tratamento móvel e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8621602",
        "DescricaoServicoMunicipal": "Serviços móveis de atendimento a urgências, exceto por UTI móvel",
        "CodigoServicoFederal": "04.21",
        "DescricaoServicoFederal": "Unidade de atendimento, assistência ou tratamento móvel e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8622400",
        "DescricaoServicoMunicipal": "Serviços de remoção de pacientes, exceto os serviços móveis de atendim",
        "CodigoServicoFederal": "04.21",
        "DescricaoServicoFederal": "Unidade de atendimento, assistência ou tratamento móvel e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8630501",
        "DescricaoServicoMunicipal": "Atividade médica ambulatorial com recursos para realização de procedim",
        "CodigoServicoFederal": "04.01",
        "DescricaoServicoFederal": "Medicina e biomedicina."
    },
    {
        "CodigoServicoMunicipal": "8630501",
        "DescricaoServicoMunicipal": "Atividade médica ambulatorial com recursos para realização de procedim",
        "CodigoServicoFederal": "04.03",
        "DescricaoServicoFederal": "Hospitais, clínicas, laboratórios, sanatórios, manicômios, casas de saúde, prontos-socorros, ambulatórios e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8630501",
        "DescricaoServicoMunicipal": "Atividade médica ambulatorial com recursos para realização de procedim",
        "CodigoServicoFederal": "04.04",
        "DescricaoServicoFederal": "Instrumentação cirúrgica."
    },
    {
        "CodigoServicoMunicipal": "8630502",
        "DescricaoServicoMunicipal": "Atividade médica ambulatorial com recursos para realização de exames c",
        "CodigoServicoFederal": "04.01",
        "DescricaoServicoFederal": "Medicina e biomedicina."
    },
    {
        "CodigoServicoMunicipal": "8630502",
        "DescricaoServicoMunicipal": "Atividade médica ambulatorial com recursos para realização de exames c",
        "CodigoServicoFederal": "04.03",
        "DescricaoServicoFederal": "Hospitais, clínicas, laboratórios, sanatórios, manicômios, casas de saúde, prontos-socorros, ambulatórios e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8630503",
        "DescricaoServicoMunicipal": "Atividade médica ambulatorial restrita a consultas",
        "CodigoServicoFederal": "04.01",
        "DescricaoServicoFederal": "Medicina e biomedicina."
    },
    {
        "CodigoServicoMunicipal": "8630504",
        "DescricaoServicoMunicipal": "Atividade odontológica",
        "CodigoServicoFederal": "04.12",
        "DescricaoServicoFederal": "Odontologia."
    },
    {
        "CodigoServicoMunicipal": "8630506",
        "DescricaoServicoMunicipal": "Serviços de vacinação e imunização humana",
        "CodigoServicoFederal": "04.03",
        "DescricaoServicoFederal": "Hospitais, clínicas, laboratórios, sanatórios, manicômios, casas de saúde, prontos-socorros, ambulatórios e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8630507",
        "DescricaoServicoMunicipal": "Atividades de reprodução humana assistida",
        "CodigoServicoFederal": "04.18",
        "DescricaoServicoFederal": "Inseminação artificial, fertilização in vitro e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8630507",
        "DescricaoServicoMunicipal": "Atividades de reprodução humana assistida",
        "CodigoServicoFederal": "04.19",
        "DescricaoServicoFederal": "Bancos de sangue, leite, pele, olhos, óvulos, sêmen e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8630599",
        "DescricaoServicoMunicipal": "Atividades de atenção ambulatorial não especificadas anteriormente",
        "CodigoServicoFederal": "04.01",
        "DescricaoServicoFederal": "Medicina e biomedicina."
    },
    {
        "CodigoServicoMunicipal": "8640201",
        "DescricaoServicoMunicipal": "Laboratórios de anatomia patológica e citológica",
        "CodigoServicoFederal": "04.02",
        "DescricaoServicoFederal": "Análises clínicas, patologia, eletricidade médica, radioterapia, quimioterapia, ultra-sonografia, ressonância magnética, radiologia, tomografia e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640201",
        "DescricaoServicoMunicipal": "Laboratórios de anatomia patológica e citológica",
        "CodigoServicoFederal": "04.03",
        "DescricaoServicoFederal": "Hospitais, clínicas, laboratórios, sanatórios, manicômios, casas de saúde, prontos-socorros, ambulatórios e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640202",
        "DescricaoServicoMunicipal": "Laboratórios clínicos",
        "CodigoServicoFederal": "04.02",
        "DescricaoServicoFederal": "Análises clínicas, patologia, eletricidade médica, radioterapia, quimioterapia, ultra-sonografia, ressonância magnética, radiologia, tomografia e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640202",
        "DescricaoServicoMunicipal": "Laboratórios clínicos",
        "CodigoServicoFederal": "04.03",
        "DescricaoServicoFederal": "Hospitais, clínicas, laboratórios, sanatórios, manicômios, casas de saúde, prontos-socorros, ambulatórios e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640202",
        "DescricaoServicoMunicipal": "Laboratórios clínicos",
        "CodigoServicoFederal": "04.20",
        "DescricaoServicoFederal": "Coleta de sangue, leite, tecidos, sêmen, órgãos e materiais biológicos de qualquer espécie."
    },
    {
        "CodigoServicoMunicipal": "8640202",
        "DescricaoServicoMunicipal": "Laboratórios clínicos",
        "CodigoServicoFederal": "30.01",
        "DescricaoServicoFederal": "Serviços de biologia, biotecnologia e química."
    },
    {
        "CodigoServicoMunicipal": "8640203",
        "DescricaoServicoMunicipal": "Serviços de diálise e nefrologia",
        "CodigoServicoFederal": "04.02",
        "DescricaoServicoFederal": "Análises clínicas, patologia, eletricidade médica, radioterapia, quimioterapia, ultra-sonografia, ressonância magnética, radiologia, tomografia e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640203",
        "DescricaoServicoMunicipal": "Serviços de diálise e nefrologia",
        "CodigoServicoFederal": "04.03",
        "DescricaoServicoFederal": "Hospitais, clínicas, laboratórios, sanatórios, manicômios, casas de saúde, prontos-socorros, ambulatórios e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640204",
        "DescricaoServicoMunicipal": "Serviços de tomografia",
        "CodigoServicoFederal": "04.02",
        "DescricaoServicoFederal": "Análises clínicas, patologia, eletricidade médica, radioterapia, quimioterapia, ultra-sonografia, ressonância magnética, radiologia, tomografia e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640204",
        "DescricaoServicoMunicipal": "Serviços de tomografia",
        "CodigoServicoFederal": "07.20",
        "DescricaoServicoFederal": "Aerofotogrametria (inclusive interpretação), cartografia, mapeamento, levantamentos topográficos, batimétricos, geográficos, geodésicos, geológicos, geofísicos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640205",
        "DescricaoServicoMunicipal": "Serviços de diagnóstico por imagem com uso de radiação ionizante, exce",
        "CodigoServicoFederal": "04.02",
        "DescricaoServicoFederal": "Análises clínicas, patologia, eletricidade médica, radioterapia, quimioterapia, ultra-sonografia, ressonância magnética, radiologia, tomografia e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640206",
        "DescricaoServicoMunicipal": "Serviços de ressonância magnética",
        "CodigoServicoFederal": "04.02",
        "DescricaoServicoFederal": "Análises clínicas, patologia, eletricidade médica, radioterapia, quimioterapia, ultra-sonografia, ressonância magnética, radiologia, tomografia e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640207",
        "DescricaoServicoMunicipal": "Serviços de diagnóstico por imagem sem uso de radiação ionizante, exce",
        "CodigoServicoFederal": "04.02",
        "DescricaoServicoFederal": "Análises clínicas, patologia, eletricidade médica, radioterapia, quimioterapia, ultra-sonografia, ressonância magnética, radiologia, tomografia e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640208",
        "DescricaoServicoMunicipal": "Serviços de diagnóstico por registro gráfico - ECG, EEG e outros exame",
        "CodigoServicoFederal": "04.02",
        "DescricaoServicoFederal": "Análises clínicas, patologia, eletricidade médica, radioterapia, quimioterapia, ultra-sonografia, ressonância magnética, radiologia, tomografia e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640209",
        "DescricaoServicoMunicipal": "Serviços de diagnóstico por métodos ópticos - endoscopia e outros exam",
        "CodigoServicoFederal": "04.02",
        "DescricaoServicoFederal": "Análises clínicas, patologia, eletricidade médica, radioterapia, quimioterapia, ultra-sonografia, ressonância magnética, radiologia, tomografia e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640210",
        "DescricaoServicoMunicipal": "Serviços de quimioterapia",
        "CodigoServicoFederal": "04.02",
        "DescricaoServicoFederal": "Análises clínicas, patologia, eletricidade médica, radioterapia, quimioterapia, ultra-sonografia, ressonância magnética, radiologia, tomografia e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640211",
        "DescricaoServicoMunicipal": "Serviços de radioterapia",
        "CodigoServicoFederal": "04.02",
        "DescricaoServicoFederal": "Análises clínicas, patologia, eletricidade médica, radioterapia, quimioterapia, ultra-sonografia, ressonância magnética, radiologia, tomografia e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640212",
        "DescricaoServicoMunicipal": "Serviços de hemoterapia",
        "CodigoServicoFederal": "04.09",
        "DescricaoServicoFederal": "Terapias de qualquer espécie destinadas ao tratamento físico, orgânico e mental."
    },
    {
        "CodigoServicoMunicipal": "8640212",
        "DescricaoServicoMunicipal": "Serviços de hemoterapia",
        "CodigoServicoFederal": "04.19",
        "DescricaoServicoFederal": "Bancos de sangue, leite, pele, olhos, óvulos, sêmen e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640213",
        "DescricaoServicoMunicipal": "Serviços de litotripsia",
        "CodigoServicoFederal": "04.03",
        "DescricaoServicoFederal": "Hospitais, clínicas, laboratórios, sanatórios, manicômios, casas de saúde, prontos-socorros, ambulatórios e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640214",
        "DescricaoServicoMunicipal": "Serviços de bancos de células e tecidos humanos",
        "CodigoServicoFederal": "04.19",
        "DescricaoServicoFederal": "Bancos de sangue, leite, pele, olhos, óvulos, sêmen e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8640299",
        "DescricaoServicoMunicipal": "Atividades de serviços de complementação diagnóstica e terapêutica não",
        "CodigoServicoFederal": "04.09",
        "DescricaoServicoFederal": "Terapias de qualquer espécie destinadas ao tratamento físico, orgânico e mental."
    },
    {
        "CodigoServicoMunicipal": "8650001",
        "DescricaoServicoMunicipal": "Atividades de enfermagem",
        "CodigoServicoFederal": "04.06",
        "DescricaoServicoFederal": "Enfermagem, inclusive serviços auxiliares."
    },
    {
        "CodigoServicoMunicipal": "8650002",
        "DescricaoServicoMunicipal": "Atividades de profissionais da nutrição",
        "CodigoServicoFederal": "04.10",
        "DescricaoServicoFederal": "Nutrição."
    },
    {
        "CodigoServicoMunicipal": "8650003",
        "DescricaoServicoMunicipal": "Atividades de psicologia e psicanálise",
        "CodigoServicoFederal": "04.15",
        "DescricaoServicoFederal": "Psicanálise."
    },
    {
        "CodigoServicoMunicipal": "8650003",
        "DescricaoServicoMunicipal": "Atividades de psicologia e psicanálise",
        "CodigoServicoFederal": "04.16",
        "DescricaoServicoFederal": "Psicologia."
    },
    {
        "CodigoServicoMunicipal": "8650004",
        "DescricaoServicoMunicipal": "Atividades de fisioterapia",
        "CodigoServicoFederal": "04.08",
        "DescricaoServicoFederal": "Terapia ocupacional, fisioterapia e fonoaudiologia."
    },
    {
        "CodigoServicoMunicipal": "8650005",
        "DescricaoServicoMunicipal": "Atividades de terapia ocupacional",
        "CodigoServicoFederal": "04.08",
        "DescricaoServicoFederal": "Terapia ocupacional, fisioterapia e fonoaudiologia."
    },
    {
        "CodigoServicoMunicipal": "8650006",
        "DescricaoServicoMunicipal": "Atividades de fonoaudiologia",
        "CodigoServicoFederal": "04.08",
        "DescricaoServicoFederal": "Terapia ocupacional, fisioterapia e fonoaudiologia."
    },
    {
        "CodigoServicoMunicipal": "8650007",
        "DescricaoServicoMunicipal": "Atividades de terapia de nutrição enteral e parenteral",
        "CodigoServicoFederal": "04.09",
        "DescricaoServicoFederal": "Terapias de qualquer espécie destinadas ao tratamento físico, orgânico e mental."
    },
    {
        "CodigoServicoMunicipal": "8650099",
        "DescricaoServicoMunicipal": "Atividades de profissionais da área de saúde não especificadas anterio",
        "CodigoServicoFederal": "04.04",
        "DescricaoServicoFederal": "Instrumentação cirúrgica."
    },
    {
        "CodigoServicoMunicipal": "8650099",
        "DescricaoServicoMunicipal": "Atividades de profissionais da área de saúde não especificadas anterio",
        "CodigoServicoFederal": "04.13",
        "DescricaoServicoFederal": "Ortóptica."
    },
    {
        "CodigoServicoMunicipal": "8660700",
        "DescricaoServicoMunicipal": "Atividades de apoio à gestão de saúde",
        "CodigoServicoFederal": "17.12",
        "DescricaoServicoFederal": "Administração em geral, inclusive de bens e negócios de terceiros."
    },
    {
        "CodigoServicoMunicipal": "8690901",
        "DescricaoServicoMunicipal": "Atividades de práticas integrativas e complementares em saúde humana",
        "CodigoServicoFederal": "04.05",
        "DescricaoServicoFederal": "Acupuntura."
    },
    {
        "CodigoServicoMunicipal": "8690901",
        "DescricaoServicoMunicipal": "Atividades de práticas integrativas e complementares em saúde humana",
        "CodigoServicoFederal": "04.09",
        "DescricaoServicoFederal": "Terapias de qualquer espécie destinadas ao tratamento físico, orgânico e mental."
    },
    {
        "CodigoServicoMunicipal": "8690902",
        "DescricaoServicoMunicipal": "Atividades de bancos de leite humano",
        "CodigoServicoFederal": "04.19",
        "DescricaoServicoFederal": "Bancos de sangue, leite, pele, olhos, óvulos, sêmen e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8690903",
        "DescricaoServicoMunicipal": "Atividades de acupuntura",
        "CodigoServicoFederal": "04.05",
        "DescricaoServicoFederal": "Acupuntura."
    },
    {
        "CodigoServicoMunicipal": "8690904",
        "DescricaoServicoMunicipal": "Atividades de podologia",
        "CodigoServicoFederal": "06.01",
        "DescricaoServicoFederal": "Barbearia, cabeleireiros, manicuros, pedicuros e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8690999",
        "DescricaoServicoMunicipal": "Outras atividades de atenção à saúde humana não especificadas anterior",
        "CodigoServicoFederal": "04.09",
        "DescricaoServicoFederal": "Terapias de qualquer espécie destinadas ao tratamento físico, orgânico e mental."
    },
    {
        "CodigoServicoMunicipal": "8690999",
        "DescricaoServicoMunicipal": "Outras atividades de atenção à saúde humana não especificadas anterior",
        "CodigoServicoFederal": "04.11",
        "DescricaoServicoFederal": "Obstetrícia."
    },
    {
        "CodigoServicoMunicipal": "8690999",
        "DescricaoServicoMunicipal": "Outras atividades de atenção à saúde humana não especificadas anterior",
        "CodigoServicoFederal": "04.19",
        "DescricaoServicoFederal": "Bancos de sangue, leite, pele, olhos, óvulos, sêmen e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8711501",
        "DescricaoServicoMunicipal": "Clínicas e residências geriátricas",
        "CodigoServicoFederal": "04.17",
        "DescricaoServicoFederal": "Casas de repouso e de recuperação, creches, asilos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8711502",
        "DescricaoServicoMunicipal": "Instituições de longa permanência para idosos",
        "CodigoServicoFederal": "04.17",
        "DescricaoServicoFederal": "Casas de repouso e de recuperação, creches, asilos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8711503",
        "DescricaoServicoMunicipal": "Atividades de assistência a deficientes físicos, imunodeprimidos e con",
        "CodigoServicoFederal": "04.17",
        "DescricaoServicoFederal": "Casas de repouso e de recuperação, creches, asilos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8711504",
        "DescricaoServicoMunicipal": "Centros de apoio a pacientes com câncer e com AIDS",
        "CodigoServicoFederal": "04.17",
        "DescricaoServicoFederal": "Casas de repouso e de recuperação, creches, asilos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8711505",
        "DescricaoServicoMunicipal": "Condomínios residenciais para idosos",
        "CodigoServicoFederal": "04.17",
        "DescricaoServicoFederal": "Casas de repouso e de recuperação, creches, asilos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8712300",
        "DescricaoServicoMunicipal": "Atividades de fornecimento de infra-estrutura de apoio e assistência a",
        "CodigoServicoFederal": "04.21",
        "DescricaoServicoFederal": "Unidade de atendimento, assistência ou tratamento móvel e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8720401",
        "DescricaoServicoMunicipal": "Atividades de centros de assistência psicossocial",
        "CodigoServicoFederal": "04.17",
        "DescricaoServicoFederal": "Casas de repouso e de recuperação, creches, asilos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8720499",
        "DescricaoServicoMunicipal": "Atividades de assistência psicossocial e à saúde a portadores de distú",
        "CodigoServicoFederal": "04.17",
        "DescricaoServicoFederal": "Casas de repouso e de recuperação, creches, asilos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8730101",
        "DescricaoServicoMunicipal": "Orfanatos",
        "CodigoServicoFederal": "04.17",
        "DescricaoServicoFederal": "Casas de repouso e de recuperação, creches, asilos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8730102",
        "DescricaoServicoMunicipal": "Albergues assistenciais",
        "CodigoServicoFederal": "04.17",
        "DescricaoServicoFederal": "Casas de repouso e de recuperação, creches, asilos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8730102",
        "DescricaoServicoMunicipal": "Albergues assistenciais",
        "CodigoServicoFederal": "09.01",
        "DescricaoServicoFederal": "Hospedagem de qualquer natureza em hotéis, apart-service condominiais, flat, apart-hotéis, hotéis residência, residence-service, suite service, hotelaria marítima, motéis, pensões e congêneres; ocupação por temporada com fornecimento de serviço (o valor da alimentação e gorjeta, quando incluído no preço da diária, fica sujeito ao Imposto Sobre Serviços)."
    },
    {
        "CodigoServicoMunicipal": "8730199",
        "DescricaoServicoMunicipal": "Atividades de assistência social prestadas em residências coletivas e ",
        "CodigoServicoFederal": "04.17",
        "DescricaoServicoFederal": "Casas de repouso e de recuperação, creches, asilos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "8800600",
        "DescricaoServicoMunicipal": "Serviços de assistência social sem alojamento",
        "CodigoServicoFederal": "27.01",
        "DescricaoServicoFederal": "Serviços de assistência social."
    },
    {
        "CodigoServicoMunicipal": "9001901",
        "DescricaoServicoMunicipal": "Produção teatral",
        "CodigoServicoFederal": "12.01",
        "DescricaoServicoFederal": "Espetáculos teatrais."
    },
    {
        "CodigoServicoMunicipal": "9001901",
        "DescricaoServicoMunicipal": "Produção teatral",
        "CodigoServicoFederal": "12.13",
        "DescricaoServicoFederal": "Produção, mediante ou sem encomenda prévia, de eventos, espetáculos, entrevistas, shows, ballet, danças, desfiles, bailes, teatros, óperas, concertos, recitais, festivais e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9001902",
        "DescricaoServicoMunicipal": "Produção musical",
        "CodigoServicoFederal": "12.07",
        "DescricaoServicoFederal": "Shows, ballet, danças, desfiles, bailes, óperas, concertos, recitais, festivais e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9001902",
        "DescricaoServicoMunicipal": "Produção musical",
        "CodigoServicoFederal": "12.12",
        "DescricaoServicoFederal": "Execução de música."
    },
    {
        "CodigoServicoMunicipal": "9001902",
        "DescricaoServicoMunicipal": "Produção musical",
        "CodigoServicoFederal": "12.13",
        "DescricaoServicoFederal": "Produção, mediante ou sem encomenda prévia, de eventos, espetáculos, entrevistas, shows, ballet, danças, desfiles, bailes, teatros, óperas, concertos, recitais, festivais e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9001902",
        "DescricaoServicoMunicipal": "Produção musical",
        "CodigoServicoFederal": "12.14",
        "DescricaoServicoFederal": "Fornecimento de música para ambientes fechados ou não, mediante transmissão por qualquer processo."
    },
    {
        "CodigoServicoMunicipal": "9001902",
        "DescricaoServicoMunicipal": "Produção musical",
        "CodigoServicoFederal": "12.15",
        "DescricaoServicoFederal": "Desfiles de blocos carnavalescos ou folclóricos, trios elétricos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9001902",
        "DescricaoServicoMunicipal": "Produção musical",
        "CodigoServicoFederal": "12.16",
        "DescricaoServicoFederal": "Exibição de filmes, entrevistas, musicais, espetáculos, shows, concertos, desfiles, óperas, competições esportivas, de destreza intelectual ou congêneres."
    },
    {
        "CodigoServicoMunicipal": "9001903",
        "DescricaoServicoMunicipal": "Produção de espetáculos de dança",
        "CodigoServicoFederal": "12.07",
        "DescricaoServicoFederal": "Shows, ballet, danças, desfiles, bailes, óperas, concertos, recitais, festivais e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9001903",
        "DescricaoServicoMunicipal": "Produção de espetáculos de dança",
        "CodigoServicoFederal": "12.13",
        "DescricaoServicoFederal": "Produção, mediante ou sem encomenda prévia, de eventos, espetáculos, entrevistas, shows, ballet, danças, desfiles, bailes, teatros, óperas, concertos, recitais, festivais e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9001903",
        "DescricaoServicoMunicipal": "Produção de espetáculos de dança",
        "CodigoServicoFederal": "12.15",
        "DescricaoServicoFederal": "Desfiles de blocos carnavalescos ou folclóricos, trios elétricos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9001904",
        "DescricaoServicoMunicipal": "Produção de espetáculos circenses, de marionetes e similares",
        "CodigoServicoFederal": "12.03",
        "DescricaoServicoFederal": "Espetáculos circenses."
    },
    {
        "CodigoServicoMunicipal": "9001904",
        "DescricaoServicoMunicipal": "Produção de espetáculos circenses, de marionetes e similares",
        "CodigoServicoFederal": "12.13",
        "DescricaoServicoFederal": "Produção, mediante ou sem encomenda prévia, de eventos, espetáculos, entrevistas, shows, ballet, danças, desfiles, bailes, teatros, óperas, concertos, recitais, festivais e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9001905",
        "DescricaoServicoMunicipal": "Produção de espetáculos de rodeios, vaquejadas e similares",
        "CodigoServicoFederal": "12.10",
        "DescricaoServicoFederal": "Corridas e competições de animais."
    },
    {
        "CodigoServicoMunicipal": "9001906",
        "DescricaoServicoMunicipal": "Atividades de sonorização e de iluminação",
        "CodigoServicoFederal": "12.14",
        "DescricaoServicoFederal": "Fornecimento de música para ambientes fechados ou não, mediante transmissão por qualquer processo."
    },
    {
        "CodigoServicoMunicipal": "9001999",
        "DescricaoServicoMunicipal": "Artes cênicas, espetáculos e atividades complementares não especificad",
        "CodigoServicoFederal": "12.01",
        "DescricaoServicoFederal": "Espetáculos teatrais."
    },
    {
        "CodigoServicoMunicipal": "9001999",
        "DescricaoServicoMunicipal": "Artes cênicas, espetáculos e atividades complementares não especificad",
        "CodigoServicoFederal": "12.03",
        "DescricaoServicoFederal": "Espetáculos circenses."
    },
    {
        "CodigoServicoMunicipal": "9001999",
        "DescricaoServicoMunicipal": "Artes cênicas, espetáculos e atividades complementares não especificad",
        "CodigoServicoFederal": "12.04",
        "DescricaoServicoFederal": "Programas de auditório."
    },
    {
        "CodigoServicoMunicipal": "9001999",
        "DescricaoServicoMunicipal": "Artes cênicas, espetáculos e atividades complementares não especificad",
        "CodigoServicoFederal": "12.05",
        "DescricaoServicoFederal": "Parques de diversões, centros de lazer e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9001999",
        "DescricaoServicoMunicipal": "Artes cênicas, espetáculos e atividades complementares não especificad",
        "CodigoServicoFederal": "35.01",
        "DescricaoServicoFederal": "Serviços de reportagem, assessoria de imprensa, jornalismo e relações públicas."
    },
    {
        "CodigoServicoMunicipal": "9002701",
        "DescricaoServicoMunicipal": "Atividades de artistas plásticos, jornalistas independentes e escritor",
        "CodigoServicoFederal": "40.01",
        "DescricaoServicoFederal": "Obras de arte sob encomenda."
    },
    {
        "CodigoServicoMunicipal": "9002702",
        "DescricaoServicoMunicipal": "Restauração de obras de arte",
        "CodigoServicoFederal": "14.05",
        "DescricaoServicoFederal": "Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "9003500",
        "DescricaoServicoMunicipal": "Gestão de espaços para artes cênicas, espetáculos e outras atividades ",
        "CodigoServicoFederal": "03.03",
        "DescricaoServicoFederal": "Exploração de salões de festas, centro de convenções, escritórios virtuais, stands, quadras esportivas, estádios, ginásios, auditórios, casas de espetáculos, parques de diversões, canchas e congêneres, para realização de eventos ou negócios de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "9101500",
        "DescricaoServicoMunicipal": "Atividades de bibliotecas e arquivos",
        "CodigoServicoFederal": "29.01",
        "DescricaoServicoFederal": "Serviços de biblioteconomia."
    },
    {
        "CodigoServicoMunicipal": "9102301",
        "DescricaoServicoMunicipal": "Atividades de museus e de exploração de lugares e prédios históricos e",
        "CodigoServicoFederal": "38.01",
        "DescricaoServicoFederal": "Serviços de museologia."
    },
    {
        "CodigoServicoMunicipal": "9102302",
        "DescricaoServicoMunicipal": "Restauração e conservação de lugares e prédios históricos",
        "CodigoServicoFederal": "07.05",
        "DescricaoServicoFederal": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "9103100",
        "DescricaoServicoMunicipal": "Atividades de jardins botânicos, zoológicos, parques nacionais, reserv",
        "CodigoServicoFederal": "07.11",
        "DescricaoServicoFederal": "Decoração e jardinagem, inclusive corte e poda de árvores."
    },
    {
        "CodigoServicoMunicipal": "9103100",
        "DescricaoServicoMunicipal": "Atividades de jardins botânicos, zoológicos, parques nacionais, reserv",
        "CodigoServicoFederal": "12.05",
        "DescricaoServicoFederal": "Parques de diversões, centros de lazer e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9200301",
        "DescricaoServicoMunicipal": "Casas de bingo",
        "CodigoServicoFederal": "19.01",
        "DescricaoServicoFederal": "Serviços de distribuição e venda de bilhetes e demais produtos de loteria, bingos, cartões, pules ou cupons de apostas, sorteios, prêmios, inclusive os decorrentes de títulos de capitalização e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9200302",
        "DescricaoServicoMunicipal": "Exploração de apostas em corridas de cavalos",
        "CodigoServicoFederal": "12.10",
        "DescricaoServicoFederal": "Corridas e competições de animais."
    },
    {
        "CodigoServicoMunicipal": "9200399",
        "DescricaoServicoMunicipal": "Exploração de jogos de azar e apostas não especificados anteriormente",
        "CodigoServicoFederal": "12.09",
        "DescricaoServicoFederal": "Bilhares, boliches e diversões eletrônicas ou não."
    },
    {
        "CodigoServicoMunicipal": "9200399",
        "DescricaoServicoMunicipal": "Exploração de jogos de azar e apostas não especificados anteriormente",
        "CodigoServicoFederal": "19.01",
        "DescricaoServicoFederal": "Serviços de distribuição e venda de bilhetes e demais produtos de loteria, bingos, cartões, pules ou cupons de apostas, sorteios, prêmios, inclusive os decorrentes de títulos de capitalização e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9311500",
        "DescricaoServicoMunicipal": "Gestão de instalações de esportes",
        "CodigoServicoFederal": "03.03",
        "DescricaoServicoFederal": "Exploração de salões de festas, centro de convenções, escritórios virtuais, stands, quadras esportivas, estádios, ginásios, auditórios, casas de espetáculos, parques de diversões, canchas e congêneres, para realização de eventos ou negócios de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "9312300",
        "DescricaoServicoMunicipal": "Clubes sociais, esportivos e similares",
        "CodigoServicoFederal": "08.02",
        "DescricaoServicoFederal": "Instrução, treinamento, orientação pedagógica e educacional, avaliação de conhecimentos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "9313100",
        "DescricaoServicoMunicipal": "Atividades de condicionamento físico",
        "CodigoServicoFederal": "06.04",
        "DescricaoServicoFederal": "Ginástica, dança, esportes, natação, artes marciais e demais atividades físicas."
    },
    {
        "CodigoServicoMunicipal": "9319101",
        "DescricaoServicoMunicipal": "Produção e promoção de eventos esportivos",
        "CodigoServicoFederal": "12.11",
        "DescricaoServicoFederal": "Competições esportivas ou de destreza física ou intelectual, com ou sem a participação do espectador."
    },
    {
        "CodigoServicoMunicipal": "9319199",
        "DescricaoServicoMunicipal": "Atividades de profissionais que atuam por conta própria em atividades ",
        "CodigoServicoFederal": "12.11",
        "DescricaoServicoFederal": "Competições esportivas ou de destreza física ou intelectual, com ou sem a participação do espectador."
    },
    {
        "CodigoServicoMunicipal": "9321200",
        "DescricaoServicoMunicipal": "Parques de diversão e parques temáticos",
        "CodigoServicoFederal": "12.05",
        "DescricaoServicoFederal": "Parques de diversões, centros de lazer e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9329801",
        "DescricaoServicoMunicipal": "Discotecas, danceterias, salões de dança e similares",
        "CodigoServicoFederal": "12.06",
        "DescricaoServicoFederal": "Boates, taxi-dancing e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9329802",
        "DescricaoServicoMunicipal": "Exploração de boliches",
        "CodigoServicoFederal": "12.09",
        "DescricaoServicoFederal": "Bilhares, boliches e diversões eletrônicas ou não."
    },
    {
        "CodigoServicoMunicipal": "9329803",
        "DescricaoServicoMunicipal": "Exploração de jogos de sinuca, bilhar e similares",
        "CodigoServicoFederal": "12.09",
        "DescricaoServicoFederal": "Bilhares, boliches e diversões eletrônicas ou não."
    },
    {
        "CodigoServicoMunicipal": "9329804",
        "DescricaoServicoMunicipal": "Exploração de jogos eletrônicos recreativos",
        "CodigoServicoFederal": "12.09",
        "DescricaoServicoFederal": "Bilhares, boliches e diversões eletrônicas ou não."
    },
    {
        "CodigoServicoMunicipal": "9329899",
        "DescricaoServicoMunicipal": "OUTRAS ATIVIDADES DE RECREAÇÃO E LAZER NÃO ESPECIFICADAS ANTERIORMENTE",
        "CodigoServicoFederal": "09.02",
        "DescricaoServicoFederal": "Agenciamento, organização, promoção, intermediação e execução de programas de turismo, passeios, viagens, excursões, hospedagens e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9329899",
        "DescricaoServicoMunicipal": "OUTRAS ATIVIDADES DE RECREAÇÃO E LAZER NÃO ESPECIFICADAS ANTERIORMENTE",
        "CodigoServicoFederal": "12.17",
        "DescricaoServicoFederal": "Recreação e animação, inclusive em festas e eventos de qualquer natureza."
    },
    {
        "CodigoServicoMunicipal": "9430800",
        "DescricaoServicoMunicipal": "Atividades de associações de defesa de direitos sociais",
        "CodigoServicoFederal": "17.01",
        "DescricaoServicoFederal": "Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista; análise, exame, pesquisa, coleta, compilação e fornecimento de dados e informações de qualquer natureza, inclusive cadastro e similares."
    },
    {
        "CodigoServicoMunicipal": "9493600",
        "DescricaoServicoMunicipal": "Atividades de organizações associativas ligadas à cultura e à arte",
        "CodigoServicoFederal": "12.15",
        "DescricaoServicoFederal": "Desfiles de blocos carnavalescos ou folclóricos, trios elétricos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9511800",
        "DescricaoServicoMunicipal": "Reparação e manutenção de computadores e de equipamentos periféricos",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "9511800",
        "DescricaoServicoMunicipal": "Reparação e manutenção de computadores e de equipamentos periféricos",
        "CodigoServicoFederal": "14.02",
        "DescricaoServicoFederal": "Assistência técnica."
    },
    {
        "CodigoServicoMunicipal": "9511800",
        "DescricaoServicoMunicipal": "Reparação e manutenção de computadores e de equipamentos periféricos",
        "CodigoServicoFederal": "14.06",
        "DescricaoServicoFederal": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido."
    },
    {
        "CodigoServicoMunicipal": "9512600",
        "DescricaoServicoMunicipal": "Reparação e manutenção de equipamentos de comunicação",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "9512600",
        "DescricaoServicoMunicipal": "Reparação e manutenção de equipamentos de comunicação",
        "CodigoServicoFederal": "14.02",
        "DescricaoServicoFederal": "Assistência técnica."
    },
    {
        "CodigoServicoMunicipal": "9521500",
        "DescricaoServicoMunicipal": "Reparação e manutenção de equipamentos eletroeletrônicos de uso pessoa",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "9529101",
        "DescricaoServicoMunicipal": "Reparação de calçados, bolsas e artigos de viagem",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "9529102",
        "DescricaoServicoMunicipal": "Chaveiros",
        "CodigoServicoFederal": "24.01",
        "DescricaoServicoFederal": "Serviços de chaveiros, confecção de carimbos, placas, sinalização visual, banners, adesivos e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9529103",
        "DescricaoServicoMunicipal": "Reparação de relógios",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "9529104",
        "DescricaoServicoMunicipal": "Reparação de bicicletas, triciclos e outros veículos não-motorizados",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "9529105",
        "DescricaoServicoMunicipal": "Reparação de artigos do mobiliário",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "9529105",
        "DescricaoServicoMunicipal": "Reparação de artigos do mobiliário",
        "CodigoServicoFederal": "14.05",
        "DescricaoServicoFederal": "Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "9529105",
        "DescricaoServicoMunicipal": "Reparação de artigos do mobiliário",
        "CodigoServicoFederal": "14.11",
        "DescricaoServicoFederal": "Tapeçaria e reforma de estofamentos em geral."
    },
    {
        "CodigoServicoMunicipal": "9529106",
        "DescricaoServicoMunicipal": "Reparação de jóias",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "9529199",
        "DescricaoServicoMunicipal": "Reparação e manutenção de outros objetos e equipamentos pessoais e dom",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "9529199",
        "DescricaoServicoMunicipal": "Reparação e manutenção de outros objetos e equipamentos pessoais e dom",
        "CodigoServicoFederal": "14.09",
        "DescricaoServicoFederal": "Alfaiataria e costura, quando o material for fornecido pelo usuário final, exceto aviamento."
    },
    {
        "CodigoServicoMunicipal": "9601701",
        "DescricaoServicoMunicipal": "Lavanderias",
        "CodigoServicoFederal": "14.10",
        "DescricaoServicoFederal": "Tinturaria e lavanderia."
    },
    {
        "CodigoServicoMunicipal": "9601702",
        "DescricaoServicoMunicipal": "Tinturarias",
        "CodigoServicoFederal": "14.10",
        "DescricaoServicoFederal": "Tinturaria e lavanderia."
    },
    {
        "CodigoServicoMunicipal": "9601703",
        "DescricaoServicoMunicipal": "Toalheiros",
        "CodigoServicoFederal": "07.10",
        "DescricaoServicoFederal": "Limpeza, manutenção e conservação de vias e logradouros públicos, imóveis, chaminés, piscinas, parques, jardins e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9601703",
        "DescricaoServicoMunicipal": "Toalheiros",
        "CodigoServicoFederal": "14.10",
        "DescricaoServicoFederal": "Tinturaria e lavanderia."
    },
    {
        "CodigoServicoMunicipal": "9602501",
        "DescricaoServicoMunicipal": "Cabeleireiros",
        "CodigoServicoFederal": "06.01",
        "DescricaoServicoFederal": "Barbearia, cabeleireiros, manicuros, pedicuros e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9602502",
        "DescricaoServicoMunicipal": "Atividades de estética e outros serviços de cuidados com a beleza",
        "CodigoServicoFederal": "06.01",
        "DescricaoServicoFederal": "Barbearia, cabeleireiros, manicuros, pedicuros e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9602502",
        "DescricaoServicoMunicipal": "Atividades de estética e outros serviços de cuidados com a beleza",
        "CodigoServicoFederal": "06.02",
        "DescricaoServicoFederal": "Esteticistas, tratamento de pele, depilação e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9603301",
        "DescricaoServicoMunicipal": "Gestão e manutenção de cemitérios",
        "CodigoServicoFederal": "25.04",
        "DescricaoServicoFederal": "Manutenção e conservação de jazigos e cemitérios."
    },
    {
        "CodigoServicoMunicipal": "9603301",
        "DescricaoServicoMunicipal": "Gestão e manutenção de cemitérios",
        "CodigoServicoFederal": "25.05",
        "DescricaoServicoFederal": "Cessão de uso de espaços em cemitérios para sepultamento."
    },
    {
        "CodigoServicoMunicipal": "9603302",
        "DescricaoServicoMunicipal": "Serviços de cremação",
        "CodigoServicoFederal": "25.02",
        "DescricaoServicoFederal": "Translado intramunicipal e cremação de corpos e partes de corpos cadavéricos."
    },
    {
        "CodigoServicoMunicipal": "9603303",
        "DescricaoServicoMunicipal": "Serviços de sepultamento",
        "CodigoServicoFederal": "25.01",
        "DescricaoServicoFederal": "Funerais, inclusive fornecimento de caixão, urna ou esquifes; aluguel de capela; transporte do corpo cadavérico; fornecimento de flores, coroas e outros paramentos; desembaraço de certidão de óbito; fornecimento de véu, essa e outros adornos; embalsamento, embelezamento, conservação ou restauração de cadáveres."
    },
    {
        "CodigoServicoMunicipal": "9603304",
        "DescricaoServicoMunicipal": "Serviços de funerárias",
        "CodigoServicoFederal": "25.01",
        "DescricaoServicoFederal": "Funerais, inclusive fornecimento de caixão, urna ou esquifes; aluguel de capela; transporte do corpo cadavérico; fornecimento de flores, coroas e outros paramentos; desembaraço de certidão de óbito; fornecimento de véu, essa e outros adornos; embalsamento, embelezamento, conservação ou restauração de cadáveres."
    },
    {
        "CodigoServicoMunicipal": "9603305",
        "DescricaoServicoMunicipal": "Serviços de somatoconservação",
        "CodigoServicoFederal": "25.01",
        "DescricaoServicoFederal": "Funerais, inclusive fornecimento de caixão, urna ou esquifes; aluguel de capela; transporte do corpo cadavérico; fornecimento de flores, coroas e outros paramentos; desembaraço de certidão de óbito; fornecimento de véu, essa e outros adornos; embalsamento, embelezamento, conservação ou restauração de cadáveres."
    },
    {
        "CodigoServicoMunicipal": "9603399",
        "DescricaoServicoMunicipal": "Atividades funerárias e serviços relacionados não especificados anteri",
        "CodigoServicoFederal": "25.01",
        "DescricaoServicoFederal": "Funerais, inclusive fornecimento de caixão, urna ou esquifes; aluguel de capela; transporte do corpo cadavérico; fornecimento de flores, coroas e outros paramentos; desembaraço de certidão de óbito; fornecimento de véu, essa e outros adornos; embalsamento, embelezamento, conservação ou restauração de cadáveres."
    },
    {
        "CodigoServicoMunicipal": "9609202",
        "DescricaoServicoMunicipal": "Agências matrimoniais",
        "CodigoServicoFederal": "10.05",
        "DescricaoServicoFederal": "Agenciamento, corretagem ou intermediação de bens móveis ou imóveis, não abrangidos em outros itens ou subitens, inclusive aqueles realizados no âmbito de Bolsas de Mercadorias e Futuros, por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "9609203",
        "DescricaoServicoMunicipal": "Alojamento, higiene e embelezamento de animais",
        "CodigoServicoFederal": "05.08",
        "DescricaoServicoFederal": "Guarda, tratamento, amestramento, embelezamento, alojamento e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9609204",
        "DescricaoServicoMunicipal": "Exploração de máquinas de serviços pessoais acionadas por moeda",
        "CodigoServicoFederal": "13.03",
        "DescricaoServicoFederal": "Fotografia e cinematografia, inclusive revelação, ampliação, cópia, reprodução, trucagem e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9609205",
        "DescricaoServicoMunicipal": "Atividades de sauna e banhos",
        "CodigoServicoFederal": "06.03",
        "DescricaoServicoFederal": "Banhos, duchas, sauna, massagens e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9609206",
        "DescricaoServicoMunicipal": "Serviços de tatuagem e colocação de piercing",
        "CodigoServicoFederal": "06.06",
        "DescricaoServicoFederal": "Aplicação de tatuagens, piercings e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9609208",
        "DescricaoServicoMunicipal": "Higiene e embelezamento de animais domésticos",
        "CodigoServicoFederal": "05.08",
        "DescricaoServicoFederal": "Guarda, tratamento, amestramento, embelezamento, alojamento e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9609299",
        "DescricaoServicoMunicipal": "Outras atividades de serviços pessoais não especificadas anteriormente",
        "CodigoServicoFederal": "06.02",
        "DescricaoServicoFederal": "Esteticistas, tratamento de pele, depilação e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9609299",
        "DescricaoServicoMunicipal": "Outras atividades de serviços pessoais não especificadas anteriormente",
        "CodigoServicoFederal": "07.10",
        "DescricaoServicoFederal": "Limpeza, manutenção e conservação de vias e logradouros públicos, imóveis, chaminés, piscinas, parques, jardins e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9609299",
        "DescricaoServicoMunicipal": "Outras atividades de serviços pessoais não especificadas anteriormente",
        "CodigoServicoFederal": "07.13",
        "DescricaoServicoFederal": "Dedetização, desinfecção, desinsetização, imunização, higienização, desratização, pulverização e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9609299",
        "DescricaoServicoMunicipal": "Outras atividades de serviços pessoais não especificadas anteriormente",
        "CodigoServicoFederal": "07.16",
        "DescricaoServicoFederal": "Florestamento, reflorestamento, semeadura, adubação, reparação de solo, plantio, silagem, colheita, corte e descascamento de árvores, silvicultura, exploração florestal e dos serviços congêneres indissociáveis da formação, manutenção e colheita de florestas, para quaisquer fins e por quaisquer meios."
    },
    {
        "CodigoServicoMunicipal": "9609299",
        "DescricaoServicoMunicipal": "Outras atividades de serviços pessoais não especificadas anteriormente",
        "CodigoServicoFederal": "11.04",
        "DescricaoServicoFederal": "Armazenamento, depósito, carga, descarga, arrumação e guarda de bens de qualquer espécie."
    },
    {
        "CodigoServicoMunicipal": "9609299",
        "DescricaoServicoMunicipal": "Outras atividades de serviços pessoais não especificadas anteriormente",
        "CodigoServicoFederal": "14.01",
        "DescricaoServicoFederal": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS)."
    },
    {
        "CodigoServicoMunicipal": "9609299",
        "DescricaoServicoMunicipal": "Outras atividades de serviços pessoais não especificadas anteriormente",
        "CodigoServicoFederal": "14.05",
        "DescricaoServicoFederal": "Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer."
    },
    {
        "CodigoServicoMunicipal": "9609299",
        "DescricaoServicoMunicipal": "Outras atividades de serviços pessoais não especificadas anteriormente",
        "CodigoServicoFederal": "17.01",
        "DescricaoServicoFederal": "Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista; análise, exame, pesquisa, coleta, compilação e fornecimento de dados e informações de qualquer natureza, inclusive cadastro e similares."
    },
    {
        "CodigoServicoMunicipal": "9609299",
        "DescricaoServicoMunicipal": "Outras atividades de serviços pessoais não especificadas anteriormente",
        "CodigoServicoFederal": "17.12",
        "DescricaoServicoFederal": "Administração em geral, inclusive de bens e negócios de terceiros."
    },
    {
        "CodigoServicoMunicipal": "9700500",
        "DescricaoServicoMunicipal": "Serviços domésticos",
        "CodigoServicoFederal": "07.10",
        "DescricaoServicoFederal": "Limpeza, manutenção e conservação de vias e logradouros públicos, imóveis, chaminés, piscinas, parques, jardins e congêneres."
    },
    {
        "CodigoServicoMunicipal": "9700500",
        "DescricaoServicoMunicipal": "Serviços domésticos",
        "CodigoServicoFederal": "07.11",
        "DescricaoServicoFederal": "Decoração e jardinagem, inclusive corte e poda de árvores."
    },
    {
        "CodigoServicoMunicipal": "9999999",
        "DescricaoServicoMunicipal": "OUTRAS ATIVIDADES DE SERVIÇOS",
        "CodigoServicoFederal": "99.99",
        "DescricaoServicoFederal": "Outros serviços"
    }
]

dicionario = {
  "01.01": {
    "descricao": "Análise e desenvolvimento de sistemas.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "01.02": {
    "descricao": "Programação.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "01.03": {
    "descricao": "Processamento, armazenamento ou hospedagem de dados, textos, imagens, vídeos, páginas eletrônicas, aplicativos e sistemas de informação, entre outros formatos, e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "01.04": {
    "descricao": "Elaboração de programas de computadores, inclusive de jogos eletrônicos, independentemente da arquitetura construtiva da máquina em que o programa será executado, incluindo tablets, smartphones e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "01.05": {
    "descricao": "Licenciamento ou cessão de direito de uso de programas de computação.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "01.06": {
    "descricao": "Assessoria e consultoria em informática.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "01.07": {
    "descricao": "Suporte técnico em informática, inclusive instalação, configuração e manutenção de programas de computação e bancos de dados.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "01.08": {
    "descricao": "Planejamento, confecção, manutenção e atualização de páginas eletrônicas.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "01.09": {
    "descricao": "Disponibilização, sem cessão definitiva, de conteúdos de áudio, vídeo, imagem e texto por meio da internet, respeitada a imunidade de livros, jornais e periódicos (exceto a distribuição de conteúdos pelas prestadoras de Serviço de Acesso Condicionado, de que trata a Lei no 12.485, de 12 de setembro de 2011, sujeita ao ICMS).",
    "aliquota": "3,00",
    "servicos": [],
  },
  "02.01": {
    "descricao": "Serviços de pesquisas e desenvolvimento de qualquer natureza.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "03.02": {
    "descricao": "Cessão de direito de uso de marcas e de sinais de propaganda.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "03.03": {
    "descricao": "Exploração de salões de festas, centro de convenções, escritórios virtuais, stands, quadras esportivas, estádios, ginásios, auditórios, casas de espetáculos, parques de diversões, canchas e congêneres, para realização de eventos ou negócios de qualquer natureza.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "03.04": {
    "descricao": "Locação, sublocação, arrendamento, direito de passagem ou permissão de uso, compartilhado ou não, de ferrovia, rodovia, postes, cabos, dutos e condutos de qualquer natureza.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "03.05": {
    "descricao": "Cessão de andaimes, palcos, coberturas e outras estruturas de uso temporário.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "04.01": {
    "descricao": "Medicina e biomedicina.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "04.02": {
    "descricao": "Análises clínicas, patologia, eletricidade médica, radioterapia, quimioterapia, ultra-sonografia, ressonância magnética, radiologia, tomografia e congêneres.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "04.03": {
    "descricao": "Hospitais, clínicas, laboratórios, sanatórios, manicômios, casas de saúde, prontos-socorros, ambulatórios e congêneres.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "04.04": {
    "descricao": "Instrumentação cirúrgica.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "04.05": {
    "descricao": "Acupuntura.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "04.06": {
    "descricao": "Enfermagem, inclusive serviços auxiliares.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "04.07": {
    "descricao": "Serviços farmacêuticos.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "04.08": {
    "descricao": "Terapia ocupacional, fisioterapia e fonoaudiologia.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "04.09": {
    "descricao": "Terapias de qualquer espécie destinadas ao tratamento físico, orgânico e mental.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "04.10": {
    "descricao": "Nutrição.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "04.11": {
    "descricao": "Obstetrícia.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "04.12": {
    "descricao": "Odontologia.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "04.13": {
    "descricao": "Ortóptica.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "04.14": {
    "descricao": "Próteses sob encomenda.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "04.15": {
    "descricao": "Psicanálise.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "04.16": {
    "descricao": "Psicologia.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "04.17": {
    "descricao": "Casas de repouso e de recuperação, creches, asilos e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "04.18": {
    "descricao": "Inseminação artificial, fertilização in vitro e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "04.19": {
    "descricao": "Bancos de sangue, leite, pele, olhos, óvulos, sêmen e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "04.20": {
    "descricao": "Coleta de sangue, leite, tecidos, sêmen, órgãos e materiais biológicos de qualquer espécie.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "04.21": {
    "descricao": "Unidade de atendimento, assistência ou tratamento móvel e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "04.22": {
    "descricao": "Planos de medicina de grupo ou individual e convênios para prestação de assistência médica, hospitalar, odontológica e congêneres.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "04.23": {
    "descricao": "Outros planos de saúde que se cumpram através de serviços de terceiros contratados, credenciados, cooperados ou apenas pagos pelo operador do plano mediante indicação do beneficiário.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "05.01": {
    "descricao": "Medicina veterinária e zootecnia.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "05.02": {
    "descricao": "Hospitais, clínicas, ambulatórios, prontos-socorros e congêneres, na área veterinária.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "05.03": {
    "descricao": "Laboratórios de análise na área veterinária.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "05.04": {
    "descricao": "Inseminação artificial, fertilização in vitro e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "05.05": {
    "descricao": "Bancos de sangue e de órgãos e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "05.06": {
    "descricao": "Coleta de sangue, leite, tecidos, sêmen, órgãos e materiais biológicos de qualquer espécie.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "05.07": {
    "descricao": "Unidade de atendimento, assistência ou tratamento móvel e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "05.08": {
    "descricao": "Guarda, tratamento, amestramento, embelezamento, alojamento e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "05.09": {
    "descricao": "Planos de atendimento e assistência médico-veterinária.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "06.01": {
    "descricao": "Barbearia, cabeleireiros, manicuros, pedicuros e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "06.02": {
    "descricao": "Esteticistas, tratamento de pele, depilação e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "06.03": {
    "descricao": "Banhos, duchas, sauna, massagens e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "06.04": {
    "descricao": "Ginástica, dança, esportes, natação, artes marciais e demais atividades físicas.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "06.05": {
    "descricao": "Centros de emagrecimento, spa e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "06.06": {
    "descricao": "Aplicação de tatuagens, piercings e congêneres. (Incluído pela Lei Complementar nº 157, de 2016)",
    "aliquota": "3,00",
    "servicos": [],
  },
  "07.01": {
    "descricao": "Engenharia, agronomia, agrimensura, arquitetura, geologia, urbanismo, paisagismo e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "07.02": {
    "descricao": "Execução, por administração, empreitada ou subempreitada, de obras de construção civil, hidráulica ou elétrica e de outras obras semelhantes, inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação, terraplanagem, pavimentação, concretagem e a instalação e montagem de produtos, peças e equipamentos (exceto o fornecimento de mercadorias produzidas pelo prestador de serviços fora do local da prestação dos serviços, que fica sujeito ao ICMS).",
    "aliquota": "5,00",
    "servicos": [],
  },
  "07.03": {
    "descricao": "Elaboração de planos diretores, estudos de viabilidade, estudos organizacionais e outros, relacionados com obras e serviços de engenharia; elaboração de anteprojetos, projetos básicos e projetos executivos para trabalhos de engenharia.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "07.04": {
    "descricao": "Demolição.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "07.05": {
    "descricao": "Reparação, conservação e reforma de edifícios, estradas, pontes, portos e congêneres (exceto o fornecimento de mercadorias produzidas pelo prestador dos serviços, fora do local da prestação dos serviços, que fica sujeito ao ICMS).",
    "aliquota": "5,00",
    "servicos": [],
  },
  "07.06": {
    "descricao": "Colocação e instalação de tapetes, carpetes, assoalhos, cortinas, revestimentos de parede, vidros, divisórias, placas de gesso e congêneres, com material fornecido pelo tomador do serviço.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "07.07": {
    "descricao": "Recuperação, raspagem, polimento e lustração de pisos e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "07.08": {
    "descricao": "Calafetação.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "07.09": {
    "descricao": "Varrição, coleta, remoção, incineração, tratamento, reciclagem, separação e destinação final de lixo, rejeitos e outros resíduos quaisquer.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "07.10": {
    "descricao": "Limpeza, manutenção e conservação de vias e logradouros públicos, imóveis, chaminés, piscinas, parques, jardins e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "07.11": {
    "descricao": "Decoração e jardinagem, inclusive corte e poda de árvores.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "07.12": {
    "descricao": "Controle e tratamento de efluentes de qualquer natureza e de agentes físicos, químicos e biológicos.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "07.13": {
    "descricao": "Dedetização, desinfecção, desinsetização, imunização, higienização, desratização, pulverização e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "07.16": {
    "descricao": "Florestamento, reflorestamento, semeadura, adubação, reparação de solo, plantio, silagem, colheita, corte e descascamento de árvores, silvicultura, exploração florestal e dos serviços congêneres indissociáveis da formação, manutenção e colheita de florestas, para quaisquer fins e por quaisquer meios.",
    "aliquota": "2,00",
    "servicos": [],
  },
  "07.17": {
    "descricao": "Escoramento, contenção de encostas e serviços congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "07.18": {
    "descricao": "Limpeza e dragagem de rios, portos, canais, baías, lagos, lagoas, represas, açudes e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "07.19": {
    "descricao": "Acompanhamento e fiscalização da execução de obras de engenharia, arquitetura e urbanismo.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "07.20": {
    "descricao": "Aerofotogrametria (inclusive interpretação), cartografia, mapeamento, levantamentos topográficos, batimétricos, geográficos, geodésicos, geológicos, geofísicos e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "07.21": {
    "descricao": "Pesquisa, perfuração, cimentação, mergulho, perfilagem, concretação, testemunhagem, pescaria, estimulação e outros serviços relacionados com a exploração e explotação de petróleo, gás natural e de outros recursos minerais.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "07.22": {
    "descricao": "Nucleação e bombardeamento de nuvens e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "08.01": {
    "descricao": "Ensino regular pré-escolar, fundamental, médio e superior.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "08.02": {
    "descricao": "Instrução, treinamento, orientação pedagógica e educacional, avaliação de conhecimentos de qualquer natureza.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "09.01": {
    "descricao": "Hospedagem de qualquer natureza em hotéis, apart-service condominiais, flat, apart-hotéis, hotéis residência, residence-service, suite service, hotelaria marítima, motéis, pensões e congêneres; ocupação por temporada com fornecimento de serviço (o valor da alimentação e gorjeta, quando incluído no preço da diária, fica sujeito ao Imposto Sobre Serviços).",
    "aliquota": "3,00",
    "servicos": [],
  },
  "09.02": {
    "descricao": "Agenciamento, organização, promoção, intermediação e execução de programas de turismo, passeios, viagens, excursões, hospedagens e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "09.03": {
    "descricao": "Guias de turismo.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "10.01": {
    "descricao": "Agenciamento, corretagem ou intermediação de câmbio, de seguros, de cartões de crédito, de planos de saúde e de planos de previdência privada.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "10.02": {
    "descricao": "Agenciamento, corretagem ou intermediação de títulos em geral, valores mobiliários e contratos quaisquer.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "10.03": {
    "descricao": "Agenciamento, corretagem ou intermediação de direitos de propriedade industrial, artística ou literária.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "10.04": {
    "descricao": "Agenciamento, corretagem ou intermediação de contratos de arrendamento mercantil (leasing), de franquia (franchising) e de faturização (factoring).",
    "aliquota": "3,00",
    "servicos": [],
  },
  "10.05": {
    "descricao": "Agenciamento, corretagem ou intermediação de bens móveis ou imóveis, não abrangidos em outros itens ou subitens, inclusive aqueles realizados no âmbito de Bolsas de Mercadorias e Futuros, por quaisquer meios.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "10.06": {
    "descricao": "Agenciamento marítimo.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "10.07": {
    "descricao": "Agenciamento de notícias.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "10.08": {
    "descricao": "Agenciamento de publicidade e propaganda, inclusive o agenciamento de veiculação por quaisquer meios.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "10.09": {
    "descricao": "Representação de qualquer natureza, inclusive comercial.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "10.10": {
    "descricao": "Distribuição de bens de terceiros.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "11.01": {
    "descricao": "Guarda e estacionamento de veículos terrestres automotores, de aeronaves e de embarcações.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "11.02": {
    "descricao": "Vigilância, segurança ou monitoramento de bens, pessoas e semoventes. (Redação dada pela Lei Complementar nº 157, de 2016)",
    "aliquota": "5,00",
    "servicos": [],
  },
  "11.03": {
    "descricao": "Escolta, inclusive de veículos e cargas.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "11.04": {
    "descricao": "Armazenamento, depósito, carga, descarga, arrumação e guarda de bens de qualquer espécie.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "12.01": {
    "descricao": "Espetáculos teatrais.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "12.02": {
    "descricao": "Exibições cinematográficas.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "12.03": {
    "descricao": "Espetáculos circenses.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "12.04": {
    "descricao": "Programas de auditório.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "12.05": {
    "descricao": "Parques de diversões, centros de lazer e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "12.06": {
    "descricao": "Boates, taxi-dancing e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "12.07": {
    "descricao": "Shows, ballet, danças, desfiles, bailes, óperas, concertos, recitais, festivais e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "12.08": {
    "descricao": "Feiras, exposições, congressos e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "12.09": {
    "descricao": "Bilhares, boliches e diversões eletrônicas ou não.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "12.10": {
    "descricao": "Corridas e competições de animais.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "12.11": {
    "descricao": "Competições esportivas ou de destreza física ou intelectual, com ou sem a participação do espectador.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "12.12": {
    "descricao": "Execução de música.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "12.13": {
    "descricao": "Produção, mediante ou sem encomenda prévia, de eventos, espetáculos, entrevistas, shows, ballet, danças, desfiles, bailes, teatros, óperas, concertos, recitais, festivais e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "12.14": {
    "descricao": "Fornecimento de música para ambientes fechados ou não, mediante transmissão por qualquer processo.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "12.15": {
    "descricao": "Desfiles de blocos carnavalescos ou folclóricos, trios elétricos e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "12.16": {
    "descricao": "Exibição de filmes, entrevistas, musicais, espetáculos, shows, concertos, desfiles, óperas, competições esportivas, de destreza intelectual ou congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "12.17": {
    "descricao": "Recreação e animação, inclusive em festas e eventos de qualquer natureza.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "13.02": {
    "descricao": "Fonografia ou gravação de sons, inclusive trucagem, dublagem, mixagem e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "13.03": {
    "descricao": "Fotografia e cinematografia, inclusive revelação, ampliação, cópia, reprodução, trucagem e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "13.04": {
    "descricao": "Reprografia, microfilmagem e digitalização.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "13.05": {
    "descricao": "Composição gráfica, inclusive confecção de impressos gráficos, fotocomposição, clicheria, zincografia, litografia e fotolitografia, exceto se destinados a posterior operação de comercialização ou industrialização, ainda que incorporados, de qualquer forma, a outra mercadoria que deva ser objeto de posterior circulação, tais como bulas, rótulos, etiquetas, caixas, cartuchos, embalagens e manuais técnicos e de instrução, quando ficarão sujeitos ao ICMS. (Redação dada pela Lei Complementar nº 157, de 2016)",
    "aliquota": "3,00",
    "servicos": [],
  },
  "14.01": {
    "descricao": "Lubrificação, limpeza, lustração, revisão, carga e recarga, conserto, restauração, blindagem, manutenção e conservação de máquinas, veículos, aparelhos, equipamentos, motores, elevadores ou de qualquer objeto (exceto peças e partes empregadas, que ficam sujeitas ao ICMS).",
    "aliquota": "5,00",
    "servicos": [],
  },
  "14.02": {
    "descricao": "Assistência técnica.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "14.03": {
    "descricao": "Recondicionamento de motores (exceto peças e partes empregadas, que ficam sujeitas ao ICMS).",
    "aliquota": "5,00",
    "servicos": [],
  },
  "14.04": {
    "descricao": "Recauchutagem ou regeneração de pneus.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "14.05": {
    "descricao": "Restauração, recondicionamento, acondicionamento, pintura, beneficiamento, lavagem, secagem, tingimento, galvanoplastia, anodização, corte, recorte, plastificação, costura, acabamento, polimento e congêneres de objetos quaisquer. (Redação dada pela Lei Complementar nº 157, de 2016)",
    "aliquota": "5,00",
    "servicos": [],
  },
  "14.06": {
    "descricao": "Instalação e montagem de aparelhos, máquinas e equipamentos, inclusive montagem industrial, prestados ao usuário final, exclusivamente com material por ele fornecido.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "14.07": {
    "descricao": "Colocação de molduras e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "14.08": {
    "descricao": "Encadernação, gravação e douração de livros, revistas e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "14.09": {
    "descricao": "Alfaiataria e costura, quando o material for fornecido pelo usuário final, exceto aviamento.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "14.10": {
    "descricao": "Tinturaria e lavanderia.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "14.11": {
    "descricao": "Tapeçaria e reforma de estofamentos em geral.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "14.12": {
    "descricao": "Funilaria e lanternagem.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "14.13": {
    "descricao": "Carpintaria e serralheria.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "14.14": {
    "descricao": "Guincho intramunicipal, guindaste e içamento.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.01": {
    "descricao": "Administração de fundos quaisquer, de consórcio, de cartão de crédito ou débito e congêneres, de carteira de clientes, de cheques pré-datados e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.02": {
    "descricao": "Abertura de contas em geral, inclusive conta-corrente, conta de investimentos e aplicação e caderneta de poupança, no País e no exterior, bem como a manutenção das referidas contas ativas e inativas.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.03": {
    "descricao": "Locação e manutenção de cofres particulares, de terminais eletrônicos, de terminais de atendimento e de bens e equipamentos em geral.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.04": {
    "descricao": "Fornecimento ou emissão de atestados em geral, inclusive atestado de idoneidade, atestado de capacidade financeira e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.05": {
    "descricao": "Cadastro, elaboração de ficha cadastral, renovação cadastral e congêneres, inclusão ou exclusão no Cadastro de Emitentes de Cheques sem Fundos - CCF ou em quaisquer outros bancos cadastrais.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.06": {
    "descricao": "Emissão, reemissão e fornecimento de avisos, comprovantes e documentos em geral; abono de firmas; coleta e entrega de documentos, bens e valores; comunicação com outra agência ou com a administração central; licenciamento eletrônico de veículos; transferência de veículos; agenciamento fiduciário ou depositário; devolução de bens em custódia.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.07": {
    "descricao": "Acesso, movimentação, atendimento e consulta a contas em geral, por qualquer meio ou processo, inclusive por telefone, fac-símile, internet e telex, acesso a terminais de atendimento, inclusive vinte e quatro horas; acesso a outro banco e a rede compartilhada; fornecimento de saldo, extrato e demais informações relativas a contas em geral, por qualquer meio ou processo.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.08": {
    "descricao": "Emissão, reemissão, alteração, cessão, substituição, cancelamento e registro de contrato de crédito; estudo, análise e avaliação de operações de crédito; emissão, concessão, alteração ou contratação de aval, fiança, anuência e congêneres; serviços relativos a abertura de crédito, para quaisquer fins.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.09": {
    "descricao": "Arrendamento mercantil (leasing) de quaisquer bens, inclusive cessão de direitos e obrigações, substituição de garantia, alteração, cancelamento e registro de contrato, e demais serviços relacionados ao arrendamento mercantil (leasing).",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.10": {
    "descricao": "Serviços relacionados a cobranças, recebimentos ou pagamentos em geral, de títulos quaisquer, de contas ou carnês, de câmbio, de tributos e por conta de terceiros, inclusive os efetuados por meio eletrônico, automático ou por máquinas de atendimento; fornecimento de posição de cobrança, recebimento ou pagamento; emissão de carnês, fichas de compensação, impressos e documentos em geral.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.11": {
    "descricao": "Devolução de títulos, protesto de títulos, sustação de protesto, manutenção de títulos, reapresentação de títulos, e demais serviços a eles relacionados.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.12": {
    "descricao": "Custódia em geral, inclusive de títulos e valores mobiliários.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.13": {
    "descricao": "Serviços relacionados a operações de câmbio em geral, edição, alteração, prorrogação, cancelamento e baixa de contrato de câmbio; emissão de registro de exportação ou de crédito; cobrança ou depósito no exterior; emissão, fornecimento e cancelamento de cheques de viagem; fornecimento, transferência, cancelamento e demais serviços relativos a carta de crédito de importação, exportação e garantias recebidas; envio e recebimento de mensagens em geral relacionadas a operações de câmbio.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.14": {
    "descricao": "Fornecimento, emissão, reemissão, renovação e manutenção de cartão magnético, cartão de crédito, cartão de débito, cartão salário e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.15": {
    "descricao": "Compensação de cheques e títulos quaisquer; serviços relacionados a depósito, inclusive depósito identificado, a saque de contas quaisquer, por qualquer meio ou processo, inclusive em terminais eletrônicos e de atendimento.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.16": {
    "descricao": "Emissão, reemissão, liquidação, alteração, cancelamento e baixa de ordens de pagamento, ordens de crédito e similares, por qualquer meio ou processo; serviços relacionados à transferência de valores, dados, fundos, pagamentos e similares, inclusive entre contas em geral.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.17": {
    "descricao": "Emissão, fornecimento, devolução, sustação, cancelamento e oposição de cheques quaisquer, avulso ou por talão.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "15.18": {
    "descricao": "Serviços relacionados a crédito imobiliário, avaliação e vistoria de imóvel ou obra, análise técnica e jurídica, emissão, reemissão, alteração, transferência e renegociação de contrato, emissão e reemissão do termo de quitação e demais serviços relacionados a crédito imobiliário.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "16.01": {
    "descricao": "Serviços de transporte coletivo municipal rodoviário, metroviário, ferroviário e aquaviário de passageiros.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "16.02": {
    "descricao": "Outros serviços de transporte de natureza municipal.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "17.01": {
    "descricao": "Assessoria ou consultoria de qualquer natureza, não contida em outros itens desta lista; análise, exame, pesquisa, coleta, compilação e fornecimento de dados e informações de qualquer natureza, inclusive cadastro e similares.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "17.02": {
    "descricao": "Datilografia, digitação, estenografia, expediente, secretaria em geral, resposta audível, redação, edição, interpretação, revisão, tradução, apoio e infra-estrutura administrativa e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "17.03": {
    "descricao": "Planejamento, coordenação, programação ou organização técnica, financeira ou administrativa.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "17.04": {
    "descricao": "Recrutamento, agenciamento, seleção e colocação de mão-de-obra.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "17.05": {
    "descricao": "Fornecimento de mão-de-obra, mesmo em caráter temporário, inclusive de empregados ou trabalhadores, avulsos ou temporários, contratados pelo prestador de serviço.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "17.06": {
    "descricao": "Propaganda e publicidade, inclusive promoção de vendas, planejamento de campanhas ou sistemas de publicidade, elaboração de desenhos, textos e demais materiais publicitários.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "17.08": {
    "descricao": "Franquia (franchising).",
    "aliquota": "3,00",
    "servicos": [],
  },
  "17.09": {
    "descricao": "Perícias, laudos, exames técnicos e análises técnicas.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "17.10": {
    "descricao": "Planejamento, organização e administração de feiras, exposições, congressos e congêneres.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "17.11": {
    "descricao": "Organização de festas e recepções; bufê (exceto o fornecimento de alimentação e bebidas, que fica sujeito ao ICMS).",
    "aliquota": "3,00",
    "servicos": [],
  },
  "17.12": {
    "descricao": "Administração em geral, inclusive de bens e negócios de terceiros.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "17.13": {
    "descricao": "Leilão e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "17.14": {
    "descricao": "Advocacia.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "17.15": {
    "descricao": "Arbitragem de qualquer espécie, inclusive jurídica.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "17.16": {
    "descricao": "Auditoria.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "17.17": {
    "descricao": "Análise de Organização e Métodos.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "17.18": {
    "descricao": "Atuária e cálculos técnicos de qualquer natureza.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "17.19": {
    "descricao": "Contabilidade, inclusive serviços técnicos e auxiliares.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "17.20": {
    "descricao": "Consultoria e assessoria econômica ou financeira.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "17.21": {
    "descricao": "Estatística.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "17.22": {
    "descricao": "Cobrança em geral.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "17.23": {
    "descricao": "Assessoria, análise, avaliação, atendimento, consulta, cadastro, seleção, gerenciamento de informações, administração de contas a receber ou a pagar e em geral, relacionados a operações de faturização (factoring).",
    "aliquota": "3,00",
    "servicos": [],
  },
  "17.24": {
    "descricao": "Apresentação de palestras, conferências, seminários e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "17.25": {
    "descricao": "Inserção de textos, desenhos e outros materiais de propaganda e publicidade, em qualquer meio (exceto em livros, jornais, periódicos e nas modalidades de serviços de radiodifusão sonora e de sons e imagens de recepção livre e gratuita).",
    "aliquota": "3,00",
    "servicos": [],
  },
  "18.01": {
    "descricao": "Serviços de regulação de sinistros vinculados a contratos de seguros; inspeção e avaliação de riscos para cobertura de contratos de seguros; prevenção e gerência de riscos seguráveis e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "19.01": {
    "descricao": "Serviços de distribuição e venda de bilhetes e demais produtos de loteria, bingos, cartões, pules ou cupons de apostas, sorteios, prêmios, inclusive os decorrentes de títulos de capitalização e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "20.01": {
    "descricao": "Serviços portuários, ferroportuários, utilização de porto, movimentação de passageiros, reboque de embarcações, rebocador escoteiro, atracação, desatracação, serviços de praticagem, capatazia, armazenagem de qualquer natureza, serviços acessórios, movimentação de mercadorias, serviços de apoio marítimo, de movimentação ao largo, serviços de armadores, estiva, conferência, logística e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "20.02": {
    "descricao": "Serviços aeroportuários, utilização de aeroporto, movimentação de passageiros, armazenagem de qualquer natureza, capatazia, movimentação de aeronaves, serviços de apoio aeroportuários, serviços acessórios, movimentação de mercadorias, logística e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "20.03": {
    "descricao": "Serviços de terminais rodoviários, ferroviários, metroviários, movimentação de passageiros, mercadorias, inclusive suas operações, logística e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "21.01": {
    "descricao": "Serviços de registros públicos, cartorários e notariais.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "22.01": {
    "descricao": "Serviços de exploração de rodovia mediante cobrança de preço ou pedágio dos usuários, envolvendo execução de serviços de conservação, manutenção, melhoramentos para adequação de capacidade e segurança de trânsito, operação, monitoração, assistência aos usuários e outros serviços definidos em contratos, atos de concessão ou de permissão ou em   normas oficiais.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "23.01": {
    "descricao": "Serviços de programação e comunicação visual, desenho industrial e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "24.01": {
    "descricao": "Serviços de chaveiros, confecção de carimbos, placas, sinalização visual, banners, adesivos e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "25.01": {
    "descricao": "Funerais, inclusive fornecimento de caixão, urna ou esquifes; aluguel de capela; transporte do corpo cadavérico; fornecimento de flores, coroas e outros paramentos; desembaraço de certidão de óbito; fornecimento de véu, essa e outros adornos; embalsamento, embelezamento, conservação ou restauração de cadáveres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "25.02": {
    "descricao": "Translado intramunicipal e cremação de corpos e partes de corpos cadavéricos.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "25.03": {
    "descricao": "Planos ou convênio funerários.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "25.04": {
    "descricao": "Manutenção e conservação de jazigos e cemitérios.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "25.05": {
    "descricao": "Cessão de uso de espaços em cemitérios para sepultamento.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "26.01": {
    "descricao": "Serviços de coleta, remessa ou entrega de correspondências, documentos, objetos, bens ou valores, inclusive pelos correios e suas agências franqueadas; courrier e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "27.01": {
    "descricao": "Serviços de assistência social.",
    "aliquota": "2,00",
    "servicos": [],
  },
  "28.01": {
    "descricao": "Serviços de avaliação de bens e serviços de qualquer natureza.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "29.01": {
    "descricao": "Serviços de biblioteconomia.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "30.01": {
    "descricao": "Serviços de biologia, biotecnologia e química.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "31.01": {
    "descricao": "Serviços técnicos em edificações, eletrônica, eletrotécnica, mecânica, telecomunicações e congêneres.",
    "aliquota": "5,00",
    "servicos": [],
  },
  "32.01": {
    "descricao": "Serviços de desenhos técnicos.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "33.01": {
    "descricao": "Serviços de desembaraço aduaneiro, comissários, despachantes e congêneres.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "34.01": {
    "descricao": "Serviços de investigações particulares, detetives e congêneres.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "35.01": {
    "descricao": "Serviços de reportagem, assessoria de imprensa, jornalismo e relações públicas.",
    "aliquota": "4,00",
    "servicos": [],
  },
  "36.01": {
    "descricao": "Serviços de meteorologia.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "37.01": {
    "descricao": "Serviços de artistas, atletas, modelos e manequins.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "38.01": {
    "descricao": "Serviços de museologia.",
    "aliquota": "3,00",
    "servicos": [],
  },
  "39.01": {
    "descricao": "Serviços de ourivesaria e lapidação (quando o material for fornecido pelo tomador do serviço).",
    "aliquota": "3,00",
    "servicos": [],
  },
  "40.01": {
    "descricao": "Obras de arte sob encomenda.",
    "aliquota": "3,00",
    "servicos": [],
  }
}


for item in lista_cnaes:
	if item['CodigoServicoFederal'] != "":
		try:
			lista = dicionario[ item['CodigoServicoFederal'] ]['servicos']
			#print(lista)
			lista.append(item['CodigoServicoMunicipal'])
			#print(lista)
			dicionario[ item['CodigoServicoFederal'] ]['servicos'] = lista
		except:
			pass
	#print(item['CodigoServicoFederal'])
	#print(dicionario[ item['CodigoServicoFederal'] ]['servicos']) #= dicionario[ item['CodigoServicoFederal'] ]['servicos'].append(item['CodigoServicoMunicipal'])

with open('lista_item_cnae.json', 'w') as outfile:
    json.dump(dicionario, outfile, indent=4)