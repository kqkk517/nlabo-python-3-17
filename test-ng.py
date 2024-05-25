import pandas as pd
from dateutil.relativedelta import relativedelta

nlabo_customer = pd.read_csv("nlabo_customer_master.csv")

nlabo_exit_customer = nlabo_customer.loc[nlabo_customer["is_deleted"] == 1]
# nlabo_exit_customer = nlabo_customer.loc[nlabo_customer["is_deleted"] == 1].copy()  # SettingWithCopyWarning回避のためcopyが必要

nlabo_exit_customer["exit_date"] = None  # SettingWithCopyWarning
nlabo_exit_customer["end_date"] = pd.to_datetime(nlabo_exit_customer["end_date"])

for i in range(len(nlabo_exit_customer)):
    nlabo_exit_customer["exit_date"].iloc[i] = nlabo_exit_customer["end_date"].iloc[i] - relativedelta(
        months=1
    )  # SettingWithCopyWarning

# 以下で回避できるが、nlabo_exit_customer["exit_date"]をdatetime型で認識してくれない
# そもそもfor文で書き換えるのが推奨されない
# nlabo_exit_customer.reset_index(drop=True, inplace=True)
# for i in range(len(nlabo_exit_customer)):
# nlabo_exit_customer.at[i, "exit_date"] = nlabo_exit_customer.at[i, "end_date"] - relativedelta(months=1)

nlabo_exit_customer["年月"] = nlabo_exit_customer["exit_date"].dt.strftime("%Y%m")  # AttributeError

print(nlabo_exit_customer)
