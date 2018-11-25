#!/usr/bin/env python3

"""
BORIS
Behavioral Observation Research Interactive Software
Copyright 2012-2018 Olivier Friard

This file is part of BORIS.

  BORIS is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 3 of the License, or
  any later version.

  BORIS is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not see <http://www.gnu.org/licenses/>.

"""


programName = "eMOC"

project_format_version = "4.0"

VLC_MIN_VERSION = "2"

CHECK_NEW_VERSION_DELAY = 15 * 24 * 60 * 60

#FFMPEG_BIN = 'ffmpeg'

function_keys = {16777264: 'F1', 16777265: 'F2', 16777266: 'F3', 16777267: 'F4', 16777268: 'F5',
                 16777269: 'F6', 16777270: 'F7', 16777271: 'F8', 16777272: 'F9', 16777273: 'F10',
                 16777274: 'F11', 16777275: 'F12'}

PROJECT_NAME = "project_name"
PROJECT_DATE = "project_date"
PROJECT_DESCRIPTION = "project_description"

OBSERVATIONS = 'observations'
EVENTS = 'events'
TIME_OFFSET = 'time offset'
TIME_OFFSET_SECOND_PLAYER='time offset second player'

SUBJECTS = 'subjects_conf'
ETHOGRAM = 'behaviors_conf'
BEHAVIORAL_CATEGORIES = "behavioral_categories"

CODING_MAP_RESIZE_W = 640
CODING_MAP_RESIZE_H = 640

POINT_EVENT_PLOT_DURATION = 0.010
POINT_EVENT_PLOT_COLOR = "black"

subjects_config = ['key', 'id']

subjectsFields = ['key', 'name', 'description']

UNPAIRED = 'UNPAIRED'

YES = "Yes"
NO = "No"
CANCEL = "Cancelar"
REMOVE = "Remove"
SAVE = "Salvar"
DISCARD = "Descartar"
OK = "OK"

NO_FOCAL_SUBJECT = 'No focal subject'

TYPE = "type"
FILE = "file"

PLOT_DATA = "plot_data"

PLOT_DATA_FILEPATH_IDX = 0
PLOT_DATA_COLUMNS_IDX = 1
PLOT_DATA_PLOTTITLE_IDX = 2
PLOT_DATA_VARIABLENAME_IDX = 3
PLOT_DATA_CONVERTERS_IDX = 4
PLOT_DATA_TIMEINTERVAL_IDX = 5
PLOT_DATA_TIMEOFFSET_IDX = 6
PLOT_DATA_SUBSTRACT1STVALUE_IDX = 7
PLOT_DATA_PLOTCOLOR_IDX = 8

DATA_PLOT_FIELDS = {PLOT_DATA_FILEPATH_IDX: "file_path",
                    PLOT_DATA_COLUMNS_IDX: "columns",
                    PLOT_DATA_PLOTTITLE_IDX: "title",
                    PLOT_DATA_VARIABLENAME_IDX: "variable_name",
                    PLOT_DATA_CONVERTERS_IDX: "converters",
                    PLOT_DATA_TIMEINTERVAL_IDX: "time_interval",
                    PLOT_DATA_TIMEOFFSET_IDX: "time_offset",
                    PLOT_DATA_SUBSTRACT1STVALUE_IDX: "substract_first_value",
                    PLOT_DATA_PLOTCOLOR_IDX: "color"
                    }
DATA_PLOT_STYLES = ["b-", "r-", "g-", "bo", "ro", "go"]

BEHAVIOR_CODE = "key"
BEHAVIOR_CATEGORY = "category"

# fields for event configuration
#fields = {'type': 0, 'key': 1, 'code': 2, 'description': 3, 'modifiers': 4, 'excluded': 5, 'coding map': 6}
fields = {'type': 0, 'key': 1, 'description': 2, 'category': 3, 'modifiers': 4}

#behav_fields_in_mainwindow = {0: "key", 1: "code", 2: "type", 3: "description", 4:"category", 5:"modifiers", 6:"excluded"}
behav_fields_in_mainwindow = {'type': 0, 'key': 1, 'description': 2, 'category': 3, 'modifiers': 4}

# fields in ethogram table from project window
#behavioursFields = {'type': 0, 'key': 1, 'code': 2, 'description': 3, 'category': 4, 'modifiers': 5, 'excluded': 6, 'coding map': 7}
behavioursFields = {'type': 0, 'key': 1, 'description': 2, 'category': 3, 'modifiers': 4}

