#!/usr/bin/env bash

PIP_REQUIREMENTS="build/bibliotecas.txt"

if [[ ! -f "$PIP_REQUIREMENTS" ]]; then
    echo "Erro: Arquivo 'bibliotecas.txt' não encontrado em $PIP_REQUIREMENTS."
    exit 1
fi

pip install -r "$PIP_REQUIREMENTS"
if [[ $? -ne 0 ]]; then
    echo "Erro ao instalar dependências."
    exit 1
fi

# python3 build/download_chromeDrive.py
# if [[ $? -ne 0 ]]; then
#     echo "Erro ao executar download_chromeDrive.py."
#     exit 1
# fi

echo "Executando teste.py..."
python3 build/teste.py
if [[ $? -ne 0 ]]; then
    echo "Erro ao executar teste.py."
    exit 1
fi

exit 0
