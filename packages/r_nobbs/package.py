# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNobbs(RPackage):
	"""Nowcasting by Bayesian Smoothing

	A Bayesian approach to estimate the number of occurred-but-not-yet-reported cases from incomplete, time-stamped reporting data for disease outbreaks. 'NobBS' learns the reporting delay distribution and the time evolution of the epidemic curve to produce smoothed nowcasts in both stable and time-varying case reporting settings, as described in McGough et al. (2020) <doi:10.1371/journal.pcbi.1007735>.  
	"""
	
	cran = "NobBS" 

	version("1.0.0", md5="7b9168c3e23632c67b69cf3146c763d7")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
