<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <header>
        <h1>IoT Assignment 3</h1>
    </header>
    
  <section>
      <h2>By</h2>
      <p>Neeraj Patil</p>
      
  </section>
  
  <section>
      <h2>Overview</h2>
      <p>This involves setting up a simulated IoT environment using ESP32 with MicroPython on Wokwi and publishing sensor data to ThingSpeak. The simulation includes virtual sensors for monitoring temperature, humidity, and CO2 levels.</p>
  </section>
    <section>
      <h2>Description</h2>
      <p>Build a cloud-based IoT system which collects data from a set of virtual sensors that are
deployed to collect environmental information using the MQTT protocol.
Display the latest sensor data values received from all the sensors of a specified environmental
station.
Display the sensor data values received during the last five hours from all environmental station
of a specified sensor</p>
  </section>
  <section>
      <h2>Pre-requisites</h2>
      <ul>
          <li>Wokwi account for ESP32 simulation.</li>
          <li>ThingSpeak account for data visualization.</li>
      </ul>
  </section>
  
  <section>
      <h2>Setup Instructions</h2>
      <h3>1. Wokwi Setup</h3>
      <ol>
          <li>Sign up or log in to Wokwi.</li>
          <li>Create a new ESP32 MicroPython project.</li>
          <li>Include a DHT22 sensor and LEDs in your diagram if needed.</li>
      </ol>

  <h3>2. ThingSpeak Channel Creation</h3>
  <ol>
      <li>Log into ThingSpeak and create a new channel.</li>
      <li>Add fields for Temperature, Humidity, and CO2.</li>
      <li>Note down the channel ID and other credentials.</li>
  </ol>

  <h3>3. MQTT Configuration</h3>
  <p>Use Python to configure MQTT clients and ensure proper authentication using the umqtt library.
</p>

  <h3>4. Code Configuration</h3>
  <p>Insert your ThingSpeak and Wi-Fi credentials into the provided code.Update the WiFi with your current Wi-Fi credentials. Since we are using wokwi, it creates a virtual WiFi access point called Wokwi-GUEST. It is an open access point, thus no password is necessary.</p>


  <h3>5. Simulation Execution</h3>
  <p>Paste the code into Wokwi's editor and run it. The code will simulate temperature, humidity, and CO2 readings, and publish this data to the ThingSpeak.</p>

  <h3>6. ThingSpeak Visualization</h3>
  <p>You should see the published data visualized in the corresponding fields.
Use ThingSpeak's analytics tools to process and visualize the data as needed. For reference, see the output image which i have provided.
</p>
  </section>
  
</body>
</html>
