###########################################
###                                     ###
###     BSCP : Foundation Architect     ###
###                                     ###
###           ---------------           ###
###   Build. Secure. Contain. Protect   ###
###                                     ###
###########################################


FACTIONS = [
    "CI",  # Chaos Insurgency
    "CD",  # Class-D
    "IA",  # Internal Administration
    "ISD",  # Internal Security Department
    "MTF",  # Mobile Task Force
    "O5",  # O5 Council
    "RRT",  # Rapid Response Team
    "SCD",  # Scientific Department
    "SD",  # Security Department
    "SID",  # Site Director
    "MD",  # Medical Department
]

FACTION_TYPES = {
    "CI": "e",
    "CD": "n",
    "IA": "a",
    "ISD": "a",
    "MTF": "a",
    "O5": "a",
    "RRT": "a",
    "SCD": "ns",
    "SD": "a",
    "SID": "a",
    "MD": "ns",
}

ALLIANCES_TYPES = {
    "a": "alliance",
    "ns": "neutral support",
    "n": "neutral",
    "e": "enemy"
}

ALLIANCES = {
    "CI": ["CD"],
    "CD": ["SCD", "MD", "CI"],
    "IA": ["ISD", "MTF", "O5", "RRT", "SD", "SID", "SCD", "MD"],
    "ISD": ["IA", "MTF", "O5", "RRT", "SD", "SID", "SCD", "MD"],
    "MTF": ["IA", "ISD", "O5", "RRT", "SD", "SID", "SCD", "MD"],
    "O5": ["IA", "ISD", "MTF", "RRT", "SD", "SID", "SCD", "MD"],
    "RRT": ["IA", "ISD", "MTF", "O5", "SD", "SID", "SCD", "MD"],
    "SCD": ["CD", "IA", "ISD", "MTF", "O5", "RRT", "SD", "SID", "MD"],
    "SD": ["IA", "ISD", "MTF", "O5", "RRT", "SCD", "SID", "MD"],
    "SID": ["IA", "ISD", "MTF", "O5", "RRT", "SD", "SCD", "MD"],
    "MD": ["CD", "SCD", "IA", "ISD", "MTF", "O5", "RRT", "SD", "SID"],
}

ENEMIES = {
    "CI": ["IA", "ISD", "MTF", "O5", "RRT", "SD", "SID", "SCD", "MD"],
    "CD": ["IA", "ISD", "MTF", "O5", "RRT", "SD", "SID", "SCD", "MD"],
    "IA": ["CI"],
    "ISD": ["CI"],
    "MTF": ["CI"],
    "O5": ["CI"],
    "RRT": ["CI"],
    "SCD": ["CI"],
    "SD": ["CI"],
    "SID": ["CI"],
    "MD": ["CI"],
}

FACTION_INFO = {
    "CI": {
        "full_name": "Chaos Insurgency",
        "type": "e",
        "description": "Highly dangerous rogue faction attempting containment breaches.",
    },
    "CD": {
        "full_name": "Class-D Personnel",
        "type": "n",
        "description": "Disposable personnel; sometimes used for experiments or tasks.",
    },
    "IA": {
        "full_name": "Internal Administration",
        "type": "a",
        "description": "Facility administration staff and security management.",
    },
    "ISD": {
        "full_name": "Internal Security Department",
        "type": "a",
        "description": "Security personnel managing daily operations and containment.",
    },
    "MTF": {
        "full_name": "Mobile Task Force",
        "type": "a",
        "description": "Specialized tactical units deployed for SCP recontainment, hostile threat neutralization, and high-risk facility operations."
    },
    "O5": {
        "full_name": "O5 Council",
        "type": "a",
        "description": "High-ranking oversight council with command authority.",
    },
    "RRT": {
        "full_name": "Rapid Response Team",
        "type": "a",
        "description": "Specialized units for urgent threat neutralization.",
    },
    "SCD": {
        "full_name": "Scientific Department",
        "type": "ns",
        "description": "Researchers and lab personnel.",
    },
    "SD": {
        "full_name": "Security Department",
        "type": "a",
        "description": "Facility security staff, manages general containment and patrols.",
    },
    "SID": {
        "full_name": "Site Director",
        "type": "a",
        "description": "Leads and manages the facility, overseeing containment protocols, security, and internal operations. Responsible for high-level decisions and reports directly to the O5 Council.",
    },
    "MD": {
        "full_name": "Medical Department",
        "type": "ns",
        "description": "Medical personnel for treatment and recovery.",
    },
}
