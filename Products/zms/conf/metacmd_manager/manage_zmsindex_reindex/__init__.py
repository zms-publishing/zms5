class manage_zmsindex_reindex:
	"""
	python-representation of manage_zmsindex_reindex
	"""

	# Acquired
	acquired = 0

	# Action
	action = "%smanage_executeMetacmd?id=manage_zmsindex_reindex"

	# Description
	description = ""

	# Execution
	execution = False

	# Icon_clazz
	icon_clazz = "fas fa-cogs"

	# Id
	id = "manage_zmsindex_reindex"

	# Meta_types
	meta_types = ["ZMS"]

	# Name
	name = "Re-Index All Clients"

	# Nodes
	nodes = "{$}"

	# Package
	package = "com.zms.index"

	# Revision
	revision = "3.2.1"

	# Roles
	roles = ["ZMSAdministrator"]

	# Stereotype
	stereotype = ""

	# Title
	title = "Full Multisite-Reindexing in customisable increments"

	# Impl
	class Impl:
		manage_zmsindex_reindex = {"id":"manage_zmsindex_reindex"
			,"type":"External Method"}
