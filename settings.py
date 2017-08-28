class Settings():

    def __init__(self):
        """Initialize the simulation's static settings."""
        # Screen settings.
        self.screen_width = 1000
        self.screen_height = 1000
        self.bg_color = (230, 230, 230)

        # Wall settings
        self.wall_size = (50, self.screen_width)
        # Particle settings
        self.particle_size = (40, 40)
        self.particle_pos = (20, 20)
        self.particle_radius = 20
        self.number_particles = 5
        self.max_speed = 100
        self.initial_speed = 20
