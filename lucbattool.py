def extract_rhyme_pairs(poem):
    line = poem.split("\n")
    line_pairs68 = []

    for i in range(0, len(line) - 1, 2):
        line_pairs68.append((line[i], line[i+1]))

    rhyme_pairs = []

    for (l6, l8) in line_pairs68:
        word66 = l6.split(" ")[5]
        word68 = l8.split(" ")[5]
        rhyme_pairs.append((word66, word68))

    line_pairs86 = []

    for i in range(1, len(line) - 2, 2):
        line_pairs86.append((line[i], line[i+1]))

    rhyme_pairs = []

    for (l6, l8) in line_pairs68:
        word66 = l6.split(" ")[5]
        word68 = l8.split(" ")[5]
        rhyme_pairs.append((word66, word68))

    for (l8, l6) in line_pairs86:
        word88 = l8.split(" ")[7]
        word66 = l6.split(" ")[5]
        rhyme_pairs.append((word88, word66))

    return rhyme_pairs


if __name__ == '__main__':
    truyen_Kieu = """Trăm năm trong cõi người ta
Chữ tài chữ mệnh khéo là ghét nhau
Trải qua một cuộc bể dâu
Những điều trông thấy mà đau đớn lòng
Lạ gì bỉ sắc tư phong
Trời xanh quen thói má hồng đánh ghen
Cảo thơm lần dở trước đèn
Phong tình cổ lục còn truyền sử xanh"""

    print(extract_rhyme_pairs(truyen_Kieu))