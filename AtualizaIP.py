import requests
import config
import PySimpleGUI as sg
import json
import os

def updateIpAddress(IP_ADDRESS):
	URL = "https://api.cloudflare.com/client/v4/zones/" + config.ZONE_ID + "/dns_records/" + config.DNS_ID
	HEADERS = { 'Authorization': 'Bearer ' + config.API_TOKEN, 'Content-Type': 'application/json' }
	DATA = '{ "content": "%s", "name": "%s", "proxied": false, "type":"A" }' % (IP_ADDRESS, config.DNS_NAME)

	# making a PUT request
	res = requests.put(URL, headers=HEADERS, data=DATA )

	# return if request as okay or not (Boolean)
	return res.ok

def getCloudflareIpAdrress():
	URL = "https://api.cloudflare.com/client/v4/zones/" + config.ZONE_ID + "/dns_records/" + config.DNS_ID
	HEADERS = { 'Authorization': 'Bearer ' + config.API_TOKEN, 'Content-Type': 'application/json' }
	res = requests.get(URL, headers=HEADERS)
	res = json.loads(res.text)
	return res['result']['content']

def getPublicIpAddress():
	return requests.get('https://checkip.amazonaws.com').text.strip()

def interface():
	path = os.path.abspath(os.getcwd())
	icon = "%s\\icon.ico" % (path)

	new_theme = {"BACKGROUND": '#f9f9f9', "TEXT": sg.COLOR_SYSTEM_DEFAULT, "INPUT": sg.COLOR_SYSTEM_DEFAULT,
			"TEXT_INPUT": sg.COLOR_SYSTEM_DEFAULT, "SCROLL": sg.COLOR_SYSTEM_DEFAULT,
			"BUTTON": sg.OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR, "PROGRESS": sg.COLOR_SYSTEM_DEFAULT, "BORDER": 1,
			"SLIDER_DEPTH": 1, "PROGRESS_DEPTH": 0
	}
	sg.theme_add_new('MyTheme', new_theme)
	sg.theme('MyTheme')
	
	column_to_be_centered  = [
		[sg.Text("DNS: " + config.DNS_NAME)], 
		[sg.Text("IP ATUAL: " + getCloudflareIpAdrress())], 
		[sg.Text("IP PUBLICO: " + getPublicIpAddress())], 
		[sg.Button("ATUALIZAR"), sg.Button("SAIR")]
	]
	
	layout = [[sg.VPush()],
			[sg.Push(), sg.Column(column_to_be_centered,element_justification='c'), sg.Push()],
			[sg.VPush()]]

	# create window
	window = sg.Window("Atualiza IP", layout, size=(400,200), icon=icon, finalize=True)

	# create an event loop
	while True:
		event, values = window.read()
		if event == "ATUALIZAR":
			ipAddress = getPublicIpAddress()
			requestStatus = updateIpAddress(ipAddress)
			if requestStatus:
				sg.popup('Atualizado com sucesso!!!', icon=icon)
			else:
				sg.popup('Erro!!!', icon=icon)

		if event == 'SAIR' or event == sg.WIN_CLOSED:
			break

def main():
	interface()

if __name__ == '__main__':
	main()