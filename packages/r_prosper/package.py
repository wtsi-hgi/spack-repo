# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProsper(RPackage):
	"""Simulation of Weed Population Dynamics

	An environment to simulate the development of annual plant populations with regard to population dynamics and genetics, especially herbicide resistance. It combines genetics on the individual level (Renton et al. 2011) with a stochastic development on the population level (Daedlow, 2015).
	Renton, M, Diggle, A, Manalil, S and Powles, S (2011) <doi:10.1016/j.jtbi.2011.05.010> 
	Daedlow, Daniel (2015, doctoral dissertation: University of Rostock, Faculty of Agriculture and Environmental Sciences.)
	"""
	
	cran = "PROSPER" 

	version("0.3.3", md5="3c0f3cca2f4ddf05c1c949e03c5dcd96")

	depends_on("r-data-table", type=("build", "run"))
