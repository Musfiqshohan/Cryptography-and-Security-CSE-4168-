#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ,~$:�si��(���?��S)� �@������toJÛ�!�=����_�Fq��m�f4r:,��}{Xz\��:Mc7�dt�ҫ��`H�ד X����?�Z:�
����=}	)P�xF;~O���W�4��8Nop���'h������@������#^t��2��h�5�u���ij�p��N�� ��'�fW�")<�M"4��7��!Y�	?��o\O�����i�j��H�M{�����u�	�a,pf���؂/@�)��k荻�+��VA}/(&=�)
ˀ�~o�e#�#\�����ⴌ"�޺�/�z^��L�+�ݱaK�%���G�_�*J���ɣK_�A%v���ԋ~�g1����ӧ�)	O�c����tI�&pΑ�3Z޾�#u�޷>m��yA�7:�&�r���c���L��?5���c{�u��2z� �]oC��O�)LI\��x�4��F>:v��O���l�*�L���؀�n#�ᣇ�Gr{طU����*7ϵ��݁ �ʁ���ٛPY��&8m�09���(�>o�V�e�,����
M�J^p0�s�[�%��۱O���]C�MK%G߽�.���__]%��\��%��V�kɇ�j�����ٵzD�Im���Kd��c���^�U�bS�UC�<��6�D���/B᭳�n����8�5UFn�)/������s�u��WZ�̐@������5��P��l��J^��}�s�a�H�I=
��0��
s���U~��*a
"""
from hashlib import sha256
sha=sha256(blob).hexdigest()
print(sha)

