def iOS(deeplink: str): 
    x =  '''
    function openURL(url) {
	    const UIApplication = ObjC.classes.UIApplication.sharedApplication()
	    const toOpen = ObjC.classes.NSURL.URLWithString_(url)
	    return UIApplication.openURL_(toOpen)
    }
 	openURL("%s")''' % (deeplink.replace("\n", ""))
    return x