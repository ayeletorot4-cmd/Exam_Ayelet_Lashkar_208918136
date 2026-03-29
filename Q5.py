#unfinished
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


    tuple_ = tuple(list_)
    set_=set(list_)
    dict_={}
    for i in set_:
        n = tuple_.count(i)
        dict_[i]=n


    maximum = max(dict_.values())
    for k,v in dict_.items():
        if v==maximum:
            print(k)
            print(f"{maximum} times")



most_common_word(("hello world", "hello there- today is sunday","weekend is fun","yes it is"))
most_common_word(story = (
    "The little fox saw the little bird and the little cat.",
    "The fox was happy because the little bird sang, and the little cat jumped.",
    "The little fox, the little bird, and the little cat became friends."
))