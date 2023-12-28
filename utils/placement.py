from typing import final
from dataclasses import dataclass

from pcbnew import BOARD_ITEM, FOOTPRINT, VECTOR2I


@final
@dataclass
class Placement():
	x: int
	y: int
	angle: float
	flipped: bool

	@staticmethod
	def of(item: BOARD_ITEM) -> "Placement":
		if isinstance(item, FOOTPRINT):  # Also PAD, but we don't consider those yet
			position = item.GetPosition()
			return Placement(
				x=position.x,
				y=position.y,
				angle=item.GetOrientationDegrees(),
				flipped=item.IsFlipped(),
			)
		else:
			position = item.GetPosition()
			# Can not get rotation or flipped state for most items
			return Placement(
				x=position.x,
				y=position.y,
				angle=0,
				flipped=False,
			)

	@property
	def position(self):
		return VECTOR2I(
			x=self.x,
			y=self.y
		)
