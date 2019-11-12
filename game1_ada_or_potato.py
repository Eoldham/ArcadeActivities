import arcade

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Ada or Potato?"
GAME_SPEED = 1 / 60
TIMER_MAXIMUM = 100

IMAGE_ADA = arcade.load_texture("images/ada.png")
IMAGE_POTATO = arcade.load_texture("images/potato.png")


class Image(arcade.Sprite):
    timer: int

    def __init__(self):
        super().__init__()
        self.timer = 0
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 2
        self.texture = IMAGE_POTATO

    def update_timer(self):
        if self.timer < TIMER_MAXIMUM:
            self.timer += 1
        else:
            self.timer = 0

    def update(self):
        self.update_timer()
        if self.timer == 100:
            self.update_image()

    def update_image(self):
        if self.texture == IMAGE_POTATO:
            self.texture = IMAGE_ADA
        else:
            self.texture = IMAGE_POTATO


class AdaOrPotato(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.image_list = None
        self.count = 0

    def setup(self):
        arcade.set_background_color(BACKGROUND_COLOR)
        self.image_list = arcade.SpriteList()
        self.image_list.append(Image())

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.image_list.draw()
        output = f"Score: {self.count}"
        arcade.draw_text(output, 10, 20, arcade.color.GREEN, 14)

    def on_update(self, delta_time):
        self.image_list.update()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        for images in self.image_list:
            if images.texture == IMAGE_ADA:
                self.count += 1
            images.update_image()


def main():
    window = AdaOrPotato()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
