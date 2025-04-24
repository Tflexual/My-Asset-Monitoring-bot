#from fetch_data import fetch_data
#from anomaly_checker import check_anomalies
#from alert_sender import send_alert

#def main():
   # data = fetch_data()
  #  anomalies = check_anomalies(data)
 #   send_alert(anomalies)

#if __name__ == "__main__":
  #  main()


#from fetch_data import fetch_data
#from anomaly_checker import check_anomalies
#from alert_sender import send_alert

#def main():
 #   print("Fetching data...")  # Debugging print
  #  data = fetch_data()

   # print("Checking for anomalies...")  # Debugging print
    #anomalies = check_anomalies(data)
    #print(f"Anomalies detected: {anomalies}")  # Debugging print

    #print("Sending alerts...")  # Debugging print
    #send_alert(anomalies)



#if __name__ == "__main__":
 #   main()




from fetch_data import fetch_data
from anomaly_checker import check_anomalies
from alert_sender import send_alert, send_email,log_alerts_to_csv

def main():
    print("Fetching data...")
    data = fetch_data()
    print(f"Data fetched: {data}")

    print("Checking for anomalies...")
    anomalies = check_anomalies(data)
    print(f"Anomalies detected: {anomalies}")

    if anomalies:
        print("Sending alerts...")
        send_alert(anomalies)
        send_email(anomalies)  # Send email alerts
        log_alerts_to_csv(anomalies)  # Log alerts to CSV

if __name__ == "__main__":
    main()
