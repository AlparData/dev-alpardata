{
    'name': 'Reparación de Fecha IVA (Studio)',
    'version': '1.0',
    'author': 'Sebastian Ríos & Alpardata',
    'summary': 'Modifica el reporte de IVA para usar el campo x_studio_vat_date',
    'description': """
        Este módulo hace dos cosas:
        1. Modifica el reporte 'account.ar.vat.line' para que use el campo 'x_studio_vat_date'
           en lugar de la fecha contable para el Resumen de IVA.
        2. Añade lógica al campo 'x_studio_vat_date' para que se complete
           automáticamente con la fecha contable, permitiendo la edición manual.
    """,
    'category': 'Accounting/Localizations',
    'depends': [
        'l10n_ar',             # Depende de la localización
        'studio_customization',  # Depende del módulo de Studio
    ],
    'data': [
        # No necesitamos XML porque Studio ya hizo visible el campo
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}