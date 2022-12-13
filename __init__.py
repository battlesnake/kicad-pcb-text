import traceback
from .message_box import MessageBox

try:
	from .text_plugin import TextPluginWrapper
	from .clone_plugin import ClonePluginWrapper
except Exception as error:
	diagnostic = "".join(traceback.TracebackException.from_exception(error).format())
	MessageBox("Mark's plugin framework: Error", diagnostic)
