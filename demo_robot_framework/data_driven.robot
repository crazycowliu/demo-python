*** Settings ***
[Documentation]    Example test cases using the keyword-driven testing approach.
     
*** Variables ***
${var1}          1+2+3
@{list1}           a    b    c    ${var1}
&{dict1}          key1=sf   key2=${list1}
     
*** Test Cases ***
First Case
    Log to console    ${var1}    
    Log to console    ${list1}    
    Log to console    ${dict1}  
 
Second Case
    Calculate and Check Equals    ${var1}    ${6}
 
Third Case
    Calculate and Check Equals    ‘i’*3    iii

Fourth Case
    [Documentation]    data-driven case
    [Template]    Calculate "${expression}" and Check Equals "${expected}"
    2+4    ${6}
    9-2    ${7}
    6*4    ${24}

 
*** Keywords ***
Calculate and Check Equals
    [Arguments]    ${expression}    ${expected}
    ${res}=    Evaluate     ${expression}
    Should Be Equal    ${res}     ${expected}

Calculate "${expression}" and Check Equals "${expected}"
    Calculate and Check Equals    ${expression}    ${expected}

