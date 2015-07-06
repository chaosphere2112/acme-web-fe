import requests
from django.core.exceptions import ValidationError
from urlparse import urlparse


def validate_source_type(value):
    if value in ("jira", "github"):
        return
    else:
        raise ValidationError("Source Type %(value)s not implemented.", params={"value": value})


def validate_github_api_url(value):
	# Ping the API and see if it comes back as a 200
	try:
		response = requests.head(value)
		if response.status != 200:
			raise Exception()
	except Exception:
		raise ValidationError("Unable to reach GitHub URL %(value)s", params={"value": value})


def validate_jira_api_url(value):
	# This *should* ping the API for a 200
	# Instead, we're just going to check if it's on acme-climate.atlassian.net
	parts = urlparse(value)
	if parts.hostname != "acme-climate.atlassian.net":
		raise ValidationError("Unrecognized JIRA URL %(value)s", params={"value": value})
