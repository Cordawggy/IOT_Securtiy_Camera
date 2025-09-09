# IOT_SECURITY_CAMERA 

### This is a cloned repository of a group project for Cambrian Colleges Internet of Things - Computer Programming course.

### This project is a secure surveillance system, comprising multiple cameras with anti-tampering measures.
These features will include sensors attached to the cameras to detect any physical tampering such as shock, temperature and motion sensors, and software which will detect if the camera lenses are disrupted in any way (ex. paint, cloth). The system will log relevent events as time-series data in an InfluxDB database, will comprise a dashboard using home assistant modules from Azure, will send alerts to mobile devices when the camera detects motion during customizable specified times or any tampering events are triggered, and may include a physical alarm depending on the clients wishes.

### Database Selection
Our surveillance system will utilize the rust-based InfluxDB as our time-series database model of choice, and will integrate the Python-based home-assistant modules from Azure.

### Networking Aspect

Some End-to-end encryption for the camera will be up and working to ensure the protection of the video stream, we will have it linked and working on a private and safe network with good connection. Network Protocols, Connectivity, Security, Bandwidth and Compression, Storage and Streaming, Monitoring and Maintenance will all be covered. 
