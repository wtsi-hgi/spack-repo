# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpduration(RPackage):
	"""Split-Population Duration (Cure) Regression

	An implementation of split-population duration regression models. 
    Unlike regular duration models, split-population duration models are
    mixture models that accommodate the presence of a sub-population that is 
    not at risk for failure, e.g. cancer patients who have been cured by 
    treatment. This package implements Weibull and Loglogistic forms for the 
    duration component, and focuses on data with time-varying covariates. 
    These models were originally formulated in Boag (1949) and Berkson and Gage 
    (1952), and extended in Schmidt and Witte (1989).
	"""
	
	homepage = "https://github.com/andybega/spduration"
	cran = "spduration" 

	version("0.17.2", md5="6feac6bac8c7e8a944fc4851cf94fd3a")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-separationplot", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
