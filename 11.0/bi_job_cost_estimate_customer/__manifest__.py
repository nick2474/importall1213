# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Cost Estimation for Material, Labour and Overheads',
    'version': '11.0.0.5',
    'category': 'Project',
    'summary': 'This apps helps to calculate Job Estimation for Materials, Labous and Overheads',
    'description': """
        Send Estimation to your Customers for materials, labour, overheads details in job estimation.
        Estimation for Jobs - Material / Labour / Overheads
        Material Esitmation
        Job estimation
        labour estimation
        Overheads estimation
        BrowseInfo developed a new odoo/OpenERP module apps.
        This module use for Real Estate Management, Construction management, Building Construction,
        Material Line on JoB Estimation
        Labour Lines on Job Estimation.
        Overhead Lines on Job Estimation.
        create Quotation from the Job Estimation.
        overhead on job estimation
        Construction Projects
        Budgets
        Notes
        Materials
        Material Request For Job Orders
        Add Materials
        Job Orders
        Create Job Orders
        Job Order Related Notes
        Issues Related Project
        Vendors
        Vendors / Contractors

        Construction Management
        Construction Activity
        Construction Jobs
        Job Order Construction
        Job Orders Issues
        Job Order Notes
        Construction Notes
        Job Order Reports
        Construction Reports
        Job Order Note
        Construction app
        Project Report
        Task Report
        Construction Project - Project Manager
        real estate property
        propery management
        bill of material
        Material Planning On Job Order

        Bill of Quantity On Job Order
        Bill of Quantity construction
        Project job costing on manufacturing

Envíe Estimación a sus Clientes para materiales, mano de obra, detalles de gastos generales en la estimación del trabajo.
        Estimación de trabajos: material / mano de obra / gastos generales
        Esitmation material
        Estimación de trabajo
        estimación laboral
        Estimación de gastos generales
        BrowseInfo desarrolló una nueva aplicación de módulo odoo / OpenERP.
        Este uso del módulo para la gestión inmobiliaria, la gestión de la construcción, la construcción de edificios,
        Línea de material en la estimación de JoB
        Líneas laborales sobre estimación laboral.
        Líneas aéreas en la estimación del trabajo.
        crear oferta de la estimación del trabajo.
        sobrecarga en la estimación del trabajo
        Proyectos de construcción
        Presupuestos
        Notas
        Materiales
        Solicitud de material para órdenes de trabajo
        Agregar materiales
        Órdenes de trabajo
        Crear órdenes de trabajo
        Notas relacionadas con la orden de trabajo
        Temas relacionados Proyecto
        Vendedores
        Vendedores / Contratistas

        Gestión de la construcción
        Actividad de construcción
        Trabajos de construcción
        Construcción de órdenes de trabajo
        Problemas de pedidos de trabajo
        Notas de la orden de trabajo
        Notas de construcción
        Informes de órdenes de trabajo
        Informes de construcción
        Nota de orden de trabajo
        Aplicación de construcción
        Informe del proyecto
        Informe de tareas
        Proyecto de construcción - Gerente de proyecto
        propiedad de bienes raíces
        gestión de la propiedad
        lista de materiales
        Planificación de material en orden de trabajo

        Factura de cantidad en orden de trabajo
        Proyecto de ley de cantidad
        Costo del trabajo del proyecto en la fabricación

1562/5000
Envoyer l'estimation à vos clients pour les matériaux, le travail, les détails de frais généraux dans l'estimation du travail.
        Estimation pour les emplois - Matériel / main-d'œuvre / frais généraux
        Esitmation matérielle
        Estimation du travail
        estimation du travail
        Estimation des frais généraux
        BrowseInfo a développé une nouvelle application de module odoo / OpenERP.
        Ce module d'utilisation pour la gestion immobilière, la gestion de la construction, la construction de bâtiments,
        Ligne de matériau sur Estimation JoB
        Lignes de main-d'œuvre sur l'estimation du travail.
        Lignes aériennes sur l'estimation du travail.
        créer une citation à partir de l'estimation du travail.
        frais généraux sur l'estimation du travail
        Projets de construction
        Budgets
        Remarques
        Matériaux
        Demande de matériel pour les commandes d'emploi
        Ajouter des matériaux
        Commandes d'emploi
        Créer des commandes d'emploi
        Notes relatives à la commande d'emploi
        Problèmes liés au projet
        Vendeurs
        Vendeurs / Entrepreneurs

        Gestion de la construction
        Activité de construction
        Emplois en construction
        Construction d'une commande d'emploi
        Problèmes d'ordres de travail
        Notes de commande de travail
        Notes de construction
        Rapports de commande
        Rapports de construction
        Note de commande
        Application de construction
        Rapport de projet
        Rapport de tâche
        Projet de construction - Gestionnaire de projet
        propriété immobilière
        gestion de la propriété
        nomenclature
        Planification matérielle sur l'ordre de travail

        Projet de loi sur la commande
        Projet de loi de la quantité
        Projet de travail coûtant sur la fabrication
    
""",
    'author': 'BrowseInfo',
    'website': 'http://www.browseinfo.in',
    'depends': ['sale','sale_management','project','account_invoicing','hr_timesheet','mail'],
    'data': [
            'security/ir.model.access.csv',
            'report/job_estimate_report.xml',
            'report/job_estimate_report_view.xml',
            'data/ir_sequence_data.xml',
            'data/mail_template_data.xml',
            'views/custom_job_estimate_view.xml',
            
    ],
    "price": 39,
    "currency": 'EUR',
    'installable': True,
    'auto_install': False,
    "images":['static/description/Banner.png'],
    'live_test_url':'https://youtu.be/f-3f4DwaOnM',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
