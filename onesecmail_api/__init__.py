"""onesecmail_api"""

from .onesecmail_api import (
    MailBoxMessage,
    MailAttachment,
    MailMessage,
    get_domain_list,
    gen_random_emails,
    fetch_mailbox,
    fetch_msg,
    download_attachment,
)

__all__ = [
    "MailBoxMessage",
    "MailAttachment",
    "MailMessage",
    "get_domain_list",
    "gen_random_emails",
    "fetch_mailbox",
    "fetch_msg",
    "download_attachment",
]
