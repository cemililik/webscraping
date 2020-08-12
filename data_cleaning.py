# numpy__version__ : 1.18.1
import numpy as np
# pandas__version__ : 1.0.4
import pandas as pd
# json__version__ : 2.0.9 
import json


# ### V1: Drop duplicated values

companies = pd.read_csv("Companies.csv")

## drop duplicates considering all columns
companies_v2 = companies.drop_duplicates()
companies_v2.to_csv("Companies_v2.csv", index=False)

## drop duplicates by column: Title
companies_v3 = companies_v2.drop_duplicates("Title")
companies_v3.to_csv("Companies_v3.csv", index=False)


# ## V2: Get Company Informations
comp3 = pd.read_csv("CompanyDetails3.csv")

comp3["Title_Clean"] = comp3.Title.apply(lambda t: " ".join(t.split("\n")[1:-1]).strip())
comp3["Title_Dict"] = comp3.Title_Clean.apply(lambda t: json.loads(t) if t != "" else np.NaN)

comp3 = comp3.dropna()

features = ["MainCategory", "Name", "Telephone", "Address", "City", "State", "ZipCode", "Country", "Lat", "Long", "Description", "Url", "Image", "AreaServed", "OfferCatalog"]

for feature in features:
    comp3[feature] = np.NaN


comp3["Name"]      = comp3.Title_Dict.apply(lambda t: t[0]["name"])
comp3["Telephone"] = comp3.Title_Dict.apply(lambda t: t[0]["telephone"] if "telephone" in t[0].keys() else np.NaN)
comp3["Url"]       = comp3.Title_Dict.apply(lambda t: t[0]["url"] if "url" in t[0].keys() else np.NaN)
comp3["Image"]     = comp3.Title_Dict.apply(lambda t: t[0]["image"] if "image" in t[0].keys() else np.NaN)

## Address//
comp3["Address"]  = comp3.Title_Dict.apply(lambda t: t[0]["address"]["streetAddress"] if "address" in t[0].keys() else np.NaN)
comp3["City"]     = comp3.Title_Dict.apply(lambda t: t[0]["address"]["addressLocality"] if "address" in t[0].keys() else np.NaN)
comp3["State"]    = comp3.Title_Dict.apply(lambda t: t[0]["address"]["addressRegion"] if "address" in t[0].keys() else np.NaN)
comp3["ZipCode"]  = comp3.Title_Dict.apply(lambda t: t[0]["address"]["postalCode"] if "address" in t[0].keys() else np.NaN)
comp3["Country"]  = comp3.Title_Dict.apply(lambda t: t[0]["address"]["addressCountry"] if "address" in t[0].keys() else np.NaN)

## Coordinates
comp3["Lat"]      = comp3.Title_Dict.apply(lambda t: t[0]["geo"]["latitude"] if "geo" in t[0].keys() else np.NaN)
comp3["Long"]     = comp3.Title_Dict.apply(lambda t: t[0]["geo"]["longitude"] if "geo" in t[0].keys() else np.NaN)

comp3["AreaServed"]   = comp3.Title_Dict.apply(lambda t: t[0]["areaServed"]["name"] if "areaServed" in t[0].keys() else np.NaN)
comp3["OfferCatalog"] = comp3.Title_Dict.apply(lambda t: t[0]["hasOfferCatalog"]["name"] if "hasOfferCatalog" in t[0].keys() else np.NaN)
comp3["Description"]  = comp3.Title_Dict.apply(lambda t: t[0]["description"] if "description" in t[0].keys() else np.NaN)

comp3["MainCategory"]  = comp3.Title_Dict.apply(lambda t: t[1]["itemListElement"][0]["item"]["name"])



compdet4 = comp3[["Category"] + features]
compdet4.to_csv("CompanyDetails4.csv", index=False)
