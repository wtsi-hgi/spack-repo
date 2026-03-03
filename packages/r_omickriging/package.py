# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmickriging(RPackage):
	"""Poly-Omic Prediction of Complex TRaits

	It provides functions to generate a correlation matrix
    from a genetic dataset and to use this matrix to predict the phenotype of an
    individual by using the phenotypes of the remaining individuals through
    kriging. Kriging is a geostatistical method for optimal prediction or best
    unbiased linear prediction. It consists of predicting the value of a
    variable at an unobserved location as a weighted sum of the variable at
    observed locations. Intuitively, it works as a reverse linear regression:
    instead of computing correlation (univariate regression coefficients are
    simply scaled correlation) between a dependent variable Y and independent
    variables X, it uses known correlation between X and Y to predict Y.
	"""
	
	cran = "OmicKriging" 

	version("1.4.0", md5="301f9cbe500a3542c5ddeb2598e412e7")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
