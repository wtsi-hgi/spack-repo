# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBmstdr(RPackage):
	"""Bayesian Modeling of Spatio-Temporal Data with R

	Fits, validates and compares a number of Bayesian models for
    spatial and space time point referenced and areal unit data. Model fitting
    is done using several packages: 'rstan', 'INLA', 'spBayes', 'spTimer',
    'spTDyn', 'CARBayes' and 'CARBayesST'. Model comparison is performed using
    the DIC and WAIC,  and K-fold cross-validation where the user is free
    to select their own subset of data rows for validation. Sahu (2022)
    <doi:10.1201/9780429318443> describes the methods in detail.
	"""
	
	homepage = "https://www.sujitsahu.com"
	cran = "bmstdr" 

	version("0.7.9", md5="8dae0965881a3e1e1cda454ccd40218a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-sptimer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "run"))
	depends_on("r-spbayes", type=("build", "run"))
	depends_on("r-carbayes", type=("build", "run"))
	depends_on("r-carbayesst", type=("build", "run"))
	depends_on("r-sptdyn", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-inlabru", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
