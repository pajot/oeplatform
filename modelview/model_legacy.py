from django.db import models
from django.db.models import (
    BooleanField,
    CharField,
    EmailField,
    ForeignKey,
    ImageField,
    IntegerField,
    SmallIntegerField,
    TextField,
    DateField,
)
from django.contrib.postgres.fields import ArrayField

class Energystudy(models.Model):
    def __str__(self):
        return self.name_of_the_study

    name_of_the_study = CharField(
        verbose_name="Name of the study",
        help_text="What is the name of the study?",
        max_length=1000,
    )
    author_Institution = CharField(
        verbose_name="Author, Institution",
        help_text="Who are the authors of the study and for which institution do they work?",
        max_length=1000,
    )
    contact_email = EmailField(
        verbose_name="Contact (e-mail)",
        help_text="What is the e-mail contact of the developer (group)",
        null=True,
    )
    client = CharField(
        verbose_name="Client",
        help_text="Who are the customers requesting the study?",
        max_length=1000,
        null=True,
    )
    funding_private = BooleanField(verbose_name="private")
    funding_public = BooleanField(verbose_name="public")
    funding_no_funding = BooleanField(verbose_name="no funding")
    citation_reference = ArrayField(
        CharField(max_length=1000), verbose_name="Citation reference", null=True
    )
    citation_doi = ArrayField(
        CharField(max_length=1000), verbose_name="Citation doi", null=True
    )
    aim = CharField(
        verbose_name="Aim",
        help_text="What is the purpose (hypothesis) and research question of the study?",
        max_length=1000,
        null=True,
    )
    new_aspects = CharField(
        verbose_name="New aspects",
        help_text="What is new? (beyond state of research)",
        max_length=1000,
        null=True,
    )
    spatial_Geographical_coverage = CharField(
        verbose_name="Spatial / Geographical coverage",
        help_text="Which geographical region is adressed in the study?",
        max_length=1000,
        null=True,
    )
    time_frame_2020 = BooleanField(verbose_name="2020")
    time_frame_2030 = BooleanField(verbose_name="2030")
    time_frame_2050 = BooleanField(verbose_name="2050")
    time_frame_other = BooleanField(verbose_name="other")
    time_frame_other_text = CharField(max_length=1000, null=True)

    time_frame_2_target_year = BooleanField(verbose_name="target year")
    time_frame_2_transformation_path = BooleanField(verbose_name="transformation path")
    tools_models = ForeignKey(
        to="Energymodel",
        verbose_name="Tools",
        help_text="Which model(s) and other tools have been used?",
        null=True,
        on_delete=models.SET_NULL
    )
    tools_other = CharField(
        verbose_name="Tools",
        help_text="Which model(s) and other tools have been used?",
        max_length=1000,
        null=True,
    )
    modeled_energy_sectors_electricity = BooleanField(verbose_name="electricity")
    modeled_energy_sectors_heat = BooleanField(verbose_name="heat")
    modeled_energy_sectors_liquid_fuels = BooleanField(verbose_name="liquid fuels")
    modeled_energy_sectors_gas = BooleanField(verbose_name="gas")
    modeled_energy_sectors_others = BooleanField(verbose_name="others")
    modeled_energy_sectors_others_text = CharField(max_length=1000, null=True)

    modeled_demand_sectors_households = BooleanField(verbose_name="households")
    modeled_demand_sectors_industry = BooleanField(verbose_name="industry")
    modeled_demand_sectors_commercial_sector = BooleanField(
        verbose_name="commercial sector"
    )
    modeled_demand_sectors_transport = BooleanField(verbose_name="transport")

    economic_behavioral_perfect = BooleanField(
        verbose_name="single fictive decision-maker with perfect knowledge (perfect foresight optimization)"
    )

    economic_behavioral_myopic = BooleanField(
        verbose_name="single fictive decision-maker with myopic foresight (time-step optimization)"
    )
    economic_behavioral_qualitative = BooleanField(
        verbose_name="decisions simulated by modeller due to qualitative criteria (spread-sheet simulation)"
    )
    economic_behavioral_agentbased = BooleanField(
        verbose_name="representation of heterogenous decision rules for multiple agents (agent-based approach)"
    )
    economic_behavioral_other = BooleanField(verbose_name="other")
    economic_behavioral_other_text = CharField(max_length=1000, null=True)

    renewables_PV = BooleanField(verbose_name="PV")
    renewables_wind = BooleanField(verbose_name="wind")
    renewables_hydro = BooleanField(verbose_name="hydro")
    renewables_biomass = BooleanField(verbose_name="biomass")
    renewables_biogas = BooleanField(verbose_name="biogas")
    renewables_solar = BooleanField(verbose_name="solar thermal")
    renewables_others = BooleanField(verbose_name="others")
    renewables_others_text = CharField(max_length=1000, null=True)

    conventional_generation_gas = BooleanField(verbose_name="gas")
    conventional_generation_coal = BooleanField(verbose_name="coal")
    conventional_generation_oil = BooleanField(verbose_name="oil")
    conventional_generation_liquid = BooleanField(verbose_name="liquid fuels")
    conventional_generation_nuclear = BooleanField(verbose_name="nuclear")

    CHP = BooleanField(verbose_name="CHP")

    networks_electricity_gas_electricity = BooleanField(verbose_name="electricity")
    networks_electricity_gas_gas = BooleanField(verbose_name="gas")
    networks_electricity_gas_heat = BooleanField(verbose_name="heat")

    storages_battery = BooleanField(verbose_name="battery")
    storages_kinetic = BooleanField(verbose_name="kinetic")
    storages_CAES = BooleanField(verbose_name="compressed air")
    storages_PHS = BooleanField(verbose_name="pump hydro")
    storages_chemical = BooleanField(verbose_name="chemical")

    economic_focuses_included = CharField(
        verbose_name="Economic focuses included",
        help_text="Have there been economic focusses/sectors included?",
        max_length=1000,
        null=True,
    )
    social_focuses_included = CharField(
        verbose_name="Social focuses included",
        help_text="Have there been social focusses/sectors included? ",
        max_length=1000,
        null=True,
    )
    endogenous_variables = CharField(
        verbose_name="Endogenous variables",
        help_text="Which time series and variables are generated inside the model?",
        max_length=1000,
        null=True,
    )
    sensitivities = BooleanField(
        verbose_name="Sensitivities", help_text="Have there been sensitivities?"
    )
    time_steps_anual = BooleanField(verbose_name="anual")
    time_steps_hour = BooleanField(verbose_name="hour")
    time_steps_15_min = BooleanField(verbose_name="15 min")
    time_steps_1_min = BooleanField(verbose_name="1 min")
    time_steps_sec = BooleanField(verbose_name="sec")
    time_steps_other = BooleanField(verbose_name="other")
    time_steps_other_text = CharField(max_length=1000, null=True)

