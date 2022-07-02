
from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def index():
    output = "Output of your code will be shown here"
    code = ""
    if request.method == 'POST':
        output = run_code(request.form.get("code"))
        code = request.form.get("code")

    return render_template('index.html', result = output, code = code)


def run_code(code):
    print("old: " + code)
    output = ""
    try:
        code = code.replace("\r\n", " ")
        commands = code.split(" ")
        now_command_id = 0
        x = 0
        y = 0
        while True:
            if commands[now_command_id] == "KwA":
                x += 1
                print("x+1")
            elif commands[now_command_id] == "Kwa":
                x -= 1
                print("x-1")
            elif commands[now_command_id] == "kwA":
                y += 1
                print("y+1")
            elif commands[now_command_id] == "kwa":
                y -= 1
                print("y-1")
            elif commands[now_command_id] == "Kwaa":
                print("OUT +: " + str(x))
                output += chr(x)
            elif commands[now_command_id] == "KWA":
                x = x**2
                print("x**2")
            elif commands[now_command_id] == "KWAA":
                y = y**2
                print("y**2")
            elif commands[now_command_id] == "Kwaaa":
                print("OUT +: " + str(y))
                output += chr(y)




            if commands[now_command_id] == "kWa":
                if x < y:
                    now_command_id -= 4

            now_command_id += 1


            if now_command_id >= len(commands):
                print("END")
                break




    except Exception:
        output += " <Error>"

    if output == "":
        output = "<This program did not output anything to the console>"
    return output



if __name__ == "__main__":
    app.run()