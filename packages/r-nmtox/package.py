# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmtox(RPackage):
	"""Dose-Response Relationship Analysis of Nanomaterial Toxicity

	Perform an exploration and a preliminary analysis on the dose-
    response relationship of nanomaterial toxicity. Several functions are
    provided for data exploration, including functions for creating a subset of
    dataset, frequency tables and plots. Inference for order restricted dose-
    response data is performed by testing the significance of monotonic
    dose-response relationship, using Williams, Marcus, M, Modified M and 
    Likelihood ratio tests. Several methods of multiplicity adjustment 
    are also provided. Description of the methods can be found in <https://github.com/rahmasarina/dose-response-analysis/blob/main/Methodology.pdf>.
	"""
	
	cran = "NMTox" 

	version("0.1.0", md5="92c9956066e486c35831057ba976436d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-iso", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
