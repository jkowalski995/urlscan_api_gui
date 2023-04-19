from passivetotal import analyzer


def whois_an(domain=None):
    # TODO: Solve auto logging without command line commands
    """

    Before first run
    In terminal:

    $ pt-config setup <USERNAME>
    After being prompt provide API-KEY

    https://pypi.org/project/passivetotal/1.0.25/

    Same to do when running in PyCharm -> navigate to the Terminal at the bottom and configure the API-KEY

    Will connect with the RiskIQ API and return values from it. Already supported values are:
    host, registrant, registrar, IP, NS(s), and MX(s)
    :param domain: (string) a string url of scanned website with or without https://www.
    :return: (string) all information obtained from passivetotal
    """
    whois_record = ""

    analyzer.init()
    host = analyzer.Hostname(domain)

    try:
        registrant = host.whois.organization
    except Exception:
        registrant = ""

    whois_record = whois_record + "Analyzed host: " + str(host) + "\n"
    whois_record = whois_record + "Registrant: " + str(registrant) + "\n"

    try:
        registrar = analyzer.Hostname(domain).whois.registrar
    except Exception:
        registrar = ""

    whois_record = whois_record + "Registrar: " + str(registrar) + "\n"

    try:
        ip = analyzer.Hostname(domain).ip
    except Exception:
        ip = ""

    whois_record = whois_record + "IP: " + str(ip) + "\n"

    whois_record += "Nameserver(s): \n"
    try:
        for record in analyzer.Hostname(domain).whois.nameservers:
            whois_record += str(record)
            whois_record += "\n"
    except Exception:
        whois_record += ""
        whois_record += "\n"

    whois_record += "MX(s): \n"
    try:
        for record in analyzer.Hostname(domain).resolutions.only_hostnames.filter(recordtype='MX'):
            whois_record += str(record)
            whois_record += "\n"
    except Exception:
        whois_record += ""
        whois_record += "\n"
    # Host
    # print(f'host {host}')
    # Registrant
    # print(f'registrant {registrant}')
    # NS
    # for record in analyzer.Hostname('riskiq.net').whois.nameservers:
    #     print(f'Nameserver {record}')
    # Registrar
    # print(f"Registrar {analyzer.Hostname('riskiq.net').whois.registrar}")
    # IP
    # print(f"IP {analyzer.Hostname('riskiq.net').ip}")
    # MX
    # for record in analyzer.Hostname('riskiq.net').resolutions.only_hostnames.filter(recordtype = 'MX'):
    #     print(record)
    return whois_record
