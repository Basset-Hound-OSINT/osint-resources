## Email Addresses

- [Have I Been Pwned](https://haveibeenpwned.com/)

```YAML
tool_info: 
    name: haveibeenpwned
    type: web
    base_url: https://haveibeenpwned.com/
    usage_url: https://haveibeenpwned.com/
tool_cmd:
    login: false
    target_info: email
    fields: 
        'input#AccountCheck_Account': 'test@example.com'
```