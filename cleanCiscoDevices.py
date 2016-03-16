# $language = "Python"
# $interface ="1.0"
# This is a secureCRT Script to login to multiple devices into UOIT's networking lab
# Please be forgiving since secureCRT has terrible documentation. Many possibly
# useful lines are commented out for the sake of learning
#~~~~~~~~~~~~~~~~~~~~
# TODO: TEST THIS SCRIPT! UOIT doesn't allow networking/IT students to log into
# the lab if they aren't in a intro/advanced networking course.


def Main():
    try:
        crt.GetTabCount()
    except:
        crt.Dialog.MessageBox("Why No Tabs?", "Ok :")
        return
    response = crt.Dialog.MessageBox(
        "Are you sure you want to erase starup-config and reload ALL  TABS?", "Erase/Reload All Tabs - Confirm", BUTTON_YESNO)
        if response != IDYES:
            return
    for i in range(1, crt.GetTabCount() + 1):
        tab = crt.GetTab(i)
        tab.Screen.Synchronous = True

        tab.Screen.Send("end /n")
        tab.Sleep(200)

        tab.Screen.WaitForString(
            "Erasing the nvram filesystem will remove all configuration files! Continue? [confirm]")
        tab.Screen.Send("\n")
        tab.Screen.WaitForString("Erase of nvram: complete")
        tab.Screen.Send("\n")
        tab.Screen.Send("reload \n")
        tab.Screen.WaitForString("System configuration has been modified. Save? [yes/no]:")
        tab.Screen.Send("no \n")
        tab.Screen.WaitForString("Proceed with reload? [confirm]")
        tab.Screen.Send("\n")

    crt.Quit  # mayquit securityCRT not sure 😕
Main()
