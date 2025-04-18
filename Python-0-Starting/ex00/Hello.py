ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}



#your code here

ft_list[1] = "World!"

ft_list_tuple    = list(ft_tuple)
ft_list_tuple[1] = "Morocco!"
ft_tuple         = tuple(ft_list_tuple)

ft_set.remove("tutu!")

ft_set.add("Ben Guerir!")

ft_dict["Hello"] = "1337!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
