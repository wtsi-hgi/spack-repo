# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdinalbayes(RPackage):
	"""Bayesian Ordinal Regression for High-Dimensional Data

	Provides a function for fitting various penalized Bayesian
    cumulative link ordinal response models when the number of parameters
    exceeds the sample size. These models have been described in 
    Zhang and Archer (2021) <doi:10.1186/s12859-021-04432-w>.
	"""
	
	homepage = "https://github.com/kelliejarcher/ordinalbayes"
	cran = "ordinalbayes" 

	version("0.1.1", md5="22b5a2e5342d339e6cf2554f00a9ac1a")

	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-dclone", type=("build", "run"))
	depends_on("r-runjags", type=("build", "run"))
	depends_on("jags@4.0.0:", type=("build", "link", "run"))
