import yaml
import os

#with open(os.path.join(sys.path[0], 'config', "config.yml"), "r") as ymlfile:
with open(os.path.join(__file__, "..","config.yml"), "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

#print(cfg)

#REP_BASED_ACTIVITIES = ['squats', 'push-ups'] # List of activities
#TIME_BASED_ACTIVITIES = ['walk', 'run']
REP_BASED_ACTIVITIES = cfg['REP_BASED_ACTIVITIES']
TIME_BASED_ACTIVITIES = cfg['TIME_BASED_ACTIVITIES']
ACTIVITIES = {
    'REP_BASED_ACTIVITIES' : [REP_BASED_ACTIVITIES, 'rep'],
    'TIME_BASED_ACTIVITIES' : [TIME_BASED_ACTIVITIES, 'minutes']
    }
REP_COUNT = [5,10,15] # number of reps

ALERT_FILE = cfg['ALERT_FILE'][0]