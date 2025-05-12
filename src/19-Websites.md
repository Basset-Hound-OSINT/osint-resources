## Domains

- [Chiasmodon](https://github.com/chiasmod0n/chiasmodon)
  
```YAML
- tool_info: 
  - name: chiasmodon
  - type: serverside
  - git_url: https://github.com/chiasmod0n/chiasmodon
  - usage_url: https://github.com/chiasmod0n/chiasmodon/blob/main/README.md
- tool_cmd:
  - sudo: false
  - cmd: chiasmodon_cli.py ${DOMAIN} -ot ${PROFILE}/logs/${tool_name}_${LOGID}_${timestamp}.log_${tool_name} | tee ${PROFILE}/logs/${tool_name}_${LOGID}_${timestamp}.log
  - target_info: firstname, lastname
  - target_info_opt: phonenumber, email
```