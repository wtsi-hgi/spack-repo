# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcbiomark(RPackage):
	"""Data-Driven Design of Targeted Gene Panels for Estimating
Immunotherapy Biomarkers

	Implementation of the methodology proposed in 'Data-driven design of targeted gene panels for estimating immunotherapy biomarkers', Bradley and Cannings (2021) <arXiv:2102.04296>. This package allows the user to fit generative models of mutation from an annotated mutation dataset, and then further to produce tunable linear estimators of exome-wide biomarkers. It also contains functions to simulate mutation annotated format (MAF) data, as well as to analyse the output and performance of models.
	"""
	
	cran = "ICBioMark" 

	version("0.1.4", md5="b5b8fc6135d552b6e8dc5ba16f611ca2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gglasso", type=("build", "run"))
	depends_on("r-prroc", type=("build", "run"))
