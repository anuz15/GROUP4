import socket
import requests
import google.generativeai as genai

API_URL = "https://api-inference.huggingface.co/models/thennal/whisper-medium-ml"
HUGGING_FACE_API_KEY = "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"
headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("recorded_audio.wav")
print(output['text'])

GEMINI_API_KEY = "AIzaSyBOhZ2W2X3w_GsugIaRO2DfkndiNCHxoNg"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

PROMPT = '''
ഇടത്യാനെ 	TURN_LEFT
വലത്യാനെ 	TURN_RIGHT
നാടയാനെ 	WALK_FORWARD
സെറ്റാനെ 	WALK_BACKWARD
നില്ലാനെ 	STOP
കിടന്നാനെ 	LIE_DOWN
ഇരിയാനെ 	SIT
ഊന്നാനെ 	LOCK_THE_FOOT_FIRMLY_ON_LAND
ഭീരിയാനെ 	POUR_WATER_WITH_THE_TRUNK
ഊന്നാനെ 	BEND_DOWN_AND_GET_THE_LEAVES
താങ്ങാനെ 	LIFT_LEAVES_WITH_THE_TRUNK
ആശിർവദിക്കാനെ 	GIVE_ASHIRVAD_WITH_THE_TRUNK
ചെവിയാട്ടാനെ	MOVE_EARS
തലയാട്ട്ട്ടാനെ 	MOVE_HEAD
കാല് പോക്കാനെ 	LIFT_ONE_BACK_LEG
കണ്ണ് അടക്കാനെ 	CLOSE_EYES

The above is malayalam and its corresponding command. 
I transcribed a real-time audio into this malayalam word. 
Give me the most closely related command for that in the 
JSON format {"command":"command_here"} returned in the JSON.
Text is 
'''

response = model.generate_content(f"{PROMPT} {output['text']}")
data = response.text

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4455

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))

    while True:
        data, addr = server.recvfrom(1024)
        data = data.decode("utf-8")
        s = data

        print(f"client: {data}")

        def query(filename):
            with open(filename, "rb") as f:
                data = f.read()
            response = requests.post(API_URL, headers=headers, data=data)
            return response.json()

        output = query("recorded_audio.wav")

        GEMINI_API_KEY = "AIzaSyBOhZ2W2X3w_GsugIaRO2DfkndiNCHxoNg"
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-pro')

        PROMPT = '''
        ഇടത്യാനെ 	TURN_LEFT
        വലത്യാനെ 	TURN_RIGHT
        നാടയാനെ 	WALK_FORWARD
        സെറ്റാനെ 	WALK_BACKWARD
        നില്ലാനെ 	STOP
        കിടന്നാനെ 	LIE_DOWN
        ഇരിയാനെ 	SIT
        ഊന്നാനെ 	LOCK_THE_FOOT_FIRMLY_ON_LAND
        ഭീരിയാനെ 	POUR_WATER_WITH_THE_TRUNK
        ഊന്നാനെ 	BEND_DOWN_AND_GET_THE_LEAVES
        താങ്ങാനെ 	LIFT_LEAVES_WITH_THE_TRUNK
        ആശിർവദിക്കാനെ 	GIVE_ASHIRVAD_WITH_THE_TRUNK
        ചെവിയാട്ടാനെ	MOVE_EARS
        തലയാട്ട്ട്ടാനെ 	MOVE_HEAD
        കാല് പോക്കാനെ 	LIFT_ONE_BACK_LEG
        കണ്ണ് അടക്കാനെ 	CLOSE_EYES

        The above is malayalam and its corresponding command. 
        I transcribed a real-time audio into this malayalam word. 
        Give me the most closely related command for that in the 
        JSON format {"command":"command_here"} returned in the JSON.
        Text is 
        '''

        response = model.generate_content(f"{PROMPT} {output['text']}")
        data = response.text

        print(response.text)

        server.sendto(data.encode("utf-8"), addr)
