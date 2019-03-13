# PizzaPy
A script to automatically select a pizza from dominos for delivery and bring you to the checkout page

<br>
<p>This project was written as a final project assignment for CS 41 at Stanford. The script depends on the Selenium and time modules in python, as well as having the chrome driver set up to use the webdriver portion of selenium. I have included my chrome driver file, but if issues arise, please refer to google's page and download the driver yourself for best compatibility. Link <a href = "http://chromedriver.chromium.org/downloads">here</a>. </p>

<br>
<p>This script was written on Mac OS 10.14 Mojave and has only been tested on this in python 3.7. You must have this version of python with the selenium package installed for the script to work properly. Once the selenium package and proper chrome driver is installed, the script should be as easy as opening the terminal and running the script.</p>

<br>

<p> As a first step, you should enter your address into the script file in the appropriate format so that the script can locate a proper store for delivery. If no store exists, the program will most likely crash. This was not tested.</p>

<br>

<p> I chose not to allow the script to check out completely for a couple of reasons. First being i have no security experience, and do not want to write code that deals with that sensitive information yet. Second, i couldnt get the selenium package to easily interact with the payment fields on the site and am leaving it for later personal updating. Feel free to add this funtionality yourself if you want, but i am not responsible for your personal payment information.</p>

<br>
<h1>Instructions</h1>
<ol>
  <li>Download proper chrome driver from the link</li>
  <li>Download the pizza.py script</li>
  <li>Install Selenium through pip</li>
  <li>Place chrome driver in same directory as the script</li>
  <li>Run script with "python3 pizza.py"</li>
</ol>


<h3>Contact info</h3>
<p> If you want to contact me about this project to commit changes or anything, or just to reach out my email is tnollman@stanford.edu</p>
