#                                                Группа:		M-PT1-82-25
#                                                Учащийся:	Марцинкевич А.Н.
#
#
#                        Домашняя работа №7
# Задание 1.

# сделать еще 4 фильтра для картинки:

# 1. Негатив: для каждого цвета в пикселе взять его противоположное значение: 255 - цвет

# 2. Соляризация (solarization) - 
#    Сначала считаем яркость пикселя: brightness, она будет равна среднему арифметическому r g и b (просто их складываем и делим на 3)
#    Затем проверяем эту яркость. Если она больше порога (порог задаём сами в самом начале функции соляризации), то вместо r берем 255-r, вместо g  255-g и для b так же. Если она не больше порога, то ничего не делаем, просто оставляем r g b как есть

# 3. Кастомный коэффициент. У юзера нужно дополнително спросить коэффициент ( >= 0), но помнить, что цвет в пикселе может принимать значение от 0 до 255. Каждый цвет в пикселе помножить на этот коэффициент с учетом вышесказанного ограничения. 

# 2. Poster-filter:
# Параметр levels спрашиваем у юзера (целое 2…256, по умолчанию 4) - сколько градаций оставить в каждом канале.

# Чем меньше levels, тем сильнее «постеризация»:
# 2 → чёрно-красный-зелёный-синий постер, 8 → мягкий эффект.

# r = ((r // step) * step) + offset, где: step это 256 / / levels, а offset - это целая часть половины шага

# Для остальных цветов формула та же. Опять же помним, что в цвет может попасть значение только от 0 до 255

# Решение:

# pip install pillow

print('-' * 80)
print('Task 1')


from PIL import Image
import os.path


def gray_filter(img):
    pixels = img.load()
    width, height = img.size

    # (255, 255, 255) - white
    # (0, 0, 0) - black
    # (128, 128, 128) - middle gray


    for y in range(0, height):
        for x in range(0, width):
            pixel = pixels[x, y]
            red, green, blue = pixel # (244, 200, 10)
            gray = (red + green + blue) // 3
            pixels[x, y] = (gray, gray, gray)
    return img


def sepia_filter(img):
    pixels = img.load()
    width, height = img.size

    # (255, 255, 255) - white
    # (0, 0, 0) - black
    # (128, 128, 128) - middle gray


    for y in range(0, height):
        for x in range(0, width):
            pixel = pixels[x, y]
            red, green, blue = pixel # (244, 200, 10)
            new_red = int(0.393 * red + 0.769 * green + 0.189 * blue)
            new_green = int(0.349 * red + 0.686 * green + 0.168 * blue)
            new_blue = int(0.272 * red + 0.534 * green + 0.131 * blue)
            pixels[x, y] = (new_red, new_green, new_blue)
    return img

# Add functionality

def filter_negative(img):
    pixels = img.load()
    width, height = img.size

    for y in range(0, height):
        for x in range(0, width):
            pixel = pixels[x, y]
            red, green, blue = pixel # (244, 200, 10)
            # gray = (red + green + blue) // 3
            pixels[x, y] = 255 - red, 255 - green, 255 - blue
    return img

def filter_solarization(img):
    pixels = img.load()
    width, height = img.size
    threshold = 100

    for y in range(0, height):
        for x in range(0, width):
            pixel = pixels[x, y]
            red, green, blue = pixel # (244, 200, 10)
            brightness = (red + green + blue) // 3
            pixels[x, y] = (
                red if brightness < threshold else 255 - red,
                green if brightness < threshold else 255 - green,
                blue if brightness < threshold else 255 - blue
            )
    return img

def filter_custom(img):
    pixels = img.load()
    width, height = img.size

    param = int(input('Enter int value 1-10 for color multiplication: '))

    for y in range(0, height):
        for x in range(0, width):
            pixel = pixels[x, y]
            red, green, blue = pixel # (244, 200, 10)
            pixels[x, y] = (
                (red * param) // 3 if (red * param) // 3 < 255 else 255,
                (green * param) // 3 if (green * param) // 3 < 255 else 255,
                (blue * param) // 3 if (blue * param) // 3 < 255 else 255
            )
    return img

def filter_poster(img):
    pixels = img.load()
    width, height = img.size

    param = int(input('Enter int value 2-256 for color postering: '))
    levels = param
    step = 256 // levels
    offset = step // 2

    for y in range(0, height):
        for x in range(0, width):
            pixel = pixels[x, y]
            red, green, blue = pixel # (244, 200, 10)
            pixels[x, y] = (
                ((red // step) * step) + offset if ((red // step) * step) + offset < 255 else 255,
                ((green // step) * step) + offset if ((green // step) * step) + offset < 255 else 255,
                ((blue // step) * step) + offset if ((blue // step) * step) + offset < 255 else 255
            )
    return img

def main():
    # file_path = "home/users/olga/picture.jpg
    # file_path = "home/users/olga/picture_result.jpg
    file_path = input("Enter file path ONLY JPG: ")
    result_path = file_path.replace('.jpg', '_result.jpg')

    choice_filter = input("1 - чб, 2 - сепия, 3 - негатив, 4 - соляризация, 5 - пользовательский, 6 - постер: ")

    if os.path.exists(file_path):
        with Image.open(file_path).convert('RGB') as img:
            if choice_filter == '1':
                result_img = gray_filter(img)
            elif choice_filter == '2':
                result_img = sepia_filter(img)
            elif choice_filter == '3':
                result_img = filter_negative(img)
            elif choice_filter == '4':
                result_img = filter_solarization(img)
            elif choice_filter == '5':
                result_img = filter_custom(img)
            elif choice_filter == '6':
                result_img = filter_poster(img)

            result_img.save(result_path)
    else:
        print("Wrong path!")

main()
