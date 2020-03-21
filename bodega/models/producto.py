from odoo import fields, models

class BodegaProducto(models.Model):
    _name = "bodega.producto"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Item de bodega"

    name = fields.Char(string="Nombre Producto", required=True)
    precio_unitario = fields.Float(string="Precio Unitario", required=True)
    cantidad = fields.Integer(string="Cantidad", required=True)

    categoria_producto = fields.Selection([
        ("verduras","Verduras"),
        ("frutas","Frutas"),
        ("carnes","Carnes"),
        ("pescados","Pescados"),
        ("lacteos","Lacteos"),
        ("bebida","Bebidas"),
        ("dulces","Dulces")
    ],string = "Tipo de producto", default="verduras")

    perecible = fields.Boolean(string="Es perecible?", required=True)

    fecha = fields.Datetime(string = "Fecha de Comprado")

    proveedor = fields.Char(string = "Proveedor")

