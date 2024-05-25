import pandas as pd

nlabo_customer = pd.read_csv("nlabo_customer_master.csv")

nlabo_exit_customer = nlabo_customer.loc[nlabo_customer["is_deleted"] == 1].copy()
nlabo_exit_customer["exit_date"] = None
nlabo_exit_customer["end_date"] = pd.to_datetime(nlabo_exit_customer["end_date"])
nlabo_exit_customer["exit_date"] = nlabo_exit_customer["end_date"] - pd.DateOffset(months=1)
nlabo_exit_customer["年月"] = nlabo_exit_customer["exit_date"].dt.strftime("%Y%m")

print(nlabo_exit_customer)
