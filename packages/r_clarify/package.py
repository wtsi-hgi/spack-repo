# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClarify(RPackage):
	"""Simulation-Based Inference for Regression Models

	Performs simulation-based inference as an alternative to the delta method for obtaining valid confidence intervals and p-values for regression post-estimation quantities, such as average marginal effects and predictions at representative values. This framework for simulation-based inference is especially useful when the resulting quantity is not normally distributed and the delta method approximation fails. The methodology is described in King, Tomz, and Wittenberg (2000) <doi:10.2307/2669316>. 'clarify' is meant to replace some of the functionality of the archived package 'Zelig'; see the vignette "Translating Zelig to clarify" for replicating this functionality.
	"""
	
	homepage = "https://github.com/iqss/clarify"
	cran = "clarify" 

	version("0.2.0", md5="d6ecef8c4216d456483b64c5797db15d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-pbapply@1.7.0:", type=("build", "run"))
	depends_on("r-chk@0.9:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-insight@0.19.2:", type=("build", "run"))
	depends_on("r-marginaleffects@0.14:", type=("build", "run"))
	depends_on("r-mvnfast@0.2.6:", type=("build", "run"))
