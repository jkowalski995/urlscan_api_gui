import pdb
from passivetotal import analyzer

def init_analyzer(domain):
    analyzer.init()
    analyzer.set_date_range(days_back=30)
    pt_object = analyzer.Hostname('atos.net')
    return pt_object

# pdns = pt_object.ip.resolutions
# for record in pdns.sorted_by('lastseen'):
#     print(record)

# print('------')
# whois = pt_object.whois
# print()
# age = pt_object.whois.age  # e.g. 5548
# print(age)
# pdb.set_trace()


#A "staging-api.passivetotal.org" [ 465 days] (2019-12-11 to 2021-03-21)
#A "api.passivetotal.org" [ 459 days] (2019-12-18 to 2021-03-22)