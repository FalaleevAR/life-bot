START_MSG = '''This is Conway's Game of Life bot. Not a regular one, but continuous. Try it out with /life command!
As a result, you will get a unique environment no one has seen before!\n
Go /help for more commands.
'''
INFO_MSG = r'''Inspired by [this article](https://arxiv.org/abs/1111.1567) and implemented by @sashundikus.'''
EXCEPTION_MSG = "Exception massage. :("
COMMAND_NOT_FOUND_MSG = "Unknown command. Start with /start"
LIFE_TEXT_RESPONSE = "Rendering a unique life for your request. Usually, it takes about 15 sec, so wait a bit."
CONFIGURE_BEFORE = """We randomly initialize the field with dense squares with a fixed size.\n
You are welcome to configure the number of squares and its' weights to be initialized.\n
You can find initialization result in the first frame of video.
"""
CONFIGURE_COUNT = "**Number of dense squares**\n" \
                  ""
CONFIGURE_INTENSITY = "**Square weight**\n" \
                      "Every cell has its weight. The greater weight causes a higher influence on neighbor cells."
CONFIGURE_STYLE = "**Plotting style**\n" \
                  "Pick a style to be used while plotting your environment."
CONFIGURE_AFTER = "READY? Go /life"
