# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamba(RPackage):
	"""Selection and Misclassification Bias Adjustment for Logistic
Regression Models

	
    Health research using data from electronic health records (EHR) has gained
    popularity, but misclassification of EHR-derived disease status and lack of
    representativeness of the study sample can result in substantial bias in
    effect estimates and can impact power and type I error for association
    tests. Here, the assumed target of inference is the relationship between
    binary disease status and predictors modeled using a logistic regression
    model. 'SAMBA' implements several methods for obtaining bias-corrected
    point estimates along with valid standard errors as proposed in Beesley and
    Mukherjee (2020) <doi:10.1101/2019.12.26.19015859>, currently under review.
	"""
	
	cran = "SAMBA" 

	version("0.9.0", md5="adbbec426190b42dba7f6e66b44c413d")

	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
