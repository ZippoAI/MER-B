# MER-B The Last Signal — local font weights, no runtime network dependency.
# Use the actual designed faces for inline emphasis, rather than synthetic bold.
init python:
    config.font_replacement_map.update({
        ("fonts/SourceSans3-Regular.ttf", True, False):
            ("fonts/SourceSans3-Bold.ttf", False, False),
        ("fonts/SourceSans3-Regular.ttf", False, True):
            ("fonts/SourceSans3-It.ttf", False, False),
        ("fonts/SourceSans3-Regular.ttf", True, True):
            ("fonts/SourceSans3-BoldIt.ttf", False, False),
        ("fonts/SpaceGrotesk-Medium.ttf", True, False):
            ("fonts/SpaceGrotesk-Bold.ttf", False, False),
    })
