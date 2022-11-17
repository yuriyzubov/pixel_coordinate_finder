# pixel_coordinate_finder
This web service calculates pixel coordinate values for an image
given the dimensions of the image and the corner points of the image as it is to be displayed.


To run the web service locally, please install *docker*, build and run the docker container. 

1. Install docker: https://docs.docker.com/get-docker/


2. In a terminal, switch to the pixel_coordinate_finder directory:
    ```
   cd PATH_TO_DIRECTORY/pixel_coordinate_finder
   ```
   
4. Build docker file:
   ```
   docker build -t pixel-finder . 
   ```
   
5. Run docker container:
   ```
   docker run -p 5000:5000 pixel-finder
   ```
6. Open http://127.0.0.1:5000/input, in your web browser, 
  enter dimensions and corner coordinates, and submit form data
7. The pixel grid array should be displayed on http://127.0.0.1:5000/calculate
   1. If dimensions were not entered correctly the result message would be:
   ```
   Rectangle dimensions are incorrect
   ```
   2. If entered list of coordinates does not form a rectangle:
   ```
   Points do not form a rectangle
   ```
