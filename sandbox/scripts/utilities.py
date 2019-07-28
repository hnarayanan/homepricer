import pandas as pd


def read_property_transactions(file_path="../../data/pp-complete.csv"):
    property_transactions = pd.read_csv(
        file_path,
        header=None,
        names=[
            "transaction_id",
            "transaction_price",
            "transaction_transfer_date",
            "property_postcode",
            "property_type",
            "property_age",
            "property_duration",
            "property_paon",
            "property_saon",
            "property_street",
            "property_locality",
            "property_town_or_city",
            "property_district",
            "property_county",
            "transaction_category",
            "_record_type",
        ],
        parse_dates=["transaction_transfer_date"],
    ).fillna("")
    # Remove the transactions that are not market price
    property_transactions = property_transactions[
        property_transactions["transaction_category"] == "A"
    ]
    return property_transactions


def read_postcode_locations(file_path="../../data/NSPL_FEB_2018_UK.csv"):
    postcode_locations = pd.read_csv(file_path).set_index(
        "pcds"
    )
    return postcode_locations


def read_wards(file_path="../../data/Ward names and codes UK as at 12_17.txt"):
    wards = pd.read_csv(
        file_path,
        sep="\t",
        encoding="latin-1",
    ).set_index("WD17CD")
    return wards


def read_property_transactions_for_ward(ward_name):
    property_transactions = read_property_transactions()
    postcode_locations = read_postcode_locations()
    wards = read_wards()
    ward = wards[wards["WD17NM"] == ward_name].index[0]
    ward_postcodes = postcode_locations[postcode_locations["ward"] == ward].index
    property_transactions_ward = property_transactions[
        property_transactions["property_postcode"].isin(ward_postcodes)
    ]
    return property_transactions_ward
