class Settings():

    def __init__(self):
        """Initialize the simulation's static settings."""
        # Screen settings.
        self.screen_width = 1000
        self.screen_height = 1000
        self.bg_color = (230, 230, 230)

        # Particle settings
        self.particle_size = (20, 20)
        self.number_particles = 10
        self.max_speed = 100
