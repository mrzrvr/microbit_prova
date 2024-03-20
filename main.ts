basic.showLeds(`
    # . . . .
    . # . . .
    . . # . .
    . . . # .
    . . . . #
    `)
music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Dadadadum), music.PlaybackMode.InBackground)
basic.showLeds(`
    . . . . #
    . . . # .
    . . # . .
    . # . . .
    # . . . .
    `)
basic.showLeds(`
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    `)
basic.pause(3000)
basic.forever(function on_forever() {
    basic.showIcon(IconNames.Square)
    basic.showIcon(IconNames.SmallSquare)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.showIcon(IconNames.SmallSquare)
})
