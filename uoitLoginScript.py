# $language = "Python"
# $interface ="1.0"
# This is a secureCRT Script to login to multiple devices into UOIT's networking lab
# Please be forgiving since secureCRT has terrible documentation. Many possibly
# useful lines are commented out for the sake of learning
#~~~~~~~~~~~~~~~~~~~~
# TODO: test this script! UOIT doesn't allow networking/IT students to log into
# the lab if they aren't in a intro/advanced networking course.


# initialTab not used but placed here since because of terrible API documentation for
#secureCRT
initialTab = crt.GetScriptTab()


def Main():

    try:
        crt.GetTabCount()
    except:
        crt.Dialog.MessageBox("Why no Tabs?", "Ok :")
        crt.quit()
    devRouter[1, 2, 3, 4]
    devSwitch[5, 6, 7, 8]
    for i in range(1, crt.GetTabCount() + 1):
        tab = crt.GetTab(i)
        tab.Screen.Synchronous = True

        if user or passwd == None:
            user = crt.Dialog.Prompt(
                "Enter UOIT Net LAB Username", "Log-in", "1005...", False)
            passwd = crt.Dialog.Prompt(
                "Enter UOIT Net LAB Password", "Log-in", "FUN", True)
        if selectedDevices == None:
            selectedDevices = crt.Dialog.Prompt(
                "List each desired devices number if multiple use SPACE to seperate", "Select Devices", "1 2 3 4 5 6", False)
        if devicelist == None:
            selectedDevices = selectdDevices.strip()
            devicelist = selectedDevices.split()

        # Login section
        # FIXME: fix the fact that I don't know how UOIT asks you to log in
        # tab.Screen.WaitForString("Login:")
        tab.Sleep(100)
        tab.Screen.Send(user + "\n")
        # tab.Screen.WaitForString("Password:")
        tab.Sleep(100)
        tab.Screen.Send(passwd + "\n")

        # selects the devicelist
        # FIXME: replace with wait4string dialog stated after login
        tab.Sleep(100)
        temptab.Screen.Send(devicelist(i - 1) + "\n")

        # get through that anonying cisco text on boot
        tab.Screen.WaitForString(
            "Would you like to enter the initial configuration dialog? [yes/no]:")
        tab.Screen.Send("no \n")
        tab.Sleep(100)
        tab.Screen.Send("\n")

        # checks if it is router/switch and waits for individual dialog
        if devicelist(i - 1) in devSwitch:
            tab.Screen.WaitForString("Switch>")
        elif devicelist(i - 1) in devRouter:
            tab.Screen.WaitForString("Router>")

        # gets into config t assumes no passwords are set
        tab.Screen.Send("enable \n")
        tab.Sleep(100)
        tab.Screen.Send("config t \n")

Main()

# Gets that little bit before the curser (if you want that type of thing)
"""def WaitForPrompt(command):
    row = crt.Screen.CurrentRow
    prompt = crt.Screen.Get(row, 0, row, crt.Screen.CurrentColumn - 1)
    prompt = prompt.strip()
    # executes commands
    # HERE
    #!!
    crt.Screen.WaitForString(prompt)
"""
