from gmail import GMail, Message
gmail = GMail('hogi.burning@gmail.com','younottheonly1')
html_template='''
<p>Ch&agrave;o anh</p>
<p>S&aacute;ng nay cuối th&aacute;ng, em cảm thấy cần 100 triệu để lo cho gia đinh v&agrave; cổ vũ tuyển Việt Nam. Mong anh tăng lương cho em.</p>
<p>B&ecirc;n cạnh đ&oacute; em đang bị&nbsp;{{symptom}} </p>
<p>Y&ecirc;u anh</p>
<p>Nh&acirc;n vi&ecirc;n số 1 của anh.</p>
'''
symptom_list = ['đau chân', 'đau bụng', 'đau vai']
from random import choice
x = choice(symptom_list)
html_content = html_template.replace("{{symptom}}", x)
msg = Message('nah', to='hoanggiang.ng10@gmail.com', html=html_content)
gmail.send(msg) 
