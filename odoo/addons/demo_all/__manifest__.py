# Copyright 2023 TINCID SRL (Régis Pirard)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Demo Project (all addons)",
    "author": "TINCID SRL (Régis Pirard)",
    "summary": """
    Demo Odoo Project - All addons and dependencies""",
    "website": "",
    "category": "demo",
    "version": "16.0.0.0.7",
    "license": "AGPL-3",
    "depends": [
        # Odoo addons - no odoo enterprise addons dependencies !!!
        "base",
        "mail",
        "resource",
        "web",
        # OCA modules
        "web_environment_ribbon",
        "base_user_role",
        # Custom modules
        "demo_module1",
    ],
    "data": [
        "data/web_environment_ribbon.xml",
    ],
    "application": True,
}
