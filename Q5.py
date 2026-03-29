def most_common_word(story: tuple[str,...])->str:
    """
    get a story and find which word appeared the most times in that story
    :param story: tuple
    :return: string

    """
    most_common_word=story[0]
    for word in story:
        if word == most_common_word:
            return most_common_word
        else:
            most_common_word=most_common_word+"_"+word

