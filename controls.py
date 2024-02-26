import pygame


class Controls:

    @staticmethod
    def handle_keys():
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
