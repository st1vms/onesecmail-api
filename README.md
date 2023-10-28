# 1secmail unofficial API

This is an unofficial wrapper for 1secmail API.

It provides:

- `MailBoxMessage`, `MailMessage`, and `MailAttachment` convience dataclasses.

- **Wrapper** methods for:
    - Getting list of 1secmail active domains -> `get_domain_list`
    - Generating random emails -> `gen_random_emails`
    - Fetching mailbox for an email -> `fetch_mailbox`
    - Fetching a message out of an email -> `fetch_msg`
    - Downloading file attachments from email messages: `download_attachment`


# How to install
```
pip install onesecmail-api
```

# How to import

Import this library with:
```py
import onesecmail_api
```
or just some individual components with:
```py
from onesecmail_api import (
    MailBoxMessage,
    MailAttachment,
    MailMessage,
    get_domain_list,
    gen_random_emails,
    fetch_mailbox,
    fetch_msg,
    download_attachment,
)
```