class Energyscenario(models.Model):

    study = ForeignKey(
        "Energystudy", db_column="name_of_the_study_id", null=True, blank=True, on_delete=models.CASCADE
    )

    exogenous_time_series_used_climate = BooleanField(verbose_name="climate")
    exogenous_time_series_used_feedin = BooleanField(verbose_name="feed-in")
    exogenous_time_series_used_loadcurves = BooleanField(verbose_name="load-curves")
    exogenous_time_series_used_others = BooleanField(verbose_name="others")
    exogenous_time_series_used_others_text = CharField(max_length=1000, null=True)

    technical_data = CharField(
        verbose_name="Technical data + usage",
        help_text="What kind of technical data(sets) are included /used? (heat-/powerplants; grid infrastructure;...) What were the data(sets) used for (e.g. model calibration)?",
        max_length=1000,
        null=True,
    )
    social_data = CharField(
        verbose_name="Social data",
        help_text="What kind of social data(sets) are included / were used / considered? (e.g. demographic changes, employment rate; social structure, ...) What were the data(sets) used for (e.g. model calibration)?",
        max_length=1000,
        null=True,
    )
    economical_data = CharField(
        verbose_name="Economical data",
        help_text="What kind of economical data(sets) are included / were used? (e.g. price structures, market settings,...) What were the data(sets) used for (e.g. model calibration)?",
        max_length=1000,
        null=True,
    )
    ecological_data = CharField(
        verbose_name="Ecological data",
        help_text="What kind of ecological data(sets) are included / were used? (e.g. landuse, CO2 emissions,...) What were the data(sets) used for (e.g. model calibration)?",
        max_length=1000,
        null=True,
    )
    preProcessing = CharField(
        verbose_name="Pre-Processing",
        help_text="Have the mentioned values been modified before being used for the modelling exercise or are they used directly? Please, describe what kind of modification have been made? Additionally, you can link to data processing scripts.",
        max_length=1000,
        null=True,
    )
    name_of_scenario = CharField(
        verbose_name="Name of the Scenario",
        help_text="What is the name of the scenario?",
        max_length=1000,
        unique=True,
    )

    energy_saving_amount = SmallIntegerField(
        verbose_name="Energy savings",
        help_text="development of energy savings or efficiency",
        null=True,
    )
    energy_saving_kind = CharField(
        max_length=15,
        choices=(
            ("until", "until"),
            ("per", "per"),
            ("not estimated", "not estimated"),
        ),
        default="not estimated",
        null=True,
    )
    energy_saving_year = SmallIntegerField(null=True)

    potential_energy_savings_amount = SmallIntegerField(
        verbose_name="Potential energy saving",
        help_text="How was the potential of energy savings determined?",
        null=True,
    )
    potential_energy_savings_kind = CharField(
        max_length=15,
        choices=(
            ("until", "until"),
            ("per", "per"),
            ("not estimated", "not estimated"),
        ),
        default="not estimated",
        null=True,
    )
    potential_energy_savings_year = SmallIntegerField(null=True)

    emission_reductions_amount = SmallIntegerField(
        verbose_name="Emission reductions",
        help_text="Development of emissions",
        null=True,
    )
    emission_reductions_kind = CharField(
        max_length=15,
        choices=(
            ("until", "until"),
            ("per", "per"),
            ("not estimated", "not estimated"),
        ),
        default="not estimated",
        null=True,
    )
    emission_reductions_year = SmallIntegerField(null=True)

    share_RE_power_amount = SmallIntegerField(
        verbose_name="Share RE (power sector)",
        help_text="Development of renewable energy in the power sector",
        null=True,
    )
    share_RE_power_kind = CharField(
        max_length=15,
        choices=(
            ("until", "until"),
            ("per", "per"),
            ("not estimated", "not estimated"),
        ),
        default="not estimated",
        null=True,
    )
    share_RE_power_year = SmallIntegerField(null=True)

    share_RE_heat_amount = SmallIntegerField(
        verbose_name="Share RE (heat sector)",
        help_text="development of renewable energy in the heat sector",
        null=True,
    )
    share_RE_heat_kind = CharField(
        max_length=15,
        choices=(
            ("until", "until"),
            ("per", "per"),
            ("not estimated", "not estimated"),
        ),
        default="not estimated",
        null=True,
    )
    share_RE_heat_year = SmallIntegerField(null=True)

    share_RE_mobility_amount = SmallIntegerField(
        verbose_name="Share RE (mobility sector)",
        help_text="development of renewable energy in the mobility sector",
        null=True,
    )
    share_RE_mobility_kind = CharField(
        max_length=15,
        choices=(
            ("until", "until"),
            ("per", "per"),
            ("not estimated", "not estimated"),
        ),
        default="not estimated",
        null=True,
    )
    share_RE_mobility_year = SmallIntegerField(null=True)

    share_RE_total_amount = SmallIntegerField(
        verbose_name="Share RE (total energy supply)",
        help_text="development of total renewable energy supply",
        null=True,
    )
    share_RE_total_kind = CharField(
        max_length=15,
        choices=(
            ("until", "until"),
            ("per", "per"),
            ("not estimated", "not estimated"),
        ),
        default="not estimated",
        null=True,
    )
    share_RE_total_year = SmallIntegerField(null=True)

    cost_development_capex = BooleanField(verbose_name="capex")
    cost_development_opex = BooleanField(verbose_name="opex")
    cost_development_learning_curves = BooleanField(verbose_name="learning curves")
    cost_development_constant = BooleanField(verbose_name="constant")
    cost_development_rediscount = BooleanField(verbose_name="rediscount")

    technological_innovations = CharField(
        verbose_name="Technological innovations",
        help_text="Have future technological innovations been regarded?",
        max_length=10000,
        null=True,
    )

    potential_wind_whole = BooleanField(verbose_name="whole")
    potential_wind_technical = BooleanField(verbose_name="technical")
    potential_wind_economical = BooleanField(verbose_name="economical")
    potential_wind_ecological = BooleanField(verbose_name="ecological")
    potential_wind_other = BooleanField(verbose_name="other")
    potential_wind_other_text = CharField(max_length=1000, null=True)

    potential_solar_electric_whole = BooleanField(verbose_name="whole")
    potential_solar_electric_technical = BooleanField(verbose_name="technical")
    potential_solar_electric_economical = BooleanField(verbose_name="economical")
    potential_solar_electric_ecological = BooleanField(verbose_name="ecological")
    potential_solar_electric_other = BooleanField(verbose_name="other")
    potential_solar_electric_other_text = CharField(max_length=1000, null=True)

    potential_solar_thermal_whole = BooleanField(verbose_name="whole")
    potential_solar_thermal_technical = BooleanField(verbose_name="technical")
    potential_solar_thermal_economical = BooleanField(verbose_name="economical")
    potential_solar_thermal_ecological = BooleanField(verbose_name="ecological")
    potential_solar_thermal_other = BooleanField(verbose_name="other")
    potential_solar_thermal_other_text = CharField(max_length=1000, null=True)

    potential_biomass_whole = BooleanField(verbose_name="whole")
    potential_biomass_technical = BooleanField(verbose_name="technical")
    potential_biomass_economical = BooleanField(verbose_name="economical")
    potential_biomass_ecological = BooleanField(verbose_name="ecological")
    potential_biomass_other = BooleanField(verbose_name="other")
    potential_biomass_other_text = CharField(max_length=1000, null=True)

    potential_geothermal_whole = BooleanField(verbose_name="whole")
    potential_geothermal_technical = BooleanField(verbose_name="technical")
    potential_geothermal_economical = BooleanField(verbose_name="economical")
    potential_geothermal_ecological = BooleanField(verbose_name="ecological")
    potential_geothermal_other = BooleanField(verbose_name="other")
    potential_geothermal_othertext = CharField(max_length=1000, null=True)

    potential_hydro_power_whole = BooleanField(verbose_name="whole")
    potential_hydro_power_technical = BooleanField(verbose_name="technical")
    potential_hydro_power_economical = BooleanField(verbose_name="economical")
    potential_hydro_power_ecological = BooleanField(verbose_name="ecological")
    potential_hydro_power_other = BooleanField(verbose_name="other")
    potential_hydro_power_other_text = CharField(max_length=1000, null=True)

    social_developement = CharField(
        verbose_name="Social developement",
        help_text="How are changes of social structure considered? (e.g. demographic changes, employment rate, ...)",
        max_length=1000,
        null=True,
    )
    economic_development = CharField(
        verbose_name="Economic development",
        help_text="e.g. price structures, market settings,..",
        max_length=1000,
        null=True,
    )
    development_of_environmental_aspects = CharField(
        verbose_name="Development of environmental aspects",
        help_text="e.g. landuse",
        max_length=1000,
        null=True,
    )
    postprocessing = BooleanField(
        verbose_name="Post-processing",
        help_text="Are the presented results directly taken from the models’ outcome or are they modified?",
    )
    further_assumptions_for_postprocessing = BooleanField(
        verbose_name="Further assumptions for post-processing",
        help_text="Are additional assumptions applied for this modification?",
    )
    further_assumptions_for_postprocessing_text = CharField(max_length=1000, null=True)
    uncertainty_assessment = CharField(
        verbose_name="Uncertainty assessment",
        help_text="How are the identified uncertain factors considered in the study?",
        max_length=1000,
        null=True,
    )
    robustness = CharField(
        verbose_name="Robustness",
        help_text="How is the robustness of the results proofed?",
        max_length=1000,
        null=True,
    )
    comparability_Validation = CharField(
        verbose_name="Comparability / Validation",
        help_text="How far do the modelling results fit in compared to similar scientific research?",
        max_length=1000,
        null=True,
    )
    conclusions = CharField(
        verbose_name="Conclusions",
        help_text="What political, social (or in another way) relevant conclusions are drawn from the scenario analysis? ",
        max_length=1000,
        null=True,
    )
