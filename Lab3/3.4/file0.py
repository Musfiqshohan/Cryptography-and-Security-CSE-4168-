#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ,~$:�si��(���?��S)� �@������toJÛ�!�=����_�Fq��m�f4r:,��}{Xz\��:Mc7�dt�ҫ��`H�ד X����?�Z:�
����=}	)P�xF;~O���W�4��8Nop���'h������@������#^t��2��h�5�u���ij�p��N�� ��'�fW�")<�M"4��7��!Y�	?��o\O�����i�j��H�M{�����u�	�a,pf���؂/@�)��k荻+��VA}/(&=�)
ˀ�~o�e#�[�����ⴌ"�޺3/�z^��L�+�ݱaK�%���G�_8*J���ɣK_�A%v���ԋ~�g1�q��ӧ�)	O�c8���tI�&pΑ�3Z޾�#u�޷>m���yA�7:�&�r���c���L�o?5���c{�u��2zI �]oC��O�)LI\��x�4�tF>:v��O���l�*�L���؀zo#�ᣇ�Gr{ط�����*7ϵ��݁ �ʁ����PY��&8m�09���(�>o�Vze�,����
M�J^p�0�s�[�%��۱O���]C�MK%G�߽�.���__]%��\��%��V�k��j�����ٵzD��m���Kd��c���^�U�bS�Uê<��6�D���/B᭳�n����8�5UFn�)/��v���s�u��WZ�̐@���������P��l��J^��}�s�a�H�I=
�X1��
s���U~e��*a
"""
from hashlib import sha256
sha=sha256(blob).hexdigest()
print(sha)

