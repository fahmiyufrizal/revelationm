# RVLM  simple launcher
# by fahmiyufrizal@2023

import os
import subprocess
from os import path
import asyncio

# parameters
version = 'v1.0'
titlewindow = 'fahmiyufrizal@2023 [github.com/fahmiyufrizal]'
RVLMFN = (r'RVLM_NetCafe_Launcher.exe')
RVLMLN = (r'RvlLauncher\rvlLauncher.exe')
#protection
if not path.exists (RVLMFN):
	print(" [x] Don't change filename!")
	async def display():
		await asyncio.sleep(5)
	asyncio.run(display())
	os._exit()
if not path.exists (RVLMLN):
	print(" [x] RvlLauncher\rvlLauncher.exe not found, Place inside Revelations Mobile folder!")
	async def display():
		await asyncio.sleep(5)
	asyncio.run(display())
	os._exit()
if not path.exists (RVLMLN_game):
	print(" [x] Complete the Installation first!")
	async def display():
		await asyncio.sleep(5)
	asyncio.run(display())
	os._exit()

#window_init
os.system('title ' + titlewindow)
print(" ")
print("      Revelations Mobile PC Global Netcafe Launcher       ")
print("              " + version)
print("        by fahmiyufrizal@2023        ")
print(" ")
print("[+] Initializing....")
print("[+] Importing module & config...")
