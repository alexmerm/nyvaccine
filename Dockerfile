FROM python:3.8


#Install Cron
RUN apt-get -y update && apt-get -y install cron

#Install Python Requiremnts
WORKDIR /home

COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/covid-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/covid-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

#Copy code
COPY nystatechecker.py .
RUN chmod +x nystatechecker.py
COPY nychecker.sh .
RUN chmod +x nychecker.sh


# Run the command on container startup
CMD cron && tail -f /var/log/cron.log
#CMD /home/nystatechecker.py