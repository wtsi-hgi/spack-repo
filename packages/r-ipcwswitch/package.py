# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpcwswitch(RPackage):
	"""Inverse Probability of Censoring Weights to Deal with Treatment
Switch in Randomized Clinical Trials

	Contains functions for formatting clinical trials data and implementing inverse probability of censoring weights to handle treatment switches when estimating causal treatment effect in randomized clinical trials.
	"""
	
	cran = "ipcwswitch" 

	version("1.0.4", md5="6d0b46ae33aee0c23e360d571254ee2a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival@2.42:", type=("build", "run"))
