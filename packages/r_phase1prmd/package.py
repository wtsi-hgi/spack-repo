# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhase1prmd(RPackage):
	"""Personalized Repeated Measurement Design for Phase I Clinical
Trials

	Implements Bayesian phase I repeated measurement design that 
    accounts for multidimensional toxicity endpoints and longitudinal efficacy 
    measure from multiple treatment cycles. The package provides flags to 
    fit a variety of model-based phase I design, including 1 stage models with
    or without individualized dose modification, 3-stage models with or without
    individualized dose modification, etc. Functions are provided to recommend 
    dosage selection based on the data collected in the available patient cohorts 
    and to simulate trial characteristics given design parameters. 
    Yin, Jun, et al. (2017) <doi:10.1002/sim.7134>. 
	"""
	
	cran = "phase1PRMD" 

	version("1.0.2", md5="c978fad0db9447d7906adb91479c047d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-coda@0.13:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-arrayhelpers", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
