from mymodules import discord_alert, jsonlog

def load_txt(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        data = f.read().splitlines()[0]
    return data

def disco_md():
    webhook = load_txt("webhook_url")

    messages = """
    # title

    - testmarkdown
        - hoge
        - foo
    """

    discord_alert.discord_messages(webhook, messages)



def main():
    # disco_md()
    data = {
        "score": 123,
        "recall": 567
    }
    jsonlog("test.json", data)


if __name__=="__main__":
    main()
