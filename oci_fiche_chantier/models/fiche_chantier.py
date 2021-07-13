from odoo import fields, models, api


class ficheChantierForm(models.Model):
    _name = 'oci_fiche_chantier.fiche_chantier'

# INFORMATION GENERALES SUR LE TRAVAILLEUR
    nom = fields.Char(string="Nom")
    prenom = fields.Char(string="Prénom")
    nom_chantier = fields.Char(string="Nom du chantier")
    age = fields.Integer(string="Age")
    numero_chantier = fields.Integer(string="Numéro du chantier")
    qualification = fields.Char(string="Emploi & qualification")
    date_arrive = fields.Date(string="Date d'arrivée sur chantier")

    statut = fields.Selection(
        [('interimaire', 'Intérimaire'),
         ('stagiaire', 'Stagiaire'),
         ('cdd', 'CDD'),
         ('cdi', 'CDI'),
         ('autre', 'Autre')], string="Statut")
    statut_autre = fields.Char(string="Autre")

# INFORMATION SUR LA VISITE MEDICALE
    date_visite = fields.Date(string="Date de la visite")
    restriction = fields.Selection(
        [('yes', 'Oui'),
         ('no', 'Non')], string="Restrictions éventuelles")
    restriction_char = fields.Char(string="Laquelle")
    visite_autre = fields.Char(string="Autre")

# INFORMATIONS RECU
    information_horraire = fields.Boolean(string="Les horraires de travail")
    information_acceschantier = fields.Boolean(string="Accès chantier / Circulation / zones stockage")
    information_cantonnement = fields.Boolean(string="Le cantonnement(vestiaire, réfectoire, sanitaires")
    information_consigne = fields.Boolean(string="Les consignes particulières du chantier")
    information_postetravail = fields.Boolean(string="Le poste de travail, son équipe et son résponsable")
    information_laconduite = fields.Boolean(string="La conduiteà tenir en cas d'accident")
    information_secouriste = fields.Boolean(string="Si présence de secouriste(s) au travail")

# INFORMATIONS RECU SUR LES REGLES DE PREVENTION

    information_prev_moperatoire = fields.Boolean(string="Le mode opératoire du poste de travail")
    information_prev_conspost = fields.Boolean(string="Les consignes du poste de travail")
    information_prev_risqcoactivite = fields.Boolean(string="Risques liés à la coactivité")
    information_prev_risqposte = fields.Boolean(string="Risques liés au poste de travail, outils, produits, matériels, matériaux")
    information_prev_protcollec = fields.Boolean(string="Les protections collectives à mettre en place et à respecter")

# HABILITATION

    permis_conduire = fields.Boolean(string="Permis de conduire Permis B valide")
    sst = fields.Boolean(string="SST")
    echafaudage_reception = fields.Boolean(string="échafaudage(réception)")
    echafaudage_montage = fields.Boolean(string="échafaudage(montage / démontage)")

# CONCLUSION
    ccl_fait = fields.Char(string="Fait à")
    ccl_datefait = fields.Date(string="Le")