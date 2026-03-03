# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimalthreshold(RPackage):
	"""Bayesian Methods for Optimal Threshold Estimation

	Functions to estimate the optimal threshold of diagnostic markers or treatment selection markers. The optimal threshold is the marker value that maximizes the utility of the marker based-strategy (for diagnostic or treatment selection) in a given population. The utility function depends on the type of marker (diagnostic or treatment selection), but always takes into account the preferences of the patients or the physician in the decision process. For estimating the optimal threshold, ones must specify the distributions of the marker in different groups (defined according to the type of marker, diagnostic or treatment selection) and provides data to estimate the parameters of these distributions. Ones must also provide some features of the target populations (disease prevalence or treatment efficacies) as well as the preferences of patients or physicians. The functions rely on Bayesian inference which helps producing several indicators derived from the optimal threshold. See Blangero, Y, Rabilloud, M, Ecochard, R, and Subtil, F (2019) <doi:10.1177/0962280218821394> for the original article that describes the estimation method for treatment selection markers and Subtil, F, and Rabilloud, M (2019) <doi:10.1002/bimj.200900242> for diagnostic markers.
	"""
	
	cran = "optimalThreshold" 

	version("1.0", md5="765b77d9511aa1a4b578070e89739750")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-ars", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-hdinterval", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("jags@4:", type=("build", "link", "run"))
