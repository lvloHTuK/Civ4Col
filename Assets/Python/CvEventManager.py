## Sid Meier's Civilization 4
## Copyright Firaxis Games 2006
##
## CvEventManager
## This class is passed an argsList from CvAppInterface.onEvent
## The argsList can contain anything from mouse location to key info
## The EVENTLIST that are being notified can be found

from CvPythonExtensions import *
import CvUtil
import CvScreensInterface
import CvDebugTools
import CvWBPopups
import CvCameraControls
import sys
import CvWorldBuilderScreen
import CvAdvisorUtils


encoded_chars = {
    # Латиница (заглавные)
    65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I',
    74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R',
    83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z',
    
    # Латиница (строчные)
    97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i',
    106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q', 114: 'r',
    115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z',
    
    # Кириллица (заглавные)
    1040: 'А', 1041: 'Б', 1042: 'В', 1043: 'Г', 1044: 'Д', 1045: 'Е', 1025: 'Ё', 1046: 'Ж',
    1047: 'З', 1048: 'И', 1049: 'Й', 1050: 'К', 1051: 'Л', 1052: 'М', 1053: 'Н', 1054: 'О',
    1055: 'П', 1056: 'Р', 1057: 'С', 1058: 'Т', 1059: 'У', 1060: 'Ф', 1061: 'Х', 1062: 'Ц',
    1063: 'Ч', 1064: 'Ш', 1065: 'Щ', 1066: 'Ъ', 1067: 'Ы', 1068: 'Ь', 1069: 'Э', 1070: 'Ю',
    1071: 'Я',
    
    # Кириллица (строчные)
    1072: 'а', 1073: 'б', 1074: 'в', 1075: 'г', 1076: 'д', 1077: 'е', 1105: 'ё', 1078: 'ж',
    1079: 'з', 1080: 'и', 1081: 'й', 1082: 'к', 1083: 'л', 1084: 'м', 1085: 'н', 1086: 'о',
    1087: 'п', 1088: 'р', 1089: 'с', 1090: 'т', 1091: 'у', 1092: 'ф', 1093: 'х', 1094: 'ц',
    1095: 'ч', 1096: 'ш', 1097: 'щ', 1098: 'ъ', 1099: 'ы', 1100: 'ь', 1101: 'э', 1102: 'ю',
    1103: 'я',
    
    # Цифры
    48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9',
    
    # Основная пунктуация и символы
    32: ' ',  33: '!',  34: '"',  35: '#',  36: '$',  37: '%',  38: '&',  39: "'",  40: '(',  
    41: ')',  42: '*',  43: '+',  44: ',',  45: '-',  46: '.',  47: '/',  58: ':',  59: ';',  
    60: '<',  61: '=',  62: '>',  63: '?',  64: '@',  91: '[',  92: '\\', 93: ']',  94: '^',  
    95: '_',  96: '`',  123: '{', 124: '|', 125: '}', 126: '~',
    
    # Дополнительные спецсимволы
    171: '«', 187: '»', 8230: '…', 8212: '—', 8216: '‘', 8217: '’', 8220: '“', 8221: '”',
    8364: '€', 8470: '№', 8592: '←', 8593: '↑', 8594: '→', 8595: '↓'
}


def decode(encoded_name):
    # Удаляем квадратные скобки с начала и конца строки
    if not encoded_name.startswith('[') or not encoded_name.endswith(']'):
        raise ValueError("Некорректный формат входной строки")
    
    # Извлекаем содержимое между скобками
    content = encoded_name[1:-1]
    
    # Разделяем строку по символу '_'
    codes = content.split('_')
    
    # Декодируем числовые коды в символы
    decoded_name = ""
    for code in codes:
        try:
            # Преобразуем строку в число
            num = int(code)
            # Получаем символ из словаря
            if num in encoded_chars:
                decoded_name += encoded_chars[num]
            else:
                # Если кода нет в словаре, добавляем символ '?'
                decoded_name += '?'
        except ValueError:
            # Если не удалось преобразовать в число, добавляем символ '?'
            decoded_name += '?'
    
    return decoded_name

def encode(name):
    data = []
    for char in name:
        data.append(str(ord(char))) 
     # Преобразуем каждый символ в его числовой код
    return '[%s]' % '_'.join(data)  # Преобразуем список чисел в строку, заключая в квадратные скобки
	


def transliterate(text):
    """
    Простая функция для транслитерации кириллицы в латиницу.
    """
    cyrillic_to_latin = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',  
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '',
        'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo',
        'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M',
        'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': '',
        'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
    }
    return ''.join(cyrillic_to_latin.get(char, char) for char in text)



gc = CyGlobalContext()
localText = CyTranslator()
RES = ['food', 'Lumber','Stone','Hemp','Ore','Sheep','Cattle','Horses','Coca leaves','Cocoa Pods',
	   'Coffee Berries','Tobacco ','Wool','Cotton','Indigo','Cowhides','Fur','Premium fur','Rock salt ',
	   'Red Pepper','Barley','Sugar','Grapes','Whale fat','Valuable wood','Trade goods','Ropes','Sailcloth ',
	   'Tools','Blades','Guns','Cannons','Silver','Gold','Gems','Cocoa','Coffee','Cigars','Wool Cloth','Cloth',
	   'Coloured cloth','Leather','Coats','Premium coats','Salt','Spices','Beer','Rum','Wine','Train oil','Furniture',
	   'Luxury goods']


# Проработать список юнитов в игре id 3 = 'Indentured Servant' id 4 = 'Expert Ore Miner'
UNITS = [
    'Colonist',           # Базовый колонист
    'Expert Farmer',      # Эксперт-фермер
	'Indentured Servant',  # Кабальный слуга
	'Expert Ore Miner',   # Эксперт-шахтёр (руда)
    'Expert Tobacco Planter',  # Эксперт по выращиванию табака
    'Expert Cotton Planter',  # Эксперт по выращиванию хлопка
    'Expert Fur Trapper',  # Эксперт-охотник на пушнину
    'Expert Lumberjack',  # Эксперт-лесоруб
    'Expert Silver Miner',  # Эксперт-шахтёр (серебро)
    'Expert Fisherman',   # Эксперт-рыбак
    'Expert Distiller',   # Эксперт-винокур
    'Expert Weaver',      # Эксперт-ткач
    'Expert Tobacconist',  # Эксперт-табачник
    'Expert Fur Trader',  # Эксперт-торговец пушниной
    'Expert Carpenter',   # Эксперт-плотник
    'Expert Blacksmith',  # Эксперт-кузнец
    'Expert Gunsmith',    # Эксперт-оружейник
    'Expert Brewmaster',  # Эксперт-пивовар
    'Expert Potter',      # Эксперт-гончар
    'Expert Tanner',      # Эксперт-кожевник
    'Expert Furrier',     # Эксперт-меховщик
    'Expert Rancher',     # Эксперт-скотовод
    'Expert Hunter',      # Эксперт-охотник
    'Expert Scout',       # Эксперт-разведчик
    'Expert Pioneer',     # Эксперт-первопроходец
    'Expert Soldier',     # Эксперт-солдат
    'Expert Dragoon',     # Эксперт-драгун
    'Expert Artillery',   # Эксперт-артиллерист
    'Expert Missionary',  # Эксперт-миссионер
    'Free Colonist',      # Свободный колонист
    'Petty Criminal',     # Мелкий преступник
    'Converted Native',   # Обращённый туземец
    'Veteran Soldier',    # Ветеран-солдат
    'Seasoned Scout',     # Опытный разведчик
    'Hardy Pioneer',      # Выносливый первопроходец
    'Jesuit Missionary',  # Иезуитский миссионер
    'Firebrand Preacher',  # Пылкий проповедник
    'Pioneer',            # Первопроходец
	'Expert Sugar Planter',  # Эксперт по выращиванию сахара
    'Soldier',            # Солдат
    'Dragoon',            # Драгун
    'Artillery',          # Артиллерия
    'Missionary',         # Миссионер
    'Statesman',          # Государственный деятель
    'Scout',              # Разведчик
    'Treasure Transport',  # Транспорт с сокровищами
    'Galleon',            # Галеон
    'Privateer',          # Капер
    'Frigate',            # Фрегат
    'Man-O-War',          # Линейный корабль
    'Ship of the Line',   # Корабль линии
    'Merchantman',        # Торговое судно
    'Wagon Train',        # Обоз
    'Caravel',            # Каравелла
    'Treasure Fleet',     # Флот с сокровищами
    'Native Scout',       # Туземный разведчик
    'Native Warrior',     # Туземный воин
    'Native Archer',      # Туземный лучник
    'Native Brave',       # Туземный воин (храбрец)
    'Native Chief',       # Туземный вождь
    'Native Convert',     # Обращённый туземец
    'Native Missionary',  # Туземный миссионер
    'Native Settler',     # Туземный поселенец
    'Native Trader',      # Туземный торговец
    'Native Fisherman',   # Туземный рыбак
    'Native Hunter',      # Туземный охотник
    'Native Farmer',      # Туземный фермер
    'Native Miner',       # Туземный шахтёр
    'Native Lumberjack',  # Туземный лесоруб
    'Native Trapper',     # Туземный охотник на пушнину
    'Native Weaver',      # Туземный ткач
    'Native Distiller',   # Туземный винокур
    'Native Blacksmith',  # Туземный кузнец
    'Native Gunsmith',    # Туземный оружейник
    'Native Carpenter',   # Туземный плотник
    'Native Rancher',     # Туземный скотовод
    'Native Potter',      # Туземный гончар
    'Native Tanner',      # Туземный кожевник
    'Native Furrier',     # Туземный меховщик
    'Native Brewmaster',  # Туземный пивовар
    'Native Tobacconist',  # Туземный табачник
    'Native Sugar Planter',  # Туземный плантатор сахара
    'Native Cotton Planter',  # Туземный плантатор хлопка
    'Native Silver Miner',  # Туземный шахтёр (серебро)
    'Native Ore Miner',   # Туземный шахтёр (руда)
    'Native Fisherman',   # Туземный рыбак
    'Native Hunter',      # Туземный охотник
    'Native Scout',       # Туземный разведчик
    'Native Warrior',     # Туземный воин
    'Native Archer',      # Туземный лучник
    'Native Brave',       # Туземный воин (храбрец)
    'Native Chief',       # Туземный вождь
    'Native Convert',     # Обращённый туземец
    'Native Missionary',  # Туземный миссионер
    'Native Settler',     # Туземный поселенец
    'Native Trader',      # Туземный торговец
    'Native Fisherman',   # Туземный рыбак
    'Native Hunter',      # Туземный охотник
    'Native Farmer',      # Туземный фермер
    'Native Miner',       # Туземный шахтёр
    'Native Lumberjack',  # Туземный лесоруб
    'Native Trapper',     # Туземный охотник на пушнину
    'Native Weaver',      # Туземный ткач
    'Native Distiller',   # Туземный винокур
    'Native Blacksmith',  # Туземный кузнец
    'Native Gunsmith',    # Туземный оружейник
    'Native Carpenter',   # Туземный плотник
    'Native Rancher',     # Туземный скотовод
    'Native Potter',      # Туземный гончар
    'Native Tanner',      # Туземный кожевник
    'Native Furrier',     # Туземный меховщик
    'Native Brewmaster',  # Туземный пивовар
    'Native Tobacconist',  # Туземный табачник
    'Native Sugar Planter',  # Туземный плантатор сахара
    'Native Cotton Planter',  # Туземный плантатор хлопка
    'Native Silver Miner',  # Туземный шахтёр (серебро)
    'Native Ore Miner',   # Туземный шахтёр (руда)
]


def get_dict(filename):
    """
    Из файла получает словарь, ключ определяется по символам начала строки ", а значение по [].
    """
    PLAYER_BUILD = {}
    try:
        f = open(filename, 'r')
        content = f.read()
        if content:
            PLAYER_BUILD = eval(content)  # Преобразуем строку в словарь
        f.close()
    except Exception, e:
        print "Ошибка чтения файла %s: %s" % (filename, str(e))
    return PLAYER_BUILD

