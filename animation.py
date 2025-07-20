import pygame
from  facetracker_module.facetracker import Tracker
import threading
import time

pygame.init()

screen = pygame.display.set_mode((0, 0))

dt = 1

print(screen.get_width(), screen.get_height())

prev_x = 0

def move_pupil(result, output_image, timestamp_ms):
    global pupil1, pupil2, screen, prev_x


    if result.detections:

        for detection in result.detections:

            boundingBox = detection.bounding_box
            x, y = boundingBox.origin_x, boundingBox.origin_y

            centre_x = x / 520 * dt * screen.get_width()
            gap = 300

            min_x = screen.get_width() / 3 
            max_x = screen.get_width() * 2 / 3
            if centre_x > min_x and centre_x < max_x:
                # print(f"difference: {x - prev_x}")
                if abs(x - prev_x) > 10:
                    pupil1.x = centre_x + gap
                    pupil2.x = centre_x - gap
                    prev_x = x
                    # print("done")

            elif centre_x > max_x:
                centre_x = max_x
            
            elif centre_x < min_x:
                centre_x = min_x

            # print(x, y)



tracking = Tracker(0, 'blazeface_sr.tflite', move_pupil)

thread1 = threading.Thread(target = tracking.start, kwargs={'looping_condition':True})
# thread2 = threading.Thread(target = animate)

thread1.start()
# thread2.start()

blinks = 0
completion = False

def blink(prevBlinkTime, timePeriod, timePerBlink, top_lid, bottom_lid):
    '''
    speed: this parameter is in seconds/blink
    '''
    global blinks, prevTop, completion

    BlinkTime = time.time()
    
    # if int(BlinkTime - prevBlinkTime) == blinks:
    if (int(BlinkTime - prevBlinkTime)) % timePeriod == 0:
        completion = False
        prevTop = top_lid.y
        # print(int(BlinkTime - prevBlinkTime))
    
    else:
        # print(int(BlinkTime - prevBlinkTime))
        if completion == False:
            # print(int(BlinkTime - prevBlinkTime))

            speed = 0.6 / timePerBlink

            if top_lid.y == screen.get_height() / 2 + 40 and bottom_lid.y == -40: 

                if prevTop < top_lid.y:
                    # have just opened
                    completion = True
                    # print("Completed")
                else:
                    # starting to close
                    # print("close")

                    prevTop = top_lid.y

                    top_lid.y -= speed    
                    bottom_lid.y += speed

            elif int(top_lid.y) == screen.get_height() / 2 and int(bottom_lid.y) == 0:
                # starting to open
                # print("open")

                prevTop = top_lid.y

                top_lid.y += speed
                bottom_lid.y -= speed

            else:
                if prevTop > top_lid.y:
                    # closing
                    # print("closing")

                    prevTop = top_lid.y

                    top_lid.y -= speed
                    bottom_lid.y += speed
                
                elif prevTop < top_lid.y:
                    # opening
                    # print("opening")

                    prevTop = top_lid.y

                    top_lid.y += speed
                    bottom_lid.y -= speed
                
                else:
                    print("BLINK ERROR!")

pupil1 = pygame.Vector2(y=screen.get_height() / 2)
pupil2 = pygame.Vector2(y=screen.get_height() / 2)

toplid = pygame.Vector2(y=screen.get_height() / 2 + 40)
bottomlid = pygame.Vector2(y=-40)

running = True

prevTime = time.time()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    keys = pygame.key.get_pressed()

    pygame.draw.circle(screen, "black", pupil1, 40)
    pygame.draw.circle(screen, "black", pupil2, 40)

    # blinking logic starts here

    topRect = pygame.Rect(toplid.x, toplid.y, screen.get_width(), screen.get_height() / 2)
    bottomRect = pygame.Rect(bottomlid.x, bottomlid.y, screen.get_width(), screen.get_height() / 2)

    pygame.draw.rect(screen, "white", topRect)
    pygame.draw.rect(screen, "white", bottomRect)

    blink(prevTime, 5, 1, toplid, bottomlid)

    # blinking logic ends here

    pygame.draw.line(screen, "black", (pupil2.x, pupil2.y), (pupil1.x, pupil1.y), 10)

    if keys[pygame.K_ESCAPE]:
        running = False

    pygame.display.flip()