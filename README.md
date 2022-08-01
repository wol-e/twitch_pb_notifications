# twitch_pb_notifications

get live notifications on telegram for twitch speedrunners being close to PB (personal best)

-- work in progress --

Idea is to to use the twitch API to query for speedrunners current live thumbnails (lag should be below 5 mins) and use computer vision to extract the information required in order to determine if they are close to achieving a new pb. In case a pb is likely, send a message to telegram via a telegram bot.This way, you will never again miss your favourite speedrunners pb's ;)

-- status quo --

The infrastrucure around twitch and telegram apis is mostly working well enough for a first version. However, using out of the box frameworks for OCR (optical character recognition) seems to be not working well enough on average on twitch thumbnails due to the high background noise and the format the runners overlay for displaying the current pace (extensive testing was done with google tesseract plus some additional tools). Either we will need to train our own models or find a better preprocessing to make, for example, tesseract work well enough. To be continued.
