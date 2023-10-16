#Declare an empty list
empty_list = []
print(len(empty_list))

#Declare a list with more than 5 items
names = ['ritu','seema','ranu','riya','ridhi']
print(names)



#Find the length of your list
list = ['ritu','seema','ranu','riya','ridhi']
print(len(list))




#Get the first item, the middle item and the last item of the list
list = ['ritu','seema','ranu','riya','ridhi']

first_list = list[0]
print(first_list)
middle_list = list[2]
print(middle_list)
last_name = list[-1]
print(last_name)






# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)




#Print the list using print()
list = []
print(list)






#Print the number of companies in the list
company = ['google','amazon','vivo','facebook','Mi']
print(len(company))



#Print the first, middle and last company
company = ['google','amazon','vivo','facebook','Mi']
first_company = company[0]
print(first_company)
middle_company = company[2]
print(middle_company)
last_company = company[-1]
print(last_company)


#Print the list after modifying one of the companies
company = ['google','amazon','vivo','facebook','Mi']
company[0] = 'apple'
print(company)


#Add an IT company to it_companies
it_companies = ['apple','microsoft','google','IBM','dell']

it_companies.append('intl')
print(it_companies)


#Insert an IT company in the middle of the companies list
it_companies = ['apple','microsoft','google','IBM','dell']
middle_company = it_companies[2] = ('Intl')
print(it_companies)


#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies = ['apple','microsoft','google','IBM','dell']
it_companies = [i.upper() for i in it_companies]
print(it_companies)


#Join the it_companies with a string '#;  '
list_1 = ['vivo','microsoft','facebook']
list_2 = ['mi','google']
companies = list_1 + list_2
print(companies)


#Check if a certain company exists in the it_companies list.
it_company = ['apple','microsoft','google','IBM','dell']
does_exist = 'apple' in it_company
print(does_exist)



#Sort the list using sort() method
name = ['priya','ridhi','tiya','sidhi','nidhi']
name.sort()
print(name)



list = [90,70,80,30,50]
list.sort()
print(list)




#Reverse the list in descending order using reverse() method
list = [20,90,80,70,30]
list.reverse()
print(list)


#Slice out the first 3 companies from the list
it_companies = ['apple','microsoft','google','IBM','dell','intel']
del it_companies[0:3]
print(it_companies)


#Slice out the last 3 companies from the list
it_companies = ['apple','microsoft','google','IBM','dell','intel']
del it_companies[-3:]
print(it_companies)


#Slice out the middle IT company or companies from the list
it_companies = ['apple','microsoft','google','IBM','dell']
del it_companies[2:3]
print(it_companies)

#Remove the first IT company from the list
it_companies = ['apple','microsoft','google','IBM','dell']
it_companies.remove('apple')
print(it_companies)

#Remove the middle IT company or companies from the list
it_companies = ['apple','microsoft','google','IBM','dell']
it_companies.remove('google')
print(it_companies)



#Remove the last IT company from the list
it_companies = ['apple','microsoft','google','IBM','dell']
it_companies.pop()
print(it_companies)





#Remove all IT companies from the list
it_companies = ['apple','microsoft','google','IBM','dell']
it_companies.clear()
print(it_companies)

#Destroy the IT companies list
it_companies = ['apple','microsoft','google','IBM','dell']
del it_companies[0:5]
print(it_companies)


#Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)



#Find the middle country(ies) in the countries list

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_country = ['Finland']
print(middle_country)

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

list = ['china','russia','usa','finland','sweden','norway','denmark']
china,russia,usa,finland,*scandic,es = list
print('china')
print(russia)
print(usa)
print(finland)
print(scandic)
print(es)










