@echo off

@set CLASSPATH=.\commons-codec-1.14\commons-codec-1.14.jar;%CLASSPATH%

@set TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmdW4td2l0aC1qd3RzIiwic3ViIjoiQXp1cmVEaWFtb25kIiwianRpIjoiZjZjMTA5N2YtY2M0OC00OTQ5LWE2MjctOGI5NGZjNWUzN2JhIiwiaWF0IjoxNTk2MTg1MDAxLCJleHAiOjE1OTYxODUwNjF9.UXvXY97CNcHv7LobrBagePBPeGiW2F-Z-nuINSmUy5k
@set SECRET=my-secret

java -cp %CLASSPATH% JwtTokenValidator %TOKEN% %SECRET%
