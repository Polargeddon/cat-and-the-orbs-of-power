@namespace
class SpriteKind:
    Bubble = SpriteKind.create()

def on_on_score():
    global HeartContainer
    HeartContainer = sprites.create(img("""
            ....................
                    ....................
                    ....................
                    ....................
                    ....................
                    ....................
                    .......22...22......
                    ......2322.2222.....
                    ......232222222.....
                    ......222222222.....
                    .......22222b2......
                    ........222b2.......
                    .........222........
                    ..........2.........
                    ....................
                    ....................
                    ....................
                    ....................
                    ....................
                    ....................
        """),
        SpriteKind.food)
    tiles.place_on_random_tile(HeartContainer, sprites.dungeon.stair_ladder)
info.on_score(95, on_on_score)

def on_on_score2():
    global HeartContainer
    HeartContainer = sprites.create(img("""
            ....................
                    ....................
                    ....................
                    ....................
                    ....................
                    ....................
                    .......22...22......
                    ......2322.2222.....
                    ......232222222.....
                    ......222222222.....
                    .......22222b2......
                    ........222b2.......
                    .........222........
                    ..........2.........
                    ....................
                    ....................
                    ....................
                    ....................
                    ....................
                    ....................
        """),
        SpriteKind.food)
    tiles.place_on_random_tile(HeartContainer, sprites.dungeon.stair_ladder)
info.on_score(45, on_on_score2)

def on_on_score3():
    tiles.set_current_tilemap(tilemap("""
        level7
    """))
    tiles.place_on_random_tile(Cat, sprites.dungeon.dark_ground_center)
    tiles.place_on_random_tile(Ball, sprites.dungeon.dark_ground_center)
    tiles.place_on_random_tile(Spike, sprites.dungeon.collectible_insignia)
    tiles.place_on_random_tile(Spike2, sprites.dungeon.collectible_insignia)
    tiles.place_on_random_tile(Spike3, sprites.dungeon.collectible_insignia)
    tiles.place_on_random_tile(Spike4, sprites.dungeon.collectible_insignia)
    game.show_long_text("Level 2", DialogLayout.BOTTOM)
info.on_score(25, on_on_score3)

def on_on_score4():
    game.show_long_text("You did it!", DialogLayout.BOTTOM)
    game.show_long_text("Here's a trophy for your hard work!", DialogLayout.BOTTOM)
    game.game_over(True)
info.on_score(100, on_on_score4)

def on_life_zero():
    game.game_over(False)
info.on_life_zero(on_life_zero)

def on_on_score5():
    global HeartContainer
    HeartContainer = sprites.create(img("""
            ....................
                    ....................
                    ....................
                    ....................
                    ....................
                    ....................
                    .......22...22......
                    ......2322.2222.....
                    ......232222222.....
                    ......222222222.....
                    .......22222b2......
                    ........222b2.......
                    .........222........
                    ..........2.........
                    ....................
                    ....................
                    ....................
                    ....................
                    ....................
                    ....................
        """),
        SpriteKind.food)
    tiles.place_on_random_tile(HeartContainer, sprites.dungeon.stair_ladder)
info.on_score(70, on_on_score5)

def on_on_score6():
    tiles.set_current_tilemap(tilemap("""
        level11
    """))
    tiles.place_on_random_tile(Cat, sprites.dungeon.dark_ground_center)
    tiles.place_on_random_tile(Ball, sprites.dungeon.dark_ground_center)
    tiles.place_on_random_tile(Spike, sprites.dungeon.collectible_insignia)
    tiles.place_on_random_tile(Spike2, sprites.dungeon.collectible_insignia)
    tiles.place_on_random_tile(Spike3, sprites.dungeon.collectible_insignia)
    tiles.place_on_random_tile(Spike4, sprites.dungeon.collectible_insignia)
    game.show_long_text("Level 3", DialogLayout.BOTTOM)
info.on_score(50, on_on_score6)

