import csv

DATASET = 'books-en.csv'


#1
def lenght_str(Data):
  Data.seek(0)
  reader = csv.DictReader(Data, delimiter = ';')
  counter = 0
  for i in reader:
      if len(i["Book-Title"]) > 30:
          counter += 1
  return counter


#2
def author_finder(Data, author):
  Data.seek(0)
  result = []
  reader = csv.DictReader(Data, delimiter = ';')
  for i in reader:
    if i["Book-Author"] == author:
      if 2016 <= int(i["Year-Of-Publication"]) <= 2018:
        result.append(i["Book-Title"])
  return result


#3.
def generator(Data):
  Data.seek(0)
  reader =csv.DictReader(Data, delimiter = ';')
  counter = 0
  with open('generator.txt', 'w') as sequence:
     for i in reader:
        counter += 1
        sequence.write(f"""{i["Book-Author"]}. {i["Book-Title"]} - {i["Year-Of-Publication"]}\n)""")
        if counter == 20:
           break


if __name__ == "__main__":
       with open(DATASET) as dataset:
        print("point 1:", lenght_str(dataset))
        print("point 2:",author_finder(dataset, "Celia Brooks Brown"))
        generator(dataset)
   