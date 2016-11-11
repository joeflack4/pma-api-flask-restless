from app import db
from flask_sqlalchemy import declarative_base
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship
# from datetime import datetime
# - Deprecations: flask.ext has been deprecated.
# from sqlalchemy.ext.declarative import declarative_base

db.Base = declarative_base()

# - To Do: Figure out relational mapping.
# user_messages = db.Table('user_messages', db.Base.metadata,
#     db.Column('user_id', db.Integer, ForeignKey('user.id')),
#     db.Column('messages_id', db.Integer, ForeignKey('messages.id'))
# )


##############
# - Super Classes
class BaseModel(db.Model):
    __abstract__ = True

    created_on = db.Column(db.DateTime, default=db.func.now(), index=True)
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), index=True)


class BaseConfig(BaseModel):
    __abstract__ = True

    key = db.Column(db.String(100), primary_key=True, nullable=False)
    value = db.Column(db.String(200), nullable=False)
    permission_level = db.Column(db.Integer, nullable=False, index=True)
    active = db.Column(db.Boolean, nullable=False, index=True)

    def __init__(self, key, value, permission_level, active):
        self.key = key
        self.value = value
        self.permission_level = permission_level
        self.active = active

    def __repr__(self):
        return '<key name: {}>'.format(self.key)


##############
# - App Core Models
class AppConfig(BaseConfig):
    __tablename__ = 'app_config'


