# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-28 17:08
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BasicFactsheet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "model_name",
                    models.CharField(
                        help_text="What is the full model name?",
                        max_length=100,
                        unique=True,
                        verbose_name="Model name",
                    ),
                ),
                (
                    "acronym",
                    models.CharField(
                        help_text="What is the abbreviation?",
                        max_length=20,
                        verbose_name="Acronym",
                    ),
                ),
                (
                    "institutions",
                    models.CharField(
                        help_text="Which institutions develop(ed) the model?",
                        max_length=100,
                        verbose_name="Institution(s)",
                    ),
                ),
                (
                    "authors",
                    models.CharField(
                        help_text="Who are the authors? Where do / did they work, on which parts of the model, during which time period?",
                        max_length=300,
                        verbose_name="Author(s) (institution, working field, active time period)",
                    ),
                ),
                (
                    "current_contact_person",
                    models.CharField(
                        help_text="Who is the main contact person?",
                        max_length=100,
                        null=True,
                        verbose_name="Current contact person",
                    ),
                ),
                (
                    "contact_email",
                    models.EmailField(
                        help_text="Please, fill in an e-mail address.",
                        max_length=254,
                        verbose_name="Contact (e-mail)",
                    ),
                ),
                ("website", models.URLField(null=True, verbose_name="Website")),
                (
                    "logo",
                    models.ImageField(null=True, upload_to="", verbose_name="Logo"),
                ),
                (
                    "primary_purpose",
                    models.CharField(
                        help_text="What is the primary purpose the model?",
                        max_length=100,
                        null=True,
                        verbose_name="Primary Purpose",
                    ),
                ),
                (
                    "primary_outputs",
                    models.CharField(
                        help_text="What are the main outputs of the model?",
                        max_length=100,
                        null=True,
                        verbose_name="Primary Outputs",
                    ),
                ),
                (
                    "support",
                    models.BooleanField(
                        default=False, verbose_name="Support / Community / Forum"
                    ),
                ),
                (
                    "framework",
                    models.BooleanField(
                        default=False,
                        help_text="Is the model based on a framework? If yes, which?",
                        verbose_name="Framework",
                    ),
                ),
                ("framework_yes_text", models.CharField(max_length=100, null=True)),
                (
                    "user_documentation",
                    models.URLField(
                        help_text="Where is the user documentation publicly available?",
                        verbose_name="User Documentation",
                    ),
                ),
                (
                    "code_documentation",
                    models.URLField(
                        help_text="Where is the code documentation publicly available?",
                        verbose_name="Developer/Code Documentation",
                    ),
                ),
                (
                    "documentation_quality",
                    models.CharField(
                        choices=[
                            ("expandable", "expandable"),
                            ("good", "good"),
                            ("excellent", "excellent"),
                        ],
                        default="expandable",
                        help_text="How is the quality of the documentations?",
                        max_length=100,
                        verbose_name="Documentation quality",
                    ),
                ),
                (
                    "source_of_funding",
                    models.CharField(
                        help_text="What's the main source of funding?",
                        max_length=200,
                        null=True,
                        verbose_name="Source of funding",
                    ),
                ),
                (
                    "open_source",
                    models.BooleanField(default=False, verbose_name="Open Source"),
                ),
                (
                    "open_up",
                    models.BooleanField(
                        default=False,
                        help_text="Will the source code be available in future?",
                        verbose_name="Planned to open up in the future",
                    ),
                ),
                (
                    "costs",
                    models.CharField(max_length=100, null=True, verbose_name="Costs"),
                ),
                (
                    "license",
                    models.CharField(
                        choices=[("Apache", "Apache"), ("Other", "Other")],
                        default="Apache",
                        max_length=100,
                        verbose_name="License",
                    ),
                ),
                ("license_other_text", models.CharField(max_length=100, null=True)),
                (
                    "source_code_available",
                    models.BooleanField(
                        default=False,
                        help_text="Is the source code directly downloadable?",
                        verbose_name="Source code available",
                    ),
                ),
                (
                    "gitHub",
                    models.BooleanField(
                        default=False,
                        help_text="Is the model available on GitHub?",
                        verbose_name="GitHub",
                    ),
                ),
                (
                    "link_to_source_code",
                    models.URLField(null=True, verbose_name="Link to source code"),
                ),
                (
                    "data_provided",
                    models.CharField(
                        choices=[("none", "none"), ("some", "some"), ("all", "all")],
                        default="none",
                        help_text="Is the necessary data to run a scenario available?",
                        max_length=100,
                        verbose_name="Data provided",
                    ),
                ),
                (
                    "cooperative_programming",
                    models.BooleanField(
                        default=False,
                        help_text="Is it possible to join the coding group?",
                        verbose_name="Cooperative programming",
                    ),
                ),
                (
                    "number_of_devolopers",
                    models.CharField(
                        choices=[
                            ("less than 10", "less than 10"),
                            (" less than 20", " less than 20"),
                            (" less than 50", " less than 50"),
                            (" more than 50", " more than 50"),
                        ],
                        default="less than 10",
                        help_text="How many people are involved in the model development?",
                        max_length=100,
                        verbose_name="Number of devolopers",
                    ),
                ),
                (
                    "number_of_users",
                    models.CharField(
                        choices=[
                            ("less than 10", "less than 10"),
                            (" less than 100", " less than 100"),
                            (" less than 1000", " less than 1000"),
                            (" more than 1000", " more than 1000"),
                        ],
                        default="less than 10",
                        help_text="How many people approximately use the model?",
                        max_length=100,
                        verbose_name="Number of users ",
                    ),
                ),
                (
                    "modelling_software",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            help_text="What modelling software and which version is used?",
                            max_length=100,
                        ),
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "interal_data_processing_software",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            help_text="Which data processing software is required?",
                            max_length=100,
                        ),
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "external_optimizer",
                    models.BooleanField(
                        default=False,
                        help_text="Which external optimizer can the model apply?",
                        verbose_name="External optimizer",
                    ),
                ),
                (
                    "external_optimizer_yes_text",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=100),
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "additional_software",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            help_text="Which additional software is required to run the model?",
                            max_length=100,
                        ),
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "gui",
                    models.BooleanField(
                        default=False,
                        help_text="Is a graphical user interface available?",
                        verbose_name="GUI",
                    ),
                ),
                (
                    "citation_reference",
                    models.CharField(
                        help_text="publications about the model",
                        max_length=1000,
                        null=True,
                        verbose_name="Citation reference",
                    ),
                ),
                (
                    "citation_DOI",
                    models.CharField(
                        help_text="publications about the model",
                        max_length=1000,
                        null=True,
                        verbose_name="Citation DOI",
                    ),
                ),
                (
                    "references_to_reports_produced_using_the_model",
                    models.CharField(
                        help_text="Which studies have been calculated with this model?",
                        max_length=1000,
                        null=True,
                        verbose_name="References to reports produced using the model",
                    ),
                ),
                (
                    "larger_scale_usage",
                    models.CharField(
                        help_text="Is this model used on a larger scale? If so, who uses it?",
                        max_length=1000,
                        null=True,
                        verbose_name="Larger scale usage",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Energyframework",
            fields=[
                (
                    "basicfactsheet_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="modelview.BasicFactsheet",
                    ),
                ),
                (
                    "model_types",
                    models.CharField(
                        choices=[
                            ("Grid optimisation", "Grid optimisation"),
                            ("demand simulation", "demand simulation"),
                            ("feed-in simulation", "feed-in simulation"),
                            ("other + text", "other + text"),
                        ],
                        max_length=20,
                        null=True,
                        verbose_name="API to openmod database",
                    ),
                ),
                ("model_types_other_text", models.CharField(max_length=100, null=True)),
                (
                    "api_doc",
                    models.URLField(
                        null=True, verbose_name="Link to API documentation"
                    ),
                ),
                (
                    "data_api",
                    models.BooleanField(verbose_name="API to openmod database"),
                ),
                (
                    "abstraction",
                    models.TextField(
                        null=True, verbose_name="Points/degree of abstraction"
                    ),
                ),
                (
                    "used",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=100),
                        default=list,
                        null=True,
                        size=None,
                        verbose_name="Models using this framework",
                    ),
                ),
            ],
            bases=("modelview.basicfactsheet",),
        ),
        migrations.CreateModel(
            name="Energymodel",
            fields=[
                (
                    "basicfactsheet_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="modelview.BasicFactsheet",
                    ),
                ),
                (
                    "energy_sectors_electricity",
                    models.BooleanField(default=False, verbose_name="electricity"),
                ),
                (
                    "energy_sectors_heat",
                    models.BooleanField(default=False, verbose_name="heat"),
                ),
                (
                    "energy_sectors_liquid_fuels",
                    models.BooleanField(default=False, verbose_name="liquid fuels"),
                ),
                (
                    "energy_sectors_gas",
                    models.BooleanField(default=False, verbose_name="gas"),
                ),
                (
                    "energy_sectors_oil",
                    models.BooleanField(default=False, verbose_name="oil"),
                ),
                (
                    "energy_sectors_others",
                    models.BooleanField(default=False, verbose_name="others"),
                ),
                (
                    "energy_sectors_others_text",
                    models.CharField(max_length=200, null=True),
                ),
                (
                    "demand_sectors_households",
                    models.BooleanField(default=False, verbose_name="Households"),
                ),
                (
                    "demand_sectors_industry",
                    models.BooleanField(default=False, verbose_name="Industry"),
                ),
                (
                    "demand_sectors_commercial_sector",
                    models.BooleanField(
                        default=False, verbose_name="Commercial sector"
                    ),
                ),
                (
                    "demand_sectors_transport",
                    models.BooleanField(default=False, verbose_name="Transport"),
                ),
                (
                    "energy_carrier_gas_natural_gas",
                    models.BooleanField(default=False, verbose_name="Natural gas"),
                ),
                (
                    "energy_carrier_gas_biogas",
                    models.BooleanField(default=False, verbose_name="Biogas"),
                ),
                (
                    "energy_carrier_gas_hydrogen",
                    models.BooleanField(default=False, verbose_name="Hydrogen"),
                ),
                (
                    "energy_carrier_liquids_petrol",
                    models.BooleanField(default=False, verbose_name="Petrol"),
                ),
                (
                    "energy_carrier_liquids_diesel",
                    models.BooleanField(default=False, verbose_name="Diesel"),
                ),
                (
                    "energy_carrier_liquids_ethanol",
                    models.BooleanField(default=False, verbose_name="Ethanol"),
                ),
                (
                    "energy_carrier_solid_hard_coal",
                    models.BooleanField(default=False, verbose_name="Hard coal"),
                ),
                (
                    "energy_carrier_solid_hard_lignite",
                    models.BooleanField(default=False, verbose_name="Lignite"),
                ),
                (
                    "energy_carrier_solid_hard_uranium",
                    models.BooleanField(default=False, verbose_name="Uranium"),
                ),
                (
                    "energy_carrier_solid_hard_biomass",
                    models.BooleanField(default=False, verbose_name="Biomass"),
                ),
                (
                    "energy_carrier_renewables_sun",
                    models.BooleanField(default=False, verbose_name="Sun"),
                ),
                (
                    "energy_carrier_renewables_wind",
                    models.BooleanField(default=False, verbose_name="Wind"),
                ),
                (
                    "energy_carrier_renewables_hydro",
                    models.BooleanField(default=False, verbose_name="Hydro"),
                ),
                (
                    "energy_carrier_renewables_geothermal_heat",
                    models.BooleanField(default=False, verbose_name="Geothermal heat"),
                ),
                (
                    "generation_renewables_PV",
                    models.BooleanField(default=False, verbose_name="PV"),
                ),
                (
                    "generation_renewables_wind",
                    models.BooleanField(default=False, verbose_name="Wind"),
                ),
                (
                    "generation_renewables_hydro",
                    models.BooleanField(default=False, verbose_name="Hydro"),
                ),
                (
                    "generation_renewables_biomass",
                    models.BooleanField(default=False, verbose_name="Biomass"),
                ),
                (
                    "generation_renewables_biogas",
                    models.BooleanField(default=False, verbose_name="Biogas"),
                ),
                (
                    "generation_renewables_solar_thermal",
                    models.BooleanField(default=False, verbose_name="Solar thermal"),
                ),
                (
                    "generation_renewables_others",
                    models.BooleanField(default=False, verbose_name="Others"),
                ),
                (
                    "generation_renewables_others_text",
                    models.CharField(max_length=200, null=True),
                ),
                (
                    "generation_conventional_gas",
                    models.BooleanField(default=False, verbose_name="gas"),
                ),
                (
                    "generation_conventional_coal",
                    models.BooleanField(default=False, verbose_name="coal"),
                ),
                (
                    "generation_conventional_oil",
                    models.BooleanField(default=False, verbose_name="oil"),
                ),
                (
                    "generation_conventional_liquid_fuels",
                    models.BooleanField(default=False, verbose_name="liquid fuels"),
                ),
                (
                    "generation_conventional_nuclear",
                    models.BooleanField(default=False, verbose_name="nuclear"),
                ),
                (
                    "generation_CHP",
                    models.BooleanField(default=False, verbose_name="CHP"),
                ),
                (
                    "transfer_electricity",
                    models.BooleanField(default=False, verbose_name="electricity"),
                ),
                (
                    "transfer_electricity_distribution",
                    models.BooleanField(default=False),
                ),
                ("transfer_electricity_transition", models.BooleanField(default=False)),
                (
                    "transfer_gas",
                    models.BooleanField(default=False, verbose_name="gas"),
                ),
                ("transfer_gas_distribution", models.BooleanField(default=False)),
                ("transfer_gas_transition", models.BooleanField(default=False)),
                (
                    "transfer_heat",
                    models.BooleanField(default=False, verbose_name="heat"),
                ),
                ("transfer_heat_distribution", models.BooleanField(default=False)),
                ("transfer_heat_transition", models.BooleanField(default=False)),
                (
                    "network_coverage_AC",
                    models.BooleanField(default=False, verbose_name="AC load flow"),
                ),
                (
                    "network_coverage_DC",
                    models.BooleanField(default=False, verbose_name="DC load flow"),
                ),
                (
                    "storage_electricity_battery",
                    models.BooleanField(default=False, verbose_name="battery"),
                ),
                (
                    "storage_electricity_kinetic",
                    models.BooleanField(default=False, verbose_name="kinetic"),
                ),
                (
                    "storage_electricity_CAES",
                    models.BooleanField(default=False, verbose_name="CAES"),
                ),
                (
                    "storage_electricity_PHS",
                    models.BooleanField(default=False, verbose_name="PHS"),
                ),
                (
                    "storage_electricity_chemical",
                    models.BooleanField(default=False, verbose_name="chemical"),
                ),
                (
                    "storage_heat",
                    models.BooleanField(default=False, verbose_name="heat"),
                ),
                ("storage_gas", models.BooleanField(default=False, verbose_name="gas")),
                (
                    "user_behaviour",
                    models.BooleanField(
                        default=False,
                        help_text="How can user behaviour changes and demand side management be considered?",
                        verbose_name="User behaviour and demand side management",
                    ),
                ),
                (
                    "user_behaviour_yes_text",
                    models.CharField(max_length=200, null=True),
                ),
                (
                    "market_models",
                    models.BooleanField(
                        default=False,
                        help_text="Which / Is a market models are included?",
                        verbose_name="Market models",
                    ),
                ),
                (
                    "geographical_coverage",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            default="",
                            help_text="What regions are covered? Please, list the regions covered by the model. Leave blank, if the model and data are not limited to a specific region. Example input: USA, Canada, Mexico",
                            max_length=100,
                        ),
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "geo_resolution_global",
                    models.BooleanField(default=False, verbose_name="global"),
                ),
                (
                    "geo_resolution_continents",
                    models.BooleanField(default=False, verbose_name="continents"),
                ),
                (
                    "geo_resolution_national_states",
                    models.BooleanField(default=False, verbose_name="national states"),
                ),
                (
                    "geo_resolution_TSO_regions",
                    models.BooleanField(default=False, verbose_name="TSO regions"),
                ),
                (
                    "geo_resolution_federal_states",
                    models.BooleanField(default=False, verbose_name="federal states"),
                ),
                (
                    "geo_resolution_regions",
                    models.BooleanField(default=False, verbose_name="regions"),
                ),
                (
                    "geo_resolution_NUTS_3",
                    models.BooleanField(default=False, verbose_name="NUTS 3"),
                ),
                (
                    "geo_resolution_municipalities",
                    models.BooleanField(default=False, verbose_name="municipalities"),
                ),
                (
                    "geo_resolution_districts",
                    models.BooleanField(default=False, verbose_name="districts"),
                ),
                (
                    "geo_resolution_households",
                    models.BooleanField(default=False, verbose_name="households"),
                ),
                (
                    "geo_resolution_power_stations",
                    models.BooleanField(default=False, verbose_name="power stations"),
                ),
                (
                    "geo_resolution_others",
                    models.BooleanField(default=False, verbose_name="others"),
                ),
                (
                    "geo_resolution_others_text",
                    models.CharField(max_length=200, null=True),
                ),
                (
                    "comment_on_geo_resolution",
                    models.CharField(
                        help_text="Feel free to explain the geographical resolution of the model e.g. with regard to the grid data.",
                        max_length=200,
                        null=True,
                        verbose_name="Comment on geographic (spatial) resolution",
                    ),
                ),
                (
                    "time_resolution_anual",
                    models.BooleanField(default=False, verbose_name="anual"),
                ),
                (
                    "time_resolution_hour",
                    models.BooleanField(default=False, verbose_name="hour"),
                ),
                (
                    "time_resolution_15_min",
                    models.BooleanField(default=False, verbose_name="15 min"),
                ),
                (
                    "time_resolution_1_min",
                    models.BooleanField(default=False, verbose_name="1 min"),
                ),
                (
                    "observation_period_1_year",
                    models.BooleanField(default=False, verbose_name="1 year"),
                ),
                (
                    "time_resolution_other",
                    models.BooleanField(default=False, verbose_name="other"),
                ),
                (
                    "time_resolution_other_text",
                    models.CharField(max_length=200, null=True),
                ),
                (
                    "additional_dimensions_sector_ecological",
                    models.BooleanField(default=False, verbose_name="ecological"),
                ),
                (
                    "additional_dimensions_sector_ecological_text",
                    models.CharField(max_length=100, null=True),
                ),
                (
                    "additional_dimensions_sector_economic",
                    models.BooleanField(default=False, verbose_name="economic"),
                ),
                (
                    "additional_dimensions_sector_economic_text",
                    models.CharField(max_length=100, null=True),
                ),
                (
                    "additional_dimensions_sector_social",
                    models.BooleanField(default=False, verbose_name="social"),
                ),
                (
                    "additional_dimensions_sector_social_text",
                    models.CharField(max_length=100, null=True),
                ),
                (
                    "additional_dimensions_sector_others",
                    models.BooleanField(default=False, verbose_name="others"),
                ),
                (
                    "additional_dimensions_sector_others_text",
                    models.CharField(max_length=100, null=True),
                ),
                (
                    "model_class_optimization_LP",
                    models.BooleanField(default=False, verbose_name="LP"),
                ),
                (
                    "model_class_optimization_MILP",
                    models.BooleanField(default=False, verbose_name="MILP"),
                ),
                (
                    "model_class_optimization_Nonlinear",
                    models.BooleanField(default=False, verbose_name="Nonlinear"),
                ),
                (
                    "model_class_optimization_LP_MILP_Nonlinear_text",
                    models.CharField(max_length=100, null=True),
                ),
                (
                    "model_class_simulation_Agentbased",
                    models.BooleanField(default=False, verbose_name="Agent-based"),
                ),
                (
                    "model_class_simulation_System_Dynamics",
                    models.BooleanField(default=False, verbose_name="System Dynamics"),
                ),
                (
                    "model_class_simulation_Accounting_Framework",
                    models.BooleanField(
                        default=False, verbose_name="Accounting Framework"
                    ),
                ),
                (
                    "model_class_simulation_Game_Theoretic_Model",
                    models.BooleanField(
                        default=False, verbose_name="Game Theoretic Model"
                    ),
                ),
                (
                    "model_class_other",
                    models.BooleanField(default=False, verbose_name="Other"),
                ),
                ("model_class_other_text", models.BooleanField(default=False)),
                (
                    "short_description_of_mathematical_model_class",
                    models.CharField(
                        max_length=100,
                        null=True,
                        verbose_name="Short description of mathematical model class",
                    ),
                ),
                (
                    "mathematical_objective_cO2",
                    models.BooleanField(default=False, verbose_name="CO2"),
                ),
                (
                    "mathematical_objective_costs",
                    models.BooleanField(default=False, verbose_name="costs"),
                ),
                (
                    "mathematical_objective_rEshare",
                    models.BooleanField(default=False, verbose_name="RE-share"),
                ),
                (
                    "mathematical_objective_other",
                    models.BooleanField(default=False, verbose_name="other"),
                ),
                (
                    "mathematical_objective_other_text",
                    models.BooleanField(default=False),
                ),
                (
                    "uncertainty_deterministic",
                    models.BooleanField(default=False, verbose_name="Deterministic"),
                ),
                (
                    "uncertainty_Stochastic",
                    models.BooleanField(default=False, verbose_name="Stochastic"),
                ),
                (
                    "uncertainty_Other",
                    models.BooleanField(default=False, verbose_name="Other"),
                ),
                (
                    "montecarlo",
                    models.BooleanField(
                        default=False,
                        verbose_name="Suited for many scenarios / monte-carlo",
                    ),
                ),
                (
                    "typical_computation_time_less_than_a_second",
                    models.BooleanField(
                        default=False, verbose_name="less than a second"
                    ),
                ),
                (
                    "typical_computation_time_less_than_a_minute",
                    models.BooleanField(
                        default=False, verbose_name="less than a minute"
                    ),
                ),
                (
                    "typical_computation_time_less_than_an_hour",
                    models.BooleanField(
                        default=False, verbose_name="less than an hour"
                    ),
                ),
                (
                    "typical_computation_time_less_than_a_day",
                    models.BooleanField(default=False, verbose_name="less than a day"),
                ),
                (
                    "typical_computation_time_more_than_a_day",
                    models.BooleanField(default=False, verbose_name="more than a day"),
                ),
                (
                    "typical_computation_hardware",
                    models.CharField(
                        help_text="Here you can specify which hardware was assumed to estimate above time (e.g. RAM, CPU, GPU, etc).",
                        max_length=1000,
                        null=True,
                        verbose_name="Typical computation hardware",
                    ),
                ),
                (
                    "technical_data_anchored_in_the_model",
                    models.CharField(
                        help_text="If there is technical data already embedded (hard code) in the model and not part of the scenario, please make that transparent here.",
                        max_length=1000,
                        null=True,
                        verbose_name="Technical data anchored in the model",
                    ),
                ),
                (
                    "example_research_questions",
                    models.CharField(
                        help_text="What would be a good research question that could be answered with the model?",
                        max_length=1000,
                        null=True,
                        verbose_name="Example research questions",
                    ),
                ),
                (
                    "validation",
                    models.CharField(
                        help_text="How is the model validated?",
                        max_length=1000,
                        null=True,
                        verbose_name="Validation",
                    ),
                ),
                (
                    "model_specific_properties",
                    models.CharField(
                        help_text="What are main specific characteristics (strengths and weaknesses) of this model regarding the purpose of the recommendation?",
                        max_length=1000,
                        null=True,
                        verbose_name="Model specific properties",
                    ),
                ),
            ],
            bases=("modelview.basicfactsheet",),
        ),
    ]
