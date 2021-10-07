import discord
import os
import requests
import random
import ListFunctionTest as LFT

token = os.environ['DISCORDBOTTOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$goaway'):
        await message.channel.send('Go Fuck Yourself')

    if message.content.startswith('$leetcode'):
        await message.channel.send(getLeetCodeProblem())

    if message.content.startswith('$findleetcode'):
        name = message.content[len('$findleetcode') + 2:]
        problemTitleSlug = LFT.findNamedProblem(name)
        await message.channel.send('**Here are the problems: **')
        for element in problemTitleSlug:
            await message.channel.send(element[0] + ": " + 'https://leetcode.com/problems/' + element[1])
    if message.content.startswith('$ideas'):
        await message.channel.send(makeSentence())

def readList(fileName):
    wordList = []
    for line in open(fileName):
        wordList.append(line.strip())
    return wordList

verbs = readList('Verbs.list')
nouns = readList('Nouns.list')
adjectives = readList('Adjective.list')
prepositions = readList('Prepositions.list')
adverbs = readList('Adverbs.list')

def pickWord(wordList):
    numOfWords = len(wordList)
    wordNum = random.randint(0, numOfWords - 1)
    return wordList[wordNum]

def makeSentence():
    return pickWord(adjectives) + " " + pickWord(nouns) + " " + pickWord(adverbs) + " " + pickWord(verbs) + " " + pickWord(prepositions) + " " + pickWord(nouns)


def randDifficulty():
    difficulty = ""
    randNum = random.random()
    if randNum < 0.20:
        difficulty = "EASY"
    elif randNum < 0.75:
        difficulty = "MEDIUM"
    else:
        difficulty = "HARD"
    
    return difficulty

tagsList = [
  "array",
  "string",
  "hash-table",
  "dynamic-programming",
  "math",
  "depth-first-search",
  "sorting",
  "greedy",
  "breadth-first-search",
  "tree",
  "database",
  "binary-tree",
  "bit-manipulation",
  "two-pointers",
  "matrix",
  "binary-search",
  "stack",
  "design",
  "heap-priority-queue",
  "backtracking",
  "prefix-sum",
  "sliding-window",
  "simulation",
  "graph",
  "linked-list",
  "union-find",
  "counting",
  "recursion",
  "monotonic-stack",
  "trie",
  "binary-search-tree",
  "divide-and-conquer",
  "ordered-set",
  "bitmask",
  "queue",
  "segment-tree",
  "game-theory",
  "geometry",
  "memoization",
  "hash-function",
  "interactive",
  "topological-sort",
  "enumeration",
  "string-matching",
  "data-stream",
  "rolling-hash",
  "randomized",
  "binary-indexed-tree",
  "shortest-path",
  "combinatorics",
  "iterator",
  "concurrency",
  "probability-and-statistics",
  "monotonic-queue",
  "brainteaser",
  "number-theory",
  "doubly-linked-list",
  "merge-sort",
  "counting-sort",
  "minimum-spanning-tree",
  "bucket-sort",
  "quickselect",
  "shell",
  "suffix-array",
  "line-sweep",
  "strongly-connected-component",
  "reservoir-sampling",
  "eulerian-circuit",
  "radix-sort",
  "rejection-sampling",
  "biconnected-component"
]

def randTags():
    randTagNum = random.randint(0,70)
    randTagString = tagsList[randTagNum]
    return randTagString

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



def getLeetCodeProblem():
    difficultyString = randDifficulty()
    tagString = randTags()
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
    '","variables":{"categorySlug":"","skip":0,"limit":1917,"filters":{"difficulty": "' + difficultyString + '", "tags": ["' + tagString + '"]}}}'
    )
    problemsJson = requests.post('https://leetcode.com/graphql/', headers=headers, data=data).json()
    try: 
        numOfProblems = problemsJson["data"]["problemsetQuestionList"]["total"]
    except: 
        print("Something went wrong...")
        print(problemsJson)
    problemNum = random.randint(0,numOfProblems - 1)
    while problemsJson["data"]["problemsetQuestionList"]["questions"][problemNum]["paidOnly"] == True:
        problemNum = random.randint(0, numOfProblems - 1)
        print("Picking New Problem")
    problemDirectory = problemsJson["data"]["problemsetQuestionList"]["questions"][problemNum]["titleSlug"]
    problemUrl = 'https://leetcode.com/problems/' + problemDirectory
    return "The difficulty is: **" + difficultyString.lower() + "**\nThe tag is: **" + tagString + "**\nThe problem is: " + problemUrl


client.run(token)

"""
JSON (JavaScript Object Notation)

emptyObject = {}
object = {
    "key" : "value",
    "name" : "RayMonsterInter6969",
    "integeer" : 123,
    "float" : 1.23f,
    "string" : "a string",
    "long" : 1231231243124124124L,
    "nestedObject" : {
        "someKey": "someValue"
    },
    "myList": [{"name": "object1"}, {"name": "object2"}]
}
someList = [{"name": "object1"}, {"name": "object2"}]
"""


for line in open("ProblemList.txt"):
    problemList = line.split(', ')
    TitleSlug = problemList[1]