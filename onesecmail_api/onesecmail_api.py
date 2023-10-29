"""1secmail disposable email manager"""
from dataclasses import dataclass
from datetime import datetime
from requests import get as http_get


@dataclass(frozen=True)
class MailBoxMessage:
    """Dataclass holding a message from getMessages results"""

    msg_id: int
    from_addr: str
    subject: str
    date: datetime


@dataclass(frozen=True)
class MailAttachment:
    """Dataclass holding message attachment data"""

    filename: str
    content_type: str
    size: int


@dataclass(frozen=True)
class MailMessage:
    """Dataclass holding a message from readMessage results"""

    msg_id: int
    from_addr: str
    subject: str
    date: datetime
    attachments: list[MailAttachment]
    body: str
    text_body: str
    html_body: str


__BASE_URL = "https://www.1secmail.com/api/v1/"


def get_domain_list() -> list[str]:
    """Retrieves 1secmail domain list"""
    endpoint = "?action=getDomainList"
    return http_get(__BASE_URL + endpoint, timeout=2).json()


def gen_random_emails(count: int = 1, domain: str = None) -> list[str]:
    """Generate random emails, use `count` argument to change number of emails generated.

    Use `domain` argument to override generated email domain"""

    if count <= 0:
        return ValueError("'count' must be positive")
    endpoint = f"?action=genRandomMailbox&count={count}"
    res = http_get(__BASE_URL + endpoint, timeout=2).json()
    if not res:
        return []
    if not domain:
        return res
    return list(map(lambda e: e.split("@", maxsplit=1)[0] + f"@{domain}", res))


def fetch_mailbox(email: str) -> list[MailBoxMessage] | None:
    """Returns incoming messages for an email"""
    user, domain = email.split("@", maxsplit=1)
    endpoint = f"?action=getMessages&login={user}&domain={domain}"
    res = http_get(__BASE_URL + endpoint, timeout=2).json()
    if not res:
        return None
    return [MailBoxMessage(j["id"], j["from"], j["subject"], j["date"]) for j in res]


def fetch_msg(email: str, msg_id: int) -> MailMessage | None:
    """Fetch email message by numeric ID"""
    user, domain = email.split("@", maxsplit=1)
    endpoint = f"?action=readMessage&login={user}&domain={domain}&id={msg_id}"
    j = http_get(__BASE_URL + endpoint, timeout=2).json()
    if not j:
        return None
    return MailMessage(
        j["id"],
        j["from"],
        j["subject"],
        j["date"],
        j["attachments"],
        j["body"],
        j["textBody"],
        j["htmlBody"],
    )


def download_attachment(email: str, msg_id: int, filename: str) -> bytes:
    """Download file attachment from mail message"""
    user, domain = email.split("@", maxsplit=1)
    endpoint = (
        f"?action=download&login={user}&domain={domain}&id={msg_id}&file={filename}"
    )
    return http_get(__BASE_URL + endpoint, timeout=10).content
