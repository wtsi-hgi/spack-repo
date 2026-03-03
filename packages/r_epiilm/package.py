# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpiilm(RPackage):
	"""Spatial and Network Based Individual Level Models for Epidemics

	Provides tools for simulating from discrete-time individual level models for infectious disease data analysis. This epidemic model class contains spatial and contact-network based models with two disease types: Susceptible-Infectious (SI) and Susceptible-Infectious-Removed (SIR).
	"""
	
	homepage = "https://github.com/waleedalmutiry/EpiILM"
	cran = "EpiILM" 

	version("1.5.2", md5="a94d6ba4782fb2482cd89568bf0c1511")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r-adaptmcmc", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