#BEHAVIOR_TYPES = ["Point event", "State event", "Point event with coding map", "State event with coding map"]
BEHAVIOR_TYPES = ["Crença", "Coordenação", "Comunicação", "Cooperação", "Percepção", "Intenção de Compartilhar"]

BEHAVIOR_BARRIERS = {"Crença": ["Capacidade de absorção", "Interação infreqüente", "Confiança", "Personalidade individual", "Características interpessoais", "Fatores motivacionais", "Capacidade de absorção" , "Transferência efetiva de conhecimento", "Proficiência em conhecimento", "Atitudes"],
                     "Coordenação": ["Baixa capacidade de trabalho", "Diversidade", "Redes sociais", "Esforço", "Certificar", "Dificuldade em transferir o conhecimento", "planejar"],
                     "Comunicação": ["Falta de transparência", "Falta de estratégias", "Falta de compartilhamento de conhecimento", "Confusão", "Relações difíceis", "Comunicação", "Ajudar", "Conversar", "Falta de habilidades", "Negociar"],
                     "Cooperação": ["Apatia laboral", "Falta de reciprocidade", "Processos em equipe", "Convergência", "Ensinar", "Permitir"],
                     "Percepção": ["Não identifica o valor da informação;", "Argumentar"],
                     "Intenção de Compartilhar": ["Confiabilidade", "Alertar", "Convidar", "Dificuldade em transferir o conhecimento", "Proteger seus próprios conhecimentos", "Impor"]}

DEFAULT_BEHAVIOR_TYPE = "Crença"

# fields for events table
#tw_events_fields = ['time', 'subject', 'code', 'type', 'modifier', 'comment']
tw_events_fields = ['Tempo', 'Sujeito', 'Chave', 'Tipo', 'Modificador', 'Barreira']

# fields for project events list
#pj_events_fields = ["time", "subject", "code", "modifier", "comment"]
pj_events_fields = ['Tempo', 'Sujeito', 'Chave', 'Tipo', 'Modificador', 'Barreira']

tw_indVarFields = ["label", "description", "type", "default value", "possible values"]

BEHAV_CODING_MAP_FIELDS = ["name", "Behavior codes"]

EXCEL_FORBIDDEN_CHARACTERS = r"\/*[]:?"

# create dictionaries
tw_obs_fields, pj_obs_fields = {}, {}

for idx, field in enumerate(tw_events_fields):
    tw_obs_fields[ field ] = idx


for idx, field in enumerate(pj_events_fields):
    pj_obs_fields[ field ] = idx


EVENT_TIME_FIELD_IDX = 0

SUBJECT_EVENT_FIELD = 1       # to be removed after check
EVENT_SUBJECT_FIELD_IDX = 1

BEHAVIOR_EVENT_FIELD = 2
EVENT_BEHAVIOR_FIELD_IDX = 2

EVENT_MODIFIER_FIELD_IDX = 3

EVENT_COMMENT_FIELD_IDX = 4

SUBJECT_NAME_FIELD_IDX = 1

LIVE = 'LIVE'
MEDIA = 'MEDIA'
VIEWER = 'VIEWER'

HHMMSS = 'hh:mm:ss'
HHMMSSZZZ = "hh:mm:ss.zzz"
S = 's'

NEW = 'new'
LIST = 'list'
EDIT = 'edit'
OPEN = 'open'
VIEW = "view"
SELECT = 'select'
SINGLE = 'single'
MULTIPLE = 'multiple'

SELECT1 = 'select1'

FILTERED_BEHAVIORS = "filtered behaviors"


# indep variables
NUMERIC = "numeric"
NUMERIC_idx = 0
TEXT = "text"
TEXT_idx = 1
SET_OF_VALUES = "value from set"
SET_OF_VALUES_idx = 2
TIMESTAMP = "timestamp"
TIMESTAMP_idx = 3


TIME_FULL_OBS = "full obs"
TIME_EVENTS = "limit to events"
TIME_ARBITRARY_INTERVAL = "time interval"

AVAILABLE_INDEP_VAR_TYPES = [NUMERIC, TEXT, SET_OF_VALUES, TIMESTAMP]


INDEPENDENT_VARIABLES = 'independent_variables'
OBSERVATIONS = 'observations'

CLOSE_BEHAVIORS_BETWEEN_VIDEOS = "close_behaviors_between_videos"

OPENCV = 'opencv'
VLC = 'vlc'
FFMPEG = 'ffmpeg'

MEDIA_FILE_INFO = "media_file_info"

STATE = "STATE"
POINT = "POINT"

