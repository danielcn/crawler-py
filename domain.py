from urlparse import urlparse

# Get domein name (exaple,com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

#Get sub domein name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except Exception as e:
        return ''

print(get_domain_name('https://thenewboston.com/index.pho'))
