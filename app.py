from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

print('Введите имя: ')
name = input()

print('Введите номер сертификата: ')
number = input()

input_image_path = 'services/Sertificat_base.jpg'
output_image_path = f'Sertificats/{name}_{number}.jpg'

position_name = (550, 530)
position_number = (550, 770)


def nameRight(input_image_path, output_image_path, name, position_name, position_number):
    photo = Image.open(input_image_path)
    """ Open img"""
    drawing = ImageDraw.Draw(photo)
    """make the image editable"""
    color = (255, 0, 0)
    """ FontColor"""
    font = ImageFont.truetype('services/font/MyriadPro-Light.ttf', 60)
    """ Font & Size"""
    drawing.text(position_name, name, color, font=font)
    """ Record Name in sertificat"""
    drawing.text(position_number, number, color, font=font)
    """ Record Number in Sertificate"""
    # photo.show()
    """Demonstrate resultgit remote add origin https://github.com/KYONY/Python-Pillow.git"""
    photo.save(output_image_path)
    """Saving result"""
    return print('Создание сертификата завершено')


if __name__ == '__main__':
    nameRight(input_image_path, output_image_path, name, position_name, position_number)
