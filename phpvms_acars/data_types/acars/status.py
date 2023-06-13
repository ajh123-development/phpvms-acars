INITIATED = 'INI'
SCHEDULED = 'SCH'
BOARDING = 'BST'
RDY_START = 'RDT'
PUSHBACK_TOW = 'PBT'
DEPARTED = 'OFB' # Off block
RDY_DEICE = 'DIR'
STRT_DEICE = 'DIC'
GRND_RTRN = 'GRT' # Ground return
TAXI = 'TXI' # Taxi
TAKEOFF = 'TOF'
INIT_CLIM = 'ICL'
AIRBORNE = 'TKO'
ENROUTE = 'ENR'
DIVERTED = 'DV'
APPROACH = 'TEN'
APPROACH_ICAO = 'APR'
ON_FINAL = 'FIN'
LANDING = 'LDG'
LANDED = 'LAN'
ARRIVED = 'ONB' # On block
CANCELLED = 'DX'
EMERG_DESCENT = 'EMG'
PAUSED = 'PSD'

labels = {
	INITIATED     : 'pireps.status.initialized',
	SCHEDULED     : 'pireps.status.scheduled',
	BOARDING      : 'pireps.status.boarding',
	RDY_START     : 'pireps.status.ready_start',
	PUSHBACK_TOW  : 'pireps.status.push_tow',
	DEPARTED      : 'pireps.status.departed',
	RDY_DEICE     : 'pireps.status.ready_deice',
	STRT_DEICE    : 'pireps.status.deicing',
	GRND_RTRN     : 'pireps.status.ground_ret',
	TAXI          : 'pireps.status.taxi',
	TAKEOFF       : 'pireps.status.takeoff',
	INIT_CLIM     : 'pireps.status.initial_clb',
	AIRBORNE      : 'pireps.status.enroute',
	ENROUTE       : 'pireps.status.enroute',
	DIVERTED      : 'pireps.status.diverted',
	APPROACH      : 'pireps.status.approach',
	APPROACH_ICAO : 'pireps.status.approach',
	ON_FINAL      : 'pireps.status.final_appr',
	LANDING       : 'pireps.status.landing',
	LANDED        : 'pireps.status.landed',
	ARRIVED       : 'pireps.status.arrived',
	CANCELLED     : 'pireps.status.cancelled',
	EMERG_DESCENT : 'pireps.status.emerg_decent',
	PAUSED        : 'pireps.status.paused',
}