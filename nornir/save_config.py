from nornir import InitNornir
from nornir.plugins.tasks.files import write_file
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.tasks.networking import napalm_get
from nornir.plugins.functions.text import print_result
from pprint import pprint
import datetime as dt
import pathlib


def collect_config(task):
    '''
    The purpose of this section is to create a local directory named config_backup.
    If it already exists, no harm will be done to the directory
    '''
    config_dir = "backup"
    entry_dir = config_dir + "/" + task.host.name
    pathlib.Path(config_dir).mkdir(exist_ok=True)
    pathlib.Path(entry_dir).mkdir(exist_ok=True)
    '''
    The purpose of this section is to an object containing the appropriate commands per host OS type
    This can be expanded upon for additional operating systems.
    We will use this set in the next section
    '''
    commands = {
        "junos": "show configuration",
        "eos": "show running-config",
        "ios": "show running-config",
    }
    '''
    Here we run the Nornir task to retrieve the configuration from our devices
    take note that the commands used are defined in the section above
    the platform assigned to the host (hosts.yaml --> groups.yaml) determines the command sent to it.
    '''
    out = task.run(
              task=netmiko_send_command,
              command_string=commands[task.host.platform]
    )
    '''
    This final task writes the output of the results into a dedicated, timestamped file.
    I have selected a `.conf` file extension since VScode knows to render that appropriately with pretty text coloring on the syntax
    '''
    task.run(
        task=write_file,
        content=out.result,
        filename=f"" + str(entry_dir) + "/" + str(dt.datetime.today().strftime('%Y-%m-%d-%H-%M')) + ".conf"
    )


def main():
    '''
    Quite simply speaking, this function's sole purpose is to instantiate Nornir as an object called `nr`.
    Note that we have a custom configuration file, we reference it upon the creation of `nr`.
    Finally, this function calls the task function of `collect_config`
    Magic ensues
    '''
    nr = InitNornir(config_file="config.yaml")
    nr.run(task=collect_config)


if __name__ == '__main__':
    main()