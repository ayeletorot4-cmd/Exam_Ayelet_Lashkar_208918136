def most_common_word(story: tuple[str,...])->str:
    """
    get a story and find which word appeared the most times in that story
    :param story: tuple
    :return: string

    """
    list_=[]
    for i in story:
        lst1= i.split()
        list_.extend(lst1)

    print(list_)
    my_story=tuple(list_)
    for word in my_story:
        n=my_story.count(word)
        print(word,n)

most_common_word(("hello world", "hello there- today is sunday","weekend is fun","yes it is"))
