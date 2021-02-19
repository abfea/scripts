#!/bin/python

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.EXPIRES_NEVER=2
Notify.init("showKeys")
test = Notify.Notification.new("hello world", "This is a test", "input-keyboard")
test.show()
