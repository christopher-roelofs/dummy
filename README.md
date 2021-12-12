# dummy
Quick and dirty voice command

* Owner and self can be customized in config.json
* Activation phrases can be customized. These are used to get it to listen.
* Activation responses can be customzed and a random one will be chosen.
* Voice can be customzed. 1 for female and 0 for male
* Subscriptions are used to set which providers you are subscribed to. The only ones are jokes and stop.

Actions are setup in the actions.json file. These are words that will be used to trigger the action. The spoken phrase is split up and then checked against each action. If the number of words in the phrase that match the action string are over the processor threshold then the action will trigger. The threashold can be set in the processor.

The basic concepts are here and it's pretty flixible. The string matching is probbaly fragile but seems to work ok?
