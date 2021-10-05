from ocr import OCR

if __name__ == "__main__":
    try:
        filename = input("Enter the file name:")
    except FileNotFoundError as error:
        print(str(error))
    else:
        file = OCR(filename)
        print("Please provide the required details:")
        [x0, y0, x2, y2] = map(int, input("Enter the rectangle:").split())
        reqText = file.spanWords(x0=x0, y0=y0, x2=x2, y2=y2)
        print(reqText)
