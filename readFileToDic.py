def readFileToDic(studentsFileName) -> dict:
    kashkoolFile = open("kashkool.txt","r")
    lines = kashkoolFile.readlines()
    kashkoolFile.close()

    students = {}

    for line in lines:
        studentDataList = line[:-1].split(",")
        id = int(studentDataList[0])
        name = studentDataList[1]
        gpa = float(studentDataList[2])
        students[id] = {"name" : name, "gpa": gpa}

    return students