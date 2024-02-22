# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCountstar(RPackage):
	"""Flexible Modeling of Count Data

	For Bayesian and classical inference and prediction with count-valued data,
    Simultaneous Transformation and Rounding (STAR) Models provide a flexible, interpretable,
    and easy-to-use approach. STAR models the observed count data using a rounded 
    continuous data model and incorporates a transformation for greater flexibility.
    Implicitly, STAR formalizes the commonly-applied yet incoherent procedure of 
    (i) transforming count-valued data and subsequently 
    (ii) modeling the transformed data using Gaussian models. 
    STAR is well-defined for count-valued data, which is reflected in predictive accuracy, 
    and is designed to account for zero-inflation, bounded or censored data, and over- or underdispersion. 
    Importantly, STAR is easy to combine with existing MCMC or point estimation
    methods for continuous data, which allows seamless adaptation of continuous data
    models (such as linear regressions, additive models, BART, random forests,
    and gradient boosting machines) for count-valued data. The package also includes several
    methods for modeling count time series data, namely via warped Dynamic Linear Models. 
    For more details and background on these methodologies, see the works of 
    Kowal and Canale (2020) <doi:10.1214/20-EJS1707>, 
    Kowal and Wu (2022) <doi:10.1111/biom.13617>, 
    King and Kowal (2022) <arXiv:2110.14790>, and 
    Kowal and Wu (2023) <arXiv:2110.12316>.
	"""
	
	homepage = "https://bking124.github.io/countSTAR/"
	cran = "countSTAR" 

	version("1.0.2", md5="9cac79f02bab339173be4b34e8d3b01c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-dbarts", type=("build", "run"))
	depends_on("r-fastgp", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-spikeslabgam", type=("build", "run"))
	depends_on("r-splines2", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-truncatednormal", type=("build", "run"))
	depends_on("r-truncdist", type=("build", "run"))
	depends_on("r-kfas", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
