import urllib.request

# data = urllib.request.urlopen("https://drchrono.com/onpatient_api/fhir/Patient").read()

data = urllib.request.urlopen("https://onpatient.com/athorize")

print(data)
