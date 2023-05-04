import pygame, time, configparser

pygame.init()

# Get the screen size
infoObject = pygame.display.Info()
screen_width = infoObject.current_w
screen_height = infoObject.current_h

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Load the background images
black_img = pygame.image.load('images/black.png')

# Set the initial background image
background = black_img

# Set up the font and font size for the clock
font_size = int(screen_width * 0.10)
font = pygame.font.Font("OpenSans-Bold.ttf", font_size)

# Set up the clock
clock = pygame.time.Clock()

# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Build a dictionary of key-value pairs from the configuration file
key_value_pairs = {}
for key, value in config['Keys'].items():
    key_value_pairs[pygame.__dict__['K_' + key]] = pygame.image.load('images/' + value)

last_blink = 0
# in milliseconds
blink_rate = 1000
colon_display = True

# Run the game loop
running = True
while running:
    # Limit the frame rate to 60 FPS
    dt = clock.tick(60) 
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # Change the background image when a key is pressed
            if event.key in key_value_pairs:
                background = key_value_pairs[event.key]

    # Draw the background image
    screen.blit(background, (0, 0))

    # Get the current time and format hour and minute separately
    hour_text = font.render(time.strftime("%H"), True, (255, 255, 255))
    minute_text = font.render(time.strftime("%M"), True, (255, 255, 255))

    # Blink the colon between alpha 0 and alpha 255 every one second
    last_blink += dt
    if last_blink > blink_rate:
        if colon_display == True:
            colon_display = False
        else:
            colon_display = True
        last_blink = 0
    colon_text = font.render(":", True, (255, 255, 255))

    # Draw the clock text onto the screen
    clock_padding_x = int(screen_width * 0.05)
    clock_padding_y = int(screen_height * 0.05)
    clock_x = screen_width - hour_text.get_width() - minute_text.get_width() - colon_text.get_width() - clock_padding_x
    clock_y = screen_height - hour_text.get_height() - clock_padding_y
    screen.blit(hour_text, (clock_x, clock_y))
    if colon_display:
        screen.blit(colon_text, (clock_x + hour_text.get_width(), clock_y - font_size / 16))
    screen.blit(minute_text, (clock_x + hour_text.get_width() + colon_text.get_width(), clock_y))

    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()
