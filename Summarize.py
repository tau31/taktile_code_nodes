def add(data):
    """Function that summarized cols a and b"""
    print("this is even newer")
    data["sum"] = data["a"] + data["b"]

    return data


if __env:  # indicates we are running on Taktile
    data = add(data)
