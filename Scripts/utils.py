
def planets_overlap(planet1,planet2,spaceship):
    dist = planet1.position.distance_to(planet2.position)
    required_space = planet1.radius + planet2.radius \
                    + max(spaceship.rect.width,spaceship.rect.height)
    return dist < required_space