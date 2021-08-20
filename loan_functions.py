# Functions
def start_pipeline(dataf):
    return dataf.copy()


def clean_dataset(dataf):
    dataf.columns = [c.replace(" ", "") for c in dataf]
    return dataf


def delete_cols(dataf, columns_to_delete):
    return dataf.drop(columns_to_delete, axis=1)


def convert_to_date(dataf, columns_to_date):
    dataf[columns_to_date] = dataf[columns_to_date].astype("datetime64")
    return dataf
