namespace SpriteKind {
    export const Bubble = SpriteKind.create()
}

info.onScore(95, function on_on_score() {
    
    HeartContainer = sprites.create(img`
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
        `, SpriteKind.Food)
    tiles.placeOnRandomTile(HeartContainer, sprites.dungeon.stairLadder)
})
info.onScore(45, function on_on_score2() {
    
    HeartContainer = sprites.create(img`
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
        `, SpriteKind.Food)
    tiles.placeOnRandomTile(HeartContainer, sprites.dungeon.stairLadder)
})
info.onScore(25, function on_on_score3() {
    tiles.setCurrentTilemap(tilemap`
        level7
    `)
    tiles.placeOnRandomTile(Cat, sprites.dungeon.darkGroundCenter)
    tiles.placeOnRandomTile(Ball, sprites.dungeon.darkGroundCenter)
    tiles.placeOnRandomTile(Spike, sprites.dungeon.collectibleInsignia)
    tiles.placeOnRandomTile(Spike2, sprites.dungeon.collectibleInsignia)
    tiles.placeOnRandomTile(Spike3, sprites.dungeon.collectibleInsignia)
    tiles.placeOnRandomTile(Spike4, sprites.dungeon.collectibleInsignia)
    game.showLongText("Level 2", DialogLayout.Bottom)
})
info.onScore(100, function on_on_score4() {
    game.showLongText("You did it!", DialogLayout.Bottom)
    game.showLongText("Here's a trophy for your hard work!", DialogLayout.Bottom)
    game.gameOver(true)
})
info.onLifeZero(function on_life_zero() {
    game.gameOver(false)
})
info.onScore(70, function on_on_score5() {
    
    HeartContainer = sprites.create(img`
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
        `, SpriteKind.Food)
    tiles.placeOnRandomTile(HeartContainer, sprites.dungeon.stairLadder)
})
info.onScore(50, function on_on_score6() {
    tiles.setCurrentTilemap(tilemap`
        level11
    `)
    tiles.placeOnRandomTile(Cat, sprites.dungeon.darkGroundCenter)
    tiles.placeOnRandomTile(Ball, sprites.dungeon.darkGroundCenter)
    tiles.placeOnRandomTile(Spike, sprites.dungeon.collectibleInsignia)
    tiles.placeOnRandomTile(Spike2, sprites.dungeon.collectibleInsignia)
    tiles.placeOnRandomTile(Spike3, sprites.dungeon.collectibleInsignia)
    tiles.placeOnRandomTile(Spike4, sprites.dungeon.collectibleInsignia)
    game.showLongText("Level 3", DialogLayout.Bottom)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Bubble, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    
    info.changeScoreBy(1)
    sprites.destroy(otherSprite, effects.disintegrate, 500)
    Ball = sprites.create(img`
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
        `, SpriteKind.Bubble)
    tiles.placeOnRandomTile(Ball, sprites.dungeon.darkGroundCenter)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function on_on_overlap2(sprite2: Sprite, otherSprite2: Sprite) {
    info.changeLifeBy(1)
    sprites.destroy(otherSprite2, effects.ashes, 500)
})
info.onScore(20, function on_on_score7() {
    
    HeartContainer = sprites.create(img`
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
        `, SpriteKind.Food)
    tiles.placeOnRandomTile(HeartContainer, sprites.dungeon.stairLadder)
})
info.onScore(75, function on_on_score8() {
    tiles.setCurrentTilemap(tilemap`
        level14
    `)
    tiles.placeOnRandomTile(Cat, sprites.dungeon.darkGroundCenter)
    tiles.placeOnRandomTile(Ball, sprites.dungeon.darkGroundCenter)
    tiles.placeOnRandomTile(Spike, sprites.dungeon.collectibleInsignia)
    tiles.placeOnRandomTile(Spike2, sprites.dungeon.collectibleInsignia)
    tiles.placeOnRandomTile(Spike3, sprites.dungeon.collectibleInsignia)
    tiles.placeOnRandomTile(Spike4, sprites.dungeon.collectibleInsignia)
    game.showLongText("Level 4, Final level!", DialogLayout.Bottom)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap3(sprite3: Sprite, otherSprite3: Sprite) {
    info.changeLifeBy(-1)
    tiles.placeOnRandomTile(Cat, sprites.dungeon.darkGroundCenter)
})
let HeartContainer : Sprite = null
let Spike4 : Sprite = null
let Spike3 : Sprite = null
let Spike2 : Sprite = null
let Spike : Sprite = null
let Ball : Sprite = null
let Cat : Sprite = null
let speed = 100
Cat = sprites.create(img`
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
    `, SpriteKind.Player)
scene.cameraFollowSprite(Cat)
Ball = sprites.create(img`
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
    `, SpriteKind.Bubble)
Spike = sprites.create(img`
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
    `, SpriteKind.Enemy)
Spike2 = sprites.create(img`
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
    `, SpriteKind.Enemy)
Spike3 = sprites.create(img`
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
    `, SpriteKind.Enemy)
Spike4 = sprites.create(img`
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
    `, SpriteKind.Enemy)
controller.moveSprite(Cat, speed, speed)
tiles.setCurrentTilemap(tilemap`
    level0
`)
tiles.placeOnRandomTile(Cat, sprites.dungeon.darkGroundCenter)
tiles.placeOnRandomTile(Ball, sprites.dungeon.darkGroundCenter)
tiles.placeOnRandomTile(Spike, sprites.dungeon.collectibleInsignia)
tiles.placeOnRandomTile(Spike2, sprites.dungeon.collectibleInsignia)
tiles.placeOnRandomTile(Spike3, sprites.dungeon.collectibleInsignia)
tiles.placeOnRandomTile(Spike4, sprites.dungeon.collectibleInsignia)
info.setLife(3)
game.showLongText("Welcome! Collect as many Orbs as you can!", DialogLayout.Bottom)
game.showLongText("Level 1", DialogLayout.Bottom)
