for i in alarm.service telegram_status.service
do
	sudo cp -rf $i /lib/systemd/system/$i
	sudo chmod 644 /lib/systemd/system/$i
	sudo systemctl daemon-reload
	sudo systemctl enable $i
	sudo systemctl restart $i
	sudo systemctl status $i
done
