# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmctreer(RPackage):
	"""Prepare MCMCtree Analyses and Plot Bayesian Divergence Time
Analyses Estimates on Trees

	Provides functions to prepare time priors for 'MCMCtree' analyses in the 'PAML' software from Yang (2007)<doi:10.1093/molbev/msm088> and plot time-scaled phylogenies from any Bayesian divergence time analysis. Most time-calibrated node prior distributions require user-specified parameters. The package provides functions to refine these parameters, so that the resulting prior distributions accurately reflect confidence in known, usually fossil, time information. These functions also enable users to visualise distributions and write 'MCMCtree' ready input files. Additionally, the package supplies flexible functions to visualise age uncertainty on a plotted tree with using node bars, using branch widths proportional to the age uncertainty, or by plotting the full posterior distributions on nodes. Time-scaled phylogenetic plots can be visualised with absolute and geological timescales . All plotting functions are applicable with output from any Bayesian software, not just 'MCMCtree'.
	"""
	
	cran = "MCMCtreeR" 

	version("1.1", md5="194f6fef6aafde0a51250b25ad189783")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ape@3.0.7:", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
