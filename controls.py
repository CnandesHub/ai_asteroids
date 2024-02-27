import pygame


class Controls:
    def __init__(self, control_type="Player"):
        self.control_type = control_type

    @staticmethod
    def handle_keys_player():
        keys = pygame.key.get_pressed()
        pressed_keys = []

        if keys[pygame.K_w]:
            pressed_keys.append("forward")
        if keys[pygame.K_s]:
            pressed_keys.append("backward")
        if keys[pygame.K_d]:
            pressed_keys.append("right")
        if keys[pygame.K_a]:
            pressed_keys.append("left")
        return pressed_keys

    def handle_keys_ai(self, brain_output, threshold=0.5):
        pressed_keys = []
        actions = ["forward", "backward", "right", "left"]

        for i in range(len(brain_output)):
            if brain_output[i] > threshold:
                pressed_keys.append(actions[i])

        return pressed_keys

    def handle_keys(self, brain_output=None):
        if self.control_type == "Player":
            return self.handle_keys_player()
        if self.control_type == "AI":
            return self.handle_keys_ai(brain_output)
        return [False, False, False, False]
