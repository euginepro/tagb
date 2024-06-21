import json

badc = 0
goodc = 0


def save(oc):
    with open("okcookies.json", 'w') as file:
        json.dump(oc, file, indent=4)


with open("zcookies.json", 'r') as c:
    with open("okcookies.json", 'r') as o:
        oc = []
        zc = json.load(c)
        for cookie in zc:
            if ("googleadservices" in str(cookie["domain"])) or ("doubleclick.net" in str(cookie["domain"])) or (
                    "googleadservices" in str(cookie["domain"])):
                badc += 1
            else:
                goodc += 1
                oc.append(cookie)
        save(oc)
        print(f'goodc: {goodc}')
        print(f'badc: {badc}')
