import GetAnnounce, MessageSender, Logger, ProcessText, time

global APIKEY, Province

APIKEY = "x5Pza5ihMyZCkFpW28D6KY"
Province = "内蒙古" # get by shortname, if want details go to that website


def main():
    l = Logger.Logger("")
    methodFlag = True
    while methodFlag:
        l.info("开始接收消息。")
        m = MessageSender.MessageSender("bark")
        l.notice("APIKEY:" + APIKEY)
        m.config({'apikey': APIKEY})
        methodFlag = False
    l.info("请选择日志输出方式（默认控制台）:")
    l.info("1. 控制台")
    l.info("2. 文件announcebot.log")
    l.notice("请输入：")
    userInput = int(input())
    if userInput == 2:
        l.setMethod("file")
    g = GetAnnounce.GetAnnounce("", l)

    g.createCache()
    cache = g.get()
    for i in cache:
        p = ProcessText.ProcessText(i)
        if m.getMethod() == "serverchan":
            l.notice(m.send(p.getFullTextMD()))
        elif m.getMethod() == "smtp":
            l.notice(m.send(p.getFullText()))
        elif m.getMethod() == "console":
            l.notice(m.send(p.getNormalText()))
        elif m.getMethod() == "bark":
            l.notice(m.send(p.getSimpleText()))
        time.sleep(1)
    while True:
        cache = g.freshCache()
        if cache != None:
            for i in cache:
                p = ProcessText.ProcessText(i)
                l.notice(m.getMethod())
                if m.getMethod() == "serverchan":
                    l.notice(m.send(p.getFullTextMD()))
                elif m.getMethod() == "smtp":
                    l.notice(m.send(p.getFullText()))
                elif m.getMethod() == "console":
                    l.notice(m.send(p.getNormalText()))
                elif m.getMethod() == "bark":
                    l.notice(m.send(p.getSimpleText()))
                time.sleep(1)
        # 休息5分钟
        l.info("5分钟后重试")
        time.sleep(300)

main()
