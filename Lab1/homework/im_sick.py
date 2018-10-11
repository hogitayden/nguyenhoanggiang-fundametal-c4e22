from gmail import GMail, Message
gmail = GMail('hogi.burning@gmail.com', 'younottheonly1')
html_template='''
<p>Gửi chị trưởng ph&ograve;ng đ&aacute;ng k&iacute;nh,</p>
<p>H&ocirc;m nay thời tiết rất lạnh, em hy vọng chị đi l&agrave;m với quần &aacute;o ấm đầy đủ. Đ&aacute;ng lẽ h&ocirc;m nay em c&oacute; thể mang cho chị một ch&uacute;t ch&egrave; đỗ đen em nấu h&ocirc;m qua, nhưng &ocirc;ng trời kh&ocirc;ng cho em cơ hội l&agrave;m điều đ&oacute;.</p>
<p>Em bị ốm nặng lắm chị ạ, trời lạnh thế n&agrave;y ra ngo&agrave;i đường chắc c&ograve;n nặng th&ecirc;m. Chị cho em nghỉ tĩnh dưỡng, mai gặp lại chị. Em cảm ơn chị.</p>

'''
msg = Message('Good news', to = 'hoanggiang.ng10@gmail.com', html = html_template)

import datetime
now = datetime.datetime.now()
while True:
    if now.hour == 7:
        gmail.send(msg)
        break