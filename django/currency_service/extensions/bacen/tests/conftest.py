from decimal import Decimal

import pytest


@pytest.fixture
def response_bacen_cotation():
    return {
        'anoFim': 0,
        'anoInicio': 1984,
        'aviso': {
            '_value_1': None,
            'id': None,
            'href': None,
            '_attr_1': {}
        },
        'diaFim': 0,
        'diaInicio': 28,
        'especial': False,
        'fonte': {
            '_value_1': 'Sisbacen PTAX800',
            'id': None,
            'href': None,
            '_attr_1': {}
        },
        'fullName': {
            '_value_1': (
                'Exchange rate - Free - United States dollar (sale) - 1'
            ),
            'id': None,
            'href': None,
            '_attr_1': {}
        },
        'gestorProprietario': {
            '_value_1': 'DEPIN/GEROP/DICAM',
            'id': None,
            'href': None,
            '_attr_1': {}
        },
        'mesFim': 0,
        'mesInicio': 11,
        'nomeAbreviado': {
            '_value_1': 'Dólar comercial (venda)',
            'id': None,
            'href': None,
            '_attr_1': {}
        },
        'nomeCompleto': {
            '_value_1': (
                'Taxa de câmbio - Livre - Dólar americano (venda) - diário'
            ),
            'id': None,
            'href': None,
            '_attr_1': {}
        },
        'oid': 1,
        'periodicidade': {
            '_value_1': 'Diária',
            'id': None,
            'href': None,
            '_attr_1': {}
        },
        'periodicidadeSigla': {
            '_value_1': 'D',
            'id': None,
            'href': None,
            '_attr_1': {}
        },
        'possuiBloqueios': False,
        'publica': True,
        'shortName': {
            '_value_1': 'Commercial exchange rate',
            'id': None,
            'href': None,
            '_attr_1': {}
        },
        'ultimoValor': {
            'ano': 2021,
            'anoFim': 1800,
            'bloqueado': False,
            'bloqueioLiberado': True,
            'dia': 1,
            'diaFim': 1,
            'mes': 2,
            'mesFim': 1,
            'oid': 8539080,
            'oidSerie': 1,
            'svalor': {
                '_value_1': '5.4608',
                'id': None,
                'href': None,
                '_attr_1': {}
            },
            'valor': {
                '_value_1': Decimal('5.4608'),
                'id': 'id23',
                'href': None,
                '_attr_1': {
                    '{http://schemas.xmlsoap.org/soap/encoding/}root': '0',
                    '{http://schemas.xmlsoap.org/soap/envelope/}encoding'
                    'Style': 'http://schemas.xmlsoap.org/soap/encoding/'
                }
            }
        },
        'unidadePadrao': {
            '_value_1': 'u.m.c./US$',
            'id': None,
            'href': None,
            '_attr_1': {}
        },
        'unidadePadraoIngles': {
            '_value_1': 'c.m.u./US$',
            'id': None,
            'href': None,
            '_attr_1': {}
        },
        'valorDiaNaoUtil': False,
        'valores': []
    }
