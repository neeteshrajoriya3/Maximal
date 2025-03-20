project_id = "ABC123"
url = "/rest/api/3/project/{projectIdOrKey}/restore"
url = url.replace("{projectIdOrKey}", project_id)
print(url)