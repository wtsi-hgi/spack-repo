# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhase1rmd(RPackage):
	"""Repeated Measurement Design for Phase I Clinical Trial

	Implements our Bayesian phase I repeated measurement design that accounts for multidimensional toxicity endpoints from multiple treatment cycles. The package also provides a novel design to account for both multidimensional toxicity endpoints and early-stage efficacy endpoints in the phase I design. For both designs, functions are provided to recommend the next dosage selection based on the data collected in the available patient cohorts and to simulate trial characteristics given design parameters. Yin, Jun, et al. (2017) <doi:10.1002/sim.7134>.
	"""
	
	cran = "phase1RMD" 

	version("1.0.9", md5="b0af281e20b5626da44de27994875904")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-arrayhelpers", type=("build", "run"))
