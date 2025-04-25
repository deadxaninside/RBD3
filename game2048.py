import pygame, sys, random, time

random.seed()


def SameBesides(List):
    for i in range(3):
        for j in range(3):
            if (List[i][j] == List[i][j + 1]):
                return True
            elif (List[i][j] == List[i + 1][j]):
                return True
    if (List[3][3] == List[3][2] or List[3][3] == List[2][3]):
        return True
    else:
        return False


def EndingDetect(List):
    counter = 0
    for i in range(4):
        for j in range(4):
            if (List[i][j] != 0):
                counter += 1
    if (counter == 16):
        if (SameBesides(List) == True):
            return False
        else:
            return True
    else:
        return False

def RandomGeneration(List):
    counter = 0
    for i in range(4):
        for j in range(4):
            if (List[i][j] != 0):
                counter += 1
    repeat = 1

    while (repeat == 1 and counter != 16):
        repeat = 0
        # Generate Random Coordinate
        addingVert = random.randint(0, 3)
        addingHorz = random.randint(0, 3)
        if (List[addingVert][addingHorz] == 0):
            List[addingVert][addingHorz] = 2
        else:
            repeat = 1
    return List


def MovingLeft(numberList):
    for i in range(4):
        num = [0, 0, 0, 0]
        count = 0
        j = 0
        while (j <= 3):
            if (numberList[i][j] != 0):
                k = 1
                check = 0
                while (check == 0 and k <= 3 - j):
                    check = 1
                    if (j + k <= 3):

                        if (numberList[i][j + k] == 0 and j + k < 3):
                            k += 1
                            check = 0

                        else:

                            if (numberList[i][j] == numberList[i][j + k]):
                                num[count] = numberList[i][j] * 2
                                count += 1
                                k += 1
                            else:
                                num[count] = numberList[i][j]
                                count += 1
                if (j == 3):
                    num[count] = numberList[i][j]
                j += k
            else:
                j += 1
        numberList[i][0] = num[0]
        numberList[i][1] = num[1]
        numberList[i][2] = num[2]
        numberList[i][3] = num[3]
    return numberList



def MovingRight(numberList):
    for i in range(4):
        num = [0, 0, 0, 0]
        count = 3
        j = 3
        while (j >= 0):
            if (numberList[i][j] != 0):
                k = 1
                check = 0
                while (check == 0 and j - k >= 0):
                    check = 1
                    if (j - k >= 0):
                        if (numberList[i][j - k] == 0 and j - k > 0):
                            k += 1
                            check = 0
                        else:
                            if (numberList[i][j] == numberList[i][j - k]):
                                num[count] = numberList[i][j] * 2
                                count -= 1
                                k += 1
                            else:
                                num[count] = numberList[i][j]
                                count -= 1
                if (j == 0):
                    num[count] = numberList[i][j]
                j -= k
            else:
                j -= 1
        numberList[i][0] = num[0]
        numberList[i][1] = num[1]
        numberList[i][2] = num[2]
        numberList[i][3] = num[3]
    return numberList


def MovingUp(numberList):
    for j in range(4):
        num = [0, 0, 0, 0]
        count = 0
        i = 0
        while (i <= 3):
            if (numberList[i][j] != 0):
                k = 1
                check = 0
                while (check == 0 and k <= 3 - i):
                    check = 1
                    if (i + k <= 3):

                        if (numberList[i + k][j] == 0 and i + k < 3):
                            k += 1
                            check = 0
                        else:

                            if (numberList[i][j] == numberList[i + k][j]):
                                num[count] = numberList[i][j] * 2
                                count += 1
                                k += 1
                            else:
                                num[count] = numberList[i][j]
                                count += 1
                if (i == 3):
                    num[count] = numberList[i][j]

                i += k
            else:
                i += 1
        numberList[0][j] = num[0]
        numberList[1][j] = num[1]
        numberList[2][j] = num[2]
        numberList[3][j] = num[3]
    return numberList



