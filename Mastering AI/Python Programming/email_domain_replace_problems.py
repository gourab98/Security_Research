def domain_replace(email, old_domain, new_domain):
    if "@"+old_domain in email:
        index = email.index("@"+old_domain)
        new_email = email[:index]+ "@" +new_domain
        return new_email
    return email

print(domain_replace("gourabsahag@gmail.com", "@gmail.com", "@student.edu"))
