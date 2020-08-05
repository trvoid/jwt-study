@echo off

@set CLASSPATH=.\commons-codec-1.14\commons-codec-1.14.jar;%CLASSPATH%

javac -cp %CLASSPATH% JwtTokenValidator.java