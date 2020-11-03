# python-rpm-server
Simple web server using Python to serve RPM files for custom RPM repo

# Docker Build
docker build -t python-rpm-server:yourtaghere .

# Docker run
docker run --rm --name SuperDuperPythonRPMServer -v /Path/To/Your/Files:/web/files -p 80:80 -it python-rpm-server:yourtaghere