# globals
###################################################
class CvEventManager:
	def __init__(self):
		#################### ON EVENT MAP ######################
		self.bCtrl = False
		self.bShift = False
		self.bAlt = False
		self.bAllowCheats = False

		# OnEvent Enums
		self.EventLButtonDown=1
		self.EventLcButtonDblClick=2
		self.EventRButtonDown=3
		self.EventBack=4
		self.EventForward=5
		self.EventKeyDown=6
		self.EventKeyUp=7

		self.__LOG_MOVEMENT = 0
		self.__LOG_BUILDING = 0
		self.__LOG_COMBAT = 1
		self.__LOG_CONTACT = 0
		self.__LOG_IMPROVEMENT =0
		self.__LOG_CITYBUILT = 0	# TAC - koma13
		self.__LOG_CITYLOST = 0
		self.__LOG_CITYBUILDING = 0
		self.__LOG_UNITBUILD = 0
		self.__LOG_UNITKILLED = 1
		self.__LOG_UNITLOST = 0
		self.__LOG_UNITPROMOTED = 0
		self.__LOG_UNITSELECTED = 0
		self.__LOG_UNITPILLAGE = 0
		self.__LOG_GOODYRECEIVED = 0
		self.__LOG_WARPEACE = 0
		self.__LOG_PUSH_MISSION = 0

		## EVENTLIST
		self.EventHandlerMap = {
			'mouseEvent'			: self.onMouseEvent,
			'kbdEvent' 				: self.onKbdEvent,
			'ModNetMessage'			: self.onModNetMessage,
			'Init'					: self.onInit,
			'Update'				: self.onUpdate,
			'UnInit'				: self.onUnInit,
			'OnSave'				: self.onSaveGame,
			'OnPreSave'				: self.onPreSave,
			'OnLoad'				: self.onLoadGame,
			'GameStart'				: self.onGameStart,
			'GameEnd'				: self.onGameEnd,
			'plotRevealed' 			: self.onPlotRevealed,
			'plotFeatureRemoved' 	: self.onPlotFeatureRemoved,
			'plotPicked'			: self.onPlotPicked,
			'gotoPlotSet'			: self.onGotoPlotSet,
			'BeginGameTurn'			: self.onBeginGameTurn,
			'EndGameTurn'			: self.onEndGameTurn,
			'BeginPlayerTurn'		: self.onBeginPlayerTurn,
			'EndPlayerTurn'			: self.onEndPlayerTurn,
			'endTurnReady'			: self.onEndTurnReady,
			'combatResult' 			: self.onCombatResult,
			'combatLogCalc'	 		: self.onCombatLogCalc,
			'combatLogHit'			: self.onCombatLogHit,
			'improvementBuilt' 		: self.onImprovementBuilt,
			'improvementDestroyed' 	: self.onImprovementDestroyed,
			'routeBuilt' 			: self.onRouteBuilt,
			'firstContact' 			: self.onFirstContact,
			'cityBuilt' 			: self.onCityBuilt,
			'cityRazed'				: self.onCityRazed,
			'cityAcquired' 			: self.onCityAcquired,
			'cityAcquiredAndKept' 	: self.onCityAcquiredAndKept,
			'cityLost'				: self.onCityLost,
			'cultureExpansion' 		: self.onCultureExpansion,
			'cityGrowth' 			: self.onCityGrowth,
			'cityDoTurn' 			: self.onCityDoTurn,
			'cityBuildingUnit'		: self.onCityBuildingUnit,
			'cityBuildingBuilding'	: self.onCityBuildingBuilding,
			'cityRename'			: self.onCityRename,
			'createTradeRoute'		: self.onCreateTradeRoute,
			'editTradeRoute'		: self.onEditTradeRoute,
			'cityHurry'				: self.onCityHurry,
			'selectionGroupPushMission'		: self.onSelectionGroupPushMission,
			'unitMove' 				: self.onUnitMove,
			'unitSetXY' 			: self.onUnitSetXY,
			'unitCreated' 			: self.onUnitCreated,
			'unitBuilt' 			: self.onUnitBuilt,
			'unitKilled'			: self.onUnitKilled,
			'unitLost'				: self.onUnitLost,
			'unitPromoted'			: self.onUnitPromoted,
			'unitSelected'			: self.onUnitSelected,
			'missionaryConvertedUnit' : self.onMissionaryConvertedUnit,
			'UnitRename'			: self.onUnitRename,
			'unitPillage'			: self.onUnitPillage,
			'unitGifted'			: self.onUnitGifted,
			'unitBuildImprovement'	: self.onUnitBuildImprovement,
			'goodyReceived'        	: self.onGoodyReceived,
			'buildingBuilt' 		: self.onBuildingBuilt,
			'chat' 					: self.onChat,
			'victory'				: self.onVictory,
			'yieldSoldToEurope'		: self.onYieldSoldToEurope,
			'yieldBoughtFromEurope'	: self.onYieldBoughtFromEurope,
			'unitBoughtFromEurope'	: self.onUnitBoughtFromEurope,
			'unitTravelStateChanged'	: self.onUnitTravelStateChanged,
			'emmigrantAtDocks'		: self.onEmmigrantAtDocks,
			'populationJoined'		: self.onPopulationJoined,
			'populationUnjoined'	: self.onPopulationUnjoined,
			'unitLearned'			: self.onUnitLearned,
			'yieldProduced'			: self.onYieldProduced,
			'changeWar'				: self.onChangeWar,
			'setPlayerAlive'		: self.onSetPlayerAlive,
			'playerGoldTrade'		: self.onPlayerGoldTrade,
			'windowActivation'		: self.onWindowActivation,
			'cityScreenOpen'		: self.onCityScreenOpen,
			'gameUpdate'			: self.onGameUpdate,		# sample generic event
			'DiplomacyEvent'        : self.onDiplomacyEvent,
			'logHiredUnit'			: self.logHiredUnit,
			'getAllAttitudes'		: self.getAllAttitudes,

		}

		################## Events List ###############################
		#
		# Dictionary of Events, indexed by EventID (also used at popup context id)
		#   entries have name, beginFunction, applyFunction [, randomization weight...]
		#
		# Normal events first, random events after
		#
		################## Events List ###############################
		self.Events={
			CvUtil.EventEditCityName : ('EditCityName', self.__eventEditCityNameApply, self.__eventEditCityNameBegin),
			CvUtil.EventEditCity : ('EditCity', self.__eventEditCityApply, self.__eventEditCityBegin),
			CvUtil.EventPlaceObject : ('PlaceObject', self.__eventPlaceObjectApply, self.__eventPlaceObjectBegin),
			CvUtil.EventAwardGold: ('AwardGold', self.__EventAwardGoldApply, self.__EventAwardGoldBegin),
			CvUtil.EventEditUnitName : ('EditUnitName', self.__eventEditUnitNameApply, self.__eventEditUnitNameBegin),
			CvUtil.EventWBAllPlotsPopup : ('WBAllPlotsPopup', self.__eventWBAllPlotsPopupApply, self.__eventWBAllPlotsPopupBegin),
			CvUtil.EventWBLandmarkPopup : ('WBLandmarkPopup', self.__eventWBLandmarkPopupApply, self.__eventWBLandmarkPopupBegin),
			CvUtil.EventWBScriptPopup : ('WBScriptPopup', self.__eventWBScriptPopupApply, self.__eventWBScriptPopupBegin),
			CvUtil.EventWBStartYearPopup : ('WBStartYearPopup', self.__eventWBStartYearPopupApply, self.__eventWBStartYearPopupBegin),
			CvUtil.EventShowWonder: ('ShowWonder', self.__eventShowWonderApply, self.__eventShowWonderBegin),
			CvUtil.EventCreateTradeRoute: ('CreateTradeRoute', self.__eventCreateTradeRouteApply, self.__eventCreateTradeRouteBegin),
			CvUtil.EventEditTradeRoute: ('EditTradeRoute', self.__eventEditTradeRouteApply, self.__eventEditTradeRouteBegin),

# Dale - AoD: AoDCheatMenu START
			CvUtil.EventAoDCheatMenu: ('AoDCheatMenu', self.AoDCheatMenuApply, self.AoDCheatMenuBegin),
# Dale - AoD: AoDCheatMenu END

# EuropeScreen START
			CvUtil.EventDoEuropeScreen: ('DoEuropeScreen', self.doEuropeScreenApply, self.doEuropeScreenBegin),
# EuropeScreen END

		}
#################### EVENT STARTERS ######################
	def handleEvent(self, argsList):
		'EventMgr entry point'
		# extract the last 6 args in the list, the first arg has already been consumed
		self.origArgsList = argsList	# point to original
		tag = argsList[0]				# event type string
		idx = len(argsList)-6
		bDummy = false
		self.bDbg, bDummy, self.bAlt, self.bCtrl, self.bShift, self.bAllowCheats = argsList[idx:]
		ret = 0
		if self.EventHandlerMap.has_key(tag):
			fxn = self.EventHandlerMap[tag]
			ret = fxn(argsList[1:idx])
		return ret

#################### EVENT APPLY ######################
	def beginEvent( self, context, argsList=-1 ):
		'Begin Event'
		entry = self.Events[context]
		return entry[2]( argsList )

	def applyEvent( self, argsList ):
		'Apply the effects of an event '
		context, playerID, netUserData, popupReturn = argsList

		if context == CvUtil.PopupTypeEffectViewer:
			return CvDebugTools.g_CvDebugTools.applyEffectViewer( playerID, netUserData, popupReturn )

		entry = self.Events[context]

		if ( context not in CvUtil.SilentEvents ):
			self.reportEvent(entry, context, (playerID, netUserData, popupReturn) )
		return entry[1]( playerID, netUserData, popupReturn )   # the apply function

	def reportEvent(self, entry, context, argsList):
		'Report an Event to Events.log '
		if (gc.getGame().getActivePlayer() != -1):
			message = "DEBUG Event: %s (%s)" %(entry[0], gc.getActivePlayer().getName())
			CyInterface().addImmediateMessage(message,"")
			CvUtil.pyPrint(message)
		return 0

#################### ON EVENTS ######################
	def onKbdEvent(self, argsList):
		'keypress handler - return 1 if the event was consumed'

		eventType,key,mx,my,px,py = argsList
		game = gc.getGame()

		if (self.bAllowCheats):
			# notify debug tools of input to allow it to override the control
			argsList = (eventType,key,self.bCtrl,self.bShift,self.bAlt,mx,my,px,py,gc.getGame().isNetworkMultiPlayer())
			if ( CvDebugTools.g_CvDebugTools.notifyInput(argsList) ):
				return 0

		if ( eventType == self.EventKeyDown ):
			theKey=int(key)

			#Custom Camera Controls

			if (theKey == int(InputTypes.KB_LEFT)):
				if self.bCtrl:
						CyCamera().SetBaseTurn(CyCamera().GetBaseTurn() - 45.0)
						return 1
				elif self.bShift:
						CyCamera().SetBaseTurn(CyCamera().GetBaseTurn() - 15.0)
						return 1
			
			elif (theKey == int(InputTypes.KB_RIGHT)):
					if self.bCtrl:
							CyCamera().SetBaseTurn(CyCamera().GetBaseTurn() + 45.0)
							return 1
					elif self.bShift:
							CyCamera().SetBaseTurn(CyCamera().GetBaseTurn() + 15.0)
							return 1

			elif (theKey == int(InputTypes.KB_UP)):
					if (self.bCtrl or self.bShift) and CyCamera().GetBasePitch() > -45:
						#CyCamera().SetBasePitch(CyCamera().GetBasePitch() - 5.0)
						return 1

			elif (theKey == int(InputTypes.KB_DOWN)):
					if (self.bCtrl or self.bShift) and CyCamera().GetBasePitch() < 20:
						#CyCamera().SetBasePitch(CyCamera().GetBasePitch() + 5.0)
						return 1

			elif (theKey == int(InputTypes.KB_HOME) and self.bCtrl):
						CyCamera().SetBaseTurn(0)
						CyCamera().SetBasePitch(0)
						return 1

			#End Custom Camera Controls

			CvCameraControls.g_CameraControls.handleInput( theKey )

