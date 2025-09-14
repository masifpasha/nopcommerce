*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Wait Example
    Open Browser    https://www.example.com    edge
    Sleep    10s
    Close Browser
