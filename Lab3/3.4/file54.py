#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ,~$:�si��(���?�S)� �@������toJÛ�=����_�Fq����f4r:,��}{Xz\��:Mc7��t�ҫ��`H�ד X����?�Z:l
����=}	)P@xF;~O���W�4��8Nop��'h������@������#^t�[3��h�5�u���i��p��N�� ��'�fW�")<�M�"4��7��!Y�	?��o\O�����iBj��H�M{�������	�a,pf���؂/@�)��k荻+��VA}/(&=�)
ˀ�~o�e#�[�����ⴌ"�޺3/�z^��L�+�ݱaK�%���G�_8*J���ɣK_�A%v���ԋ~�g1�q��ӧ�)	O�c8���tI�&pΑ�3Z޾�#u�޷>m��yA�7:�&�r���c���L��?5���c{�u��2z� �]oC��O�)LI\��x�4��F>:v��O���l�*�L���؀�n#�ᣇ�Gr{طU����*7ϵ��݁ �ʁ���ٛPY��&8m�09���(�>o�V�e�,����
M�J^p0�s�[�%��۱O���]C�MK%G߽�.���__]%��\��%��V�kɇ�j�����ٵzD�Im���Kd��c���^�U�bS�Uê<��6�D���/B᭳�n����8�5UFn�)/��v���s�u��WZ�̐@���������P��l��J^��}�s�a�H�I=
�X1��
s���U~e��*a
"""
from hashlib import sha256
sha=sha256(blob).hexdigest()
print(sha)

