from ..typing import Headers, User_Agent, Dict

def get_headers(user_agent: User_Agent, content_length: int) -> Headers | Dict[str, str]:

    return {
        "POST": "/api/langchain/tool/agent/nodejs HTTP/3",
        "Host": "free.chatgpt.org.uk",
        "User-Agent": f"{user_agent}",
        "Accept": "application/json, text/event-stream",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Content-Length": f"{content_length}",
        "Referer": "https://free.chatgpt.org.uk/",
        "x-requested-with": "XMLHttpRequest",
        "Origin": "https://free.chatgpt.org.uk",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Connection": "keep-alive",
        "Alt-Used": "free.chatgpt.org.uk",
        "TE": "trailers"
}