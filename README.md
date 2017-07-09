# passwordGenerator
This project is licensed under the GNU General Public License. This generator creates a password of various lengths, with a minimum of 8 characters, and a maximum of 30 characters. This is designed to create random passwords invulnerable to brute force and dictionary attacks. This program will never repeat a password either. There are 2 fundemental styles, one of random characters, and one that generates relatively easy to remember xkcd-style passwords, found [here](https://xkcd.com/936/). This current version creates cryptographically random passwords, but get stored in an unprotected file. It is up to the user to manage how passwords are stored, however there is a dependance upon the file holding generated passwords. Later versions will incude a GUI and fix obvious security flaws.
