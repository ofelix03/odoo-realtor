# odoo-realtor
A basic odoo module to demonstrate two implementations of sending emails in Odoo.
Both implementations are functional but one is preferrable and recommended over the other.

## #1 Poor Implementation
This implementation is considered poor and must be avoided. 
It's functional yet considered poorly implemented because of the following reasons

1. Uses directly the `mail.mail` to send the email
2. Manually udpates the `body_html` field on the `mail.template` with the dynamic information it requires
3. Static information about the email including sender email address, email subject, recipient email address
are passed to the `mail.mail` instead of declaratively in the `mail.template`

## #2 Ideal Implementation
This implementation in constrast with  the poor implementation above employs the delegation pattern.
It focuses on the mail template without caring about the mechanism the `mail.mail` model uses to send the 
email.

This implementation is ideal for the following reasons:
1. All the static and dynamic information required by the `mail.template` are all
defined in the template
2. The template as direct access to the record and therefore access the required static and 
dynamic information it requires to build the email template

