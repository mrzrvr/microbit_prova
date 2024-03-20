basic.show_leds("""
    # . . . .
    . # . . .
    . . # . .
    . . . # .
    . . . . #
    """)
music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM),
    music.PlaybackMode.IN_BACKGROUND)
basic.show_leds("""
    . . . . #
    . . . # .
    . . # . .
    . # . . .
    # . . . .
    """)
basic.show_leds("""
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    """)
basic.pause(3000)

def on_forever():
    basic.show_icon(IconNames.SQUARE)
    basic.show_icon(IconNames.SMALL_SQUARE)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.show_icon(IconNames.SMALL_SQUARE)
basic.forever(on_forever)
