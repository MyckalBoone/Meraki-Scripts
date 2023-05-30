#! /usr/bin/env python

from meraki_sdk.meraki_sdk_client import MerakiSdkClient


# Cisco Devnet Sandbox Meraki API key

X_CISCO_MERAKI_API_KEY = 'Enter API KEY HERE -> 12jujnk344k654k53jk34'


# Establish a new client connection to the Meraki REST API

MERAKI = MerakiSdkClient(X_CISCO_MERAKI_API_KEY)


# Get a list of all the organizations for the Cisco Devnet account

ORGS = MERAKI.organizations.get_organizations()
for ORG in ORGS:
    print("Org ID: {} and Org Name: {}".format(ORG['ID'], ORG['name']))

# Query one of the organizations specifically

PARAMS = {}
PARAMS["organization_id"] = "1322848"

# Get a list of all the networks for the specific organization above
NETS = MERAKI.networks.get_organization_networks(PARAMS)
for NET in NETS:
    print("Network ID: {0:20s}, Name: {1:45s},Tags: {2:<10s}".format(\ NET['ID'], NET['name'], str(NET['tags'])))


# Get a list of all the devices that are a part of the Always on network
DEVICES = MERAKI.devices.get_network_devices("Enter device here -> L_22343534453452")
for DEVICE in DEVICES:
    print("Device Model: {0:9s},Serial: {1:14s},MAC: {2:17},Firmware: {3:12s}"\.format([DEVICE['model'], DEVICE['serial'], DEVICE['mac'], \ DEVICE['firmware']))