def MovingDown(numberList):
    for j in range(4):
        num = [0, 0, 0, 0]
        count = 3
        i = 3
        while (i >= 0):
            if (numberList[i][j] != 0):
                k = 1
                check = 0
                while (check == 0 and i - k >= 0):
                    check = 1
                    if (i - k >= 0):
                        if (numberList[i - k][j] == 0 and i - k > 0):
                            k += 1
                            check = 0
                        else:
                            if (numberList[i][j] == numberList[i - k][j]):
                                num[count] = numberList[i][j] * 2
                                count -= 1
                                k += 1
                            else:
                                num[count] = numberList[i][j]
                                count -= 1
                if (i == 0):
                    num[count] = numberList[i][j]
                i -= k
            else:
                i -= 1
        numberList[0][j] = num[0]
        numberList[1][j] = num[1]
        numberList[2][j] = num[2]
        numberList[3][j] = num[3]
    return numberList



def show(List):
    background = pygame.Rect(trans_x - 10, trans_y - 10, 4 * box_w + 3 * gap + 20, 4 * box_h + 3 * gap + 20)
    bg_color = color_dic['gray']
    pygame.draw.rect(playSurface, bg_color, background)
    for i in range(4):
        for j in range(4):
            x_pos = j * (box_w + gap) + trans_x
            y_pos = i * (box_h + gap) + trans_y
            color_name = ColorChange(List[i][j])
            RGB = color_dic[color_name]
            box_rect = pygame.Rect(x_pos, y_pos, box_w, box_h)
            pygame.draw.rect(playSurface, RGB, box_rect)
            Font1 = pygame.font.SysFont('monaco', 50)
            if List[i][j] == 0:
                FontColor = bg_color
            else:
                FontColor = color_dic['black']
            surf1 = Font1.render('{0}'.format(List[i][j]), True, FontColor)
            rect1 = surf1.get_rect()
            rect1.center = box_rect.center
            playSurface.blit(surf1, rect1)


def ColorChange(num):
    return {
        0: 'gray',
        2: 'white',
        4: 'light_yellow',
        8: 'sandy_brown',
        16: 'coral',
        32: 'tomato',
        64: 'red',
        128: 'yellow_1',
        256: 'yellow_2',
        512: 'yellow_3',
        1024: 'yellow_3',
        2048: 'yellow_3',
        4096: 'green',
        8192: 'blue',
    }[num]


check_errors = pygame.init()
if (check_errors[1] > 0):
    print("(!) Had {0} initializing errors,exiting... ".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Pygame successfully initialized!")

pygame.font.init()

width = 600
height = 600

trans_x = 100
trans_y = 100

playSurface = pygame.display.set_mode((width, height))
pygame.display.set_caption('2048 Game!')

color_dic = {}
color_dic['black'] = pygame.Color(0, 0, 0)
color_dic['gray'] = pygame.Color(150, 150, 150)  # bg
color_dic['white'] = pygame.Color(245, 245, 245)  # 2
color_dic['light_yellow'] = pygame.Color(255, 248, 220)  # 4
color_dic['sandy_brown'] = pygame.Color(244, 164, 96)  # 8
color_dic['coral'] = pygame.Color(255, 127, 80)  # 16
color_dic['tomato'] = pygame.Color(255, 99, 71)  # 32
color_dic['red'] = pygame.Color(210, 0, 0)  # 64
color_dic['yellow_1'] = pygame.Color(255, 255, 204)  # 128
color_dic['yellow_2'] = pygame.Color(255, 255, 153)  # 256
color_dic['yellow_3'] = pygame.Color(255, 255, 102)  # 512, 1024, 2048
color_dic['green'] = pygame.Color(0, 255, 0)  # 4096
color_dic['blue'] = pygame.Color(0, 0, 255)  # 8192
color_dic['purple'] = pygame.Color(238, 130, 238)  # 16384, 32768


fpsController = pygame.time.Clock()

frame_rate = 50

numberList = [[0 for i in range(4)] for j in range(4)]
numberList = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

box_h = 90
box_w = 90
gap = 20

numberList = RandomGeneration(numberList)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                numberList = MovingRight(numberList)
                numberList = RandomGeneration(numberList)
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                numberList = MovingLeft(numberList)
                numberList = RandomGeneration(numberList)
            if event.key == pygame.K_UP or event.key == ord('w'):
                numberList = MovingUp(numberList)
                numberList = RandomGeneration(numberList)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                numberList = MovingDown(numberList)
                numberList = RandomGeneration(numberList)
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    show(numberList)
    pygame.display.flip()
    fpsController.tick(frame_rate)
