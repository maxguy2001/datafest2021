import pandas as pd

stop_search_list_03 = ["2018-03-avon-and-somerset-stop-and-search.csv",
                       "2018-03-bedfordshire-stop-and-search",
                       "2018-03-btp-stop-and-search",
                       "2018-03-cambridgeshire-stop-and-search",
                       "2018-03-cheshire-stop-and-search",
                       "2018-03-city-of-london-stop-and-search",
                       "2018-03-cleveland-stop-and-search",
                       "2018-03-cumbria-stop-and-search",
                       "2018-03-derbyshire-stop-and-search",
                       "2018-03-bedfordshire-stop-and-search",
                       "2018-03-devon-and-cornwall-stop-and-search",
                       "2018-03-dorset-stop-and-search",
                       "2018-03-durham-stop-and-search",
                       "2018-03-dyfed-powys-stop-and-search",
                       "2018-03-essex-stop-and-search",
                       "2018-03-gloucestershire-stop-and-search",
                       "2018-03-greater-manchester-stop-and-search",
                       "2018-03-gwent-stop-and-search",
                       "2018-03-hampshire-stop-and-search",
                       "2018-03-hertfordshire-stop-and-search",
                       "2018-03-humberside-stop-and-search",
                       "2018-03-kent-stop-and-search",
                       "2018-03-lancashire-stop-and-search",
                       "2018-03-leicestershire-stop-and-search",
                       "2018-03-lincolnshire-stop-and-search",
                       "2018-03-merseyside-stop-and-search",
                       "2018-03-metropolitan-stop-and-search",
                       "2018-03-norfolk-stop-and-search",
                       "2018-03-northamptonshire-stop-and-search",
                       "2018-03-northumbria-stop-and-search",
                       "2018-03-north-wales-stop-and-search",
                       "2018-03-north-yorkshire-stop-and-search",
                       "2018-03-nottinghamshire-stop-and-search",
                       "2018-03-south-wales-stop-and-search",
                       "2018-03-south-yorkshire-stop-and-search",
                       "2018-03-staffordshire-stop-and-search",
                       "2018-03-suffolk-stop-and-search",
                       "2018-03-surrey-stop-and-search",
                       "2018-03-sussex-stop-and-search",
                       "2018-03-thames-valley-stop-and-search",
                       "2018-03-warwickshire-stop-and-search",
                       "2018-03-west-mercia-stop-and-search",
                       "2018-03-west-midlands-stop-and-search",
                       "2018-03-west-yorkshire-stop-and-search",
                       "2018-03-wiltshire-stop-and-search"]

stop_search_list_04 = ["2018-04-avon-and-somerset-stop-and-search",
                       "2018-04-bedfordshire-stop-and-search",
                       "2018-04-btp-stop-and-search",
                       "2018-04-cambridgeshire-stop-and-search",
                       "2018-04-cheshire-stop-and-search",
                       "2018-04-city-of-london-stop-and-search",
                       "2018-04-cleveland-stop-and-search",
                       "2018-04-cumbria-stop-and-search",
                       "2018-04-derbyshire-stop-and-search",
                       "2018-04-bedfordshire-stop-and-search",
                       "2018-04-devon-and-cornwall-stop-and-search",
                       "2018-04-dorset-stop-and-search",
                       "2018-04-durham-stop-and-search",
                       "2018-04-dyfed-powys-stop-and-search",
                       "2018-04-essex-stop-and-search",
                       "2018-04-gloucestershire-stop-and-search",
                       "2018-04-greater-manchester-stop-and-search",
                       "2018-04-gwent-stop-and-search",
                       "2018-04-hampshire-stop-and-search",
                       "2018-04-hertfordshire-stop-and-search",
                       "2018-04-humberside-stop-and-search",
                       "2018-04-kent-stop-and-search",
                       "2018-04-lancashire-stop-and-search",
                       "2018-04-leicestershire-stop-and-search",
                       "2018-04-lincolnshire-stop-and-search",
                       "2018-04-merseyside-stop-and-search",
                       "2018-04-metropolitan-stop-and-search",
                       "2018-04-norfolk-stop-and-search",
                       "2018-04-northamptonshire-stop-and-search",
                       "2018-04-northumbria-stop-and-search",
                       "2018-04-north-wales-stop-and-search",
                       "2018-04-north-yorkshire-stop-and-search",
                       "2018-04-nottinghamshire-stop-and-search",
                       "2018-04-south-wales-stop-and-search",
                       "2018-04-south-yorkshire-stop-and-search",
                       "2018-04-staffordshire-stop-and-search",
                       "2018-04-suffolk-stop-and-search",
                       "2018-04-surrey-stop-and-search",
                       "2018-04-sussex-stop-and-search",
                       "2018-04-thames-valley-stop-and-search",
                       "2018-04-warwickshire-stop-and-search",
                       "2018-04-west-mercia-stop-and-search",
                       "2018-04-west-midlands-stop-and-search",
                       "2018-04-west-yorkshire-stop-and-search",
                       "2018-04-wiltshire-stop-and-search"]

df = pd.read_csv(f"data/crime-data/2018-03/{stop_search_list_03[0]}")

for i in range(1, len(stop_search_list_03)):
    new_df = pd.read_csv(f"data/crime-data/2018-03/{stop_search_list_03[i]}.csv")
    df = df.append(new_df)

for i in range(len(stop_search_list_03)):
    new_df = pd.read_csv(f"data/crime-data/2018-04/{stop_search_list_04[i]}.csv")
    df = df.append(new_df)

notnan = df[df["Longitude"].notna()]
drugstops = notnan[notnan["Object of search"].isin(["Controlled drugs"])]
#print(len(drugstops))
#drugstops.to_csv("data/drugstops_uk.csv")