def on_on_overlap(sprite, otherSprite):
    global Ball
    info.change_score_by(1)
    sprites.destroy(otherSprite, effects.disintegrate, 500)
    Ball = sprites.create(img("""
            . . . . . b b b b b b . . . . . 
                    . . . b b 9 9 9 9 9 9 b b . . . 
                    . . b b 9 9 9 9 9 9 9 9 b b . . 
                    . b b 9 d 9 9 9 9 9 9 9 9 b b . 
                    . b 9 d 9 9 9 9 9 1 1 1 9 9 b . 
                    b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b 
                    b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b 
                    b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b 
                    b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b 
                    b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b 
                    b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b 
                    . b 5 3 3 3 d 9 9 9 9 d d 5 b . 
                    . b d 5 3 3 3 3 3 3 3 d 5 b b . 
                    . . b d 5 d 3 3 3 3 5 5 b b . . 
                    . . . b b 5 5 5 5 5 5 b b . . . 
                    . . . . . b b b b b b . . . . .
        """),
        SpriteKind.Bubble)
    tiles.place_on_random_tile(Ball, sprites.dungeon.dark_ground_center)
sprites.on_overlap(SpriteKind.player, SpriteKind.Bubble, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_life_by(1)
    sprites.destroy(otherSprite2, effects.ashes, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

def on_on_score7():
    global HeartContainer
    HeartContainer = sprites.create(img("""
            ....................
                    ....................
                    ....................
                    ....................
                    ....................
                    ....................
                    .......22...22......
                    ......2322.2222.....
                    ......232222222.....
                    ......222222222.....
                    .......22222b2......
                    ........222b2.......
                    .........222........
                    ..........2.........
                    ....................
                    ....................
                    ....................
                    ....................
                    ....................
                    ....................
        """),
        SpriteKind.food)
    tiles.place_on_random_tile(HeartContainer, sprites.dungeon.stair_ladder)
info.on_score(20, on_on_score7)

def on_on_score8():
    tiles.set_current_tilemap(tilemap("""
        level14
    """))
    tiles.place_on_random_tile(Cat, sprites.dungeon.dark_ground_center)
    tiles.place_on_random_tile(Ball, sprites.dungeon.dark_ground_center)
    tiles.place_on_random_tile(Spike, sprites.dungeon.collectible_insignia)
    tiles.place_on_random_tile(Spike2, sprites.dungeon.collectible_insignia)
    tiles.place_on_random_tile(Spike3, sprites.dungeon.collectible_insignia)
    tiles.place_on_random_tile(Spike4, sprites.dungeon.collectible_insignia)
    game.show_long_text("Level 4, Final level!", DialogLayout.BOTTOM)
info.on_score(75, on_on_score8)

def on_on_overlap3(sprite3, otherSprite3):
    info.change_life_by(-1)
    tiles.place_on_random_tile(Cat, sprites.dungeon.dark_ground_center)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

HeartContainer: Sprite = None
Spike4: Sprite = None
Spike3: Sprite = None
Spike2: Sprite = None
Spike: Sprite = None
Ball: Sprite = None
Cat: Sprite = None
speed = 100
Cat = sprites.create(img("""
        e e e . . . . e e e . . . . 
            c d d c . . c d d c . . . . 
            c b d d f f d d b c . . . . 
            c 3 b d d b d b 3 c . . . . 
            f b 3 d d d d 3 b f . . . . 
            e d d d d d d d d e . . . . 
            e d f d d d d f d e . b f b 
            f d d f d d f d d f . f d f 
            f b d d b b d d 2 f . f d f 
            . f 2 2 2 2 2 2 b b f f d f 
            . f b d d d d d d b b d b f 
            . f d d d d d b d d f f f . 
            . f d f f f d f f d f . . . 
            . f f . . f f . . f f . . .
    """),
    SpriteKind.player)
scene.camera_follow_sprite(Cat)
Ball = sprites.create(img("""
        . . . . . b b b b b b . . . . . 
            . . . b b 9 9 9 9 9 9 b b . . . 
            . . b b 9 9 9 9 9 9 9 9 b b . . 
            . b b 9 d 9 9 9 9 9 9 9 9 b b . 
            . b 9 d 9 9 9 9 9 1 1 1 9 9 b . 
            b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b 
            b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b 
            b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b 
            b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b 
            b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b 
            b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b 
            . b 5 3 3 3 d 9 9 9 9 d d 5 b . 
            . b d 5 3 3 3 3 3 3 3 d 5 b b . 
            . . b d 5 d 3 3 3 3 5 5 b b . . 
            . . . b b 5 5 5 5 5 5 b b . . . 
            . . . . . b b b b b b . . . . .
    """),
    SpriteKind.Bubble)
Spike = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . b . . . . . . . 
            . . . . . . . b d b . . . . . . 
            . . . . . . . c d c . . . . . . 
            . . . . . . . c 5 c . . . . . . 
            . . . . . . c d 5 d c . . . . . 
            . . . b c c d 5 5 5 d c c b . . 
            . . b d d 5 5 5 5 5 5 5 d d b . 
            . . . b c c d 5 5 5 d c c b . . 
            . . . . . . c d 5 d c . . . . . 
            . . . . . . . c 5 c . . . . . . 
            . . . . . . . c d c . . . . . . 
            . . . . . . . b d b . . . . . . 
            . . . . . . . . b . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
Spike2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . b . . . . . . . 
            . . . . . . . b d b . . . . . . 
            . . . . . . . c d c . . . . . . 
            . . . . . . . c 5 c . . . . . . 
            . . . . . . c d 5 d c . . . . . 
            . . . b c c d 5 5 5 d c c b . . 
            . . b d d 5 5 5 5 5 5 5 d d b . 
            . . . b c c d 5 5 5 d c c b . . 
            . . . . . . c d 5 d c . . . . . 
            . . . . . . . c 5 c . . . . . . 
            . . . . . . . c d c . . . . . . 
            . . . . . . . b d b . . . . . . 
            . . . . . . . . b . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
Spike3 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . b . . . . . . . 
            . . . . . . . b d b . . . . . . 
            . . . . . . . c d c . . . . . . 
            . . . . . . . c 5 c . . . . . . 
            . . . . . . c d 5 d c . . . . . 
            . . . b c c d 5 5 5 d c c b . . 
            . . b d d 5 5 5 5 5 5 5 d d b . 
            . . . b c c d 5 5 5 d c c b . . 
            . . . . . . c d 5 d c . . . . . 
            . . . . . . . c 5 c . . . . . . 
            . . . . . . . c d c . . . . . . 
            . . . . . . . b d b . . . . . . 
            . . . . . . . . b . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
Spike4 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . b . . . . . . . 
            . . . . . . . b d b . . . . . . 
            . . . . . . . c d c . . . . . . 
            . . . . . . . c 5 c . . . . . . 
            . . . . . . c d 5 d c . . . . . 
            . . . b c c d 5 5 5 d c c b . . 
            . . b d d 5 5 5 5 5 5 5 d d b . 
            . . . b c c d 5 5 5 d c c b . . 
            . . . . . . c d 5 d c . . . . . 
            . . . . . . . c 5 c . . . . . . 
            . . . . . . . c d c . . . . . . 
            . . . . . . . b d b . . . . . . 
            . . . . . . . . b . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
controller.move_sprite(Cat, speed, speed)
tiles.set_current_tilemap(tilemap("""
    level0
"""))
tiles.place_on_random_tile(Cat, sprites.dungeon.dark_ground_center)
tiles.place_on_random_tile(Ball, sprites.dungeon.dark_ground_center)
tiles.place_on_random_tile(Spike, sprites.dungeon.collectible_insignia)
tiles.place_on_random_tile(Spike2, sprites.dungeon.collectible_insignia)
tiles.place_on_random_tile(Spike3, sprites.dungeon.collectible_insignia)
tiles.place_on_random_tile(Spike4, sprites.dungeon.collectible_insignia)
info.set_life(3)
game.show_long_text("Welcome! Collect as many Orbs as you can!",
    DialogLayout.BOTTOM)
game.show_long_text("Level 1", DialogLayout.BOTTOM)