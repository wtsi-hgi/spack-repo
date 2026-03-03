# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmcvis(RPackage):
	"""Tools to Visualize, Manipulate, and Summarize MCMC Output

	Performs key functions for MCMC analysis using minimal code - visualizes, manipulates, and summarizes MCMC output. Functions support simple and straightforward subsetting of model parameters within the calls, and produce presentable and 'publication-ready' output. MCMC output may be derived from Bayesian model output fit with 'Stan', 'NIMBLE', 'JAGS', and other software.
	"""
	
	homepage = "https://github.com/caseyyoungflesh/MCMCvis"
	cran = "MCMCvis" 

	version("0.16.3", md5="d538b05010314d14f5c58855d3e9d559")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-overlapping", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
