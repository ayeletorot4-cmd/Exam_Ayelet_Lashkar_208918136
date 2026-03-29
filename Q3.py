def snake_to_camel(text:str)->str:
    """
    convert text from snake_case to camelCase
    :param text: string
    :return: string
    """
    copy=list(text)
    if "_" in copy:
        for i in range(len(text)):
            if copy[i]=="_":
                copy[i + 1]=copy[i + 1].upper()

        copy.remove("_")
        text="".join(copy)
    return text
print(snake_to_camel("Hello_python"))
print(snake_to_camel("my_variable_name"))
print(snake_to_camel("python"))
print(snake_to_camel("a_b_c_d"))