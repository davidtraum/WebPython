 # WebPython
 
 ## About
 WebPython is a lightweight python3 http server that executes python scripts and returns the result as a html page.
 It can be used standalone or as a proxy behind a nginx server.
 
 ## Setup
 1. Clone the git repository to a location you want using **git clone https://github.com/davidtraum/WebPython**
 2. Edit the config.json file and insert the base path of your webserver under **base_directory** You can also specify a port and more here.
 3. Run the server using **python3 web_python.py**
 4. If you want to autostart the server you could, for example, add the command to your **/etc/rc.local** file.
 5. Test your server by adding a python file that prints something to your webserver directory and open the url in your browser    like http://myserver/test.py
 6. Optional: If you want to use the server as a **nginx proxy** have a look at the example configuration included in the repository.
