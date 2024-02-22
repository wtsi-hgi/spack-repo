# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBbl(RPackage):
	"""Boltzmann Bayes Learner

	Supervised learning using Boltzmann Bayes model inference, 
    which extends naive Bayes model to include interactions. Enables 
    classification of data into multiple response groups based on a large 
    number of discrete predictors that can take factor values of 
    heterogeneous levels. Either pseudo-likelihood or mean field 
    inference can be used with L2 regularization, cross-validation, and 
    prediction on new data. 
    <doi:10.18637/jss.v101.i05>.
	"""
	
	cran = "bbl" 

	version("1.0.0", md5="e02c228ebb7d2e1af624b6efa851f065")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
