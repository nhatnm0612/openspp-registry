# Part of OpenSPP. See LICENSE file for full copyright and licensing details.
{
    "name": "OpenSPP Change Request",
    "category": "OpenSPP",
    "version": "15.0.0.0.0",
    "sequence": 1,
    "author": "OpenSPP.org",
    "website": "https://github.com/openspp/openspp-registry",
    "license": "LGPL-3",
    "development_status": "Alpha",
    "maintainers": ["jeremi", "gonzalesedwin1123"],
    "external_dependencies": {
        "python": [
            "python-magic",
        ]
    },
    "depends": [
        "base",
        "g2p_registry_base",
        "g2p_registry_individual",
        "g2p_registry_group",
        "g2p_registry_membership",
        "spp_service_points",
        "spp_area",
        "spp_scan_id_document",
        "dms_field",
        "web_domain_field",
        "spp_idqueue",
        "spp_event_data",
    ],
    "data": [
        "security/change_request_security.xml",
        "security/ir.model.access.csv",
        "data/sequences.xml",
        "data/mail_activity.xml",
        "data/dms.xml",
        "wizard/confirm_user_assignment_view.xml",
        "wizard/reject_change_request_view.xml",
        "wizard/cancel_change_request_view.xml",
        "views/main_view.xml",
        "views/change_request_view.xml",
        "views/change_request_validation_sequence_view.xml",
        "views/dms_file_view.xml",
        "views/registrant_view.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "spp_change_request/static/src/scss/change_request.scss",
            "spp_change_request/static/src/js/hide_button.js",
            "spp_change_request/static/src/js/dms_preview.js",
        ],
        "web.assets_qweb": {
            "/spp_change_request/static/src/xml/dms_preview_widget.xml",
        },
    },
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
