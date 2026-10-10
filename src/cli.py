import runpx

to_print = [
    "      _______      ",
    "     /       \\    ",
    ",-----------------,",
    "|                 |",
    "| ###    #    ### |",
    "| #      #     #  |",
    "| #      #     #  |",
    "| ###    ###  ### |",
    "|                 |",
    "'-----------------'",
    "\n",
    "PortexCLI v1.0 - Run PortexJSON executables"
]

for i in to_print:
    print(i)

cmd_inp = input("> ")

if cmd_inp == "run":
    arg1_inp = input("PortexJSON array? > ")

