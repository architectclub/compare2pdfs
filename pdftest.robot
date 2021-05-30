*** Settings ***
Library   pdflib.py

*** Variables ***
${PDF_PATH}=    sample1.pdf
${PDF_PATH2}=    sample2.pdf

*** Test Cases ***
Log Number Of Pages In Pdf File
    ${pages_count}=    Get Number Of Pages In Pdf    ${PDF_PATH}
    Log    ${pages_count}

Log Specific Page Text From Pdf File
    ${pdf_text}=    Get Specific Page Text In Pdf    ${PDF_PATH}   2
    Log    ${pdf_text}

Log Entire Pdf File Text
    ${pdf_text1}=    Get Entire Pdf Text    ${PDF_PATH}
    Log    ${pdf_text1}
    ${pdf_text2}=    Get Entire Pdf Text    ${PDF_PATH2}
    Log    ${pdf_text2}
    Should Be Equal    ${pdf_text1}    ${PDF_PATH2}

# Log Pdf Info
    # ${pdf_info}=    Get Pdf Info    ${PDF_PATH}
    # Log    ${pdf_info}