# Dale - AoD: AoDCheatMenu START
			if (self.bAllowCheats):		# TAC - Multiplayer - koma13
				if( theKey == int(InputTypes.KB_Z) and self.bShift and self.bCtrl ) :
					self.beginEvent(CvUtil.EventAoDCheatMenu)
# Dale - AoD: AoDCheatMenu END

# Achievements START
			if( theKey == int(InputTypes.KB_F10) and not self.bShift and not self.bCtrl ) :
				CvScreensInterface.showAchieveAdvisorScreen()
# Achievements END

# TAC: EventTriggerMenu START
# Shift+Ctrl+E im Cheatmodus
			if( theKey == int(InputTypes.KB_E) and self.bShift and self.bCtrl and self.bAllowCheats) :
				ePlayer = gc.getGame().getActivePlayer()
				popupInfo = CyPopupInfo()
				popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
				popupInfo.setText(CyTranslator().getText("TXT_KEY_POPUP_SELECT_EVENT",()))
				popupInfo.setData1(ePlayer)
				popupInfo.setOnClickedPythonCallback("selectOneEvent")
				popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_POPUP_SELECT_NEVER_MIND", ()), "")
				for i in range(gc.getNumEventTriggerInfos()):
					trigger = gc.getEventTriggerInfo(i)
					name = trigger.getType().replace("EVENTTRIGGER_", "").replace("_", " ").title()
					popupInfo.addPythonButton(name, "")
					# popupInfo.addPythonButton(str(trigger.getType()), "")
				popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_POPUP_SELECT_NEVER_MIND", ()), "")
				
				popupInfo.addPopup(ePlayer)
# TAC: EventTriggerMenu END

			if (self.bAllowCheats):
				# Shift - T (Debug - No MP)
				if (theKey == int(InputTypes.KB_T)):
					if ( self.bShift ):
						self.beginEvent(CvUtil.EventAwardGold)
						#self.beginEvent(CvUtil.EventCameraControlPopup)
						return 1

