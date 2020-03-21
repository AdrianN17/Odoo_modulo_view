{
	'name' : 'Bodega',
	'version' : "13.0.1.0.0",
	'category' : 'Extra Tools',
	'author' : 'Adrian',
	'website' : 'adrian.com',
	'license' : 'AGPL-3',
	'summary' : 'Bodega Management Software',
	'description' : "***Module to Manage Bodega***",
	'depends' : ['base','mail'],
	'data' : [
		'security/ir.model.access.csv',
		'views/bodega.xml'
	],
	'demo' : [],
	'qweb' : [],
	'installable' : True,
	'application' : True,
	'auto_install' : False
}