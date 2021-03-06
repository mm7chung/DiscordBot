import requests
import random

# for line in open("ProblemList.txt"):
#     print(line)


# for line in open("ProblemList.txt"):
#     problemList = line.split(', ')
#     TitleSlug = problemList[1]
#     print(TitleSlug)

for line in open("ProblemList.txt"):
    problemList = line.split(', ')
    problemName = problemList[0]
    if problemName.find("Queen") > -1:
        print(problemName)

def findNamedProblem(name):
    problemNameList = []
    for line in open("ProblemList.txt"):
        problemList = line.split(', ')
        problemName = problemList[0]
        problemTitleSlug = problemList[1]
        if problemName.find(name) > -1:
            problemNameList.append((problemName, problemTitleSlug))
    return problemNameList

print(findNamedProblem("Queens"))

headers = {
    'authority': 'leetcode.com',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
    'x-csrftoken': 'StvZGCA9XP97GYjy8aOrQ9cLLCRZV1X1rrgicIBZ5hs4PExgxqHOnSQ1W4Xszll8',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.59 Safari/537.36 Edg/92.0.902.22',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://leetcode.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://leetcode.com/problemset/all/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'csrftoken=StvZGCA9XP97GYjy8aOrQ9cLLCRZV1X1rrgicIBZ5hs4PExgxqHOnSQ1W4Xszll8; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNDMwMDEwOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImU5YjllMWRjNmMwNTNlMzQzNTMyZTNkNTFiYjhlOWFjNzQzZjU2MzAiLCJpZCI6NDMwMDEwOCwiZW1haWwiOiJ0eWxlci53LndoaXRlaHVyc3RAZ21haWwuY29tIiwidXNlcm5hbWUiOiJhMXJlMSIsInVzZXJfc2x1ZyI6ImExcmUxIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2ExcmUxL2F2YXRhcl8xNjIxMzc4NzcxLnBuZyIsInJlZnJlc2hlZF9hdCI6MTYyNDkyOTEzMywiaXAiOiI3My42MC4yNTIuMjE2IiwiaWRlbnRpdHkiOiJjOTM3MDE3OGY4NDA2OTgyNWI2NWEyODE3ODM0ODRjNCIsInNlc3Npb25faWQiOjk5OTEwNzB9.tIrmcXLxZISehv3ii2Bext_KdJBX_0Te13rxOBkoXKo; __cf_bm=70cf680ccb285894558f0cbdb9969d4cd9c896e4-1624929133-1800-AZuJu3QB0MOizbPV6rTyG/8TOWrh/yyep38evFcft5WkliSI0S+JqbNkSUW7zZln+k+WExrqFwqEsF9HCrj993c=; NEW_PROBLEMLIST_PAGE=1',
}

def appendProblemList():
    data = (
    '{"query":"\\n '
    'query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\\n '
    'problemsetQuestionList: questionList(\\n '
    'categorySlug: $categorySlug\\n '
    'limit: $limit\\n '
    'skip: $skip\\n '
    'filters: $filters\\n '
    ') {\\n '
    'total: totalNum\\n '
    'questions: data {\\n '
    'acRate\\n '
    'difficulty\\n '
    'freqBar\\n '
    'frontendQuestionId: questionFrontendId\\n '
    'isFavor\\n '
    'paidOnly: isPaidOnly\\n '
    'status\\n '
    'title\\n '
    'titleSlug\\n '
    'topicTags {\\n '
    'name\\n '
    'id\\n '
    'slug\\n '
    '}\\n '
    'hasSolution\\n '
    'hasVideoSolution\\n '
    '}\\n '
    '}\\n}\\n '
    '","variables":{"categorySlug":"","skip":0,"limit":1917,"filters":{}}}'
    )
    problemsJson = requests.post('https://leetcode.com/graphql/', headers=headers, data=data).json()
    try: 
        numOfProblems = len(problemsJson["data"]["problemsetQuestionList"]["questions"])
    except: 
        print("Something went wrong...")
        print(problemsJson)
    problemNum = 0
    file = open("ProblemList.txt", "a")
    while problemNum < numOfProblems:
        problemName = problemsJson["data"]["problemsetQuestionList"]["questions"][problemNum]["title"]
        problemDirectory = problemsJson["data"]["problemsetQuestionList"]["questions"][problemNum]["titleSlug"]
        file.write(problemName + ", " + problemDirectory + "\n")
        problemNum += 1
    problemUrl = 'https://leetcode.com/problems/' + problemDirectory
