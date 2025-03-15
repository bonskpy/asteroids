import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def detect_collision(self, object) -> bool:
        """/
        This function checks if object is in collision
        with another object. Returns True if collision 
        is detected.
        """
        distance = self.position.distance_to(object.position) # returns float

        if distance <= self.radius + object.radius:
            return True
        return False
