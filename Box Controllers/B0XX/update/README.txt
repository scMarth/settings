Check to make sure you are using the right updater for the B0XX. On the back sticker it should say B0XX-R2 (mine is R2, yours may be different)

If you have trouble running the updater:

	The application was unable to start correctly (0xc000007b).
	Click OK to close the application.

Install latest version of Arduino IDE and copy all files from

C:\Program Files (x86)\Arduino\hardware\tools\avr\bin

into:

B0XXUpdater_V3\B0XXUpdater\avrdude511

overwrite everything. And it worked for me. I have no idea which of these files is the pre-requisite for avrdude to work. But w/e it works lol
Install Arduino IDE: https://www.arduino.cc/en/Main/software