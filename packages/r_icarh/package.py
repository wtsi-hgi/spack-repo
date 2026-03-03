# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcarh(RPackage):
	"""Integrative Conditional Autoregressive Horseshoe Model

	Implements the integrative conditional autoregressive horseshoe model 
    discussed in Jendoubi, T., Ebbels, T.M. Integrative analysis of time course metabolic data and biomarker discovery. 
    BMC Bioinformatics 21, 11 (2020) <doi:10.1186/s12859-019-3333-0>.
    The model consists in three levels: Metabolic pathways level modeling interdependencies between
    variables via a conditional auto-regressive (CAR) component, integrative analysis level to identify
    potential associations between heterogeneous omic variables via a Horseshoe prior and experimental
    design level to capture experimental design conditions through a mixed-effects model.
    The package also provides functions to simulate data from the model, construct pathway matrices,
    post process and plot model parameters.
	"""
	
	cran = "iCARH" 

	version("2.0.2.1", md5="ab56d96ada1bedaa9a045f5a0bc1a6ce")

	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-kegggraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-mc2d", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
