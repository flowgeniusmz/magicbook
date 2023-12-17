from tempfile import NamedTemporaryFile

def get_tempfile_path(varImage):
    with NamedTemporaryFile(delete=False, suffix=".jpg") as tmpfile:
        varImage.save(tmpfile, format="JPEG")  # Save the image to the temporary file
        image_path = tmpfile.name
    return image_path