START = "START"
STOP = "STOP"

PLAYER1, PLAYER2 = "1", "2"
ALL_PLAYERS = [PLAYER1, PLAYER2]

POINT_EVENT_ST_DURATION = 0.5

VIDEO_TAB = 0
FRAME_TAB = 1

slider_maximum = 1000

FRAME_BITMAP_FORMAT_LIST = ["JPG", "PNG"]
FRAME_DEFAULT_BITMAP_FORMAT = "JPG"

FRAME_DEFAULT_CACHE_SIZE = 1

# modifiers
MODIFIERS = "modifiers"
SINGLE_SELECTION = 0
MULTI_SELECTION = 1
NUMERIC_MODIFIER = 2

MODIFIERS_STR = {SINGLE_SELECTION: "Single item selection", MULTI_SELECTION: "Multiple items selection", NUMERIC_MODIFIER: "Numeric"}

#colors
subtitlesColors = ['cyan','red','blue','yellow','fuchsia','orange', 'lime', 'green']

CATEGORY_COLORS_LIST = ["#FF96CC", "#96FF9C","#CCFFFE", "#EEFF70", "#FF4F64", "#F8BF15", "#3DC7AD"]

SPECTROGRAM_COLOR_MAPS = ['viridis','inferno','plasma', 'magma', "gray", "YlOrRd"]
SPECTROGRAM_DEFAULT_COLOR_MAP = 'viridis'

# see matplotlib.colors.cnames.keys()
# https://xkcd.com/color/rgb/

# sage colors are no more available 
# darksage #598556
# lightsage #bcecac
# sage #87ae73


BEHAVIORS_PLOT_COLORS = ['tab:blue',
                         'tab:orange',
                         'tab:green',
                         'tab:red',
                         'tab:purple',
                         'tab:brown',
                         'tab:pink',
                         'tab:gray',
                         'tab:olive',
                         'tab:cyan',
                         "blue", "green", "red", "cyan", "magenta","yellow", "lime",
                         "darksalmon", "purple", "orange", "maroon", "silver",
                         "slateblue", "hotpink", "steelblue", "darkgoldenrod",
                         'aqua','aquamarine',
                         'beige','bisque','black','blanchedalmond','blueviolet','brown',
                         'burlywood','cadetblue','chartreuse','chocolate','coral',
                         'cornflowerblue','cornsilk','crimson','darkblue','darkcyan',
                         'darkgreen','darkgrey','darkkhaki','darkmagenta',
                         'darkolivegreen','darkorange','darkorchid','darkred',
                         '#598556','darkseagreen','darkslateblue','darkslategray',
                         'darkslategrey','darkturquoise','darkviolet','deeppink',
                         'deepskyblue','dimgray','dimgrey','dodgerblue','firebrick',
                         'floralwhite','forestgreen','fuchsia','gainsboro',
                         'gold','goldenrod','gray','greenyellow','grey','honeydew',
                         'indianred','indigo','khaki',
                         'lawngreen','lemonchiffon','lightblue','lightcoral',
                         'lightgoldenrodyellow','lightgray','lightgreen','lightgrey',
                         'lightpink','#bcecac','lightsalmon','lightseagreen',
                         'lightskyblue','lightslategray','lightslategrey','lightsteelblue',
                         'lightyellow','limegreen','linen','mediumaquamarine','mediumblue',
                         'mediumorchid','mediumpurple','mediumseagreen','mediumslateblue',
                         'mediumspringgreen','mediumturquoise','mediumvioletred',
                         'midnightblue','mintcream','mistyrose','moccasin','navajowhite',
                         'navy','oldlace','olive','olivedrab','orangered','orchid',
                         'palegoldenrod','palegreen','paleturquoise','palevioletred',
                         'papayawhip','peachpuff','peru','pink','plum','powderblue','rosybrown',
                         'royalblue','saddlebrown','#87ae73','salmon','sandybrown','seagreen',
                         'seashell','sienna','skyblue','slategray','slategrey',
                         'springgreen','tan','teal','thistle','tomato','turquoise','violet',
                         'wheat','yellowgreen','darkgray']

EMPTY_PROJECT = {"time_format": HHMMSS,
                       "project_date": "",
                       "project_name": "",
                       "project_description": "",
                       "project_format_version": project_format_version,
                       SUBJECTS: {},
                       ETHOGRAM: {},
                       OBSERVATIONS: {},
                       BEHAVIORAL_CATEGORIES: [],
                       INDEPENDENT_VARIABLES: {}}
