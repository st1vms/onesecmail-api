<a href="https://www.buymeacoffee.com/st1vms"><img src="https://img.buymeacoffee.com/button-api/?text=1 Pizza Margherita&emoji=🍕&slug=st1vms&button_colour=0fa913&font_colour=ffffff&font_family=Bree&outline_colour=ffffff&coffee_colour=FFDD00" width="200" height="30" style="max-width:100%;"/></a>

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
