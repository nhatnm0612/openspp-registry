# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
{
    "name": "SPP Program: Manual Entitlement",
    "category": "OpenSPP",
    "version": "17.0.1.0.0",
    "sequence": 1,
    "author": "OpenSPP.org",
    "website": "https://github.com/OpenSPP/openspp-modules",
    "license": "LGPL-3",
    "development_status": "Alpha",
    "maintainers": ["jeremi", "gonzalesedwin1123"],
    "depends": [
        "base",
        "g2p_registry_base",
        "g2p_programs",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/cycle_view.xml",
        "wizard/manual_entitlement_wizard.xml",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
