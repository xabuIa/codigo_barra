from barcode import EAN13
from barcode.writer import ImageWriter

##codigos criados com IA generativa
codigo_items = {
"Arroz" : "487239485620",
"Feijão" : "192837465091",
"Leite" : "384759202830",
"Pão" : "567890123456",
"Ovo" : "908172634581",
"Macarrão" : "234567890123",
"Açúcar" : "345678901234",
"Café" : "456789012345",
"Óleo" : "567890123987",
"Tomate" : "678901234567",
"Frango" : "789012345678",
"Manteiga" : "890123456789",
}

for produto in codigo_items:
    codigo = codigo_items[produto]
    codigo_barra = EAN13(codigo, writer= ImageWriter())
    codigo_barra.save(produto)
    
    
