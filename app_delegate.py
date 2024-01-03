import objc
from AppKit import NSApplicationDelegate
from Foundation import NSObject

class AppDelegate(NSObject):
    def applicationSupportsSecureRestorableState_(self, application):
        return True

# from Cocoa import NSObject, NSApplicationDelegate

class AppDelegate(NSObject, NSApplicationDelegate):
    def applicationSupportsSecureRestorableState_(self, application):
        return True