# TAC: Wonder Movie Cheat disabled
				#elif (theKey == int(InputTypes.KB_W)):
				#	if ( self.bShift and self.bCtrl):
				#		self.beginEvent(CvUtil.EventShowWonder)
				#		return 1

				# Shift - ] (Debug - currently mouse-overd unit, health += 10
				elif (theKey == int(InputTypes.KB_LBRACKET) and self.bShift ):
					unit = CyMap().plot(px, py).getUnit(0)
					if ( not unit.isNone() ):
						d = min( unit.maxHitPoints()-1, unit.getDamage() + 10 )
						unit.setDamage( d )

				# Shift - [ (Debug - currently mouse-overd unit, health -= 10
				elif (theKey == int(InputTypes.KB_RBRACKET) and self.bShift ):
					unit = CyMap().plot(px, py).getUnit(0)
					if ( not unit.isNone() ):
						d = max( 0, unit.getDamage() - 10 )
						unit.setDamage( d )

				elif (theKey == int(InputTypes.KB_F1)):
					if ( self.bShift ):
						CvScreensInterface.replayScreen.showScreen(False)
						return 1
					# don't return 1 unless you want the input consumed


		return 0

	def onModNetMessage(self, argsList):
		'Called whenever CyMessageControl().sendModNetMessage() is called - this is all for you modders!'

		iData1, iData2, iData3, iData4, iData5 = argsList

		print("Modder's net message!")

		CvUtil.pyPrint( 'onModNetMessage' )

	def onInit(self, argsList):
		'Called when Civ starts up'
		CvUtil.pyPrint( 'OnInit' )

	def onUpdate(self, argsList):
		'Called every frame'
		fDeltaTime = argsList[0]

		# allow camera to be updated
		CvCameraControls.g_CameraControls.onUpdate( fDeltaTime )

	def onWindowActivation(self, argsList):
		'Called when the game window activates or deactivates'
		bActive = argsList[0]

	def onCityScreenOpen(self, argsList):
		'Called when the game window activates or deactivates'
		iPlayer = argsList[0]
		iCityId = argsList[1]
		CvAdvisorUtils.cityScreenFeats(iPlayer, iCityId)

	def onUnInit(self, argsList):
		'Called when Civ shuts down'
		CvUtil.pyPrint('OnUnInit')

	def onPreSave(self, argsList):
		"called before a game is actually saved"
		CvUtil.pyPrint('OnPreSave')

	def onSaveGame(self, argsList):
		"return the string to be saved - Must be a string"
		return ""

	def onLoadGame(self, argsList):
		return 0

	def onGameStart(self, argsList):
		'Called at the start of the game'
		if (gc.getGame().getGameTurnYear() == gc.getDefineINT("START_YEAR") and not gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ADVANCED_START)):
			for iPlayer in range(gc.getMAX_PLAYERS()):
				player = gc.getPlayer(iPlayer)
				if (player.isAlive() and player.isHuman()):
					popupInfo = CyPopupInfo()
					popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON_SCREEN)
					popupInfo.setText(u"showDawnOfMan")
					popupInfo.addPopup(iPlayer)
		else:
			CyInterface().setSoundSelectionReady(true)

		if gc.getGame().isPbem():
			for iPlayer in range(gc.getMAX_PLAYERS()):
				player = gc.getPlayer(iPlayer)
				if (player.isAlive() and player.isHuman()):
					popupInfo = CyPopupInfo()
					popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_DETAILS)
					popupInfo.setOption1(true)
					popupInfo.addPopup(iPlayer)

		f = open(str(gc.getGame().getName()) + '.txt', 'w')  # создаем файл в режиме перезаписывания
		f.write('Game start\n ----------------StartTurn 0----------------\n')

		CyMap().calculateCanalAndChokePoints() # Super Forts

	def onGameEnd(self, argsList):
		'Called at the End of the game'
		print("Game is ending")
		f = open(str(gc.getGame().getName()) + '.txt', 'a')
		f.write('\n --------------------------------End--------------------------------\n')
		return

	def onBeginGameTurn(self, argsList):
		'Called at the beginning of the end of each turn'
		iGameTurn = argsList[0]

	def onEndGameTurn(self, argsList):
		'Called at the end of the end of each turn'
		iGameTurn = argsList[0]
		f = open(str(gc.getGame().getName()) + '.txt', 'a')
		f.write(' ----------------StartTurn %s----------------\n\n' % (str(iGameTurn + 1)))

	def onBeginPlayerTurn(self, argsList):
		'Called at the beginning of a players turn'
		iGameTurn, iPlayer = argsList
		

	def onEndPlayerTurn(self, argsList):
		'Called at the end of a players turn'
		iGameTurn, iPlayer = argsList
		game = gc.getGame()
		year = game.getGameTurnYear()  # Год в игре
		gold = gc.getPlayer(iPlayer).getGold()  # Количество золота игрока
		# Получаем список всех отношений
		allAttitudes = self.getAllAttitudes(iPlayer)

		# Логирование налогов и доходов
		try:
			f = open(str(gc.getGame().getName()) + '_economy_log.txt', 'a')  # Открываем файл в режиме добавления
			f.write("Turn %d: Player %s ended turn with %d gold.\n" % (gc.getGame().getGameTurn(), encode(player.getName()), gold))
			
			# Логирование налоговых поступлений
			taxRate = player.getTaxRate()
			totalTaxIncome = player.calculateTaxRateIncome(taxRate)
			f.write("Tax Rate: %d%%, Tax Income: %d\n" % (taxRate, totalTaxIncome))
			
			# Логирование других источников дохода (например, торговля, производство)
			totalTradeIncome = player.calculateTotalCommerce(CommerceTypes.COMMERCE_GOLD)
			f.write("Trade Income: %d\n" % (totalTradeIncome))
			
			# Логирование расходов (например, содержание армии)
			unitMaintenance = player.calculateUnitCost()
			buildingMaintenance = player.calculateBuildingCost()
			f.write("Unit Maintenance: %d, Building Maintenance: %d\n" % (unitMaintenance, buildingMaintenance))
			
			# Логирование общего баланса
			totalIncome = totalTaxIncome + totalTradeIncome
			totalExpenses = unitMaintenance + buildingMaintenance
			balance = totalIncome - totalExpenses
			f.write("Total Income: %d, Total Expenses: %d, Balance: %d\n" % (totalIncome, totalExpenses, balance))
			
			f.close()
		except Exception, e:
			CvUtil.pyPrint("Ошибка записи в лог-файл: %s" % str(e))

		# юниты игрока
		unit_count = 0

		# Получаем объект игрока
		player = gc.getPlayer(iPlayer)

		# Считаем юниты на карте
		unit_count += player.getNumUnits()

		# Считаем население в городах (как альтернативу юнитам в городах)
		(pCity, iter) = player.firstCity(False)
		while (pCity):
			# Добавляем население города к общему количеству "юнитов"
			unit_count += pCity.getPopulation()
			(pCity, iter) = player.nextCity(iter, False)

		# Получаем столицу игрока (если нужно)
		capital_city = player.getCapitalCity()
		if capital_city:
			# Можно добавить дополнительную логику для столицы, если нужно
			pass

		# Преобразуем количество юнитов в строку
		unit_names_str = str(unit_count)

		# Молоточки (Продуктивность городов)
		hammers = 0

		if gc.getPlayer(iPlayer).isHuman():  # Если игрок не является ии / ход завершил человек
			f = open(str(gc.getGame().getName()) + '.txt', 'a')
			f.write('-- Year:' + str(year) + '\n-- Golg:' + str(gold) + '\n-- Units:' + unit_names_str + '\n\n')

			# Добавляем данные о торговле с Европой из _trade_log.txt
			try:
				trade_log_file = open(str(gc.getGame().getName()) + '_trade_log.txt', 'r')
				trade_log_lines = trade_log_file.readlines()
				trade_log_file.close()

				if trade_log_lines:
					f.write('\n------Trade with Europe------\n')
					for line in trade_log_lines:
						f.write(line)
					f.write('\n')

				# Очищаем файл _trade_log.txt после добавления данных
				trade_log_file = open(str(gc.getGame().getName()) + '_trade_log.txt', 'w')
				trade_log_file.close()
			except Exception, e:
				CvUtil.pyPrint("Ошибка чтения/очистки файла _trade_log.txt: %s" % str(e))

			# # Добавляем данные о найме юнитов из _hired_units_log.txt
			# try:
			# 	hired_units_log_file = open(str(gc.getGame().getName()) + '_hired_units_log.txt', 'r')
			# 	hired_units_log_lines = hired_units_log_file.readlines()
			# 	hired_units_log_file.close()

			# 	if hired_units_log_lines:
			# 		f.write('\n------Hired Units------\n')
			# 		for line in hired_units_log_lines:
			# 			f.write(line)
			# 		f.write('\n')

			# 	# Очищаем файл _hired_units_log.txt после добавления данных
			# 	hired_units_log_file = open(str(gc.getGame().getName()) + '_hired_units_log.txt', 'w')
			# 	hired_units_log_file.close()
			# except Exception, e:
			# 	CvUtil.pyPrint("Ошибка чтения/очистки файла _hired_units_log.txt: %s" % str(e))

			# Добавляем данные о дипломатических событиях из _diplomacy_log.txt
			try:
				diplomacy_log_file = open(str(gc.getGame().getName()) + '_diplomacy_log.txt', 'r')
				diplomacy_log_lines = diplomacy_log_file.readlines()
				diplomacy_log_file.close()

				if diplomacy_log_lines:
					f.write('\n------Diplomatic Events------\n')
					for line in diplomacy_log_lines:
						f.write(line)
					f.write('\n')

				# Очищаем файл _diplomacy_log.txt после добавления данных
				diplomacy_log_file = open(str(gc.getGame().getName()) + '_diplomacy_log.txt', 'w')
				diplomacy_log_file.close()
			except Exception, e:
				CvUtil.pyPrint("Ошибка чтения/очистки файла _diplomacy_log.txt: %s" % str(e))

			# Добавляем данные о юнитах из _unit_death_log.txt
			try:
				unit_death_log_file = open(str(gc.getGame().getName()) + '_unit_death_log.txt', 'r')
				unit_death_log_lines = unit_death_log_file.readlines()
				unit_death_log_file.close()

				if unit_death_log_lines:
					f.write('\n------Incidents with units------\n')
					for line in unit_death_log_lines:
						f.write(line)
					f.write('\n')

				# Очищаем файл _unit_death_log.txt после добавления данных
				unit_death_log_file = open(str(gc.getGame().getName()) + '_unit_death_log.txt', 'w')
				unit_death_log_file.close()
			except Exception, e:
				CvUtil.pyPrint("Ошибка чтения/очистки файла _unit_death_log.txt: %s" % str(e))

			if gc.getPlayer(iPlayer).getNumCities() > 0:  # если у игрока есть города
				PLAYER_CITY = get_dict(str(gc.getGame().getName()) + str(encode(gc.getPlayer(iPlayer).getName())) + '_CITY.txt')
				# получаем словарь из файла, название которого соотвествует этой переменной

				for city_id in PLAYER_CITY[str(encode(gc.getPlayer(iPlayer).getName()))]:  # в словаре сохраняются 'игрок' : [1231,231] цифры это id города
					city = gc.getPlayer(iPlayer).getCity(city_id)  # получаем класс города

					f.write('\n------Cities------\n\n' + '----' + decode(encode(city.getName())) + '\n')
					PLAYER_CITY_BUILD = get_dict(str(gc.getGame().getName()) + str(encode(gc.getPlayer(iPlayer).getName())) + '_CITY_BUILD.txt')
					# словарь построек в городах, словарь вида {'название_города' : ['название постройки']}

					if city_id in PLAYER_CITY_BUILD.keys():  # Если ID города есть в словаре
						last = open(str(gc.getGame().getName()) + str(encode(gc.getPlayer(iPlayer).getName())) + '_LAST_PROD.txt', 'a')
						# файл отвечающий за продуктивность городов, молоточки
						last.close()
						last_production = get_dict(str(gc.getGame().getName()) + str(encode(gc.getPlayer(iPlayer).getName())) + '_LAST_PROD.txt')

						if str(city_id) in last_production.keys():
							final_production = int(city.getProduction()) - int(last_production[str(city_id)][0])
							# в игре продуктивность получается во время строительства зданий и накапливается в процессе, поэтому ее изменение является продуктивностью (+3 или что то другое)
							last_production[str(city_id)] = [int(city.getProduction())]
						# обязательно сохраняется в списке (type = list) иначе функция get_dict сломается
						else:
							final_production = int(city.getProduction())
							last_production[str(city_id)] = [int(city.getProduction())]
						last = open(str(gc.getGame().getName()) + str(encode(gc.getPlayer(iPlayer).getName())) + '_LAST_PROD.txt', 'w')
						last.write(str(last_production))

						hammers += final_production  # продуктивность со всех городов

						f.write('Production: ' + str(final_production) + '\n')

						index = 0
						while index < 52:  # цикл для проверки производимых в городе ресурсов
							# ресуры имееют id от 0 до 52
							res = city.getYieldRate(index)  # получаем значение ресурса
							if res != 0:
								f.write(RES[index] + ': ' + str(res) + '\n')
							index += 1
						f.write('-- Buildings:\n')
						for build in PLAYER_CITY_BUILD[city_id]:
							f.write('-' + encode(gc.getBuildingInfo(build).getDescription()) + '\n')

			f.write('\n\n\n---- Relations with civilizations ---- \n')
			# Записываем все отношения в лог
			for attitude in allAttitudes:  # Исправлено: allAttitudes вместо allАttitudes
				f.write('- ' + attitude + '\n')				

			f.write('\n--- Total Production:' + str(hammers) + '\n')
			f.write('---- Elapsed Time %s seconds\n' % (str(gc.getPlayer(iPlayer).getTotalTimePlayed())))
			f.write('\n--------- End of Turn %s for Player %s ---------\n\n\n' % (str(iGameTurn), str(encode(gc.getPlayer(iPlayer).getName()))))

		CvAdvisorUtils.endTurnNags(iPlayer)
		CvAdvisorUtils.endTurnFeats(iPlayer)

	def onEndTurnReady(self, argsList):
		iGameTurn = argsList[0]

	def onFirstContact(self, argsList):
		'Contact'
		iTeamX,iHasMetTeamY = argsList
		if (not self.__LOG_CONTACT):
			return
		CvUtil.pyPrint('Team %d has met Team %d' %(iTeamX, iHasMetTeamY))

	def getAllAttitudes(self, player_id):
		attitudes = []
		for team_id in range(gc.getMAX_CIV_TEAMS()):  # Перебираем все команды
			team = gc.getTeam(team_id)
			if team and team.isAlive() and team_id != player_id:  # Проверяем, что команда существует и активна, и исключаем текущего игрока
				leader_id = team.getLeaderID()
				if leader_id != -1:  # Проверяем, что лидер существует
					player = gc.getPlayer(leader_id)
					if player and player.isAlive():  # Проверяем, что игрок существует и активен
						try:
							team_name = encode(player.getCivilizationDescription(0))
							attitude_string = encode(CyGameTextMgr().getAttitudeString(team_id, player_id))
							attitudes.append(team_name + " " + attitude_string)
						except Exception, e:
							# Логируем ошибку, если что-то пошло не так
							CvUtil.pyPrint("Ошибка при получении данных о команде")
		return attitudes

	def onCombatResult(self, argsList):
		'Combat Result'
		pWinner, pLoser = argsList
		playerX = gc.getPlayer(pWinner.getOwner())
		unitX = gc.getUnitInfo(pWinner.getUnitType())
		playerY = gc.getPlayer(pLoser.getOwner())
		unitY = gc.getUnitInfo(pLoser.getUnitType())

		# Проверяем, является ли проигравший игрок человеком
		if playerY.isHuman():
			# Формируем сообщение для лога
			log_message = "Unit %s player %s %d killed a unit %s player %s %d.\n" % (
				encode(unitX.getDescription()),
				encode(playerX.getCivilizationDescription(0)),
				playerX.getID(),
				encode(unitY.getDescription()),
				encode(playerY.getCivilizationDescription(0)),
				playerY.getID()
			)
			
			# Записываем сообщение в лог-файл
			try:
				f = open(str(gc.getGame().getName()) + '_unit_death_log.txt', 'a')  # Открываем файл в режиме добавления
				f.write(log_message)
				f.close()
			except Exception, e:
				CvUtil.pyPrint("Ошибка записи в лог-файл: %s" % str(e))

		# Логирование для отладки (независимо от того, человек это или AI)
		if playerX and playerX and unitX and playerY:
			CvUtil.pyPrint('Player %d Civilization %s Unit %s has defeated Player %d Civilization %s Unit %s'
				%(playerX.getID(), playerX.getCivilizationDescription(0), unitX.getDescription(),
				playerY.getID(), playerY.getCivilizationDescription(0), unitY.getDescription()))

		if (not self.__LOG_UNITKILLED):
			return
		CvUtil.pyPrint('Player %d Civilization %s Unit %s was killed by Player %d'
			%(playerY.getID(), playerY.getCivilizationDescription(0), gc.getUnitInfo(pLoser.getUnitType()).getDescription(), playerX.getID()))


	def onCombatLogCalc(self, argsList):
		'Combat Result'
		genericArgs = argsList[0][0]
		cdAttacker = genericArgs[0]
		cdDefender = genericArgs[1]
		iCombatOdds = genericArgs[2]
		CvUtil.combatMessageBuilder(cdAttacker, cdDefender, iCombatOdds)

	def onCombatLogHit(self, argsList):
		'Combat Message'
		global gCombatMessages, gCombatLog
		genericArgs = argsList[0][0]
		cdAttacker = genericArgs[0]
		cdDefender = genericArgs[1]
		iIsAttacker = genericArgs[2]
		iDamage = genericArgs[3]

		if cdDefender.eOwner == cdDefender.eVisualOwner:
			szDefenderName = gc.getPlayer(cdDefender.eOwner).getNameKey()
		else:
			szDefenderName = localText.getText("TXT_KEY_TRAIT_PLAYER_UNKNOWN", ())
		if cdAttacker.eOwner == cdAttacker.eVisualOwner:
			szAttackerName = gc.getPlayer(cdAttacker.eOwner).getNameKey()
		else:
			szAttackerName = localText.getText("TXT_KEY_TRAIT_PLAYER_UNKNOWN", ())

		if (iIsAttacker == 0):
			combatMessage = localText.getText("TXT_KEY_COMBAT_MESSAGE_HIT", (szDefenderName, cdDefender.sUnitName, iDamage, cdDefender.iCurrHitPoints, cdDefender.iMaxHitPoints))
			CyInterface().addCombatMessage(cdAttacker.eOwner,combatMessage)
			CyInterface().addCombatMessage(cdDefender.eOwner,combatMessage)
			if (cdDefender.iCurrHitPoints <= 0):
				combatMessage = localText.getText("TXT_KEY_COMBAT_MESSAGE_DEFEATED", (szAttackerName, cdAttacker.sUnitName, szDefenderName, cdDefender.sUnitName))
				CyInterface().addCombatMessage(cdAttacker.eOwner,combatMessage)
				CyInterface().addCombatMessage(cdDefender.eOwner,combatMessage)
		elif (iIsAttacker == 1):
			combatMessage = localText.getText("TXT_KEY_COMBAT_MESSAGE_HIT", (szAttackerName, cdAttacker.sUnitName, iDamage, cdAttacker.iCurrHitPoints, cdAttacker.iMaxHitPoints))
			CyInterface().addCombatMessage(cdAttacker.eOwner,combatMessage)
			CyInterface().addCombatMessage(cdDefender.eOwner,combatMessage)
			if (cdAttacker.iCurrHitPoints <= 0):
				combatMessage = localText.getText("TXT_KEY_COMBAT_MESSAGE_DEFEATED", (szDefenderName, cdDefender.sUnitName, szAttackerName, cdAttacker.sUnitName))
				CyInterface().addCombatMessage(cdAttacker.eOwner,combatMessage)
				CyInterface().addCombatMessage(cdDefender.eOwner,combatMessage)

	def onImprovementBuilt(self, argsList):
		'Improvement Built'
		iImprovement, iX, iY = argsList
		if (not self.__LOG_IMPROVEMENT):
			return
		CvUtil.pyPrint('Improvement %s was built at %d, %d'
			%(gc.getImprovementInfo(iImprovement).getDescription(), iX, iY))


	def onImprovementDestroyed(self, argsList):
		'Improvement Destroyed'
		iImprovement, iOwner, iX, iY = argsList
		if (not self.__LOG_IMPROVEMENT):
			return
		CvUtil.pyPrint('Improvement %s was Destroyed at %d, %d'
			%(gc.getImprovementInfo(iImprovement).getDescription(), iX, iY))


	def onRouteBuilt(self, argsList):
		'Route Built'
		iRoute, iX, iY = argsList
		if (not self.__LOG_IMPROVEMENT):
			return
		CvUtil.pyPrint('Route %s was built at %d, %d'
			%(gc.getRouteInfo(iRoute).getDescription(), iX, iY))

	def onPlotRevealed(self, argsList):
		'Plot Revealed'
		pPlot = argsList[0]
		iTeam = argsList[1]

	def onPlotFeatureRemoved(self, argsList):
		'Plot Revealed'
		pPlot = argsList[0]
		iFeatureType = argsList[1]
		pCity = argsList[2] # This can be null

	def onPlotPicked(self, argsList):
		'Plot Picked'
		pPlot = argsList[0]
		CvUtil.pyPrint('Plot was picked at %d, %d'
			%(pPlot.getX(), pPlot.getY()))

	def onGotoPlotSet(self, argsList):
		'Goto Plot'
		pPlot, iPlayer = argsList

	def onBuildingBuilt(self, argsList):
		'Building Completed'
		pCity, iBuildingType = argsList

		# Логирование завершения строительства
		CvAdvisorUtils.buildingBuiltFeats(pCity, iBuildingType)

		if gc.getPlayer(pCity.getOwner()).isHuman():  # Если игрок человек
			city_build_file_name = str(gc.getGame().getName()) + str(encode(gc.getPlayer(pCity.getOwner()).getName())) + '_CITY_BUILD.txt'
			print("Файл для построек города: %s" % city_build_file_name)  # Отладочное сообщение

			# Получаем словарь из файла
			PLAYER_CITY_BUILD = get_dict(city_build_file_name)
			list_city = []

			# Получаем список идентификаторов городов
			city_in_file = get_dict(str(gc.getGame().getName()) + str(encode(gc.getPlayer(pCity.getOwner()).getName())) + '_CITY.txt')
			for city_id in city_in_file.values():
				for i in city_id:
					list_city.append(i)  # Используем идентификатор города вместо имени

			if pCity.getID() in list_city:  # если город есть в списке
				keys = pCity.getID()  # Используем идентификатор города в качестве ключа

				if keys in PLAYER_CITY_BUILD.keys():  # если у города уже есть постройки
					list_build = []
					for build_id in PLAYER_CITY_BUILD[keys]:
						list_build.append(build_id)

					list_build.append(iBuildingType)  # Добавляем завершенную постройку
					PLAYER_CITY_BUILD[keys] = list_build
				else:
					PLAYER_CITY_BUILD[keys] = [iBuildingType]  # Создаем новую запись для города

				# Записываем обновленный словарь в файл
				try:
					f = open(city_build_file_name, 'w')
					f.write(str(PLAYER_CITY_BUILD))
					print("Данные о постройках города обновлены: %s" % str(PLAYER_CITY_BUILD))  # Отладочное сообщение
				finally:
					f.close()

		if (not self.__LOG_BUILDING):
			return
		CvUtil.pyPrint('%s was finished by Player %d Civilization %s'
			%(gc.getBuildingInfo(iBuildingType).getDescription(), pCity.getOwner(), gc.getPlayer(pCity.getOwner()).getCivilizationDescription(0)))


	def onSelectionGroupPushMission(self, argsList):
		'selection group mission'
		eOwner = argsList[0]
		eMission = argsList[1]
		iNumUnits = argsList[2]
		listUnitIds = argsList[3]

		if (not self.__LOG_PUSH_MISSION):
			return
		if pHeadUnit:
			CvUtil.pyPrint("Selection Group pushed mission %d" %(eMission))

	def onUnitMove(self, argsList):
		'unit move'
		pPlot,pUnit,pOldPlot = argsList
		player = gc.getPlayer(pUnit.getOwner())
		unitInfo = gc.getUnitInfo(pUnit.getUnitType())
		CvAdvisorUtils.unitMoveFeats(pUnit, pPlot, pOldPlot)
		if (not self.__LOG_MOVEMENT):
			return
		if player and unitInfo:
			CvUtil.pyPrint('Player %d Civilization %s unit %s is moving to %d, %d'
				%(player.getID(), player.getCivilizationDescription(0), unitInfo.getDescription(),
				pUnit.getX(), pUnit.getY()))

	def onUnitSetXY(self, argsList):
		'units xy coords set manually'
		pPlot,pUnit = argsList
		if (not self.__LOG_MOVEMENT):
			return
			
	def onUnitCreated(self, argsList):
		'Unit Completed'
		unit = argsList[0]
		player = gc.getPlayer(unit.getOwner())

		# Получаем информацию о созданном юните и игроке
		unitName = gc.getUnitInfo(unit.getUnitType()).getDescription()
		playerName = player.getName()

		# Формируем сообщение для лога
		log_message = "Turn %d: Player %s created unit %s at location (%d, %d).\n" % (
			gc.getGame().getGameTurn(), 
			encode(playerName), 
			encode(unitName), 
			unit.getX(), 
			unit.getY()
		)

		# Записываем сообщение в лог-файл
		try:
			f = open(str(gc.getGame().getName()) + '_unit_death_log.txt', 'a')  # Открываем файл в режиме добавления
			f.write(log_message)
			f.close()
		except Exception, e:
			CvUtil.pyPrint("Ошибка записи в лог-файл: %s" % str(e))

		# Проверяем, был ли юнит нанят (если это применимо)
		if unit.isHired():
			self.logHiredUnit(unit.getOwner(), unit.getUnitType())
		
		if (not self.__LOG_UNITBUILD):
			return

	def onUnitBuilt(self, argsList):
		'Unit Completed'
		city = argsList[0]
		unit = argsList[1]
		player = gc.getPlayer(city.getOwner())

		# Получаем информацию о созданном юните, игроке и городе
		unitName = gc.getUnitInfo(unit.getUnitType()).getDescription()
		playerName = player.getName()
		cityName = city.getName()

		# Формируем сообщение для лога
		log_message = "Turn %d: Player %s built unit %s in city %s at location (%d, %d).\n" % (
			gc.getGame().getGameTurn(), 
			encode(playerName), 
			encode(unitName), 
			encode(cityName), 
			city.getX(), 
			city.getY()
		)

		# Записываем сообщение в лог-файл
		try:
			f = open(str(gc.getGame().getName()) + '_unit_death_log.txt', 'a')  # Открываем файл в режиме добавления
			f.write(log_message)
			f.close()
		except Exception, e:
			CvUtil.pyPrint("Ошибка записи в лог-файл: %s" % str(e))

		# Вызываем стандартные действия для завершения строительства юнита
		CvAdvisorUtils.unitBuiltFeats(city, unit)

		if (not self.__LOG_UNITBUILD):
			return
		CvUtil.pyPrint('%s was finished by Player %d Civilization %s'
			%(gc.getUnitInfo(unit.getUnitType()).getDescription(), player.getID(), player.getCivilizationDescription(0)))

	def onUnitKilled(self, argsList):
		'Unit Killed'
		unit, iAttacker, = argsList
		player = gc.getPlayer(unit.getOwner())
		attacker = gc.getPlayer(iAttacker)
		# if player.isHuman():
		# 	# Получаем информацию о юните и атакующем
		# 	unitName = gc.getUnitInfo(unit.getUnitType()).getDescription()
		# 	attackerName = gc.getPlayer(iAttacker).getCivilizationDescription(0)
			
		# 	# Формируем сообщение для лога
		# 	log_message = "Turn %d: Player %s's юнит %s был убит игроком %s's.\n" % (
		# 		gc.getGame().getGameTurn(), 
		# 		encode(player.getName()), 
		# 		encode(unitName), 
		# 		encode(attackerName)
		# 	)
			
		# 	# Записываем сообщение в лог-файл
		# 	try:
		# 		f = open(str(gc.getGame().getName()) + '_unit_death_log.txt', 'a')  # Открываем файл в режиме добавления
		# 		f.write(log_message)
		# 		f.close()
		# 	except Exception, e:
		# 		CvUtil.pyPrint("Ошибка записи в лог-файл: %s" % str(e))

		if (not self.__LOG_UNITKILLED):
			return
		CvUtil.pyPrint('Player %d Civilization %s Unit %s was killed by Player %d'
			%(player.getID(), player.getCivilizationDescription(0), gc.getUnitInfo(unit.getUnitType()).getDescription(), attacker.getID()))

	def onUnitLost(self, argsList):
		'Unit Lost'
		unit = argsList[0]
		player = gc.getPlayer(unit.getOwner())
		if (not self.__LOG_UNITLOST):
			return
		CvUtil.pyPrint('%s was lost by Player %d Civilization %s'
			%(gc.getUnitInfo(unit.getUnitType()).getDescription(), player.getID(), player.getCivilizationDescription(0)))

	def onUnitPromoted(self, argsList):
		'Unit Promoted'
		pUnit, iPromotion = argsList
		player = gc.getPlayer(pUnit.getOwner())
		if (not self.__LOG_UNITPROMOTED):
			return
		CvUtil.pyPrint('Unit Promotion Event: %s - %s' %(player.getCivilizationDescription(0), pUnit.getName(),))

	def onUnitRename(self, argsList):
		'Unit is renamed'
		pUnit = argsList[0]
		if (pUnit.getOwner() == gc.getGame().getActivePlayer()):
			self.__eventEditUnitNameBegin(pUnit)

	def onUnitPillage(self, argsList):
		'Unit pillages a plot'
		pUnit, iImprovement, iRoute, iOwner = argsList
		iPlotX = pUnit.getX()
		iPlotY = pUnit.getY()
		pPlot = CyMap().plot(iPlotX, iPlotY)

		if (not self.__LOG_UNITPILLAGE):
			return
		CvUtil.pyPrint("Player %d's %s pillaged improvement %d and route %d at plot at (%d, %d)"
			%(iOwner, gc.getUnitInfo(pUnit.getUnitType()).getDescription(), iImprovement, iRoute, iPlotX, iPlotY))

	def onUnitGifted(self, argsList):
		'Unit is gifted from one player to another'
		pUnit, iGiftingPlayer, pPlotLocation = argsList

		# Получаем информацию о подаренном юните, дарителе и получателе
		unitName = gc.getUnitInfo(pUnit.getUnitType()).getDescription()
		giftingPlayer = gc.getPlayer(iGiftingPlayer)
		receivingPlayer = gc.getPlayer(pUnit.getOwner())

		# Формируем сообщение для лога
		log_message = "Turn %d: Player %s gifted unit %s to Player %s at location (%d, %d).\n" % (
			gc.getGame().getGameTurn(), 
			encode(giftingPlayer.getName()), 
			encode(unitName), 
			encode(receivingPlayer.getName()),
			pPlotLocation.getX(), 
			pPlotLocation.getY()
		)

		# Записываем сообщение в лог-файл
		try:
			f = open(str(gc.getGame().getName()) + '_unit_death_log.txt', 'a')  # Открываем файл в режиме добавления
			f.write(log_message)
			f.close()
		except Exception, e:
			CvUtil.pyPrint("Ошибка записи в лог-файл: %s" % str(e))

	def onUnitBuildImprovement(self, argsList):
		'Unit begins enacting a Build (building an Improvement or Route)'
		pUnit, iBuild, bFinished = argsList

	def onUnitSelected(self, argsList):
		pUnit = argsList[0]
		CvAdvisorUtils.unitSelectedFeats(pUnit)
		
	def onMissionaryConvertedUnit(self, argsList):
		pUnit = argsList[0]
		CvAdvisorUtils.addUnitToNagList(pUnit)

	def onGoodyReceived(self, argsList):
		'Goody received'
		iPlayer, pPlot, pUnit, iGoodyType = argsList
		if (not self.__LOG_GOODYRECEIVED):
			return
		CvUtil.pyPrint('%s received a goody' %(gc.getPlayer(iPlayer).getCivilizationDescription(0)),)

	# def onChangeWar(self, argsList):
	# 	'War Status Changes'
	# 	bIsWar = argsList[0]
	# 	iTeam = argsList[1]
	# 	iRivalTeam = argsList[2]
	# 	f = open(str(gc.getGame().getName()) + '.txt', 'a')
	# 	f.write('ChangeWar\n')
	# 	f.write(str(gc.getPlayer(gc.getTeam(iTeam).getLeaderID()).getName()) + ' теперь враждует с ' + str(
	# 		gc.getPlayer(gc.getTeam(iRivalTeam).getLeaderID()).getName()) + '\n')
	# 	if not (bIsWar):
	# 		# TAC Baby Boom Event Start
	# 		pPlayer = gc.getPlayer(gc.getTeam(iTeam).getLeaderID())
	# 		pRivalPlayer = gc.getPlayer(gc.getTeam(iRivalTeam).getLeaderID())
	# 		if gc.getNumEventTriggerInfos() > 0: # prevents mods that don't have events from getting an error
	# 			iEvent = CvUtil.findInfoTypeNum('EVENTTRIGGER_BABY_BOOM')
	# 			if iEvent != -1 and gc.getGame().isEventActive(iEvent):
	# 				pPlayer.trigger(iEvent)
	# 				pRivalPlayer.trigger(iEvent)
	# 		# TAC Baby Boom Event Ende
	# 	if (not self.__LOG_WARPEACE):
	# 		return
	# 	if (bIsWar):
	# 		strStatus = "declared war"
	# 	else:
	# 		strStatus = "declared peace"
	# 	CvUtil.pyPrint('Team %d has %s on Team %d'
	# 		%(iTeam, strStatus, iRivalTeam))



	def onDiplomacyEvent(self, argsList):
		'''
		Логирование дипломатических событий, таких как объявление войны, заключение мира, торговые соглашения и т.д.
		argsList: Список аргументов, содержащий информацию о событии.
		'''
		eventType, iPlayer1, iPlayer2, additionalInfo = argsList  # Пример аргументов
		player1 = gc.getPlayer(iPlayer1)
		player2 = gc.getPlayer(iPlayer2)

		# Определяем тип события и формируем сообщение для лога
		if eventType == "WAR":
			message = "War declared: %s has declared war on %s" % (encode(player1.getName()), encode(player2.getName()))
		elif eventType == "PEACE":
			message = "Peace declared: %s has made peace with %s" % (encode(player1.getName()), encode(player2.getName()))
		elif eventType == "TRADE_AGREEMENT":
			message = "Trade agreement: %s and %s have signed a trade agreement" % (encode(player1.getName()), encode(player2.getName()))
		elif eventType == "ALLIANCE":
			message = "Alliance formed: %s and %s have formed an alliance" % (encode(player1.getName()), encode(player2.getName()))
		else:
			message = "Diplomatic event: %s and %s have interacted in an unknown way" % (encode(player1.getName()), encode(player2.getName()))

		# Записываем сообщение в лог-файл
		try:
			f = open(str(gc.getGame().getName()) + '_diplomacy_log.txt', 'a')  # Открываем файл в режиме добавления
			f.write("Turn %d: %s\n" % (gc.getGame().getGameTurn(), message))
			f.close()
		except Exception, e:
			CvUtil.pyPrint("Ошибка записи в лог-файл: %s" % str(e))

	def onChangeWar(self, argsList):
		'''
		Логирование объявления войны и заключения мира.
		'''	
		bIsWar, iTeam, iRivalTeam = argsList
		iPlayer1 = gc.getTeam(iTeam).getLeaderID()
		iPlayer2 = gc.getTeam(iRivalTeam).getLeaderID()

		# Вызываем onDiplomacyEvent для логирования
		if bIsWar:
			self.onDiplomacyEvent(("WAR", iPlayer1, iPlayer2, None))
		else:
			self.onDiplomacyEvent(("PEACE", iPlayer1, iPlayer2, None))

		# Остальная часть функции onChangeWar
		try:
			f = open(str(gc.getGame().getName()) + '.txt', 'a')  # Открываем файл в режиме добавления
			if bIsWar:
				f.write('War Declared: Team %s has declared war on Team %s\n' % (
					encode(gc.getPlayer(gc.getTeam(iTeam).getLeaderID()).getName()),
					encode(gc.getPlayer(gc.getTeam(iRivalTeam).getLeaderID()).getName())))
			else:
				f.write('Peace Declared: Team %s has made peace with Team %s\n' % (
					encode(gc.getPlayer(gc.getTeam(iTeam).getLeaderID()).getName()),
					encode(gc.getPlayer(gc.getTeam(iRivalTeam).getLeaderID()).getName())))
			f.close()
		except Exception, e:
			CvUtil.pyPrint('Ошибка записи в лог-файл: %s' % str(e))

		# Дополнительная логика (ивент Baby Boom)
		if not bIsWar:
			pPlayer = gc.getPlayer(gc.getTeam(iTeam).getLeaderID())
			pRivalPlayer = gc.getPlayer(gc.getTeam(iRivalTeam).getLeaderID())
			if gc.getNumEventTriggerInfos() > 0:  # Проверка наличия событий
				iEvent = CvUtil.findInfoTypeNum('EVENTTRIGGER_BABY_BOOM')
				if iEvent != -1 and gc.getGame().isEventActive(iEvent):
					pPlayer.trigger(iEvent)
					pRivalPlayer.trigger(iEvent)

		if not self.__LOG_WARPEACE:
			return

		if bIsWar:
			strStatus = "declared war"
		else:
			strStatus = "declared peace"

		CvUtil.pyPrint('Team %d has %s on Team %d' % (iTeam, strStatus, iRivalTeam))




	def onChat(self, argsList):
		'Chat Message Event'
		chatMessage = "%s" %(argsList[0],)

	def onSetPlayerAlive(self, argsList):
		'Set Player Alive Event'
		iPlayerID = argsList[0]
		bNewValue = argsList[1]
		CvUtil.pyPrint("Player %d's alive status set to: %d" %(iPlayerID, int(bNewValue)))

	def onPlayerGoldTrade(self, argsList):
		'Player Trades gold to another player'
		iFromPlayer, iToPlayer, iGoldAmount = argsList

	def onCityBuilt(self, argsList):
		'City Built'
		city = argsList[0]

		if gc.getPlayer(city.getOwner()).isHuman():  # Если ходит человек
			city_file_name = str(gc.getGame().getName()) + str(encode(gc.getPlayer(city.getOwner()).getName())) + '_CITY.txt'
			print("Создан файл для города: %s" % city_file_name)  # Отладочное сообщение

			# Получаем словарь из файла
			PLAYER_CITY = get_dict(city_file_name)
			keys = encode(gc.getPlayer(city.getOwner()).getName())  # имя игрока

			if keys in PLAYER_CITY.keys():  # если имя игрока есть в словаре
				LIST = []
				for i in PLAYER_CITY[keys]:  # перебираем id городов
					LIST.append(i)
				LIST.append(city.getID())
				PLAYER_CITY[keys] = LIST
			else:
				PLAYER_CITY[keys] = [city.getID()]

			# Записываем итоговый словарь в файл
			try:
				f = open(city_file_name, 'w')
				f.write(str(PLAYER_CITY))
				print("Данные о городе записаны: %s" % str(PLAYER_CITY))  # Отладочное сообщение
			finally:
				f.close()

		# Остальная часть функции
		if (city.getOwner() == gc.getGame().getActivePlayer() and gc.getGame().getAIAutoPlay() == 0 and gc.getPlayer(city.getOwner()).isHuman()):
			self.__eventEditCityNameBegin(city, False)

		if (not self.__LOG_CITYBUILT):
			return
		CvUtil.pyPrint('City Built Event: %s' % (city.getName()))

	def onCityRazed(self, argsList):
		'City Razed'
		city, iPlayer = argsList
		iOwner = city.findHighestCulture()

		CvUtil.pyPrint("City Razed Event: %s" %(city.getName(),))

	def onCityAcquired(self, argsList):
		'City Acquired'
		iPreviousOwner,iNewOwner,pCity,bConquest,bTrade = argsList
		CvUtil.pyPrint('City Acquired Event: %s' %(pCity.getName()))

	def onCityAcquiredAndKept(self, argsList):
		'City Acquired and Kept'
		iOwner,pCity = argsList
		CvUtil.pyPrint('City Acquired and Kept Event: %s' %(pCity.getName()))

	def onCityLost(self, argsList):
		'City Lost'
		city = argsList[0]
		player = gc.getPlayer(city.getOwner())

		if gc.getPlayer(city.getOwner()).isHuman():  # Если ходит человек
			city_file_name = str(gc.getGame().getName()) + str(encode(gc.getPlayer(city.getOwner()).getName())) + '_CITY.txt'
			print "Файл для города: %s" % city_file_name  # Отладочное сообщение

			# Получаем словарь из файла
			PLAYER_CITY = get_dict(city_file_name)
			keys = str(encode(gc.getPlayer(city.getOwner()).getName()))  # имя игрока

			if encode(keys) in PLAYER_CITY.keys():
				new_list_city = []
				for i in PLAYER_CITY[encode(keys)]:
					if str(i) != str(city.getID()):
						new_list_city.append(i)
				PLAYER_CITY[encode(keys)] = new_list_city

				# Записываем обновленный словарь в файл
				try:
					f = open(city_file_name, 'w')
					f.write(str(PLAYER_CITY))
					print "Данные о городе обновлены: %s" % str(PLAYER_CITY)  # Отладочное сообщение
				finally:
					f.close()

		if (not self.__LOG_CITYLOST):
			return
		CvUtil.pyPrint('City %s was lost by Player %d Civilization %s'
					% (city.getName(), player.getID(), player.getCivilizationDescription(0)))

	def onCultureExpansion(self, argsList):
		'City Culture Expansion'
		pCity = argsList[0]
		iPlayer = argsList[1]
		CvUtil.pyPrint("City %s's culture has expanded" %(pCity.getName(),))

	def onCityGrowth(self, argsList):
		'City Population Growth'
		pCity = argsList[0]
		iPlayer = argsList[1]
		CvUtil.pyPrint("%s has grown" %(pCity.getName(),))

	def onCityDoTurn(self, argsList):
		'City Production'
		pCity = argsList[0]
		iPlayer = argsList[1]

		CvAdvisorUtils.cityAdvise(pCity, iPlayer)

	def onCityBuildingUnit(self, argsList):
		'City begins building a unit'
		pCity = argsList[0]
		iUnitType = argsList[1]
		if (not self.__LOG_CITYBUILDING):
			return
		CvUtil.pyPrint("%s has begun building a %s" %(pCity.getName(),gc.getUnitInfo(iUnitType).getDescription()))

	def onCityBuildingBuilding(self, argsList):
		'City begins building a Building'
		pCity = argsList[0]
		iBuildingType = argsList[1]

		if (not self.__LOG_CITYBUILDING):
			return
		CvUtil.pyPrint("%s has begun building a %s" % (pCity.getName(), gc.getBuildingInfo(iBuildingType).getDescription()))

	def onCityRename(self, argsList):
		'City is renamed'
		pCity = argsList[0]
		if (pCity.getOwner() == gc.getGame().getActivePlayer()):
			try:
				player = gc.getPlayer(pCity.getOwner())
				old_name = pCity.getName()  # Получаем старое имя города
				self.__eventEditCityNameBegin(pCity, True)  # Вызываем стандартную логику переименования
				
				# После переименования логируем событие
				new_name = pCity.getName()  # Получаем новое имя города
				
				# Логирование переименования города
				log_message = "Turn %d: Player %s renamed city from '%s' to '%s'.\n" % (
					gc.getGame().getGameTurn(), 
					encode(player.getName()), 
					old_name, 
					new_name
				)
				
				# Записываем сообщение в лог-файл
				f = open(str(gc.getGame().getName()) + '_city_rename_log.txt', "a")
				f.write(log_message)
				f.close()
			except Exception, e:
				CvUtil.pyPrint("Ошибка при переименовании города: %s" % str(e))

	def onCreateTradeRoute(self, argsList):
		'Trade Route is Created'
		PlayerID = argsList[0]
		self.__eventCreateTradeRouteBegin(PlayerID)

	def onEditTradeRoute(self, argsList):
		'Trade Route is Modified'
		PlayerID = argsList[0]
		iRouteID = argsList[1]
		self.__eventEditTradeRouteBegin(PlayerID, iRouteID)

	def onCityHurry(self, argsList):
		'City is renamed'
		pCity = argsList[0]
		iHurryType = argsList[1]

	def onVictory(self, argsList):
		'Victory'
		iTeam, iVictory = argsList
		if (iVictory >= 0 and iVictory < gc.getNumVictoryInfos()):
			victoryInfo = gc.getVictoryInfo(int(iVictory))
			CvUtil.pyPrint("Victory!  Team %d achieves a %s victory"
				%(iTeam, victoryInfo.getDescription()))

	def onYieldSoldToEurope(self, argsList):
		'Yield Sold To Europe'
		iPlayer, iYield, iAmount = argsList
		player = gc.getPlayer(iPlayer)
		
		# Проверка, что игрок является человеком
		if player.isHuman():
			yieldName = gc.getYieldInfo(iYield).getDescription()
			
			# Логирование в файл
			try:
				f = open(str(gc.getGame().getName()) + '_trade_log.txt', 'a')  # Открываем файл в режиме добавления
				f.write("Turn %d: Player %s sold %d units of %s to Europe.\n" % (gc.getGame().getGameTurn(), encode(player.getName()), iAmount, encode(yieldName)))
				f.close()
			except Exception, e:
				CvUtil.pyPrint("Ошибка записи в лог-файл: %s" % str(e))

	def onYieldBoughtFromEurope(self, argsList):
		'Yield Bought From Europe'
		iPlayer, iYield, iAmount = argsList
		player = gc.getPlayer(iPlayer)
		
		# Проверка, что игрок является человеком
		if player.isHuman():
			yieldName = gc.getYieldInfo(iYield).getDescription()
			
			# Логирование в файл
			try:
				f = open(str(gc.getGame().getName()) + '_trade_log.txt', 'a')  # Открываем файл в режиме добавления
				f.write("Turn %d: Player %s bought %d units of %s from Europe.\n" % (gc.getGame().getGameTurn(), encode(player.getName()), iAmount, encode(yieldName)))
				f.close()
			except Exception, e:
				CvUtil.pyPrint("Ошибка записи в лог-файл: %s" % str(e))

	def onUnitBoughtFromEurope(self, argsList):
		'Unit Bought From Europe'
		iPlayer, iUnitId = argsList
		player = gc.getPlayer(iPlayer)

		# Проверка, что игрок является человеком
		if player.isHuman():
			unitName = player.getEuropeUnitById(iUnitId).getName()

			# Логирование найма юнита
			self.logHiredUnit(iPlayer, iUnitId)

			# Логирование в файл
			try:
				f = open(str(gc.getGame().getName()) + '_trade_log.txt', 'a')  # Открываем файл в режиме добавления
				f.write("Turn %d: Player %s bought a %s from Europe.\n" % (gc.getGame().getGameTurn(), encode(player.getName()), encode(unitName)))
				f.close()
			except Exception, e:
				CvUtil.pyPrint("Ошибка записи в лог-файл: %s" % str(e))



	def logHiredUnit(self, iPlayer, iUnitId):
		'''
		Логирование найма юнита.
		''' 
		player = gc.getPlayer(iPlayer)
		unitName = player.getEuropeUnitById(iUnitId).getName()
		
		try:
			f = open(str(gc.getGame().getName()) + '_hired_units_log.txt', 'a')  # Открываем файл в режиме добавления
			f.write("Turn %d: Player %s hired a %s.\n" % (gc.getGame().getGameTurn(), encode(player.getName()), encode(unitName)))
			f.close()
		except Exception, e:
			CvUtil.pyPrint("Ошибка записи в лог-файл: %s" % str(e))





	def onUnitTravelStateChanged(self, argsList):
		'Ship Arrived in Europe or America'
		iPlayer, iUnitTravelState, iUnitId = argsList

	def onEmmigrantAtDocks(self, argsList):
		'Emmigrant At Docks'
		iPlayer, iUnitId = argsList

	def onPopulationJoined(self, argsList):
		'Population Joined'
		iPlayer, iCityId, iUnitId = argsList

	def onPopulationUnjoined(self, argsList):
		'Population Unjoined'
		iPlayer, iCityId, iUnitId = argsList

	def onUnitLearned(self, argsList):
		'Unit Learned'
		iPlayer, iUnitId = argsList

	def onYieldProduced(self, argsList):
		'Yield Produced'
		iPlayer, iCityId, iYield = argsList

	def onGameUpdate(self, argsList):
		'sample generic event, called on each game turn slice'
		genericArgs = argsList[0][0]	# tuple of tuple of my args
		turnSlice = genericArgs[0]

	def onMouseEvent(self, argsList):
		'mouse handler - returns 1 if the event was consumed'
		eventType,mx,my,px,py,interfaceConsumed,screens = argsList
		if ( px!=-1 and py!=-1 ):
			if ( eventType == self.EventLButtonDown ):
				if (self.bAllowCheats and self.bCtrl and self.bAlt and CyMap().plot(px,py).isCity() and not interfaceConsumed):
					# Launch Edit City Event
					self.beginEvent( CvUtil.EventEditCity, (px,py) )
					return 1

				elif (self.bAllowCheats and self.bCtrl and self.bShift and not interfaceConsumed):
					# Launch Place Object Event
					self.beginEvent( CvUtil.EventPlaceObject, (px, py) )
					return 1

		if ( eventType == self.EventBack ):
			return CvScreensInterface.handleBack(screens)
		elif ( eventType == self.EventForward ):
			return CvScreensInterface.handleForward(screens)

		return 0


