# inddo_back_end
## Codigo para entendimento do algoritmo (Notebook)
Esse codigo utiliza o serviço de OCR do AWS Rekognition para buscar os exames descritos no receituario, onde o detalhe pode ser visto no notebook (rekognition.ipynb).

## Arquitetura do back-end
O back-end, pensando em escalabilidade, foi feita utilizando o lambda, e as imagens, são salvas no S3.
Foi utilizada uma biblioteca chamada PyLambda, o projeto pode ser visto no link (https://github.com/nficano/python-lambda);

Macro desenho: 

S3 > lambda > Rekognition
