# Phone Recommendation System
## Description
A simple Prolog based system to recommend phones to end users based on a few rules constructed by the 

## Utilized Environment
* Python 3.11
### Packages
* Latest pyswip version
* Latest Pandas version
* re
* os

## Instructions
To run the application, simply execute `python3 main.py` from within the repository directory. You may need to install some of the utilized packages if your local python environment does not have them.

##Notes
* The Prolog database has standardized units for comparison and matching within the rules. Those units are:
    * Inches for dimensions (length, height, width)
    * Gigahertz for CPU speeds
    * Gigabytes for storage and RAM values.

## Future Scope
* Additional rules and facts for finer tuning
* Expand phone dataset and update to more current data with scraping technology or other database
* Investigate "in-Prolog" sorting; currently handled by Python
* Proper user interface
