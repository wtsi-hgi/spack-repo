# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpiilmct(RPackage):
	"""Continuous Time Distance-Based and Network-Based Individual
Level Models for Epidemics

	Provides tools for simulating from continuous-time individual level models of disease transmission, and carrying out infectious disease data analyses with the same models. The epidemic models considered are distance-based and/or contact network-based models within Susceptible-Infectious-Removed (SIR) or Susceptible-Infectious-Notified-Removed (SINR) compartmental frameworks. <doi:10.18637/jss.v098.i10>.
	"""
	
	homepage = "https://github.com/waleedalmutiry/EpiILMCT/"
	cran = "EpiILMCT" 

	version("1.1.7", md5="b13b146d7c1b61dd67fa58b17f190b98")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
