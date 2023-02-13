# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
{
    "name": "G2P Connect Demo",
    "category": "OpenSPP",
    "version": "15.0.0.0.0",
    "sequence": 1,
    "author": "OpenSPP.org",
    "website": "https://github.com/openspp/openspp-demo",
    "license": "LGPL-3",
    "development_status": "Alpha",
    "maintainers": ["jeremi", "gonzalesedwin1123"],
    "depends": [
        "spp_base_demo",
        "g2p_registry_base",
        "g2p_registry_individual",
        "g2p_registry_group",
        "g2p_registry_membership",
        "g2p_programs",
        "g2p_bank",
        "spp_custom_field",
        "spp_custom_fields_ui",
        "g2p_entitlement_cash",
        # "spp_dashboard",
        "spp_idpass",
        "spp_idqueue",
        # "spp_helpdesk",
        "spp_area",
        # "spp_custom_filter",
        "spp_change_request",
        "spp_event_data",
        "spp_service_points",
        "theme_openspp",
        # "spp_pos",
        # "spp_sms",
        "queue_job",
        "spp_change_request_add_children_demo",
    ],
    "external_dependencies": {"python": ["faker"]},
    "data": [
        "security/ir.model.access.csv",
        "data/users_data.xml",
        "data/sample_data.xml",
        "views/generate_data_view.xml",
        "views/generate_change_request_data_view.xml",
        "views/groups_view.xml",
        "views/individuals_view.xml",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