#################### TRIGGERED EVENTS ##################

	def __eventEditCityNameBegin(self, city, bRename):
		popup = CyPopup(CvUtil.EventEditCityName, EventContextTypes.EVENTCONTEXT_ALL, True)
		popup.setUserData((city.getID(), bRename))
		popup.setHeaderString(localText.getText("TXT_KEY_NAME_CITY", ()), CvUtil.FONT_CENTER_JUSTIFY)
		popup.setBodyString(localText.getText("TXT_KEY_SETTLE_NEW_CITY_NAME", ()), CvUtil.FONT_CENTER_JUSTIFY)
		popup.createEditBox(city.getName(), 0)
		popup.setEditBoxMaxCharCount( 15, 32, 0 )
		popup.launch(true, PopupStates.POPUPSTATE_IMMEDIATE)

	def __eventEditCityNameApply(self, playerID, userData, popupReturn):

		'Edit City Name Event'
		iCityID = userData[0]
		bRename = userData[1]
		player = gc.getPlayer(playerID)
		city = player.getCity(iCityID)
		cityName = popupReturn.getEditBoxString(0)
		if (len(cityName) > 30):
			cityName = cityName[:30]
		city.setName(cityName, not bRename)

	def __eventCreateTradeRouteBegin(self, PlayerID):
		popup = CyPopup(CvUtil.EventCreateTradeRoute, EventContextTypes.EVENTCONTEXT_ALL, 1)
		popup.setHeaderString(localText.getText("TXT_KEY_CREATE_TRADE_ROUTE", ()), CvUtil.FONT_LEFT_JUSTIFY)

		popup.setBodyString(localText.getText("TXT_KEY_SOURCE", ()), CvUtil.FONT_LEFT_JUSTIFY)
		popup.createPullDown(0)
		popup.addPullDownString(localText.getText("TXT_KEY_NO_SOURCE", ()), -1, 0)
		player = gc.getPlayer(PlayerID)
		for iPlayer in range(gc.getMAX_PLAYERS()):
			loopPlayer = gc.getPlayer(iPlayer)
			if (loopPlayer.isAlive() and player.canLoadYield(iPlayer)):
				(pCity, iter) = loopPlayer.firstCity(false)
				while (pCity):
					iId = gc.getMAX_PLAYERS() * pCity.getID() + pCity.getOwner()
					popup.addPullDownString(pCity.getName(), iId, 0)
					(pCity, iter) = loopPlayer.nextCity(iter, false)

		popup.setBodyString(localText.getText("TXT_KEY_DESTINATION", ()), CvUtil.FONT_LEFT_JUSTIFY)
		popup.createPullDown(1)
		popup.addPullDownString(localText.getText("TXT_KEY_NO_DESTINATION", ()), -1, 1)
		for iPlayer in range(gc.getMAX_PLAYERS()):
			loopPlayer = gc.getPlayer(iPlayer)
			if (loopPlayer.isAlive() and player.canUnloadYield(iPlayer)):
				(pCity, iter) = loopPlayer.firstCity(false)
				while (pCity):
					iId = gc.getMAX_PLAYERS() * pCity.getID() + pCity.getOwner()
					popup.addPullDownString(pCity.getName(), iId, 1)
					(pCity, iter) = loopPlayer.nextCity(iter, false)

		popup.setBodyString(localText.getText("TXT_KEY_YIELD", ()), CvUtil.FONT_LEFT_JUSTIFY)
		popup.createPullDown(2)
		popup.addPullDownString(localText.getText("TXT_KEY_NO_YIELD", ()), -1, 2)
		for i in range( YieldTypes.NUM_YIELD_TYPES ):
			if (gc.getYieldInfo(i).isCargo()):
				popup.addPullDownString(gc.getYieldInfo(i).getDescription(), i, 2)

		popup.launch(true, PopupStates.POPUPSTATE_IMMEDIATE)

	def __eventCreateTradeRouteApply(self, playerID, userData, popupReturn):
		'Create Trade Route Event'
		if (popupReturn.getSelectedPullDownValue(0) != -1 and popupReturn.getSelectedPullDownValue(1) != -1 and popupReturn.getSelectedPullDownValue(2) != -1):
			iSourceCityID = popupReturn.getSelectedPullDownValue( 0 ) / gc.getMAX_PLAYERS()
			iSourceCityPlayer = popupReturn.getSelectedPullDownValue( 0 ) % gc.getMAX_PLAYERS()
			iDestinationCityID = popupReturn.getSelectedPullDownValue( 1 ) / gc.getMAX_PLAYERS()
			iDestinationCityPlayer = popupReturn.getSelectedPullDownValue( 1 ) % gc.getMAX_PLAYERS()
			iYieldType = popupReturn.getSelectedPullDownValue( 2 )

			player = gc.getPlayer(playerID)
			gc.getPlayer(playerID).addTradeRoute(iSourceCityPlayer, iSourceCityID, iDestinationCityPlayer, iDestinationCityID, iYieldType)

	def __eventEditTradeRouteBegin(self, playerID, iRouteID):
		popup = CyPopup(CvUtil.EventEditTradeRoute, EventContextTypes.EVENTCONTEXT_ALL, 1)
		popup.setHeaderString(localText.getText("TXT_KEY_EDIT_TRADE_ROUTE", ()), CvUtil.FONT_LEFT_JUSTIFY)

		player = gc.getPlayer(playerID)
		pRoute = player.getTradeRoute(iRouteID)
		popup.setUserData((iRouteID,))

		popup.setBodyString(localText.getText("TXT_KEY_SOURCE", ()), CvUtil.FONT_LEFT_JUSTIFY)
		popup.createPullDown(0)
		for iPlayer in range(gc.getMAX_PLAYERS()):
			loopPlayer = gc.getPlayer(iPlayer)
			if (loopPlayer.isAlive() and player.canLoadYield(iPlayer)):
				(pCity, iter) = loopPlayer.firstCity(false)
				while (pCity):
					iId = gc.getMAX_PLAYERS() * pCity.getID() + pCity.getOwner()
					popup.addPullDownString(pCity.getName(), iId, 0)
					if (pRoute.getSourceCity().iID == pCity.getID() and pRoute.getSourceCity().eOwner == pCity.getOwner()):
						popup.setSelectedPulldownID(iId, 0);
					(pCity, iter) = loopPlayer.nextCity(iter, false)

		popup.setBodyString(localText.getText("TXT_KEY_DESTINATION", ()), CvUtil.FONT_LEFT_JUSTIFY)
		popup.createPullDown(1)
		for iPlayer in range(gc.getMAX_PLAYERS()):
			loopPlayer = gc.getPlayer(iPlayer)
			if (loopPlayer.isAlive() and player.canUnloadYield(iPlayer)):
				(pCity, iter) = loopPlayer.firstCity(false)
				while (pCity):
					iId = gc.getMAX_PLAYERS() * pCity.getID() + pCity.getOwner()
					popup.addPullDownString(pCity.getName(), iId, 1)
					if (pRoute.getDestinationCity().iID == pCity.getID() and pRoute.getDestinationCity().eOwner == pCity.getOwner()):
						popup.setSelectedPulldownID(iId, 1);
					(pCity, iter) = loopPlayer.nextCity(iter, false)

				if player.canTradeWithEurope():
					popup.addPullDownString(localText.getText("TXT_KEY_CONCEPT_EUROPE", ()), -1, 1)

				if (pRoute.getDestinationCity().iID == -1 and pRoute.getDestinationCity().eOwner == playerID):
					popup.setSelectedPulldownID(-1, 1);


		popup.setBodyString(localText.getText("TXT_KEY_YIELD", ()), CvUtil.FONT_LEFT_JUSTIFY)
		popup.createPullDown(2)
		for i in range( YieldTypes.NUM_YIELD_TYPES ):
			if (gc.getYieldInfo(i).isCargo()):
				popup.addPullDownString(gc.getYieldInfo(i).getDescription(), i, 2)
		popup.setSelectedPulldownID(pRoute.getYield(), 2);

		popup.createCheckBoxes( 1, 3 )
		popup.setCheckBoxText( 0, localText.getText("TXT_KEY_DELETE_TRADE_ROUTE", ()), 3 )

		popup.createCheckBoxes( 1, 4 )
		popup.setCheckBoxText( 0, localText.getText("TXT_KEY_CREATE_TRADE_ROUTE", ()), 4 )

		popup.launch(true, PopupStates.POPUPSTATE_IMMEDIATE)

	def __eventEditTradeRouteApply(self, PlayerID, userData, popupReturn):
		'Edit Trade Route Event'
		iSourceCityID = popupReturn.getSelectedPullDownValue( 0 ) / gc.getMAX_PLAYERS()
		iSourceCityPlayer = popupReturn.getSelectedPullDownValue( 0 ) % gc.getMAX_PLAYERS()
		iDestinationCityID = popupReturn.getSelectedPullDownValue( 1 ) / gc.getMAX_PLAYERS()
		iDestinationCityPlayer = popupReturn.getSelectedPullDownValue( 1 ) % gc.getMAX_PLAYERS()
		iYieldType = popupReturn.getSelectedPullDownValue( 2 )

		iRouteID = userData[0]
		player = gc.getPlayer(PlayerID)

		if (popupReturn.getCheckboxBitfield(3)):
			player.removeTradeRoute(iRouteID)
		elif (popupReturn.getCheckboxBitfield(4)):
			player.addTradeRoute(iSourceCityPlayer, iSourceCityID, iDestinationCityPlayer, iDestinationCityID, iYieldType)
		else:
			player.editTradeRoute(iRouteID, iSourceCityPlayer, iSourceCityID, iDestinationCityPlayer, iDestinationCityID, iYieldType)

	def __eventEditCityBegin(self, argsList):
		'Edit City Event'
		px,py = argsList
		CvWBPopups.CvWBPopups().initEditCity(argsList)

	def __eventEditCityApply(self, playerID, userData, popupReturn):
		'Edit City Event Apply'
		if (getChtLvl() > 0):
			CvWBPopups.CvWBPopups().applyEditCity( (popupReturn, userData) )

	def __eventPlaceObjectBegin(self, argsList):
		'Place Object Event'
		CvDebugTools.CvDebugTools().initUnitPicker(argsList)

	def __eventPlaceObjectApply(self, playerID, userData, popupReturn):
		'Place Object Event Apply'
		if (getChtLvl() > 0):
			CvDebugTools.CvDebugTools().applyUnitPicker( (popupReturn, userData) )
	def __EventAwardGoldBegin(self, argsList):
		'Award Gold Event'
		CvDebugTools.CvDebugTools().cheatGold()
	def __EventAwardGoldApply(self, playerID, netUserData, popupReturn):
		'Award Gold Event Apply'

		if (getChtLvl() > 0):
			CvDebugTools.CvDebugTools().applyGoldCheat( (popupReturn) )

	def __eventShowWonderBegin(self, argsList):
		'Show Wonder Event'
		CvDebugTools.CvDebugTools().wonderMovie()

	def __eventShowWonderApply(self, playerID, netUserData, popupReturn):
		'Wonder Movie Apply'
		if (getChtLvl() > 0):
			CvDebugTools.CvDebugTools().applyWonderMovie( (popupReturn) )

	def __eventEditUnitNameBegin(self, argsList):
		pUnit = argsList
		popup = CyPopup(CvUtil.EventEditUnitName, EventContextTypes.EVENTCONTEXT_ALL, True)
		popup.setUserData((pUnit.getID(),))
		popup.setBodyString(localText.getText("TXT_KEY_RENAME_UNIT", ()), CvUtil.FONT_CENTER_JUSTIFY)
		popup.createEditBox(pUnit.getNameNoDesc(), 0)
		popup.setEditBoxMaxCharCount(20, 20, 0)
		popup.launch(true, PopupStates.POPUPSTATE_IMMEDIATE)

	def __eventEditUnitNameApply(self, playerID, userData, popupReturn):

		'Edit Unit Name Event'
		iUnitID = userData[0]
		unit = gc.getPlayer(playerID).getUnit(iUnitID)
		newName = popupReturn.getEditBoxString(0)
		if (len(newName) > 25):
			newName = newName[:25]
		unit.setName(newName)

	def __eventWBAllPlotsPopupBegin(self, argsList):
		CvScreensInterface.getWorldBuilderScreen().allPlotsCB()
		return
	def __eventWBAllPlotsPopupApply(self, playerID, userData, popupReturn):
		if (popupReturn.getButtonClicked() >= 0):
			CvScreensInterface.getWorldBuilderScreen().handleAllPlotsCB(popupReturn)
		return

	def __eventWBLandmarkPopupBegin(self, argsList):
		CvScreensInterface.getWorldBuilderScreen().setLandmarkCB("")
		return

	def __eventWBLandmarkPopupApply(self, playerID, userData, popupReturn):
		if (popupReturn.getEditBoxString(0)):
			szLandmark = popupReturn.getEditBoxString(0)
			if (len(szLandmark)):
				CvScreensInterface.getWorldBuilderScreen().setLandmarkCB(szLandmark)
		return

	def __eventWBScriptPopupBegin(self, argsList):
		popup = CyPopup(CvUtil.EventWBScriptPopup, EventContextTypes.EVENTCONTEXT_ALL, True)
		popup.setHeaderString(localText.getText("TXT_KEY_WB_SCRIPT", ()), CvUtil.FONT_CENTER_JUSTIFY)
		popup.createEditBox(CvScreensInterface.getWorldBuilderScreen().getCurrentScript(), 0)
		popup.launch(true, PopupStates.POPUPSTATE_IMMEDIATE)

	def __eventWBScriptPopupApply(self, playerID, userData, popupReturn):
		if (popupReturn.getEditBoxString(0)):
			szScriptName = popupReturn.getEditBoxString(0)
			CvScreensInterface.getWorldBuilderScreen().setScriptCB(szScriptName)

	def __eventWBStartYearPopupBegin(self, argsList):
		popup = CyPopup(CvUtil.EventWBStartYearPopup, EventContextTypes.EVENTCONTEXT_ALL, True)
		popup.createSpinBox(0, "", gc.getGame().getStartYear(), 1, 5000, -5000)
		popup.launch(true, PopupStates.POPUPSTATE_IMMEDIATE)

	def __eventWBStartYearPopupApply(self, playerID, userData, popupReturn):
		iStartYear = popupReturn.getSpinnerWidgetValue(int(0))
		CvScreensInterface.getWorldBuilderScreen().setStartYearCB(iStartYear)
		
