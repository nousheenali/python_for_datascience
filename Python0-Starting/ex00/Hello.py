ft_list  = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set   = {"Hello", "tutu!"}
ft_dict  = {"Hello" : "titi!"}

#change value of list
ft_list[1] = "World!"

#tuple is immutable so we convert it to list
ft_new_list = list(ft_tuple)
ft_new_list[1] = "United Arab Emirates!"
ft_tuple = tuple(ft_new_list)

# or alternatively
ft_tuple = (ft_tuple[0], "United Arab Emirates!") + ft_tuple[2:]


#set is mutable so we remove "tutu!" and add "AbuDhabi!"
# Once a set is created, you cannot change its items, but you can add or remove items.
ft_set.remove("tutu!")
ft_set.add("AbuDhabi!")


# for value in dictionary
ft_dict["Hello"] = "42AbuDhabi!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)