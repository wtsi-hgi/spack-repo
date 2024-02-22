# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoolabc(RPackage):
	"""Approximate Bayesian Computation with Pooled Sequencing Data

	Provides functions to simulate Pool-seq data under models of
    demographic formation and to import Pool-seq data from real populations.
    Implements two ABC algorithms for performing parameter estimation and 
    model selection using Pool-seq data. Cross-validation can also be 
    performed to assess the accuracy of ABC estimates and model choice.
    Carvalho et al., (2022) <doi:10.1111/1755-0998.13834>.
	"""
	
	homepage = "https://github.com/joao-mcarvalho/poolABC"
	cran = "poolABC" 

	version("1.0.0", md5="fd9172f3084aa542154b7d41295e592c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-metricsweighted", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-poolhelper@1.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scrm", type=("build", "run"))
