# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVirtualpop(RPackage):
	"""Simulation of Populations by Sampling Waiting-Time Distributions

	Generates lifespans and fertility histories in continuous time using individual-level state transition (multi-state) models and data from the Human Mortality Database and the Human Fertility Database. To facilitate virtual population analysis, data on virtual individuals are stored in a data structure commonly used in sample surveys. Life histories are generated for multiple generations. The genealogies that result facilitate the study of family ties. 
	"""
	
	cran = "VirtualPop" 

	version("1.0.2", md5="9b139fb833bb6817a20f8e894919f8fc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-hmdhfdplus", type=("build", "run"))
