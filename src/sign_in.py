#RC 1st, managing the finance pop up app

#Create main loop/class

    #Pull all needed values and create the main buttins inside of __init__

    #Log in button
        # Create a new top-level window
            #Keep popup on top

        #Create a Header Label

        #Put into loop
            #Text Input (Name)

            #Number Input (password)

            #Save Button
                #If the values check out, then go back to the main pop up and pull from the file
                #Else print that some of the information is wrong

        # Retrieve the values from inputs using .get()
    #Sign up button
        # Create a new top-level window
            #Keep popup on top

        #Create a Header Label

        #Put into loop
            #Text Input (Name)

            #Number Input (password)

            #Save Button
                #If there are inputs and the usernames don't match, create the account and open it up
    #Exit button
        #If they click it do .done() to close everything and sign them out.

    #Return whatever they use to sign in or sign up

    #Afterward use .clear()