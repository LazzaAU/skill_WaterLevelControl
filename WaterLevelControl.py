from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class WaterLevelControl(AliceSkill):
	"""
	Author: LazzaAU
	Description: Monitor and control water level of your tanks
	"""

	@IntentHandler('MyIntentName')
	def dummyIntent(self, session: DialogSession, **_kwargs):
		pass
