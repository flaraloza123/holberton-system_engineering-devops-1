from datadog import initialize, api

options = {
    'api_key': '7f8d10748f7d57f18943238d70cd6331',
    'app_key': '6e1602a90729cb13affe001dde804b7445f63805'
}

initialize(**options)

print(api.Dashboard.get_all())
