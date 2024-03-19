class adwords:
	"""
	python-representation of adwords
	"""

	# Access
	access = {"delete_custom":""
		,"delete_deny":[""
			,""
			,""]
		,"insert_custom":"{$}"
		,"insert_deny":[""
			,""
			,""]}

	# Enabled
	enabled = 1

	# Id
	id = "adwords"

	# Name
	name = "Adwords (Toptreffer)"

	# Package
	package = "com.zms.catalog.opensearch"

	# Revision
	revision = "0.0.3"

	# Type
	type = "ZMSRecordSet"

	# Attrs
	class Attrs:
		records = {"default":""
			,"id":"records"
			,"keys":[]
			,"mandatory":1
			,"multilang":0
			,"name":"Datensätze"
			,"repetitive":0
			,"type":"list"}

		grid = {"default":"1"
			,"id":"_grid"
			,"keys":[]
			,"mandatory":1
			,"multilang":0
			,"name":"Grid?"
			,"repetitive":0
			,"type":"boolean"}

		col_id = {"default":""
			,"id":"col_id"
			,"keys":[]
			,"mandatory":1
			,"multilang":0
			,"name":"COL_ID"
			,"repetitive":0
			,"type":"identifier"}

		adword = {"custom":1
			,"default":""
			,"id":"adword"
			,"keys":[]
			,"mandatory":1
			,"multilang":0
			,"name":"Adword"
			,"repetitive":0
			,"type":"string"}

		url = {"custom":1
			,"default":""
			,"id":"url"
			,"keys":[]
			,"mandatory":1
			,"multilang":0
			,"name":"URL"
			,"repetitive":0
			,"type":"url"}

		synonyms = {"default":""
			,"id":"synonyms"
			,"keys":[]
			,"mandatory":0
			,"multilang":0
			,"name":"Synonyms (space-sep.)"
			,"repetitive":0
			,"type":"string"}

		category = {"default":""
			,"id":"category"
			,"keys":["##"
				,"return ["
				,"  ('person','Person'),"
				,"  ('news','News'),"
				,"  ('study','Studium'),"
				,"  ('event','Veranstaltung'),"
				,"  ('tip','Tipp')"
				,"]"]
			,"mandatory":0
			,"multilang":0
			,"name":"Category"
			,"repetitive":0
			,"type":"select"}

		icon_clazz = {"custom":"far fa-list-alt text-danger"
			,"default":""
			,"id":"icon_clazz"
			,"keys":[]
			,"mandatory":0
			,"multilang":0
			,"name":"Icon-Class (CSS)"
			,"repetitive":0
			,"type":"constant"}

		get_targets = {"default":""
			,"id":"get_targets"
			,"keys":[]
			,"mandatory":0
			,"multilang":0
			,"name":"Get targets by keyword as dict"
			,"repetitive":0
			,"type":"py"}

		get_targets_json = {"default":""
			,"id":"get_targets_json"
			,"keys":[]
			,"mandatory":0
			,"multilang":0
			,"name":"REST-Interface: Return targets as JSON"
			,"repetitive":0
			,"type":"Script (Python)"}

		standard_html = {"default":""
			,"id":"standard_html"
			,"keys":[]
			,"mandatory":0
			,"multilang":0
			,"name":"Template: Adwords (Toptreffer)"
			,"repetitive":0
			,"type":"zpt"}
