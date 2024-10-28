def main():
  myFile = open("qbdata.txt", 'r')

  for line in myFile:
    info = line.split("\t")
    if info[7] != "Rate" and float(info[7])>100:
      print(info[0], "had a rating of", info[7])
      
  myFile.close()


if __name__ == '__main__':
  main()
