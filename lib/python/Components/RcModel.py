from enigma import getBoxType
import os

class RcModel:
	RCTYPE_DMM = 0
	RCTYPE_DMM1 = 1
	RCTYPE_DMM2 = 2
	RCTYPE_ET4X00 = 3
	RCTYPE_ET6X00 = 4
	RCTYPE_ET6500 = 5
	RCTYPE_ET9X00 = 6
	RCTYPE_ET9500 = 7
	RCTYPE_GB = 8
	RCTYPE_INIX000 = 9
	RCTYPE_ODIN = 10
	RCTYPE_TM = 11
	RCTYPE_VU = 12
	RCTYPE_VU2 = 13
	RCTYPE_XP1000 = 14

	def __init__(self):
		self.currentRcType = self.RCTYPE_DMM
		self.readRcTypeFromProc()

	def rcIsDefault(self):
		if self.currentRcType != self.RCTYPE_DMM:
			return False
		return True

	def readFile(self, target):
		fp = open(target, 'r')
		out = fp.read()
		fp.close()
		return out.split()[0]

	def readRcTypeFromProc(self):
		if getBoxType() == 'dm8000':
			self.currentRcType = self.RCTYPE_DMM
		elif getBoxType() == 'dm7020hd':
			self.currentRcType = self.RCTYPE_DMM2
		elif getBoxType() == 'dm800' or getBoxType() == 'dm800se' or getBoxType() == 'dm500hd':
			self.currentRcType = self.RCTYPE_DMM1
		elif getBoxType().startswith('et'):
			model = self.readFile('/proc/stb/info/boxtype')
			rc = self.readFile('/proc/stb/ir/rc/type')
			if rc == '5':
				self.currentRcType = self.RCTYPE_ET9X00
			elif rc == '7':
				self.currentRcType = self.RCTYPE_ET6X00
			elif rc == '9' and model == 'et9500':
				self.currentRcType = self.RCTYPE_ET9500
			elif rc == '9' and model == 'et6500':
				self.currentRcType = self.RCTYPE_ET6500
			elif rc == '11' and model == 'et9200':
				self.currentRcType = self.RCTYPE_ET9500
			elif rc == '11' and model == 'et9000':
				self.currentRcType = self.RCTYPE_ET9X00
			elif rc == '13' and model == 'et4000':
				self.currentRcType = self.RCTYPE_ET4X00
		elif getBoxType().startswith('gb'):
			self.currentRcType = self.RCTYPE_GB
		elif getBoxType().startswith('odin'):
			self.currentRcType = self.RCTYPE_ODIN
		elif getBoxType().startswith('tm'):
				self.currentRcType = self.RCTYPE_TM
		elif getBoxType().startswith('venton'):
			model = self.readFile('/proc/stb/info/boxtype')
			if model.startswith('ini-'):
				self.currentRcType = self.RCTYPE_INIX000
		elif getBoxType().startswith('vu'):
			if getBoxType() == 'vuultimo':
				self.currentRcType = self.RCTYPE_VU2
			else:
				self.currentRcType = self.RCTYPE_VU
		elif getBoxType().startswith('xp'):
			self.currentRcType = self.RCTYPE_XP1000

	def getRcLocation(self):
		if self.currentRcType == self.RCTYPE_DMM:
			return '/usr/share/enigma2/rc_models/dmm0/'
		elif self.currentRcType == self.RCTYPE_DMM1:
			return '/usr/share/enigma2/rc_models/dmm1/'
		elif self.currentRcType == self.RCTYPE_DMM2:
			return '/usr/share/enigma2/rc_models/dmm2/'
		elif self.currentRcType == self.RCTYPE_ET4X00:
			return '/usr/share/enigma2/rc_models/et4x00/'
		elif self.currentRcType == self.RCTYPE_ET6X00:
			return '/usr/share/enigma2/rc_models/et6x00/'
		elif self.currentRcType == self.RCTYPE_ET6500:
			return '/usr/share/enigma2/rc_models/et6500/'
		elif self.currentRcType == self.RCTYPE_ET9X00:
			return '/usr/share/enigma2/rc_models/et9x00/'
		elif self.currentRcType == self.RCTYPE_ET9500:
			return '/usr/share/enigma2/rc_models/et9500/'
		elif self.currentRcType == self.RCTYPE_GB:
			return '/usr/share/enigma2/rc_models/gb/'
		elif self.currentRcType == self.RCTYPE_INIX000:
			return '/usr/share/enigma2/rc_models/inix000/'
		elif self.currentRcType == self.RCTYPE_ODIN:
			return '/usr/share/enigma2/rc_models/odin/'
		elif self.currentRcType == self.RCTYPE_TM:
			return '/usr/share/enigma2/rc_models/tm/'
		elif self.currentRcType == self.RCTYPE_VU:
			return '/usr/share/enigma2/rc_models/vu/'
		elif self.currentRcType == self.RCTYPE_VU2:
			return '/usr/share/enigma2/rc_models/vu2/'
		elif self.currentRcType == self.RCTYPE_XP1000:
			return '/usr/share/enigma2/rc_models/xp1000/'

rc_model = RcModel()