##############
# - Test Models
class EthiopiaRound2SDP(BaseModel):
    __tablename__ = 'Ethiopia_Round2_SDP'

    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    SubmissionDate = db.Column(db.String(500))
    SubmissionDateSIF = db.Column(db.String(500))
    times_visited = db.Column(db.String(500))
    RE = db.Column(db.String(500))
    region = db.Column(db.String(500))
    zone = db.Column(db.String(500))
    district = db.Column(db.String(500))
    locality = db.Column(db.String(500))
    EArandom = db.Column(db.String(500))
    EA = db.Column(db.String(500))
    facility_number = db.Column(db.String(500))
    facility_type = db.Column(db.String(500))
    advanced_facility = db.Column(db.String(500))
    managing_authority = db.Column(db.String(500))
    available = db.Column(db.String(500))
    consent_obtained = db.Column(db.String(500))
    facility_name = db.Column(db.String(500))
    position = db.Column(db.String(500))
    year_open = db.Column(db.String(500))
    year_openSIF = db.Column(db.String(500))
    days_open = db.Column(db.String(500))
    staffing_doctor_tot = db.Column(db.String(500))
    staffing_doctor_here = db.Column(db.String(500))
    staffing_nurse_tot = db.Column(db.String(500))
    staffing_nurse_here = db.Column(db.String(500))
    staffing_ho_tot = db.Column(db.String(500))
    staffing_ho_here = db.Column(db.String(500))
    staffing_ambulance_tot = db.Column(db.String(500))
    staffing_ambulance_here = db.Column(db.String(500))
    staffing_pharmacist_tot = db.Column(db.String(500))
    staffing_pharmacist_here = db.Column(db.String(500))
    staffing_mca_tot = db.Column(db.String(500))
    staffing_mca_here = db.Column(db.String(500))
    staffing_other_tot = db.Column(db.String(500))
    staffing_other_here = db.Column(db.String(500))
    present_24hr = db.Column(db.String(500))
    knows_population_served = db.Column(db.String(500))
    population_served = db.Column(db.String(500))
    beds = db.Column(db.String(500))
    supervisor_visit = db.Column(db.String(500))
    electricity = db.Column(db.String(500))
    water = db.Column(db.String(500))
    handwashing_stations = db.Column(db.String(500))
    handwashing_observations = db.Column(db.String(500))
    soap_present = db.Column(db.String(500))
    stored_water_present = db.Column(db.String(500))
    running_water_present = db.Column(db.String(500))
    near_sanitation = db.Column(db.String(500))
    computer = db.Column(db.String(500))
    sharps = db.Column(db.String(500))
    fp_offered = db.Column(db.String(500))
    fp_begin = db.Column(db.String(500))
    fp_beginSIF = db.Column(db.String(500))
    fp_days = db.Column(db.String(500))
    fp_today = db.Column(db.String(500))
    fp_community_health_volunteers = db.Column(db.String(500))
    community_health_volunteers = db.Column(db.String(500))
    methods_offered = db.Column(db.String(500))
    chv_condoms = db.Column(db.String(500))
    chv_pills = db.Column(db.String(500))
    chv_injectables = db.Column(db.String(500))
    mobile_outreach = db.Column(db.String(500))
    fees = db.Column(db.String(500))
    fees_posted = db.Column(db.String(500))
    opinions_collected = db.Column(db.String(500))
    opinion_box = db.Column(db.String(500))
    opinion_survey = db.Column(db.String(500))
    opinion_interview = db.Column(db.String(500))
    opinion_meeting = db.Column(db.String(500))
    opinion_informal = db.Column(db.String(500))
    opinion_direct = db.Column(db.String(500))
    opinion_other = db.Column(db.String(500))
    opinions_reported = db.Column(db.String(500))
    opinions_observed = db.Column(db.String(500))
    opinion_action = db.Column(db.String(500))
    opinion_no_change = db.Column(db.String(500))
    opinion_change_in_service = db.Column(db.String(500))
    opinion_change_in_comfort = db.Column(db.String(500))
    opinion_change_other = db.Column(db.String(500))
    service_stats = db.Column(db.String(500))
    stats_analyzed = db.Column(db.String(500))
    reports_wall_chart = db.Column(db.String(500))
    reports_written = db.Column(db.String(500))
    reports_other = db.Column(db.String(500))
    reports_nothing = db.Column(db.String(500))
    offered_female_ster = db.Column(db.String(500))
    offered_male_ster = db.Column(db.String(500))
    offered_implants = db.Column(db.String(500))
    offered_iud = db.Column(db.String(500))
    offered_injectables = db.Column(db.String(500))
    offered_pills = db.Column(db.String(500))
    offered_progestin_pill = db.Column(db.String(500))
    offered_male_condom = db.Column(db.String(500))
    offered_female_condom = db.Column(db.String(500))
    offered_ec = db.Column(db.String(500))
    offered_beads = db.Column(db.String(500))
    offered_lam = db.Column(db.String(500))
    offered_rhythm = db.Column(db.String(500))
    offered_withdrawal = db.Column(db.String(500))
    counseled_female_ster = db.Column(db.String(500))
    counseled_male_ster = db.Column(db.String(500))
    counseled_implants = db.Column(db.String(500))
    counseled_iud = db.Column(db.String(500))
    counseled_injectables = db.Column(db.String(500))
    counseled_progestin = db.Column(db.String(500))
    counseled_pills = db.Column(db.String(500))
    counseled_male_condom = db.Column(db.String(500))
    counseled_female_condom = db.Column(db.String(500))
    counseled_ec = db.Column(db.String(500))
    counseled_beads = db.Column(db.String(500))
    counseled_lam = db.Column(db.String(500))
    counseled_rhythm = db.Column(db.String(500))
    counseled_withdrawal = db.Column(db.String(500))
    provided_female_ster = db.Column(db.String(500))
    provided_male_ster = db.Column(db.String(500))
    provided_implants = db.Column(db.String(500))
    provided_iud = db.Column(db.String(500))
    provided_injectables = db.Column(db.String(500))
    provided_progestin = db.Column(db.String(500))
    provided_pills = db.Column(db.String(500))
    provided_male_condom = db.Column(db.String(500))
    provided_female_condom = db.Column(db.String(500))
    provided_ec = db.Column(db.String(500))
    provided_beads = db.Column(db.String(500))
    prescribed_female_ster = db.Column(db.String(500))
    prescribed_male_ster = db.Column(db.String(500))
    prescribed_implants = db.Column(db.String(500))
    prescribed_iud = db.Column(db.String(500))
    prescribed_injectables = db.Column(db.String(500))
    prescribed_progestin = db.Column(db.String(500))
    prescribed_pills = db.Column(db.String(500))
    prescribed_male_condom = db.Column(db.String(500))
    prescribed_female_condom = db.Column(db.String(500))
    prescribed_ec = db.Column(db.String(500))
    prescribed_beads = db.Column(db.String(500))
    charged_female_ster = db.Column(db.String(500))
    charged_male_ster = db.Column(db.String(500))
    charged_implants = db.Column(db.String(500))
    charged_iud = db.Column(db.String(500))
    charged_injectables = db.Column(db.String(500))
    charged_progestin = db.Column(db.String(500))
    charged_pills = db.Column(db.String(500))
    charged_male_condom = db.Column(db.String(500))
    charged_female_condom = db.Column(db.String(500))
    charged_ec = db.Column(db.String(500))
    charged_beads = db.Column(db.String(500))
    fees_female_ster = db.Column(db.String(500))
    fees_male_ster = db.Column(db.String(500))
    fees_implants = db.Column(db.String(500))
    fees_iud = db.Column(db.String(500))
    fees_injectables = db.Column(db.String(500))
    fees_pills = db.Column(db.String(500))
    fees_progestin = db.Column(db.String(500))
    fees_male_condom = db.Column(db.String(500))
    fees_female_condom = db.Column(db.String(500))
    fees_ec = db.Column(db.String(500))
    fees_beads = db.Column(db.String(500))
    implant_insert = db.Column(db.String(500))
    implant_remove = db.Column(db.String(500))
    iud_insert = db.Column(db.String(500))
    iud_remove = db.Column(db.String(500))
    implant_supplies = db.Column(db.String(500))
    implant_gloves = db.Column(db.String(500))
    implant_antiseptic = db.Column(db.String(500))
    implant_sterile_gauze = db.Column(db.String(500))
    implant_anesthetic = db.Column(db.String(500))
    implant_sealed_pack = db.Column(db.String(500))
    implant_blade = db.Column(db.String(500))
    iud_supplies = db.Column(db.String(500))
    iud_forceps = db.Column(db.String(500))
    iud_speculums = db.Column(db.String(500))
    iud_tenaculum = db.Column(db.String(500))
    iud_clamp = db.Column(db.String(500))
    visits_female_ster = db.Column(db.String(500))
    visits_male_ster = db.Column(db.String(500))
    visits_implants_total = db.Column(db.String(500))
    visits_implants_new = db.Column(db.String(500))
    visits_iud_total = db.Column(db.String(500))
    visits_iud_new = db.Column(db.String(500))
    visits_progestin_total = db.Column(db.String(500))
    visits_progestin_new = db.Column(db.String(500))
    visits_injectables_total = db.Column(db.String(500))
    visits_injectables_new = db.Column(db.String(500))
    visits_pills_total = db.Column(db.String(500))
    visits_pills_new = db.Column(db.String(500))
    visits_male_condom_total = db.Column(db.String(500))
    visits_male_condom_new = db.Column(db.String(500))
    visits_female_condom_total = db.Column(db.String(500))
    visits_female_condom_new = db.Column(db.String(500))
    visits_ec_total = db.Column(db.String(500))
    visits_ec_new = db.Column(db.String(500))
    visits_beads_total = db.Column(db.String(500))
    visits_beads_new = db.Column(db.String(500))
    sold_implants = db.Column(db.String(500))
    sold_iud = db.Column(db.String(500))
    sold_injectables = db.Column(db.String(500))
    sold_progestin = db.Column(db.String(500))
    sold_pills = db.Column(db.String(500))
    sold_male_condoms = db.Column(db.String(500))
    sold_female_condoms = db.Column(db.String(500))
    sold_ec = db.Column(db.String(500))
    sold_beads = db.Column(db.String(500))
    maternalservices = db.Column(db.String(500))
    antenatal = db.Column(db.String(500))
    delivery = db.Column(db.String(500))
    postnatal = db.Column(db.String(500))
    post_abortion = db.Column(db.String(500))
    postpartum = db.Column(db.String(500))
    postpartum_diet = db.Column(db.String(500))
    postpartum_mental = db.Column(db.String(500))
    postpartum_fertility = db.Column(db.String(500))
    postpartum_healthy_spacing = db.Column(db.String(500))
    postpartum_lam = db.Column(db.String(500))
    postpartum_long_acting_fp = db.Column(db.String(500))
    postpartum_spacing = db.Column(db.String(500))
    fp_during_postpartum = db.Column(db.String(500))
    postabortion_discussion = db.Column(db.String(500))
    postabortion_mental = db.Column(db.String(500))
    postabortion_fertility = db.Column(db.String(500))
    postabortion_healthy_spacing = db.Column(db.String(500))
    postabortion_long_acting_fp = db.Column(db.String(500))
    postabortion_spacing = db.Column(db.String(500))
    fp_during_postabortion = db.Column(db.String(500))
    adolescents = db.Column(db.String(500))
    adolescents_counseled = db.Column(db.String(500))
    adolescents_provided = db.Column(db.String(500))
    adolescents_prescribed = db.Column(db.String(500))
    hiv_services = db.Column(db.String(500))
    sti_services = db.Column(db.String(500))
    hiv_fp = db.Column(db.String(500))
    hiv_fp_counseled = db.Column(db.String(500))
    hiv_fp_provided = db.Column(db.String(500))
    hiv_fp_prescribed = db.Column(db.String(500))
    hiv_consultation_intentions = db.Column(db.String(500))
    hiv_consultation_method = db.Column(db.String(500))
    hiv_consultation_dual_method = db.Column(db.String(500))
    hiv_consultation_condoms = db.Column(db.String(500))
    hiv_consultation_instructions = db.Column(db.String(500))
    hiv_consultation_fp = db.Column(db.String(500))
    exam_room_piped_water = db.Column(db.String(500))
    exam_room_other_running_water = db.Column(db.String(500))
    exam_room_bucket_water = db.Column(db.String(500))
    exam_room_soap = db.Column(db.String(500))
    exam_room_towels = db.Column(db.String(500))
    exam_room_wastebin = db.Column(db.String(500))
    exam_room_sharps = db.Column(db.String(500))
    exam_room_latex_gloves = db.Column(db.String(500))
    exam_room_disinfectant = db.Column(db.String(500))
    exam_room_needles = db.Column(db.String(500))
    exam_room_auditory_privacy = db.Column(db.String(500))
    exam_room_visual_privacy = db.Column(db.String(500))
    exam_room_tables = db.Column(db.String(500))
    exam_room_ed_materials = db.Column(db.String(500))
    fp_room_conditions_floor = db.Column(db.String(500))
    fp_room_conditions_tables = db.Column(db.String(500))
    fp_room_conditions_equipment = db.Column(db.String(500))
    fp_room_conditions_doors = db.Column(db.String(500))
    fp_room_conditions_walls = db.Column(db.String(500))
    fp_room_conditions_roof = db.Column(db.String(500))
    fp_room_conditions_wallsc = db.Column(db.String(500))
    stock_implants = db.Column(db.String(500))
    stockout_days_implants = db.Column(db.String(500))
    stockout_3mo_implants = db.Column(db.String(500))
    stock_iud = db.Column(db.String(500))
    stockout_days_iud = db.Column(db.String(500))
    stockout_3mo_iud = db.Column(db.String(500))
    stock_injectables = db.Column(db.String(500))
    stockout_days_injectables = db.Column(db.String(500))
    stockout_3mo_injectables = db.Column(db.String(500))
    stock_pills = db.Column(db.String(500))
    stockout_days_pills = db.Column(db.String(500))
    stockout_3mo_pills = db.Column(db.String(500))
    stock_progestin = db.Column(db.String(500))
    stockout_days_progestin = db.Column(db.String(500))
    stockout_3mo_progestin = db.Column(db.String(500))
    stock_male_condoms = db.Column(db.String(500))
    stockout_days_male_condoms = db.Column(db.String(500))
    stockout_3mo_male_condoms = db.Column(db.String(500))
    stock_female_condoms = db.Column(db.String(500))
    stockout_days_female_condoms = db.Column(db.String(500))
    stockout_3mo_female_condoms = db.Column(db.String(500))
    stock_ec = db.Column(db.String(500))
    stockout_days_ec = db.Column(db.String(500))
    stockout_3mo_ec = db.Column(db.String(500))
    stock_beads = db.Column(db.String(500))
    stockout_days_beads = db.Column(db.String(500))
    stockout_3mo_beads = db.Column(db.String(500))
    protected_floor = db.Column(db.String(500))
    protected_water = db.Column(db.String(500))
    protected_sun = db.Column(db.String(500))
    protected_pests = db.Column(db.String(500))
    locationlatitude = db.Column(db.String(500))
    locationlongitude = db.Column(db.String(500))
    locationaltitude = db.Column(db.String(500))
    locationaccuracy = db.Column(db.String(500))
    SDP_result = db.Column(db.String(500))
    start = db.Column(db.String(500))
    startSIF = db.Column(db.String(500))
    end = db.Column(db.String(500))
    endSIF = db.Column(db.String(500))
    metainstanceID = db.Column(db.String(500))
    metainstancename = db.Column(db.String(500))
    RErandom = db.Column(db.String(500))
    facility_type_v2 = db.Column(db.String(500))
    sector = db.Column(db.String(500))
    offer_stock_iud = db.Column(db.String(500))
    offer_stock_implants = db.Column(db.String(500))
    offer_stock_injectables = db.Column(db.String(500))
    offer_stock_pills = db.Column(db.String(500))
    offer_stock_male_condoms = db.Column(db.String(500))
    offer_stock3_iud = db.Column(db.String(500))
    offer_stock3_implants = db.Column(db.String(500))
    offer_stock3_injectables = db.Column(db.String(500))
    offer_stock3_pills = db.Column(db.String(500))
    offer_stock3_male_condoms = db.Column(db.String(500))
    available_iud = db.Column(db.String(500))
    available_implants = db.Column(db.String(500))
    available_injectables = db.Column(db.String(500))
    available_pills = db.Column(db.String(500))
    available_progestin = db.Column(db.String(500))
    available_male_condom = db.Column(db.String(500))
    available_female_condom = db.Column(db.String(500))
    available_ec = db.Column(db.String(500))
    available_beads = db.Column(db.String(500))
    total_methods_available = db.Column(db.String(500))
    threshold_3 = db.Column(db.String(500))
    threshold_5 = db.Column(db.String(500))
    fp_days_mean = db.Column(db.String(500))
    fp_days_mean_total = db.Column(db.String(500))
    adfp = db.Column(db.String(500))
    chws = db.Column(db.String(500))
    mobile_outreach_2 = db.Column(db.String(500))
    mhsoffer = db.Column(db.String(500))
    fpmhs = db.Column(db.String(500))
    fphiv = db.Column(db.String(500))
    fppa = db.Column(db.String(500))
    Probabilityofselection = db.Column(db.String(500))
    FQweight = db.Column(db.String(500))
    EAtag = db.Column(db.String(500))
    EAweight = db.Column(db.String(500))
    _merge = db.Column(db.String(500))

    def __init__(self, id, _merge):
        self.id = id
        self._merge = _merge

    def __repr__(self):
        return '<id: {}>'.format(self.id)
