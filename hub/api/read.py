from hub.core.sample import Sample  # type: ignore


def read(path: str, verify: bool = False) -> Sample:
    """Utility that reads raw data from supported files into hub format. Recompresses data into format required by the tensor
    if permitted by the tensor htype. Simply copies the data in the file if file format matches sample_compression of the tensor,
    thus maximizing upload speeds.

    Note:
        No data is actually loaded until you try to get a property of the returned `Sample`. This is useful for passing along to
            `tensor.append` and `tensor.extend`.

    Examples:
        >>> sample = hub.read("path/to/cat.jpeg")
        >>> type(sample.array)
        <class 'numpy.ndarray'>
        >>> sample.compression
        'jpeg'

        >>> ds.create_tensor("images", htype="image", sample_compression="jpeg")
        >>> ds.images.append(sample)
        >>> ds.images.shape
        (1, 399, 640, 3)

        >>> ds.create_tensor("videos", htype="video", sample_compression="mp4")
        >>> ds.videos.append(hub.read("path/to/video.mp4"))
        >>> ds.videos.shape
        (1, 136, 720, 1080, 3)

    Supported file types:
        Image: "bmp", "dib", "gif", "ico", "jpeg", "jpeg2000", "pcx", "png", "ppm", "sgi", "tga", "tiff", "webp", "wmf", "xbm"

        Audio: "flac", "mp3", "wav"

        Video: "mp4", "mkv", "avi"

    Args:
        path (str): Path to a supported file.
        verify (bool):  If True, contents of the file are verified.

    Returns:
        Sample: Sample object. Call `sample.array` to get the `np.ndarray`.
    """

    sample = Sample(path, verify=verify)
    return sample
