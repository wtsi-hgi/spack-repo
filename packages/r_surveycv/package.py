# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurveycv(RPackage):
	"""Cross Validation Based on Survey Design

	Functions to generate K-fold cross validation (CV) folds
    and CV test error estimates that take into account
    how a survey dataset's sampling design was constructed
    (SRS, clustering, stratification, and/or unequal sampling weights).
    You can input linear and logistic regression models, along with data and a 
    type of survey design in order to get an output that can help you determine
    which model best fits the data using K-fold cross validation.
    Our paper on "K-Fold Cross-Validation for Complex Sample Surveys"
    by Wieczorek, Guerin, and McMahon (2022)
    <doi:10.1002/sta4.454>
    explains why differing how we take folds based on survey design is useful.
	"""
	
	homepage = "https://github.com/ColbyStatSvyRsch/surveyCV/"
	cran = "surveyCV" 

	version("0.2.0", md5="35b2323596464cf969193888349f30d4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-survey@4.1:", type=("build", "run"))
	depends_on("r-magrittr@2:", type=("build", "run"))
