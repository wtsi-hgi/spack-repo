# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBspcov(RPackage):
	"""Bayesian Sparse Estimation of a Covariance Matrix

	Provides functions which perform Bayesian estimations of 
        a covariance matrix for multivariate normal data. Assumes that
        the covariance matrix is sparse or band matrix and positive-definite. 
        This software has been developed using funding supported by
        Basic Science Research Program through the National Research
        Foundation of Korea ('NRF') funded by the Ministry of Education
        ('RS-2023-00211979', 'NRF-2022R1A5A7033499', 'NRF-2020R1A4A1018207' 
        and 'NRF-2020R1C1C1A01013338').
	"""
	
	homepage = "https://github.com/statjs/bspcov"
	cran = "bspcov" 

	version("1.0.0", md5="fc676a5e931f7d785bd41225101d27a9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gigrvg", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-bayesfactor", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-cholwishart", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggmcmc", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-fincovregularization", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
