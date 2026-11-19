---
name: Bug Report for BillLists.html and billing.py
about: Report a software defect or unexpected behavior
title: "[BILL BUGS] "
labels: bug, bill
assignees: ""
---
• ## Bug Description: Duplicate lines caused crash in browser.
• ## Steps to Reproduce: in BillLists creating duplicate lines for cases 1 and 2 caused the browser to report any errors.
• ## Expected vs. Actual Behavior: If everything goes as expected, no error messages should appear in the browser. Sadly, the error messages were the first thing I saw when I opened the browser with the live server extension via VS Code.
• ## Risk & Severity Assessment: - [X] Low. Easily fixable via indentations corrected in billing.py
• ## Environment & Browser: 46-51 and 56-61 in BillsList.html.
