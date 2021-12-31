# What is this for?

This folder should be used to store configuration files used by Kedro or by separate tools.

This file can be used to provide users with instructions for how to reproduce local configuration with their own credentials. You can edit the file however you like, but you may wish to retain the information below and add your own section in the [Instructions](#Instructions) section.

## Local configuration

The `local` folder should be used for configuration that is either user-specific (e.g. IDE configuration) or protected (e.g. security keys).

> *Note:* Please do not check in any local configuration to version control.

## Base configuration

The `base` folder is for shared configuration, such as non-sensitive and project-related configuration that may be shared across team members.

WARNING: Please do not put access credentials in the base configuration folder.

## Instructions





## Find out more
You can find out more about configuration from the [user guide documentation](https://kedro.readthedocs.io/en/stable/04_user_guide/03_configuration.html).

 install kedro mac
 chmod +x ./Miniconda3-latest-MacOSX-arm64.sh
 ./Miniconda3-latest-MacOSX-arm64.sh
 conda create python=3.8 --name kedro
 conda activate kedro
 pip install kedro==0.17.1
 pip install jupyter
 pip install kedro-viz
 git clone https://github.com/walmartdigital/de-challenge.git
 git checkout -b daniel
 mkdir kedro
 cd kedro
 kedro new walmart
 cd walmart
 kedro pipeline create data_engineer 