# Dale - AoD: AoDCheatMenu START
	def AoDCheatMenuBegin(self, argsList):
		popup = CyPopup(CvUtil.EventAoDCheatMenu, EventContextTypes.EVENTCONTEXT_ALL, True)
		popup.setHeaderString(localText.getText("TXT_KEY_CHEATMENU_TITLE", ()), CvUtil.FONT_CENTER_JUSTIFY)
		popup.setBodyString(localText.getText("TXT_KEY_CHEATMENU_TEXT", ()), CvUtil.FONT_CENTER_JUSTIFY)
		popup.addButton(localText.getText("TXT_KEY_CHEATMENU_CANCEL", ()))
		popup.addSeparator()
		popup.setBodyString(localText.getText("TXT_KEY_AIAUTOPLAY", ()), CvUtil.FONT_CENTER_JUSTIFY)
		popup.createSpinBox(0, "", 0, 5, 300, 0)
		popup.addButton(localText.getText("TXT_KEY_AIAUTOPLAY10", ()))
		popup.addButton(localText.getText("TXT_KEY_AIAUTOPLAY50", ()))
		popup.addSeparator()
		popup.setBodyString(localText.getText("TXT_KEY_MONEYTREE", ()), CvUtil.FONT_CENTER_JUSTIFY)
		popup.createSpinBox(1, "", 0, 100, 10000, 0)
		popup.addButton(localText.getText("TXT_KEY_MONEYTREE1000", ()))
		popup.addButton(localText.getText("TXT_KEY_MONEYTREE5000", ()))
		popup.addSeparator()
		popup.launch(True, PopupStates.POPUPSTATE_IMMEDIATE)
		return

	def AoDCheatMenuApply(self, playerID, userData, popupReturn):
		autoIdx = popupReturn.getButtonClicked()
		iPlayer = gc.getPlayer(playerID)
		iAutoplay = 0
		iAutoplay = popupReturn.getSpinnerWidgetValue(int(0))
		if (iAutoplay > 0):
			CyGame().setAIAutoPlay(iAutoplay)
		if (autoIdx == 0):
			return
		if (autoIdx == 1):
			CyGame().setAIAutoPlay(10)
		if (autoIdx == 2):
			CyGame().setAIAutoPlay(50)
		iMoneyTree = 0
		iMoneyTree = popupReturn.getSpinnerWidgetValue(int(1))
		if (iMoneyTree > 0):
			iPlayer.changeGold(iMoneyTree)
		if (autoIdx == 3):
			iPlayer.changeGold(1000)
		if (autoIdx == 4):
			iPlayer.changeGold(5000)
		return
