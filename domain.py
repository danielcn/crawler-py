from urllib import parse

# Get domein name (exaple,com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except Exception as exception:
        return exception

#Get sub domein name (name.example.com)
def get_sub_domain_name(url):
    try:
        return parse(url).netloc
    except Exception as exception:
        return exception

print(get_domain_name('https://thenewboston.com/index.pho'))
