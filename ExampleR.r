# Prototype
require(osfr)

?read.osf
# read.osf {osfr}    R Documentation
# Read osf file
# 
# Description
# 
# Create a data.frame from a file on the OSF

dat <- read.osf("osf.io/api/v1/project/5ctke/osffiles/this.csv/version/1/")

head(dat)

# > head(dat)
# A B C D
# 1 1 2 3 4
# 2 2 3 4 5
# 3 3 4 5 6
# 4 4 5 6 7
# 5 5 6 7 8
# 6 6 7 8 9


Fabian's edits

Adding new line


Editing my example file