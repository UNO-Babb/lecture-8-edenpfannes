def main():
  myFile = open("ufo_sightings.csv", 'r')

  for line in myFile:
    info = line.split(",")
    #print(info[1])
    if info[1] == '"NE"':
      print(line)
      
  myFile.close()


if __name__ == '__main__':
  main()