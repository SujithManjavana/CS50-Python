from PIL import Image, ImageFilter
before = Image.open("e.jpg")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("o.jpg")
