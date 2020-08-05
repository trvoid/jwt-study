@echo off

@set CLASSPATH=.\commons-codec-1.14\commons-codec-1.14.jar;%CLASSPATH%

@set HEADER_FILE=header.json
@set PAYLOAD_FILE=payload.json
@set SECRET=my-secret

java -cp %CLASSPATH% JwtTokenCreator %HEADER_FILE% %PAYLOAD_FILE% %SECRET%
