# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLawbl(RPackage):
	"""Latent (Variable) Analysis with Bayesian Learning

	A variety of models to analyze latent variables based on Bayesian learning: the partially CFA (Chen, Guo, Zhang, & Pan, 2020) <DOI: 10.1037/met0000293>; generalized PCFA; partially confirmatory IRM (Chen, 2020) <DOI: 10.1007/s11336-020-09724-3>; Bayesian regularized EFA <DOI: 10.1080/10705511.2020.1854763>; Fully and partially EFA.
	"""
	
	homepage = "https://github.com/Jinsong-Chen/LAWBL"
	cran = "LAWBL" 

	version("1.5.0", md5="c5e3686064618387420190a2f10148a9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
