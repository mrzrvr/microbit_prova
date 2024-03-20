music._play_default_background(music.built_in_playable_melody(Melodies.PRELUDE),
    music.PlaybackMode.IN_BACKGROUND)

def on_forever():
    basic.show_icon(IconNames.SQUARE)
    basic.show_icon(IconNames.SMALL_SQUARE)
basic.forever(on_forever)