# Dale - AoD: AoDCheatMenu END

# EuropeScreen START	
	def doEuropeScreenBegin(self, argslist):
		return 0
	
	def doEuropeScreenApply(self, playerID, userData, popupReturn):
		iMode, iUnit, iX, iY, iCityX, iCityY, iSellPrice, iYield, iBoycottPrice = userData
		
		SEND_TO_NEW_WORLD_CITY = 0
		SEND_TO_EAST_OR_WEST = 1
		RECALL_TO_EUROPE = 2
		SELL_SHIP_IN_EUROPE = 3
		LIFT_BOYCOTT_IN_EUROPE = 4
		RECALL_TO_AFRICA = 5
		RECALL_TO_PORT_ROYAL = 8
				
		player = gc.getPlayer(playerID)
		transport = player.getUnit(iUnit)
		
		if iMode == SEND_TO_NEW_WORLD_CITY:
			transport.getGroup().clearMissionQueue ()
			transport.getGroup().pushMoveToMission(iCityX, iCityY)
			if not iX == transport.getX() or not iY == transport.getY():
				transport.setXY(iX, iY, true, false, false)
		elif iMode == SEND_TO_EAST_OR_WEST:
			if not iX == transport.getX() or not iY == transport.getY():
				transport.setXY(iX, iY, true, false, false)
		elif iMode == RECALL_TO_EUROPE:
			transport.setUnitTravelState(1,false)
			transport.getGroup().clearMissionQueue()
		elif iMode == RECALL_TO_AFRICA:
			transport.setUnitTravelState(5,false)
			transport.getGroup().clearMissionQueue()
		elif iMode == RECALL_TO_PORT_ROYAL:
			transport.setUnitTravelState(8,false)
			transport.getGroup().clearMissionQueue()
		elif iMode == SELL_SHIP_IN_EUROPE:
			if (not transport.isNone() and not iSellPrice == -1):
				transport.kill(false)
				player.changeGold(iSellPrice)
				CyInterface().setDirty(InterfaceDirtyBits.EuropeScreen_DIRTY_BIT, true)
				CyInterface().setDirty(InterfaceDirtyBits.AfricaScreen_DIRTY_BIT, true)
				CyInterface().setDirty(InterfaceDirtyBits.PortRoyalScreen_DIRTY_BIT, true)
		elif iMode == LIFT_BOYCOTT_IN_EUROPE:
			if (not iYield == -1 and (player.getGold() - iBoycottPrice) >= 0):
				player.setYieldEuropeTradable(iYield, true)
				player.changeGold(-iBoycottPrice)
				CyInterface().setDirty(InterfaceDirtyBits.EuropeScreen_DIRTY_BIT, true)
				CyInterface().setDirty(InterfaceDirtyBits.AfricaScreen_DIRTY_BIT, true)
				
		return 0
		
# EuropeScreen END

