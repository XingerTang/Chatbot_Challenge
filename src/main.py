import requests
 
def main():
    API_URL = "https://sexkqhzet0df7r78.us-east-1.aws.endpoints.huggingface.cloud"
    headers = {
                    "Accept" : "application/json",
                    "Content-Type": "application/json"
    }
    
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    
    def get_question(level):
        question_file = open(f"L{level}.txt")
        question = question_file.readlines()
        return "\n".join(question)

    flag = True
    level = "1"
    level_up = False
    
    background = open("background.txt", "r")
    background = background.readlines()
    background = "\n".join(background)

    query({
            "parameters": {
		 "top_k": 1,
		 "top_p": 50
	},
            "inputs": background,
            })
    
    query({
        "parameters": {
		 "top_k": 1,
		 "top_p": 50
	},
        "inputs": get_question(level),
                })
    
    print(query({
                "parameters": {
		 "top_k": 1,
		 "top_p": 50
	},
                "inputs": "The role-playing is started, please start asking me question.",
                }))
    
    stdin = str(input("USER INPUT: "))
    
    while flag:
        if stdin == "":
            flag = False
            print("Game stop")
            break

        print(query({
              "parameters": {
		 "top_k": 1,
		 "top_p": 50
	},
              "inputs": stdin,
                        }))
        
        if level_up:
            query({
                "parameters": {
		 "top_k": 1,
		 "top_p": 50
	},
                "inputs": get_question(level),
                })
            
        stdin = str(input("INPUT: "))

    #     new_level = query({
    #         "parameters": {
	# 	 "top_k": 1,
	# 	 "top_p": 50
	# },
    #         "inputs": "Please tell me the current level in one single number (e.g. 1)"
    #     })

    #     if new_level > level:
    #         level_up = True
    #         level = new_level
    #     else:
    #         level_up = False


if __name__ == "__main__":
    main()
