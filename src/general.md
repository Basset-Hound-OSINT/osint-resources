## Domains

- [Chiasmodon](https://github.com/chiasmod0n/chiasmodon)
  
```YAML
tool_info:
    name: chiasmodon
    type: serverside
    git_url: https://github.com/chiasmod0n/chiasmodon
    usage_url: https://github.com/chiasmod0n/chiasmodon/blob/main/README.md
tool_cmd:
    sudo: false
    cmd: chiasmodon_cli.py ${DOMAIN} -ot ${PROFILE}/logs/${tool_name}_${LOGID}_${timestamp}.log_${tool_name} | tee ${PROFILE}/logs/${tool_name}_${LOGID}_${timestamp}.log
    target_info: firstname, lastname
    target_info_opt: phonenumber, email
```

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

## Passwords 

- [Hashes.com](https://hashes.com)

```YAML
tool_info:
    name: hashes.com
    type: web
    base_url: https://hashes.com
    usage_url: https://hashes.com
tool_cmd:
    login: false
    js: window.open...
    target_info: fullname, phonenumber, firstname, lastname
    target_info_opt: dob, address, city, state, zipcode, linkedin, twitter
```

## Cloud / CDN

[CloakQuest3r](https://github.com/spyboy-productions/CloakQuest3r)

[CloudPeler](https://github.com/zidansec/CloudPeler)

[GhostTrack](https://github.com/HunxByts/GhostTrack)

[web-check](https://github.com/Lissy93/web-check)