# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntrinsic(RPackage):
	"""Likelihood-Based Intrinsic Dimension Estimators

	Provides functions to estimate the intrinsic dimension of a dataset 
  via likelihood-based approaches. Specifically, the package implements the 
  'TWO-NN' and 'Gride' estimators and the 'Hidalgo' Bayesian mixture model. 
  In addition, the first reference contains an extended vignette on the usage of 
  the 'TWO-NN' and 'Hidalgo' models. References: 
    Denti (2023, <doi:10.18637/jss.v106.i09>); 
    Allegra et al. (2020, <doi:10.1038/s41598-020-72222-0>); 
    Denti et al. (2022, <doi:10.1038/s41598-022-20991-1>);
    Facco et al. (2017, <doi:10.1038/s41598-017-11873-y>); 
    Santos-Fernandez et al. (2021, <doi:10.1038/s41598-022-20991-1>).
	"""
	
	homepage = "https://github.com/Fradenti/intRinsic"
	cran = "intRinsic" 

	version("1.0.2", md5="89a04bc3c99d4cbe504e4989be01e221")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-salso", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
