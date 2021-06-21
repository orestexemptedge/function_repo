
# this function sanitizes phone numbers and appends any digits beyond 10 to a separate column
def phone_split(df, phone='phone', main='phone_main', ext='phone_ext'):
    df[phone].replace(to_replace='[^0-9]+', value='', inplace=True, regex=True)
    df[main] = df[phone].str[:10]
    df[ext] = df[phone].str[11:]
    df.drop(phone, axis=1, inplace=True)

