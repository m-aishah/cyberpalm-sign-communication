import sign_language_translator as slt

# Initialize the ConcatenativeSynthesis model for English to ASL video
model = slt.models.ConcatenativeSynthesis(
    text_language="english",          # or slt.languages.text.English()
    sign_language="pk-sl",           # Make sure "us-asl" is supported (ASL = American Sign Language)
    sign_format="video"               # You can also try "landmarks"
)

# Input English text
input_text = "this is world"

# Translate to ASL
sign = model.translate(input_text)

# Show the sign language translation video
sign.show()   # This opens the video window with gestures
sign.save("output.mp4")