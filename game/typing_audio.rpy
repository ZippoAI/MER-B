# MER-B The Last Signal — text-reveal audio, isolated from music/voice/SFX.
# Ren'Py 8.5.3 routes the Text displayable's completion/dismissal to slow_done.
# No estimated duration, character timers, or changes to the text speed.

define merb_keyboard_file = "audio/sfx/Keyboard-Sound.mp3"
define merb_keyboard_channel = "merb_keyboard"
define merb_keyboard_volume = 0.18

# Defaults keep older saves loadable. This flag is cleared after loading;
# it never grants a restored audio loop permission to resume by itself.
default _merb_keyboard_revealing = False

init -5 python:
    renpy.music.register_channel(
        "merb_keyboard", mixer="sfx", loop=True, tight=True,
        stop_on_mute=True, buffer_queue=True, synchro_start=False,
    )

    def merb_keyboard_stop():
        # Clear both playback and its loop queue. A 10ms release avoids a hard
        # waveform cut without a perceptible sound tail after text completion.
        if not renpy.is_init_phase():
            renpy.music.stop(channel=merb_keyboard_channel, fadeout=0.01)

    def merb_keyboard_clear():
        store._merb_keyboard_revealing = False
        merb_keyboard_stop()

    def merb_keyboard_sync():
        # Re-check on interaction restarts (skip/preferences/menu return). Never
        # restart the recording merely because a screen was re-evaluated.
        text = renpy.get_widget("say", "what")
        allowed = (
            store._merb_keyboard_revealing
            and text is not None and text.slow
            and preferences.text_cps > 0
            and not preferences.self_voicing
            and not preferences.get_mute("sfx")
            and preferences.get_volume("sfx") > 0
            and not renpy.is_skipping() and not renpy.in_rollback()
            and not renpy.context()._menu and not store.main_menu
            and not getattr(store, "_windows_hidden", False)
        )
        if not allowed:
            merb_keyboard_stop()
        elif renpy.music.get_loop(channel=merb_keyboard_channel) != [merb_keyboard_file]:
            renpy.music.play(
                merb_keyboard_file, channel=merb_keyboard_channel,
                loop=True, tight=True, fadein=0.01,
                relative_volume=merb_keyboard_volume,
            )

    def merb_keyboard_boundary(event, **kwargs):
        # Every speaker, including silent Earth/narrator/centered, starts clean.
        if event == "begin":
            merb_keyboard_clear()

    def merb_keyboard_voice(event, interact=True, **kwargs):
        # Attached to character objects below, never matched by displayed name.
        if event == "show_done":
            store._merb_keyboard_revealing = bool(interact)
            merb_keyboard_sync()
        elif event in ("slow_done", "interact_done", "end"):
            merb_keyboard_clear()

init 10 python:
    config.all_character_callbacks.append(merb_keyboard_boundary)
    config.interact_callbacks.append(merb_keyboard_sync)
    # Menus, hidden-interface mode, console, and other new contexts stop audio
    # immediately; returning may resume only if the actual text is still slow.
    config.context_callbacks.append(merb_keyboard_stop)
    config.before_load_callbacks.append(merb_keyboard_clear)
    config.after_load_callbacks.append(merb_keyboard_clear)
    config.fast_skipping_callbacks.append(merb_keyboard_clear)
